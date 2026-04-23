import re

html_file = r"c:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\design-md-b2b-system-mockup-blog.html"

with open(html_file, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    'step-01-stitch-home.png': '<strong>👉 Bước 1:</strong> Mở trang chủ Google Stitch, nhớ dăng nhập và <strong>chọn chế độ Web</strong>.',
    'step-02-direction-brief.png': '<strong>👉 Bước 2:</strong> Mở Notepad, gõ 4 dòng định hướng (Policy) để làm "kim chỉ nam" cho dự án.',
    'step-03-first-prompt.png': '<strong>👉 Bước 3:</strong> Dán Prompt chi tiết phía trên vào ô Chat của Stitch để AI bắt đầu công việc.',
    'step-04-rough-mockup.png': '<strong>👉 Bước 4:</strong> Bấm nút Gửi (Enter) và đợi AI vẽ xong màn hình thô (Rough Mockup).',
    'step-05-iteration-prompts.png': '<strong>👉 Bước 5:</strong> Click vào Bảng dữ liệu (Table), nhập lệnh màu cảnh báo (đỏ/vàng) vào ô công cụ nhỏ vừa bật lên.',
    'step-06-design-system-board.png': '<strong>👉 Bước 6:</strong> Gõ Prompt tạo Design System vào khung Chat. Một bảng màu sắc và font chữ sẽ được AI vẽ ra bên cạnh.',
    'step-07-design-md-panel.png': '<strong>👉 Bước 7:</strong> Yêu cầu AI xuất bộ luật đó ra định dạng mã nguồn <code>DESIGN.md</code>.',
    'step-08-apply-design-system.png': '<strong>👉 Bước 8:</strong> Chọn lại khung giao diện nháp ở trên. Dán Prompt yêu cầu ép khuôn (Apply) để AI ốp hệ màu chuẩn từ DESIGN.md vào.',
    'step-09-before-after.png': '<strong>👉 Bước 9:</strong> Đặt nháp cũ (bên trái) và bản vừa áp dụng khuôn (bên phải) cạnh nhau để đối chiếu sự lột xác.',
    'step-10-prototype-check.png': '<strong>👉 Bước 10:</strong> Bấm nút Play / Preview trên góc phải để thử rê chuột vào nút bấm xem hiệu ứng Hover.',
    'step-11-export-or-handoff.png': '<strong>👉 Bước 11:</strong> Bấm nút Code / Export trên góc phải để xem và copy mã nguồn HTML.',
    'step-12-final-result-local.png': '<strong>👉 Bước 12:</strong> Bỏ toàn bộ file HTML, file DESIGN.md và 12 ảnh vào chung một thư mục trên máy tính.'
}

for img_name, caption in replacements.items():
    # Find <img src="images/xxx.png" ...> and prepend <p>
    pattern = r'(<img\s+src="images/' + img_name + r'".*?>)'
    replacement = f'<p style="margin-top:16px; margin-bottom: 8px;">{caption}</p>\n        \\1'
    text = re.sub(pattern, replacement, text)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS")
