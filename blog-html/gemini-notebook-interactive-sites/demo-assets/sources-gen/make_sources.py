"""Generate the FICTIONAL AeroPure AQ-200 manual set (Markdown + PDF) into ../../sources/.

Usage:  python make_sources.py
"""
from pathlib import Path
from fpdf import FPDF
from fpdf.fonts import FontFace
import product_data as D

OUT = Path(__file__).resolve().parents[2] / "sources"
OUT.mkdir(exist_ok=True)
FONT_DIR = Path("C:/Windows/Fonts")


class Doc:
    """Builds the same content as Markdown and as PDF."""

    def __init__(self, title, doc_no):
        self.title, self.doc_no = title, doc_no
        self.md = [f"# {title}", "", f"> **{D.DISCLAIMER}**", "",
                   f"Document {doc_no} - {D.COMPANY} - Revision 1.0 (Nov 2026)", ""]
        pdf = FPDF(format="A4")
        pdf.add_font("Arial", "", str(FONT_DIR / "arial.ttf"))
        pdf.add_font("Arial", "B", str(FONT_DIR / "arialbd.ttf"))
        pdf.add_font("Arial", "I", str(FONT_DIR / "ariali.ttf"))
        pdf.set_auto_page_break(True, 18)
        pdf.set_margins(16, 18, 16)
        doc = self

        def header():
            pdf.set_font("Arial", "B", 8)
            pdf.set_text_color(200, 40, 40)
            pdf.cell(0, 5, D.DISCLAIMER, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(2)

        def footer():
            pdf.set_y(-12)
            pdf.set_font("Arial", "I", 8)
            pdf.set_text_color(120, 120, 120)
            pdf.cell(0, 5, f"{doc.title} | {doc.doc_no} | page {pdf.page_no()}", align="C")
            pdf.set_text_color(0, 0, 0)

        pdf.header, pdf.footer = header, footer
        pdf.add_page()
        pdf.set_font("Arial", "B", 18)
        pdf.multi_cell(0, 9, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Arial", "", 9)
        pdf.cell(0, 6, f"Document {doc_no} - {D.COMPANY} - Revision 1.0 (Nov 2026)", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)
        self.pdf = pdf

    def h2(self, text):
        self.md += [f"## {text}", ""]
        self.pdf.ln(3)
        self.pdf.set_font("Arial", "B", 13)
        self.pdf.set_text_color(13, 71, 161)
        self.pdf.multi_cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.ln(1)

    def p(self, text):
        self.md += [text, ""]
        self.pdf.set_font("Arial", "", 10)
        self.pdf.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
        self.pdf.ln(1.5)

    def ol(self, items):
        for i, t in enumerate(items, 1):
            self.md.append(f"{i}. {t}")
            self.pdf.set_font("Arial", "", 10)
            self.pdf.multi_cell(0, 5.5, f"{i}. {t}", new_x="LMARGIN", new_y="NEXT")
        self.md.append("")
        self.pdf.ln(1.5)

    def table(self, headers, rows, widths=None, font=8.5):
        rows = [[str(c) for c in r] for r in rows]
        self.md.append("| " + " | ".join(headers) + " |")
        self.md.append("|" + "---|" * len(headers))
        for r in rows:
            self.md.append("| " + " | ".join(r) + " |")
        self.md.append("")
        self.pdf.set_font("Arial", "", font)
        with self.pdf.table(col_widths=widths, text_align="LEFT", line_height=4.6,
                            headings_style=FontFace(emphasis="BOLD", fill_color=(220, 230, 245))) as t:
            for row in [headers] + rows:
                rr = t.row()
                for c in row:
                    rr.cell(c)
        self.pdf.ln(3)

    def save(self, stem):
        (OUT / f"{stem}.md").write_text("\n".join(self.md), encoding="utf-8")
        self.pdf.output(str(OUT / f"{stem}.pdf"))
        print("wrote", stem + ".pdf / .md")


# ---------- 1. User manual ----------
d = Doc("AeroPure AQ-200 Series Air Purifier - User Manual", "AQ200-UM-01")
d.p("This manual covers three models: AQ-200 Lite, AQ-200 (standard) and AQ-200 Pro. "
    "Read the safety notes before first use. All names, numbers and prices in this document are fictional.")
d.h2("1. Model comparison and specifications")
d.table(["Specification"] + D.MODELS, D.SPECS, widths=(34, 22, 22, 22))
d.h2("2. Safety notes")
d.p("- Do not use the purifier in bathrooms or where relative humidity exceeds 80%.\n"
    "- Keep at least 30 cm clearance on all sides and 1 m from heaters.\n"
    "- Unplug before opening any cover. The UV-C lamp (Pro) switches off automatically when the front cover opens.")
d.h2("3. Setup (first use)")
d.ol(D.SETUP_STEPS)
d.h2("4. Control panel")
d.table(["Button", "Short press", "Long press"], [
    ("Power", "-", "3 s: on/off"),
    ("Mode", "Cycle Auto > Sleep > Manual", "Power + Mode 10 s: firmware recovery"),
    ("Fan", "Speed 1 > 2 > 3 > 4 (Turbo)", "-"),
    ("Timer", "1 h > 2 h > 4 h > 8 h > off", "Wi-Fi + Timer 5 s: start app pairing"),
    ("Lock", "-", "3 s: child lock on/off"),
    ("Filter Reset", "-", "3 s: reset filter life counter"),
    ("Wi-Fi (AQ-200, Pro)", "Show Wi-Fi status", "5 s: reset network settings"),
], widths=(25, 35, 40))
d.h2("5. Maintenance schedule")
d.table(["Component", "Interval", "Action", "Models"], D.MAINTENANCE, widths=(28, 30, 47, 13))
d.h2("6. Frequently asked questions")
for q, a in D.FAQ:
    d.p(f"Q: {q}\nA: {a}")
d.save("AQ-200_User_Manual")

# ---------- 2. Troubleshooting ----------
d = Doc("AeroPure AQ-200 Series - Troubleshooting & Error Codes", "AQ200-TS-02")
d.p("The display shows an error code (E01-E15) when the unit detects a problem. "
    "Find the code below, follow the fix, then restart the unit. If a code keeps returning after the fix, contact an authorized service center. "
    "Column 'Models' shows which models can display the code.")
d.h2("Error code table")
d.table(["Code", "Meaning", "Likely cause", "Fix", "Models"], D.ERROR_CODES, widths=(9, 20, 30, 45, 13), font=8)
d.h2("Symptoms without an error code")
d.table(["Symptom", "What to check"], [
    ("Unusual smell after replacing filter", "Normal for 1-2 days (new carbon layer). If it persists, check that the plastic bag was removed."),
    ("Unit is loud on Auto mode", "Air quality is poor so fan runs faster; or pre-filter is clogged. Clean the pre-filter."),
    ("Air-quality ring always blue (good) even when cooking", "Sensor lens may be dirty or covered; clean it."),
    ("App shows device offline", "Router changed or 5 GHz only; see error E11 procedure."),
], widths=(40, 60))
d.save("AQ-200_Troubleshooting_Error_Codes")

# ---------- 3. Parts & service price list ----------
d = Doc("AeroPure AQ-200 Series - Spare Parts & Service Price List 2026", "AQ200-PL-03")
d.p("Recommended retail prices in USD, valid 1 Jan - 31 Dec 2026, excluding tax and shipping. Fictional prices for demo only.")
d.h2("Spare parts")
d.table(["Part no.", "Description", "Compatible models", "Price (USD)"], [(a, b, c, f"${p}") for a, b, c, p in D.PARTS], widths=(18, 42, 28, 14))
d.h2("Service fees")
d.table(["Service", "Fee (USD)"], [(a, f"${p}") for a, p in D.SERVICE_FEES], widths=(70, 30))
d.p("Consumables (main filters, pre-filters, UV-C lamps) are not covered by the warranty. "
    "Parts replaced under warranty are free of charge, including labor.")
d.save("AQ-200_Parts_Price_List")

# ---------- 4. Sales & support report ----------
d = Doc("AeroPure AQ-200 Series - Monthly Sales & Support Report (Jan-Oct 2026)", "AQ200-RP-04")
d.p("Fictional monthly figures for a demo dashboard. Units = units sold to end customers. "
    "Support tickets are grouped by category. Resolution time is the average hours from ticket open to close. "
    "CSAT is the average customer satisfaction score on a 1-5 scale.")
d.h2("Table A - Units sold by model")
d.table(["Month"] + D.MODELS, [[m] + [D.UNITS[k][i] for k in D.MODELS] for i, m in enumerate(D.MONTHS)], widths=(25, 25, 25, 25), font=9)
d.h2("Table B - Support tickets by category")
d.table(["Month"] + D.TICKET_CATS + ["Avg resolution (h)", "CSAT (1-5)"],
        [[m] + D.TICKETS[i] + [D.RESOLUTION_H[i], D.CSAT[i]] for i, m in enumerate(D.MONTHS)],
        widths=(18, 11, 11, 13, 11, 11, 15, 12), font=8.5)
d.h2("Notes")
for n in D.REPORT_NOTES:
    d.p("- " + n)
d.save("AQ-200_Sales_Support_Report_2026")
