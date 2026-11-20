# Hướng dẫn quay video demo – Quest 5: Gemini Notebook interactive site vs RAG truyền thống

> Toàn bộ dữ liệu là **hư cấu** (AeroPure AQ-200 của "Nimbus Home Appliances (fictional)"). Không dùng tài liệu nội bộ/khách hàng.
> API key nằm trong `.env`, **không bao giờ** mở file này hay in key ra màn hình khi quay.

## Thông tin đã tạo sẵn (lần chạy thử 20/11/2026)

| Mục | Giá trị |
|---|---|
| Notebook | **AQ-200 Demo – Interactive Site** – https://notebook.google.com/notebook/90c0adbc-111b-4ee9-a023-9e3d1cff6a75 |
| Site A (troubleshooting/user guide) | https://notebook.google.com/notebook/90c0adbc-111b-4ee9-a023-9e3d1cff6a75/artifact/ec65a47b-4d58-4317-b757-d2df4c9d05ac |
| Site B (dashboard) | https://notebook.google.com/notebook/90c0adbc-111b-4ee9-a023-9e3d1cff6a75/artifact/29a58f49-9d7b-4968-9614-1ff42f98aefc |
| Nguồn | `sources/*.pdf` (4 file) – tạo lại bằng `demo-assets/sources-gen/make_sources.py` |
| Prompt | `demo-assets/prompts/prompt-a-site.txt`, `prompt-b-dashboard.txt`, `prompt-c-refine.txt` |

**Khuyến nghị khi quay:** tạo **notebook mới** (đặt tên `AQ-200 Demo – Interactive Site (video)`) để quay trọn luồng từ đầu; notebook ở trên dùng làm "bản dự phòng" nếu generate chậm (có thể cắt ghép).

## Thời gian đo được (để canh khi quay)

| Thao tác | Thời gian thực đo |
|---|---|
| Upload 4 PDF (đến khi hiện đủ 4 nguồn) | ~8.5 s |
| Notebook tạo tóm tắt nguồn | ~5–10 s |
| Prompt "Make me a site" (site A) → chat trả lời ngay "I've started generating…" | vài giây |
| Studio hiện **"Generating Site… / based on 4 sources"** đến khi xong | **182–212 s (~3,5 phút)** |
| Dashboard (site B): chat xác nhận / site xong | 16,8 s / ≤157 s (~2,5 phút) |
| `rag.py build` | ~10 s |
| `rag.py ask` mỗi câu | 2–7 s |

## Shot list

### Cảnh 0 – Mở đầu (Explorer, ~15 s)
1. Mở thư mục `blog-html/gemini-notebook-interactive-sites/sources/` → mở nhanh `AQ-200_User_Manual.pdf`, chỉ vào dòng đỏ trên đầu trang **"FICTIONAL SAMPLE - FOR DEMO ONLY"**.

### Cảnh 1 – Tạo notebook (Chrome, ~40 s)
1. Tab mới → `https://notebook.google.com/`.
2. Bấm nút **`+ New notebook`** (góc phải, dưới thanh tìm kiếm).
   - ⚠ Trang chủ hiển thị tên các notebook cá nhân khác → quay nhanh hoặc làm mờ khi hậu kỳ.
3. Notebook mở với tiêu đề **"Untitled notebook"** (góc trái trên) → click vào tiêu đề, gõ `AQ-200 Demo – Interactive Site (video)` → Enter.
4. Đóng banner "Meet the new notes!" (nút **X**).

