# Hướng dẫn chụp ảnh demo – Google Workspace Studio

Làm lần lượt theo các bước dưới đây khi chụp ảnh demo. Mỗi bước ghi rõ **mục đích ảnh**, **thao tác**, và **điểm cần chụp rõ**. Lưu ảnh vào thư mục `images/` theo tên trong [images/README.md](images/README.md).

**Lưu ý:**
- Cần tài khoản Google Workspace (Business hoặc Enterprise) với Gemini AI đã bật
- Truy cập tại: https://studio.workspace.google.com
- Format ảnh: PNG, khuyến nghị ~1280px chiều ngang
- Demo gồm 3 phần: (A) Giao diện tổng quan, (B) Workflow từ Template, (C) Workflow từ đầu
- Phần 8 (Smart Meeting Notes Pipeline) trong blog chỉ có mô tả, không cần ảnh demo

---

## PHẦN A: GIAO DIỆN TỔNG QUAN

---

### Bước 1: Trang Discover (Home)

**File ảnh:** `step-01-discover-page.png`

**Mục đích:** Thể hiện giao diện trang chủ Workspace Studio và các tùy chọn tạo flow.

**Thao tác:**
1. Mở trình duyệt, truy cập https://studio.workspace.google.com
2. Đăng nhập tài khoản Google Workspace.
3. Chụp toàn bộ trang Discover khi đã load xong.

**Điểm cần chụp rõ:**
- Logo/tên "Workspace Studio" ở trên cùng
- Nút **"Create from scratch"**
- Khu vực **Templates** (flow mẫu)
- Ô nhập **"Describe a task for Gemini"** (tạo flow bằng AI)
- Menu bên trái (My flows, Discover)

---

### Bước 2: Danh sách Templates

**File ảnh:** `step-02-templates-list.png`

**Mục đích:** Hiển thị các template có sẵn, phân loại theo app/use case.

**Thao tác:**
1. Trên trang Discover, cuộn xuống hoặc click vào khu vực Templates.
2. Chụp màn hình danh sách template đang hiển thị.

**Điểm cần chụp rõ:**
- Ít nhất 4-6 template cards (tên + mô tả ngắn)
- Các bộ lọc theo app (Gmail, Sheets, Drive...) nếu có
- Template **"Get a daily summary of unread emails"** (sẽ dùng ở Phần B)

---

### Bước 3: Trang My Flows

**File ảnh:** `step-03-my-flows.png`

**Mục đích:** Hiển thị danh sách các flow đã tạo (có thể trống nếu chưa tạo).

**Thao tác:**
1. Click **"My flows"** từ menu bên trái.
2. Chụp màn hình trang My Flows.

**Điểm cần chụp rõ:**
- Tiêu đề "My flows"
- Danh sách flow (nếu có) hoặc trạng thái trống
- Nút tạo flow mới (nếu hiển thị)

---

## PHẦN B: WORKFLOW TỪ TEMPLATE – Daily Email Summary

---

### Bước 4: Chọn template "Daily Email Summary"

**File ảnh:** `step-04-select-template.png`

**Mục đích:** Mở template và vào Flow Editor.

**Thao tác:**
1. Quay lại trang Discover.
2. Tìm và click vào template **"Get a daily summary of unread emails"**.
3. Chụp màn hình ngay khi Flow Editor mở ra với template đã load.

**Điểm cần chụp rõ:**
- Tên flow ở trên cùng (có thể đổi tên)
- **3 steps** đã có sẵn trong editor:
  - Step 1: On a schedule
  - Step 2: Recap unread emails
  - Step 3: Notify me in Chat
- Nút **Test run** và **Turn on** ở phía dưới

---

### Bước 5: Cấu hình Step 1 – On a schedule (Starter)

**File ảnh:** `step-05-configure-schedule.png`

**Mục đích:** Chi tiết cấu hình starter lịch trình.

**Thao tác:**
1. Click vào **Step 1: On a schedule** để mở chi tiết.
2. Chụp màn hình panel cấu hình.

**Điểm cần chụp rõ:**
- Tùy chọn tần suất (Daily, Weekly, Weekdays...)
- Thời gian chạy (ví dụ: 8:00 AM)
- Label "Starter" hoặc icon trigger

---

### Bước 6: Cấu hình Step 2 – Recap unread emails (AI Step)

