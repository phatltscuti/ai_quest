"""Build 3 custom diagrams as HTML/CSS (+inline SVG arrows) in VI and EN, then render to PNG
with Playwright (real Chrome). Output: ../images/diagram-*.png and diagrams/*.html"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "diagrams"); os.makedirs(OUT_HTML, exist_ok=True)
IMG = os.path.join(HERE, "..", "images")

CSS = """
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',Arial,sans-serif;background:#fff;color:#202124}
.canvas{width:1600px;padding:36px 44px;background:linear-gradient(135deg,#f8fbff 0%,#ffffff 60%)}
h1{margin:0 0 4px;font-size:34px;color:#1a73e8}.sub{color:#5f6368;font-size:18px;margin-bottom:26px}
.foot{margin-top:22px;font-size:14px;color:#80868b}
"""

def page(title, body, extra_css=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}{extra_css}</style></head><body>{body}</body></html>"

# ---------------- 1. ROADMAP ----------------
ROAD_CSS = """
.road{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:18px}
.lane{position:absolute;left:0;right:0;top:58px;height:10px;background:linear-gradient(90deg,#9aa0a6,#1a73e8,#34a853,#fbbc04,#ea4335);border-radius:6px;z-index:0}
.ph{position:relative;z-index:1}
.dot{width:46px;height:46px;border-radius:50%;margin:40px auto 18px;color:#fff;font-weight:700;font-size:20px;display:flex;align-items:center;justify-content:center;border:4px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.25)}
.card{border:2px solid #dadce0;border-radius:14px;background:#fff;padding:16px 16px 12px;min-height:370px;box-shadow:0 2px 8px rgba(0,0,0,.06);display:flex;flex-direction:column}
.card h3{margin:0 0 2px;font-size:21px}.when{font-size:14px;color:#5f6368;margin-bottom:10px;font-weight:600}
.card ul{margin:0;padding-left:18px;font-size:15.5px;line-height:1.5;flex:1}.card li{margin-bottom:6px}
.gate{margin-top:12px;border-top:1px dashed #bbb;padding-top:8px;font-size:14px;color:#3c4043}
.gate b{color:#137333}.src{display:inline-block;font-size:12px;padding:1px 8px;border-radius:10px;margin:0 4px 8px 0;font-weight:600}
.s-l{background:#fce8e6;color:#c5221f}.s-s{background:#e6f4ea;color:#137333}
"""
ROAD = {
 "vi": dict(title="Lộ trình triển khai AI toàn công ty (tổng hợp từ 2 slide deck)",
   sub="Không phải “phát tool cho tất cả” mà là: xác định đích → thử sâu ở 1 bộ phận → nối với kết quả kinh doanh → dựng guardrail & golden path → nhân rộng bằng mô hình vận hành",
   ph=[("0","#9aa0a6","Định hướng & khảo sát","Tháng 0–1",["Định nghĩa “trạng thái muốn đạt” bằng kết quả kinh doanh, không phải số user","Kiểm kê tool, chi phí, sáng kiến đang rải rác","Phỏng vấn trong và ngoài công ty"],"Có mục tiêu trung hạn + danh sách vấn đề thật",["SmartHR"]),
       ("1","#1a73e8","Pilot hẹp & sâu","Tháng 1–3",["Chọn 1 bộ phận làm “khách hàng đầu tiên”","Trưởng bộ phận cam kết mục tiêu (return + request)","AX promoter đồng hành ~2 tháng (66 ngày để hình thành thói quen)"],"Thành viên dùng AI hằng ngày trong công việc thật",["LMI"]),
       ("2","#34a853","Nối với kết quả","Tháng 2–4",["Vẽ outcome map: dùng AI → chỉ số dẫn → chỉ số trễ → tác động","Quyết định thời gian tiết kiệm được dùng vào việc gì","Đo 5 tầng: chi phí → sử dụng → sáng kiến → tổ chức → kinh doanh"],"Trưởng bộ phận xem số liệu định kỳ",["LMI","SmartHR"]),
       ("3","#f29900","Guardrail & Golden path","Tháng 3–5",["Phân quyền tool theo cấp độ: no-code → low-code → pro-code","Đội rủi ro liên phòng ban nhận báo cáo, cập nhật luật","Quy trình chuẩn cho tool nội bộ: CPF → PSF → PMF → GTM"],"Tool tự làm phải qua review bảo mật & chi phí",["LMI","SmartHR"]),
       ("4","#ea4335","Nhân rộng & vận hành","Tháng 5–6+",["Lãnh đạo là owner; AI Ops là enabler, không phải gatekeeper","WG Governance + WG Promotion + AI Lead từng bộ phận","Báo cáo tháng lên ban điều hành, chia sẻ tri thức"],"Mỗi bộ phận mới đạt lại cùng điều kiện PMF",["SmartHR","LMI"])],
   gate="Điều kiện qua cổng", foot="Nguồn: Link and Motivation (PEK2026, 25/09/2026) & SmartHR (28/09/2026) trên Speaker Deck — tổng hợp & diễn giải bởi tác giả. Mốc tháng là đề xuất của tác giả, không có trong slide."),
 "en": dict(title="Company-wide AI adoption roadmap (synthesized from both decks)",
   sub="Not “hand tools to everyone” but: define the destination → go deep in one department → link to business outcomes → build guardrails & a golden path → scale with an operating model",
   ph=[("0","#9aa0a6","Aspire & Assess","Month 0–1",["Define the target state as business outcomes, not user counts","Inventory scattered tools, costs and initiatives","Interview people inside and outside"],"Mid-term goal + list of real problems",["SmartHR"]),
       ("1","#1a73e8","Narrow & deep pilot","Month 1–3",["Pick one department as the “first customer”","Department head commits to a target (return + request)","AX promoter coaches ~2 months (66 days to form a habit)"],"Members use AI daily in real work",["LMI"]),
       ("2","#34a853","Link to outcomes","Month 2–4",["Draw an outcome map: AI use → leading → lagging → impact","Decide what the saved time is spent on","Measure 5 layers: cost → usage → initiatives → org → business"],"Department head reviews the numbers regularly",["LMI","SmartHR"]),
       ("3","#f29900","Guardrails & Golden path","Month 3–5",["Tier tool access: no-code → low-code → pro-code","Cross-functional risk team takes reports, updates rules","Standard path for internal tools: CPF → PSF → PMF → GTM"],"Self-built tools pass security & cost review",["LMI","SmartHR"]),
       ("4","#ea4335","Scale & operate","Month 5–6+",["Executives own it; AI Ops is an enabler, not a gatekeeper","Governance WG + Promotion WG + AI Lead per unit","Monthly report to management, knowledge sharing"],"Each new unit re-passes the same PMF criteria",["SmartHR","LMI"])],
   gate="Exit gate", foot="Sources: Link and Motivation (PEK2026, 2026-09-25) & SmartHR (2026-09-28) on Speaker Deck — synthesized and interpreted by the author. Month ranges are the author's proposal, not from the slides."),
}
def roadmap(lang):
    d = ROAD[lang]; cards = ""
    for num, col, name, when, items, gate, srcs in d["ph"]:
        tags = "".join(f"<span class='src {'s-l' if s=='LMI' else 's-s'}'>{s}</span>" for s in srcs)
        lis = "".join(f"<li>{i}</li>" for i in items)
        cards += (f"<div class='ph'><div class='dot' style='background:{col}'>{num}</div>"
                  f"<div class='card' style='border-top:6px solid {col}'><h3 style='color:{col}'>{name}</h3>"
                  f"<div class='when'>{when}</div><div>{tags}</div><ul>{lis}</ul>"
                  f"<div class='gate'><b>&#10004; {d['gate']}:</b> {gate}</div></div></div>")
    body = (f"<div class='canvas' id='cv'><h1>{d['title']}</h1><div class='sub'>{d['sub']}</div>"
            f"<div class='road'><div class='lane'></div>{cards}</div><div class='foot'>{d['foot']}</div></div>")
    return page(d["title"], body, ROAD_CSS)

# ---------------- 2. ORG STRUCTURE ----------------
ORG_CSS = """
.org{position:relative;height:660px}
.box{position:absolute;border-radius:14px;padding:12px 16px;border:2px solid;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.07)}
.box h3{margin:0 0 4px;font-size:20px}.box p{margin:0;font-size:15px;line-height:1.45;color:#3c4043}
.exec{left:560px;top:0;width:480px;border-color:#202124;background:#f1f3f4}
.ops{left:560px;top:150px;width:480px;border-color:#1a73e8;background:#e8f0fe}
.gov{left:30px;top:150px;width:400px;border-color:#ea4335;background:#fce8e6}
.sec{left:1170px;top:150px;width:380px;border-color:#9334e6;background:#f3e8fd}
.unit{top:400px;width:350px;border-color:#34a853;background:#e6f4ea;min-height:130px}
.u1{left:40px}.u2{left:420px}.u3{left:800px}.u4{left:1180px;width:370px;border-style:dashed;background:#fff}
.mem{position:absolute;left:40px;top:580px;width:1510px;border:2px dashed #9aa0a6;border-radius:14px;padding:12px 16px;font-size:16px;color:#3c4043;background:#fafafa}
svg{position:absolute;left:0;top:0}
.lbl{font-size:14px;fill:#5f6368;font-family:'Segoe UI',Arial}
"""
ORG = {
 "vi": dict(title="Cơ cấu tổ chức cần có để đẩy AI toàn công ty",
   sub="Kết hợp “AX推進体制” của LMI và mô hình PO/PM/WG/AI Lead của SmartHR — điểm chung: lãnh đạo sở hữu, đội trung tâm làm enabler, người thúc đẩy nằm ngay trong bộ phận",
   exec=("Ban điều hành = Product Owner","Coi AI là chương trình nghị sự của ban lãnh đạo; nhận báo cáo tháng; quyết định đầu tư hay cắt lỗ"),
   ops=("Đội AI Ops / Platform (enabler)","Chiến lược & đo giá trị • hạ tầng tool chung • đồng hành hiện trường • đào tạo theo vai trò. Có thể bắt đầu rất nhỏ (SmartHR: 1 trưởng phòng kiêm nhiệm)"),
   gov=("WG Governance (bảo mật, pháp chế, IT)","Luật & tiêu chuẩn guardrail • duyệt đơn xin dùng tool • phân cấp quyền theo năng lực đã chứng minh"),
   sec=("Đội ứng phó rủi ro AI","Nhận báo cáo tool chưa duyệt, link public, hành vi lạ trong log → cập nhật luật"),
   units=[("Bộ phận A (pilot)","Trưởng bộ phận cam kết mục tiêu • AX promoter / AI Lead đồng hành ~2 tháng"),("Bộ phận B","AI Lead: cửa sổ đầu tiên cho câu hỏi, đơn xin, use case, phản hồi hiện trường"),("Bộ phận C","AI Lead chọn theo tính cách: muốn giúp người khác, thích thử, hay lan toả"),("Bộ phận tiếp theo…","Chỉ mở rộng khi đạt điều kiện GTM")],
   mem="Thành viên hiện trường: dùng AI mỗi ngày trong công việc thật → cải tiến → báo cáo kết quả (Slack / form) → tri thức được chia sẻ ngang",
   l1="báo cáo tháng", l2="hỗ trợ, đồng hành", l3="báo rủi ro", l4="guardrail",
   foot="Nguồn: LMI slide 14, 16, 32 • SmartHR slide 12, 13 — vẽ lại & diễn giải bởi tác giả."),
 "en": dict(title="The organization you need for company-wide AI adoption",
   sub="Combines LMI's “AX promotion structure” with SmartHR's PO/PM/WG/AI Lead model — common thread: executives own it, a central team enables, champions sit inside each unit",
   exec=("Executives = Product Owner","AI is a management agenda item; receive monthly reports; decide whether to invest or cut"),
   ops=("AI Ops / Platform team (enabler)","Strategy & value measurement • shared tool platform • field coaching • role-based learning. Can start tiny (SmartHR: 1 part-time head)"),
   gov=("Governance WG (security, legal, IT)","Rules & guardrail criteria • review tool requests • tier permissions by proven skill"),
   sec=("AI risk response team","Collects reports of unapproved tools, public links, odd log behaviour → updates rules"),
   units=[("Unit A (pilot)","Head commits to a target • AX promoter / AI Lead coaches ~2 months"),("Unit B","AI Lead: first contact for questions, requests, use cases, field feedback"),("Unit C","AI Leads chosen by traits: want to help, enjoy trial-and-error, spread wins"),("Next units…","Expand only after meeting GTM criteria")],
   mem="Field members: use AI daily in real work → improve → report results (Slack / form) → knowledge spreads sideways",
   l1="monthly report", l2="support, coaching", l3="risk reports", l4="guardrails",
   foot="Sources: LMI slides 14, 16, 32 • SmartHR slides 12, 13 — redrawn and interpreted by the author."),
}
def org(lang):
    d = ORG[lang]
    def bx(cls, t): return f"<div class='box {cls}'><h3>{t[0]}</h3><p>{t[1]}</p></div>"
    units = "".join(bx(f"unit u{i+1}", u) for i, u in enumerate(d["units"]))
    svg = f"""<svg width="1600" height="660"><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5f6368"/></marker></defs>
    <g stroke="#5f6368" stroke-width="2.5" fill="none">
    <path d="M800,150 L800,116" marker-end="url(#a)"/>
    <path d="M560,225 L430,225" stroke-dasharray="5 4"/><path d="M1040,225 L1170,225" stroke-dasharray="5 4"/>
    <path d="M800,280 L800,355 L215,355 L215,394" marker-end="url(#a)"/><path d="M595,355 L595,394" marker-end="url(#a)"/>
    <path d="M975,355 L975,394" marker-end="url(#a)"/><path d="M975,355 L1365,355 L1365,394" marker-end="url(#a)" stroke-dasharray="6 5"/>
    </g>
    <text class="lbl" x="812" y="138">{d['l1']}</text><text class="lbl" x="440" y="214">{d['l4']}</text>
    <text class="lbl" x="1050" y="214">{d['l3']}</text><text class="lbl" x="812" y="346">{d['l2']}</text></svg>"""
    body = (f"<div class='canvas' id='cv'><h1>{d['title']}</h1><div class='sub'>{d['sub']}</div>"
            f"<div class='org'>{svg}{bx('exec',d['exec'])}{bx('ops',d['ops'])}{bx('gov',d['gov'])}{bx('sec',d['sec'])}{units}"
            f"<div class='mem'>{d['mem']}</div></div><div class='foot'>{d['foot']}</div></div>")
    return page(d["title"], body, ORG_CSS)

# ---------------- 3. BOTTLENECK -> SOLUTION ----------------
BN_CSS = """
.flow{display:flex;align-items:stretch;margin-bottom:18px}
.stage{flex:1;border-radius:12px;color:#fff;font-weight:700;font-size:17px;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;min-height:60px}
.arrow{flex:0 0 30px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#9aa0a6}
.row{display:grid;grid-template-columns:280px 1fr 1fr;gap:12px;margin-bottom:12px}
.wall{border-radius:12px;padding:12px 14px;color:#fff}.wall h3{margin:0;font-size:19px}.wall p{margin:4px 0 0;font-size:14px;opacity:.95}
.cell{border:2px solid #dadce0;border-radius:12px;padding:10px 14px;background:#fff;font-size:15.5px;line-height:1.5}
.cell b{color:#202124}.hd{font-weight:700;color:#5f6368;font-size:15px;padding:0 4px}
"""
BN = {
 "vi": dict(title="Bản đồ nút thắt → cách gỡ",
   sub="Gộp “2 bức tường” của LMI và “3 bức tường” của SmartHR thành 5 điểm tắc trên đường từ “phát tool” đến “kết quả kinh doanh”",
   stages=["Phát tool","Dùng hằng ngày","Tạo ra thứ chạy được","Dùng được trong thực tế","Tổ chức duy trì","Kết quả kinh doanh"],
   hd=["Bức tường","Triệu chứng / nguyên nhân","Cách gỡ (từ 2 deck)"],
   rows=[("#1a73e8","① Tường định hình thói quen","LMI: 定着の壁",["~70% không dùng mỗi ngày dù đã được phát ChatGPT + học lý thuyết","Không nghĩ ra việc để dùng (57%), không biết cách ra lệnh (26%)"],["Hẹp & sâu: làm 1 bộ phận trước","AX promoter trong bộ phận + đồng hành ~2 tháng, chốt thời điểm dùng mỗi ngày"]),
         ("#34a853","② Tường kết quả","LMI: 成果の壁",["Hiệu suất tăng nhưng năng suất đi ngang (“giờ được ăn trưa thong thả hơn”)","Không ai quyết thời gian dư dùng vào đâu, không ai kiểm tra"],["Outcome map nối dùng AI → chỉ số dẫn → chỉ số trễ","Trưởng bộ phận cùng xem số liệu định kỳ"]),
         ("#f29900","③ Tường tạo ra","SmartHR: つくる壁",["Dùng AI ≠ làm ra thứ chạy được","Không có môi trường thử nhỏ một cách an toàn"],["Chia sẻ case, phân rã nghiệp vụ, môi trường thử","Cấp tool theo level (no-code → low-code → pro-code)"]),
         ("#ea4335","④ Tường triển khai","SmartHR: 実装の壁 + LMI: 野良ツール",["Chạy được ≠ dùng được thực tế; tool “hoang” và tool không ai dùng","Tiêu chí ngầm, chưa nối với hệ thống trước/sau"],["Golden path CPF→PSF→PMF→GTM có điều kiện hoàn thành","Review bảo mật & chi phí trước khi giao cho người dùng"]),
         ("#9334e6","⑤ Tường tổ chức hoá","SmartHR: 組織化の壁",["1 người dùng được ≠ tổ chức dùng bền vững","Tri thức đóng trong cá nhân, không owner, không chỉ số"],["Chuẩn hoá, gán owner, thiết kế vận hành, đo hiệu quả","Lãnh đạo sở hữu, WG + AI Lead, báo cáo tháng"])],
   foot="Nguồn: LMI slide 9–22, 24, 34 • SmartHR slide 8, 18 — gộp & diễn giải bởi tác giả."),
 "en": dict(title="Bottleneck → remedy map",
   sub="Merging LMI's “2 walls” and SmartHR's “3 walls” into 5 blockages on the road from “tools handed out” to “business results”",
   stages=["Tools handed out","Daily use","Something that works","Usable in real work","Sustained by the org","Business results"],
   hd=["Wall","Symptom / root cause","Remedy (from the decks)"],
   rows=[("#1a73e8","① Adoption wall","LMI: 定着の壁",["~70% didn't use it daily despite ChatGPT + lectures","Can't think of a use case (57%), don't know how to prompt (26%)"],["Narrow & deep: one department first","AX promoter inside the unit + ~2-month coaching, fixed daily moments of use"]),
         ("#34a853","② Outcome wall","LMI: 成果の壁",["Efficiency up, productivity flat (“I can eat lunch slowly now”)","Nobody decided where saved time goes, nobody checked"],["Outcome map: AI use → leading → lagging indicators","Department head reviews the numbers regularly"]),
         ("#f29900","③ Build wall","SmartHR: つくる壁",["Using AI ≠ building something that works","No safe place to try small"],["Case sharing, task decomposition, sandbox","Tiered tools (no-code → low-code → pro-code)"]),
         ("#ea4335","④ Implementation wall","SmartHR: 実装の壁 + LMI: rogue tools",["Works ≠ usable in real work; rogue and unused tools pile up","Implicit criteria, not connected to upstream/downstream systems"],["Golden path CPF→PSF→PMF→GTM with exit criteria","Security & cost review before handing to users"]),
         ("#9334e6","⑤ Institutionalization wall","SmartHR: 組織化の壁",["One person can use it ≠ the org keeps using it","Knowledge stuck in individuals, no owner, no metrics"],["Standardize, assign owners, design operations, measure","Executive ownership, WGs + AI Leads, monthly report"])],
   foot="Sources: LMI slides 9–22, 24, 34 • SmartHR slides 8, 18 — merged and interpreted by the author."),
}
def bottleneck(lang):
    d = BN[lang]; cols = ["#9aa0a6","#1a73e8","#f29900","#ea4335","#9334e6","#137333"]
    flow = "<div class='arrow'>&rsaquo;</div>".join(f"<div class='stage' style='background:{c}'>{s}</div>" for s, c in zip(d["stages"], cols))
    rows = f"<div class='row'><div class='hd'>{d['hd'][0]}</div><div class='hd'>{d['hd'][1]}</div><div class='hd'>{d['hd'][2]}</div></div>"
    for col, name, src, sym, fix in d["rows"]:
        rows += (f"<div class='row'><div class='wall' style='background:{col}'><h3>{name}</h3><p>{src}</p></div>"
                 f"<div class='cell'>{'<br>'.join('• '+s for s in sym)}</div>"
                 f"<div class='cell' style='border-color:{col}'>{'<br>'.join('<b>&rarr;</b> '+f for f in fix)}</div></div>")
    body = f"<div class='canvas' id='cv'><h1>{d['title']}</h1><div class='sub'>{d['sub']}</div><div class='flow'>{flow}</div>{rows}<div class='foot'>{d['foot']}</div></div>"
    return page(d["title"], body, BN_CSS)

def build():
    files = []
    for lang in ("vi", "en"):
        sfx = "" if lang == "vi" else "-en"
        for name, fn in (("roadmap", roadmap), ("org-structure", org), ("bottlenecks", bottleneck)):
            path = os.path.join(OUT_HTML, f"diagram-{name}{sfx}.html")
            open(path, "w", encoding="utf-8").write(fn(lang))
            files.append((path, os.path.join(IMG, f"diagram-{name}{sfx}.png")))
    return files

def render(pg, files, hold_ms=500):
    for html, png in files:
        pg.goto("file:///" + html.replace("\\", "/"))
        pg.wait_for_timeout(hold_ms)
        pg.locator("#cv").screenshot(path=png)
        print("rendered", os.path.basename(png))

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    files = build()
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=False)
        pg = b.new_page(viewport={"width": 1600, "height": 1000})
        render(pg, files)
        b.close()
