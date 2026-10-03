# Hướng dẫn demo & chụp ảnh – Motion Graphics Scuti AI

## Chuẩn bị

```
pip install -r requirements.txt
cd D:\ai_quest\blog-html\scuti-ai-motion-graphics-video
python studio/studio_server.py
```

Mở `http://localhost:8766/studio/` trên Chrome, cửa sổ khoảng 1440×900. Cần có internet để tải GSAP và font.

## 8 bước (mỗi bước 1 ảnh)

| # | Thao tác | File ảnh |
|---|---|---|
| 1 | Mở Motion Studio, xem storyboard 5 shot | `images/step-01-mo-studio.png` |
| 2 | Bấm **▶ Mở bản xem trước**, animation tự chạy. Chụp khoảng giây 2.8 (shot 1) | `images/step-02-xem-truoc.png` |
| 3 | Kéo thanh thời gian tới khoảng giây 7.7 (shot 5 dịch vụ) | `images/step-03-keo-thanh-thoi-gian.png` |
| 4 | Bấm **← Studio**, rồi **🖼️ Tạo contact sheet**, chờ dòng ✅ | `images/step-04-contact-sheet.png` |
| 5 | Bấm **📝 Xem nhận xét critic** (2 vòng, mỗi lỗi kèm mốc thời gian) | `images/step-05-nhan-xet-critic.png` |
| 6 | Bấm **🎬 Render MP4**, chụp khi thanh tiến độ khoảng frame 240/540 | `images/step-06-dang-render.png` |
| 7 | Render xong: dòng ✅ báo 18 s, 1920×1080, 30 fps, có nhạc nền | `images/step-07-render-xong.png` |
| 8 | Bấm **▶ Mở video**, chụp ở shot cuối (logo + rồng) | `images/step-08-phat-video.png` |

Video quá trình dừng ở bước 8, không quay đoạn mở blog.

## Chạy lại tự động

```
python run_demo.py
```

Script tự bật Studio, thao tác đủ 8 bước, render lại thật `video/scuti-ai-motion-graphics.mp4` và quay `video/scuti-ai-motion-graphics-video-demo.mp4`.
