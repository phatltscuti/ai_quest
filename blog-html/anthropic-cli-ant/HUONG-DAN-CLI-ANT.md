# Hướng dẫn demo Anthropic CLI (`ant`)

Đồng bộ với `anthropic-cli-ant-blog.html`. Luồng demo giả lập **đã có API key** (OAuth). Đường dẫn terminal: `C:\anthropic-cli-ant\`.

---

## Hướng dẫn chụp ảnh minh họa cho blog

Phần này **không nằm trong blog HTML** — chỉ dùng khi cần ảnh terminal. Có hai cách:

### Cách A — Fake terminal (khuyến nghị, nhanh)

Mở file HTML trong Chrome/Edge → chụp khung `vscode-panel` → lưu vào `images/`.

| Ảnh blog | Mở file fake-terminal | Nội dung cần thấy trong khung chụp |
|----------|----------------------|-------------------------------------|
| `step-00-install-windows.png` | `step-00-install-windows.html` | Script cài + `Get-ChildItem` có `ant.exe` |
| `step-01-ant-version-help.png` | `step-01-ant-version-help.html` | `--version` → `ant version 1.10.0` + `--help` |
| `step-02-auth-status-not-configured.png` | `step-02-auth-status-not-configured.html` | `auth status` → not configured |
| `step-03-auth-configured.png` | `step-03-auth-configured.html` | `auth login` OK + OAuth valid |
| `step-04-models-list.png` | `step-04-models-list.html` | `models list` + transform model IDs |
| `step-05-messages-create-success.png` | `step-05-messages-create-success.html` | `messages create` JSON + `--raw-output` |
| `step-06-beta-agents-help.png` | `step-06-beta-agents-help.html` | `beta:agents create` từ YAML |
| `step-07-transform-error.png` | `step-07-transform-error.html` | `--transform` trích text |
| `step-09-count-tokens.png` | `step-09-count-tokens.html` | `messages count-tokens` → `input_tokens` |
| `step-10-system-prompt.png` | `step-10-system-prompt.html` | `--system` + transform text |
| `step-11-multiturn-limit.png` | `step-11-multiturn-limit.html` | lỗi YAML multi-turn inline |
| `step-12-debug-mode.png` | `step-12-debug-mode.html` | `--debug` HTTP request/response |
| `step-13-beta-sessions-help.png` | `step-13-beta-sessions-help.html` | `beta:sessions --help` |
| `step-14-profile-help.png` | `step-14-profile-help.html` | `profile --help` |

**Tổng ảnh blog:** 14 (Step 7 không cần ảnh; Step 8–14 gồm bổ sung theo [Scuti testing guide](https://scuti.asia/anthropic-cli-ant-complete-installation-and-testing-guide/)).

**Index tất cả bước:** `fake-terminal/ant_terminal.html`

**Thao tác chụp:**

1. Mở file HTML (ví dụ `file:///.../fake-terminal/step-01-ant-version-help.html`).
2. `Windows + Shift + S` → chọn khung terminal (viền xám `vscode-panel`).
3. Paste vào Paint → Save As → `blog-html/anthropic-cli-ant/images/step-XX-....png`.

### Cách B — Chụp terminal thật

Chạy lệnh theo các bước bên dưới trên PowerShell thật, chụp màn hình terminal VS Code hoặc Windows Terminal.

---

## Chuẩn bị

Đọc: `demo-assets/CHUAN-BI-TRUOC-DEMO.md`

