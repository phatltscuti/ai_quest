# Hướng dẫn chi tiết từng thao tác chụp ảnh demo thiết kế B2B bằng Google Stitch

File này cung cấp hướng dẫn "cầm tay chỉ việc" từng click chuột, từng phím bấm để bạn có thể tự mình tạo ra và chụp lại 12 bức ảnh demo quá trình sử dụng Google Stitch và DESIGN.md. Nội dung Prompt trong hướng dẫn đã được đồng bộ chuẩn xác với cấu trúc trong bài Blog HTML.

**Lưu ý quan trọng trước khi bắt đầu:**
- Sử dụng công cụ cắt ảnh của máy tính (Ví dụ: Nhấn tổ hợp phím `Windows + Shift + S` trên Windows hoặc `Cmd + Shift + 4` trên Mac) để chọn vùng màn hình cần chụp.
- Mở sẵn thư mục `C:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\images\` trên máy tính.
- Mỗi khi cắt ảnh xong, hệ thống lưu Clipboard của bạn sẽ có ảnh. Hãy mở thư mục `images/` trên ra, ấn Paste (`Ctrl + V`), rồi đổi tên nó thành đúng các tên dạng `.png` theo yêu cầu bên dưới (hoặc dán vào Paint để Save As cho chắc chắn). Các bức ảnh đúng tên sẽ tự động được gắp (nhúng) vào bài Blog!

---

## Danh sách 12 bước thao tác & chụp ảnh

### 1. Thao tác chụp `step-01-stitch-home.png`
- **Bước 1:** Mở trình duyệt web (Chrome/Edge), gõ địa chỉ `https://stitch.withgoogle.com` và nhấn phím `Enter`.
- **Bước 2:** Đăng nhập bằng tài khoản Google của bạn.
- **Bước 3:** Đợi trang chủ tải xong. Trên màn hình chính bạn sẽ thấy một khung nhập liệu rỗng. **Lưu ý: Hãy chắc chắn bạn đang chọn chế độ "Web" (hoặc Desktop)** vì trang Dashboard B2B cần không gian màn hình rộng để hiển thị bảng dữ liệu và menu trái, tuyệt đối không chọn "App" (Mobile).
- **Bước 4 (Chụp ảnh):** Bấm tổ hợp phím `Windows + Shift + S`, quét chọn **toàn bộ cửa sổ trình duyệt** để lấy cả thanh địa chỉ, nút chế độ Web đang được sáng lên và khung nhập liệu rỗng.
- **Bước 5:** Lưu thành tên file: `step-01-stitch-home.png`.

### 2. Thao tác chụp `step-02-direction-brief.png`
- **Bước 1:** Thu phần mềm trình duyệt (Chrome) hẹp lại một chút (không phóng to toàn màn hình).
- **Bước 2:** Mở ứng dụng **Notepad** có sẵn trên Windows (Bấm phím `Windows`, gõ chữ "Notepad" và enter).
- **Bước 3:** Gõ đúng nội dung Brief (Policy) sau vào chính Notepad:
  ```text
  - Ai sử dụng: Operation manager, support lead
  - Mục tiêu: Theo dõi sức khỏe hệ thống, xử lý incident
  - Cảm giác: Trực quan, tin cậy, control tower
  - Tránh: Lòe loẹt, vui nhộn, đồ họa Marketing
  ```
- **Bước 4 (Chụp ảnh):** Di chuyển cửa sổ Notepad đặt đè lên một góc cửa sổ trình duyệt Google Stitch đang mở. Bấm `Windows + Shift + S` quét chọn hẹp lấy cả cửa sổ Notepad và một bệ nhỏ của Stitch nền phía sau. 
- **Bước 5:** Lưu tên file: `step-02-direction-brief.png`.

### 3. Thao tác chụp `step-03-first-prompt.png`
- **Bước 1:** Quay lại màn hình chính của Google Stitch. Đảm bảo thanh tuỳ chọn thiết bị đang được đặt ở **Web** (Desktop). Sau đó, click chuột vào ô nhập lệnh (Prompt) to nằm ở giữa phân minh.
- **Bước 2:** Bôi đen trọn vẹn 100% khối chữ tiếng Anh dưới đây, bấm `Ctrl + C` và dán `Ctrl + V` vào ô đó: 

```text
Design a desktop B2B system management dashboard for enterprise operations.
Audience: operation managers and compliance teams.
Main sections:
- Top navigation with environment badge and global search
- Left side navigation (Overview, Incidents, Users, Integrations, Billing, Audit)
- KPI row: Uptime, Active Incidents, Queue Backlog, SLA Breach Risk
- Incident table with severity, owner, status, updated time
- Right action panel for "Assign owner", "Escalate", "Resolve"
Style: professional, standard data density, high readability.
Avoid playful visuals and avoid marketing-style hero blocks. Focus on utility.
```

- **Bước 3 (Chụp ảnh):** Kéo chuột định nhấn đến nút có hình "Mũi tên bay/Generate" nhưng **ĐỪNG CLICK VỘI**. Bấm `Windows + Shift + S` và khoanh vùng chụp lại cửa sổ nhập liệu chứa đoạn chữ trên và cái nút gửi đang sẵn sàng ấn. 
- **Bước 4:** Lưu tên file: `step-03-first-prompt.png`.

