# Plan Quest T11 (5 quest)

> Nguồn: `QuestT11.txt` · Lập ngày 2026-11-20
> Thứ tự: **Quest 3 → Quest 5** (ưu tiên), sau đó Quest 2 → Quest 1 → Quest 4.

## Quy ước chung (theo các blog đã có trong `blog-html/`)

Mỗi quest một thư mục `blog-html/<slug>/` gồm:

| File / thư mục | Nội dung |
|---|---|
| `<slug>-blog.html` | Blog tiếng Việt (bản chính) |
| `<slug>-blog-en.html` | Bản tiếng Anh |
| `HUONG-DAN-DEMO-QUAY-VIDEO.md` | Kịch bản quay: từng bước, lệnh, thời lượng |
| `demo-assets/` | Code, script, dữ liệu mẫu (không bí mật) |
| `images/` | Screenshot `step-XX-*.png` cắt từ video |
| `videos/` | Video demo `.mp4` (full + từng đoạn) |

**Cách quay video:** `ffmpeg` (gdigrab) quay toàn màn hình 1920×1080, 30fps.
- Phần terminal: mở cửa sổ PowerShell **hiển thị trên màn hình**, chạy script demo (gõ lệnh có hiệu ứng typewriter) → mọi lệnh đều nằm trong video.
- Phần Chrome: mở Chrome thật (profile riêng cho demo), thao tác bằng Playwright (headed) hoặc bạn thao tác tay theo kịch bản trong lúc mình quay.
- Hậu kỳ: ghép đoạn, chèn chú thích bước (`drawtext`), xuất `full-demo.mp4` + cắt screenshot cho blog.

**Bảo mật:** chỉ dùng dữ liệu tự tạo / tài liệu public; API key đọc từ biến môi trường, không bao giờ xuất hiện trên màn hình hay trong repo (`.env` vào `.gitignore`).

---

## Quest 3 – Gemini Decisions API vs text-gen truyền thống  (ƯU TIÊN 1)

Thư mục: `blog-html/gemini-decisions-api-classification/`

**Bối cảnh (từ bài gốc, 11/11/2026):** model `gemini-decision-1`, gọi qua `client.decisions.create(...)` (SDK `google-genai`, `api_version=v1beta`). Chấm điểm các lựa chọn trong 1 forward pass, trả xác suất + confidence 0–1. Câu hỏi dạng `noul` (Yes/No), `choice` (2–255 nhãn), `score` (rubric). Giá $0.10/1M input token, output $0. Latency công bố 150–250 ms.

**Thiết kế thí nghiệm**
1. Dataset ~40 mẫu, tự tạo, có nhãn đúng (ground truth):
   - 20 tài liệu PDF/ảnh: hoá đơn, báo giá, hợp đồng, đơn xin nghỉ, CV mẫu (sinh bằng script, dữ liệu giả).
   - 20 ảnh public (license tự do): phân loại tình trạng hàng hoá / bối cảnh văn phòng.
   - Cố ý thêm 5–6 mẫu “khó” (scan mờ, xoay, 2 loại lẫn nhau) để xem confidence.
2. So sánh 3 phương pháp trên cùng dataset:
   - **A.** `gemini-decision-1` – Decisions API (`choice` + `noul` + `score` trong 1 request).
   - **B.** Gemini Flash-Lite qua generate/Interactions API, prompt yêu cầu trả JSON nhãn.
   - **C.** Gemini Flash (model mạnh hơn) cùng prompt – làm mốc chất lượng.
3. Đo: accuracy, confusion matrix, latency p50/p95, token in/out thực tế → chi phí / 1.000 tài liệu; thêm thử nghiệm “ngưỡng confidence” (bao nhiêu % được tự động, bao nhiêu % đẩy cho người duyệt).
4. Mỗi phương pháp chạy 3 lần để tính độ ổn định.

**Bước làm & quay video**
| # | Bước | Quay |
|---|---|---|
| 1 | Lấy API key trên AI Studio (che key) | Chrome |
| 2 | Mở AI Studio Playground của Decisions API, chạy thử 1 ảnh | Chrome |
| 3 | Cài Python, `pip install google-genai`, tạo venv | Terminal |
| 4 | Chạy `make_dataset.py` → xem tài liệu mẫu | Terminal + Explorer |
| 5 | Chạy `run_decisions.py`, `run_textgen.py` | Terminal |
| 6 | Chạy `report.py` → mở `report.html` (bảng + biểu đồ) | Terminal + Chrome |
| 7 | Demo routing theo confidence (case khó → human review) | Terminal |

