"""Minimal "traditional RAG" baseline over the FICTIONAL AQ-200 PDFs.

  python rag.py build                 # extract -> chunk -> embed -> save index
  python rag.py ask "question" [-k 5] # retrieve top-k + answer with citations
  python rag.py eval ../eval/questions.json   # run all eval questions -> ../eval/rag_answers.json

The API key is read from GEMINI_API_KEY (loaded from the repo-root .env). It is never printed.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pypdf import PdfReader
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]                      # repo root (ai_quest)
SOURCES = HERE.parents[1] / "sources"
INDEX = HERE / "index.json"
EMBED_MODEL = "gemini-embedding-2"
GEN_MODEL = "gemini-3.5-flash-lite"
PRICE_IN, PRICE_OUT = 0.30, 2.50            # USD per 1M tokens, gemini-3.5-flash-lite
CHUNK_CHARS, OVERLAP_LINES = 900, 2

load_dotenv(ROOT / ".env")
con = Console(width=110)


def client():
    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("GEMINI_API_KEY not set (expected in .env)")
    return genai.Client()


# ---------------------------------------------------------------- build
def extract_chunks():
    chunks = []
    for pdf in sorted(SOURCES.glob("*.pdf")):
        for pno, page in enumerate(PdfReader(pdf).pages, 1):
            lines = [re.sub(r"\s+", " ", l).strip() for l in page.extract_text().splitlines()]
            lines = [l for l in lines if l and not l.startswith("FICTIONAL SAMPLE")]
            buf = []
            for line in lines:
                if buf and sum(len(x) for x in buf) + len(line) > CHUNK_CHARS:
                    chunks.append({"source": pdf.name, "page": pno, "text": "\n".join(buf)})
                    buf = buf[-OVERLAP_LINES:]          # small line overlap keeps table headers/context
                buf.append(line)
            if buf:
                chunks.append({"source": pdf.name, "page": pno, "text": "\n".join(buf)})
    return chunks


def embed(c, texts, task):
    # NOTE: gemini-embedding-2 is multimodal and merges a list of contents into ONE vector,
    # so we embed each chunk with its own call (17 chunks -> 17 small calls).
    out = []
    for t in texts:
        r = c.models.embed_content(model=EMBED_MODEL, contents=t,
                                   config=types.EmbedContentConfig(task_type=task))
        out.append(r.embeddings[0].values)
    return np.array(out, dtype=np.float32)


def build():
    c = client()
    t0 = time.perf_counter()
    con.rule("[bold cyan]RAG build: PDF -> text -> chunks -> embeddings")
    chunks = extract_chunks()
    t1 = time.perf_counter()
    tbl = Table(title=f"{len(chunks)} chunks from {len(list(SOURCES.glob('*.pdf')))} PDFs")
    for col in ("#", "source", "page", "chars", "preview"):
        tbl.add_column(col)
    for i, ch in enumerate(chunks):
        tbl.add_row(str(i), ch["source"], str(ch["page"]), str(len(ch["text"])), ch["text"][:48].replace("\n", " ") + "...")
    con.print(tbl)
    tok = c.models.count_tokens(model=EMBED_MODEL, contents="\n".join(ch["text"] for ch in chunks)).total_tokens
    vecs = embed(c, [ch["text"] for ch in chunks], "RETRIEVAL_DOCUMENT")
    t2 = time.perf_counter()
    for ch, v in zip(chunks, vecs):
        ch["vec"] = v.tolist()
    INDEX.write_text(json.dumps({"embed_model": EMBED_MODEL, "dim": int(vecs.shape[1]), "embed_tokens": tok,
                                 "chunks": chunks}), encoding="utf-8")
    stats = {"extract_chunk_s": round(t1 - t0, 2), "embed_s": round(t2 - t1, 2), "total_s": round(time.perf_counter() - t0, 2),
             "chunks": len(chunks), "dim": int(vecs.shape[1]), "embed_tokens": tok}
    (HERE / "build_stats.json").write_text(json.dumps(stats, indent=2))
    con.print(Panel(f"extract+chunk: {stats['extract_chunk_s']} s   embed ({EMBED_MODEL}, dim {stats['dim']}): {stats['embed_s']} s\n"
                    f"embedded tokens: {tok:,}   TOTAL build time: [bold green]{stats['total_s']} s[/]   -> {INDEX.name}",
                    title="build done", border_style="green"))


# ---------------------------------------------------------------- query
SYSTEM = """You answer questions about a product using ONLY the numbered context chunks.
Rules:
- Cite the chunks you used like [S1], [S3] right after each fact.
- If the context does not contain the answer, reply exactly: "Not found in the documents." and nothing else.
- For calculations, show the numbers you used. Be concise (max 6 sentences)."""


def load_index():
    if not INDEX.exists():
        sys.exit("index.json missing - run: python rag.py build")
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    M = np.array([ch["vec"] for ch in idx["chunks"]], dtype=np.float32)
    return idx["chunks"], M / np.linalg.norm(M, axis=1, keepdims=True)


def ask(question, k=5, c=None, chunks=None, M=None, show=True):
    c = c or client()
    if chunks is None:
        chunks, M = load_index()
    t0 = time.perf_counter()
    q = embed(c, [question], "RETRIEVAL_QUERY")[0]
    sims = M @ (q / np.linalg.norm(q))
    top = np.argsort(-sims)[:k]
    t1 = time.perf_counter()
    ctx = "\n\n".join(f"[S{r + 1}] ({chunks[i]['source']} p.{chunks[i]['page']})\n{chunks[i]['text']}" for r, i in enumerate(top))
    resp = c.models.generate_content(
        model=GEN_MODEL, contents=f"Context:\n{ctx}\n\nQuestion: {question}",
        config=types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0))
    t2 = time.perf_counter()
    u = resp.usage_metadata
    tin, tout = u.prompt_token_count or 0, (u.candidates_token_count or 0) + (u.thoughts_token_count or 0)
    cost = tin / 1e6 * PRICE_IN + tout / 1e6 * PRICE_OUT
    res = {"question": question, "answer": resp.text.strip(),
           "retrieved": [{"rank": r + 1, "chunk": int(i), "source": chunks[i]["source"], "page": chunks[i]["page"],
                          "score": round(float(sims[i]), 4)} for r, i in enumerate(top)],
           "retrieve_s": round(t1 - t0, 3), "generate_s": round(t2 - t1, 3), "total_s": round(t2 - t0, 3),
           "tokens_in": tin, "tokens_out": tout, "cost_usd": round(cost, 6)}
    if show:
        con.print(Panel(question, title="[bold]Question", border_style="cyan"))
        tb = Table(title=f"Top-{k} retrieved chunks (cosine similarity)")
        for col in ("rank", "score", "source", "page", "chunk preview"):
            tb.add_column(col)
        for r in res["retrieved"]:
            tb.add_row(f"S{r['rank']}", f"{r['score']:.3f}", r["source"], str(r["page"]),
                       chunks[r["chunk"]]["text"][:46].replace("\n", " ") + "...")
        con.print(tb)
        con.print(Panel(res["answer"], title=f"[bold green]Answer ({GEN_MODEL})", border_style="green"))
        con.print(f"[dim]retrieve {res['retrieve_s']} s | generate {res['generate_s']} s | total [bold]{res['total_s']} s[/bold] | "
                  f"tokens in {tin} / out {tout} | cost ${cost:.6f}[/dim]\n")
    return res


def run_eval(path):
    qs = json.loads(Path(path).read_text(encoding="utf-8"))
    c = client()
    chunks, M = load_index()
    out = []
    for q in qs:
        con.rule(f"[bold]{q['id']} - {q['type']}")
        r = ask(q["question"], c=c, chunks=chunks, M=M)
        r["id"] = q["id"]
        out.append(r)
    dest = Path(path).parent / "rag_answers.json"
    dest.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    lat = sorted(r["total_s"] for r in out)
    con.print(Panel(f"{len(out)} questions | median latency {lat[len(lat) // 2]:.2f} s | max {lat[-1]:.2f} s | "
                    f"tokens in {sum(r['tokens_in'] for r in out):,} / out {sum(r['tokens_out'] for r in out):,} | "
                    f"total cost ${sum(r['cost_usd'] for r in out):.5f}\nsaved -> {dest}", title="eval done", border_style="magenta"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    a = sub.add_parser("ask"); a.add_argument("question"); a.add_argument("-k", type=int, default=5)
    e = sub.add_parser("eval"); e.add_argument("path")
    args = ap.parse_args()
    if args.cmd == "build":
        build()
    elif args.cmd == "ask":
        ask(args.question, k=args.k)
    else:
        run_eval(args.path)
