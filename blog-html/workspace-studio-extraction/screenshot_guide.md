# Hướng Dẫn Chụp Ảnh Demo: Luồng Trích Xuất CV (12 Bước)

Để hoàn thiện bản thiết kế vận hành chuyên nghiệp (High-Fidelity), hãy thực hiện chụp 12 bức ảnh sau đây theo đúng thứ tự luồng công việc trong **Google Workspace Studio**:

---

## 🖥 GIAI ĐOẠN 1: ĐẦU VÀO DỮ LIỆU (DRIVE)

### Ảnh 1: Thư mục Nguồn (Source Folder)
- **Thao tác:** Chụp giao diện thư mục Google Drive (Incoming_CVs) chứa 3-5 tệp PDF Resume mẫu (tên giả).
- **Mục tiêu:** Hiển thị "nguyên liệu" đầu vào.

### Ảnh 2: Cấu hình Starter (Trigger)
- **Thao tác:** Trong Workspace Studio, chụp bước Starter: "When a file is added to folder" và chọn thư mục Incoming_CVs.

---

## 🖥 GIAI ĐOẠN 2: TRÍCH XUẤT THÔNG MINH (GEMINI)

### Ảnh 3: Soạn Prompt cho Gemini (Extraction Step)
- **Thao tác:** Chụp bước "Extract data with Gemini". Hiển thị rõ danh sách các trường cần lấy (Name, Email, Phone, Role, Skills, Preferences).
- **Lưu ý:** Sử dụng Prompt trích xuất JSON như trong blog để đạt độ chính xác cao nhất (xem code block ở Bước 3).

### Ảnh 4: Ánh xạ Biến (Variables Mapping)
- **Thao tác:** Chụp giao diện Variables. Hiển thị cách gán "Output" của Gemini vào các biến Flow (ví dụ: `var_CandidateEmail`).

---

## 🖥 GIAI ĐOẠN 3: LOGIC VẬN HÀNH (BRANCHING)

### Ảnh 5: Kiểm tra Trùng lặp (Lookup Sheet)
- **Thao tác:** Chụp cấu hình bước "Lookup Sheet row". Hiển thị việc tìm kiếm trong cột Email dựa trên biến `var_CandidateEmail`.

### Ảnh 6: Cấu hình Nhánh rẽ (Condition Step)
- **Thao tác:** Chụp bước "Condition". Hiển thị logic: If `LookupRow.index` > 0 -> Path A (Review/Update); If NOT -> Path B (Append).

### Ảnh 7: Ghi dữ liệu mới (Append Row)
- **Thao tác:** Chụp cấu hình bước "Add row to Google Sheets". Hiển thị danh sách các cột A, B, C... được gán với các biến tương ứng theo Schema đã định nghĩa (Name, Email, Phone, Role, Skills, Preference).

### Ảnh 8: Xử lý CV dạng ảnh (OCR Vision)
- **Thao tác:** Chụp màn hình quá trình "Run test" với 1 tệp CV scan (không có text layer). Hiển thị kết quả Gemini vẫn đọc và hiểu được nội dung.

---

## 🖥 GIAI ĐOẠN 4: THÔNG BÁO & KIỂM CHỨNG (OUTPUT)

### Ảnh 9: Thông báo HR (Gmail Step)
- **Thao tác:** Chụp cấu hình bước gửi email. Hiển thị tiêu đề động: "Phát hiện ứng viên mới: {var_CandidateName}".

### Ảnh 10: Lịch sử vận hành (Flow Logs)
- **Thao tác:** Chụp tab "History" hoặc "Logs" của Workspace Studio. Hiển thị các lượt chạy thành công với trạng thái "Succeeded".

### Ảnh 11: Đối soát 10 điểm (QA Lab)
- **Thao tác:** Chia đôi màn hình (Side-by-side): Bên trái là tệp PDF CV gốc, bên phải là hàng dữ liệu tương ứng trong Google Sheets. Vẽ vòng tròn đỏ vào các điểm khớp nhau (Email, Phone, Title).

### Ảnh 12: Bảng Talent Tracker tổng thể
- **Thao tác:** Chụp toàn bộ Google Sheets sau khi đã tự động trích xuất xong 5-10 CV. Các cột dữ liệu sạch sẽ, đồng nhất theo Schema A-F.
