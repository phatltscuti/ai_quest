# Greg Isenberg X Post Insights – AI Roll-ups

Blog tóm tắt các insight chính từ bài viết dài (X Article) **“$5T opportunity: AI Roll Ups”** của Greg Isenberg trên X (đăng 26/09/2026), kèm bài học cá nhân và cách áp dụng vào dự án, vận hành hằng ngày tại Scuti AI (công ty outsourcing AI/phần mềm tại Việt Nam, khách hàng Nhật Bản).

## AI Quest Requirements (Type 1 – Investigate What)

| # | Requirement | Deliverable |
|---|-------------|-------------|
| 1 | Tóm tắt thông điệp cốt lõi và các insight cụ thể | Mục 2–3 trong blog |
| 2 | Viết bằng lời của mình, không dịch nguyên văn | Toàn bộ blog (tóm tắt, diễn giải lại) |
| 3 | Bài học cá nhân | Mục 5 trong blog |
| 4 | Cách áp dụng vào dự án & vận hành tại Scuti AI | Mục 6 (infographic, 5 bước, mẫu file, prompt) |
| 5 | Ảnh minh hoạ + video demo | `images/`, `video/` |

## Nội dung blog

1. **Bài viết gốc & cách tiếp cận nguồn** – thông tin bài, số tương tác, login wall của X, mirror fxtwitter
2. **Thông điệp cốt lõi** – mua doanh nghiệp dịch vụ có sẵn niềm tin, để AI agent làm lại back-office
3. **Các insight cụ thể** – AI roll-up là PE kiểu mới, 3 lý do “vì sao bây giờ”, ai đang làm, không chỉ cho quỹ lớn, mua thay vì build, cấu trúc thư mục holdco, 2 nhóm agent, quy trình 6 bước, rulebook & corrections log, dashboard 5 số, ngành nên mua & 6 cách thất bại
4. **Infographic tổng hợp playbook**
5. **Bài học cá nhân** (5 bài học)
6. **Áp dụng tại Scuti AI** – ánh xạ ý tưởng, hướng dẫn 5 bước, mẫu `corrections-log.md`, prompt tổng hợp rule hằng tuần, vận hành hằng ngày
7. **Video demo**
8. **Kết luận**

## Files

| File | Ngôn ngữ | Mô tả |
|------|-----------|-------|
| `greg-isenberg-x-post-insights-blog.html` | Tiếng Việt | Blog chính |
| `greg-isenberg-x-post-insights-blog-en.html` | English | Bản tiếng Anh |
| `images/figure-01 … figure-04-*.jpg` | EN | 4 hình minh hoạ gốc của tác giả dùng trong blog (bản sao sạch của `sources/article-img-0/1/2/7.jpg`): who's doing AI roll-ups, holdco folder structure, agents you build, dashboard 5 numbers |
| `images/infographic-01-ai-rollup-playbook-{vi,en}.png` | VI/EN | Infographic tự thiết kế: playbook 6 bước |
| `images/infographic-02-scuti-application-{vi,en}.png` | VI/EN | Infographic tự thiết kế: áp dụng cho Scuti AI |
| `video/greg-isenberg-x-post-insights-demo.mp4` | — | Video demo toàn bộ phiên (~2 phút 07 giây, 1440×900) |
| `sources/fxtwitter-api.json` | EN | JSON gốc lấy từ api.fxtwitter.com |
| `sources/article-text.md` | EN | Văn bản bài viết trích từ JSON (để tra cứu) |
| `sources/article-reader.html` + `article-img-*.jpg`, `article-cover.jpg` | EN | Reader view cục bộ + 8 ảnh minh hoạ gốc và ảnh bìa |
| `build_reader.py` | — | Script tạo reader view từ JSON |
| `infographics/build_infographics.py` (+ các file `.html`) | — | Script tạo infographic HTML và render ra PNG |
| `record_session.py` | — | Script Playwright ghi toàn bộ phiên, chụp screenshot, convert video |

