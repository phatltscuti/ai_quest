# Hướng dẫn chụp ảnh demo: LLM Wiki + Claude Code + Obsidian

Đồng bộ với `llm-wiki-claude-code-obsidian-blog.html`. Lưu ảnh vào thư mục `images/` cùng cấp với file này, **đúng tên file** để blog tự hiển thị.

**Công cụ chụp nhanh**

- Windows: `Win + Shift + S` (Snipping Tool), hoặc `PrtScn`.
- macOS: `Cmd + Shift + 4`.

**Chuẩn bị**

- [Obsidian](https://obsidian.md/) đã cài.
- (Tùy chọn) [Claude Code](https://claude.com/product/claude-code) hoặc môi trường agent CLI tương đương.
- Vault mẫu trong repo: `blog-html/llm-wiki-claude-code-obsidian/sample-llm-wiki/` (đường dẫn đầy đủ trên máy bạn có thể khác).

---

## Phương án nhanh: ảnh giả lập bằng HTML (không cần Obsidian thật)

Trong repo có thư mục **`mockup-screenshots/`** (giao diện kiểu **Windows 11**: nút minimize/maximize/close bên phải, thanh địa chỉ giống Explorer, nội dung mock **tiếng Anh**).

Đường dẫn trên mock **bước 1–5, 7–8** (ví dụ):

`D:\Users\PhatLT\Projects\ai_quest\blog-html\llm-wiki-claude-code-obsidian\sample-llm-wiki`

**Bước 6** dùng giao diện sát Obsidian thật; vault path trên tooltip chip là:

`D:\PhatLT\project\sample-llm-wiki`

1. Mở `mockup-screenshots/index.html` trong trình duyệt để vào danh sách các bước.
2. Mở từng `step-*.html` tương ứng với danh sách bên dưới (`step-01-…png` ⇔ `step-01-….html`).
3. Phóng to cửa sổ trình duyệt ~**1280px** ngang (hoặc F11 fullscreen rồi thu nhỏ một chút), zoom **100%**.
4. **`Win + Shift + S`** chọn khung **`chrome-app`** (cả thanh tiêu đề Windows + thanh đường dẫn + nội dung) hoặc khung **`terminal-app`** cho bước 7–8: lưu PNG vào `images/` với đúng tên file trong từng mục.
5. *(Tuỳ chọn)* Muốn bỏ dòng watermark góc dưới phải, mở `mockup-base.css`, thêm vào đầu file tạm: `.mock-label { display: none !important; }` rồi chụp lại — nhớ không commit thay đổi đó nếu bạn thích giữ watermark.

---

## 1. `step-01-obsidian-open-as-vault.png`

1. Mở Obsidian → **Open folder as vault**.
2. Chọn thư mục `sample-llm-wiki` (chứa `CLAUDE.md`, `raw`, `wiki`).
3. Đảm bảo sidebar trái hiển thị cả ba mục: `CLAUDE.md`, `raw`, `wiki`.
4. Chụp **toàn cửa sổ** Obsidian (có tiêu đề vault/tab nếu có).

## 2. `step-02-file-explorer-wiki-overview.png`

1. Trong Obsidian, mở file `wiki/overview.md` (preview hoặc edit).
2. Cuộn để thấy phần “Mục đích vault mẫu” và “Liên kết nhanh”.
3. Chụp khung chỉnh sửa/đọc chính (có thể kèm sidebar file tree).

## 3. `step-03-graph-view.png`

1. Mở **Graph view** (biểu tượng đồ thị hoặc lệnh palette: “Graph view”).
2. Chọn chế độ local/global tùy ý nhưng cần thấy **vài nút** nối giữa các ghi chú wiki.
3. Chụp canvas graph (ưu tiên nhìn thấy `overview`, `index`, `llm-wiki-pattern` nếu plugin parse được wiki links).

## 4. `step-04-claude-md-schema.png`

1. Mở `CLAUDE.md` ở Obsidian (Reading), tab tên ghi chú **CLAUDE**, cây file có **CLAUDE** đang chọn, vault `D:\PhatLT\project\sample-llm-wiki` (nếu khớp máy bạn).
2. Hoặc mở **`mockup-screenshots/step-04-claude-md-schema.html`**: layout bắt chước Obsidian (ribbon trái Graph/Canvas/…, explorer hai hàng nút, sidebar `#171717`, chọn dòng **CLAUDE**, link màu `#ab7fe6`, status `204 words`…).
3. Chụp khung toàn app (tab + sidebar + nội dung + status bar).

## 5. `step-05-index-and-log.png`

1. Chia pane (optional): một pane `wiki/index.md`, một pane `wiki/log.md`.
2. Zoom chữ vừa đủ đọc bảng index và 2 entry log mẫu.
3. Chụp cả hai pane hoặc tab chuyển nhanh (nếu một ảnh).

## 6. `step-06-raw-source-immutable.png`

1. Mở `raw/2026-05-07-karpathy-llm-wiki-gist-notes.md`.
2. Thể hiện rõ đây là **nguồn thô** (tiêu đề + vài bullet).
3. Chụp.

## 7. `step-07-claude-code-terminal-optional.png` *(tùy chọn)*

1. Trong terminal tại thư mục `sample-llm-wiki`, chạy `claude` (hoặc lệnh bạn dùng để mở Claude Code) — *chỉ khi đã cài và đăng nhập*.
2. Chụp **không lộ khóa/API**; có thể che token nếu có.
3. Nếu không dùng Claude Code, chụp thay bằng agent khác (Cursor, v.v.) với prompt: “Đọc CLAUDE.md và cập nhật wiki sau khi đọc raw/…”.

## 8. `step-08-git-status-optional.png` *(tùy chọn)*

1. Trong repo, chạy `git status` sau khi chỉnh sửa vault (nếu bạn version-control vault).
2. Chụp terminal cho thấy các file `.md` được theo dõi — minh chứng wiki là “codebase markdown”.

---

**Lưu ý quyền riêng tư:** che email, đường dẫn home thật, workspace nội bộ nếu ảnh lộ trong thanh địa chỉ hoặc tab.
