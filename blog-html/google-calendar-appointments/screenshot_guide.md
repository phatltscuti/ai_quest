# Hướng Dẫn Chụp Ảnh Demo (12 Bước Quy Trình Full Lifecycle)

Để minh họa cho bản thiết kế vận hành chuyên nghiệp, hãy thực hiện chụp 12 bức ảnh sau đây theo đúng thứ tự luồng công việc:

---

## 🖥 GIAI ĐOẠN 1: THIẾT LẬP HỘI ĐỒNG (TRANG 1)

### Ảnh 1: Khởi tạo Lịch hẹn (Create)
- **Thao tác:** Google Calendar > Nút **Create (+)** > Chọn **Appointment schedule**.

### Ảnh 2: Thêm Người Phỏng Vấn (Co-hosts)
- **Thao tác:** Tại mục **Co-hosts**, nhập email của co-hosts tham gia hội đồng. [ĐÃ CÓ - setup_page_1.png]

### Ảnh 3: Cấu hình Cửa sổ đặt lịch (Scheduling Window)
- **Thao tác:** Thiết lập số ngày đặt trước (60 ngày) và thời gian báo trước tối thiểu (4 giờ). [ĐÃ CÓ - setup_page_1.png]

### Ảnh 4: Thiết lập Vùng bảo vệ (Booked Appointment Setting)
- **Thao tác:** Cài đặt **Buffer time** (30 phút) và **Max bookings per day** (3 ca). [ĐÃ CÓ - setup_page_1.png]

### Ảnh 5: Kiểm tra Lịch trống (Calendar Availability)
- **Thao tác:** Tích chọn lịch của tất cả Co-hosts để AI quét giờ trống chung. [ĐÃ CÓ - setup_page_1.png]

---

## 🖥 GIAI ĐOẠN 2: BẢO MẬT & NỘI DUNG (TRANG 2)

### Ảnh 6: Biểu mẫu & Xác minh (Booking Form & OTP Setup)
- **Thao tác:** Thiết lập 3 biến (First name, Last name, Email address) và chọn **Email verification required**. [ĐÃ CÓ - setup_page_2.png]

---

## 🖥 GIAI ĐOẠN 3: VẬN HÀNH & XÁC THỰC (LIVE OPERATION)

### Ảnh 7: Soạn Email theo Template (Outreach Email)
- **Thao tác:** Mở Gmail, soạn thư theo mẫu, dán link đặt lịch vào nội dung mail để gửi cho ứng viên.

### Ảnh 8: Ứng viên chọn giờ (Candidate Booking UI)
- **Thao tác:** Ứng viên click vào link, chọn ngày/giờ và nhập 3 biến thông tin.

### Ảnh 9: Nhập mã xác minh (Email OTP Verification)
- **Thao tác:** Ứng viên nhập mã OTP 6 chữ số được gửi về email để xác nhận danh tính.

### Ảnh 10: Thông báo Đặt lịch Thành công (Success confirmation)
- **Thao tác:** Màn hình xác nhận sau khi ứng viên đã hoàn tất đặt chỗ thành công.

---

## 🖥 GIAI ĐOẠN 4: KIỂM TRA ĐỒNG BỘ (CALENDAR SYNC)

### Ảnh 11: Kiểm tra Lịch cá nhân (Recruiter Calendar Check)
- **Thao tác:** Kiểm tra trên lịch của người tuyển duyệt, đảm bảo sự kiện phỏng vấn đã được thêm tự động.

### Ảnh 12: Email Phản hồi Thành công (Final Confirmation Email)
- **Thao tác:** Kiểm tra hòm thư để thấy email xác nhận lịch hẹn (Confirmation) tự động từ Google.
