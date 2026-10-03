# How Claude.ai Got Faster – Kỹ thuật làm claude.ai nhanh hơn 3 lần

Blog AI Quest (Type 1 – Investigate What): tóm tắt các kỹ thuật và chiến lược kỹ thuật trong bài **"How we made claude.ai 3x faster in two weeks"** (claude.dev, 23/09/2026), kèm bài học cá nhân và cách áp dụng vào dự án web/app và vận hành hằng ngày tại Scuti AI.

## AI Quest Requirements

| # | Requirement | Deliverable |
|---|-------------|-------------|
| 1 | Tóm tắt các cách tiếp cận kỹ thuật & chiến lược giúp Claude AI nhanh hơn | Mục 1–8 trong blog |
| 2 | Viết bằng lời của mình, không dịch trực tiếp | Toàn bộ blog (diễn giải + gom nhóm lại) |
| 3 | Bài học cá nhân + cách áp dụng vào dự án và vận hành hằng ngày | Mục 9–10 (bảng áp dụng, checklist, ví dụ guardrail, prompt Claude Code) |
| Extra | Sơ đồ HTML/SVG → PNG + minh họa before/after tự làm | `images/diagram-01..04` |

## Nội dung blog

1. Tóm tắt nhanh & con số chính (3,1x; 3,1s → 0,55s; 3.000+ thay đổi; 150+ thread)
2. Bối cảnh: sprint 2 tuần, kênh Slack, 4 hành trình / 13 phép đo
3. Chiến lược 1 – Đo lường trước (đếm lệnh CPU bằng Valgrind, metric tất định, ratchet)
4. Chiến lược 2 – Vòng lặp theo thread (ví dụ sidebar jank, Layout Instability API)
5. Chiến lược 3 – Các tối ưu cụ thể (static composer, V8 code cache, prefetch on hover, hook census, `:root:has()`, `location.reload()`, em dash UTF-16, streaming)
6. Chiến lược 4 – Guardrail (test trước, feature flag, ratchet, rollout từng bước, lỗi Chrome prerender)
7. Chiến lược 5 – Con người điều hướng (tham vọng, gu, định hướng)
8. Case study ngân sách 8 ms/frame (rig 120 Hz)
9. Bài học cá nhân
10. Áp dụng tại Scuti AI (dự án khách Nhật + vận hành hằng ngày + ví dụ `size-limit` / `web-vitals` + prompt cho Claude Code)
11. Video demo
12. Tài liệu tham khảo

## Files

