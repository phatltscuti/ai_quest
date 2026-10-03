# Báo cáo tổng hợp – 10 blog AI Quest (cập nhật 03/10/2026)

10 blog theo đề bài trong `D:\ai_quest\DeBai.txt`, mỗi blog nằm trong 1 folder riêng ở `D:\ai_quest\blog-html\`.

Mỗi folder có:
- `<slug>-blog.html`: bản tiếng Việt (bản chính)
- `<slug>-blog-en.html`: bản tiếng Anh
- `README.md` chi tiết riêng cho blog đó
- `images/`: ảnh dùng trong blog, kèm `thumbnail.png` (1280×720) làm ảnh đại diện khi đăng
- `video/`: video quay lại quá trình làm
- Script Python để chạy lại toàn bộ

Blog Type 2 có thêm `HUONG-DAN-DEMO-CHUP-ANH.md` và video sản phẩm.

## Quy tắc nội dung (áp dụng cho cả 10 blog)
- **Không chụp nội dung bài nguồn** (đoạn văn, tweet, README, trang web) để đưa vào blog. Chỉ giữ biểu đồ, bảng-hình và sơ đồ, cắt gọn chỉ còn phần hình (`*-crop.png`), cùng các sơ đồ tự vẽ.
- **Không nhắc công cụ tự động hoá** (Playwright…) trong chữ của blog. Chi tiết kỹ thuật chỉ ghi trong README.
- **Ngắn gọn**, mỗi bước 1 ảnh.
- Ảnh bị bỏ khỏi blog vẫn còn trên đĩa để đối chiếu. README từng blog ghi rõ ảnh nào đang dùng.

Đã kiểm tra tự động: mọi link ảnh/video trong 20 file HTML đều tồn tại; độ dài video đo bằng ffmpeg.

## Bảng tổng hợp

| # | Loại | Folder | Ảnh trong blog | Video | Thumbnail | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | Type 1 | [arxiv-2609-19656-paper-summary](arxiv-2609-19656-paper-summary/) | 11 | demo 2:08 | ✅ | Sẵn sàng đăng |
| 2 | Type 2 | [scuti-ai-motion-graphics-video](scuti-ai-motion-graphics-video/) | 6 | **sản phẩm v4 0:18 (1080p, có nhạc)**; quá trình 4:03 | ✅ | **Đã đăng** |
| 3 | Type 1 | [anthropic-test-impact-analysis-ci](anthropic-test-impact-analysis-ci/) | 8 | demo 1:31 | ✅ | Sẵn sàng đăng |
| 4 | Type 1 | [company-wide-ai-adoption-roadmap](company-wide-ai-adoption-roadmap/) | 11 | demo 2:56 | ✅ | Sẵn sàng đăng |
| 5 | Type 1 | [how-claude-ai-got-faster](how-claude-ai-got-faster/) | 8 | demo 2:11 | ✅ | Sẵn sàng đăng |
| 6 | Type 2 | [scuti-ai-red-dragon-talking-video](scuti-ai-red-dragon-talking-video/) | 8 | **sản phẩm 0:33 (có giọng nói)**; demo 1:50 | – | **Đã đăng** |
| 7 | Type 1 | [greg-isenberg-x-post-insights](greg-isenberg-x-post-insights/) | 6 | demo 2:07 | ✅ | Sẵn sàng đăng |
| 8 | Type 1 | [ai-hr-performance-evaluation](ai-hr-performance-evaluation/) | 5 | demo 4:23 | ✅ | Sẵn sàng đăng |
| 9 | Type 1 | [ai-driven-code-modernization-prep](ai-driven-code-modernization-prep/) | 2 | demo 2:13 | ✅ | Sẵn sàng đăng |
| 10 | Type 2 | [google-pics-vs-nanobanana](google-pics-vs-nanobanana/) | 21 | **demo hoàn chỉnh 6:32** (gồm phiên dùng thật Pics + Gemini 3:11) | – | **Đã đăng** |

Ghi chú:
- "Ảnh trong blog" là số ảnh mỗi file HTML, chưa tính thumbnail.
- Các video quá trình **không có tiếng**. Video sản phẩm của blog 2 và blog 6 **có audio**.
- Video demo của blog Type 1 quay trước đợt dọn ảnh, nên vẫn có cảnh lướt qua bài nguồn. Phần chữ trong blog đã không còn nhắc công cụ quay.

## Chi tiết từng blog

### 1. Paper arXiv 2609.19656 – "Self-Evolving Search Index"
- **Nội dung:** đóng góp chính; phương pháp (Self-Diagnosis / Self-Revision / Self-Validation + Query Simulator); kết quả trên BRIGHT, truy xuất bảng, BrowseComp-Plus, LongMemEval-V2; ablation; giới hạn; cách áp dụng cho RAG tài liệu tiếng Nhật, Text-to-SQL và agent memory.
- **Ảnh (11):** 8 Figure/Table của paper, đã cắt chỉ còn phần hình (Table 1 và Table 3 chụp lại đầy đủ kèm caption: `step-06-table1-full.png`, `step-07-table3-full.png`), cùng 3 sơ đồ tự vẽ. Đã bỏ ảnh chụp abstract, introduction, trang tiêu đề, README GitHub.
- **Lưu ý:**
  - Code chính thức của paper chưa được chạy (cần GPU và model 35B). Pseudo-code trong blog là bản tự rút gọn.
  - Lộ trình PoC 4 tuần là đề xuất cá nhân.

### 2. Video motion graphics giới thiệu Scuti AI – đã đăng
- **Blog:**
  - Mục 1: giới thiệu + 3 prompt (storyboard → build → critic).
  - Mục 4: demo Studio 4 bước.
  - Mục 5: critic v1 → v4.
  - Mục 6: Claude Code trong terminal (critic vòng 3, 2 bước).
- **Thành phẩm:** `video/scuti-ai-motion-graphics.mp4` là **v4**: 18 giây, 1920×1080, 30 fps, có nhạc. Bản v1/v2/v3 giữ để so sánh.
- **Video quá trình:** `video/scuti-ai-motion-graphics-video-demo1.mp4` (4:03).
  - 0:00–1:50: phiên Claude Code trong terminal, đoạn chờ được tua nhanh.
  - 1:50–4:03: demo Studio.
- **Thumbnail:** "Making a Motion Graphics Intro for Scuti AI with Code".
- **Lưu ý:**
  - Không dùng HyperFrames vì cần Node ≥ 22, máy đang chạy Node 16. Renderer tự làm theo cùng nguyên lý.
  - Rồng và logo dựng bằng SVG, nên thay bằng asset chính thức.
  - Critic vòng 3 còn 6 lỗi minor chưa sửa (`animation/critic-notes-v3.md`).

### 3. Anthropic – Test Impact Analysis cho CI thời agentic coding
- **Nội dung:** thách thức của agentic coding với CI; cơ chế TIA được scale (listener → journal → rollup → selector); số liệu từ bài gốc; lộ trình áp dụng CI/CD cho dự án khách Nhật.
- **Ảnh (8):** 5 biểu đồ/sơ đồ của bài gốc và 3 sơ đồ tự làm. Đã bỏ ảnh chụp đầu bài, đoạn chữ, thread Slack/hội thoại.
- **File thêm:** `tia_demo.py`, script minh họa tự viết, chạy được.
- **Lưu ý:**
  - Bài gốc không công bố thuật toán chi tiết, nên dependency map trong script là minh họa (blog có ghi rõ).
  - Từ "Playwright" còn lại trong blog chỉ là nội dung: link sang bài `playwright-parallel-e2e-ci` và lệnh `playwright test --only-changed`.

### 4. Lộ trình triển khai AI toàn công ty (LMI + SmartHR)
- **Ảnh (11):** 8 slide quan trọng nhất (đã cắt viền trình xem slide) và 3 sơ đồ tự vẽ.
  - LMI: kết quả, hai bức tường, outcome map, guardrail 3 cấp.
  - SmartHR: 5As, mô hình vận hành, đo lường 5 tầng, ba bức tường.
- **Nội dung:** lộ trình 5 giai đoạn, tổ chức 4 lớp, 5 nút thắt và cách gỡ, bảng so sánh LMI / SmartHR / Scuti, 6 chiến lược S1–S6 kèm lộ trình 6 tháng.
- **Lưu ý:**
  - Phần **"Scuti hiện tại" là giả định**, cần bạn kiểm tra lại.
  - Các mốc tháng là đề xuất cá nhân.
  - Tỉ lệ guardrail: slide 27 ghi khoảng 70/20/10%, slide 30 ghi "tỉ lệ hiện tại" 85/10/5%. Blog nêu cả hai và ghi rõ đây là số xấp xỉ.

### 5. How we made Claude AI faster
- **Nội dung:** đủ 5 nhóm chiến lược, case study ngân sách 8 ms/frame, bảng áp dụng cho dự án web/app, ví dụ size-limit / web-vitals.
- **Ảnh (8):** 4 biểu đồ/sơ đồ của bài gốc (đã cắt, `*-crop.png`) và 4 sơ đồ tự vẽ. Đã bỏ ảnh chụp đầu bài, các đoạn chữ, thread Slack.
- **Lưu ý:** đã loại một số liệu do WebFetch tự sinh ra, không có trong bài gốc.

### 6. Video Rồng Đỏ biết nói giới thiệu Scuti AI – đã đăng
- **Blog:** khoảng 20 KB. Mục 1 tóm tắt ý tưởng, kèm prompt và đoạn code tính độ mở miệng. Demo 8 bước trên **Rồng Đỏ Studio** (`studio/`).
- **Thành phẩm:** `video/scuti-ai-red-dragon.mp4`, dài 33,3 giây, 1280×720, có tiếng.
- **Video quá trình:** `video/scuti-ai-red-dragon-talking-video-demo.mp4` (1:50).
- **Lưu ý:**
  - Lip-sync theo âm lượng, không theo âm vị.
  - Rồng do AI vẽ lại, không phải mascot chính thức.
  - edge-tts là dịch vụ không chính thức, cần kiểm tra điều khoản nếu dùng thương mại.

### 7. Greg Isenberg – "$5T opportunity: AI Roll Ups"
- **Nội dung:** playbook mua lại doanh nghiệp dịch vụ và để AI agent làm back-office; 5 bài học cá nhân; 5 bước áp dụng tại Scuti, kèm mẫu `corrections-log.md`.
- **Ảnh (6):** 4 hình minh hoạ gốc của tác giả (bản ảnh sạch `figure-01…04`, không kèm chữ của bài) và 2 infographic tự làm. Đã bỏ ảnh chụp trang X, JSON, các đoạn chữ.
- **Lưu ý:** số liệu trong bài là do tác giả tự báo cáo, blog có ghi rõ.

### 8. AI trong đánh giá nhân sự (note.com Ubie + webinar YouTube)
- **Nội dung:**
  - Thu thập dữ liệu hằng ngày: Slack, Jira, GitHub, Notion… → BigQuery → Activity Report.
  - Fact Sheet → Evaluation Report → Companion agent; rubric 3 tầng.
  - Áp dụng cho HR Scuti, kèm phần quyền riêng tư (Nghị định 13/2023).
- **Ảnh (5):**
  - Sơ đồ 成果×能力 của bài note, đã cắt chỉ còn phần hình.
  - 2 slide webinar, đã bỏ phụ đề và khung người nói.
  - 2 sơ đồ tự vẽ.
  - Đã bỏ 16 ảnh chụp trang note/YouTube.
- **Lưu ý:**
  - Transcript YouTube lỗi, nên dùng phụ đề tự động tiếng Nhật và đối chiếu lại với slide.
  - Thông tin về Luật Bảo vệ dữ liệu cá nhân 2025 chưa được kiểm chứng.

### 9. Chuẩn bị cho dự án hiện đại hoá code bằng AI
- **Nội dung:**
  - 6 bước chuẩn bị theo bài gốc, chi phí token.
  - Áp dụng cho dự án legacy PHP/Java/VB của khách Nhật, kèm Preparation Checklist và prompt kick-off mẫu.
- **Ảnh (2):** 2 sơ đồ tự vẽ. Bản EN dùng ảnh tiếng Anh riêng (`*-en.png`). Đã bỏ 8 ảnh chụp từng mục của bài gốc.
- **Lưu ý:** thông tin plugin lấy từ README GitHub (nguồn phụ).

### 10. Google Pics vs NanoBanana – đã đăng
- **Nội dung:** tóm tắt tính năng Pics và bảng so sánh 11 tiêu chí. Ý chính: Pics chạy trên NanoBanana và là lớp canvas để thiết kế.
- **Demo thật** bằng tài khoản Workspace (profile riêng `D:\chrome-profiles\ai-quest`, `record_pics_live.py`):
  - Tạo banner có rồng đỏ.
  - Sửa theo phần tử.
  - Dịch chữ sang tiếng Việt.
  - Transform.
  - Export 2K.
  - So sánh với Gemini.
- **Video hoàn chỉnh** `video/google-pics-vs-nanobanana-demo.mp4` (6:32).
- **Lưu ý:** các file "Scuti AI Quest Banner" / "Untitled image" tạo trong lúc demo vẫn còn trong Drive của tài khoản phatlt@scuti.asia.

## Việc cần bạn kiểm tra trước khi đăng 7 blog còn lại
1. **Blog 4** (và phần "áp dụng tại Scuti" ở các blog khác): xem lại các giả định về quy trình hiện tại của công ty.
2. Đọc lại phần "bài học cá nhân" và chỉnh giọng văn cho đúng trải nghiệm của bạn.
3. Khi đăng, dùng `images/thumbnail.png` của từng blog làm ảnh đại diện.
4. **Blog 10:** dọn các file Pics demo trong Drive nếu cần.
5. Chưa commit git.

## Môi trường đã cài
- Python: `playwright` (dùng Chrome có sẵn qua `channel="chrome"`), `imageio-ffmpeg` (ffmpeg đi kèm), `edge-tts`, `Pillow`
- `playwright install ffmpeg` để quay video
