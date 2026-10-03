# Google Pics vs NanoBanana – Blog dùng thử & so sánh

Blog AI Quest (Type 2 – Investigate How): dùng thử **Google Pics** (công cụ tạo/sửa ảnh AI trong Google Workspace, GA 01/09/2026)
và làm rõ khác biệt với **NanoBanana** (model ảnh của Gemini – chính là model Pics dùng bên dưới).

## AI Quest Requirements

| # | Yêu cầu | Đáp ứng |
|---|---------|---------|
| 1 | Tóm tắt Google Pics làm được gì + khác biệt với NanoBanana | Mục 1–3 (bảng tính năng + bảng so sánh) |
| 2 | Dùng thử thực tế, chia sẻ kết quả | Mục 4 (11 ảnh nguồn) + **Mục 5: dùng thật Pics** (tạo banner Scuti AI, sửa con rồng, dịch tiếng Việt, Transform, Export 2K, so sánh Gemini) + bảng kết quả đo thực tế + video |
| 3 | Ý kiến cá nhân + áp dụng vào công việc | Mục 7–9 |

## Nội dung

1. **Google Pics là gì?** – GA, truy cập, gói hỗ trợ, hạn mức
2. **Tính năng** – tạo ảnh, variations, sửa theo phần tử, sửa/dịch chữ, crop, 2K/4K, share, Slides/Docs/Drive
3. **Google Pics vs NanoBanana** – bảng so sánh 11 tiêu chí
4. **Demo A** – khảo sát nguồn chính thức (video, blog, trang sản phẩm, Help Center, sign-in wall)
5. **Demo B (thật)** – banner Scuti AI có rồng đỏ: 4 variations → sửa riêng con rồng → dịch tiếng Việt → Transform → Export 2K → cùng prompt trong Gemini
6. **Video** hoàn chỉnh
7. **Nhận xét cá nhân**
8. **Áp dụng** vào công việc hằng ngày
9. **Mẹo prompt**
10. **Kết luận**

## Kết quả thực tế (03/10/2026)

| | Google Pics | Gemini (NanoBanana) |
|---|---|---|
| Phương án / lượt | 4 | 1 |
| Thời gian | ~15 s / lượt; export 2K ~15 s | ~25 s |
| Sửa 1 phần tử | Click rồng → Pics tự nhận "cartoon dragon" → chỉ rồng thay đổi | Phải mô tả lại bằng lời |
| Dịch tiếng Việt | Đúng dấu, giữ font/bố cục; nhưng dịch cả tên "AI QUEST" | – |
| Xuất file | Original 1365×768 / 2K 2752×1536 / 4K | Tải từ chat |

## Files

| File | Mô tả |
|------|-------|
| `google-pics-vs-nanobanana-blog.html` | Blog chính (Tiếng Việt) |
| `google-pics-vs-nanobanana-blog-en.html` | Bản tiếng Anh |
| `HUONG-DAN-DEMO-CHUP-ANH.md` | Hướng dẫn chạy lại demo + danh sách ảnh |
| `trial_playwright.py` / `trial_report.json` | Phiên khảo sát nguồn (không đăng nhập) + log |
| `record_pics_live.py` / `live_report.json` | Phiên dùng thật Pics + Gemini (profile đã đăng nhập) + log thời gian |
| `build_full_video.py` | Ghép video hoàn chỉnh (nguồn + Pics thật + cuộn blog) |
| `images/` | 22 ảnh thật – xem `images/README.md` |
| `video/google-pics-vs-nanobanana-demo.mp4` | **Video hoàn chỉnh** 6:32 (1440×900) |
| `video/google-pics-live-session.mp4` | Riêng phiên Pics + Gemini 3:11 |
| `video/google-pics-sources-part.mp4` | Riêng phần khảo sát nguồn 1:24 |

## Ghi chú

- Đăng nhập Google làm **bằng tay một lần** trong profile riêng `D:\chrome-profiles\ai-quest`; script không đọc/lưu mật khẩu.
- Các lần chạy thử và chạy chính đã tạo vài file "Scuti AI Quest Banner" / "Untitled image" trong Google Drive của tài khoản demo.
- Thanh bên Gemini (lịch sử chat cá nhân) được thu gọn trước khi quay. Dòng chân trang Gemini chứa tên tổ chức Workspace đã được cắt khỏi ảnh step-19, nhưng vẫn thấy thoáng qua trong video.

## Nguồn tham khảo

- [Video: Say hello to Google Pics from Google Workspace](https://www.youtube.com/watch?v=S18L1NFTda8)
- [Workspace Updates: Google Pics brings pro-level AI image creation and editing](https://workspaceupdates.googleblog.com/2026/09/google-pics-brings-pro-level-ai-image-creation-and-editing-to-Google-Workspace.html)
- [Google Pics – trang sản phẩm](https://workspace.google.com/products/pics/)
- [Google Blog: Try Google Pics](https://blog.google/products-and-platforms/products/workspace/google-pics/)
- [Help: Get started with Google Pics](https://support.google.com/docs/answer/17170048) · [Edit images](https://support.google.com/docs/answer/17170454) · [Download/share](https://support.google.com/docs/answer/17170934) · [Availability](https://support.google.com/docs/answer/17256710) · [Prompts](https://support.google.com/docs/answer/17499238)

---

Ngày tạo: 03/10/2026
