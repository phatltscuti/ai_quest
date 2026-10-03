# Hướng dẫn demo & chụp ảnh – Google Pics vs NanoBanana

Blog gồm **19 bước** (22 ảnh). Tất cả đã được chụp thật bằng Playwright + Chrome:

- **step-01 → step-11**: nguồn chính thức, phiên **không đăng nhập** (`trial_playwright.py`).
- **step-12 → step-19**: thao tác thật bên trong **Google Pics** và **Gemini app** bằng tài khoản Workspace (`record_pics_live.py`).

**Lưu ý:**
- Tài khoản cần: Google Workspace **Business Standard / Plus**, **Enterprise Standard / Plus**, AI Expanded Access, Google AI Pro for Education, hoặc **Google AI Pro / Ultra**. Business Starter **không** có Pics.
- Pics hiện **chỉ chạy trên Desktop** và đang rollout dần.
- **Không bao giờ** đưa mật khẩu vào script. Đăng nhập làm **bằng tay một lần** bằng Chrome thường.
- Mỗi lần mở `pics.new` sẽ tạo **một file ảnh mới trong Drive** – xoá bớt file demo nếu không cần.

---

## PHẦN 0: CHUẨN BỊ (một lần)

1. Python 3.11 + `playwright`, `imageio-ffmpeg`, `Pillow` (đã cài). Chrome thật đã cài trên máy.
2. Mở Chrome **thường** (không phải Playwright – Google chặn đăng nhập trong trình duyệt tự động) với profile riêng:
   ```
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="D:\chrome-profiles\ai-quest" https://pics.new
   ```
3. Đăng nhập tài khoản Workspace bằng tay, kiểm tra thấy canvas Pics.
4. **Đóng hẳn** cửa sổ Chrome đó (Playwright không mở được profile đang dùng; nếu Chrome còn chạy nền thì tắt tiến trình của profile này).

> Không thể điều khiển cửa sổ Chrome đang dùng hằng ngày: từ Chrome 136, remote debugging bị chặn trên profile mặc định.

---

## PHẦN A: Nguồn chính thức (step-01 → step-11)

Chạy lại: `python trial_playwright.py --profile <thư mục profile tạm>` (không đăng nhập).

| # | File | Nội dung |
|---|------|----------|
| 1 | `step-01-youtube-video.png` | Trang video "Say hello to Google Pics" + mô tả "Built on our Nano Banana…" |
| 2 | `step-02-yt-generate-variations.png` | Khung hình 0:18 – Pics tạo 4 phiên bản, panel trái |
| 3 | `step-03-yt-add-element.png` | Khung hình 0:34 – sửa phần tử "An illustration of a taco" |
| 4 | `step-04-yt-edit-text.png` | Khung hình 0:39 – Edit text trên ảnh hộp quà |
| 5 | `step-05-yt-translate-result.png` | Khung hình 0:50 – poster đã dịch sang tiếng Tây Ban Nha |
| 6 | `step-06-yt-edit-in-slides.png` | Khung hình 1:00 – Pics trong Slides |
| 7 | `step-07-workspace-updates-post.png` | Bài Workspace Updates (GA 01/09/2026) |
| 8 | `step-08-product-page-hero.png` | Trang sản phẩm – hero |
| 9 | `step-09-product-page-features.png` | Trang sản phẩm – "No more prompt-and-pray" |
| 10 | `step-10-help-center-get-started.png` | Help Center "Get started with Google Pics" |
| 11 | `step-11-pics-signin-wall.png` | `pics.new` khi chưa đăng nhập → trang Sign in |

---

## PHẦN B: Thao tác thật trong Pics + Gemini (step-12 → step-19)

```
cd D:\ai_quest\blog-html\google-pics-vs-nanobanana
python record_pics_live.py
```

Script mở profile `D:\chrome-profiles\ai-quest` (đã đăng nhập), quay video cả phiên (~3 phút), hiện con trỏ đỏ + phụ đề trong video (ẩn khi chụp ảnh).

