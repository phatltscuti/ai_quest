# Chuẩn bị trước khi demo từng bước

Trước khi làm theo `HUONG-DAN-DEMO-CHUP-ANH.md`, hãy hoàn thành các mục dưới đây. Toàn bộ nội dung copy-paste nằm trong cùng thư mục `demo-assets/`.

## 1. Tài khoản & quyền

- [ ] Tài khoản Google Workspace có **Workspace Studio** (và Gemini nếu flow dùng extract).
- [ ] Quyền **tạo/sửa** Calendar (lịch test riêng hoặc lịch team).
- [ ] Quyền **Drive**: tạo thư mục gốc + chia sẻ cho user chạy flow (hoặc domain-wide theo policy).
- [ ] **Google Chat**: một Space nội bộ; tài khoản automation / app được phép gửi tin (theo cấu hình admin). Web: [https://chat.google.com/](https://chat.google.com/)

## 2. Việc cần làm một lần trên Drive

1. Tạo thư mục gốc (ví dụ): `WS_Client_Intake_Pipeline`.
2. Tạo các thư mục con: `00_Templates`, `10_Minutes`, `20_Proposals`, `30_Estimates`, `99_Logs`.
3. Tạo **Google Doc** mới → dán nội dung file `03-template-minutes-body.txt` → đặt tên ví dụ `TEMPLATE_Minutes_IT_Intake` → di chuyển vào `00_Templates`.
4. Tạo **Google Doc** mới → dán `04-template-proposal-body.txt` → đặt tên `TEMPLATE_Proposal_IT_Intake` → vào `00_Templates`.
5. Tạo **Google Sheet** mới → dán / import hàng tiêu đề từ `05-estimate-sheet-headers.csv` (dòng 1 = header) → đặt tên `TEMPLATE_Estimate_IT` → vào `00_Templates`.
6. Tạo **Google Sheet** (hoặc tab trong cùng file) cho log: dán header từ `06-flow-execution-log-headers.csv` → đặt tên `Flow_Execution_Log` → vào `99_Logs` (hoặc nơi bạn quy ước).

## 3. Ghi lại ID (để điền vào Workspace Studio)

Sau khi tạo file trên Drive, mở từng file và copy **ID** từ URL (đoạn giữa `/d/` và `/edit` hoặc `/copy`):

| Tài nguyên | File mẫu | Ghi chú |
|------------|----------|---------|
| Doc template biên bản | `TEMPLATE_Minutes_IT_Intake` | Dán ID vào bước “copy template” flow B |
| Doc template đề xuất | `TEMPLATE_Proposal_IT_Intake` | Dán ID vào flow C |
| Sheet dự toán | `TEMPLATE_Estimate_IT` | spreadsheetId cho bước append |
| Sheet log (tuỳ chọn) | `Flow_Execution_Log` | spreadsheetId + tên sheet tab |

Bạn có thể ghi ID vào file trống `ids-can-bo-rieng.txt` (tự tạo bản sao từ `ids-template.txt`).

## 4. Calendar — sự kiện test

- **Tiêu đề** (copy từ `01-calendar-event-title.txt`).
- **Mô tả** (copy từ `02-calendar-event-description.json` — nguyên khối JSON).
- Đặt **thời gian** sao cho còn đủ phút để quan sát trigger “trước họp” (ví dụ bắt đầu sau 20 phút nếu flow A là “15 phút trước”).

## 5. Sau khi flow B tạo xong Doc biên bản

- Mở Doc trong `10_Minutes`, cuối buổi hoặc khi demo flow C: dán thêm nội dung từ `07-minutes-after-meeting-notes.txt` (ghi chú sau họp + câu work package rõ) rồi **Lưu**.

## 6. Danh sách file trong `demo-assets/`

| File | Mục đích |
|------|----------|
| `01-calendar-event-title.txt` | Tiêu đề sự kiện |
| `02-calendar-event-description.json` | Mô tả Calendar (metadata) |
| `03-template-minutes-body.txt` | Nội dung template biên bản (Google Doc) |
| `04-template-proposal-body.txt` | Nội dung template đề xuất (Google Doc) |
| `05-estimate-sheet-headers.csv` | Hàng tiêu đề Sheet dự toán |
| `06-flow-execution-log-headers.csv` | Hàng tiêu đề Sheet log |
| `07-minutes-after-meeting-notes.txt` | Ghi chú dán vào biên bản trước flow C |
| `08-chat-pre-meeting-message.txt` | Mẫu tin Chat (đối chiếu với cấu hình flow A) |
| `09-gemini-extract-schema.json` | Schema JSON gợi ý cho bước Extract |
| `ids-template.txt` | Mẫu điền ID Drive (copy thành file riêng, không commit secret) |

Khi điền xong checklist trên, chạy demo theo `HUONG-DAN-DEMO-CHUP-ANH.md` và chụp ảnh vào `images/`.