### Cảnh 2 – Upload nguồn (Chrome, ~20 s)
1. Bấm **`+ Add sources`** (panel trái "Sources").
2. Hộp thoại có các nút: `Upload files`, `Websites`, `Play Books`, `Drive`, `Textbooks`, `Copied text` → bấm **`Upload files`**.
3. Hộp thoại chọn file của Windows → chọn cả 4 PDF trong `sources\` (Ctrl+A) → Open.
4. Chờ ~9 s đến khi panel Sources hiện 4 file, ô chat hiện **"4 sources"**; giữa màn hình hiện tóm tắt notebook.

### Cảnh 3 – Prompt site A (Chrome, ~4 phút → cắt còn ~30 s)
1. Click ô chat **"Ask a question or create something"** (dưới giữa).
2. Dán/gõ nội dung `prompt-a-site.txt` (bắt đầu bằng `Make me a site: ...`) → Enter.
3. Chat trả lời: *"I've started generating your interactive troubleshooting and user-guide site … in your Studio panel."*
4. Panel **Studio** (phải) hiện thẻ **"Generating Site… based on 4 sources"** (vòng xoay). Nếu hiện banner "Get notified when it's ready" → bấm **`Not now`**.
5. Chờ ~3,5 phút (cắt video). Xong: thẻ đổi thành **"AeroPure AQ-200 Interactive Troubleshooting & User Guide · 4 sources"** với chấm xanh (Unread). *(Tiêu đề do Gemini đặt, có thể khác chút.)*

### Cảnh 4 – Xem & dùng site A (Chrome, ~60 s)
1. Click thẻ trong Studio → site mở trong khung xem lớn; góc phải có các nút: **Open in new tab** (icon mũi tên ra ngoài), **Collapse**, **More options** (⋮), **Close**; dưới có `Good content` / `Bad content`; trên có `View 4 sources`.
2. Bấm **Open in new tab** → tab mới URL dạng `.../notebook/<id>/artifact/<id>`, thanh trên có `To notebook`, `Create your own`.
3. Thao tác:
   - Ô **"Type an error code (E01–E15) or keyword"** → gõ `E03` → bấm thẻ **E03** → xem Root cause / Step-by-step fix.
   - Gõ `E02` → thấy bảng phụ tùng FL-200H $39 / FL-200H-2 $70 / FL-200P $59.
   - Tab **Compare models** → bảng so sánh, toggle *Highlight differences only*.
   - **Maintenance & filter cost**: tick 2 ô checklist; chọn **AQ-200 Pro** + **Pets / smoke / cooking (4 mo)** → **$177 / year**; tick *Include annual UV-C lamp replacement* → cộng thêm $35.
   - **Searchable FAQ**: gõ `bathroom`.

### Cảnh 5 – Prompt dashboard (site B) (Chrome, ~4 phút → cắt ~30 s)
1. Quay lại tab notebook, ô chat → dán `prompt-b-dashboard.txt` → Enter.
2. Chờ thẻ "Generating Site…" xong → mở → **Open in new tab** → thử bộ lọc model / month range, rê chuột vào biểu đồ.

### Cảnh 6 – Prompt chỉnh sửa (tuỳ chọn)
- Dán `prompt-c-refine.txt` vào chat. Ghi nhận: Notebook sẽ tạo **artifact mới** trong Studio (không sửa tại chỗ) – xem phần kết quả trong blog.

### Cảnh 7 – Share (Chrome, ~15 s)
- Trong tab artifact: nút **⋮** (More options) góc phải; trong notebook: nút **Share** (trên cùng). Chỉ mở hộp thoại để thấy tùy chọn, **không** chia sẻ public, không quay email.

### Cảnh 8 – RAG truyền thống (PowerShell hiển thị, ~2 phút)
```powershell
cd D:\code\personal\ai_quest\blog-html\gemini-notebook-interactive-sites\demo-assets
powershell -ExecutionPolicy Bypass -File .\run-demo.ps1 -Quick     # build + 3 câu (~45 s)
# hoặc bản đầy đủ (thêm eval 10 câu, ~1,5 phút):
powershell -ExecutionPolicy Bypass -File .\run-demo.ps1
```
Script tự "gõ" từng lệnh (typewriter) rồi chạy: `Get-ChildItem ..\sources\*.pdf`, `python rag.py build`, 3 lệnh `python rag.py ask "..."`, (`python rag.py eval ..\eval\questions.json`). Không in key.

### Cảnh 9 – So sánh 10 câu hỏi (Chrome + VS Code/Explorer, ~40 s)
1. Hỏi lại trong chat notebook 2–3 câu tiêu biểu (Q4, Q7, Q10 trong `demo-assets/eval/questions.json`).
2. Mở `demo-assets/eval/results.md` → bảng chấm điểm.

## Lưu ý khi quay
- Đừng mở tab AI Studio API keys, đừng mở `.env`.
- Trang chủ Gemini Notebook có tên notebook cá nhân + avatar/email trong tooltip → làm mờ khi hậu kỳ.
- Thời gian generate site dao động (đo được ~3–3,5 phút) → quay liên tục rồi cắt.
- Notebook chỉ trả lời dựa trên 4 nguồn đã chọn (các ô checkbox bên phải tên nguồn đều phải được tick).
