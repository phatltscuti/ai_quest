# Chuẩn bị trước demo — Gemini tạo cả presentation native trong Google Slides

## 1. Điều kiện và tình trạng rollout

- Dùng Google Slides trên máy tính; tính năng hiện chỉ hỗ trợ tiếng Anh.
- Cần một trong các gói đủ điều kiện: Workspace Business Standard/Plus, Enterprise Standard/Plus, Google AI Pro/Ultra, Google AI Pro for Education hoặc AI Expanded Access.
- Google bắt đầu extended rollout cho Rapid Release và Scheduled Release từ 29/06/2026; có thể mất hơn 15 ngày mới xuất hiện.
- Không có công tắc admin riêng cho tính năng này. Release track chỉ quyết định thời điểm nhận tính năng, không bảo đảm menu xuất hiện ngay.
- Đến ít nhất 01/08/2026, Google công bố promotional access với hạn mức tạo multi-slide cao hơn; sau đó áp dụng hạn mức theo người dùng.

## 2. Tài liệu mẫu cần đưa lên Drive

| File trong `demo-assets/` | Dùng để làm gì |
|---|---|
| `01-presentation-style-reference-notes.md` | Tạo deck `STYLE_Reference_Deck` có màu, font và bố cục mẫu |
| `02-source-doc-project-brief.txt` | Tạo Google Doc `Project brief — Northwind` làm nguồn nội dung |
| `03-prompts-create-slides.txt` | Prompt full-deck chính, câu trả lời làm rõ và prompt fallback |
| `04-prompts-enhance-slide.txt` | Prompt chỉnh từng slide sau khi deck được tạo |
| `05-demo-run-log-template.md` | Ghi kết quả, thời gian và các điểm phải sửa tay |

## 3. Cấu trúc Drive đề xuất

```text
Gemini_Slides_Demo/
├── 00_Style_Reference/STYLE_Reference_Deck
├── 10_Source/Project brief — Northwind
└── 20_Output/Northwind Customer Portal MVP — Gemini
```

## 4. Chuẩn bị deck style

1. Tạo `STYLE_Reference_Deck` với 3 slide: title, nội dung 2 cột, timeline/KPI.
2. Dùng xanh navy `#0B57D0`, cyan `#00A6A6`, nền trắng, font Aptos hoặc Arial.
3. Giữ logo giả lập nhỏ ở góc phải và footer `Confidential — internal draft`.
4. Không đưa dữ liệu Northwind vào deck style; file này chỉ định hướng hình thức.

## 5. Checklist trước khi chụp

- [ ] Google Account/Slides UI đặt English.
- [ ] Tài khoản có gói đủ điều kiện.
- [ ] Hai file nguồn đã nằm trên Drive.
- [ ] Mở trang chủ Slides hoặc một presentation hoàn toàn trống, chưa có slide nội dung.
- [ ] Zoom trình duyệt 100%, ẩn bookmark bar và tắt thông báo.
- [ ] Không đưa dữ liệu thật, bí mật hoặc thông tin khách hàng vào prompt/demo.
- [ ] Thư mục lưu ảnh: `../images/`.
- [ ] Đọc `HUONG-DAN-DEMO-CHUP-ANH.md` và mở sẵn `03-prompts-create-slides.txt`.

## 6. Nếu chưa thấy luồng full presentation

1. Xác nhận đang ở màn hình Slides và deck hoàn toàn trống.
2. Kiểm tra ngôn ngữ English và gói tài khoản.
3. Hỏi admin domain đang ở Rapid hay Scheduled Release.
4. Chờ extended rollout; Scheduled Release không phải lỗi và có thể xuất hiện muộn.
5. Không ghi rằng đã demo full-deck nếu UI chỉ cho tạo từng slide. Dùng phần fallback trong file prompt, ghi rõ tình trạng vào run log.