**File ảnh:** `step-06-configure-ai-recap.png`

**Mục đích:** Chi tiết cấu hình bước AI tóm tắt email.

**Thao tác:**
1. Click vào **Step 2: Recap unread emails** để mở chi tiết.
2. Chụp màn hình panel cấu hình AI.

**Điểm cần chụp rõ:**
- Tên step: "Recap unread emails"
- Icon hoặc label AI/Gemini
- Cấu hình thời gian: "Yesterday" hoặc tương tự
- Prompt hoặc settings AI (nếu hiển thị)

---

### Bước 7: Cấu hình Step 3 – Notify me in Chat

**File ảnh:** `step-07-configure-chat-notify.png`

**Mục đích:** Chi tiết bước gửi thông báo Chat và cách dùng Variable.

**Thao tác:**
1. Click vào **Step 3: Notify me in Chat** để mở chi tiết.
2. Chụp màn hình panel cấu hình.

**Điểm cần chụp rõ:**
- Trường "Message" với **variable chip màu xanh** `[Step 2: Summary of unread email]`
- Label "Notify me in Chat"
- Thể hiện rõ variable đang được dùng để truyền dữ liệu từ step trước

---

### Bước 8: Test run template flow

**File ảnh:** `step-08-test-run-template.png`

**Mục đích:** Chạy thử flow và hiển thị kết quả.

**Thao tác:**
1. Click nút **Test run** → **Start**.
2. Đợi flow chạy xong.
3. Chụp màn hình khi hiện **"Run Completed"**.

**Điểm cần chụp rõ:**
- Thông báo **"Run Completed"** (hoặc tương đương thành công)
- Dấu check xanh trên từng step (nếu có)
- Thời gian chạy (nếu hiển thị)

---

### Bước 9: Kết quả trong Google Chat

**File ảnh:** `step-09-chat-result.png`

**Mục đích:** Kết quả thực tế nhận được trong Google Chat.

**Thao tác:**
1. Mở Google Chat (chat.google.com hoặc app).
2. Tìm tin nhắn tóm tắt email vừa được flow gửi.
3. Chụp màn hình tin nhắn.

**Điểm cần chụp rõ:**
- Tin nhắn từ flow (tên flow hoặc bot name)
- Nội dung tóm tắt email AI-generated
- Timestamp tin nhắn

---

## PHẦN C: WORKFLOW TỪ ĐẦU – Auto-reply Invoice Email

---

### Bước 10: Tạo flow mới từ đầu

**File ảnh:** `step-10-create-from-scratch.png`

**Mục đích:** Bắt đầu tạo flow mới (blank canvas).

**Thao tác:**
1. Quay lại trang Discover.
2. Click **"Create from scratch"**.
3. Chụp màn hình Flow Editor trống với danh sách Starters hiển thị.

**Điểm cần chụp rõ:**
- Giao diện editor trống / blank
- Danh sách **Starters** để chọn (On a schedule, When I get an email, ...)
- Hoặc prompt chọn starter

---

### Bước 11: Chọn Starter – When I get an email

**File ảnh:** `step-11-select-email-starter.png`

**Mục đích:** Chọn starter email trigger và cấu hình filter.

**Thao tác:**
1. Chọn starter **"When I get an email"** từ danh sách.
2. Trong trường filter, nhập: `Invoice`
3. Chụp màn hình sau khi cấu hình.

**Điểm cần chụp rõ:**
- Starter đã chọn: "When I get an email"
- Trường filter với từ khóa **"Invoice"** đã nhập
- Phần "Choose a step" bên dưới (chưa có step nào)

---

### Bước 12: Thêm Step – Draft a reply

**File ảnh:** `step-12-add-draft-reply-step.png`

**Mục đích:** Thêm step Gmail "Draft a reply" và hiển thị danh sách steps.

**Thao tác:**
1. Click **"Choose a step"** bên dưới starter.
2. Duyệt danh mục **Gmail** → chọn **"Draft a reply"**.
3. Chụp màn hình khi đang chọn hoặc vừa chọn xong step.

**Điểm cần chụp rõ:**
- Danh sách categories (AI, Gmail, Chat, Sheets...) hoặc step đã chọn
- Step **"Draft a reply"** highlighted hoặc đã thêm vào flow

---

### Bước 13: Cấu hình Draft reply với Variables