| Bước | File ảnh | Thao tác script làm | Ghi chú thực tế (03/10/2026) |
|------|----------|---------------------|------------------------------|
| 12 | `step-12-pics-home.png` | Mở `pics.new` | Tạo file mới trong Drive; canvas + prompt bar "Bring your ideas to life with Gemini" |
| 13 | `step-13-prompt-entered.png` | Gõ prompt banner Scuti AI (có rồng đỏ) | Prompt trong `record_pics_live.py` (`PROMPT_MAIN`) |
| 14 | `step-14-generated-variations.png` | Submit → chờ nút "Stop generating" biến mất → xem 3 thumbnail | ~15 s, **4 phiên bản**; sau đó bấm **Confirm** |
| 15 | `step-15-select-element-edit.png` | Tìm vùng màu đỏ trên ảnh, click lần lượt tới khi Pics báo "Describe changes for the … dragon" → gõ yêu cầu | Vị trí rồng mỗi lần tạo khác nhau nên script dò theo màu + nhãn đối tượng; dự phòng: sửa bằng prompt |
| 15b | `step-15b-element-edit-result.png` | **Add** → **Apply 1 edit** → chờ | Chỉ con rồng thay đổi (vẫy tay + khăn "AI") |
| 16 | `step-16-translate-text.png` | Prompt dịch toàn bộ chữ sang tiếng Việt | Đúng dấu; Pics dịch cả "AI QUEST" → "CHINH PHỤC AI"; sau đó **Confirm** |
| 17 | `step-17-crop-aspect-ratio.png` | Nút tỉ lệ → Transform → chọn **1:1** → chụp → về 16:9 → **Exit** | Có 16:9, 4:3, 3:2, 5:4, 1:1, xoay ±90° |
| 18 | `step-18-download-menu.png` | **Export** → chụp menu → **2K JPEG** | Lưu `images/pics-final-2k.jpg` (2752×1536) |
| 19 | `step-19-nanobanana-gemini.png` | Mở gemini.google.com, gõ `Create an image: ` + cùng prompt | ~25 s, 1 ảnh; ảnh lưu riêng `images/gemini-nanobanana.png`. Dòng footer chứa tên tổ chức Workspace đã được cắt khỏi ảnh |

Kết quả:
- `video/google-pics-live-session.mp4` – riêng phiên Pics + Gemini.
- `live_report.json` – thời gian từng bước.

**Riêng tư:** trước khi quay, thanh bên Gemini (lịch sử chat cá nhân) đã được **thu gọn** để không lọt vào ảnh/video.

---

## PHẦN C: Video hoàn chỉnh

```
python build_full_video.py
```

Ghép: phần nguồn chính thức (`video/google-pics-sources-part.mp4`, 1:24) + phiên Pics/Gemini thật (3:11) + cuộn blog VI từ đầu đến cuối
→ `video/google-pics-vs-nanobanana-demo.mp4` (~6:32, 1440×900).

---

## Danh sách ảnh

| # | File | Trạng thái |
|---|------|------------|
| 1–11 | `step-01` … `step-11` | Đã có (nguồn chính thức) |
| 12 | `step-12-pics-home.png` | Đã có (thật) |
| 13 | `step-13-prompt-entered.png` | Đã có (thật) |
| 14 | `step-14-generated-variations.png` | Đã có (thật) |
| 15 | `step-15-select-element-edit.png`, `step-15b-element-edit-result.png` | Đã có (thật) |
| 16 | `step-16-translate-text.png` | Đã có (thật) |
| 17 | `step-17-crop-aspect-ratio.png` | Đã có (thật) |
| 18 | `step-18-download-menu.png` + `pics-final-2k.jpg` | Đã có (thật) |
| 19 | `step-19-nanobanana-gemini.png` + `gemini-nanobanana.png` | Đã có (thật) |
