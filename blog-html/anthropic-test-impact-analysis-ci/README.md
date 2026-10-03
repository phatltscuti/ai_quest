# Anthropic Test Impact Analysis – Agentic coding làm CI quá tải

Blog AI Quest (Type 1 – Investigate What) tóm tắt và phân tích bài viết của Anthropic về việc agentic coding làm CI quá tải và cách họ mở rộng dịch vụ Test Impact Analysis (TIA), kèm bài học cá nhân và cách áp dụng tại Scuti AI.

## Nội dung blog

1. Bài viết gốc & vì sao đáng đọc
2. Thách thức: agentic coding đè lên CI (8× code, 80% do Claude viết, 10× test, 25× CI job)
3. Kiến trúc TIA v0: listener + selector trong một tiến trình, hậu quả của lag
4. Ba bản vá: máy to hơn (~70 ngày) → sharding theo package (29 ngày) → restart hằng ngày (<1 ngày)
5. Bản thiết kế lại: listener stateless + journal trong in-memory store + rollup consumer + selector
6. Điều tác giả sẽ làm khác đi (thiết kế cho 25× trong 2 quý, instrument "in = out", state ngoài process)
7. Minh họa nhỏ `tia_demo.py` (code tự viết, KHÔNG phải code của Anthropic)
8. Bài học cá nhân & lộ trình áp dụng cho dự án outsource / khách hàng Nhật
9. Video demo
10. Kết luận & tài liệu tham khảo

## Files

| File | Ngôn ngữ | Mô tả |
|------|-----------|-------|
| `anthropic-test-impact-analysis-ci-blog.html` | Tiếng Việt | Blog chính |
| `anthropic-test-impact-analysis-ci-blog-en.html` | English | Bản tiếng Anh |
| `images/step-02/03/07/08/09-*.png` | — | 5 hình biểu đồ/sơ đồ lấy từ bài gốc (nút thắt dịch chuyển, CI job volume, bộ nhớ listener, before/after selection service, backlog listener) — được dùng trong blog |
| `images/step-01/04/05/06/10-*.png` | — | Ảnh chụp trang/đoạn text/hội thoại của bài gốc — giữ trên đĩa nhưng **không còn dùng** trong blog |
| `images/diagram-01-tia-pipeline.png` | — | Sơ đồ cơ chế TIA trước/sau redesign (tự vẽ) |
| `images/diagram-02-patch-timeline.png` | — | Sơ đồ tải agentic & tuổi thọ các bản vá (tự vẽ) |
| `images/diagram-03-tia-demo-output.png` | — | Output thật của `tia_demo.py` |
| `diagrams/*.html` | — | Nguồn HTML/SVG của các sơ đồ |
| `video/anthropic-test-impact-analysis-ci-demo.mp4` | — | Video toàn bộ phiên nghiên cứu (~1 phút 32 giây, 1440×900) |
| `tia_demo.py` | Python | Minh họa "changed files → dependency map → selected tests" + listener/journal/rollup |
| `render_diagrams.py` | Python | Render `diagrams/*.html` → `images/diagram-*.png` |
| `capture_demo.py` | Python | Phiên Playwright có quay video: chụp ảnh nguồn, mở sơ đồ, mở blog, convert mp4 |

## Cách tạo ảnh & video

- **Blog hiện dùng 8 ảnh:** 5 hình biểu đồ/sơ đồ từ bài gốc (step-02, 03, 07, 08, 09) + 3 sơ đồ tự làm (diagram-01..03). Ảnh chụp text/trang nguồn đã được bỏ khỏi blog.
- **Kiểm tra crop (03/10/2026):** đã mở lại 5 hình step-02/03/07/08/09 — cả 5 chỉ chứa đúng figure (không có menu, TOC, UI trình duyệt hay đoạn văn xung quanh) nên giữ nguyên, không tạo file `-crop.png`.
- **Nội dung blog:** phần mô tả video (mục 9) trong cả bản VI/EN không còn nhắc tới công cụ chụp/quay; chỉ mô tả quá trình đọc bài. Các chữ "Playwright" còn lại trong blog là nội dung (link/tiêu đề blog liên quan `playwright-parallel-e2e-ci` và lệnh `playwright test --only-changed` trong bảng công cụ gợi ý mục 8).
- **Ảnh nguồn (step-01..10):** Python Playwright điều khiển Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440×900). Ảnh hình minh họa được chụp theo vùng của từng figure (tạm ẩn thanh header dính để không che hình); ảnh text là ảnh viewport.
- **Sơ đồ:** viết bằng HTML/SVG trong `diagrams/`, render sang PNG bằng Playwright (`python render_diagrams.py`). Sơ đồ 3 được dựng từ output thật khi chạy `tia_demo.py`.
- **Video:** `capture_demo.py` ghi lại một phiên duy nhất (`record_video_dir="video_raw"`): mở bài gốc → cuộn qua các phần chính → mở 3 sơ đồ → mở blog hoàn chỉnh qua `file://` và cuộn từ trên xuống dưới. File webm được convert sang mp4 (libx264, yuv420p) bằng ffmpeg đi kèm `imageio-ffmpeg`, sau đó xoá `video_raw/`. Vì blog được quay trước khi file mp4 tồn tại, khung video trong blog lúc quay còn trống.

## Chạy lại

```powershell
python tia_demo.py          # chạy minh họa
python render_diagrams.py   # tạo lại sơ đồ PNG
python capture_demo.py      # chụp lại ảnh nguồn + quay video
```

## Nguồn tham khảo

- Anthropic (Sachin Malhotra), 14/09/2026 – [Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
- Blog liên quan: [`../playwright-parallel-e2e-ci/`](../playwright-parallel-e2e-ci/)

## Ghi chú trung thực

- Mọi số liệu lấy từ bài gốc. Bài gốc không công bố mã nguồn hay thuật toán chọn test chi tiết; phần đó trong blog là minh họa của tác giả và được ghi rõ.
- Các công cụ gợi ý ở mục 8 (Nx affected, pytest-testmon, `jest --findRelatedTests`, `playwright test --only-changed`...) là kiến thức chung, không đến từ bài gốc.
- Không gặp login wall; trang nguồn tải bình thường, không cần đăng nhập.

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
