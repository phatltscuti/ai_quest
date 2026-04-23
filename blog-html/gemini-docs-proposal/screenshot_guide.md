# Hướng Dẫn Chụp Ảnh Demo (Screenshot Guide)

Để bài blog `index.html` hoàn thiện, bạn cần chuẩn bị 6 bức ảnh minh họa. Dưới đây là hướng dẫn chi tiết:

## Các Ảnh Cho Action 1: UI Help me write (Tạo bản nháp)
Đây là quy trình tạo ra tài liệu Proposal cốt lõi, gồm 4 bước nối tiếp nhau:

- **Ảnh 1:** 
  - *Thao tác:* Mở 1 trang Google Docs mới tinh. Di chuột lại gần lề trái hoặc dòng đầu tiên để biểu tượng cây bút chì có ngôi sao ("Help me write") hiện ra, KHÔNG CLICK vội, để chuột hiển thị chữ "Help me write" (Tooltip).
  - *Chụp ảnh:* Chụp đoạn lề văn bản có tooltip/nút bút chì này để thay thế `[Chèn Ảnh 1]`.
  
- **Ảnh 2:**
  - *Thao tác:* Click vào nút bút chì ở trên. Popup hộp thoại Help me write mở ra. Bạn dán đoạn prompt 1 vào hộp: `Write a formal Project Kickoff Document for a Product Management Web Application. Structure must include: Executive Summary, Project Scope, Timeline, Budget & Risks. Use the following details: Goal: Build a web app to manage inventory, pricing, and suppliers. Timeline: Starts Dec 1, 2026, duration 4 months. Budget: $30,000 for development and hosting. Key Risk: Delayed integration with the legacy ERP system.`
  - *Chụp ảnh:* Chụp toàn bộ khung màn hình UI có popup chứa prompt vừa nhập và có nút "Create" màu xanh bên dưới. Thay thế cho `[Chèn Ảnh 2]`.
  
- **Ảnh 3:**
  - *Thao tác:* Nhấn nút **Create**. Chờ Docs chạy xong, hộp thoại sẽ phình to ra và chứa toàn bộ văn bản "Project Kickoff..." bên trong, ở dưới cùng là 2 nút "Insert" và "Refine".
  - *Chụp ảnh:* Chụp khoảnh khắc popup đang hiển thị kết quả (chưa insert vào trang). Thấy rõ chữ "Insert". Thay thế cho `[Chèn Ảnh 3]`.

- **Ảnh 4:**
  - *Thao tác:* Nhấn nút **Insert**.
  - *Chụp ảnh:* Chụp toàn bộ giao diện Google Docs cho thấy văn bản (đã được bôi đậm các Heading rất rõ ràng) vừa chèn lên. Thay thế cho `[Chèn Ảnh 4]`.

## Ảnh 5: Tính năng Rewrite & Formalize (Action 2)
- **Chuẩn bị:** Sử dụng tiếp file Docs vừa thành hình ở bước trên.
- **Thao tác:**
  1. Dùng chuột bôi đen toàn bộ đoạn "Executive Summary".
  2. Một biểu tượng bút chì (Refine) nhỏ sẽ hiện ra trôi nổi cạnh dòng bôi đen -> Click vào đó.
  3. Nhập Prompt 2 vào ô **Modify with a prompt** (hoặc bấm chọn thiết lập sẵn **More formal**):
     `Make this executive summary more formal, concise and impactful for C-level executives.`
  4. Chờ đoạn văn bản mới (formal hơn) được sinh ra bên dưới popup.
- **Chụp ảnh:** Chụp khoảnh khắc popup sinh ra có chứa cả nút **Replace** / **Insert** / bản cũ gạch ngang (nếu hiển thị). Thay thế hình này vào chỗ `[Chèn Ảnh 5]`.

## Ảnh 6: Trích xuất bảng Action items từ Side Panel (Action 3)
- **Chuẩn bị:** Cùng file Docs đó.
- **Thao tác:**
  1. Nhấn vào biểu tượng ngôi sao lấp lánh (Ask Gemini) ở góc trên cùng bên phải màn hình để mở **Gemini Side Panel**.
  2. Nhập vào ô chat của Side Panel prompt 3:
     `Extract the project timeline and milestones from the document into a table with 3 columns: Phase, Duration, and Deliverables.`
  3. Đợi Gemini đọc file và xuất ra một bảng (table) ngay trong Side Panel chatbox.
  4. Move trỏ chuột vào bảng vừa xuất hiện, click vào nút `Insert` để chèn vào bên trong nội dung Docs.
- **Chụp ảnh:** Chụp chế độ màn hình rộng để thấy cả Layout Docs bên trái (đang chứa bảng vừa insert) và cửa sổ Gemini Side Panel bên phải đang bật hiển thị lời chat/bảng kết quả. Thay thế vào mục `[Chèn Ảnh 6]`.
