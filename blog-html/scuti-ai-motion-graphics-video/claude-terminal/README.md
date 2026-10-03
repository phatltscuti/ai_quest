# Claude Code trong terminal: critic vòng 3 (đã xong 03/10/2026)

Phiên Claude Code thật, chạy trong Windows Terminal: critic vòng 3, sửa lỗi major, render v4, kiểm tra bằng ffmpeg. Phiên này là mục 6 của blog.

## Kết quả
- Critic vòng 3 tìm ra **2 lỗi major và 6 lỗi minor** (`animation/critic-notes-v3.md`). Lỗi major: ở 6.5s các thẻ hiện ra dưới dạng khung rỗng, và ở 12.5–14s có khoảng 2 giây không có chữ.
- Đã sửa 2 lỗi major. `video/scuti-ai-motion-graphics.mp4` giờ là **v4** (18.00s, 1920×1080, 30 fps, có AAC). Bản v3 được lưu ở `video/scuti-ai-motion-graphics-v3.mp4` và `backup-v3/`.
- Còn lại: khoảng 0.5s chuyển cảnh không có chữ (12.35–12.85s) và 6 lỗi minor chưa sửa.
- Thời gian chạy: prompt A khoảng 2 phút, prompt B khoảng 3 phút, cả bản quay khoảng 10 phút (gồm đoạn chờ).

## Files
| File | Mô tả |
|---|---|
| `prompts-round3.txt` | Prompt A (critic) và prompt B (sửa + render) |
| `drive_session.py`, `termcap.py` | Mở Windows Terminal, chạy `claude --permission-mode auto`, gửi prompt, chụp 3 giây/lần vào `shots/`, quay màn hình |
| `record_terminal.py` | Cách thủ công: tự gõ prompt, script chỉ chụp ảnh và quay |
| `shots/` | 182 ảnh gốc. 2 ảnh đã chọn được chép sang `../images/terminal-03`, `-06` |
| `terminal-session-raw.mkv` | Bản quay thô 10 phút (desktop 1920×1080, 10 fps) |
| `backup-v3/` | Bản v3 trước khi sửa |

## Video quá trình
`../video/scuti-ai-motion-graphics-video-demo1.mp4` (4:03) gồm 2 phần ghép từ bản quay thô và video demo Studio:

| Đoạn trong bản quay thô | Tốc độ | Nội dung |
|---|---|---|
| 5–20s | 1× | Gõ prompt A (bỏ 5s đầu) |
| 20–111s | 4× | Tạo stills, contact sheet, critic chạy nền |
| 111–126s | 1× | Danh sách lỗi |
| 126–416s | bỏ | Chờ và gửi lại prompt B |
| 416–574s | 5× | Sửa code, kiểm tra stills, render, chạy ffmpeg |
| 574–600s | 1× | Tóm tắt kết quả |

Sau đó là toàn bộ demo Studio (đã chạy lại `run_demo.py` với v4).

## Lưu ý khi chạy lại
- `turn_done()` báo xong quá sớm: nó dựa vào `end_turn`, mà Claude kết thúc lượt ngay khi gửi critic chạy nền. Lần này prompt B bị gửi khi critic chưa xong, nên bị mất và phải gửi lại bằng `type_prompt`. Nếu chạy lại, nên chờ thêm đến khi có file `critic-notes-v3.md`.
- Gõ prompt bằng SendKeys khi bộ gõ tiếng Việt (Telex) đang bật sẽ làm sai chữ, ví dụ "Here" thành "Hể". Phải tắt bộ gõ trước khi chạy. Lỗi này không ảnh hưởng tới kết quả, nhưng chữ sai vẫn hiện trong terminal. Blog không dùng ảnh có đoạn chữ sai này.