### 4. Thao tác chụp `step-04-rough-mockup.png`
- **Bước 1:** Bây giờ thì hãy click chuột trái vào cái nút Gửi (Mũi tên sinh thiết kế) hoặc nhấn phím `Enter`.
- **Bước 2:** Đợi AI của Stitch xoay vòng khoảng 15-30 giây. Nó sẽ tự nhả ra các màn hình màu sắc ban đầu.
- **Bước 3:** Đưa chuột ra vùng khoảng xám của Infinite Canvas (Bảng vẽ vô cực). Lăn bánh xe con chuột lùi lại (Scroll down) hoặc bấm giữ `Ctrl + Lăn chuột` để thu nhỏ toàn màn hình (Zoom out) sao cho vào một khung ảnh thấy hết toàn bộ các bảng, các thẻ KPI và thanh menu hệ thống vừa vẽ ra.
- **Bước 4 (Chụp ảnh):** Bấm `Windows + Shift + S`, khoanh vuông quét toàn bộ khu Canvas với bao quát hệ thống nháp trên. 
- **Bước 5:** Lưu tên file: `step-04-rough-mockup.png`.

### 5. Thao tác chụp `step-05-iteration-prompts.png`
- **Bước 1:** Đưa trỏ chuột click thẳng vào cái Bảng Incident (Table) do AI vừa tạo trên Canvas.
- **Bước 2:** Ngay khi bạn click, hệ thống sẽ nổi lên một thanh công cụ (Widget) hình viên thuốc nhỏ, hoặc một ô sửa prompt (sửa cục bộ) ngay mép trên của phần tử.
- **Bước 3:** Gõ lửng lo đoạn chữ sau vào ô nhỏ đấy: *"Make the status column texts use warning colors (red/orange)"*. Gõ xong đừng ấn ngay.
- **Bước 4 (Chụp ảnh):** Bấm tổ hợp `Windows + Shift + S`, khoanh đúng khu vực bao lấy thanh công cụ Widget mini này kèm đoạn dòng kẻ bị đè ở dưới. 
- **Bước 5:** Lưu tên file: `step-05-iteration-prompts.png`. (Chụp xong thì hãy nhấn Enter cho hệ thống xử lý tiếp).

### 6. Thao tác chụp `step-06-design-system-board.png`
- **Bước 1:** Cửa sổ trò chuyện luồng chính của hệ thống (Text chat chung/Thanh sidebar) nằm ở bên trái hoặc panel dưới cùng. Ấn vào vị trí đó.
- **Bước 2:** Copy và gửi chính xác đoạn lệnh Design System bên dưới (Giống như trong file Blog): 

```text
From this B2B dashboard draft, create a reusable enterprise design system.
Organize into:
- Color roles (Primary, Warning, Critical, Backgrounds)
- Typography (Headers, Body, Dense Table Data)
- Spacing (Rhythm for high-density cards)
- Components (nav, KPI cards, table, status badges, action area)
- Layout principles (Grid distribution, Sidebar behavior)
Prioritize consistency, auditability, and enterprise clarity over decoration. Generate a DESIGN.md containing these precise metrics and hex codes.
```

- **Bước 3:** Đợi AI xử lý 10s. Bạn sẽ thấy không gian Canvas chớp hiển thị thêm các Artboard mới hoàn toàn bên cạnh bản cũ. Artboad này chứa chi chít các bảng vuông mã màu sắc, và các kiểu hiển thị Font chữ to nhỏ (Typography).
- **Bước 4 (Chụp ảnh):** Đưa con trỏ (Giữ Spacebar kéo chuột) sang ngay trước khu vực vừa vẽ đó. Nhấn `Windows + Shift + S` bao vùng chụp trọn vẹn cụm bảng màu của Design System Board. 
- **Bước 5:** Lưu tên file: `step-06-design-system-board.png`.

### 7. Thao tác chụp `step-07-design-md-panel.png`
- **Bước 1:** Nhìn vào khung phản hồi Chat của hệ thống nơi tạo ra khung thiết kế trên (hoặc gõ lệnh "Generate the DESIGN.md code").
- **Bước 2:** Hệ thống xuất ra một cục mã (Code Block Markdown) nền màu đậm, bên trong toàn chứa các thẻ `#` và `##` cùng mã màu Hex, với nút Copy nhỏ ở góc của cục Code.
- **Bước 3 (Chụp ảnh):** Bấm `Windows + Shift + S`, lấy con trỏ đóng khung quét chọn đúng cục khung sẫm màu chứa mã code Design System này (chụp rõ khối Code). 
- **Bước 4:** Lưu tên file: `step-07-design-md-panel.png`.

### 8. Thao tác chụp `step-08-apply-design-system.png`
- **Bước 1:** Bôi đen chọn lại khung Frame giao diện B2B bạn làm nháp lúc đầu (Rough mockup của bước 4).
- **Bước 2:** Tại khung Chat chung, copy và dán đoạn lệnh sau: 

