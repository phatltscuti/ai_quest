"""Generate the 2 custom infographics (VI + EN) as HTML, then render them to PNG with Playwright.

Outputs:
  infographics/infographic-01-ai-rollup-playbook-{vi,en}.html  -> images/infographic-01-ai-rollup-playbook-{vi,en}.png
  infographics/infographic-02-scuti-application-{vi,en}.html   -> images/infographic-02-scuti-application-{vi,en}.png
All numbers in infographic 01 come from Greg Isenberg's article (see sources/article-text.md).
Infographic 02 is the author's own proposal for Scuti AI (not from the article).
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
IMG = HERE.parent / "images"
IMG.mkdir(exist_ok=True)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#fff;font-family:'Segoe UI',Roboto,Arial,sans-serif;color:#212121}
.canvas{width:1400px;padding:44px 52px;background:linear-gradient(180deg,#f7f9fc,#ffffff)}
.top{background:linear-gradient(135deg,#0d47a1,#1565c0,#00838f);color:#fff;border-radius:18px;padding:26px 34px;margin-bottom:26px}
.top .k{font-size:15px;letter-spacing:2px;text-transform:uppercase;opacity:.85}
.top h1{font-size:33px;margin:6px 0 8px}
.top p{font-size:19px;opacity:.95}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:#fff;border:1px solid #e0e0e0;border-radius:14px;padding:18px 20px;box-shadow:0 2px 6px rgba(0,0,0,.05);position:relative}
.card .n{position:absolute;top:-14px;left:18px;background:#ff6d00;color:#fff;font-weight:700;border-radius:20px;padding:2px 14px;font-size:15px}
.card h3{font-size:21px;color:#0d47a1;margin:8px 0 8px}
.card li{font-size:15.5px;line-height:1.5;margin-left:18px;margin-bottom:3px}
.card .big{font-size:26px;font-weight:800;color:#2e7d32}
.row{display:flex;gap:18px;margin-top:22px}
.box{flex:1;border-radius:14px;padding:16px 20px}
.box h4{font-size:18px;margin-bottom:6px}
.box li{font-size:15px;line-height:1.5;margin-left:18px}
.green{background:#e8f5e9;border-left:5px solid #2e7d32}
.amber{background:#fff8e1;border-left:5px solid #f57f17}
.red{background:#ffebee;border-left:5px solid #c62828}
.foot{margin-top:20px;font-size:13px;color:#757575;text-align:right}
table{width:100%;border-collapse:separate;border-spacing:0 10px}
th{font-size:17px;text-align:left;padding:8px 16px;color:#fff;background:#0d47a1}
th:first-child{border-radius:10px 0 0 10px} th:last-child{border-radius:0 10px 10px 0}
td{background:#fff;border-top:1px solid #e0e0e0;border-bottom:1px solid #e0e0e0;padding:14px 16px;font-size:16px;line-height:1.5;vertical-align:top}
td:first-child{border-left:5px solid #ff6d00;border-radius:10px 0 0 10px;width:34%}
td:nth-child(2){width:8%;text-align:center;font-size:26px;color:#ff6d00}
td:last-child{border-right:1px solid #e0e0e0;border-radius:0 10px 10px 0}
td b{color:#0d47a1}
.tag{display:inline-block;background:#e3f2fd;color:#0d47a1;border-radius:10px;padding:1px 10px;font-size:13px;margin-top:4px}
"""

