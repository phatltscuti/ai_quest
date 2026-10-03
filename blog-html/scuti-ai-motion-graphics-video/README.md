# Scuti AI – Video Motion Graphics bằng code (AI Quest Type 2 – Investigate How)

Video giới thiệu Scuti AI **18 giây, 1920×1080, 30 fps, có nhạc nền**. Claude Code viết animation bằng HTML + GSAP, critic độc lập review 3 vòng (v1 → v4), sau đó render từng frame thành MP4.

## Đáp ứng yêu cầu AI Quest

| Yêu cầu | Ở đâu |
|---|---|
| Tự làm video motion graphics ≥ 10 giây, lấy cảm hứng từ bài tham khảo | `video/scuti-ai-motion-graphics.mp4` (18 s) |
| Ghi lại quy trình: công cụ, prompt, cách làm | Blog mục 1 (giới thiệu + 3 prompt rút ra từ bài), mục 3–6 (công cụ, demo Studio 4 bước, critic v1 → v4, phiên Claude Code trong terminal), video quá trình |
| Ý kiến cá nhân + áp dụng vào công việc | Blog mục 8 |

## Files

| File | Mô tả |
|---|---|
| `scuti-ai-motion-graphics-video-blog.html` / `-en.html` | Blog tiếng Việt (chính) / tiếng Anh |
| `HUONG-DAN-DEMO-CHUP-ANH.md` | Hướng dẫn thao tác demo 8 bước + danh sách ảnh |
| `studio/studio_server.py`, `studio/index.html` | **Motion Studio** chạy local (port 8766): storyboard, xem trước, contact sheet, nhận xét critic, nút Render MP4 có thanh tiến độ |
| `animation/scuti-intro.html` | Video là code: 1 timeline GSAP + `seekTo(t)`, có thanh play/scrub |
| `animation/render_frames.py` | Render: tua timeline từng frame trong Chrome → ảnh 1920×1080 → ffmpeg ghép MP4 + nhạc nền |
| `animation/storyboard.md`, `prompts.md`, `critic-notes-v1.md` … `-v3.md` | Storyboard, bộ prompt, nhận xét gốc của critic 3 vòng |
| `run_demo.py` | Tự động chạy lại toàn bộ phiên demo, chụp 8 ảnh và quay video quá trình (có render lại thật) |
| `requirements.txt` | Thư viện Python cần cài |
| `images/step-01 … step-08` | 8 ảnh do `run_demo.py` chụp; blog dùng 4 ảnh (01, 02, 05, 07) |
| `images/terminal-03`, `-06` | 2 ảnh phiên Claude Code trong terminal: danh sách lỗi của critic, kết quả render + ffmpeg |
| `claude-terminal/` | Script quay phiên terminal, prompt vòng 3, ảnh gốc `shots/`, bản quay thô, bản backup v3 |
| `video/scuti-ai-motion-graphics.mp4` | **Thành phẩm v4**: 18 s, 1920×1080, có nhạc |
| `video/scuti-ai-motion-graphics-v1.mp4`, `-v2.mp4`, `-v3.mp4` | Các bản trước critic, giữ lại để so sánh |
| `video/scuti-ai-motion-graphics-video-demo1.mp4` | Video quá trình 4:03: phiên Claude Code trong terminal (0:00–1:50, đoạn chờ được tua nhanh), sau đó là demo Studio (1:50–4:03) |

## Tự làm lại

```
pip install -r requirements.txt
python studio/studio_server.py
# mở http://localhost:8766/studio/ trên Chrome
```

## Ghi chú

- **Bài tham khảo:** blog chỉ tóm tắt ý chính và 3 prompt rút ra (storyboard → build → critic), không dùng ảnh chụp từ bài. Bài trên X đọc được khi chưa đăng nhập.
- **Số liệu:** chỉ lấy từ scuti.asia.
- **Logo và con rồng:** logo được dựng lại bằng SVG. Con rồng là hình minh họa, không phải mascot chính thức.
- **HyperFrames:** không dùng được vì cần Node ≥ 22, máy đang chạy Node 16. Mình tự làm renderer theo cùng nguyên lý.
- **Mạng khi render:** cần có internet, vì GSAP và font tải từ CDN.
- **Nhạc nền:** là pad đơn giản tạo bằng ffmpeg, không có bản quyền bên thứ ba.

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
