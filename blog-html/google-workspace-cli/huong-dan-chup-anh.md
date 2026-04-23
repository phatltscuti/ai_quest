# 📸 Hướng dẫn Chụp ảnh Demo – Google Workspace CLI Blog

Bạn cần chụp **9 ảnh** tương ứng với 9 vùng placeholder trong blog `index.html`.  
Sau khi chụp, lưu vào thư mục `assets/` với **đúng tên file** ghi phía dưới.  
Khi có file ảnh đúng tên, blog sẽ hiển thị ảnh thay cho ô "Chụp màn hình tại đây".

---

## ⚙️ Chuẩn bị chung (làm 1 lần trước khi bắt đầu)

**1. Mở Windows Terminal** (không dùng cmd thông thường, dùng Windows Terminal vì đẹp hơn).

**2. Phím tắt chụp ảnh:** `Windows + Shift + S`
- Chọn "Rectangular Snip" (hình chữ nhật)
- Kéo chuột bao quanh vùng muốn chụp
- Ảnh tự copy vào clipboard
- Mở **Paint** → `Ctrl + V` → `Ctrl + S` → chọn định dạng PNG → lưu vào thư mục `assets/`

**3. Kích thước cửa sổ terminal:**  
Thu nhỏ terminal sao cho ngang khoảng **900–1100px**, đừng để toàn màn hình. Ảnh sẽ tập trung hơn.

---

## 📋 Danh sách 9 ảnh cần chụp

---

### 📸 Ảnh 1 — Cài đặt gws thành công
**Tên file:** `assets/step1-install.png`

**Lệnh chạy:**
```
npm install -g @googleworkspace/cli
gws --version
```

**Chụp khi:** Terminal in ra dòng `gws 0.18.1` (hoặc version cao hơn).  
**Vùng chụp:** Bao gồm cả dòng lệnh `gws --version` và kết quả `gws 0.18.1` phía dưới.

---

### 📸 Ảnh 2A — Google Cloud Console trang Credentials
**Tên file:** `assets/step2a-gcloud-credentials.png`

**Thao tác:**
1. Mở trình duyệt
2. Vào: https://console.cloud.google.com/
3. Vào mục **APIs & Services → Credentials**

**Chụp khi:** Trang Credentials đang hiển thị list OAuth 2.0 Client IDs.  
**Vùng chụp:** Toàn bộ trang trình duyệt, thấy rõ tiêu đề "Credentials".

---

### 📸 Ảnh 2B — Client ID và Client Secret sau khi tạo
**Tên file:** `assets/step2b-client-id.png`

**Thao tác:** Sau khi tạo OAuth 2.0 Client ID, Google sẽ hiện popup hoặc trang với Client ID và Secret.

**Chụp khi:** Màn hình hiển thị "Your client ID" và "Your client secret".  
⚠️ **Quan trọng: Blur (làm mờ) phần giá trị thật** của Client ID và Client Secret trước khi lưu ảnh vào blog.  
Dùng Paint hoặc Snagit để vẽ hình chữ nhật màu đen che phủ phần đó.

---

### 📸 Ảnh 3 — gws auth setup
**Tên file:** `assets/step3-auth-setup.png`

**Lệnh chạy:**
```
gws auth setup
```

**Chụp khi:** Terminal đang hiển thị dấu nhắc `? Enter your OAuth2 Client ID:` chờ bạn nhập.  
⚠️ Nếu bạn đã nhập và thấy dấu `*` che khuất thì càng tốt, chụp luôn.

---

### 📸 Ảnh 4A — Terminal in URL xác thực
**Tên file:** `assets/step4a-login-url.png`

**Lệnh chạy:**
```
gws auth login
```

**Chụp khi:** Terminal in ra dòng chữ "Please open the following URL in your browser:" kèm đường link dài.  
**Mẹo:** Chụp phần đầu của URL (thấy `https://accounts.google.com/o/oauth2/auth?`) là đủ, không cần thấy hết URL.  
⚠️ Nếu URL chứa `client_id=`, hãy blur phần giá trị đó.

---

### 📸 Ảnh 4B — Màn hình OAuth Consent trên trình duyệt
**Tên file:** `assets/step4b-oauth-browser.png`