| Chuẩn bị | Chi tiết |
|----------|----------|
| Binary | `ant` v1.10.0 — [GitHub Releases](https://github.com/anthropics/anthropic-cli/releases/tag/v1.10.0) |
| Docs cài đặt | [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) — **không có tab Windows**; dùng zip Releases hoặc WSL |
| Credential | `ant auth login` (OAuth) hoặc `$env:ANTHROPIC_API_KEY` |
| Thư mục demo | `C:\anthropic-cli-ant\tools\` |

**Lưu ý:** `ant` ≠ Claude Code (`npm install -g @anthropic-ai/claude-code`).

---

## Bước 1 — Tải và cài `ant` trên Windows

**Mục tiêu:** Có `ant.exe` chạy được.

```powershell
cd C:\anthropic-cli-ant\demo-assets
.\01-install-windows.ps1
```

Hoặc thủ công:

```powershell
$installDir = "C:\anthropic-cli-ant\tools"
New-Item -ItemType Directory -Force -Path $installDir
Invoke-WebRequest -Uri "https://github.com/anthropics/anthropic-cli/releases/download/v1.10.0/ant_1.10.0_windows_amd64.zip" -OutFile "$installDir\ant.zip"
Expand-Archive -Path "$installDir\ant.zip" -DestinationPath $installDir -Force
cd $installDir
.\ant.exe --version
```

**Output kỳ vọng:**

```
ant version 1.10.0
```

---

## Bước 2 — Kiểm tra version và danh sách lệnh

```powershell
cd C:\anthropic-cli-ant\tools
.\ant.exe --version
.\ant.exe --help
```

**Output `--version`:** `ant version 1.10.0`

**Output `--help` (rút gọn):** liệt kê `auth`, `messages`, `models`, `beta:agents`, `beta:sessions`, …

---

## Bước 3 — Auth status (trước login)

```powershell
.\ant.exe auth status
```

**Output kỳ vọng:**

```
Credentials
  (profile "default" not configured — run `ant auth login` to set it up)
```

---

## Bước 4 — Thiết lập credential

**OAuth (máy dev):**

```powershell
.\ant.exe auth login
.\ant.exe auth status
```

**API key (CI/script):**

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

**Output sau OAuth:**

```
Credentials
  (active) * OAuth (Console)    valid
```

---

## Bước 5 — Liệt kê model

```powershell
.\ant.exe models list --format json --transform "data.#.id"
```

**Output:**

```json
[
  "claude-opus-4-8",
  "claude-sonnet-4-5-20250929",
  "claude-haiku-4-5-20251001"
]
```

---

## Bước 6 — Gọi Messages API (first request)

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 128 `
  --message "{role: user, content: 'Hello from ant CLI test'}"
```

**Output (rút gọn, theo [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart)):**

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "role": "assistant",
  "content": [
    { "type": "text", "text": "Hello! How are you doing today? Is there something I can help you with?" }
  ],
  "usage": { "input_tokens": 12, "output_tokens": 20 }
}
```

**Chỉ lấy text:**

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 128 `
  --message "{role: user, content: 'Hello'}" `
  --transform "content.#(type==`"text`").text" `
  --raw-output
```

---

## Bước 7 — Demo `--transform`

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 256 `
  --message "{role: user, content: 'Summarize what ant CLI does in one sentence.'}" `
  --transform "content.#(type==`"text`").text" `
  --raw-output
```

---

## Bước 8 — Managed Agents

```powershell
.\ant.exe beta:agents --help
Get-Content C:\anthropic-cli-ant\demo-assets\03-managed-agent-sample.yaml | .\ant.exe beta:agents create
.\ant.exe beta:agents list --transform "data.#.name"
```

---

## Bước 9 — Đếm token (`count-tokens`)

Theo [Scuti Test 3](https://scuti.asia/anthropic-cli-ant-complete-installation-and-testing-guide/#testing). Không tốn token API.

```powershell
.\ant.exe messages count-tokens `
  --model claude-sonnet-4-5-20250929 `
  --message "{role: user, content: 'This is a test message to count tokens'}"
```

**Output:** `{ "input_tokens": 15 }`

**Ảnh:** `images/step-09-count-tokens.png` ← `fake-terminal/step-09-count-tokens.html`

---

## Bước 10 — System prompt

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 150 `
  --system 'You are a helpful assistant that answers in exactly 2 sentences.' `
  --message "{role: user, content: 'Explain quantum computing'}" `
  --transform "content.#(type==`"text`").text" --raw-output
```

**Ảnh:** `images/step-10-system-prompt.png`

---

## Bước 11 — Multi-turn inline (giới hạn đã biết)

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 200 `
  --message "[{role: user, content: 'Hello'}, {role: assistant, content: 'Hi!'}, {role: user, content: 'What is your purpose?'}]"
```

**Output:** lỗi YAML `sequence was used where mapping is expected`. Workaround: `beta:sessions` hoặc JSONL.

**Ảnh:** `images/step-11-multiturn-limit.png`

---

## Bước 12 — Debug mode

```powershell
.\ant.exe --debug messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 50 `
  --message "{role: user, content: 'Test'}"
```

**Ảnh:** `images/step-12-debug-mode.png`

---

## Bước 13 — beta:sessions

```powershell
.\ant.exe beta:sessions --help
```

**Ảnh:** `images/step-13-beta-sessions-help.png`

---

## Bước 14 — Profile

```powershell
.\ant.exe profile --help
```

**Ảnh:** `images/step-14-profile-help.png`

---

## Bước 15 — Shell completion (tuỳ chọn)

```powershell
.\ant.exe @completion powershell | Out-String | Invoke-Expression
```

---

## Lỗi thường gặp

| Triệu chứng | Nguyên nhân | Cách xử lý |
|-------------|-------------|------------|
| Không thấy hướng dẫn Windows trong docs | Quickstart chỉ có macOS/Linux/Go | Tải zip từ GitHub Releases |
| `flow mapping end token` | YAML thiếu quote trên PowerShell | `content: '...'` trong braces |
| `x-api-key header is required` | Chưa auth | Bước 4 |
| Multi-turn inline array | `--message "[{...}, ...]"` | Dùng `beta:sessions` (Bước 13) |
| Nhầm với Claude Code | Cài nhầm npm package | Dùng `anthropics/anthropic-cli` |

---

## Tham chiếu

- Repo: https://github.com/anthropics/anthropic-cli
- Docs: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart
- Bài X (Madni): https://x.com/hey_madni/article/2063606029146034375
- Scuti testing guide: https://scuti.asia/anthropic-cli-ant-complete-installation-and-testing-guide/
- Blog: `anthropic-cli-ant-blog.html` / `anthropic-cli-ant-blog-en.html`
