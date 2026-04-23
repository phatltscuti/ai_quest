# Hướng Dẫn Chụp Ảnh Demo: Luồng Tự Động Tạo Bản Nháp Gmail

Để hoàn thiện bản thiết kế vận hành cho hệ thống **Gmail Draft Automation**, hãy thực hiện chụp các bức ảnh sau đây trong **Google Workspace Studio**:

---

## 🖥 GIAI ĐOẠN 1: LỌC EMAIL (FILTERING)

### Ảnh 1: Cấu hình Starter Gmail
- **Thao tác:** Trong Workspace Studio, chụp bước Starter: "When a new email is received". 
- **Dữ liệu:** Nhập chuỗi query lọc nâng cao: `in:inbox is:unread -from:aiquest.com subject:("AI Expo" OR "Collaboration" OR "Báo giá")`.
- **Mục tiêu:** Hiển thị khả năng lọc chính xác đối tượng cần xử lý.

---

## 🖥 GIAI ĐOẠN 2: SUY LUẬN NGỮ CẢNH (REASONING)

### Ảnh 2: Bước Trích xuất & Tạo nháp với Gemini
- **Thao tác:** Chụp cấu hình bước "Draft a reply" hoặc bước Gemini Extract. Hiển thị rõ Prompt yêu cầu tóm tắt lịch sử (Thread history) và đề xuất 3 câu hỏi làm rõ.
- **Lưu ý:** Prompt nên nhấn mạnh việc không được "ảo tưởng" thông tin không có trong thread.

---

## 🖥 GIAI ĐOẠN 3: LƯU TRỮ & GÁN NHÃN (ACTION)

### Ảnh 3: Minh chứng Bản nháp trong Gmail
- **Thao tác:** Chụp màn hình thư mục "Drafts" trong Gmail. Hiển thị một email nháp vừa được tạo tự động với nội dung chuyên nghiệp.
- **Dữ liệu:** Kiểm tra xem nhãn `Draft-created` đã được gán tự động chưa.

---

## 🖥 GIAI ĐOẠN 4: XỬ LÝ NGOẠI LỆ (EXCEPTIONS)

### Ảnh 4: Cấu hình Nhánh rẽ (Condition Step)
- **Thao tác:** Chụp bước "Condition". Hiển thị logic: Nếu tiêu đề chứa "Complaint" hoặc "Legal" -> Đi tới nhánh "Send Chat Message".
- **Mục tiêu:** Hiển thị tính an toàn của hệ thống khi đối mặt với email nhạy cảm.

### Ảnh 5: Thông báo Google Chat (Chat Alert)
- **Thao tác:** Chụp màn hình Google Chat nhận được thông báo từ Workspace Studio: "Phát hiện email khiếu nại từ {SenderName}. Cần người duyệt gấp!".

---

## 🖥 GIAI ĐOẠN 5: CHẤT LƯỢNG & ĐỐI SOÁT (QA)

### Ảnh 6: Đối soát Tính xác thực (QA Lab)
- **Thao tác:** Chia đôi màn hình (Side-by-side): Bên trái là Thread email gốc của khách hàng, bên phải là nội dung Bản nháp AI vừa tạo. 
- **Mục tiêu:** Dùng các vòng tròn màu khác nhau để đánh dấu 5 điểm dữ liệu khớp nhau hoàn toàn (Tên booth, câu hỏi API, lịch họp...).

### Ảnh 7: Hệ thống Nhãn dán tổng thể
- **Thao tác:** Chụp danh sách email trong Inbox với các nhãn dán màu sắc khác nhau: `Draft-created` (Xanh), `Needs-review` (Vàng), `Important` (Đỏ).
- **Mục tiêu:** Hiển thị sự ngăn nắp và khoa học trong quy trình xử lý email số lượng lớn.
