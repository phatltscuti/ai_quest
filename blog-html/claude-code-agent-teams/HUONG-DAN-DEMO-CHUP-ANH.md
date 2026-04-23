# Hướng dẫn chụp ảnh demo – Claude Code Agent Teams

Làm lần lượt theo các bước dưới đây khi chụp ảnh demo. Mỗi bước ghi rõ **mục đích ảnh**, **thao tác**, và **điểm cần chụp rõ**. Lưu ảnh vào thư mục `images/` theo tên trong [images/README.md](images/README.md).

**Lưu ý:**
- Agent Teams là tính năng experimental, cần bật `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- Trên Windows: dùng mode **in-process** (mặc định khi không có tmux). Split panes cần tmux/iTerm2 (chủ yếu macOS)
- Format ảnh: PNG, khuyến nghị ~1280px chiều ngang

---

## Bước 1: Cài đặt và bật Agent Teams

**File ảnh:** `step-01-enable-agent-teams.png`

**Mục đích:** Thể hiện cách bật tính năng Agent Teams.

**Thao tác:**
1. Mở Claude Code settings (settings.json hoặc UI tương ứng).
2. Thêm biến môi trường: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
   - Ví dụ trong `settings.json`: `{"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}}`
   - Hoặc trong terminal (PowerShell): `$env:CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"`
3. Chụp màn hình nơi cấu hình rõ biến này.

**Điểm cần chụp rõ:** Tên biến `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` và giá trị `1`.

---

## Bước 2: Khởi động Claude Code trong thư mục project

**File ảnh:** `step-02-claude-code-start.png`

**Mục đích:** Claude Code đã chạy với Agent Teams được bật.

**Thao tác:**
1. Mở terminal (PowerShell / CMD / bash) trong thư mục project **quản lý trung tâm tiếng Anh**.
2. Chạy `claude` (hoặc lệnh khởi động Claude Code tương ứng).
3. Chụp màn hình ngay khi Claude Code sẵn sàng nhận prompt.

**Điểm cần chụp rõ:** Dòng lệnh `claude`, working directory (thư mục project), và Claude sẵn sàng nhận input.

---

## Bước 3: Gửi prompt tạo agent team

**File ảnh:** `step-03-prompt-create-team.png`

**Mục đích:** Prompt mô tả task và cấu trúc team.

**Thao tác:**
1. Gõ prompt ví dụ (project quản lý trung tâm tiếng Anh):

```
I'm designing an English center management system (courses, students, teachers). 
Create an agent team to explore this from different angles: one teammate on UX/user flow, 
one on technical architecture, one playing devil's advocate.
```

2. Chụp màn hình **trước khi nhấn Enter** hoặc ngay sau khi gửi prompt.

**Điểm cần chụp rõ:** Toàn bộ prompt, dễ đọc; có thể thấy rằng đây là yêu cầu tạo agent team với 3 vai trò.

---

## Bước 4: Lead tạo team và spawn teammates

**File ảnh:** `step-04-lead-spawns-teammates.png`

**Mục đích:** Lead đã tạo team và spawn các teammate; thấy output của lead về team structure.

**Thao tác:**
1. Đợi Claude (lead) xử lý prompt, tạo team, spawn 3 teammates (UX/user flow, architecture, devil's advocate) cho project quản lý trung tâm tiếng Anh.
2. Chụp màn hình khi lead hiển thị:
   - Danh sách teammates (tên, vai trò)
   - Task list ban đầu (nếu có) – có thể liên quan courses, students, teachers
   - Thông báo đã spawn teammates

**Điểm cần chụp rõ:** Phần output của lead mô tả team, tên teammates (UX, architecture, devil's advocate), trạng thái “team created” hoặc tương tự.

---

## Bước 5: Task list (Ctrl+T)

**File ảnh:** `step-05-task-list.png`

**Mục đích:** Shared task list điều phối công việc giữa teammates.

**Thao tác:**
1. Khi team đang chạy (các teammate đang explore English center management system), nhấn **Ctrl+T** để mở/toggle task list.
2. Chụp màn hình task list hiển thị các task (pending, in progress, completed) – có thể là UX research, architecture design, challenge assumptions, v.v.

**Điểm cần chụp rõ:** Task list với ít nhất vài task; trạng thái (pending/in progress/completed) rõ ràng nếu có.

**Lưu ý:** Nếu task list không xuất hiện ngay, đợi lead tạo task rồi chụp. Có thể cần chụp phần output có task list inline thay vì panel riêng tùy UI.

---

## Bước 6: Chọn teammate và xem output (Shift+Up/Down)

**File ảnh:** `step-06-select-teammate.png`

**Mục đích:** Cách chọn teammate để xem và tương tác trực tiếp (in-process mode).

**Thao tác:**
1. Dùng **Shift+Up** hoặc **Shift+Down** để chọn teammate (UX, architecture, hoặc devil's advocate).
2. Chụp màn hình khi đã chọn một teammate:
   - Thấy indicator teammate đang được chọn (tên, highlight)
   - Thấy output hoặc conversation của teammate đó (findings về hệ thống quản lý trung tâm tiếng Anh)

**Điểm cần chụp rõ:** Tên teammate được chọn, output/chat của teammate đó; thể hiện “đang xem teammate X”.

---

## Bước 7: Nhắn tin trực tiếp cho teammate

**File ảnh:** `step-07-message-teammate.png`

**Mục đích:** Gửi message trực tiếp cho teammate mà không qua lead.

**Thao tác:**
1. Chọn teammate (Shift+Up/Down) – ví dụ teammate UX.
2. Gõ message ví dụ: `Focus more on the student enrollment and course registration flow.` hoặc `Prioritize teacher schedule management.`
3. Chụp màn hình: message đã gửi và/hoặc phản hồi của teammate.

**Điểm cần chụp rõ:** Đoạn hội thoại giữa bạn và teammate; rõ đây là giao tiếp trực tiếp, không qua lead.

---

## Bước 8: Shutdown request từ team-lead

**File ảnh:** `step-08-shutdown-request.png`

**Mục đích:** Lead tự gửi shutdown request khi tất cả tasks hoàn thành.

**Thao tác:**
1. Đợi teammates hoàn thành các task (hoặc lead đánh giá đủ findings).
2. Lead tự động gửi shutdown request tới teammates.
3. Chụp màn hình thông báo: "Shutdown request from team-lead" và "Reason: All tasks complete. ... Shutting down the team."

**Điểm cần chụp rõ:** Dòng "Shutdown request from team-lead", lý do shutdown, và trạng thái teammates nhận thông báo.

---

## Bảng tóm tắt file ảnh

| Bước | File ảnh | Nội dung chính |
|------|----------|----------------|
| 1 | step-01-enable-agent-teams.png | Cấu hình bật Agent Teams |
| 2 | step-02-claude-code-start.png | Claude Code khởi động |
| 3 | step-03-prompt-create-team.png | Prompt tạo team |
| 4 | step-04-lead-spawns-teammates.png | Lead spawn teammates |
| 5 | step-05-task-list.png | Shared task list |
| 6 | step-06-select-teammate.png | Chọn teammate (Shift+Up/Down) |
| 7 | step-07-message-teammate.png | Nhắn tin trực tiếp teammate |
| 8 | step-08-shutdown-request.png | Shutdown request từ team-lead |

---

## Ghi chú khi chụp

- **Trên Windows:** Thường dùng in-process mode. Shift+Up/Down để chọn teammate; Ctrl+T để task list. Split panes có thể không khả dụng.
- **Teammates không xuất hiện:** Kiểm tra prompt đủ phức tạp; thử Shift+Down xem đã có teammate trong danh sách chưa.
- **Task list không hiện:** Đợi lead tạo task; có thể dùng output text thay cho panel nếu UI khác.
