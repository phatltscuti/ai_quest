# Hướng dẫn demo & chụp ảnh – Rồng Đỏ biết nói

## Chuẩn bị

```
pip install edge-tts imageio-ffmpeg
cd D:\ai_quest\blog-html\scuti-ai-red-dragon-talking-video
python studio/studio_server.py
```

Mở `http://localhost:8765/studio/` trên Chrome. Cửa sổ nên rộng khoảng 1440×900.

## 8 bước (mỗi bước 1 ảnh)

| # | Thao tác | File ảnh |
|---|---|---|
| 1 | Mở Rồng Đỏ Studio | `images/step-01-mo-studio.png` |
| 2 | Gõ kịch bản 5 câu (`scripts/narration-vi.txt`), chọn giọng **Nam Minh (nam)** | `images/step-02-go-kich-ban.png` |
| 3 | Bấm **🎙️ Tạo giọng đọc**, chờ dòng ✅ (khoảng 31,9 s, 101 từ, 7 câu) | `images/step-03-tao-giong-doc.png` |
| 4 | Bấm play ở trình phát để nghe thử | `images/step-04-nghe-thu.png` |
| 5 | Bấm **🐉 Mở trang hoạt hình**, rồi **▶ Xem trước**. Chụp lúc rồng đang nói (khoảng giây 6) | `images/step-05-xem-truoc-rong.png` |
| 6 | Tải lại trang, bấm **⏺ Ghi video**, Chrome hỏi quyền ghi tab thì chọn **Cho phép**. Chụp lúc cảnh "Dịch vụ" (khoảng giây 17) | `images/step-06-dang-ghi-video.png` |
| 7 | Hết lời thoại thì hộp **✅ Đã xuất video** hiện ra (tên file, thời lượng, có âm thanh) | `images/step-07-xuat-video-xong.png` |
| 8 | Bấm **▶ Mở video**, xem thành phẩm | `images/step-08-phat-video-mp4.png` |


## Chạy lại tự động

```
python scripts/run_demo.py
```

Script tự bật server Studio, thao tác đủ 8 bước và chụp 8 ảnh. Nó cũng xuất lại `video/scuti-ai-red-dragon.mp4` và quay video quá trình `video/scuti-ai-red-dragon-talking-video-demo.mp4`.

## Lưu ý khi tự ghi bằng tay

- Thanh nút (← Studio / ▶ Xem trước / ⏺ Ghi video) và đồng hồ "Đang ghi" nằm **bên dưới** khung 1280×720, nên không bị ghi vào video.
- Studio tự cắt đúng khung sân khấu 1280×720 trước khi đổi sang MP4.