**File ảnh:** `step-13-configure-variables.png`

**Mục đích:** Soạn nội dung draft reply sử dụng variable `[Email subject]`.

**Thao tác:**
1. Trong step "Draft a reply", mở panel cấu hình.
2. Soạn nội dung:
   ```
   Hello,

   I received the invoice regarding: [Email subject]

   I will review it and get back to you.
   ```
3. Dùng nút **Variables +** hoặc gõ **@** để chèn variable `[Email subject]`.
4. Chụp màn hình nội dung đã soạn.

**Điểm cần chụp rõ:**
- Trường soạn message với text đã gõ
- **Variable chip** `[Email subject]` (thường hiển thị dạng tag/chip màu xanh)
- Nút Variables + hoặc dropdown variable (nếu đang mở)

---

### Bước 14: Test run flow tự tạo

**File ảnh:** `step-14-test-run-scratch.png`

**Mục đích:** Test flow và chọn email matching.

**Thao tác:**
1. Click **Test run**.
2. Trong cửa sổ test, nhập `Invoice` vào trường "Email received" để tìm email phù hợp.
3. Chọn một email từ kết quả.
4. Click **Start**.
5. Chụp màn hình khi test đang chạy hoặc đã hoàn thành.

**Điểm cần chụp rõ:**
- Cửa sổ test với trường tìm kiếm email
- Email đã chọn để test
- Kết quả **"Run Completed"** (hoặc đang chạy)

---

### Bước 15: Kiểm tra Draft trong Gmail

**File ảnh:** `step-15-gmail-draft-result.png`

**Mục đích:** Kết quả thực tế – bản nháp email đã được tạo tự động trong Gmail.

**Thao tác:**
1. Mở Gmail → vào thư mục **Drafts**.
2. Tìm bản nháp reply mới vừa được flow tạo.
3. Mở bản nháp và chụp màn hình.

**Điểm cần chụp rõ:**
- Thư mục **Drafts** của Gmail
- Nội dung draft reply với subject gốc được chèn bởi variable
- Text "Hello, I received the invoice regarding: [subject thực tế]..."

---

## Bảng tóm tắt file ảnh

| # | File ảnh | Nội dung chính | Phần |
|---|----------|----------------|------|
| 1 | step-01-discover-page.png | Trang Discover (Home) | A |
| 2 | step-02-templates-list.png | Danh sách templates | A |
| 3 | step-03-my-flows.png | Trang My Flows | A |
| 4 | step-04-select-template.png | Chọn template Daily Email Summary | B |
| 5 | step-05-configure-schedule.png | Cấu hình On a schedule (Starter) | B |
| 6 | step-06-configure-ai-recap.png | Cấu hình Recap unread emails (AI) | B |
| 7 | step-07-configure-chat-notify.png | Cấu hình Notify me in Chat + Variable | B |
| 8 | step-08-test-run-template.png | Test run template → Run Completed | B |
| 9 | step-09-chat-result.png | Kết quả tóm tắt email trong Google Chat | B |
| 10 | step-10-create-from-scratch.png | Tạo flow mới (blank) + danh sách Starters | C |
| 11 | step-11-select-email-starter.png | Chọn starter email + filter "Invoice" | C |
| 12 | step-12-add-draft-reply-step.png | Thêm step Draft a reply (Gmail) | C |
| 13 | step-13-configure-variables.png | Soạn draft reply với variable [Email subject] | C |
| 14 | step-14-test-run-scratch.png | Test run flow + chọn email matching | C |
| 15 | step-15-gmail-draft-result.png | Kết quả draft trong Gmail Drafts | C |

---

## Ghi chú khi chụp

- **Tài khoản:** Cần Google Workspace Business/Enterprise với Gemini AI đã bật. Tài khoản Gmail cá nhân miễn phí không có Workspace Studio.
- **Test run thực hiện hành động thật:** Sẽ gửi tin nhắn Chat, tạo draft Gmail, thêm row vào Sheet...
- **Template không hiện:** Kiểm tra Workspace edition có hỗ trợ và admin đã bật Gemini AI.
- **Variable chip:** Khi chụp bước có variable, zoom vào đủ lớn để đọc được tên variable (thường là chip màu xanh).
- **Ảnh nên cắt gọn:** Chỉ giữ phần liên quan, bỏ taskbar/bookmark bar nếu không cần thiết.
