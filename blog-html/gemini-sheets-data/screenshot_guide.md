# Hướng Dẫn Chụp Ảnh Demo (Screenshot Guide) - Gemini Sheets Data

Tài liệu này hướng dẫn bạn chụp chính xác 7 bức ảnh để khớp với các vị trí `[Chèn Ảnh X]` trong bài Blog.

---

## Ảnh 1: Bước Nhập Dữ Liệu Thô (Mục 2. Kịch Bản)
- **Prompt:** Không có (Bấm File > Import).
- **Thao tác:** Tải file `raw_ticket_data.csv` lên Google Sheets.
- **Góc chụp:** Ảnh màn hình thao tác Import thành công file raw_ticket_data.csv lên Google Sheets. Dữ liệu thô lộn xộn đổ ra bảng tính, hiển nhiên bộc lộ sự thiếu sót của các trường phân loại chuẩn.

---

## Ảnh 2: Prompt 1 - Phân Loại Bằng Ngữ Nghĩa (Phase 1)
- **Prompt:** `Analyze the "Issue Description" column. Identify the context and create a new column categorizing each issue into exactly one label: Hardware, Software, Network, or Access.`
- **Thao tác:** Bôi đen dữ liệu, nhập Prompt 1 vào Side Panel.
- **Góc chụp:** Gemini phân tích xong và hiển thị cột Category mới ở Side Panel chuẩn bị Insert vào Sheet.

## Ảnh 3: Prompt 2 - Đồng Nhất Danh Xưng (Phase 1)
- **Prompt:** `Normalize the "Customer" column. Identify all sloppy variations like 'ggl', 'Google Inc', or 'GGL LLC' and standardize them to 'Google'. Apply the same logic for Amazon, Microsoft, Apple, and Salesforce.`
- **Thao tác:** Nhập Prompt 2 vào Side Panel.
- **Góc chụp:** Thao tác Gemini đang quét lại Cột Customer và trả về các tên hãng công nghệ đã được viết hoa chuẩn chỉ.

## Ảnh 4: Prompt 3 - Rút Trích Dữ Liệu Ẩn (Phase 1)
- **Prompt:** `Read the "Issue Description" column again. Extract any physical location or floor number mentioned into a new column called 'Location'. If not mentioned, write 'N/A'.`
- **Thao tác:** Nhập Prompt 3 vào Side Panel.
- **Góc chụp:** Cột Location mới xuất hiện trên Sheet, nhặt trúng phóc các chữ "3rd floor", "5th floor" từ đoạn văn mô tả.

---

## Ảnh 5: Prompt 4 - Hành Văn Tóm Tắt (Phase 2)
- **Prompt:** `Analyze the relationship between the clean "Category" column and "Resolution Time". Write a short 3-line executive summary identifying the primary driver of resolution delays.`
- **Thao tác:** Nhập Prompt 4 vào Side Panel.
- **Góc chụp:** Bảng tóm tắt chữ cực gọn của AI ở thanh Panel bên phải, chỉ rõ Hardware tốn kém 60% thời gian xử lý.

## Ảnh 6: Prompt 5 - Lập Bảng Thống Kê (Phase 2)
- **Prompt:** `Create a Pivot Table on a new sheet showing the Average Resolution Time grouped by Category. Sort them from highest to lowest time.`
- **Thao tác:** Nhập Prompt 5 vào Side Panel.
- **Góc chụp:** Một trang Sheet mới tinh vừa đẻ ra chứa chiếc Pivot Table do AI tự setup lệnh tính Average.

## Ảnh 7: Prompt 6 - Điều Khiển Giao Diện Báo Cáo Lỗi (Phase 2)
- **Prompt:** `Apply conditional formatting to the Resolution Time column: highlight cells containing values greater than 48 hours in light red.`
- **Thao tác:** Nhập Prompt 6 vào Side Panel.
- **Góc chụp:** Giao diện Sheet nơi các con số thời gian xử lý chậm (>48h) tức lự chuyển sang màu đỏ rực cảnh báo.
