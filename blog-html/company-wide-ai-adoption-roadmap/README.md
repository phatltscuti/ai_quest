# Đưa AI vào toàn công ty: Lộ trình, cơ cấu tổ chức và cách vượt nút thắt

Blog AI Quest – Type 1 (Investigate What): tổng hợp trừu tượng lộ trình, cơ cấu tổ chức cần có và chiến lược vượt nút thắt khi triển khai AI toàn công ty, học từ 2 slide deck tiếng Nhật (Link and Motivation, SmartHR), so sánh với Scuti AI (giả định theo góc nhìn tác giả) và đề xuất 6 chiến lược sẽ thử.

## Nội dung

| File / thư mục | Mô tả |
|------|--------|
| `company-wide-ai-adoption-roadmap-blog.html` | Blog tiếng Việt (bản chính) |
| `company-wide-ai-adoption-roadmap-blog-en.html` | Blog tiếng Anh |
| `images/step-02, 03, 08, 09-lmi-*-crop.png` | 4 slide LMI dùng trong blog (bản đã cắt bỏ viền và thanh tiến trình của trình xem slide): step-02 (s4 kết quả), 03 (s9 hai bức tường), 08 (s20 outcome map), 09 (s27 cấp guardrail) |
| `images/step-16, 18, 19, 20-smarthr-*-crop.png` | 4 slide SmartHR dùng trong blog (bản đã cắt): step-16 (s10 5As), 18 (s13 mô hình vận hành), 19 (s14 đo lường 5 tầng), 20 (s18 ba bức tường) |
| `images/step-XX-*.png` (bản gốc, không có `-crop`) | Ảnh gốc của tất cả slide đã chụp (kể cả 8 slide trên) – vẫn giữ trên đĩa nhưng **không dùng trong blog**. Các slide đã bỏ khỏi bài: LMI s1, s12, s13, s14, s17, s32, s42, s44; SmartHR s1, s8, s9, s12, s20 |
| `images/diagram-roadmap(-en).png` | Sơ đồ A – lộ trình 5 giai đoạn (VI/EN) |
| `images/diagram-org-structure(-en).png` | Sơ đồ B – cơ cấu tổ chức (VI/EN) |
| `images/diagram-bottlenecks(-en).png` | Sơ đồ C – bản đồ nút thắt → cách gỡ (VI/EN) |
| `video/company-wide-ai-adoption-roadmap-demo.mp4` | Video toàn bộ phiên nghiên cứu (~2 phút 56 giây, 1440×900) |
| `scripts/` | Script đã dùng (xem bên dưới) + transcript text của 2 deck |

Blog dùng tổng cộng **11 ảnh** mỗi bản (VI/EN): 8 slide mang khung/lộ trình/kết quả cốt lõi (Ảnh 1–8, dùng bản `-crop.png`) + 3 sơ đồ tự vẽ (Hình A–C).

## Cấu trúc bài viết

1. Hai nguồn tham khảo (quy mô, hiện trạng)
2. Ý tưởng cốt lõi: AI adoption là thay đổi tổ chức, không phải roll-out tool
3. Lộ trình 5 giai đoạn (tổng hợp) – sơ đồ A
4. Cơ cấu tổ chức cần có – sơ đồ B
5. Năm nút thắt và cách gỡ (guardrail theo cấp độ, golden path “Fit Journey”) – sơ đồ C
6. Bài học rút ra theo cách hiểu của tác giả
7. So sánh với Scuti AI (bảng so sánh, các giả định ghi rõ)
8. 6 chiến lược sẽ thử tại Scuti + cách áp dụng + lộ trình 6 tháng
9. Video nghiên cứu
10. Kết luận

## Nguồn

- [Link and Motivation – 全社員がAIを「使う」の次へ (PEK2026), Speaker Deck, 25/09/2026](https://speakerdeck.com/lmi/pek2026-link-and-motivation) – 45 slide
- [SmartHR – SmartHRの全社AI推進は、どう始まったか, Speaker Deck, 28/09/2026](https://speakerdeck.com/yoshikikonishi_/smarthr-no-zensha-ai-suishin-ha-dou-hajimata-ka) – 20 slide

Phần “Scuti hiện tại” trong blog là **giả định / quan sát cá nhân của tác giả**, không phải số liệu chính thức.

## Cách tạo ảnh & video

| Script | Việc làm |
|--------|----------|
| `scripts/fetch_transcripts.py` | Tải HTML 2 trang Speaker Deck, trích transcript từng slide → `scripts/lmi_transcript.txt`, `scripts/smarthr_transcript.txt` (dùng để đọc nội dung chính xác, kể cả chữ nhỏ) |
| `scripts/capture_slides.py` | Python Playwright + Chrome thật (`channel="chrome"`, `headless=False`, 1440×900): mở deck, lật từng slide bằng phím → trong player, dừng và chụp element player ở slide quan trọng → `images/step-XX-*.png` |
| `scripts/make_diagrams.py` | Dựng 3 sơ đồ bằng HTML/CSS + SVG (`scripts/diagrams/*.html`), render PNG bằng Playwright → `images/diagram-*.png` (VI + EN) |
| `scripts/record_demo.py` | **Một phiên Playwright duy nhất có ghi hình** (`record_video_dir="video_raw"`): lật 2 deck (đồng thời chụp lại ảnh step), mở 3 sơ đồ, mở blog qua `file://` và cuộn từ đầu đến cuối → chuyển webm → mp4 (libx264, yuv420p) bằng ffmpeg của `imageio-ffmpeg` → xoá `video_raw` |

Chạy lại: `cd scripts && python fetch_transcripts.py && python make_diagrams.py && python record_demo.py`

Không gặp login wall: cả 2 deck xem công khai, không cần đăng nhập.

---
Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
