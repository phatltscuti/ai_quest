# NREER Auto Click Extension

Extension tự động click cho trang nreer.com

## Cài đặt

1. Mở Chrome và vào `chrome://extensions/`
2. Bật "Developer mode" (góc trên bên phải)
3. Click "Load unpacked"
4. Chọn thư mục `nreer-extension`

## Cách sử dụng

1. Mở trang https://nreer.com
2. Click vào icon extension trên thanh công cụ
3. Bật "Enable Extension"
4. Chọn loại button muốn auto-click:
   - ❤️ Auto Hearts
   - ▶️ Auto Views
5. Extension sẽ tự động:
   - Click button "Use" trên trang chủ
   - Điền URL và click Search (nếu cần)
   - Click button "Send Auto hearts" hoặc "Auto Views" khi xuất hiện

## Lưu ý

- Extension cần bạn nhập URL vào form trước khi nó có thể click Search
- Extension sẽ tự động click button hearts/views khi chúng xuất hiện sau khi search
- Bạn có thể bật/tắt từng loại button riêng biệt

## Lưu ý về Icon

Extension hiện tại không yêu cầu icon để hoạt động. Nếu muốn thêm icon, bạn có thể:
1. Tạo 3 file icon (16x16, 48x48, 128x128 pixels)
2. Thêm lại phần `icons` và `default_icon` vào `manifest.json`

## Cấu trúc file

```
nreer-extension/
├── manifest.json      # Cấu hình extension
├── popup.html         # Giao diện popup
├── popup.js           # Logic popup
├── content.js         # Logic auto-click chính
└── README.md          # Hướng dẫn này
```

