import re

html_file = r"c:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\design-md-b2b-system-mockup-blog.html"

with open(html_file, "r", encoding="utf-8") as f:
    text = f.read()

# I will replace everything between <body> and <script> with the new detailed Vietnamese content.
new_body = """
<div class="hero">
  <h1>Thực hành: Sử dụng DESIGN.md để tạo Mockup Hệ thống B2B</h1>
  <p>Tóm tắt quy trình tham chiếu từ bài viết thực hành, tạo một mockup chuyên biệt cho hệ thống quản trị B2B và đánh giá khả năng duy trì "Design Stability" (Sự ổn định của thiết kế) nhờ DESIGN.md.</p>
</div>

<div class="container">
  <div class="card toc">
    <h3>Mục lục</h3>
    <ol>
      <li><a href="#m1">Mục tiêu và phạm vi đánh giá</a></li>
      <li><a href="#m2">Tóm tắt khách quan quy trình từ bài viết tham chiếu</a></li>
      <li><a href="#m3">Thực hành: Tự tạo Mockup B2B System Management</a></li>
      <li><a href="#m4">Kết quả Mockup B2B hiển thị</a></li>
      <li><a href="#m5">Cảm nhận về Design Stability qua DESIGN.md</a></li>
      <li><a href="#m6">Ứng dụng công nghệ vào quy trình làm việc thực tế</a></li>
    </ol>
  </div>

  <section id="m1">
    <h2>1) Mục tiêu và phạm vi đánh giá</h2>
    <div class="card">
      <p>Căn cứ theo yêu cầu thực tế, bài viết này tập trung vào các mục tiêu sau:</p>
      <ul>
        <li><strong>Tóm tắt quy trình:</strong> Đọc hiểu và tóm tắt lại bài viết tham chiếu một cách khách quan, chỉ ra cách duy trì tính đồng nhất thiết kế thông qua tính năng tạo <code>DESIGN.md</code> của Google Stitch.</li>
        <li><strong>Sáng tạo Use Case mới (B2B Dashboard):</strong> Thay vì dùng lại ví dụ trang web giới thiệu bản thân (Self-intro website) trong bài gốc, tôi sẽ đóng vai trò là Product Manager/Designer thiết kế một màn hình Quản trị hệ thống B2B (B2B System Management) mang tính đặc thù nghiệp vụ cao.</li>
        <li><strong>Phân tích ứng dụng:</strong> Đưa ra quan điểm cá nhân về cách phương pháp này giải quyết các "pain-points" (điểm nghẽn) trong công việc giữa Team Design và Team Dev hằng ngày.</li>
      </ul>
    </div>
  </section>

  <section id="m2">
    <h2>2) Tóm tắt khách quan quy trình từ bài viết tham chiếu</h2>
    <div class="card">
      <p>Bài viết tham chiếu <em>(Google Stitchがだいたい理解できるハンズオンマニュアル)</em> trình bày một chu trình 8 bước cực kỳ thực tế dành cho "Non-designers" (Người không chuyên thiết kế) để có thể tạo ra thiết kế có tính ứng dụng cao:</p>
      <ol>
        <li><strong>Bước 1: Đăng nhập và thiết lập:</strong> Đăng nhập Google Stitch, xác định rõ nhu cầu và chọn chế độ phù hợp (Web, App).</li>
        <li><strong>Bước 2: Xác định phương hướng (Policy First):</strong> Trước khi vẽ giao diện, cần xác định rõ 4 yếu tố cốt lõi: Đối tượng sử dụng, Mục tiêu của màn hình, Cảm giác/Tone&Mood cần đạt được, và Đặc điểm/Ấn tượng cần tránh.</li>
        <li><strong>Bước 3: Tạo bản phác thảo thô (Rough Draft):</strong> Đưa 4 yếu tố trên vào hệ thống để AI sinh ra bản phác thảo ban đầu. Ở bước này chưa cần quan tâm đến tiểu tiết thẩm mỹ.</li>
        <li><strong>Bước 4: Trích xuất Design System và DESIGN.md:</strong> Yêu cầu Stitch quy chuẩn hóa bản phác thảo thành một Design System hoàn chỉnh (Bảng màu, Typography, Layout spacing) và quan trọng nhất là trích xuất bộ quy tắc này thành tệp văn bản <code>DESIGN.md</code>.</li>
        <li><strong>Bước 5: Áp dụng lại Design System:</strong> Dùng chính bộ quy tắc vừa tạo để áp dụng (apply) ngược lại vào trang nháp ban đầu, giúp làm rập khuôn và đồng bộ hóa lại hệ thống phân cấp hiển thị và phong cách.</li>
        <li><strong>Bước 6: Xác thực Prototype:</strong> Chạy thử chế độ Preview/Prototype để chắc chắn dòng chảy UX hợp lý (người dùng quét được thông tin nhanh chóng).</li>
        <li><strong>Bước 7: Kết nối Claude Code qua hệ thống MCP:</strong> Thiết lập kết nối API (Model Context Protocol) giữa Google Stitch và công cụ lập trình AI (Claude Code).</li>
        <li><strong>Bước 8: Tinh chỉnh mã nguồn (Micro-fix):</strong> Yêu cầu Claude Code kéo mã nguồn thiết kế từ Stitch về môi trường phát triển (Local) và thực hiện các chỉnh sửa nhỏ trực tiếp trên Code thay vì chỉnh sửa thủ công trên công cụ thiết kế, giữ nguyên vẹn các quy tắc từ <code>DESIGN.md</code>.</li>
      </ol>
      <p><strong>Điểm cốt lõi:</strong> Bài viết khẳng định triết lý "Thiết lập quy tắc trước - Trau chuốt sau". Việc sử dụng <code>DESIGN.md</code> là chìa khóa chống lại hiện tượng "trôi dạt phong cách" (Style drift) mà các công cụ AI thế hệ trước hay gặp phải.</p>
    </div>
  </section>

  <section id="m3">
    <h2>3) Thực hành: Tự tạo Mockup B2B System Management</h2>
    <div class="card">
      <h3>3.1 Khởi tạo Policy (Brief đầu vào)</h3>
      <p>Với định hướng một hệ thống B2B chuyên nghiệp thay vì Consumer App, tôi xây dựng bộ phương hướng sau:</p>
      <ul>
        <li><strong>Ai sử dụng:</strong> Vận hành viên hệ thống (Operation manager), Đội hỗ trợ (Support lead).</li>
        <li><strong>Mục tiêu:</strong> Theo dõi sức khỏe hệ thống theo thời gian thực (KPIs), xử lý sự cố (Incidents), quản lý hàng đợi.</li>
        <li><strong>Cảm giác cần tạo ra:</strong> Trực quan, Tin cậy, Kiểm soát tốt (Control Tower), Hiện đại nhưng nghiêm túc.</li>
        <li><strong>Ấn tượng cần tránh:</strong> Quá lòe loẹt, vui nhộn, đồ họa Marketing chiếm diện tích. Cần mật độ hiển thị dữ liệu (Data density) cực tốt.</li>
      </ul>
      <div class="img-placeholder">
        <h4>📸 Ảnh 1 & 2: Màn hình chủ Stitch & Tạo Note Brief</h4>
        <p>Để hiển thị ảnh tự động, lưu 2 ảnh với tên: <code>step-01-stitch-home.png</code> và <code>step-02-direction-brief.png</code></p>
      </div>
      <img src="images/step-01-stitch-home.png" class="img-real" alt="Stitch Home">
      <img src="images/step-02-direction-brief.png" class="img-real" alt="Direction Brief">

      <h3>3.2 Nhập Prompt tạo bản phác thảo thô (Rough Mockup)</h3>
      <div class="prompt-box">Design a desktop B2B system management dashboard for enterprise operations.
Audience: operation managers and compliance teams.
Main sections:
- Top navigation with environment badge and global search
- Left side navigation (Overview, Incidents, Users, Integrations, Billing, Audit)
- KPI row: Uptime, Active Incidents, Queue Backlog, SLA Breach Risk
- Incident table with severity, owner, status, updated time
- Right action panel for "Assign owner", "Escalate", "Resolve"
Style: professional, standard data density, high readability.
Avoid playful visuals and avoid marketing-style hero blocks. Focus on utility.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 3, 4 & 5: Prompt đầu tiên, Rough Mockup & Các prompt tinh chỉnh</h4>
        <p>Lưu 3 ảnh vào thư mục images/: <code>step-03-first-prompt.png</code>, <code>step-04-rough-mockup.png</code> và <code>step-05-iteration-prompts.png</code></p>
      </div>
      <img src="images/step-03-first-prompt.png" class="img-real" alt="First Prompt">
      <img src="images/step-04-rough-mockup.png" class="img-real" alt="Rough Mockup">
      <img src="images/step-05-iteration-prompts.png" class="img-real" alt="Iteration Prompts">

      <h3>3.3 Prompt trích xuất bộ quy tắc DESIGN.md</h3>
      <div class="prompt-box">From this B2B dashboard draft, create a reusable enterprise design system.
Organize into:
- Color roles (Primary, Warning, Critical, Backgrounds)
- Typography (Headers, Body, Dense Table Data)
- Spacing (Rhythm for high-density cards)
- Components (nav, KPI cards, table, status badges, action area)
- Layout principles (Grid distribution, Sidebar behavior)
Prioritize consistency, auditability, and enterprise clarity over decoration. Generate a DESIGN.md containing these precise metrics and hex codes.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 6 & 7: Visual Board & File DESIGN.md</h4>
        <p>Lưu 2 ảnh vào thư mục images/: <code>step-06-design-system-board.png</code> và <code>step-07-design-md-panel.png</code></p>
      </div>
      <img src="images/step-06-design-system-board.png" class="img-real" alt="Design System Board">
      <img src="images/step-07-design-md-panel.png" class="img-real" alt="Design MD Panel">

      <h3>3.4 Prompt ép khuôn lại thiết kế (Apply Design System)</h3>
      <div class="prompt-box">Apply the generated design system (from the DESIGN.md rules) strictly back to this dashboard screen.
Align the heading hierarchy, spacing rhythm, table density, and component consistency automatically.
Keep the information architecture (KPIs, Tables, Sidemenu) exactly the same, only homogenize the visual language.</div>
      <div class="img-placeholder">
        <h4>📸 Ảnh 8, 9 & 10: Apply Design, So sánh Before/After & Prototype Check</h4>
        <p>Lưu 3 ảnh vào thư mục images/: <code>step-08-apply-design-system.png</code>, <code>step-09-before-after.png</code> và <code>step-10-prototype-check.png</code></p>
      </div>
      <img src="images/step-08-apply-design-system.png" class="img-real" alt="Apply Design System">
      <img src="images/step-09-before-after.png" class="img-real" alt="Before/After">
      <img src="images/step-10-prototype-check.png" class="img-real" alt="Prototype Check">
    </div>
  </section>

  <section id="m4">
    <h2>4) Kết quả Mockup B2B hiển thị</h2>
    <div class="card">
      <p>Sau khi hệ thống áp dụng bộ quy tắc chuẩn, dưới đây là phiên bản giao diện (Code nhúng giả lập) mô phỏng lại một Control Center B2B đúng chuẩn tính thực dụng của hệ thống quản trị, tuân thủ bảng màu và Spacing:</p>

      <div class="mockup">
        <div class="top"><strong>AcmeOps Control Center</strong> &nbsp;|&nbsp; Môi trường: <span style="background:#0e9f6e; padding:1px 6px; border-radius:4px; font-size:0.8rem;">Production</span> &nbsp;|&nbsp; 🔍 Tìm kiếm Incidents... &nbsp;|&nbsp; 🔔 Cảnh báo (3)</div>
        <div class="main">
          <div class="left">
            <p style="color:var(--primary); font-weight:600; padding:4px 0;">📊 Tổng quan (Overview)</p>
            <p style="color:var(--muted); padding:4px 0;">🚨 Sự cố (Incidents)</p>
            <p style="color:var(--muted); padding:4px 0;">👥 Người dùng</p>
            <p style="color:var(--muted); padding:4px 0;">🔌 Tích hợp</p>
            <p style="color:var(--muted); padding:4px 0;">💳 Thanh toán</p>
            <p style="color:var(--muted); padding:4px 0;">📋 Lịch sử (Audit Logs)</p>
          </div>
          <div class="right">
            <h3 style="margin-top:0;">Trạng thái hệ thống thời gian thực</h3>
            <div class="kpi-grid">
              <div class="kpi" style="border-top: 3px solid var(--secondary);"><div>Uptime 24h</div><div class="num" style="color:var(--secondary);">99.95%</div></div>
              <div class="kpi" style="border-top: 3px solid var(--critical);"><div>Sự cố đang mở</div><div class="num" style="color:var(--critical);">7</div></div>
              <div class="kpi" style="border-top: 3px solid var(--warning);"><div>Hàng đợi (Queue)</div><div class="num" style="color:var(--warning);">43</div></div>
              <div class="kpi"><div>Nguy cơ vi phạm SLA</div><div class="num">12%</div></div>
            </div>
            
            <h3 style="margin-top:20px;">Danh sách Sự cố cần chú ý (Incidents)</h3>
            <div class="table">
              <div class="row head">
                <div class="cell">Tên Incident</div><div class="cell">Mức độ (Severity)</div><div class="cell">Người xử lý</div><div class="cell">Trạng thái (Status)</div>
              </div>
              <div class="row">
                <div class="cell" style="font-weight:600;">API timeout - Cổng Thanh toán</div><div class="cell" style="color:var(--critical);">High (P1)</div><div class="cell">N. Tran</div><div class="cell"><span class="badge b-err">Đang điều tra</span></div>
              </div>
              <div class="row">
                <div class="cell" style="font-weight:600;">Webhook retry tăng đột biến</div><div class="cell" style="color:var(--warning);">Medium (P2)</div><div class="cell">M. Le</div><div class="cell"><span class="badge b-warn">Đang theo dõi</span></div>
              </div>
              <div class="row">
                <div class="cell">Đồng bộ dữ liệu đêm qua chậm</div><div class="cell">Low (P3)</div><div class="cell">K. Vu</div><div class="cell"><span class="badge b-ok">Đã giải quyết</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <p><strong>Artifact xuất bản:</strong> File <code>DESIGN.md</code> đóng vai trò là "nguồn chân lý" (Source of Truth) dùng để truyền tay cho AI Coding Agent (như Claude Code ở Bước 7 của bài thao khảo) để tiếp tục lập trình mà không sợ sai quy chuẩn màu sắc hệ thống.</p>
      
      <div class="img-placeholder">
        <h4>📸 Ảnh 11 & 12: Handoff & Final Result Local</h4>
        <p>Lưu 2 file ảnh cuối cùng: <code>step-11-export-or-handoff.png</code> và <code>step-12-final-result-local.png</code></p>
      </div>
      <img src="images/step-11-export-or-handoff.png" class="img-real" alt="Export or Handoff">
      <img src="images/step-12-final-result-local.png" class="img-real" alt="Final Result Local">
    </div>
  </section>

  <section id="m5">
    <h2>5) Cảm nhận về "Design Stability" khi sử dụng DESIGN.md</h2>
    <div class="card">
      <p>Việc sinh ra các thiết kế ngẫu nhiên bằng AI rất dễ, nhưng duy trì nó qua các phiên bản là bài toán khó. Từ quá trình thực hành, tôi đúc kết các góc nhìn khách quan sau:</p>
      <ul>
        <li><strong>Giữ vững Tính nhất quán trực quan (Visual Stability):</strong> Các màu sắc phân cấp (Primary, Warning, Danger) và hệ thống Typographic Spacing giữa các Card dữ liệu không bị thay đổi tùy tiện trong quá trình hệ thống tự sinh mã. Design.md bắt buộc AI khóa cứng các hằng số hex code.</li>
        <li><strong>Bảo toàn Kiến trúc thông tin (IA Stability):</strong> Dù Prompt có yêu cầu chỉnh sửa layout nhỏ lẻ (như thay đổi kích cỡ table), cấu trúc cốt lõi của màn hình B2B (Top Nav, Left Sidebar, KPI area) không hề bị gãy vỡ.</li>
        <li><strong>Giảm thiểu hao phí Align (Chấn chỉnh lệch màu):</strong> Thông thường, Team Dev và Designer rất mất thời gian soi dóng từng Pixel/Mã màu. Với Design.md đóng vai trò như hợp đồng "Smart Contract", mức độ rủi ro sai lệch trong Code Handoff được kiểm soát tuyệt đối.</li>
        <li><strong>Lưu ý và Hạn chế:</strong> <code>DESIGN.md</code> buộc phải chứa các định lượng tuyệt đối (Toán học, Mã màu Hex, Padding = 16px). Nếu file MD chỉ chứa những dòng văn xuôi chung chung (như "Làm cho nó trông sạch sẽ và chuyên nghiệp"), tính Stability sẽ lập tức đổ vỡ ở lần Scale prompt tiếp theo.</li>
      </ul>
    </div>
  </section>

  <section id="m6">
    <h2>6) Ứng dụng công nghệ này vào quy trình làm việc thực tế (Quan điểm cá nhân)</h2>
    <div class="card">
      <p>Khi đối chiếu bài toán này vào quá trình tham gia phát triển sản phẩm B2B tại doanh nghiệp của tôi, Google Stitch + thiết lập <code>DESIGN.md</code> (Hoặc kết nối MCP ra Claude Code) tạo ra một cuộc cách mạng quy trình thực sự:</p>
      <ol>
        <li><strong>Đóng vai trò như "Bản hợp đồng" giữa Product - Design - Dev:</strong> <code>DESIGN.md</code> không chỉ là file tĩnh, nó là thứ có thể đọc được (machine-readable) đối với cả con người và AI Agent. Một kỹ sư Front-end có thể ném file <code>DESIGN.md</code> này trực tiếp vào IDE để tự sinh ra bộ Variable CSS/Tailwind theo đúng chuẩn doanh nghiệp mà không cần bật Figma lên đo đạc.</li>
        <li><strong>Chuyển giao (Handoff) trơn tru hơn bằng MCP:</strong> Thay vì gửi màn hình UI và bắt Frontend Dev "xây lại từ đầu", luồng đi từ Stitch sang Claude Code thông qua giao thức MCP (như bài tham chiếu Bước 7, 8) phép cập nhật vi mô tự động. Dev chỉ lo phần Logic, AI lo việc ráp UI dựa trên MD Rules. Lợi ích tối đa cho đội ngũ năng lực Full-stack nhưng yếu về Visual.</li>
        <li><strong>Giải quyết bài toán "Sản xuất màn hình hàng loạt" trong B2B:</strong> Hệ thống quản trị nội bộ thường có đến hàng chục màn hình (CRUD, Logs, Settings) có cấu trúc na ná nhau. Khi đã chốt được 1 file <code>DESIGN.md</code> vững chắc, Product Manager hoàn toàn có thể dùng công cụ AI tự gõ Prompt để dàn dựng sẵn các màn hình chức năng phụ mà đảm bảo 100% không bị lệch Style với luồng chính.</li>
        <li><strong>Phòng chống phân mảnh (Fragmentation):</strong> Tôi đặc biệt thích ý tưởng đưa <code>DESIGN.md</code> vào quản lý phiên bản (Version Control - Git). Bất kỳ lúc nào công ty tái định vị thương hiệu (rebrand), chỉ cần sửa bộ biến số trong MD này, sau đó gọi AI cập nhật hàng loạt.</li>
      </ol>
      <p><strong>Kết luận cá nhân:</strong> Phương pháp này không đe dọa trực tiếp công việc của UX Designer, nhưng nó khai tử khâu "Tô màu - Dóng cột Pixel" lặp đi lặp lại. Nó trao cho các nhà Quản lý Sản phẩm (PM) và Kỹ sư phần mềm quyền năng biến ý tưởng hệ thống phức tạp thành các bản thử nghiệm (Mockup) đạt chất lượng thương mại chỉ sau vài dòng Prompt.</p>
    </div>
  </section>

  <div class="card">
    <h3>Danh sách Files của dự án (Project Assets)</h3>
    <ul>
      <li><code>design-md-b2b-system-mockup-blog.html</code> - Bài blog HTML báo cáo kết quả này.</li>
      <li><code>DESIGN.md</code> - Bộ quy tắc Design System của Product được trích xuất (Dành cho AI).</li>
      <li><code>HUONG-DAN-DEMO-CHUP-ANH.md</code> - File Checklist toàn bộ 12 bước quy trình hình ảnh.</li>
      <li><code>images/</code> - Thư mục chứa tài nguyên ảnh chứng minh thực tế.</li>
    </ul>
  </div>
</div>
"""

# Extract the header part before <div class="hero"> and script part after </div>\n\n<script>
parts = text.split('<div class="hero">', 1)
header = parts[0]
footer_parts = parts[1].rsplit('</div>\n\n<script>', 1)
footer = '\n<script>' + footer_parts[1]

final_html = header + new_body + footer

with open(html_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print("SUCCESS")
