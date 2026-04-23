# Hướng dẫn demo & chụp ảnh: Workspace Studio — Phỏng vấn 30 phút → Biên bản → Đề xuất → Dự toán

File này đồng bộ với bài blog HTML trong cùng thư mục. Mỗi bước gồm thao tác demo cụ thể và cách chụp ảnh để dán vào blog (ảnh tự nhúng khi đặt đúng tên file trong `images/`).

**Chuẩn bị tài liệu (đã soạn sẵn trong repo)**

- Mở thư mục **`demo-assets/`** cùng cấp với file này.
- Đọc checklist đầy đủ: **`demo-assets/CHUAN-BI-TRUOC-DEMO.md`** (quyền Workspace, tạo folder Drive, tạo Doc/Sheet từ file `.txt` / `.csv`, ghi ID vào bản sao của `ids-template.txt`).
- Nội dung copy-paste có sẵn:
  - `01-calendar-event-title.txt` + `02-calendar-event-description.json` → Calendar
  - `03-template-minutes-body.txt` → Google Doc template biên bản
  - `04-template-proposal-body.txt` → Google Doc template đề xuất
  - `05-estimate-sheet-headers.csv` + `06-flow-execution-log-headers.csv` → dòng tiêu đề Sheet
  - `07-minutes-after-meeting-notes.txt` → dán vào Doc biên bản **sau** họp (kích hoạp flow C / Gemini)
  - `08-chat-pre-meeting-message.txt` → đối chiếu nội dung tin Chat (flow A)
  - `09-gemini-extract-schema.json` → schema gợi ý cho bước Extract trong Studio

**Chuẩn bị nhanh (màn hình & tài khoản)**

- Dùng công cụ cắt màn hình: `Windows + Shift + S` (Windows) hoặc `Cmd + Shift + 4` (macOS).
- Mở sẵn thư mục ảnh: `C:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\workspace-studio-meeting-proposal-estimate\images\`
- Sau mỗi lần cắt, dán (`Ctrl + V`) vào thư mục đó và đổi tên file **đúng** như danh sách bên dưới (hoặc Save As từ Paint).
- Tài khoản Google Workspace có quyền dùng **Workspace Studio** (và Gemini theo gói tổ chức).

**Quy ước tên sự kiện Calendar (để demo nhất quán)**

- Tạo lịch mẫu tiêu đề: `[REQ] Acme Retail — Loyalty portal (30m interview)`
- Mô tả sự kiện (phần Description) dán khối JSON nhỏ trong blog HTML (mục “Dummy project data”) để bạn có thể chụp màn hình phần Description rõ ràng.

---

## Danh sách ảnh & thao tác

### 1. `step-01-drive-folder-structure.png`

1. Mở Google Drive, vào thư mục gốc quy trình (ví dụ `WS_Client_Intake_Pipeline`).
2. Bảo đảm hiển thị đủ các thư mục con: `00_Templates`, `10_Minutes`, `20_Proposals`, `30_Estimates`, `99_Logs`.
3. Chụp (`Windows + Shift + S`) toàn bộ cửa sổ trình duyệt (có thanh địa chỉ).
4. Lưu: `step-01-drive-folder-structure.png`.

### 2. `step-02-minutes-template-open.png`

1. Mở Google Doc mẫu biên bản trong `00_Templates` (file `TEMPLATE_Minutes_...`).
2. Cuộn để thấy các placeholder `{{EVENT_TITLE}}`, `{{CLIENT_NAME}}`, bảng “Key questions”.
3. Chụp vùng nội dung chính của template (có thể full cửa sổ).
4. Lưu: `step-02-minutes-template-open.png`.

### 3. `step-03-proposal-template-open.png`

1. Mở Doc mẫu đề xuất trong `00_Templates`.
2. Hiển thị các mục “Scope summary”, “Assumptions”, “Risks”, “Next steps”.
3. Chụp.
4. Lưu: `step-03-proposal-template-open.png`.

### 4. `step-04-estimate-sheet-template.png`

1. Mở Google Sheet mẫu dự toán trong `00_Templates`.
2. Hiển thị hàng tiêu đề cột và vài hàng mẫu cố định (nếu có).
3. Chụp.
4. Lưu: `step-04-estimate-sheet-template.png`.

### 5. `step-05-google-chat-space.png`

1. Mở trình duyệt, truy cập **Google Chat (web):** [https://chat.google.com/](https://chat.google.com/) — đăng nhập bằng tài khoản Workspace. Vào **Space** nội bộ dùng cho pipeline (ví dụ `#client-intake-bot` hoặc tên space tương đương).
2. Hiển thị thanh tiêu đề space và vài tin nhắn gần nhất (có thể trống).
3. Chụp cả sidebar trái nếu cần chứng minh đúng space.
4. Lưu: `step-05-google-chat-space.png`.

### 6. `step-06-workspace-studio-home.png`

1. Truy cập `https://studio.workspace.google.com` (hoặc đường dẫn Studio trong menu Workspace của tổ chức bạn).
2. Màn hình danh sách flow / nút tạo flow mới.
3. Chụp full cửa sổ trình duyệt.
4. Lưu: `step-06-workspace-studio-home.png`.

### 7. `step-07-flow-a-pre-meeting-overview.png`

1. Mở flow **A — Pre-meeting checklist** (hoặc tên tương đương bạn đặt trong blog).
2. Ở chế độ xem tổng thể (canvas), thấy rõ: trigger Calendar → (optional filter) → bước gửi Chat.
3. Chụp toàn canvas flow.
4. Lưu: `step-07-flow-a-pre-meeting-overview.png`.

### 8. `step-08-flow-a-trigger-config.png`