## Nguồn tham khảo

- Bài gốc: https://x.com/gregisenberg/status/2103927365977928019 (X Article “$5T opportunity: AI Roll Ups”, Greg Isenberg, 26/09/2026)
- Bản xem công khai fxtwitter (nguồn nội dung thực tế được dùng): https://fxtwitter.com/gregisenberg/status/2103927365977928019 (JSON: https://api.fxtwitter.com/gregisenberg/status/2103927365977928019)
- Số tương tác (1.833.831 views, 4.884 likes, 414 reposts, 214 replies, 16.014 bookmarks) lấy từ API tại thời điểm thu thập 03/10/2026.

## Cách lấy nội dung & những gì bị chặn

- **x.com (không đăng nhập):** chỉ hiện tiêu đề, ảnh bìa, số tương tác và ~3 đoạn đầu; phần còn lại bị mờ, có nút “Continue to X” và khung “Log in or sign up for X”. **Không nhập thông tin đăng nhập, không tạo tài khoản.**
- **api.fxtwitter.com:** trả về đầy đủ nội dung Article (toàn bộ đoạn văn + 8 ảnh minh hoạ). Đoạn mở đầu khớp với phần hiển thị trên x.com. Mọi nội dung tóm tắt đều dựa trên nguồn này.
- Một số nội dung của bài (cấu trúc thư mục, danh sách agent, scorecard, automation map, bài toán, dashboard) nằm **trong ảnh minh hoạ**; đã tải ảnh gốc về `sources/` và đọc trực tiếp.

## Cách tạo ảnh & video

1. `build_reader.py`: render JSON thành `sources/article-reader.html` (giữ nguyên văn bản gốc) để đọc và chụp.
2. `infographics/build_infographics.py`: viết 2 infographic bằng HTML/CSS (VI + EN), render sang PNG bằng Playwright (Chrome).
3. `record_session.py`: **một phiên Playwright liên tục** với Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440×900, `record_video_dir="video_raw"`):
   x.com (login wall) → api.fxtwitter.com JSON (bật Pretty-print) → reader view, cuộn qua các phần chính và chụp `step-03` … `step-08` → 2 infographic → blog hoàn chỉnh qua `file://`, cuộn từ đầu đến cuối.
   Sau đó convert webm → mp4 (libx264, yuv420p) bằng ffmpeg của `imageio-ffmpeg` và xoá `video_raw/`.

Chạy lại: `python build_reader.py && python infographics/build_infographics.py && python record_session.py`

## Ảnh trong blog

Mỗi bản (VI/EN) dùng **6 ảnh**: 4 hình minh hoạ gốc (`figure-01` … `figure-04`) + 2 infographic tự thiết kế. Blog không dùng ảnh chụp trang nguồn (x.com, JSON, reader view); các file `images/step-01` … `step-08-*.png` vẫn còn trong thư mục nhưng không được tham chiếu.

Nội dung blog (VI/EN) không nhắc đến công cụ tự động hoá (Playwright, headless, API/JSON); phần nguồn và video được mô tả như quá trình đọc bài và tổng hợp. Chi tiết kỹ thuật chỉ ghi trong README này.

## Lưu ý

- Cột “áp dụng tại Scuti AI” và các mẫu file là **đề xuất cá nhân**; dữ liệu trong mẫu `corrections-log.md` chỉ minh hoạ định dạng, không phải dữ liệu dự án thật.
- Các con số về Long Lake, Crescendo, Titan MSP, Dwelly, Thrive, General Catalyst là số liệu được nêu trong bài gốc; chính tác giả lưu ý đây là số tự báo cáo.
- Các hình minh hoạ gốc (`figure-01` … `figure-04`) thuộc về Greg Isenberg (gregisenberg.com), trích dẫn cho mục đích tóm tắt, học tập.

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
