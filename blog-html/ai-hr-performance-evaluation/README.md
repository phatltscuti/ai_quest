# AI đánh giá nhân sự – Dữ liệu hoạt động hằng ngày → AI phân tích → Đánh giá

Blog AI Quest (Type 1 – Investigate What): tóm tắt cách **Ubie** (Nhật Bản) dùng Generative AI cho đánh giá nhân sự – dữ liệu hằng ngày được thu thập và sử dụng thế nào, AI xử lý ra sao, con người còn vai trò gì – kèm bài học cá nhân và đề xuất áp dụng vào quy trình HR / công việc hằng ngày tại **Scuti AI** (có phần quyền riêng tư & công bằng).

## Yêu cầu AI Quest

| # | Yêu cầu | Vị trí trong blog |
|---|---------|-------------------|
| 1 | Tóm tắt insight chính về đánh giá nhân sự bằng AI | Mục 2, 3, 5, 6 |
| 2 | Giải thích chính xác cách thu thập & sử dụng dữ liệu hoạt động hằng ngày | Mục 4 (+ Sơ đồ 1) |
| 3 | Viết bằng lời của mình, không dịch nguyên văn | Toàn bài |
| 4 | Bài học cá nhân | Mục 7 |
| 5 | Áp dụng vào quy trình HR & công việc hằng ngày của công ty, lưu ý quyền riêng tư/công bằng | Mục 8 (+ Sơ đồ 2, hướng dẫn nhanh 5 bước, prompt mẫu) |
| Extra | Sơ đồ luồng dữ liệu (HTML/SVG → PNG) | `diagrams/diagram-01-data-flow.html` → `images/diagram-01-data-flow*.png` |

## Nội dung blog

1. Hai nguồn tài liệu & bối cảnh của Ubie
2. Vì sao giao đánh giá cho AI – 4 mục đích
3. 3 nguyên tắc thiết kế (CEO quyết định cuối, Thành quả × Năng lực, phản hồi thời gian thực)
4. Dữ liệu hằng ngày được thu & dùng như thế nào (Activity Report → Fact Sheet → Evaluation Report → Companion agent)
5. Rubric 3 tầng & Human-on-the-loop, cách triển khai để không bị coi là áp đặt
6. Bài học của Ubie, vai trò còn lại của con người, các điểm thẳng thắn trong Q&A
7. Bài học cá nhân
8. Áp dụng tại Scuti AI (bảng ánh xạ, quyền riêng tư & công bằng, hướng dẫn thử nghiệm 5 bước, prompt mẫu)
9. Video demo & cách làm blog
10. Kết luận & tài liệu tham khảo

## Files

| File / thư mục | Mô tả |
|----------------|-------|
| `ai-hr-performance-evaluation-blog.html` | Blog tiếng Việt (bản chính) |
| `ai-hr-performance-evaluation-blog-en.html` | Blog tiếng Anh |
| `images/step-04-note-achievement-ability-crop.png` | Sơ đồ Thành quả × Năng lực cắt từ bài note (chỉ phần hình, không có đoạn văn nguồn) – Ảnh 1 / Figure 1 trong blog (mục 3.2) |
| `images/step-17-youtube-rubric-slide-crop.png`, `images/step-18-youtube-human-on-the-loop-crop.png` | Slide sơ đồ của webinar đã cắt gọn (bỏ giao diện YouTube, phụ đề, khung hình diễn giả): rubric 3 tầng (Ảnh 2) và vòng Human-on-the-loop (Ảnh 3) – đang dùng trong blog. Ảnh gốc `step-17/18-*.png` giữ nguyên |
| `images/step-05-note-system-overview-crop.png` | Sơ đồ tổng quan hệ thống cắt từ bài note – không dùng (trùng nội dung với Sơ đồ 1 tự vẽ) |
| `images/step-01..16-*.png` | Ảnh chụp trang nguồn (bài note, trang YouTube, khung hình demo webinar) – **không còn dùng trong blog** (blog không đăng ảnh chụp nội dung nguồn), giữ lại trên đĩa để đối chiếu |
| `images/diagram-01-data-flow(.png / -en.png)` | Sơ đồ 1: luồng dữ liệu hằng ngày → AI → đánh giá (VI / EN) |
| `images/diagram-02-scuti-rollout(.png / -en.png)` | Sơ đồ 2: đề xuất áp dụng tại Scuti AI + rào chắn quyền riêng tư (VI / EN) |
| `diagrams/*.html` | Mã nguồn HTML/SVG của 2 sơ đồ (`?lang=vi` / `?lang=en`) |
| `video/ai-hr-performance-evaluation-demo.mp4` | Video demo toàn phiên (~4 phút 24 giây, 1440×900, H.264, không có tiếng) |
| `sources/note-article.txt` | Văn bản bài note trích bằng Playwright (để đối chiếu) |
| `sources/yt-description.txt` | Mô tả video YouTube |
| `sources/yt-transcript-ja.txt` | Transcript tiếng Nhật (phụ đề tự động, nhóm ~45 giây/dòng, có timestamp) |
| `research_sources.py` | Script trích văn bản bài note + thử mở bảng transcript YouTube |
| `render_diagrams.py` | Script xuất 2 sơ đồ HTML/SVG ra PNG (VI + EN) |
| `record_demo.py` | Script ghi video + chụp ảnh step-XX trong một phiên Playwright |