1. Click vào starter Calendar của flow A.
2. Hiển thị cấu hình “X phút/giờ trước khi sự kiện bắt đầu” và calendar được chọn.
3. Chụp panel cấu hình (che email cá nhân nếu cần).
4. Lưu: `step-08-flow-a-trigger-config.png`.

### 9. `step-09-flow-a-chat-message-body.png`

1. Mở bước gửi tin nhắn Google Chat trong flow A.
2. Hiển thị nội dung checklist (Purpose / Key questions / Assumptions) có biến tham chiếu từ sự kiện.
3. Chụp.
4. Lưu: `step-09-flow-a-chat-message-body.png`.

### 10. `step-10-chat-pre-meeting-message-result.png`

1. Chạy thử flow A (hoặc đợi trigger thật). Trong Chat space, tìm tin checklist vừa gửi.
2. Chụp tin nhắn đầy đủ (scroll nếu dài).
3. Lưu: `step-10-chat-pre-meeting-message-result.png`.

### 11. `step-11-flow-b-minutes-overview.png`

1. Mở flow **B — Minutes doc** (trigger: sự kiện Calendar bắt đầu / tạo — tùy bạn cấu hình theo blog).
2. Chụp canvas: Calendar → Create/copy Doc từ template → Move/save vào folder `10_Minutes` → (tuỳ chọn) ghi log.
3. Lưu: `step-11-flow-b-minutes-overview.png`.

### 12. `step-12-flow-b-copy-template-config.png`

1. Mở bước tạo bản sao từ template (Drive/Docs).
2. Hiển thị ID template hoặc chọn file template + folder đích + quy tắc đặt tên file có `eventId`.
3. Chụp (che thông tin nhạy cảm nếu có).
4. Lưu: `step-12-flow-b-copy-template-config.png`.

### 13. `step-13-minutes-doc-in-drive-result.png`

1. Trong Drive, mở `10_Minutes` và chọn file biên bản mới tạo (tên có mã sự kiện hoặc timestamp).
2. Chụp danh sách file hoặc mở file và chụp phần đầu Doc.
3. Lưu: `step-13-minutes-doc-in-drive-result.png`.

### 14. `step-14-flow-c-post-meeting-overview.png`

1. Mở flow **C — Proposal + Estimate** (trigger: sự kiện kết thúc hoặc khi Doc biên bản được cập nhật — theo hướng dẫn blog).
2. Chụp canvas: đọc Doc → Gemini extract → copy proposal template → cập nhật Doc → append Sheet → Chat notify.
3. Lưu: `step-14-flow-c-post-meeting-overview.png`.

### 15. `step-15-gemini-extract-config.png`

1. Mở bước “Extract data with Gemini” (hoặc tương đương) trong flow C.
2. Hiển thị schema JSON / trường cần trích (work items, scope bullets, assumptions).
3. Chụp prompt + schema (có thể thu nhỏ font trình duyệt để vừa khung).
4. Lưu: `step-15-gemini-extract-config.png`.

### 16. `step-16-proposal-doc-filled-result.png`

1. Mở proposal Doc output trong `20_Proposals`.
2. Hiển thị các bullet đã được điền từ biên bản (không cần hoàn hảo).
3. Chụp.
4. Lưu: `step-16-proposal-doc-filled-result.png`.

### 17. `step-17-estimate-sheet-appended-rows.png`

1. Mở Sheet dự toán trong `30_Estimates` (hoặc bản copy theo deal).
2. Highlight các hàng mới do Studio append (ví dụ hàng “API integration — Loyalty engine”).
3. Chụp.
4. Lưu: `step-17-estimate-sheet-appended-rows.png`.

### 18. `step-18-chat-post-meeting-notify.png`

1. Trong cùng Chat space, tìm tin thông báo sau meeting (link proposal + sheet + minutes).
2. Chụp tin nhắn đầy đủ.
3. Lưu: `step-18-chat-post-meeting-notify.png`.

### 19. `step-19-execution-run-log.png`

1. Trong Workspace Studio, mở **Run history** / execution log của một lần chạy flow C (hoặc B).
2. Chụp danh sách bước với trạng thái Success (hoặc một bước Failed cố ý khi demo phần “failure-prone”).
3. Lưu: `step-19-execution-run-log.png`.

### 20. `step-20-idempotency-sheet-log.png`

1. Chụp 3 ảnh riêng để làm bằng chứng idempotency:
   - Ảnh A: Sheet estimate/log (thấy dòng append hoặc trạng thái skip cho cùng event).
   - Ảnh B: Proposal Doc (nội dung không bị nhân bản mất kiểm soát khi run lại).
   - Ảnh C: Chat notify (lần chạy lại hoặc thông báo liên quan).
2. Mở Paint (hoặc công cụ ghép ảnh), đặt 3 ảnh theo bố cục 1 hàng hoặc 2x2 và thêm nhãn nhỏ `Sheet`, `Doc`, `Chat`.
3. (Khuyến nghị) thêm dòng chữ ngắn ở đầu ảnh: `Idempotency check - same event rerun`.
4. Lưu ảnh tổng hợp cuối cùng thành: `step-20-idempotency-sheet-log.png`.

---

## Gợi ý dán ảnh vào blog

- Blog HTML đã nhúng sẵn thẻ `<figure class="demo-fig">` trỏ tới `images/step-....png`. Chỉ cần đặt file đúng tên là ảnh hiện.
- Nếu thiếu ảnh, trình duyệt sẽ hiện icon vỡ; giữ nguyên tên file để sau bổ sung.
- Khi public blog, upload cả thư mục `images/` cùng file HTML.
