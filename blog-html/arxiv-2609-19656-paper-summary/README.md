# Self-Evolving Search Index (arXiv:2609.19656) – Tóm tắt paper

Blog AI Quest **Type 1 – Investigate What**: tóm tắt đóng góp kỹ thuật, phương pháp và kết quả chính của paper
[arXiv:2609.19656 – *Self-Evolving Search Index*](https://arxiv.org/abs/2609.19656) (Lee et al., 17/09/2026, cs.IR),
giải thích khái niệm bằng lời của mình, kèm bài học cá nhân và cách áp dụng vào dự án / vận hành tại Scuti AI.

## AI Quest Requirements

| # | Requirement | Deliverable |
|---|-------------|-------------|
| 1 | Tóm tắt đóng góp kỹ thuật, phương pháp, kết quả chính | Mục 1–6 trong blog |
| 2 | Viết bằng lời của mình, giải thích khái niệm (không dịch nguyên văn) | Toàn bài, sơ đồ tự vẽ (ảnh `diagram-*.png`) |
| 3 | Bài học cá nhân + cách áp dụng vào dự án & vận hành hằng ngày (bối cảnh Scuti AI) | Mục 7 trong blog |
| 4 | Hướng dẫn đơn giản để thử / áp dụng | Mục 8 trong blog |

## Nội dung blog

1. **Bối cảnh** – index key là gì, vì sao chiến lược tối ưu index cố định không thắng mọi môi trường
2. **Đóng góp chính** – framework Self-Index, kết quả nhất quán, lợi ích xuôi dòng
3. **Phương pháp** – Optimizer (Self-Diagnosis / Self-Revision / Self-Validation) + Query Simulator, ví dụ key tiến hóa
4. **Kết quả** – BRIGHT, table retrieval, BrowseComp-Plus (search agent), LongMemEval-V2 (agent memory), chi phí offline
5. **Phân tích** – ablation, nguồn câu hỏi, số vòng lặp, LLM backbone
6. **Giới hạn** – những ô không thắng, "Work in progress", chưa peer review
7. **Bài học & áp dụng tại Scuti AI** – RAG tài liệu tiếng Nhật, Text-to-SQL, agent memory, quy trình review nội dung LLM
8. **Hướng dẫn nhanh** – đọc paper, chạy repo chính thức, pseudo-code phiên bản mini
9. **Video demo** – nhúng MP4
10. **Kết luận & tài liệu tham khảo**

## Files

| File | Ngôn ngữ | Mô tả |
|------|----------|-------|
| `arxiv-2609-19656-paper-summary-blog.html` | Tiếng Việt | Blog chính |
| `arxiv-2609-19656-paper-summary-blog-en.html` | English | Bản tiếng Anh |
| `images/` | — | 25 ảnh PNG trên đĩa (17 ảnh chụp gốc + 8 bản `*-crop.png`); blog nhúng **11 ảnh**: 8 figure/table của paper ở bản crop (`step-04`, `06`–`12` `-crop.png`, chỉ giữ hình/bảng + caption, bỏ thanh menu arXiv, mục lục và đoạn văn xung quanh) + 3 sơ đồ tự vẽ (`diagram-0X-*.png`). Ảnh gốc được giữ nguyên |
| `video/arxiv-2609-19656-paper-summary-demo.mp4` | — | Video demo 2 phút 09 giây (2:08.7), 1440×900, H.264/yuv420p |
| `diagrams/*.html` | Tiếng Việt | Mã nguồn HTML/SVG của 3 sơ đồ minh họa |
| `capture_demo.py` | — | Script Playwright tái tạo toàn bộ ảnh + video |
| `capture_tables.py` | — | Script Playwright chụp riêng Table 1 và Table 3 (kèm caption, đủ bảng) từ bản HTML của paper |
| `source/` | — | Bản tải về của trang abstract, bản HTML và PDF của paper (để đối chiếu số liệu) |

### Danh sách ảnh

| Ảnh | Nội dung | Trong blog |
|-----|----------|-----------|
| `step-01-arxiv-abstract.png` | Trang abstract arXiv | Không (ảnh chụp trang/abstract của nguồn) |
| `step-02-html-paper-title.png` | Bản HTML (experimental), sau khi bấm link từ trang abstract | Không (ảnh chụp trang tiêu đề của nguồn) |
| `step-03-introduction.png` | Phần Introduction | Không (ảnh chụp đoạn văn Introduction) |
| `step-04-figure1-overview.png` | Figure 1 – tổng quan Self-Index | Không (bản gốc, blog dùng bản crop) |
| `step-04-figure1-overview-crop.png` | Crop từ `step-04-figure1-overview.png`: chỉ Figure 1 kèm caption | Ảnh 1 |
| `step-05-optimizer-section.png` | Section 3.2 – Optimizer | Không (ảnh chụp đoạn văn Section 3, trùng Figure 1) |
| `step-06-table1-bright.png` | Table 1 – kết quả BRIGHT | Không (bản gốc, blog dùng bản crop) |
| `step-06-table1-bright-crop.png` | Crop từ `step-06-table1-bright.png`: Table 1 bị cắt (thiếu caption, thiếu cột Final Avg./Δ) | Không (thay bằng bản full) |
| `step-06-table1-full.png` | Chụp riêng phần tử Table 1 trên bản HTML (`capture_tables.py`): đủ caption + toàn bộ bảng | Ảnh 5 |
| `step-07-table3-browsecomp.png` | Table 3 – search agent trên BrowseComp-Plus | Không (bản gốc, blog dùng bản crop) |
| `step-07-table3-browsecomp-crop.png` | Crop từ `step-07-table3-browsecomp.png`: Table 3 bị cắt (thiếu caption, thiếu phần cuối khối Kimi-K2.5) | Không (thay bằng bản full) |
| `step-07-table3-full.png` | Chụp riêng phần tử Table 3 trên bản HTML (`capture_tables.py`): đủ caption + toàn bộ bảng | Ảnh 6 |
| `step-08-figure2-online-cost.png` | Figure 2 & 3 – accuracy vs chi phí, độ bền theo kích thước corpus | Không (bản gốc, blog dùng bản crop) |
| `step-08-figure2-online-cost-crop.png` | Crop từ `step-08-figure2-online-cost.png`: chỉ Figure 2 kèm caption | Ảnh 7 |
| `step-09-table4-agent-memory.png` | Table 4 – LongMemEval-V2 | Không (bản gốc, blog dùng bản crop) |
| `step-09-table4-agent-memory-crop.png` | Crop từ `step-09-table4-agent-memory.png`: chỉ Table 4 kèm caption | Ảnh 8 |
| `step-10-table5-ablation.png` | Table 5 – ablation | Không (bản gốc, blog dùng bản crop) |
| `step-10-table5-ablation-crop.png` | Crop từ `step-10-table5-ablation.png`: chỉ Table 5 kèm caption | Ảnh 9 |
| `step-11-figure4-case-study.png` | Figure 4 (case study) & Figure 5 (nguồn câu hỏi) | Không (bản gốc, blog dùng bản crop) |
| `step-11-figure4-case-study-crop.png` | Crop từ `step-11-figure4-case-study.png`: chỉ Figure 4 kèm caption | Ảnh 4 |
| `step-12-figure6-evolution.png` | Figure 6 – nDCG@10 qua các vòng | Không (bản gốc, blog dùng bản crop) |
| `step-12-figure6-evolution-crop.png` | Crop từ `step-12-figure6-evolution.png`: chỉ Figure 6 kèm caption | Ảnh 10 |
| `step-13-github-repo-readme.png` | README repo chính thức trên GitHub | Không (ảnh chụp README GitHub) |
| `step-14-finished-blog.png` | Blog hoàn chỉnh mở bằng file:// (dùng cho README) | Không |
| `diagram-01-self-index-loop.png` | Sơ đồ tự vẽ: vòng lặp Self-Index + tham số cấu hình | Ảnh 2 |
| `diagram-02-key-evolution.png` | Sơ đồ tự vẽ: 2 case study key tiến hóa (#63→#2, #140→#3) | Ảnh 3 |
| `diagram-03-scuti-apply.png` | Sơ đồ tự vẽ: lộ trình PoC 4 tuần áp dụng tại Scuti (đề xuất cá nhân) | Ảnh 11 |

## Cách tạo ảnh và video

- Chạy `python capture_demo.py` (Python 3.11, `playwright`, `imageio-ffmpeg` đã cài sẵn).
- Một phiên Playwright duy nhất, Chrome thật (`channel="chrome"`, `headless=False`, viewport 1440×900, `record_video_dir="video_raw"`):
  1. mở trang abstract arXiv → bấm **HTML (experimental)**;
  2. cuộn mượt tới từng Figure/Table (Section 1, Fig 1, Sec 3.2, Table 1, 3, 4, 5, Fig 2, 4, 6) và chụp màn hình; sau đó crop riêng từng figure/table bằng PIL thành `*-crop.png` (ảnh gốc giữ nguyên);
  3. mở repo GitHub (trang public, không đăng nhập) và chụp README;
  4. mở 3 trang `diagrams/*.html` qua file:// và chụp phần tử `#card` thành PNG;
  5. mở blog tiếng Việt hoàn chỉnh qua file:// và cuộn từ đầu đến cuối.
- Mỗi thao tác chờ ~1–2,5 giây để video dễ xem. Sau khi đóng browser, file `.webm` được chuyển sang MP4 bằng ffmpeg đi kèm `imageio_ffmpeg` (`libx264`, `yuv420p`, `+faststart`), rồi xóa `video_raw/`.
- Text của paper được đọc từ bản HTML/PDF tải về (`source/`); mọi số liệu trong blog lấy trực tiếp từ paper v1.

## Nguồn tham khảo

- https://arxiv.org/abs/2609.19656 – trang abstract
- https://arxiv.org/html/2609.19656v1 – bản HTML (experimental)
- https://arxiv.org/pdf/2609.19656 – bản PDF
- https://github.com/augustinLib/Self-Index – code chính thức (README)

## Ghi chú trung thực

- Toàn bộ nguồn đều public, không gặp login wall, không đăng nhập tài khoản nào.
- **Chưa chạy code chính thức** của paper (cần GPU, Java 21, model Qwen3.6-35B-A3B và dataset lớn) – phần 8.2 chỉ trích lệnh từ README của repo. Pseudo-code ở mục 8.3 là bản rút gọn tự viết, chưa phải code chạy được.
- Lộ trình 4 tuần (ảnh `diagram-03`) và các ý áp dụng tại Scuti là đề xuất của người viết, chưa được kiểm chứng trong dự án thật.
- Paper tự ghi "Work in progress", chưa qua peer review; các model như GPT-5.4-nano, Gemini-3.7-Flash, Qwen3.6 được nêu đúng như trong paper.

---

Ngày tạo: 03/10/2026

## Thumbnail

`images/thumbnail.png`: 1280×720 (16:9), tiêu đề tiếng Anh bên trái, hình minh hoạ tự vẽ bên phải. Không dùng ảnh hay logo của bài nguồn. Dùng làm ảnh đại diện khi đăng lên blog công ty.
