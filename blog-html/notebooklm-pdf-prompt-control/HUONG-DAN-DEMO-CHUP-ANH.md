# Hướng dẫn chụp ảnh demo – NotebookLM PDF Prompt Control

Làm lần lượt theo các bước dưới đây khi chụp ảnh demo. Mỗi bước ghi rõ **mục đích ảnh**, **thao tác**, và **điểm cần chụp rõ**. Lưu ảnh vào thư mục `images/` theo tên trong [images/README.md](images/README.md).

**Lưu ý:**
- Cần tài khoản Google (Gmail hoặc Workspace), người dùng từ 18 tuổi
- Truy cập tại: https://notebooklm.google.com
- Format ảnh: PNG, khuyến nghị ~1280px chiều ngang
- Demo gồm 5 phần: (A) Setup & Sources, (B) Iteration 1, (C) Đánh giá V1, (D) Export PDF, (E) Rubric & Verification

---

## PHẦN A: SETUP & SOURCES

---

### Bước 1: Notebook với Sources đã upload

**File ảnh:** `step-01-notebook-sources.png`

**Mục đích:** Thể hiện notebook đã tạo với tối thiểu 5 sources (demo dùng 7).

**Thao tác:**
1. Mở trình duyệt, truy cập https://notebooklm.google.com
2. Tạo notebook mới, đặt tên phù hợp (VD: "EduNova 2025 Report & AI Vision 2026")
3. Upload 7 sources theo hướng dẫn trong `sources/README.md`:
   - Copied text: Annual Report, Brand Guidelines, Market Report, Investor Deck (4 file .md)
   - Google Docs: Tài liệu chiến lược sản phẩm AI (copy source-2 vào Google Docs)
   - Web URL: https://blog.google/outreach-initiatives/education/gemini-iste-2025
   - YouTube: https://www.youtube.com/watch?v=hJP5GqnTrNo (Sal Khan TED Talk)
4. Chụp toàn bộ Sources panel khi đã upload xong

**Điểm cần chụp rõ:**
- Tên notebook ở trên cùng
- **Sources panel** hiển thị ≥ 5 sources (đủ 7 càng tốt)
- Tên và **icon loại** (PDF, Docs, Web, YouTube, Slides) của từng source
- Nút "Add source" (nếu hiển thị)

---

### Bước 2: Studio Panel – Slide Deck option

**File ảnh:** `step-02-studio-panel.png`

**Mục đích:** Hiển thị panel Studio với tùy chọn tạo Slide Deck.

**Thao tác:**
1. Trong notebook, tìm panel **"Studio"** (thường ở bên phải)
2. Chụp panel Studio hiển thị mục **Slide Deck**

**Điểm cần chụp rõ:**
- Label "Studio"
- Mục **Slide Deck** (có thể kèm Infographic, Audio Overview)
- Icon/nút generate hoặc customize

---

### Bước 3: Customization Panel

**File ảnh:** `step-03-customization-panel.png`

**Mục đích:** Hiển thị panel tùy chỉnh trước khi generate.

**Thao tác:**
1. Click icon bút chì (edit) cạnh Slide Deck
2. Chụp panel customization đã mở

**Điểm cần chụp rõ:**
- Dropdown **Format**: Presenter Slides / Detailed Deck
- Dropdown **Length**: Short / Default / Long
- Dropdown **Language**
- Ô nhập **Custom Prompt** (có thể trống hoặc đã nhập)
- Nút **Generate**

---

## PHẦN B: ITERATION 1 – PROMPT V1

---

### Bước 4: Prompt V1 đã nhập

**File ảnh:** `step-04-prompt-v1-input.png`

**Mục đích:** Chụp prompt V1 (combined) đã nhập vào ô Custom Prompt.

**Thao tác:**
1. Paste combined prompt V1 vào ô Custom Prompt (xem Mục 3 trong blog):

```
Create a 14-slide detailed deck: "EduNova 2025 Annual Report & AI Vision 2026".

STRUCTURE:
- Slide 1: Title — company name, subtitle, date
- Slide 2: Agenda — list all sections
- Slides 3–4: Executive Summary — 2025 key achievements (revenue, users, product launches)
- Slide 5: Market Landscape — EdTech trends in Vietnam and SEA
- Slide 6: Competitive Positioning — EduNova vs competitors
- Slides 7–9: Three AI Strategic Pillars (one per slide)
- Slide 10: Product Roadmap — Q1–Q4 2026 milestones
- Slide 11: Team & Investment — headcount, budget allocation
- Slide 12: Key Risks and Mitigation
- Slide 13: KPI Dashboard — key metrics with targets
- Slide 14: Call to Action & Next Steps

TONE:
- Audience: Board of Directors and investors
- Professional, confident, data-driven, forward-looking
- Executive briefing style — concise, no jargon
- Maximum 6 bullet points per slide

VISUAL STYLE:
- Colors: Dark blue (#0d47a1), accent orange (#ff6d00), white, light gray (#f5f5f5)
- Modern sans-serif typography, bold headings
- Left-aligned, generous whitespace
- Clean bar charts, donut charts, and stat cards for data
- Abstract geometric illustrations — no stock photos
- Thin blue header stripe on every slide
- Flat single-color icons

Focus on Annual Report for data and Product Strategy Doc for roadmap.
Reference Brand Guidelines for visual consistency.
```

