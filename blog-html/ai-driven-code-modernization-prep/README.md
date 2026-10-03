# Chuẩn bị cho dự án hiện đại hoá code bằng AI (AI-driven Code Modernization)

Blog AI Quest (Type 1 – Investigate What) tóm tắt các bước chuẩn bị và best practice cho dự án hiện đại hoá codebase bằng AI, theo bài viết của Anthropic, kèm bài học cá nhân và cách áp dụng vào dự án legacy (PHP / Java / VB) cho khách hàng Nhật tại Scuti AI.

## Nội dung

1. **Tổng quan bài viết** – nút thắt chuyển từ "viết code" sang "huy động tổ chức"
2. **Bước 1 – Define the Target** – Uplift / Transform / Reimagine, map codebase, behavioral spec, lý do dự án
3. **Bước 2 – Certificate** – bộ điều kiện máy tự kiểm tra được, khác nhau theo từng loại
4. **Bước 3 – Promotion Policy** – duyệt phân tầng, sửa lỗi lặp tại gốc, dùng thời gian SME đúng chỗ
5. **Bước 4 – Prerequisites** – môi trường, codebase & CI/CD, team & review, security & compliance
6. **Bước 5 & 6 – Workflow và chạy thật** – pilot nhỏ, separate build vs in-place
7. **Chi phí token & tài sản để lại**
8. **Code Modernization plugin** (nguồn phụ: README trên GitHub)
9. **Diagram roadmap 6 bước**
10. **Bài học cá nhân**
11. **Áp dụng tại Scuti AI** – bảng áp dụng 6 bước + thói quen hằng ngày + prompt kick-off mẫu
12. **Preparation Checklist** – diagram + checklist 4 nhóm + cổng trước khi scale
13. **Video demo & tài liệu tham khảo**

## Files

Ảnh dùng trong blog (mỗi bản VI/EN): **2 ảnh**, đều là diagram tự vẽ – bản VI dùng `diagram-01-six-step-roadmap.png`, `diagram-02-preparation-checklist.png`; bản EN dùng bản dịch `diagram-01-six-step-roadmap-en.png`, `diagram-02-preparation-checklist-en.png` – cộng 1 video demo. Ảnh chụp nội dung bài gốc / README GitHub đã được bỏ khỏi blog.


| File | Ngôn ngữ | Mô tả |
|------|----------|-------|
| `ai-driven-code-modernization-prep-blog.html` | Tiếng Việt | Blog chính |
| `ai-driven-code-modernization-prep-blog-en.html` | English | Bản tiếng Anh |
| `images/step-01..08-*.png` | – | 8 ảnh chụp nguồn (bài gốc + trang GitHub plugin) – giữ trên đĩa nhưng **không dùng trong blog** |
| `images/diagram-01-six-step-roadmap.png` | Tiếng Việt | Diagram lộ trình 6 bước (blog VI) |
| `images/diagram-01-six-step-roadmap-en.png` | English | Diagram lộ trình 6 bước (blog EN) |
| `images/diagram-02-preparation-checklist.png` | Tiếng Việt | Diagram preparation checklist (blog VI) |
| `images/diagram-02-preparation-checklist-en.png` | English | Diagram preparation checklist (blog EN) |
| `diagrams/*.html` | – | Mã nguồn HTML/CSS của 2 diagram (bản VI) |
| `diagrams/*-en.html` | English | Mã nguồn HTML/CSS bản tiếng Anh, render cùng cách (chụp `#canvas`, rộng 1400px) |
| `video/ai-driven-code-modernization-prep-demo.mp4` | – | Video demo (~2 phút 13 giây, 1440x900) |
| `record_session.py` | – | Script Playwright: chụp ảnh, render diagram, quay video, convert mp4 |

## Cách tạo ảnh và video

- **Ảnh nguồn (step-XX):** `record_session.py` dùng Python Playwright với Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440x900), mở bài gốc, cuộn mượt tới từng heading (Step 1 → Step 5, A note on cost) và chụp viewport; sau đó mở trang GitHub của plugin và chụp phần README. Các ảnh này chỉ dùng để tham khảo khi viết, không chèn vào blog.
- **Diagram:** viết bằng HTML/CSS trong `diagrams/`, mở bằng `file://` trong cùng phiên và chụp element `#canvas` thành PNG.
- **Video:** cả phiên được ghi bằng `record_video_dir="video_raw"` (một page duy nhất → một file webm): bài gốc → các phần chính → trang plugin → 2 diagram → blog hoàn chỉnh cuộn từ đầu đến cuối. Sau đó convert sang mp4 (libx264, yuv420p, ffmpeg từ `imageio_ffmpeg.get_ffmpeg_exe()`) và xoá `video_raw`.
- Chạy lại: `python record_session.py` (ảnh và video sẽ được ghi đè).

## Nguồn tham khảo

- [Claude Blog: How to prepare for AI-driven code modernization projects](https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects) (nguồn chính, 23/09/2026, Jonah Ezekiel & Lexie Tonelli)
- [GitHub: code-modernization plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization)
- [Claude Blog: The AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)
- [Anthropic: Code modernization playbook](https://resources.anthropic.com/code-modernization-playbook)
- [Claude Blog: How AI helps break the cost barrier to COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization)

## Ghi chú

- Phần "Áp dụng tại Scuti AI" là đề xuất của tác giả, chưa phải quy trình chính thức của công ty.
- Không cần đăng nhập ở bất kỳ trang nào; không gặp login wall.
- Không chạy plugin thực tế trên codebase của khách; thông tin plugin lấy từ README trên GitHub.

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
