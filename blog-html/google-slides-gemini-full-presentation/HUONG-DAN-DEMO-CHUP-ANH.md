# Hướng dẫn demo đơn giản — Gemini tạo full presentation

Mục tiêu: mở Google Slides, dán một prompt đầy đủ, duyệt plan và để Gemini tạo deck 6 slide native/editable.

**Không cần tạo Google Doc, file DOCX hay deck style.** Toàn bộ fact và format đã nằm trong prompt.

Thư mục lưu ảnh:

`d:\ai_quest\blog-html\google-slides-gemini-full-presentation\images\`

## 1. Chuẩn bị

1. Dùng Google Slides trên máy tính.
2. Chuyển giao diện sang English nếu cần.
3. Mở `demo-assets/03-full-presentation-prompt.txt`.
4. Mở `demo-assets/04-demo-run-log.md` để ghi kết quả.
5. Dùng `Windows + Shift + S` để chụp ảnh.
6. Che email, avatar, URL có ID hoặc thông tin tài khoản trước khi xuất bản.

Tính năng được rollout dạng extended từ 29/06/2026. Nếu chưa thấy, có thể tenant của bạn chưa được bật dù gói tài khoản phù hợp.

---

## 2. Bộ 8 ảnh demo

### Ảnh 1 — `full-01-entry-point.png`

1. Mở [Google Slides](https://slides.google.com).
2. Ở màn hình đầu, bấm **Presentation**.
3. Hoặc mở một presentation hoàn toàn trống rồi bấm **Ask Gemini**.
4. Chụp toàn cửa sổ, thấy panel Gemini.

### Ảnh 2 — `full-02-prompt-format.png`

1. Copy toàn bộ phần `FULL PRESENTATION PROMPT`.
2. Dán vào Gemini.
3. Không cần thêm Sources hoặc Match presentation style.
4. Chụp phần prompt thấy:
   - yêu cầu 6 slide;
   - audience và goal;
   - project facts;
   - required presentation format.
5. Gửi prompt.

Prompt dài không cần hiện hết trong một ảnh; file `.txt` là nội dung đầy đủ.

### Ảnh 3 — `full-03-plan.png`

1. Nếu Gemini hỏi thêm, trả lời theo phần `FOLLOW-UP ANSWERS`.
2. Câu hỏi làm rõ là tùy chọn; nếu không có thì tiếp tục.
3. Bấm **Next**.
4. Chờ presentation plan xuất hiện.
5. Chụp Overview và các Steps/outline.

Kiểm tra:

- đúng mục tiêu xin duyệt kế hoạch 10 tuần;
- đúng 6 slide hoặc có thể sửa thành 6;
- không có số liệu ngoài prompt.

### Ảnh 4 — `full-04-updated-plan.png`

1. Đếm số slide trong plan.
2. Sửa title hoặc description nếu cần.
3. Dùng **Add step** nếu thiếu slide.
4. Dùng **Delete** nếu thừa slide.
5. Kiểm theo phần `PLAN CHECK BEFORE APPROVE`.
6. Bấm **Update plan**.
7. Chụp outline sau khi sửa.

Chưa bấm Approve nếu slide 5 chưa tách In scope/Out of scope hoặc slide 6 thiếu một trong hai risk.

### Ảnh 5 — `full-05-generating.png`

1. Ghi giờ bắt đầu.
2. Bấm **Approve**.
3. Giữ tab Google Slides và panel Gemini mở.
4. Chụp trạng thái generating.

### Ảnh 6 — `full-06-complete-deck.png`

1. Chờ Gemini tạo xong.
2. Ghi giờ hoàn tất.
3. Chụp toàn cửa sổ.
4. Filmstrip bên trái phải thấy đủ 6 thumbnail.

Kiểm tra nhanh:

- đúng 6 slide;
- đúng thứ tự;
- cùng một style;
- footer không đè nội dung.

### Ảnh 7 — `full-07-editable-proof.png`

Đây là ảnh quan trọng nhất để chứng minh output native.

1. Click một text box và sửa một từ.
2. Hoặc chọn một shape/KPI card rồi di chuyển nhẹ.
3. Hoặc sửa label trong flow/timeline.
4. Chụp khi thấy selection handles quanh object.
5. Hoàn tác thay đổi thử nghiệm nếu cần.

Ảnh trình chiếu hoặc filmstrip không chứng minh editability. Phải thấy một object riêng được chọn.

### Ảnh 8 — `full-08-final-review.png`

1. Kiểm tra các fact:
   - `12+ hours/week`;
   - `8 points`;
   - `40%`;
   - `25%`;
   - `10 weeks`;
   - hai risk;
   - ba next step.
2. Xóa mọi budget, quote, revenue, savings hoặc commitment không có trong prompt.
3. Nếu cần, refine slide 4 hoặc 5 bằng:

   `Simplify this slide, keep every fact from my original prompt, and make the native diagram easier to scan.`

4. Kiểm tra lại sau refine.
5. Chụp deck cuối với đủ 6 slide.
6. Ghi riêng thời gian Gemini generate và thời gian chỉnh tay.

---

## 3. Checklist kết quả

- [ ] Full-presentation UI xuất hiện.
- [ ] Đã dán prompt, không cần file nguồn.
- [ ] Plan có đúng mục tiêu.
- [ ] Outline được kiểm trước Approve.
- [ ] Deck tạo xong có đúng 6 slide.
- [ ] Các số liệu đều khớp prompt.
- [ ] Không có claim tự bịa.
- [ ] Text box sửa trực tiếp được.
- [ ] Shape hoặc KPI card di chuyển/đổi màu được.
- [ ] Flow/timeline có label chỉnh được.
- [ ] Đã ghi thời gian generate và cleanup.

## 4. Nếu chưa thấy tính năng

1. Kiểm tra đang dùng desktop và English.
2. Kiểm tra gói tài khoản.
3. Nếu là Workspace công ty, hỏi admin về Rapid/Scheduled Release.
4. Ghi ngày thử và trạng thái vào run log.
5. Không dùng luồng tạo từng slide để tuyên bố đã thử full-presentation.

## 5. Sau khi chụp

1. Đặt đúng 8 tên ảnh trong thư mục `images/`.
2. Điền `demo-assets/04-demo-run-log.md`.
3. Mở `index.html` và `index-vi.html`; ảnh đúng tên sẽ thay placeholder.
4. Cập nhật phần trạng thái/kết quả bằng quan sát thật.
5. Che thông tin tài khoản trước khi xuất bản.

