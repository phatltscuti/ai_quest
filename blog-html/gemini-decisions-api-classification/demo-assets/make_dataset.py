"""Sinh bộ tài liệu GIẢ (fictional) để test phân loại: 8 loại x 5 mẫu = 40 file.

- Ngôn ngữ trộn: Tiếng Việt / English / 日本語
- ~1/4 là mẫu "khó": mất tiêu đề, ảnh chụp nghiêng + mờ + nhiễu, độ phân giải thấp
- 8 file xuất dạng PDF (để test input PDF), còn lại PNG
- Ground truth ghi vào dataset/labels.csv

Toàn bộ tên người, công ty, số tiền đều là ngẫu nhiên / hư cấu.
"""
import csv, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(20261120)
OUT = Path(__file__).parent / "dataset"
OUT.mkdir(exist_ok=True)
W, H = 900, 1273
F = "C:/Windows/Fonts/"

def font(lang, size, bold=False):
    if lang == "ja":
        return ImageFont.truetype(F + ("YuGothB.ttc" if bold else "YuGothR.ttc"), size)
    return ImageFont.truetype(F + ("arialbd.ttf" if bold else "arial.ttf"), size)

PEOPLE = {"vi": ["Nguyễn Văn An", "Trần Thị Bình", "Lê Minh Châu", "Phạm Quốc Dũng", "Võ Thu Hà"],
          "en": ["Alex Carter", "Jamie Moore", "Taylor Reed", "Jordan Lee", "Casey Brooks"],
          "ja": ["佐藤 健", "鈴木 花子", "高橋 誠", "田中 美咲", "伊藤 翔"]}
COMPANIES = {"vi": ["Công ty TNHH Sao Mai Demo", "Công ty CP Hoa Sen Mẫu", "Công ty Bình Minh Fictional"],
             "en": ["Northwind Sample Ltd.", "Blue Harbor Demo Inc.", "Acme Fictional Co."],
             "ja": ["株式会社サンプル商事", "デモ電機株式会社", "架空システム株式会社"]}
ITEMS = {"vi": ["Phát triển website", "Bảo trì hệ thống", "Thiết kế UI", "Kiểm thử phần mềm", "License phần mềm"],
         "en": ["Web development", "System maintenance", "UI design", "QA testing", "Software license"],
         "ja": ["Web開発", "システム保守", "UIデザイン", "ソフトウェアテスト", "ライセンス費用"]}

