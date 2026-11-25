"""Ghép blog EN/VI cho bài Google Workspace CLI + MCP.

  python build_blog.py            -> google-workspace-cli-mcp-blog-en.html + google-workspace-cli-mcp-blog.html
  python build_blog.py --spec-only -> chỉ tạo parts/en_spec.html từ draft-spec-en.html (đã sửa Model Armor)
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
POST = HERE.parent
PARTS = HERE / "parts"
REF_POST = POST.parent / "gemini-decisions-api-classification" / "gemini-decisions-api-classification-blog-en.html"

MODEL_ARMOR_EN = (
    "<p>The security guide configures Model Armor for MCP as a <strong>floor setting</strong> on the Google Cloud project, "
    "using gcloud or the console. In plain words, you turn on floor-setting enforcement, add Google MCP servers "
    "(integrated service GOOGLE_MCP_SERVER) to the services it protects, choose the enforcement type (INSPECT_AND_BLOCK "
    "to block flagged traffic, or inspect only), and optionally enable Cloud Logging for MCP traffic plus filters such as "
    "malicious URL detection and responsible-AI categories with a confidence threshold. I deliberately do not reproduce "
    "the command here: the flags of this preview feature are still changing, so copy the current version from the "
    "official security page rather than from a blog post.</p>"
)

REFS = [
    ("Google Workspace CLI guide", "https://developers.google.com/workspace/guides/workspace-cli"),
    ("Google Workspace CLI release notes", "https://developers.google.com/workspace/cli/release-notes"),
    ("Configure Google Workspace MCP servers", "https://developers.google.com/workspace/guides/configure-mcp-servers"),
    ("Configure security for Google Workspace MCP servers (Model Armor)", "https://developers.google.com/workspace/guides/configure-mcp-security"),
    ("Universal Search MCP", "https://developers.google.com/workspace/guides/universal-search-mcp"),
    ("Gmail MCP reference", "https://developers.google.com/workspace/gmail/api/reference/mcp"),
    ("Drive MCP reference", "https://developers.google.com/workspace/drive/api/reference/mcp"),
    ("Docs MCP reference", "https://developers.google.com/workspace/docs/api/reference/mcp"),
    ("Sheets MCP reference", "https://developers.google.com/workspace/sheets/api/reference/mcp"),
    ("Slides MCP reference", "https://developers.google.com/workspace/slides/api/reference/mcp"),
    ("Calendar MCP reference", "https://developers.google.com/workspace/calendar/api/v3/reference/mcp"),
    ("Chat MCP reference", "https://developers.google.com/workspace/chat/api/reference/mcp"),
    ("People MCP reference", "https://developers.google.com/people/api/mcp"),
    ("Google Cloud blog: Built for trust and control: Powering the next wave of AI agents across Google Workspace and Google Cloud (November 25, 2026)",
     "https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise"),
    ("Claude Code documentation: connecting MCP servers", "https://code.claude.com/docs/en/mcp"),
]

LANG = {
    "en": dict(html_lang="en", title="Google Workspace CLI and MCP Servers Hands-on",
               s1="1. Requirement 1: Official release specifications and key features of Google Workspace CLI, MCP servers and enterprise agent security",
               refs="References", footer="AI Quest &mdash; Investigate How &bull; Google Workspace CLI + MCP servers &bull; 2026",
               out="google-workspace-cli-mcp-blog-en.html"),
    "vi": dict(html_lang="vi", title="Google Workspace CLI và MCP Servers thực hành",
               s1="1. Yêu cầu 1: Thông số phát hành chính thức và tính năng chính của Google Workspace CLI, MCP servers và bảo mật agent cho doanh nghiệp",
               refs="Tài liệu tham khảo", footer="AI Quest &mdash; Investigate How &bull; Google Workspace CLI + MCP servers &bull; 2026",
               out="google-workspace-cli-mcp-blog.html"),
}

EXTRA_CSS = """
  .todo { background: #fff3e0; border: 2px dashed #ff9800; border-radius: 8px; padding: 12px 16px; color: #e65100; }
  table.data-table td { vertical-align: top; }
  .container pre { overflow-x: auto; }
  @media (max-width: 700px) { table.data-table { display: block; overflow-x: auto; } .hero h1 { font-size: 1.6em; } }
"""


def make_spec_en():
    s = (POST / "draft-spec-en.html").read_text(encoding="utf-8")
    # 1) Model Armor: bỏ lệnh gcloud có flag đoán, thay bằng mô tả
    s, n = re.subn(r"<p>The Model Armor floor setting from the security guide looks like this.*?</pre>", MODEL_ARMOR_EN, s, flags=re.S)
    assert n == 1, "Model Armor block not found"
    # 2) bỏ References của draft (đưa xuống cuối bài)
    s = s[: s.index("<h2>References</h2>")]
    # 3) hạ cấp heading và đánh số lại dưới mục 1
    s = re.sub(r"<h3>(\d+\.\d+) ", lambda m: f"<h4>1.{m.group(1)} ", s).replace("</h3>", "</h4>")
    s = re.sub(r"<h2>(\d+)\. ", lambda m: f"<h3>1.{m.group(1)} ", s).replace("</h2>", "</h3>")
    s = s.replace("<table>", '<table class="data-table">')
    (PARTS / "en_spec.html").write_text(s.strip() + "\n", encoding="utf-8")
    return s


def head_css():
    ref = REF_POST.read_text(encoding="utf-8")
    css = ref[ref.index("<style>"): ref.index("</style>")]
    return css + EXTRA_CSS + "</style>"


def build(lang):
    L = LANG[lang]
    pre = "en" if lang == "en" else "vi"
    spec = (PARTS / f"{pre}_spec.html").read_text(encoding="utf-8")
    head = (PARTS / f"{pre}_head.html").read_text(encoding="utf-8")
    tail = (PARTS / f"{pre}_tail.html").read_text(encoding="utf-8")
    refs = "\n".join(f'    <li><a href="{u}" target="_blank">{t}</a></li>' for t, u in REFS)
    doc = f"""<!DOCTYPE html>
<html lang="{L['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{L['title']}</title>
{head_css()}
</head>
<body>
{head}
<section id="s1">
  <h2>{L['s1']}</h2>
{spec}
</section>

{tail}
<section id="refs">
  <h2>{L['refs']}</h2>
  <ul>
{refs}
  </ul>
</section>

</div>
<div class="footer">{L['footer']}</div>

</body>
</html>
"""
    out = POST / L["out"]
    out.write_text(doc, encoding="utf-8")
    print("->", out)


if __name__ == "__main__":
    make_spec_en()
    if "--spec-only" in sys.argv:
        sys.exit()
    for lg in ("en", "vi"):
        if (PARTS / f"{'en' if lg == 'en' else 'vi'}_tail.html").exists() and (PARTS / f"{lg}_spec.html").exists():
            build(lg)
