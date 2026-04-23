import re

html_file = r"c:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\design-md-b2b-system-mockup-blog.html"
md_file = r"c:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\HUONG-DAN-DEMO-CHUP-ANH.md"

md_content = """# Hướng dẫn chụp ảnh demo - DESIGN.md cho mockup B2B

Chụp ảnh theo thứ tự bên dưới và lưu vào thư mục `images/` với đúng tên file. Các ảnh này sẽ tự động hiển thị trong trang blog.

## Yêu cầu chung
- Định dạng: PNG
- Độ rộng đề xuất: Từ 1280px trở lên
- Ghi chú: Chụp rõ toàn màn hình hoặc khu vực có đầy đủ panel thao tác, prompt và kết quả giao diện.

## Danh sách ảnh cần chụp chi tiết

1. `step-01-stitch-home.png`
- **Hành động:** Mở trình duyệt, truy cập vào `https://stitch.withgoogle.com`. Đăng nhập và tìm kiếm mục "New Project" hoặc tương tự.
- **Góc chụp:** Chụp toàn màn hình trang chủ Canvas trống, thanh nhập liệu ở giữa và các menu công cụ (Web/App mode) hiện rõ.

2. `step-02-direction-brief.png`
- **Hành động:** Mở công cụ Note (hoặc Notepad) trên máy tính, gõ đoạn Brief ngắn 4 dòng: (Ai sử dụng, Mục tiêu, Cảm giác cần tạo, Ấn tượng cần tránh).
- **Góc chụp:** Chụp ảnh cửa sổ Note đó đặt cạnh màn hình Stitch để thấy sự chuẩn bị dự án trước khi nhập.

3. `step-03-first-prompt.png`
- **Hành động:** Tại khung nhập liệu của Stitch, gõ hoặc copy dán đoạn prompt Rough Draft: *"Design a desktop B2B system management dashboard for enterprise operations. Main sections: Top nav, Left nav, KPI row, Incident table, Right action panel. Style: professional, minimal noise."*
- **Góc chụp:** Chụp lại toàn bộ khu vực bạn đang gõ nội dung này ngay trước khi bấm nút gửi (Generate/Submit).

4. `step-04-rough-mockup.png`
- **Hành động:** Đợi Stitch generate xong toàn màn hình Dashboard B2B.
- **Góc chụp:** Dùng chuột cuộn nhỏ (zoom out) và chụp bao quát màn hình Dashboard vừa được tạo (hiện rõ các thẻ KPI, bảng Incident).

5. `step-05-iteration-prompts.png`
- **Hành động:** Chọn vào bảng Incident (Table) hoặc một thẻ KPI trên Canvas, mở thanh prompt chỉnh sửa cục bộ và ra lệnh (vd: đổi màu cảnh báo).
- **Góc chụp:** Chụp khoảnh khắc thanh công cụ sửa đổi đang hiển thị đè lên trên phần mềm UI.

6. `step-06-design-system-board.png`
- **Hành động:** Gõ tiếp prompt tổng thể: *"From this dashboard draft, create a reusable design system. Organize into: Color roles, Typography, Spacing, Components."*
- **Góc chụp:** Chụp màn hình khoảnh khắc Canvas tự động sinh thêm các Artboard chứa bảng màu, Typography và Components.

7. `step-07-design-md-panel.png`
- **Hành động:** Yêu cầu AI *"Generate a DESIGN.md containing all these rules"*.
- **Góc chụp:** Chụp lại đoạn mã nguồn Markdown sinh ra trong khung Chat, hoặc ảnh chụp màn hình lúc bạn sao chép nó ra trình soạn thảo VS Code.

8. `step-08-apply-design-system.png`
- **Hành động:** Mở một giao diện nháp khác bên cạnh, nhập prompt: *"Apply the generated design system to this dashboard screen."*
- **Góc chụp:** Chụp song song 2 panel: Design System bên trái và Dashboard đang được AI đổ màu bên phải.

9. `step-09-before-after.png`
- **Hành động:** Dùng phần mềm ghép tự do 2 bản: Rough Mockup bên trái (khi chưa có style) và bản đã áp dụng Design System bên phải.
- **Góc chụp:** Lưu thành một hình ảnh tổng hợp (Collage) rõ ràng.

10. `step-10-prototype-check.png`
- **Hành động:** Bấm vào nút "Play" hoặc "Preview" góc trên cùng.
- **Góc chụp:** Chụp màn hình lúc con chuột đang trỏ vào (hover) hiển thị hiệu ứng của một Button, chứng minh tính tương tác.

11. `step-11-export-or-handoff.png`
- **Hành động:** Bấm nút "Export" hoặc "Code" trên thanh công cụ.
- **Góc chụp:** Chụp cửa sổ popup hiện ra mã HTML/CSS hoặc nút Export.

12. `step-12-final-result-local.png`
- **Hành động:** Mở VS Code, hiển thị cấu trúc thư mục chứa file `DESIGN.md`, file HTML và thư mục `images`.
- **Góc chụp:** Chụp góc màn hình có Sidebar VS Code chứng minh toàn bộ asset đã trên máy tính.

## Checklist đạt yêu cầu
- [ ] Ảnh rõ nét, hiển thị cả ngữ cảnh làm việc (thanh prompt, canvas rộng).
- [ ] Chụp đúng thời điểm tương tác chỉ dẫn bên trên.
- [ ] Lưu đúng tên file vào thư mục `images/` bên cạnh file HTML.
"""

