# Hướng dẫn demo & chụp ảnh — Drive Projects (performance trends)

Đồng bộ với `drive-projects-performance-trends-blog.html`. Mỗi bước gồm **thao tác cụ thể** trên Drive/Sheets/Gemini và **tên file ảnh** lưu vào `images/`.

---

## Chuẩn bị trước khi chụp Step 1

Đọc đầy đủ: `demo-assets/CHUAN-BI-TRUOC-DEMO.md`.

**Thứ tự bắt buộc:** tạo folder → tạo Sheets/PDF → chụp Step 1–6 → tạo Project → chụp Step 7–16.

| Chuẩn bị | Chi tiết |
|----------|----------|
| Tài khoản | Google Workspace có **Gemini in Drive** + **Drive Projects** (chỉ tạo Project trên web) |
| Folder gốc | `WS_Ops_Performance_Review` |
| Folder con | `00_Source_Data`, `10_Review_Outputs` |
| 4 Sheets | Import CSV `01-` … `04-sheet-q*.csv` → đặt tên `OPS_Metrics_2025_Q1` … `Q4` |
| 2 PDF | Dán text `05-`, `06-*.txt` vào Doc → Download PDF → upload vào `00_Source_Data` |
| Project | `Performance Review — Operations 2025` (tạo sau Step 6) |