T = {
"vi": dict(
 k="Tóm tắt bài viết của Greg Isenberg trên X · 26/09/2026",
 h1="AI Roll-up Playbook: mua doanh nghiệp dịch vụ, để agent làm back-office",
 sub="Giữ nguyên khách hàng &amp; hoá đơn, tái thiết cách làm việc → biên EBITDA từ ~5–10% lên mục tiêu 30–40%",
 cards=[
  ("1","Tìm mục tiêu (Sourcing)",["Tra license board, đăng ký kinh doanh, hiệp hội ngành","Chủ 60–70 tuổi, chưa có người kế nghiệp","Tự liên hệ chủ trước khi lên marketplace"]),
  ("2","Chấm điểm (Scorecard)",["7 tiêu chí: việc lặp lại 20%, output kiểm được 20%, doanh thu định kỳ 15%…","&lt; 60% = một công việc, không phải thương vụ","≥ 80% = đáng gửi LOI"]),
  ("3","Diligence bằng mẫu công việc",["Xin 20–50 job thật (ẩn danh)","Lập <b>automation map</b>: volume × giờ","Phân loại: tự động / tự động + review / hỗ trợ / giữ người"]),
  ("4","Bài toán (ví dụ minh hoạ)",["Doanh thu $2.0M giữ nguyên","Biên 10% → 30%: EBITDA $200k → $600k","Định giá 4x: <span class='big'>$800k → $2.4M</span>"]),
  ("5","Rulebook = tài sản thật",["Phỏng vấn nhân sự senior → rule có ví dụ","Agent nháp → người sửa → <b>corrections-log.md</b>","Lỗi lặp lại ≥ 2 lần → rule + test case"]),
  ("6","100 ngày đầu",["Ngày 1–30: shadow mode, khách không thấy thay đổi","Ngày 31–60: chuyển back-office, preparer có review","Ngày 61–100: mở rộng thận trọng"]),
 ],
 g=("Nguyên tắc an toàn",["Reviewer được chặn, <b>không bao giờ</b> được gửi","Preparer không tự gửi gì ra ngoài","Con người duyệt rule &amp; gửi nội dung nhạy cảm"]),
 a=("Dashboard: 5 số mỗi thứ Hai",["Biên EBITDA · phút chú ý của người / job","Tỉ lệ phải sửa (phải giảm mỗi tháng)","Giữ chân khách hàng · giữ chân người chủ chốt"]),
 r=("Điều gì làm hỏng",["Mua nhanh hơn khả năng tích hợp","Người chủ chốt / khách rời đi","Tự động hoá mất niềm tin · agent quá nhiều quyền · tin số liệu tự báo cáo"]),
 foot="Infographic tự vẽ (HTML → PNG) · Số liệu từ bài “$5T opportunity: AI Roll Ups” – x.com/gregisenberg/status/2103927365977928019",
),
"en": dict(
 k="Summary of Greg Isenberg's post on X · Sep 26, 2026",
 h1="AI Roll-up Playbook: buy a services firm, let agents run the back office",
 sub="Keep the clients &amp; invoices, rebuild how work is delivered → EBITDA from ~5–10% toward a 30–40% target",
 cards=[
  ("1","Sourcing",["License boards, state filings, industry directories","Owners in their 60s–70s with no successor","Reach the owner before a broker lists it"]),
  ("2","Scorecard",["7 criteria: repeatable work 20%, checkable output 20%, recurring revenue 15%…","&lt; 60% = a job, not an acquisition","≥ 80% = deserves an LOI"]),
  ("3","Diligence with work samples",["Ask for 20–50 real, anonymized jobs","Build the <b>automation map</b>: volume × hours","Classify: automate / automate+review / assist / keep human"]),
  ("4","The math (illustrative)",["Revenue stays at $2.0M","Margin 10% → 30%: EBITDA $200k → $600k","Value at 4x: <span class='big'>$800k → $2.4M</span>"]),
  ("5","The rulebook is the asset",["Interview senior staff → numbered rules with examples","Agent drafts → human corrects → <b>corrections-log.md</b>","Repeated fix → new rule + test case"]),
  ("6","First 100 days",["Days 1–30: shadow mode, nothing visible to clients","Days 31–60: move the back office, every draft reviewed","Days 61–100: expand carefully"]),
 ],
 g=("Guardrails",["Reviewer can block, <b>never</b> ship","Preparer ships nothing on its own","Humans approve rules &amp; send sensitive comms"]),
 a=("Dashboard: 5 numbers every Monday",["EBITDA margin · human minutes per job","Correction rate (should fall monthly)","Client retention · key-person retention"]),
 r=("What breaks",["Buying faster than you can integrate","Key people / clients leave","Automating trust away · over-powered agents · trusting headline numbers"]),
 foot="Custom infographic (HTML → PNG) · Figures from “$5T opportunity: AI Roll Ups” – x.com/gregisenberg/status/2103927365977928019",
)}

