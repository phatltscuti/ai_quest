# Hướng dẫn demo và chụp ảnh — Gemini tạo full presentation native

Hướng dẫn này bám theo luồng Google công bố ngày 30/06/2026. Mục tiêu là tạo một deck 6 slide, khớp format chỉ định, dùng nguồn Drive, sau đó chứng minh từng thành phần vẫn chỉnh sửa được.

Thư mục ảnh: `d:\ai_quest\blog-html\google-slides-gemini-editable-generation\images\`

## Chuẩn bị

1. Làm theo `demo-assets/CHUAN-BI-TRUOC-DEMO.md`.
2. Tạo Google Doc `Project brief — Northwind` từ `02-source-doc-project-brief.txt`.
3. Tạo Google Slides `STYLE_Reference_Deck` theo `01-presentation-style-reference-notes.md`.
4. Mở `03-prompts-create-slides.txt`.
5. Chụp bằng `Windows + Shift + S`; che email, avatar, URL có ID và dữ liệu thật nếu cần.

## Bộ ảnh chính cho full-deck

### 1. `full-01-entry-point.png` — Điểm vào

1. Mở [Google Slides](https://slides.google.com) trên máy tính.
2. Ở màn hình bắt đầu, bấm **Presentation**; hoặc mở một presentation hoàn toàn trống, chưa có slide.
3. Bấm **Ask Gemini** ở góc phải.
4. Chụp toàn cửa sổ, thấy deck trống và side panel.

### 2. `full-02-prompt-and-format.png` — Prompt chỉ định format

1. Dán phần **DEMO A — PROMPT FULL PRESENTATION**.
2. Chưa gửi ngay.
3. Chụp panel thấy phần đầu prompt và các yêu cầu: 6 slide, audience, goal, format.

Mẹo: prompt dài nên chụp phần đầu và giữ file prompt làm bằng chứng đầy đủ; không cần cố nhét toàn bộ prompt vào một ảnh.

### 3. `full-03-add-content-source.png` — Thêm nguồn nội dung

1. Bấm **Add sources** → **Add from Drive**.
2. Chọn `Project brief — Northwind` → **Add**.
3. Chụp khi tên Doc xuất hiện trong danh sách nguồn.

Nếu tenant cho phép tìm nguồn từ Web/Drive/Chat/Gmail, chỉ bật những nguồn cần cho demo. Để kiểm soát fact, nên ưu tiên Doc đã chuẩn bị.

### 4. `full-04-match-style.png` — Khớp presentation style

1. Bấm **Match presentation style** → **Add from Drive**.
2. Chọn `STYLE_Reference_Deck` → **Add**.
3. Chụp tên deck style và nguồn nội dung cùng xuất hiện.

Không dùng deck chứa thông tin mật chỉ để lấy theme.

### 5. `full-05-follow-up-questions.png` — Câu hỏi làm rõ

1. Gửi prompt.
2. Gemini có thể hỏi về tone, audience, mục tiêu hoặc style.
3. Trả lời bằng block **ANSWERS FOR GEMINI FOLLOW-UP QUESTIONS**.
4. Chụp ít nhất một câu hỏi và câu trả lời.
5. Nếu Gemini không hỏi, ghi “Skipped/not shown” trong run log; đây là bước có thể bỏ qua.

### 6. `full-06-plan-overview-sources.png` — Kế hoạch: Overview + Sources

1. Bấm **Next**.
2. Chờ Gemini tạo presentation plan.
3. Chụp phần **Overview** và **Sources**, xác nhận đúng brief và hai file tham chiếu.

Điểm cần kiểm tra trước khi duyệt:
- không có số liệu ngoài brief;
- quyết định cần xin phê duyệt được nêu rõ;
- nguồn nội dung và deck style không bị đảo vai trò.

### 7. `full-07-edit-outline.png` — Sửa outline

1. Kiểm tra plan có đúng 6 bước/slide.
2. Click title hoặc mô tả một slide để sửa.
3. Nếu thiếu slide: hover title → **Add step**.
4. Nếu thừa: hover → **Delete**.
5. Áp dụng block **OUTLINE EDITS TO MAKE BEFORE APPROVE**.
6. Bấm **Update plan**.
7. Chụp outline sau chỉnh, đặc biệt slide 4–6.

### 8. `full-08-approve-generating.png` — Duyệt và tạo

1. Bấm **Approve**.
2. Giữ tab Google Slides và side panel mở. Có thể chuyển cửa sổ nhưng không đóng.
3. Chụp trạng thái generating/progress.
4. Ghi thời điểm bắt đầu vào run log.

### 9. `full-09-complete-deck.png` — Deck hoàn tất

1. Chờ Gemini tạo xong.
2. Chụp filmstrip bên trái thấy đủ 6 thumbnail và slide đang chọn.
3. Ghi thời gian hoàn tất.
4. Kiểm tra nhanh title, nguồn, số liệu, style và footer.

### 10. `full-10-native-editable-proof.png` — Chứng minh native/editable

1. Click một text box và sửa một từ.
2. Chọn một shape/KPI card, đổi màu hoặc di chuyển nhẹ.
3. Chọn flow/timeline và sửa một label.
4. Chụp khung chọn/handles của đối tượng; tránh ảnh chỉ cho thấy slide ở chế độ trình chiếu.

### 11. `full-11-refine-one-slide.png` — Tinh chỉnh một slide

1. Chọn slide 4 hoặc 5.
2. Yêu cầu Gemini:  
   `Simplify this slide, keep every fact, and make the native diagram easier to scan.`
3. Chụp preview/kết quả và ghi thay đổi vào run log.

### 12. `full-12-final-review.png` — Kiểm tra cuối

Chụp deck sau khi kiểm tra:
- đúng 6 slide;
- số `12+ hours/week`, `8 points`, `40%`, `25%`, `10 weeks` khớp brief;
- không có financial figure/customer quote do AI tự bịa;
- mọi thành phần quan trọng vẫn editable;
- footer và style nhất quán.

## Kết quả thực hành đã có trong thư mục

Các ảnh `step-01-...` đến `step-13-...` là bằng chứng của lần thực hành trước trên UI tạo từng slide:

- đã gắn deck style và Doc brief qua Sources;
- đã tạo và Insert một deck Northwind 5 slide;
- filmstrip đủ 5 slide nằm trong `step-11-five-slide-thumbnail-strip.png`;
- text, layout và thành phần slide là đối tượng native có thể chỉnh;
- đã thử Enhance và so sánh với `Beautify as image`.

Kết quả này chứng minh chất lượng luồng native/editable, nhưng **không phải** bằng chứng rằng luồng full-presentation một prompt đã chạy trên tenant đó. Không dùng ảnh cũ để minh họa các nút **Next**, **plan**, **Update plan** hoặc **Approve**.

## Fallback nếu tính năng full-deck chưa xuất hiện

1. Dùng phần **DEMO B** trong file prompt.
2. Tạo lần lượt 6 slide, mỗi preview chọn **Insert**.
3. Chụp `fallback-01-sources.png`, `fallback-02-preview.png`, `fallback-03-six-slide-filmstrip.png`, `fallback-04-editable-proof.png`.
4. Trong blog/run log ghi rõ: “Tenant chưa có full-presentation; demo dùng native single-slide generation.”
5. Không kết luận release track là lỗi. Extended rollout có thể kéo dài hơn 15 ngày.

## Sau demo

1. Điền `demo-assets/05-demo-run-log-template.md`.
2. Đổi các ô “chưa kiểm chứng” trong blog thành kết quả thực tế.
3. Mở file HTML và kiểm tra ảnh, caption, link.
4. Xóa/che dữ liệu tài khoản trước khi xuất bản.