2. Chọn format: **Detailed Deck**
3. Chọn length: **Default** hoặc **Long**
4. Chụp màn hình TRƯỚC khi nhấn Generate

**Điểm cần chụp rõ:**
- **Toàn bộ nội dung prompt** đã nhập (scroll nếu cần, chụp nhiều ảnh)
- Format / Length / Language đã chọn
- Nút Generate sẵn sàng nhấn
- **QUAN TRỌNG:** Đây là screenshot bắt buộc theo yêu cầu quest "screenshot of prompt"

---

### Bước 5: Slide Deck V1 – Overview nhiều slide

**File ảnh:** `step-05-slides-v1-overview.png`

**Mục đích:** Kết quả generate lần 1, hiển thị overview nhiều slide.

**Thao tác:**
1. Sau khi generate xong (vài phút), mở Slide Deck viewer
2. Cuộn qua các slide để có overview
3. Chụp màn hình hiển thị nhiều slide (grid view hoặc scroll view)

**Điểm cần chụp rõ:**
- Tổng quan 4–6 slide hiển thị cùng lúc
- **QUAN TRỌNG:** Đây là screenshot bắt buộc "generated slide preview"
- Chất lượng thiết kế, layout, color scheme

---

### Bước 6: Slide V1 – Chi tiết 2–3 slide

**File ảnh:** `step-06-slides-v1-detail.png`

**Mục đích:** Zoom vào 2–3 slide cụ thể để đánh giá chi tiết.

**Thao tác:**
1. Click vào slide riêng lẻ để xem full
2. Chụp 2–3 slide đại diện (VD: title slide, executive summary, AI pillar slide)

**Điểm cần chụp rõ:**
- Nội dung text: có đúng outline không?
- Tone: có executive-level không?
- Visual: màu sắc, font, layout có nhất quán không?
- Data: biểu đồ/số liệu có chính xác không?

---

## PHẦN C: ĐÁNH GIÁ V1

---

### Bước 7: Ghi chú đánh giá V1

**File ảnh:** `step-07-v1-evaluation-notes.png`

**Mục đích:** Thể hiện quá trình đánh giá và ghi chú cải thiện.

**Thao tác:**
1. Xem toàn bộ slide V1, ghi chú các vấn đề (có thể dùng chat NotebookLM)
2. Hoặc: Trong notebook chat, hỏi NotebookLM đánh giá slide:
   ```
   Review the slide deck I just generated. What are the strengths and weaknesses
   compared to the prompt requirements? Suggest specific improvements.
   ```
3. Chụp ghi chú hoặc kết quả chat

**Điểm cần chụp rõ:**
- Danh sách vấn đề phát hiện
- Hoặc: câu hỏi + câu trả lời từ NotebookLM chat
- Liên kết giữa vấn đề → hướng sửa trong V2

---

## PHẦN D: PER-SLIDE REVISION & EXPORT PDF

---

### Bước 8: Per-slide Revision (tùy chọn — có thể bỏ qua)

**File ảnh:** `step-08-per-slide-revision.png`

**Mục đích:** Chụp tính năng sửa từng slide (nếu dùng).

**Thao tác thực tế:**
1. Trong Slide Deck viewer, **click vào 1 slide** (VD: slide có bar chart)
2. Tìm **nút Edit / Revise** hoặc **ô nhập instruction** hiện ra (thường bên cạnh hoặc dưới slide)
3. Gõ instruction ngắn (VD: "Make the bar chart larger")
4. Chụp màn hình **trước khi Apply** — cần thấy: slide đang chọn + ô instruction + nút Apply

**Nếu bỏ qua bước này:**
- Có thể dùng ảnh **step-05** thay thế (blog vẫn hiển thị được)
- Hoặc chụp 1 màn hình Slide Deck viewer với 1 slide đang được chọn (không cần gõ instruction)

**Điểm cần chụp rõ:**
- Slide đang được chọn
- Ô nhập revision instruction (có text hoặc trống)
- Nút Apply / Generate revision

---

### Bước 9: Menu Export PDF

**File ảnh:** `step-09-export-menu.png`

**Mục đích:** Chụp menu xuất file.

**Thao tác thực tế:**
1. Trong Slide Deck viewer, tìm **menu 3 chấm (⋮)** hoặc **icon More** cạnh tên slide deck (thường góc trên phải)
2. Click để mở dropdown
3. Chụp ngay — menu chỉ hiện vài giây

**Điểm cần chụp rõ:**
- Dropdown đang mở
- Option **"Download PDF Document (.pdf)"** hoặc **"Download as PDF"**
- (Tùy chọn) "Download PowerPoint" nếu có

---

### Bước 10: File PDF đã xuất (bắt buộc theo quest)

**File ảnh:** `step-10-exported-pdf.png`