**Blog:** Giới thiệu → cách hoạt động (khác text-gen ở đâu) → setup → code → kết quả (bảng accuracy/speed/cost, biểu đồ) → phân tích khi nào nên dùng → áp dụng vào công việc hằng ngày của mình → kết luận.

---

## Quest 5 – Gemini Notebook interactive site vs RAG truyền thống  (ƯU TIÊN 2)

Thư mục: `blog-html/gemini-notebook-interactive-sites/`

**Bối cảnh (bài gốc 16/11/2026):** vào `https://notebook.google.com/`, thêm nguồn, gõ “make me a site …” trong chat Notebook → sinh website/dashboard tương tác → “Open in a new tab” / share.

**Nguồn tài liệu (không bí mật):** bộ manual sản phẩm **hư cấu** do mình viết (vd. “Máy lọc không khí AQ-200”: thông số, hướng dẫn, mã lỗi, FAQ, bảng giá linh kiện) + 1 manual public. Không dùng tài liệu nội bộ/khách hàng.

**Bước làm & quay video**
| # | Bước | Quay |
|---|---|---|
| 1 | Tạo bộ manual mẫu (PDF/Docs) | Terminal/Explorer |
| 2 | Tạo Notebook, upload nguồn | Chrome |
| 3 | Prompt 1: “make me a site” – trang hướng dẫn tương tác (tra mã lỗi, checklist bảo trì) | Chrome |
| 4 | Prompt 2: dashboard (so sánh model, chi phí linh kiện theo tháng) | Chrome |
| 5 | Chỉnh sửa bằng prompt tiếp, Open in new tab, share | Chrome |
| 6 | Dựng RAG truyền thống tối giản (Python: chunk → embedding → retrieve → answer) trên cùng tài liệu | Terminal |
| 7 | Hỏi cùng 8–10 câu cho cả 2 bên, chấm đúng/sai, có trích nguồn không | Terminal + Chrome |

**So sánh với RAG:** đầu ra (trang tương tác vs câu trả lời text), độ chính xác/hallucination, thời gian dựng, khả năng chia sẻ, cập nhật khi tài liệu đổi, chi phí, kiểm soát dữ liệu.

**Blog:** cùng cấu trúc Quest 3 + bảng khác biệt Notebook site vs RAG + ý kiến cá nhân + áp dụng hằng ngày.

---

## Quest 2 – Agent Skill chung cho Claude Code & Codex  (sau)

Thư mục: `blog-html/agent-skill-claude-codex/`
- Viết 2 skill theo chuẩn agentskills.io (`SKILL.md` + frontmatter `name`, `description`, thư mục `references/`, `scripts/`): `requirement-definition`, `code-review`.
- Cài vào `.claude/skills/` và thư mục skill của Codex; chạy cùng input (1 yêu cầu tính năng + 1 PR mẫu có bug cố ý) trên cả 2 tool.
- So sánh: skill có được kích hoạt tự động không, output có theo đúng template không, số bug bắt được, chỗ nào phải chỉnh riêng cho từng tool.
- Video: cài skill, chạy Claude Code, chạy Codex CLI (toàn bộ trong terminal).
- Cần: tài khoản Codex/OpenAI.

## Quest 1 – So sánh GPT-6.2 / Claude Fable 5.2 / Gemini 4  (sau)

Thư mục: `blog-html/llm-compare-gpt62-fable52-gemini4/`
- 1 task dev cố định (vd. viết API CRUD + test + refactor theo spec), cùng prompt, cùng harness Python gọi 3 API.
- Đo: test pass rate, review chất lượng code theo rubric, thời gian, token & chi phí thực tế.
- Video: chạy harness 3 model, chạy test, xem report.
- Cần: API key OpenAI, Anthropic, Gemini.

## Quest 4 – ChatGPT for Sales + HubSpot  (Type 1, sau)

Thư mục: `blog-html/chatgpt-for-sales-hubspot/`
- Bài phân tích (không dịch/tóm tắt): bảng hoạt động sales → mức tự động hoá (%) có lý do; workflow khi nối HubSpot; ý kiến áp dụng cho công ty.
- Nếu có tài khoản: demo trên dữ liệu công ty giả (HubSpot free + ChatGPT); nếu không, chỉ screenshot tài liệu public.

---

## Cần bạn chuẩn bị trước khi bắt đầu Quest 3 & 5
1. Cho phép cài: Python 3.12, ffmpeg, Node.js (qua `winget`).
2. Gemini API key (AI Studio) → đặt biến môi trường `GEMINI_API_KEY` (mình không xem key).
3. Đăng nhập Google account dùng cho Gemini Notebook trên Chrome (profile demo).
4. Xác nhận cách điều khiển Chrome (xem câu hỏi trong chat).
