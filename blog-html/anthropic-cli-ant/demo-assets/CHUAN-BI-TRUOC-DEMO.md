# Chuẩn bị trước khi demo Anthropic CLI (`ant`)

## Yêu cầu

| Hạng mục | Chi tiết |
|----------|----------|
| Hệ điều hành | Windows 10/11, macOS, hoặc Linux/WSL |
| Tài khoản | Claude Developer Platform (Console) |
| Credential | Một trong hai: `ANTHROPIC_API_KEY` hoặc `ant auth login` (OAuth) |
| Binary | `ant` v1.10.0+ (tải từ GitHub Releases hoặc Homebrew/Go) |

## Phân biệt quan trọng

- **`ant`** = CLI chính thức cho **Claude API / Developer Platform** (Go binary, repo `anthropics/anthropic-cli`).
- **`claude`** (Claude Code) = agent coding trong terminal (`npm install -g @anthropic-ai/claude-code`). Đây là công cụ khác.
- Theo tài liệu Anthropic, Claude Code có thể gọi `ant` qua skill `claude-api` — hai công cụ bổ sung nhau.

## Bước chuẩn bị (Windows)

1. Tạo thư mục cài đặt (ảo / thực tế), ví dụ:
   `C:\anthropic-cli-ant\tools`
2. Tải `ant_1.10.0_windows_amd64.zip` từ:
   https://github.com/anthropics/anthropic-cli/releases/tag/v1.10.0
3. Giải nén → có `ant.exe`.
4. Mở PowerShell trong thư mục đó, chạy:
   ```powershell
   .\ant.exe --version
   ```
   Kỳ vọng: `ant version 1.10.0`
5. Thiết lập credential (chọn một):
   - **API key:** Console → API Keys → tạo key → trong PowerShell:
     ```powershell
     $env:ANTHROPIC_API_KEY = "sk-ant-..."
     ```
   - **OAuth:** `.\ant.exe auth login` (mở browser, lưu credential tại `%APPDATA%\Anthropic\`)
6. Kiểm tra:
   ```powershell
   .\ant.exe auth status
   .\ant.exe models list --transform "data.#.id"
   ```

## File demo kèm theo

| File | Mục đích |
|------|----------|
| `01-install-windows.ps1` | Script tải + giải nén binary Windows |
| `02-first-message.ps1` | Gọi Messages API (cần API key) |
| `03-managed-agent-sample.yaml` | Mẫu YAML agent cho GitOps/CI |
| `04-gemini-blog-prompt.txt` | Prompt mẫu tóm tắt blog bằng ant |

## Lưu ý PowerShell

Khi truyền `--message` dạng YAML inline, dùng dấu nháy đơn bên trong object:

```powershell
.\ant.exe messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 128 `
  --message "{role: user, content: 'Hello from ant'}"
```

Tránh `content: Hello` không có quote — CLI sẽ báo lỗi parse YAML.