T = {  # tiêu đề + các dòng đặc trưng mỗi loại
 "invoice": {"vi": ("HÓA ĐƠN", ["Số hóa đơn: HD-{n}", "Hạn thanh toán: {d}", "Vui lòng chuyển khoản tới STK 0123 456 789 (Ngân hàng Demo)"]),
             "en": ("INVOICE", ["Invoice No: INV-{n}", "Payment due: {d}", "Please remit payment to account 0123-456-789 (Demo Bank)"]),
             "ja": ("請求書", ["請求番号: INV-{n}", "お支払期限: {d}", "下記口座へお振込みください デモ銀行 普通 1234567"])},
 "quotation": {"vi": ("BÁO GIÁ", ["Số báo giá: BG-{n}", "Báo giá có hiệu lực đến: {d}", "Giá trên chưa bao gồm VAT. Rất mong được hợp tác."]),
               "en": ("QUOTATION", ["Quote No: Q-{n}", "Valid until: {d}", "Prices exclude tax. We look forward to your order."]),
               "ja": ("御見積書", ["見積番号: Q-{n}", "有効期限: {d}", "下記の通り御見積申し上げます。"])},
 "receipt": {"vi": ("BIÊN NHẬN", ["Số: BN-{n}", "Đã nhận đủ số tiền bằng tiền mặt ngày {d}", "Cảm ơn quý khách!"]),
             "en": ("RECEIPT", ["Receipt No: R-{n}", "Paid in full by card on {d}", "Thank you for your payment."]),
             "ja": ("領収書", ["No. R-{n}", "上記正に領収いたしました {d}", "但し お品代として"])},
 "contract": {"vi": ("HỢP ĐỒNG DỊCH VỤ", ["Số hợp đồng: HĐ-{n}", "Điều 1. Phạm vi công việc", "Điều 2. Thời hạn hợp đồng đến {d}", "Điều 3. Bảo mật thông tin", "Điều 4. Giải quyết tranh chấp"]),
              "en": ("SERVICE AGREEMENT", ["Agreement No: SA-{n}", "Article 1. Scope of Services", "Article 2. Term ends on {d}", "Article 3. Confidentiality", "Article 4. Governing Law"]),
              "ja": ("業務委託契約書", ["契約番号: C-{n}", "第1条（目的）", "第2条（契約期間）{d}まで", "第3条（秘密保持）", "第4条（協議事項）"])},
 "leave_request": {"vi": ("ĐƠN XIN NGHỈ PHÉP", ["Kính gửi: Trưởng phòng", "Tôi xin nghỉ phép từ {d} (3 ngày)", "Lý do: việc gia đình", "Người bàn giao công việc: {p2}"]),
                   "en": ("LEAVE REQUEST", ["To: Team Manager", "Requested leave: {d}, 3 days", "Reason: family matters", "Backup person: {p2}"]),
                   "ja": ("休暇申請書", ["所属長 殿", "休暇期間: {d} から3日間", "理由: 私用のため", "業務代行者: {p2}"])},
 "resume": {"vi": ("SƠ YẾU LÝ LỊCH (CV)", ["Họ tên: {p}", "Kinh nghiệm: 4 năm lập trình PHP/Laravel", "Kỹ năng: JavaScript, MySQL, Docker", "Học vấn: Đại học Bách Khoa (giả định)"]),
            "en": ("RESUME", ["Name: {p}", "Experience: 5 years, full-stack developer", "Skills: Python, React, AWS", "Education: B.Sc. Computer Science (fictional)"]),
            "ja": ("履歴書", ["氏名: {p}", "職歴: ソフトウェアエンジニア 3年", "スキル: Java, Spring, SQL", "学歴: 架空大学 情報工学科 卒業"])},
 "meeting_minutes": {"vi": ("BIÊN BẢN HỌP", ["Ngày họp: {d}", "Thành phần: {p}, {p2}", "Nội dung: tiến độ dự án Demo", "Việc cần làm: {p2} gửi báo cáo trước thứ Sáu"]),
                     "en": ("MEETING MINUTES", ["Date: {d}", "Attendees: {p}, {p2}", "Agenda: Demo project status", "Action item: {p2} to send report by Friday"]),
                     "ja": ("議事録", ["日時: {d}", "出席者: {p}、{p2}", "議題: デモ案件の進捗確認", "宿題: {p2} が金曜までに報告書提出"])},
 "delivery_note": {"vi": ("PHIẾU GIAO HÀNG", ["Số phiếu: GH-{n}", "Ngày giao: {d}", "Địa chỉ giao: 12 Đường Mẫu, Quận Demo", "Người nhận ký xác nhận đã nhận đủ hàng"]),
                   "en": ("DELIVERY NOTE", ["Delivery No: DN-{n}", "Delivery date: {d}", "Ship to: 12 Sample Street, Demo City", "Goods received in good condition"]),
                   "ja": ("納品書", ["納品番号: DN-{n}", "納品日: {d}", "納品先: デモ市サンプル町1-2-3", "下記の通り納品いたします"])},
}
HAS_TABLE = {"invoice": "price", "quotation": "price", "receipt": "price", "delivery_note": "qty"}
SIGN_LBL = {"vi": "Chữ ký", "en": "Signature", "ja": "署名"}

def squiggle(d, x, y):
    pts, cx = [], x
    for _ in range(14):
        cx += random.randint(8, 16)
        pts.append((cx, y + random.randint(-18, 18)))
    d.line(pts, fill=(20, 40, 140), width=3, joint="curve")