**Thao tác:** Copy URL từ terminal, dán vào thanh địa chỉ Chrome/Edge, nhấn Enter.

**Chụp khi:** Trình duyệt hiển thị trang Google yêu cầu quyền truy cập: "Google Workspace CLI wants to access your Google Account".  
**Vùng chụp:** Toàn bộ màn hình trình duyệt (Alt + PrintScreen hoặc dùng Windows + Shift + S).

---

### 📸 Ảnh 4C — Xác thực thành công trong terminal
**Tên file:** `assets/step4c-login-success.png`

**Chụp khi:** Sau khi nhấn "Allow" trên trình duyệt, quay lại terminal và thấy thông báo `Authentication successful`.  
**Vùng chụp:** Phần terminal hiển thị thông báo thành công.

---

### 📸 Ảnh 5A — Lệnh tìm kiếm Drive đang chạy
**Tên file:** `assets/lab1a-drive-command.png`

**Lệnh chạy (copy nguyên văn vào PowerShell):**
```
gws drive files list --params '{\"q\": \"mimeType = \\\"application/vnd.google-apps.folder\\\"\", \"pageSize\": 5}' --format table
```

> Lệnh này tìm tất cả thư mục trên Drive của bạn, không cần từ khóa cụ thể.

**Chụp khi:** Lúc bạn vừa gõ xong lệnh và chuẩn bị nhấn Enter, hoặc khi lệnh đang chạy.

---

### 📸 Ảnh 5B — Kết quả tìm kiếm Drive trả về
**Tên file:** `assets/lab1b-drive-result.png`

**Chụp khi:** Terminal hiển thị bảng kết quả với cột ID và NAME của các thư mục.  
⚠️ Nếu không muốn lộ tên thư mục riêng tư, hãy blur những dòng đó trong Paint trước khi lưu.  
**Mẹo:** Chụp cả phần header bảng để ảnh dễ hiểu hơn.

---

### 📸 Ảnh 6A — Lệnh gmail +triage đang chạy
**Tên file:** `assets/lab2a-gmail-command.png`

**Lệnh chạy:**
```
gws gmail +triage --format table --max 5
```

**Chụp khi:** Lúc vừa gõ xong lệnh (trước khi nhấn Enter), hoặc khi thấy spinner đang xử lý (`⠙ Fetching...`).

---

### 📸 Ảnh 6B — Kết quả bảng email chưa đọc
**Tên file:** `assets/lab2b-gmail-triage-result.png`

**Chụp khi:** Terminal hiển thị bảng email với cột FROM, SUBJECT, DATE.  
⚠️ **Bắt buộc blur:** Địa chỉ email người gửi và tiêu đề email nếu chứa thông tin công việc nhạy cảm.

---

## ✅ Checklist sau khi chụp xong

Đánh dấu vào danh sách sau:

- [ ] `assets/step1-install.png` — Cài đặt thành công
- [ ] `assets/step2a-gcloud-credentials.png` — Google Cloud Credentials
- [ ] `assets/step2b-client-id.png` — Client ID (đã blur giá trị)
- [ ] `assets/step3-auth-setup.png` — gws auth setup
- [ ] `assets/step4a-login-url.png` — URL xác thực
- [ ] `assets/step4b-oauth-browser.png` — Màn hình OAuth trình duyệt
- [ ] `assets/step4c-login-success.png` — Thành công
- [ ] `assets/lab1a-drive-command.png` — Lệnh Drive
- [ ] `assets/lab1b-drive-result.png` — Kết quả Drive
- [ ] `assets/lab2a-gmail-command.png` — Lệnh Gmail
- [ ] `assets/lab2b-gmail-triage-result.png` — Kết quả Gmail

---

## 🖼️ Cách thêm ảnh vào blog

Sau khi lưu ảnh vào thư mục `assets/`, mở file `index.html` bằng:
1. Double-click để mở bằng trình duyệt → Ảnh sẽ tự hiển thị thay placeholder.
2. Kiểm tra xem ảnh xuất hiện đúng chỗ chưa.
3. Nếu ảnh không hiển thị → Kiểm tra tên file (phân biệt hoa/thường).

---

*Hướng dẫn tạo bởi Antigravity AI Agent · Scuti Tech Lab*
