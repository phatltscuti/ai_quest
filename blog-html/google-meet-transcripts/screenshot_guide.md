# Hướng Dẫn Chụp Ảnh Demo (Screenshot Guide)

Tài liệu này hướng dẫn người thực hiện (QA, Tester, hoặc PM) cách chụp các màn hình để thay thế cho các `[image-placeholder]` trong file `index.html`. Mục tiêu là **chứng minh bằng chứng trực quan** về việc Google Meet transcript hoạt động đúng yêu cầu.

---

## 📸 Ảnh 1: Khởi động Transcription (Start transcription)
**Vị trí chèn:** Dưới mục *1. Kích hoạt tính năng Transcription trong Google Meet*

**Cách thực hiện:**
1. Mở một Google Meet (có đăng nhập bằng tài khoản Workspace có hỗ trợ Transcript).
2. Tốt nhất là mời 1-2 tài khoản khác vào (để tạo bối cảnh có nhiều người tham gia).
3. Click vào biểu tượng **Activities** ở góc dưới cùng bên phải.
4. Chọn **Transcripts** và click nút **Start Transcription**.
5. Khi UI báo "Transcription is starting" kèm theo biểu tượng Transcript chớp xanh góc trái trên cùng, hãy chụp màn hình.

**Yêu cầu bức ảnh:**
- Thấy rõ được bảng Activities có nút **Stop transcription** (cho thấy nó đang bật).
- Thấy được **biểu tượng báo hiệu** đang ghi chép (indicator) ở góc trên bên trái màn hình.

---

## 📸 Ảnh 2: Tìm file trên Google Drive (Google Drive Location)
**Vị trí chèn:** Dưới mục *2. Xác minh việc lưu Transcript vào Google Drive*

**Cách thực hiện:**
1. Kết thúc cuộc gọi ở Ảnh 1 (ấn nút Rời khỏi và Cúp máy cho tất cả).
2. Chờ khoảng 1-2 phút, truy cập Google Drive.
3. Đi vào thư mục **Meet Recordings**. Bạn sẽ thấy một file Google Doc có tên kiểu `[Tên cuộc họp] (YYYY-MM-DD) - Transcript`.
4. Tìm kiếm từ khóa `Type: Docs "Transcript"` trên thanh tìm kiếm của Drive.
5. Chụp màn hình toàn bộ cửa sổ Drive.

**Yêu cầu bức ảnh:**
- Khung tìm kiếm / Path file hiển thị đúng thư mục `My Drive > Meet Recordings`.
- File có chữ Transcript sinh ra tự động, bên dưới có ngày sửa đổi là lúc bạn vừa kết thúc cuộc gọi.

---

## 📸 Ảnh 3: Nội dung Transcript (Timestamps & Speaker labels)
**Vị trí chèn:** Dưới mục *3. Xác minh Metadata: Timestamps & Speaker Labels*

**Cách thực hiện:**
1. Mở file Google Doc file Transcript đã tạo.
2. Nội dung file sẽ hiển thị chi tiết cuộc hội thoại.

**Yêu cầu bức ảnh:**
- Hiển thị rõ **Tài khoản người nói 1** (Ví dụ: Nguyễn Văn A) nói một câu.
- Hiển thị rõ **Tài khoản người nói 2** (Ví dụ: Client B) trả lời câu đó.
- Kèm theo **mốc thời gian** bên cạnh các dòng ghi chú. (Ví dụ: `15:02` Nguyễn Văn A: Xin chào, bạn nghe rõ không?).
- Góc trên cùng bên phải phải hiển thị avatar của chính tài khoản host (Owner file).

---

## 📸 Ảnh 4: Bằng chứng quyền chia sẻ (Access Request) 
**(Tùy chọn, thêm vào Phần 4 nếu cần minh họa sâu hơn)**

**Cách thực hiện:**
1. Lấy link file Transcript, gửi cho một người không thuộc công ty (ví dụ: dùng Gmail cá nhân `abc@gmail.com`).
2. Mở cửa sổ ẩn danh, đăng nhập `abc@gmail.com` và truy cập link.
3. Chụp màn hình báo lỗi "You need access" (Request access).
4. **Viết rõ vào ảnh (hoặc caption)**: "Bằng chứng cho thấy bảo mật Workspace ngăn External user xem nội bộ nếu không được cấp quyền."
