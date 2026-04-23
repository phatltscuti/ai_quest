# Hướng dẫn demo & chụp ảnh — Drive Projects + Ask Gemini (client pitch)

Đồng bộ với `drive-projects-client-pitch-blog.html`. Mỗi bước: thao tác trên Drive/Gemini + tên file ảnh trong `images/`.

**Chuẩn bị:** đọc `demo-assets/CHUAN-BI-TRUOC-DEMO.md`, tạo 3 Doc nguồn từ file `.txt`, tạo Project và gắn sources trước khi chụp Step 9 trở đi.

**Cắt màn hình:** `Windows + Shift + S` (Windows) / `Cmd + Shift + 4` (macOS).  
**Thư mục ảnh:** `blog-html/drive-projects-client-pitch/images/`

---

## Danh sách 16 bước

### 1. `step-01-drive-sources-folder.png`
1. Mở [drive.google.com](https://drive.google.com), vào `WS_Sales_Pitch_Sources`.
2. Hiển thị `00_Internal_Sources` và `10_Client_Outputs`.
3. Chụp cửa sổ Drive (có breadcrumb/thanh địa chỉ).

### 2. `step-02-product-spec-open.png`
1. Mở Doc `SPEC_Warehouse_Visibility_MVP_v1.2`.
2. Cuộn để thấy mục MVP scope, NFR, bảng estimate nội bộ.
3. Chụp phần nội dung chính.

### 3. `step-03-proposal-template-open.png`
1. Mở Doc `TEMPLATE_Proposal_IT_Intake`.
2. Hiển thị các section header (Executive summary, Proposed scope, Timeline…).
3. Chụp.

### 4. `step-04-past-meeting-notes-open.png`
1. Mở Doc `NOTES_Acme_Retail_2026-03-18_REQ_interview`.
2. Hiển thị mục Lessons learned và Open questions.
3. Chụp.

### 5. `step-05-drive-new-project-menu.png`
1. Trên Drive, bấm **New** (góc trái trên).
2. Mở menu và làm nổi bật mục **Project** (chưa cần bấm Create).
3. Chụp menu New (hoặc dùng `https://project.new` và chụp trang tạo project tương đương).

### 6. `step-06-project-name-and-create.png`
1. Nhập tên Project: `Pitch — Nexa Logistics — Warehouse MVP`.
2. Chụp màn hình trước khi bấm **Create Project** (hoặc ngay sau khi vừa tạo, thấy tên project).

### 7. `step-07-add-sources-picker.png`
1. Trong Project, bấm **Add sources** (hoặc biểu tượng + Sources).
2. Mở picker Drive và chọn/bắt đầu chọn 3 file nguồn.
3. Chụp dialog chọn file (thấy tên 3 file spec/template/notes).

### 8. `step-08-project-sources-panel.png`
1. Sau khi add xong, panel trái hiển thị danh sách sources đã ghim (3 file, checkbox bật).
2. Chụp toàn panel Project + danh sách sources.

### 9. `step-09-ask-gemini-fullscreen.png`
1. Trong Project, mở **Ask Gemini** (full-screen hoặc panel Gemini).
2. Xác nhận sources đang active (checked).
3. Chụp giao diện prompt trống, thấy vùng Sources.

### 10. `step-10-gemini-prompt-entered.png`
1. Dán prompt tổng hợp (nội dung trong blog HTML, mục Prompt chính).
2. Chụp ô prompt đã điền đầy đủ, chưa gửi hoặc vừa gửi.

### 11. `step-11-gemini-synthesis-response.png`
1. Gửi prompt, đợi Gemini trả lời.
2. Chụp câu trả lời có **citations** (số [1], [2]…) và các section proposal.

### 12. `step-12-citation-source-preview.png`
1. Nhìn cột phải **Sources used** (3 file đang dùng).
2. **Click tên một file** (ví dụ `SPEC_Warehouse_Visibility_MVP_v1.2`) → Drive/Docs mở file nguồn để đối chiếu.
3. (Tuỳ phiên bản) Nếu trong câu trả lời có số **[1], [2]** ở cuối câu, click số đó cũng mở nguồn tương ứng.
4. Chụp: hoặc tab Doc nguồn đang mở, hoặc màn Project với panel Sources used + một file được highlight.

**Không click ở Step 12:** nút **Export to Docs** / **Export to Sheets** dưới câu trả lời → đó là **Step 13**.

### 13. `step-13-insert-to-google-doc.png`
1. Cuộn xuống **cuối câu trả lời** Gemini (dưới bảng Risk / Next steps).
2. Bấm **Export to Docs** (icon Doc + mũi tên) — **không** bấm Export to Sheets (Sheets chỉ xuất riêng bảng, không phải cả proposal).
3. Chọn tạo Doc mới hoặc chọn Doc đích → nếu được chọn folder, trỏ vào `10_Client_Outputs`.
4. Đổi tên file thành `PITCH_Nexa_Logistics_Warehouse_MVP_draft` (trong Drive sau khi tạo).
5. Chụp: lúc menu/dialog Export to Docs đang mở, hoặc Doc vừa tạo đang mở lần đầu.

**Export to Sheets:** chỉ dùng nếu bạn muốn lưu riêng bảng Risk; **không bắt buộc** cho demo pitch. Bài blog yêu cầu đầu ra chính là **Google Doc proposal**.

### 14. `step-14-client-pitch-doc-result.png`
1. Mở Doc đầu ra `PITCH_Nexa_Logistics_Warehouse_MVP_draft`.
2. Cuộn để thấy Executive summary + Proposed scope đã điền theo khách Nexa.
3. Chụp.

### 15. `step-15-manage-sources-toggle.png`
1. Trong Project, **bỏ tick** tạm một source (ví dụ meeting notes).
2. Hỏi lại Gemini một câu ngắn và chụp panel sources (1 source off) — minh họa kiểm soát phạm vi.

### 16. `step-16-projects-history-resume.png`
1. Drive → **Projects** (sidebar) → chọn project vừa tạo.
2. Mở **History** / conversation list, thấy phiên chat vừa chạy.
3. Chụp (chứng minh resume research).

---

## Lỗi thường gặp khi chụp demo

| Triệu chứng | Cách xử lý |
|-------------|------------|
| Không thấy **New → Project** | Dùng web Drive; kiểm tra gói Gemini in Drive. |
| Collaborator không đọc được source | Cấp quyền View file gốc trên Drive trước khi share Project. |
| Citation không mở file | User cần quyền mở đúng Doc nguồn. |
| Output lệch khách hàng | Thêm client brief vào prompt; giữ đủ 3 sources bật. |