with open(md_file, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Add CSS
css_to_add = """  .img-placeholder { border: 2px dashed #cbd5e1; border-radius: 8px; padding: 20px; background: #f8fafc; margin: 16px 0; }
  .img-placeholder h4 { color: var(--primary); margin-top: 0; margin-bottom: 8px; font-size: 1.05rem; }
  .img-placeholder p { font-size: 0.9rem; color: var(--muted); margin: 0; }
  .img-placeholder code { background: #e2e8f0; color: #1e293b; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
  .img-real { width: 100%; border-radius: 8px; border: 1px solid var(--border); box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin: 16px 0; display: none; }
"""
html = html.replace('</style>', css_to_add + '</style>')

# Replace 3.1
html = html.replace("""      </ul>\n\n      <h3>3.2""", """      </ul>
      <div class="img-placeholder">
        <h4>📸 Ảnh 1 & 2: Màn hình chủ Stitch & Tạo Note Brief</h4>
        <p>Để hiển thị ảnh tự động, lưu 2 ảnh với tên: <code>step-01-stitch-home.png</code> và <code>step-02-direction-brief.png</code></p>
      </div>
      <img src="images/step-01-stitch-home.png" class="img-real" alt="Stitch Home">
      <img src="images/step-02-direction-brief.png" class="img-real" alt="Direction Brief">

      <h3>3.2""")

# Replace 3.2
html = html.replace("""ing-style hero blocks.</div>\n\n      <h3>3.3""", """ing-style hero blocks.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 3, 4 & 5: Prompt đầu tiên, Rough Mockup & Các prompt tinh chỉnh</h4>
        <p>Lưu 3 ảnh vào thư mục images/: <code>step-03-first-prompt.png</code>, <code>step-04-rough-mockup.png</code> và <code>step-05-iteration-prompts.png</code></p>
      </div>
      <img src="images/step-03-first-prompt.png" class="img-real" alt="First Prompt">
      <img src="images/step-04-rough-mockup.png" class="img-real" alt="Rough Mockup">
      <img src="images/step-05-iteration-prompts.png" class="img-real" alt="Iteration Prompts">

      <h3>3.3""")

# Replace 3.3
html = html.replace(""" over decoration.</div>\n\n      <h3>3.4""", """ over decoration.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 6 & 7: Visual Board & File DESIGN.md</h4>
        <p>Lưu 2 ảnh vào thư mục images/: <code>step-06-design-system-board.png</code> và <code>step-07-design-md-panel.png</code></p>
      </div>
      <img src="images/step-06-design-system-board.png" class="img-real" alt="Design System Board">
      <img src="images/step-07-design-md-panel.png" class="img-real" alt="Design MD Panel">

      <h3>3.4""")

# Replace 3.4
html = html.replace(""" unchanged.</div>\n    </div>""", """ unchanged.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 8, 9 & 10: Apply Design, So sánh Before/After & Prototype Check</h4>
        <p>Lưu 3 ảnh vào thư mục images/: <code>step-08-apply-design-system.png</code>, <code>step-09-before-after.png</code> và <code>step-10-prototype-check.png</code></p>
      </div>
      <img src="images/step-08-apply-design-system.png" class="img-real" alt="Apply Design System">
      <img src="images/step-09-before-after.png" class="img-real" alt="Before/After">
      <img src="images/step-10-prototype-check.png" class="img-real" alt="Prototype Check">
    </div>""")

# Replace Section 4 box
html = html.replace("""<div class="img-box">Dat anh that te vao <code>images/step-04-rough-mockup.png</code> den <code>images/step-09-before-after.png</code> de thay ro quy trinh verify.</div>""", """<div class="img-placeholder">
        <h4>📸 Ảnh 11 & 12: Handoff & Final Result Local</h4>
        <p>Lưu 2 file ảnh cuối cùng: <code>step-11-export-or-handoff.png</code> và <code>step-12-final-result-local.png</code></p>
      </div>
      <img src="images/step-11-export-or-handoff.png" class="img-real" alt="Export or Handoff">
      <img src="images/step-12-final-result-local.png" class="img-real" alt="Final Result Local">""")

# Add script at the bottom
script_to_add = """
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const placeholders = document.querySelectorAll('.img-placeholder');
    placeholders.forEach(ph => {
      let nextElem = ph.nextElementSibling;
      while (nextElem && nextElem.tagName === 'IMG' && nextElem.classList.contains('img-real')) {
        let img = nextElem;
        img.onload = function() {
          img.style.display = 'block';
          ph.style.display = 'none';
        };
        const src = img.getAttribute('src');
        img.src = src + '?t=' + new Date().getTime(); // Phuc vu test/reload khong cache
        nextElem = nextElem.nextElementSibling;
      }
    });
  });
</script>
"""
html = html.replace('</body>', script_to_add + '</body>')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS")