**Cắt màn hình:** `Windows + Shift + S` (Windows) / `Cmd + Shift + 4` (macOS)  
**Lưu ảnh:** `C:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\drive-projects-performance-trends\images\`  
Sau mỗi lần cắt: Paste (`Ctrl + V`) → đổi tên đúng `step-XX-....png` (hoặc Save As từ Paint).

---

## Danh sách 16 bước (chi tiết)

### 1. `step-01-drive-folder-structure.png`

**Mục tiêu ảnh:** Cây thư mục Drive cho pipeline review hiệu suất.

1. Mở trình duyệt → [drive.google.com](https://drive.google.com).
2. Double-click vào folder `WS_Ops_Performance_Review`.
3. Đảm bảo hiển thị đủ 2 folder con:
   - `00_Source_Data` (chứa 4 Sheet + 2 PDF sau khi chuẩn bị xong)
   - `10_Review_Outputs` (có thể trống lúc đầu)
4. **Chụp:** toàn cửa sổ Drive, thấy breadcrumb đường dẫn và tên 2 folder con.
5. **Lưu:** `step-01-drive-folder-structure.png`.

---

### 2. `step-02-sheet-q1-open.png`

**Mục tiêu ảnh:** Sheet metrics quý 1 với header chuẩn.

1. Vào `00_Source_Data` → double-click `OPS_Metrics_2025_Q1`.
2. Cuộn để thấy rõ:
   - Hàng header: `period`, `metric_category`, `metric_name`, `value`, `unit`, `notes`
   - Vài dòng metric Q1 (ví dụ Platform uptime 99.42%, P1 incidents = 4)
3. **Chụp:** vùng bảng chính (có thể full cửa sổ Sheets).
4. **Lưu:** `step-02-sheet-q1-open.png`.

**Nếu chưa có Sheet:** File → Import → Upload `demo-assets/01-sheet-q1-2025.csv` → Insert new sheet(s) → đổi tên file.

---

### 3. `step-03-sheet-q2-open.png`

**Mục tiêu ảnh:** Sheet Q2 — số liệu khác Q1 (trend demo).

1. Quay lại Drive → mở `OPS_Metrics_2025_Q2`.
2. Làm nổi bật dòng **P1 incidents = 2** (giảm so với Q1 = 4) hoặc uptime 99.58%.
3. **Chụp:** bảng metric Q2.
4. **Lưu:** `step-03-sheet-q2-open.png`.

---

### 4. `step-04-sheet-q3-open.png`

**Mục tiêu ảnh:** Sheet Q3 — inflection point (migration).

1. Mở `OPS_Metrics_2025_Q3`.
2. Cuộn tới dòng **Platform uptime 99.31%** và cột `notes` có ghi migration / below target.
3. **Chụp:** thấy rõ dip uptime + ghi chú Q3.
4. **Lưu:** `step-04-sheet-q3-open.png`.

---

### 5. `step-05-sheet-q4-open.png`

**Mục tiêu ảnh:** Sheet Q4 — recovery sau Q3.

1. Mở `OPS_Metrics_2025_Q4`.
2. Hiển thị uptime 99.61%, NPS 46 (year high), hoặc sprint completion 93%.
3. **Chụp:** bảng Q4.
4. **Lưu:** `step-05-sheet-q4-open.png`.

---

### 6. `step-06-pdf-report-open.png`

**Mục tiêu ảnh:** Báo cáo PDF định kỳ (narrative bổ sung cho Sheets).

1. Trong `00_Source_Data`, double-click `REPORT_H1_2025_Executive_Summary.pdf` (hoặc file FY).
2. Dùng preview PDF trên Drive (hoặc mở tab mới).
3. Cuộn tới mục **Key highlights** hoặc **Quarter-over-quarter narrative**.
4. **Chụp:** thấy tiêu đề báo cáo + đoạn narrative (không cần full PDF).
5. **Lưu:** `step-06-pdf-report-open.png`.

**Tạo PDF nếu chưa có:** New → Google Docs → dán `05-pdf-h1-2025-executive-summary.txt` → File → Download → PDF → upload lại Drive.

---

### 7. `step-07-drive-new-project-menu.png`

**Mục tiêu ảnh:** Menu tạo Drive Project.

1. Mở [drive.google.com](https://drive.google.com) (tab mới cũng được).
2. Bấm **New** (góc trái trên).
3. Trỏ chuột vào mục **Project** trong menu (có thể chưa bấm Create).
4. **Chụp:** menu New với **Project** hiển thị rõ.

**Cách khác:** mở [project.new](https://project.new) → chụp trang tạo project tương đương.

5. **Lưu:** `step-07-drive-new-project-menu.png`.

---

### 8. `step-08-project-name-create.png`

**Mục tiêu ảnh:** Đặt tên Project theo kỳ review.

1. Chọn **Project** từ menu New (hoặc từ project.new).
2. Nhập tên: `Performance Review — Operations 2025`
3. **Chụp:** màn hình trước khi bấm **Create Project**, hoặc ngay sau khi vừa tạo (thấy tên project trên header).
4. **Lưu:** `step-08-project-name-create.png`.

---

### 9. `step-09-add-sources-picker.png`

**Mục tiêu ảnh:** Gắn 6 nguồn (4 Sheet + 2 PDF) vào Project.

1. Trong Project vừa tạo, bấm **Add sources** (hoặc biểu tượng + / Sources).
2. Mở picker Drive → điều hướng tới `00_Source_Data`.
3. Chọn lần lượt (hoặc multi-select nếu UI hỗ trợ):
   - `OPS_Metrics_2025_Q1`, `Q2`, `Q3`, `Q4`
   - `REPORT_H1_2025_Executive_Summary.pdf`
   - `REPORT_FY2025_Annual_Operations_Review.pdf`
4. **Chụp:** dialog chọn file đang hiển thị tên các file nguồn.
5. **Lưu:** `step-09-add-sources-picker.png`.

---

### 10. `step-10-project-sources-panel.png`

**Mục tiêu ảnh:** 6 sources đã ghim, tất cả đang bật.

1. Sau khi Add xong, kiểm tra panel **Sources** / **Sources used** (thường cột trái hoặc phải).
2. Xác nhận đủ **6 file**, mỗi file có **checkbox bật** (checked).
3. **Chụp:** toàn màn Project + danh sách 6 sources.
4. **Lưu:** `step-10-project-sources-panel.png`.

---

### 11. `step-11-ask-gemini-fullscreen.png`

**Mục tiêu ảnh:** Giao diện Ask Gemini trong Project (prompt trống).

1. Trong Project, mở **Ask Gemini** (full-screen hoặc panel chat).
2. Xác nhận indicator số source (ví dụ icon **6** file) hoặc panel Sources used.
3. Ô **Ask Gemini** đang trống, chưa gửi prompt.
4. **Chụp:** thấy vùng chat + sources, chưa có câu trả lời dài.
5. **Lưu:** `step-11-ask-gemini-fullscreen.png`.

---

### 12. `step-12-gemini-prompt-entered.png`

**Mục tiêu ảnh:** Prompt phân tích trend đã nhập.

1. Mở file `demo-assets/07-gemini-trends-prompt.txt` (hoặc copy từ blog HTML — mục Triển khai Bước C).
2. Copy toàn bộ prompt → dán vào ô **Ask Gemini**.
3. **Chụp:** ô prompt đã điền đầy đủ, **chưa gửi** hoặc vừa bấm gửi (mũi tên ↑).

**Nội dung prompt (tóm tắt):** trích metric theo category → so trend Q1→Q4 → cross-check PDF → output Executive snapshot + bảng metric + improvements/risks + actions.

4. **Lưu:** `step-12-gemini-prompt-entered.png`.

---

### 13. `step-13-gemini-trends-response.png`

**Mục tiêu ảnh:** Kết quả phân tích xu hướng từ Gemini.

1. Gửi prompt → đợi Gemini trả lời (10–30 giây).
2. Cuộn câu trả lời để thấy:
   - **Executive snapshot** (bullet)
   - **Bảng metric** Q1 | Q2 | Q3 | Q4 | trend
   - **Top improvements** / **Top risks**
   - (Tuỳ chọn) số citation [1], [2]…
3. **Chụp:** phần response chính (có thể cần 2 lần cuộn — ưu tiên bảng so sánh quý).
4. **Lưu:** `step-13-gemini-trends-response.png`.

---

### 14. `step-14-citation-or-source-verify.png`

**Mục tiêu ảnh:** Kiểm chứng số liệu — mở nguồn Sheet hoặc PDF.

1. **Cách A:** Ở cột **Sources used**, click tên file (ví dụ `OPS_Metrics_2025_Q3`) → file mở để đối chiếu uptime 99.31% với câu trả lời Gemini.
2. **Cách B:** Click số **[1], [2]** trong câu trả lời (nếu có) → preview nguồn.
3. **Chụp:** tab Sheet/PDF nguồn đang mở, hoặc Project với Sources used + file highlight.

**Chưa bấm Export ở bước này** — Export là Step 15.

4. **Lưu:** `step-14-citation-or-source-verify.png`.

---

### 15. `step-15-export-summary-doc.png`

**Mục tiêu ảnh:** Xuất structured summary ra Doc/Word.

1. Cuộn xuống **cuối** câu trả lời Gemini.
2. Bấm **Export to Docs** (icon tài liệu) — **không** bấm Export to Sheets (Sheets chỉ xuất riêng một bảng, không phải cả summary).
3. Chọn tạo file mới; nếu được chọn folder → `10_Review_Outputs`.
4. Sau khi tạo, đổi tên: `REVIEW_2025_Ops_Performance_Summary` (Doc hoặc Word `.docx` tùy tenant).
5. **Chụp:** lúc dialog Export đang mở, hoặc file summary vừa tạo mở lần đầu.
6. **Lưu:** `step-15-export-summary-doc.png`.

---

### 16. `step-16-project-history-resume.png`

**Mục tiêu ảnh:** Lịch sử Project — resume research.

1. Trên Drive sidebar trái, bấm **Projects** (hoặc quay lại Project `Performance Review — Operations 2025`).
2. Mở panel **History** (hoặc danh sách conversation trong Project).
3. Thấy phiên chat vừa chạy (prompt trends + response).
4. **Chụp:** panel History với conversation gần nhất.
5. **Lưu:** `step-16-project-history-resume.png`.

**Step 15 follow-up (tuỳ chọn):** Mở file summary trong `10_Review_Outputs`, cuộn Executive snapshot → chụp thêm nếu blog cần ảnh “kết quả cuối” riêng (hiện blog gom vào Step 15 export).

---

## Checklist sau khi chụp xong

- [ ] Đủ 16 file `step-01` … `step-16` trong `images/`
- [ ] Step 2–5: 4 Sheet khác nhau (Q1–Q4)
- [ ] Step 10: đủ 6 sources
- [ ] Step 13: có bảng trend Q1–Q4
- [ ] Mở `drive-projects-performance-trends-blog.html` trong trình duyệt → ảnh hiển thị đúng

---

## Lỗi thường gặp

| Triệu chứng | Nguyên nhân | Xử lý |
|-------------|-------------|--------|
| Không thấy **New → Project** | Gói Workspace / chỉ mobile | Dùng web Drive hoặc project.new |
| Gemini không đọc PDF | Thiếu quyền hoặc PDF scan | Share View; dùng PDF text từ Google Docs |
| Trend sai / thiếu quý | Schema Sheet Q3 khác cột | Dùng cùng header CSV mẫu cho cả 4 quý |
| Số không khớp PDF | Gemini diễn giải narrative | Yêu cầu `[VERIFY]`; đối chiếu Step 14 |
| Export ra Word thay vì Doc | Tuỳ tenant | Vẫn hợp lệ demo; move vào `10_Review_Outputs` |
| Collaborator không phân tích được | Thiếu quyền file gốc | Share folder `00_Source_Data` trước khi share Project |

---

## Ghi ID (tuỳ chọn)

Điền link/ID vào `demo-assets/ids-template.txt` sau khi tạo file trên Drive (hướng dẫn lấy ID nằm trong file đó).