**Mục đích:** Chụp kết quả cuối — file PDF đã tải, mở xem.

**Thao tác thực tế:**
1. Click **Download PDF** → file tải về thư mục Downloads
2. Mở file PDF (double-click hoặc kéo vào Chrome/Edge)
3. Chụp màn hình **trình xem PDF** sao cho thấy:
   - **Tab/title bar** có tên file (VD: `EduNova_2025_Report.pdf`)
   - **Nội dung 1–2 slide** đang hiển thị (trang 1 + trang 2, hoặc 1 trang full)

**Lưu ý chụp ảnh:**
- Có thể chụp **File Explorer** (file .pdf trong Downloads) + **PDF viewer** mở bên cạnh — 1 ảnh đủ 2 phần
- Hoặc chỉ cần PDF viewer với nội dung slide rõ ràng

**Điểm cần chụp rõ:**
- Tên file .pdf (trên tab hoặc title bar)
- Nội dung slide trong PDF (chất lượng hình ảnh khi xuất)

---

## PHẦN E: RUBRIC & VERIFICATION (Tùy chọn)

---

### Bước 11: Chat NotebookLM – Verify facts (tùy chọn)

**File ảnh:** `step-11-chat-fact-check.png`

**Mục đích:** Chụp chat NotebookLM verify số liệu từ sources.

**Lưu ý thực tế:** NotebookLM **không thể xem slide deck** đã generate. Nên hỏi theo cách nó có thể trả lời — verify **số liệu trong sources** thay vì "trong slide deck".

**Thao tác thực tế:**
1. Trong notebook, mở **Chat**
2. Hỏi (dùng 1 trong 2):

   **Cách 1:** "List all key numbers from the Annual Report source: revenue 2025, MAU, growth rates. Cite the source for each."

   **Cách 2:** "Verify these numbers against our sources: $28.7M revenue, 2.1M MAU, 57.7% growth. Are they correct?"

3. Chụp màn hình: **câu hỏi + câu trả lời** của NotebookLM (có citations/references)

**Điểm cần chụp rõ:**
- Câu hỏi đã gửi
- Phần trả lời của NotebookLM
- Citations đến sources (nếu có)

---

### Bước 12: View Custom Prompt (tùy chọn — tùy phiên bản)

**File ảnh:** `step-12-view-custom-prompt.png`

**Mục đích:** Chụp prompt đã dùng (nếu NotebookLM có tính năng này).

**Thao tác thực tế:**
1. Click menu 3 chấm (⋮) cạnh tên Slide Deck
2. Tìm option **"View custom prompt"** hoặc **"See prompt used"**
3. Nếu có → chụp dialog/panel hiển thị prompt V2
4. **Nếu không có** → bỏ qua bước này (không phải tất cả phiên bản đều có)

**Có thể bỏ qua** — step-04 đã chụp prompt trước khi generate.

---

## Bảng tóm tắt file ảnh

| # | File ảnh | Nội dung chính | Phần | Bắt buộc? |
|---|----------|----------------|------|-----------|
| 1 | step-01-notebook-sources.png | Notebook với 5+ sources | A | Có |
| 2 | step-02-studio-panel.png | Studio panel – Slide Deck option | A | Có |
| 3 | step-03-customization-panel.png | Customization panel | A | Có |
| 4 | step-04-prompt-v1-input.png | Prompt V1 đã nhập | B | **Bắt buộc** (quest) |
| 5 | step-05-slides-v1-overview.png | Slide Deck V1 – overview | B | **Bắt buộc** (quest) |
| 6 | step-06-slides-v1-detail.png | Slide V1 – chi tiết 2–3 slide | B | Có |
| 7 | step-07-v1-evaluation-notes.png | Ghi chú đánh giá V1 | C | Có |
| 8 | step-08-per-slide-revision.png | Per-slide revision interface | D | Tùy chọn |
| 9 | step-09-export-menu.png | Menu export PDF/PPTX | D | Có |
| 10 | step-10-exported-pdf.png | File PDF đã xuất | D | **Bắt buộc** (quest) |
| 11 | step-11-chat-fact-check.png | Chat verify facts | E | Tùy chọn |
| 12 | step-12-view-custom-prompt.png | View custom prompt dialog | E | Tùy chọn |

---

## Ghi chú khi chụp

- **Tối thiểu bắt buộc:** 3 ảnh (step-04, 05, 10) theo yêu cầu quest
- **Khuyến nghị chụp:** Toàn bộ 12 ảnh để blog đầy đủ nhất
- **Format:** PNG, ~1280px chiều ngang
- **Crop gọn:** Chỉ giữ phần liên quan, bỏ taskbar / bookmark bar / tab khác
- **Prompt dài:** Nếu prompt không hiển thị hết trong 1 màn hình, chụp nhiều ảnh (step-04a, step-04b) hoặc dùng scroll capture
- **Annotate (tùy chọn):** Dùng Snagit, ShareX, hoặc Windows Snipping Tool đánh dấu vùng quan trọng bằng box/arrow đỏ