```text
Apply the generated design system (from the DESIGN.md rules) strictly back to this dashboard screen.
Align the heading hierarchy, spacing rhythm, table density, and component consistency automatically.
Keep the information architecture (KPIs, Tables, Sidemenu) exactly the same, only homogenize the visual language.
```

- Nhấn nút Mũi Tên Gửi.
- **Bước 3:** Quan sát Canvas, nó đang tự động cân bằng hệ màu, dóng cột theo đúng bộ số Hex đã định hình. 
- **Bước 4 (Chụp ảnh):** Chỉnh khoảng cách trên màn hình đưa 2 khung đặt trên cùng 1 hàng: Khung Design System (Bảng màu) nằm bên Trái và Màn hình Dashboard đang được cập nhật đặt bên Phải. Nhấn `Windows + Shift + S` và quét ngang lấy sự so sánh đó!
- **Bước 5:** Lưu tên file: `step-08-apply-design-system.png`.

### 9. Thao tác chụp `step-09-before-after.png`
*Bước này có thể làm bằng phần mềm làm ảnh trên máy.*
- **Bước 1:** Mở phần mềm **Paint** trên Windows lên (Nhấn nút Start, gõ Paint > Enter).
- **Bước 2:** Bấm `File > Open` và chọn bức ảnh `step-04-rough-mockup.png` (bản vẽ nháp ban đầu) đã lưu. Kéo nó để sang nửa bờ trái. 
- **Bước 3:** Vào lại thư mục gắp file màn hình vừa được hoàn thiện tại Bước 8, kéo dán qua Paint dặt nửa bờ bên phải. Gõ thêm 1 dòng text ghi "Trước" và "Sau" cho dễ nhìn. 
- **Bước 4 (Chụp ảnh / Lưu trữ):** Trong Paint bấm `File > Save As`, lưu trực tiếp thành file: `step-09-before-after.png` vào thư mục `images/`.

### 10. Thao tác chụp `step-10-prototype-check.png`
- **Bước 1:** Trên giao diện duyệt của Google Stitch, nhìn lên góc cao cùng bên phải màn hình. Tìm và click nút có hình tam giác Play (`▶`) hoặc nút có text **"Preview"**.
- **Bước 2:** Chế độ thay đổi sang trang web tĩnh Xem trước. Di chuột "rơi" nhẹ vào nút "Resolve" trong bảng UI. Nút đó sẽ phản hồi (đổi màu đậm hơn - Hiệu ứng Hover). Điểm mấu chốt là phải đang "trỏ chuột" vào nó.
- **Bước 3 (Chụp ảnh đặc biệt):** Giữ yên tay ở đó không di chuyển để hiệu ứng màu còn hoạt động, dùng tay kia bấm thẳng phím **`Print Screen / PrtScn`** trên rãnh cao nhất của bàn phím. Nếu dùng laptop bấm `Fn + PrtScn` chụp trọn cả con trỏ chuột. Dán ra Paint và crop lấy chi tiết đó.
- **Bước 4:** Lưu tên file: `step-10-prototype-check.png`.

### 11. Thao tác chụp `step-11-export-or-handoff.png`
- **Bước 1:** Quay lại môi trường Build thoát chế độ Preview. Bấm vào nút **"Export"** nằm sát góc trên cùng bên phải màn hình.
- **Bước 2:** Một bảng chọn (Panel) sẽ trượt ra chứa các tùy chọn xuất định dạng (Format) như: AI Studio, Figma, .zip, Code to Clipboard, MCP... Bạn hãy click chọn vào mục **"Code to Clipboard"** (hoặc **.zip** / **MCP** tùy chọn) để minh họa cho việc trích xuất mã nguồn (Handoff).
- **Bước 3 (Chụp ảnh):** Bấm `Windows + Shift + S`, cắt chọn riêng khu vực khung menu Export dọc chứa các tùy chọn chức năng này. 
- **Bước 4:** Lưu tên file: `step-11-export-or-handoff.png`.

### 12. Thao tác chụp `step-12-final-result-local.png`
- **Bước 1:** Thu nhỏ Chrome xuống thanh Taskbar. Mở phần mềm IDE **Visual Studio Code (VS Code)** của máy tính.
- **Bước 2:** Vào menu `File > Open Folder...`. Dẫn đường dẫn vào cây thư mục của bạn: `C:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup`. Chọn ổ thư mục đó.
- **Bước 3:** Nhìn thanh Menu cây danh sách dọc (Sidebar) bên Trái. Bấm biểu tượng tam giác sổ thư mục `images/` xuống. Bạn sẽ thấy file 12 ảnh .png đang hiển thị đồng bộ.
- **Bước 4 (Chụp ảnh):** Ấn `Windows + Shift + S`, khoanh vuông đóng khung riêng cái cột Menu Cây thư mục bên Trái này.
- **Bước 5:** Lưu tên file kết thúc chu trình: `step-12-final-result-local.png`. 

*(Đóng file lại, bỏ 12 ảnh đó vào thư mục images/ và chạy file HTML bài blog lên để xem trải nghiệm Tự Động Gắp Ảnh!)*
