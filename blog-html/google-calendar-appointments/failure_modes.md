# Failure Modes & Validation - Google Calendar Appointment Schedules

Tài liệu này liệt kê 3 tình huống lỗi (Failure modes) thực tế mà bạn có thể gặp phải khi thiết lập lịch phỏng vấn đa hội đồng và cách để "debug" chúng.

---

## 🚩 Lỗi 1: Co-host Vẫn Bị Trùng Lịch (Double Booking)
- **Nguyên nhân:** Người tạo lịch không có quyền xem "Busy" (Bận) trên lịch của Co-host.
- **Cách Kiểm Chứng (Validation):**
  1. Mở thiết lập Appointment Schedule.
  2. Nếu cạnh tên Co-host có biểu tượng chấm than (!) hoặc thông báo "Calendar not shared", nghĩa là hệ thống không thể quét lịch bận của họ.
- **Cách Khắc Phục:** Yêu cầu Co-host vào cài đặt Google Calendar của họ > Chọn lịch cá nhân > **Share with specific people** > Thêm email người tạo lịch với quyền ít nhất là **"See only free/busy (hide details)"**.

## 🚩 Lỗi 2: Múi Giờ Bị Lệch (Time Zone Disparity)
- **Nguyên nhân:** Ứng viên (ví dụ ở nước ngoài) không nhận diện được múi giờ địa phương, dẫn đến việc đặt lịch nhầm sáng thành tối.
- **Cách Kiểm Chứng (Validation):**
  1. Mở trang Booking Page bằng trình duyệt ẩn danh (Incognito).
  2. Nhìn vào góc dưới bên trái. Nếu múi giờ hiển thị không tự động nhảy theo múi giờ của máy tính, hệ thống đang bị khóa múi giờ cố định.
- **Cách Khắc Phục:** Trong thiết lập **Scheduling configuration**, đảm bảo mục múi giờ đang để trạng thái **"User's local time zone"** thay vì cố định một múi giờ duy nhất.

## 🚩 Lỗi 3: Lịch Cá Nhân (Personal) vs Lịch Công Việc (Work)
- **Nguyên nhân:** Co-host có thói quen ghi chú lịch đi bác sĩ, đón con vào lịch cá nhân (Personal/Private email) nhưng HR chỉ thêm email công việc (Workspace) vào Co-host.
- **Cách Kiểm Chứng (Validation):**
  1. Yêu cầu Co-host tự check trang Booking link. Nếu khung giờ họ bận việc riêng vẫn hiện ra cho ứng viên đặt, nghĩa là Google chưa quét được lịch cá nhân của họ.
- **Cách Khắc Phục:** 
  - Cách A: Co-host cần Share lịch cá nhân của mình cho email công việc.
  - Cách B: Trong Appointment Schedule, người tạo lịch có thể thêm cả 2 email của Co-host đó vào (tuy nhiên cách này sẽ tốn slot Co-host). Tốt nhất là sử dụng tính năng **Syncing multiple calendars** có sẵn trong Workspace.