T2 = {
"vi": dict(
 k="Bài học cá nhân · áp dụng cho Scuti AI (đề xuất của tác giả)",
 h1="Từ AI Roll-up đến dự án outsourcing của Scuti AI",
 sub="Ý tưởng cốt lõi giống nhau: giữ niềm tin của khách hàng, để AI agent gánh phần việc lặp lại, con người giữ cửa chất lượng",
 th=("Ý tưởng trong bài của Greg","Cách áp dụng tại Scuti AI"),
 rows=[
  ("<b>Automation map</b> (volume × giờ)","Kiểm kê task của từng dự án: dịch JP↔VI, viết test case, unit test, tài liệu basic/detail design, báo cáo tuần → chọn task nhiều giờ, ít rủi ro làm trước","Tuần 1"),
  ("<b>Rulebook + corrections-log.md</b>","Gom các 指摘 (chỉ trích review) của khách Nhật thành rule file cho agent (CLAUDE.md / rules/) và test case; review log mỗi tuần","Liên tục"),
  ("<b>Preparer ≠ Reviewer</b> (block, never ship)","Agent tạo PR / tài liệu nháp; reviewer agent chỉ được chặn; chỉ người (dev lead, BrSE) mới merge hoặc gửi cho khách","Quy trình"),
  ("<b>Shadow mode 30 ngày</b>","Chạy agent song song với cách làm hiện tại trên 1 loại task, so sánh chất lượng &amp; thời gian trước khi đưa vào sản xuất","Pilot"),
  ("<b>5 số mỗi thứ Hai</b>","Dashboard dự án: margin, phút người / ticket, tỉ lệ phải sửa, phản hồi khách, giữ chân thành viên chủ chốt","Hằng tuần"),
  ("<b>Đừng tự động hoá mất niềm tin</b>","BrSE / PM vẫn là người nói chuyện với khách; AI ở back-office, không tự gửi email cho khách","Nguyên tắc"),
 ],
 foot="Infographic tự vẽ (HTML → PNG) · Cột phải là đề xuất cá nhân, không phải số liệu đã kiểm chứng của Scuti AI",
),
"en": dict(
 k="Personal learnings · applying to Scuti AI (author's proposal)",
 h1="From AI Roll-ups to Scuti AI's outsourcing projects",
 sub="Same core idea: protect client trust, let AI agents carry the repetitive work, keep humans as the quality gate",
 th=("Idea from Greg's post","How we apply it at Scuti AI"),
 rows=[
  ("<b>Automation map</b> (volume × hours)","Inventory each project's tasks: JP↔VI translation, test cases, unit tests, basic/detail design docs, weekly reports → start with high-hour, low-risk tasks","Week 1"),
  ("<b>Rulebook + corrections-log.md</b>","Turn Japanese clients' review comments (指摘) into agent rule files (CLAUDE.md / rules/) and test cases; review the log weekly","Ongoing"),
  ("<b>Preparer ≠ Reviewer</b> (block, never ship)","Agents draft PRs/docs; the reviewer agent can only block; only humans (dev lead, BrSE) merge or send to the client","Process"),
  ("<b>30-day shadow mode</b>","Run agents in parallel with the current way on one task type; compare quality &amp; time before production","Pilot"),
  ("<b>5 numbers every Monday</b>","Project dashboard: margin, human minutes per ticket, correction rate, client feedback, key-member retention","Weekly"),
  ("<b>Don't automate trust away</b>","BrSE/PM stay the client's point of contact; AI works in the back office and never emails clients on its own","Principle"),
 ],
 foot="Custom infographic (HTML → PNG) · Right column is a personal proposal, not verified Scuti AI data",
)}


def page1(d):
    cards = "".join(
        f"<div class='card'><span class='n'>{n}</span><h3>{h}</h3><ul>{''.join(f'<li>{x}</li>' for x in li)}</ul></div>"
        for n, h, li in d["cards"])
    box = lambda cls, t: f"<div class='box {cls}'><h4>{t[0]}</h4><ul>{''.join(f'<li>{x}</li>' for x in t[1])}</ul></div>"
    return (f"<div class='canvas'><div class='top'><div class='k'>{d['k']}</div><h1>{d['h1']}</h1><p>{d['sub']}</p></div>"
            f"<div class='grid'>{cards}</div><div class='row'>{box('green', d['g'])}{box('amber', d['a'])}{box('red', d['r'])}</div>"
            f"<div class='foot'>{d['foot']}</div></div>")


def page2(d):
    rows = "".join(f"<tr><td>{a}</td><td>&#10140;</td><td>{b}<br><span class='tag'>{c}</span></td></tr>" for a, b, c in d["rows"])
    return (f"<div class='canvas'><div class='top'><div class='k'>{d['k']}</div><h1>{d['h1']}</h1><p>{d['sub']}</p></div>"
            f"<table><tr><th>{d['th'][0]}</th><th></th><th>{d['th'][1]}</th></tr>{rows}</table>"
            f"<div class='foot'>{d['foot']}</div></div>")


def wrap(title, body):
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"


jobs = []
for lang in ("vi", "en"):
    for name, fn, d in (("infographic-01-ai-rollup-playbook", page1, T[lang]), ("infographic-02-scuti-application", page2, T2[lang])):
        p = HERE / f"{name}-{lang}.html"
        p.write_text(wrap(name, fn(d)), encoding="utf-8")
        jobs.append((p, IMG / f"{name}-{lang}.png"))

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1400, "height": 900})
    for src, out in jobs:
        pg.goto(src.resolve().as_uri())
        pg.locator(".canvas").screenshot(path=str(out))
        print("rendered", out.name)
    b.close()
