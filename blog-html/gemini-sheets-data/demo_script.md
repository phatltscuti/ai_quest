# Kịch Bản Demo Live: "Vũ Điệu 6 Mã Lệnh"

Kịch bản này là show diễn sức mạnh tuyệt đối của Gemini 1.5 Pro trong Google Sheets. Bạn sẽ nã liên tục 6 viên đạn Prompt mà không cần đụng đến bàn phím thao tác 1 hàm Excel nào.

---

## 🎬 Khoảnh Khắc 0: Sự Lộn Xộn Của Data Thực Tế
- **Action:** Mở Google Sheets trống. Bấm `File > Import` và tải lên `raw_ticket_data.csv`. Phóng to màn hình để lộ ra khoảng 30 dòng dữ liệu ngổn ngang.
- **Voiceover:** "Tưởng tượng anh chị đang làm PM, nhận file Helpdesk này đi báo cáo sếp. Tên khách hàng (Customer) thì sai chính tả tè le. Lỗi hỏng hóc (Description) thì viết văn xuôi lê thê. Để dọn bãi rác này, ngày xưa em tốn nửa buổi gắn hàm VLOOKUP, INDEX MATCH... Nhưng hôm nay, em chỉ mất đúng 3 phút."

## 🎬 Phase 1: Dọn Rác Thần Tốc (3 Prompts dọn dẹp)
- **Voiceover:** "Em sẽ biến Gemini thành Data Analyst Junior. Chuyển tiền, lộn, chuyển mã lệnh thứ nhất!"
- **Action (Prompt 1 - Category):** 
  - Paste Prompt: `Analyze the "Issue Description" column. Identify the context and create a new column categorizing each issue into exactly one label: Hardware, Software, Network, or Access.`
  - Bấm Insert.
- **Voiceover:** "Giây thứ 10, Cột Category tự sinh ra, bóc tách chính xác 'monitor' vào Hardware. Rất kinh dị!"
- **Action (Prompt 2 - Normalize):** 
  - Paste Prompt: `Normalize the "Customer" column. Identify all sloppy variations like 'ggl', 'Google Inc', or 'GGL LLC' and standardize them to 'Google'. Apply the same logic for Amazon, Microsoft, Apple, and Salesforce.`
- **Voiceover:** "Nhìn cột Customer nhé. Cái đống 'ggl', Google LLC ngay lập tức bị quy chuẩn hết lại thành Google chống lỗi cho hàm đếm. Giây thứ 30!"
- **Action (Prompt 3 - Extract):** 
  - Paste Prompt: `Read the "Issue Description" column again. Extract any physical location or floor number mentioned into a new column called 'Location'. If not mentioned, write 'N/A'.`
- **Voiceover:** "Lấy số tầng ẩn giấu nốt để team kỹ thuật dễ đi sửa nào. Xong Phase 1 dọn rác." *(Màn hình hiện ra cột Location rất ảo)*.

## 🎬 Phase 2: Giải Bài Toán Quản Trị (3 Prompts báo cáo)
- **Voiceover:** "Data rác đã hoá vàng. Giờ sếp bắt họp. Ối giời ơi lỗi do đâu lâu vậy?"
- **Action (Prompt 4 - Insight):** 
  - Paste Prompt: `Analyze the relationship between the clean "Category" column and "Resolution Time". Write a short 3-line executive summary identifying the primary driver of resolution delays.`
- **Voiceover:** "Thay vì đọc số mờ mắt, Gemini đang gõ thẳng hộ em đoạn văn báo cáo dài 3 câu. Thưa sếp, lỗi thiết bị (Hardware) ăn mòn 60% leadtime. Xong việc 1!"
- **Action (Prompt 5 - Pivot Dash):** 
  - Paste Prompt: `Create a Pivot Table on a new sheet showing the Average Resolution Time grouped by Category. Sort them from highest to lowest time.`
- **Voiceover:** "Không tin à sếp? Em bung cho sếp cái Pivot Table trong nửa giây." (Màn hình bật nhảy sang tab lập Pivot tự động).
- **Action (Prompt 6 - Đổi màu UI):** 
  - Paste Prompt: `Apply conditional formatting to the Resolution Time column: highlight cells containing values greater than 48 hours in light red.`
- **Voiceover:** "Để cảnh báo cho team IT, em nhuộm đỏ toàn bộ những ông nào ngâm lỗi > 48 tiếng đập thẳng vào mặt luôn bằng quy tắc đổ màu có điều kiện. Tạch! Xong việc."

## 🎬 Kết thúc: Áp Đảo
- **Voiceover:** "Bộ 6 Prompt vừa rồi lướt trên hàng vạn ký tự thô. Nó không phải là tương lai, nó đang nằm ở bên mép phải màn hình của các anh chị ngay lúc này. Xin cảm ơn!"
