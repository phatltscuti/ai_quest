# Kịch Bản Demo: Trình Diễn Báo Cáo Kickoff Dự Án Web Quản Lý Sản Phẩm Bằng Gemini

Kịch bản này được thiết kế để bạn quay video (screencast) hoặc trình bày trực tiếp (live demo) trước team, mô phỏng quá trình tạo "Web App Project Kickoff Doc" thực tế.

## 🕧 Chuẩn Bị Trước Khi Demo
1. Mở sẵn trình duyệt (Chrome/Edge), đăng nhập vào tài khoản Google Workspace có bật bản quyền Gemini Advanced / Duet AI.
2. Tạo trước 1 thư mục trong Google Drive tên là `Demo - Web App Kickoff`.
3. Mở sẵn file lưu các Prompt (Ghi chú hoặc Notepad) để có thể Copy/Paste cho nhanh trong lúc demo.

---

## 🎬 Act 1: Đối mặt với "Trang giấy trắng"
- **Nhịp độ:** Chậm, thư thả. Điểm nhấn là sự khó khăn khi bắt đầu viết.
- **Lời dẫn (Voiceover):** "Chào mọi người. Hôm nay mình sẽ demo cách cực nhanh để dọn dẹp hội chứng sợ trang giấy trắng khi phải viết Kickoff Document cho một dự án làm Web quản lý sản phẩm. Bình thường mình sẽ copy template và sửa từng chữ..."
- **Hành động:** 
  1. Mở `docs.new` để tạo file mới.
  2. Click thẳng vào nút **Help me write** (biểu tượng bút chì) ở dòng đầu tiên.
  3. Paste Prompt 1: `Write a formal Project Kickoff Document for a Product Management Web Application...` (chứa các thông tin về ngân sách, rủi ro tích hợp ERP).
  4. Nhấn **Create** và giả vờ dang tay ra khỏi bàn phím để mọi người thấy AI đang tự động viết.
  5. Cuộn dọc (scroll) kết quả để khán giả thấy cấu trúc báo cáo rất chuẩn chỉnh. Sau đó nhấn **Insert**.

## 🎬 Act 2: Tác động ngữ điệu (Tone & Style)
- **Nhịp độ:** Nhanh, dứt khoát.
- **Lời dẫn:** "Bản nháp này khá đủ ý rồi, nhưng phần Executive Summary đọc hơi bình dân và chưa đủ độ 'impact' (sức nặng) để gửi cho C-level. Mình sẽ dùng tính năng Refine để biến tấu nó."
- **Hành động:**
  1. Bôi đen đoạn Executive Summary hiện tại.
  2. Click popup `Refine` (Biểu tượng bút chì lấp lánh).
  3. Gõ vào ô **Modify with a prompt**: `Make this executive summary more formal, concise and impactful for C-level executives.`
  4. Trình diễn kết quả mới. Đọc highlight 1 đoạn nhỏ để thấy cách dùng từ đã chuyên nghiệp hơn (ví dụ: 'comprehensive application' thay vì 'new web app').
  5. Nhấn **Replace**.

## 🎬 Act 3: Xử lý thông tin phức tạp (Side Panel)
- **Nhịp độ:** Vừa phải, nhấn mạnh tính năng Context-aware của Side Panel so với Help me write.
- **Lời dẫn:** "Dưới phần Timeline, dạng text liệt kê theo tháng rất khó hình dung. Mình muốn chuyển nó thành một bảng cho trực quan mà không cần kẻ bảng và copy-paste thủ công."
- **Hành động:**
  1. Mở **Gemini Side Panel** ở góc trên cùng bên phải.
  2. Nhập Prompt: `Extract the project timeline and milestones from the document into a table...`
  3. Để Gemini xuất bảng ngay trong chat.
  4. Trỏ chuột vào bảng trên đoạn chat, bấm biểu tượng **Insert** và chọn ví trí trong trang Docs. Bảng ngay lập tức bay vào văn bản.

## 🎬 Act 4: Đánh giá chất lượng (Quality Gate & Conclusion)
- **Nhịp độ:** Rõ ràng, tin cậy. Nhấn mạnh việc AI trung thực với Fact ban đầu.
- **Lời dẫn:** "Để ý lại các bạn sẽ thấy: Cấu trúc số liệu ban đầu mình đưa cho Gemini là ngân sách $30,000, thời gian 4 tháng và rủi ro trễ tiến độ tích hợp ERP. Output của văn bản trung thành hoàn toàn 100% với các thông tin gốc này, hệ thống không hề bịa đặt (hallucinate) thêm ngôn ngữ lập trình hay chi phí vô lý. Rất an toàn để sử dụng."
- **Hành động:** Dùng chuột bôi đen hoặc chỉ vào các khoản tiền / tháng / Risk ERP trong file docs. Đổi tên file Docs thành `[Final] Web App Kickoff` và tắt trình duyệt. Phân đoạn kết thúc.
