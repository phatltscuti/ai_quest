# Hướng dẫn Upload Sources vào NotebookLM

Thư mục này chứa **7 sources** để upload vào NotebookLM cho demo tạo slide deck.

---

## Danh sách 7 Sources

| # | File | Loại upload | Cách upload vào NotebookLM |
|---|------|-------------|---------------------------|
| 1 | `source-1-annual-report-2025.md` | **Copied text** hoặc **Google Docs** | Copy nội dung → Paste vào Google Docs → Upload dạng "Google Docs" **HOẶC** Copy nội dung → Paste trực tiếp dạng "Copied text" |
| 2 | `source-2-ai-product-strategy-2026.md` | **Google Docs** | Copy nội dung → Paste vào Google Docs mới → Upload dạng "Google Docs" |
| 3 | `source-3-web-url.txt` | **Website URL** | Mở file, chọn 1 URL → Paste vào NotebookLM dạng "Website" |
| 4 | `source-4-youtube-url.txt` | **YouTube URL** | Mở file, chọn 1 URL → Paste vào NotebookLM dạng "YouTube" |
| 5 | `source-5-brand-guidelines.md` | **Copied text** hoặc **PDF** | Copy nội dung → Paste dạng "Copied text" **HOẶC** Convert sang PDF trước rồi upload |
| 6 | `source-6-edtech-market-report-2025.md` | **Copied text** hoặc **PDF** | Copy nội dung → Paste dạng "Copied text" **HOẶC** Convert sang PDF |
| 7 | `source-7-investor-deck-q4-2025.md` | **Copied text** hoặc **Google Slides** | Copy nội dung → Paste dạng "Copied text" **HOẶC** tạo Google Slides từ nội dung rồi upload |

---

## Hướng dẫn từng bước

### Bước 1: Mở NotebookLM
1. Truy cập https://notebooklm.google.com
2. Đăng nhập bằng tài khoản Google
3. Click **"New Notebook"** hoặc **"Create new"**
4. Đặt tên: **"EduNova 2025 Report & AI Vision 2026"**

### Bước 2: Upload Source 1 (Annual Report) — dạng Copied Text
1. Mở file `source-1-annual-report-2025.md` trong VS Code / Notepad
2. **Ctrl+A** → **Ctrl+C** (chọn tất cả, copy)
3. Trong NotebookLM, click **"Add source"** (hoặc biểu tượng +)
4. Chọn **"Copied text"**
5. Paste nội dung vào ô text
6. Đặt tên source: **"EduNova Annual Report 2025"**
7. Click **"Insert"**

### Bước 3: Upload Source 2 (Product Strategy) — dạng Google Docs
1. Mở https://docs.google.com → **Blank document**
2. Mở file `source-2-ai-product-strategy-2026.md`, copy toàn bộ nội dung
3. Paste vào Google Doc mới
4. Đặt tên: **"EduNova AI Product Strategy 2026"**
5. Quay lại NotebookLM, click **"Add source"** → **"Google Docs"**
6. Chọn file vừa tạo → **"Insert"**

### Bước 4: Upload Source 3 (Web URL)
1. Mở file `source-3-web-url.txt`, chọn 1 URL (khuyến nghị Option A)
2. Trong NotebookLM, click **"Add source"** → **"Website"**
3. Paste URL → **"Insert"**
4. Đợi NotebookLM crawl nội dung (vài giây)

### Bước 5: Upload Source 4 (YouTube)
1. Mở file `source-4-youtube-url.txt`, chọn 1 URL (khuyến nghị Option B)
2. Trong NotebookLM, click **"Add source"** → **"YouTube"**
3. Paste YouTube URL → **"Insert"**

### Bước 6: Upload Source 5 (Brand Guidelines) — dạng Copied Text
1. Mở file `source-5-brand-guidelines.md`
2. Copy toàn bộ → Trong NotebookLM chọn **"Copied text"**
3. Paste → Đặt tên: **"EduNova Brand Guidelines"** → **"Insert"**

### Bước 7: Upload Source 6 (Market Report) — dạng Copied Text
1. Mở file `source-6-edtech-market-report-2025.md`
2. Copy toàn bộ → **"Copied text"** → Đặt tên: **"SEA EdTech Market Report 2025"** → **"Insert"**

### Bước 8: Upload Source 7 (Investor Deck) — dạng Copied Text
1. Mở file `source-7-investor-deck-q4-2025.md`
2. Copy toàn bộ → **"Copied text"** → Đặt tên: **"EduNova Investor Deck Q4 2025"** → **"Insert"**

### Bước 9: Kiểm tra
- Xác nhận Sources panel hiển thị **7 sources**
- Mỗi source có icon đúng loại
- **Chụp screenshot** → lưu `images/step-01-notebook-sources.png`

---

## Lưu ý quan trọng

- **NotebookLM hỗ trợ:** PDF, Google Docs, Google Slides, Website URL, YouTube URL, Copied text
- **Cách nhanh nhất:** Dùng "Copied text" cho tất cả 5 file .md (không cần convert)
- **Cách đẹp nhất:** Convert 3 file (Annual Report, Brand Guidelines, Market Report) sang PDF trước khi upload → Sources panel sẽ hiển thị icon PDF đa dạng hơn
- **Convert .md → PDF:** Dùng VS Code extension "Markdown PDF" hoặc paste vào Google Docs → File → Download → PDF
- **Tối thiểu cần 5 sources** theo yêu cầu quest (7 sources = vượt yêu cầu)

---

## Tóm tắt nhanh (cho người vội)

```
Source 1: Copy source-1-annual-report-2025.md    → "Copied text"
Source 2: Copy source-2-ai-product-strategy-2026.md → Google Docs → upload
Source 3: Paste URL từ source-3-web-url.txt       → "Website"
Source 4: Paste URL từ source-4-youtube-url.txt   → "YouTube"
Source 5: Copy source-5-brand-guidelines.md       → "Copied text"
Source 6: Copy source-6-edtech-market-report-2025.md → "Copied text"
Source 7: Copy source-7-investor-deck-q4-2025.md  → "Copied text"
```
