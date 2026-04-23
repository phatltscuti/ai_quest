# Chuẩn bị trước demo — Drive Projects (performance trends)

## Quyền & gói

- Google Workspace có **Gemini in Drive** + **Drive Projects** (web: drive.google.com hoặc project.new).
- Collaborator cần quyền **View** từng Sheet/PDF trước khi add vào Project.

## Thứ tự làm

| Bước | Việc |
|------|------|
| 1 | Tạo folder `WS_Ops_Performance_Review` + `00_Source_Data` + `10_Review_Outputs` |
| 2 | Import 4 file CSV → Google Sheets (Q1–Q4) trong `00_Source_Data` |
| 3 | Tạo 2 PDF từ file `.txt` (H1 + FY) → upload vào `00_Source_Data` |
| 4 | Tạo Drive Project → Add sources (6 file) |
| 5 | Ask Gemini + export summary → `10_Review_Outputs` |

## Tạo Sheets từ CSV

1. Vào `00_Source_Data` → **New** → **Google Sheets** → **Blank spreadsheet**.
2. **File → Import** → Upload tab → chọn `01-sheet-q1-2025.csv` → Insert new sheet(s).
3. Đổi tên file: `OPS_Metrics_2025_Q1`.
4. Lặp cho Q2, Q3, Q4 (`02-` … `04-` csv).

## Tạo PDF demo (không cần file PDF sẵn)

1. **New** → **Google Docs** → dán nội dung `05-pdf-h1-2025-executive-summary.txt`.
2. **File → Download → PDF** → upload lại vào `00_Source_Data` với tên `REPORT_H1_2025_Executive_Summary.pdf`.
3. Lặp với `06-pdf-fy2025-annual-review.txt` → `REPORT_FY2025_Annual_Operations_Review.pdf`.

## Project

- Tên: `Performance Review — Operations 2025`
- Add sources: 4 Sheets + 2 PDFs (tất cả checked).

## Ảnh demo

Lưu vào `images/` theo `HUONG-DAN-DEMO-CHUP-ANH.md`.