def render(cls, lang, hide_title, sign):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    title, lines = T[cls][lang]
    p, p2 = random.sample(PEOPLE[lang], 2)
    comp = random.choice(COMPANIES[lang])
    fill = dict(n=random.randint(1000, 9999), d=f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}", p=p, p2=p2)
    d.text((60, 50), comp, font=font(lang, 22, True), fill="#333")
    d.line((60, 90, W - 60, 90), fill="#999", width=2)
    y = 120
    if not hide_title:
        d.text((W // 2, y), title, font=font(lang, 44, True), fill="black", anchor="mt"); y += 90
    else:
        y += 20
    for ln in lines:
        d.text((70, y), ln.format(**fill), font=font(lang, 24), fill="black"); y += 46
    if cls in HAS_TABLE:
        y += 20
        d.rectangle((60, y, W - 60, y + 44), fill="#e8edf5");
        hdr = {"price": {"vi": "Hạng mục / SL / Thành tiền", "en": "Item / Qty / Amount", "ja": "品目 / 数量 / 金額"},
               "qty": {"vi": "Hạng mục / Số lượng", "en": "Item / Quantity", "ja": "品目 / 数量"}}[HAS_TABLE[cls]][lang]
        d.text((75, y + 10), hdr, font=font(lang, 22, True), fill="black"); y += 54
        total = 0
        for it in random.sample(ITEMS[lang], 3):
            q, amt = random.randint(1, 5), random.randint(2, 40) * 500_000
            total += amt
            txt = f"{it}   x{q}" + (f"   {amt:,} VND" if HAS_TABLE[cls] == "price" else "")
            d.text((75, y), txt, font=font(lang, 22), fill="black"); y += 40
        if HAS_TABLE[cls] == "price":
            d.text((W - 75, y + 10), f"TOTAL: {total:,} VND", font=font(lang, 26, True), fill="black", anchor="ra"); y += 60
    sy = H - 230
    d.text((W - 300, sy), SIGN_LBL[lang], font=font(lang, 22), fill="#333")
    d.line((W - 300, sy + 110, W - 70, sy + 110), fill="#666", width=1)
    if sign:
        squiggle(d, W - 290, sy + 75)
    d.text((60, H - 50), "FICTIONAL SAMPLE – FOR DEMO ONLY", font=font("en", 16), fill="#aaa")
    return img

def make_hard(img, mode):
    if mode == "photo":
        img = img.rotate(random.choice([-7, -5, 4, 6]), expand=True, fillcolor=(205, 200, 190))
        img = img.filter(ImageFilter.GaussianBlur(1.6))
        noise = Image.effect_noise(img.size, 28).convert("RGB")
        img = Image.blend(img, noise, 0.12)
    elif mode == "lowres":
        img = img.resize((W // 3, H // 3)).resize((W, H))
    return img

jobs = []
langs = ["vi", "en", "ja", "vi", "en"]
for cls in T:
    hard_modes = random.sample(["notitle", "photo", "lowres", None, None], 5)
    jobs += [(cls, k, langs[k], hard_modes[k]) for k in range(5)]
random.shuffle(jobs)  # tên file doc_XX không lộ nhãn
rows = []
for i, (cls, k, lang, hard) in enumerate(jobs, 1):
    sign = random.random() < 0.55
    img = render(cls, lang, hide_title=(hard == "notitle"), sign=sign)
    if hard in ("photo", "lowres"):
        img = make_hard(img, hard)
    ext = "pdf" if k == 4 else "png"
    name = f"doc_{i:02d}.{ext}"
    img.save(OUT / name, **({"resolution": 110} if ext == "pdf" else {}))
    rows.append(dict(file=name, doc_type=cls, has_signature=int(sign), lang=lang, difficulty=hard or "normal"))

with open(OUT / "labels.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(sorted(rows, key=lambda r: r["file"]))
print(f"Created {len(rows)} documents in {OUT}")
from collections import Counter
print("Difficulty:", dict(Counter(r["difficulty"] for r in rows)))
print("Language:", dict(Counter(r["lang"] for r in rows)), "| PDF:", sum(r["file"].endswith("pdf") for r in rows))
