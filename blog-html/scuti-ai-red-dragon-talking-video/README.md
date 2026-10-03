# Scuti AI – Rồng Đỏ biết nói (AI Quest Type 2 – Investigate How)

Video quảng bá Scuti AI **33 giây, có tiếng**: linh vật Rồng Đỏ nói tiếng Việt, miệng mở theo giọng, phụ đề tô sáng từng từ.
Làm miễn phí trên máy cá nhân: **kịch bản → edge-tts → hoạt hình HTML/SVG → Chrome ghi tab → MP4**.

## Đáp ứng yêu cầu AI Quest

| Yêu cầu | Ở đâu |
|---|---|
| Tóm tắt phương pháp & công cụ của video tham khảo | Blog mục 1: ý tưởng, bảng công cụ, **prompt rút ra từ video**, đoạn code chính |
| Tự làm video ≥ 20 giây, Rồng Đỏ xuất hiện và nói | `video/scuti-ai-red-dragon.mp4` (33,3 s, H.264 + AAC, có tiếng) |
| Ý kiến cá nhân + áp dụng vào công việc | Blog mục 6–7 |

## Files

| File | Mô tả |
|---|---|
| `scuti-ai-red-dragon-talking-video-blog.html` | Blog tiếng Việt (bản chính) |
| `scuti-ai-red-dragon-talking-video-blog-en.html` | Blog tiếng Anh |
| `HUONG-DAN-DEMO-CHUP-ANH.md` | Hướng dẫn thao tác demo 8 bước + danh sách ảnh |
| `studio/studio_server.py` | Server nhỏ chạy local: `/api/tts` (edge-tts) và `/api/export` (WebM → MP4 bằng ffmpeg) |
| `studio/index.html` | **Rồng Đỏ Studio**: gõ kịch bản, chọn giọng, tạo & nghe giọng đọc, mở trang hoạt hình |
| `assets/scuti-dragon.html` | Trang hoạt hình Rồng Đỏ 1280×720, nút **▶ Xem trước** và **⏺ Ghi video** (Chrome ghi tab + âm thanh bằng MediaRecorder) |
| `assets/narration-vi.mp3`, `boundaries.json`, `timeline.js`, `waveform.png` | Giọng đọc, mốc thời gian từng từ/câu, độ mở miệng 50 fps, sóng âm |
| `scripts/make_tts.py` | Kịch bản → giọng đọc + mốc thời gian (Studio gọi script này) |
| `scripts/narration-vi.txt` | Kịch bản 5 câu |
| `scripts/run_demo.py` | Tự động chạy lại toàn bộ phiên demo (thao tác trình duyệt), chụp 8 ảnh và quay video quá trình |
| `images/step-01 … step-08` | 8 ảnh, mỗi bước 1 ảnh |
| `video/scuti-ai-red-dragon.mp4` | **Thành phẩm**: 33,3 s, 1280×720, có tiếng |
| `video/scuti-ai-red-dragon-talking-video-demo.mp4` | Video toàn bộ quá trình (1:51, không tiếng, không có đoạn mở blog) |

## Tự làm lại

```
pip install edge-tts imageio-ffmpeg
python studio/studio_server.py
# mở http://localhost:8765/studio/ trên Chrome
```

## Ghi chú

- **Video tham khảo:** blog chỉ tóm tắt ý tưởng, công cụ và prompt rút ra, không dùng ảnh chụp từ video.
- **Prompt trong blog** là prompt viết lại theo cách của video tham khảo. Phần code (trang hoạt hình, Studio, script giọng đọc) do Claude Code viết.
- **Hình Rồng Đỏ** được vẽ lại bằng SVG, không phải asset chính thức của Scuti.
- **edge-tts** dùng dịch vụ đọc của Microsoft Edge một cách không chính thức. Nếu dùng thương mại, cần kiểm tra điều khoản hoặc thay bằng Azure TTS.
- **Khẩu hình:** miệng rồng mở/đóng theo âm lượng giọng đọc, không theo từng âm.
- **Âm thanh khi chạy `run_demo.py`:** loa trình duyệt bị tắt, nhưng âm thanh vẫn được ghi trực tiếp vào video, nên file MP4 xuất ra vẫn có tiếng.