| File / thư mục | Mô tả |
|------|-------|
| `how-claude-ai-got-faster-blog.html` | Blog tiếng Việt (chính) |
| `how-claude-ai-got-faster-blog-en.html` | Blog tiếng Anh |
| `images/step-02`, `step-04`, `step-05`, `step-07` (`.png`) | Ảnh chụp nguyên trang 1440×900 (có mục lục TREE/SHARE và đoạn văn xung quanh) – giữ làm bản gốc, **không dùng trực tiếp trong blog** |
| `images/step-02-core-journeys-chart-crop.png`, `step-04-instruction-vs-wallclock-crop.png`, `step-05-loop-figure-crop.png`, `step-07-em-dash-chart-crop.png` | Bản crop chỉ còn khung hình/biểu đồ (kèm tiêu đề, trục, chú thích của chính hình) từ 4 ảnh trên – **đây là ảnh được dùng trong blog** (Core user journeys p75, CPU instructions vs wall-clock, One thread in the loop, highlight code block) |
| `images/step-01`, `03`, `06`, `08`–`12` | Ảnh chụp nội dung chữ/trang của bài gốc (header, The brief, FIG A, Guardrails/FIG B, các thread Slack, Steering, 8 ms budget, What's next) – vẫn giữ trên đĩa nhưng **không dùng trong blog** |
| `images/diagram-01..04-*.png` | 4 sơ đồ tự vẽ, mỗi sơ đồ có bản VI và `-en` (8 file) |
| `video/how-claude-ai-got-faster-demo.mp4` | Video toàn bộ phiên Playwright (~2 phút 11 giây, 1440×900, H.264) |
| `diagrams/*.html` | Mã nguồn HTML/SVG của các sơ đồ (`#en` để xem bản tiếng Anh) |
| `sources/article-text.txt`, `sources/article-meta.json` | Toàn văn bài gốc + URL cuối, tiêu đề, vị trí heading (để đối chiếu, không bịa số liệu) |
| `scripts/01_research_extract.py` | Mở bài gốc bằng Chrome thật, trích text/heading |
| `scripts/02_render_diagrams.py` | Render sơ đồ HTML → PNG (VI + EN) |
| `scripts/03_record_session.py` | Quay toàn bộ phiên: bài gốc → chụp step-XX → sơ đồ → blog; chuyển webm → mp4 và xoá `video_raw` |

## Ảnh và video được làm thế nào

- **Ảnh trong blog**: mỗi bản HTML (VI/EN) dùng 8 ảnh – 4 sơ đồ tự vẽ + 4 biểu đồ/hình minh họa của bài gốc (bản `-crop.png` của step-02, 04, 05, 07). Không dùng ảnh chụp đoạn văn, tiêu đề hay thread Slack của bài gốc.
- **Ảnh step-XX**: Python Playwright, Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440×900). Script tìm vị trí từng phần của bài (theo text, bỏ qua mục lục sticky bên trái), cuộn bằng con lăn chuột từng bước nhỏ rồi chụp viewport. Sau đó 4 ảnh dùng trong blog được crop bằng PIL theo khung của hình (bỏ sidebar mục lục và đoạn văn xung quanh), lưu thành file mới hậu tố `-crop.png`, không ghi đè ảnh gốc.
- **Sơ đồ**: tự thiết kế bằng HTML/CSS/SVG trong `diagrams/`, chụp phần tử `#canvas` thành PNG (scale 1.5).
  - `diagram-01` – bản đồ 5 lớp tối ưu (tóm tắt từ bài gốc).
  - `diagram-02` – biểu đồ trước/sau 13 phép đo p75, **vẽ lại từ số liệu bài gốc** (không phải số đo của tôi).
  - `diagram-03` – minh họa khái niệm static composer, **tự vẽ, không phải số đo thật** (có ghi rõ trên hình).
  - `diagram-04` – vòng lặp hiệu năng đề xuất cho Scuti AI (thiết kế của tôi).
- **Video**: cùng một phiên Playwright được quay bằng `record_video_dir="video_raw"` từ đầu đến cuối (mở bài gốc → cuộn qua 12 phần và chụp ảnh → mở 4 sơ đồ → mở blog qua `file://` và cuộn từ trên xuống dưới), sau đó chuyển sang mp4 bằng ffmpeg (`imageio_ffmpeg.get_ffmpeg_exe()`, libx264, yuv420p) và xoá `video_raw`. Không có thuyết minh giọng nói.

Chạy lại: `python scripts/02_render_diagrams.py` rồi `python scripts/03_record_session.py`.

## Ghi chú nghiên cứu

- URL `https://claude.dev/blog/how-we-made-claude-ai-faster/` tải trực tiếp (HTTP 200, không chuyển hướng), không cần đăng nhập.
- Bài gốc có 2 video minh họa (FIG A, FIG B) chạy trong trang; blog không dùng ảnh hay video của chúng, chỉ diễn giải bằng lời.
- Mọi con số trong blog được đối chiếu với `sources/article-text.txt`. Phần áp dụng cho Scuti (mục 9–10) là đề xuất của tác giả blog.

## Nguồn tham khảo

- [How we made claude.ai 3x faster in two weeks – claude.dev Blog](https://claude.dev/blog/how-we-made-claude-ai-faster/)
- [MDN – LayoutShift (Layout Instability API)](https://developer.mozilla.org/en-US/docs/Web/API/LayoutShift)
- [web-vitals](https://github.com/GoogleChrome/web-vitals)
- [size-limit](https://github.com/ai/size-limit)

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
