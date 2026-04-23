# Chuẩn bị trước demo — Drive Projects + Ask Gemini (client pitch)

## Quyền & gói dịch vụ

- Tài khoản **Google Workspace** có **Gemini in Drive** (Business/Enterprise hoặc gói AI tương đương).
- Tạo Project **chỉ trên web**: [drive.google.com](https://drive.google.com) hoặc [project.new](https://project.new).
- Người dùng cần quyền **xem** tất cả file nguồn bạn gắn vào Project (collaborator không thấy nội dung nếu thiếu quyền Drive).

---

## Thứ tự làm (quan trọng)

**Có — phải tạo thư mục Drive trước, sau đó mới tạo Docs và đặt đúng folder.**

| Bước | Việc cần làm | Ghi chú |
|------|----------------|--------|
| **1** | Tạo folder gốc + 2 folder con | Làm trước hết trên Drive |
| **2** | Tạo 3 Google Doc **bên trong** `00_Internal_Sources` | Dán nội dung từ file `.txt` trong `demo-assets/` |
| **3** | (Sau khi chạy Gemini) Lưu pitch draft vào `10_Client_Outputs` | Không cần tạo sẵn nội dung, chỉ cần folder trống |
| **4** | Tạo Drive **Project** + Add sources | Chọn 3 Doc ở bước 2 |
| **5** | Ask Gemini + chụp ảnh demo | Theo `HUONG-DAN-DEMO-CHUP-ANH.md` |

---

## Bước 1 — Tạo thư mục trên Drive (trước)

1. Mở [drive.google.com](https://drive.google.com).
2. **New** → **Folder** → đặt tên `WS_Sales_Pitch_Sources`.
3. Mở folder vừa tạo → **New** → **Folder** → `00_Internal_Sources`.
4. Quay lại `WS_Sales_Pitch_Sources` → **New** → **Folder** → `10_Client_Outputs`.

Kết quả:

```
WS_Sales_Pitch_Sources/
  00_Internal_Sources/     ← đặt 3 Doc nguồn ở bước 2
  10_Client_Outputs/       ← để trống; pitch draft lưu sau khi Gemini xong
```

Ảnh demo Step 1 chụp sau khi xong bước này.

---

## Bước 2 — Tạo 3 Google Doc (sau khi có folder)

**Luôn tạo Doc khi đang mở (hoặc chọn đích) folder `00_Internal_Sources`:**

1. Vào `00_Internal_Sources` → **New** → **Google Docs**.
2. Dán `01-product-spec-body.txt` → đổi tên file thành `SPEC_Warehouse_Visibility_MVP_v1.2`.
3. Lặp lại: Doc mới → dán `02-proposal-template-body.txt` → `TEMPLATE_Proposal_IT_Intake`.
4. Lặp lại: Doc mới → dán `03-past-meeting-notes.txt` → `NOTES_Acme_Retail_2026-03-18_REQ_interview`.

Ghi link/ID vào bản sao `ids-template.txt` (xem mục **Lấy ID ở đâu?** bên dưới).

Ảnh demo Step 2–4: mở từng Doc và chụp nội dung.

### Lấy ID ở đâu?

| Loại | Cách lấy |
|------|----------|
| **Folder** | Mở folder trên Drive → copy URL → ID là đoạn sau `.../folders/` |
| **Google Doc** | Mở Doc → URL dạng `docs.google.com/document/d/{DOC_ID}/edit` → lấy `{DOC_ID}` |
| **Drive Project** | Đang mở Project trên web → copy nguyên URL thanh địa chỉ |

Ví dụ Folder: `https://drive.google.com/drive/folders/1AbCdEf...` → ID = `1AbCdEf...`  
Ví dụ Doc: `https://docs.google.com/document/d/1tZ4f_9F.../edit` → ID = `1tZ4f_9F...`

Chi tiết từng bước có trong file `ids-template.txt` (phần hướng dẫn ở đầu file).

---

## Bước 3 — Tạo Drive Project (sau khi có 3 Doc)

1. Drive → **New** → **Project** (hoặc [project.new](https://project.new)).
2. Đặt tên: `Pitch — Nexa Logistics — Warehouse MVP` → **Create Project**.
3. **Add sources** → chọn **3 Doc trong** `00_Internal_Sources` (không chọn folder, chọn từng file).

---

## Thư mục ảnh

Lưu screenshot vào: `blog-html/drive-projects-client-pitch/images/`  
Đặt đúng tên `step-XX-....png` theo `HUONG-DAN-DEMO-CHUP-ANH.md`.

## Client giả lập cho pitch mới

- **Khách mới:** Nexa Logistics Co., Ltd.
- Dùng `04-client-brief-nexa.txt` / `05-gemini-synthesis-prompt.txt` khi hỏi Gemini (dán vào prompt, không bắt buộc tạo Doc riêng trên Drive).