Ảnh dùng trong blog: **5 ảnh mỗi bản** (VI: Ảnh 1, Sơ đồ 1, Ảnh 2, Ảnh 3, Sơ đồ 2; EN tương tự với bản `-en` của 2 sơ đồ) = 1 sơ đồ cắt từ bài note + 2 slide sơ đồ webinar (bản `-crop`) + 2 sơ đồ tự vẽ. Thư mục `images/` có 26 file; các ảnh chụp nguyên trang step-01..18 (không có hậu tố `-crop`) không còn được tham chiếu. Các ảnh `-crop` được cắt bằng PIL từ ảnh gốc; riêng step-18, góc khung diễn giả nằm trên nền trắng trống nên được phủ trắng, và đoạn viền nét đứt bị phụ đề che được vá lại bằng viền cùng kiểu.

## Cách tạo ảnh & video

- **Công cụ:** Python 3.11 + Playwright với Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440×900, `record_video_dir="video_raw"`), `imageio-ffmpeg` để chuyển webm → mp4 (libx264, yuv420p).
- **Video (1 phiên duy nhất):** mở bài note → cuộn qua các mục chính (chụp step-01..09) → mở YouTube, mô tả, bảng "文字起こし" (step-10..12) → phát video (tắt tiếng) và tua tới 27:10, 28:35, 29:30, 30:35, 34:35, 36:00 (step-13..18) → mở 2 sơ đồ → mở blog tiếng Việt bằng `file://` và cuộn từ đầu đến cuối. Có chú thích (caption) tiếng Việt chèn tạm vào trang trong lúc quay; caption được ẩn khi chụp ảnh. Thư mục `video_raw` đã được xóa sau khi chuyển đổi.
- **Sơ đồ:** tự vẽ bằng HTML + SVG trong `diagrams/`, xuất PNG bằng `render_diagrams.py` (device scale 1.5).
- Chạy lại: `python render_diagrams.py` rồi `python record_demo.py`.

## Những gì gặp trở ngại (ghi nhận trung thực)

- **YouTube transcript panel:** nút "文字起こしを表示" bấm được nhưng bảng chỉ quay vòng tải (API `get_transcript` trả 400) trong phiên tự động. Transcript được lấy thay thế bằng **phụ đề tự động tiếng Nhật** của video qua `yt-dlp` (cài tạm vào thư mục scratchpad, không cài vào môi trường Python chung). Phụ đề ASR có lỗi nhận dạng (ví dụ "Ubie" thành "指"/"郵便"), nên nội dung đã được đối chiếu với slide/ảnh demo trước khi dùng.
- **Video YouTube không có chapters** – chỉ có mô tả ngắn.
- **Phát video trong Playwright:** lần đầu player báo "エラーが発生しました"; khắc phục bằng cách bỏ cờ `--enable-automation` và thêm `--disable-blink-features=AutomationControlled`.
- Bài note có câu "やったことは3つあります" nhưng danh sách 3 việc không có trong phần chữ trích được (có thể nằm trong ảnh); blog dùng nội dung tương ứng từ webinar và ghi rõ điều này.
- Không đăng nhập hay tạo tài khoản nào (note.com và YouTube đều xem được không cần đăng nhập).

## Nguồn tham khảo

- [hashiyaman – 評価をAIに委ねたとき、人の役割はどこに残るのか (note.com, 30/09/2026)](https://note.com/hashiyaman/n/na03108694c97)
- [Ubieが実践するAI時代の人事評価〜評価をAIに委ねたとき、人はループのどこに残るのか〜 (YouTube)](https://www.youtube.com/watch?v=X52tm3MsSjA)

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
