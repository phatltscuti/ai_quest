# 🎯 Auto Click Search Button Extension

Chrome Extension tự động click button "Search" khi countdown timer hết thời gian.

## 📋 Tính năng

- ✅ Tự động theo dõi countdown timer trên trang web
- ✅ Tự động click button "Search" khi timer đếm về 0:00
- ✅ **TỰ ĐỘNG CLICK BUTTON VIDEO** sau 3-4 giây
- ✅ Hiển thị thông báo khi auto-click thành công
- ✅ Bật/tắt extension dễ dàng từ popup
- ✅ Hoạt động trên mọi trang web có countdown timer tương tự
- ✅ **Tự động lặp lại** toàn bộ quy trình

## 🚀 Cách cài đặt

### Bước 1: Tải Extension

Tải thư mục `auto-click-extension` về máy hoặc clone repository này.

### Bước 2: Bật Developer Mode trong Chrome

1. Mở Chrome browser
2. Vào `chrome://extensions/` (hoặc Menu > Extensions > Manage Extensions)
3. Bật **Developer mode** ở góc trên bên phải

### Bước 3: Load Extension

1. Click nút **"Load unpacked"**
2. Chọn thư mục `auto-click-extension`
3. Extension sẽ xuất hiện trong danh sách

### Bước 4: Sử dụng

1. Truy cập trang web có countdown timer và button search
2. Extension sẽ tự động hoạt động
3. Click vào icon extension để bật/tắt tính năng

## 💡 Cách hoạt động

Extension hoạt động theo **2-step workflow**:

### 🔄 Full Workflow:

1. **Monitor Countdown**: Kiểm tra countdown timer mỗi giây
2. **Detect Ready**: Phát hiện khi countdown = 0:00 hoặc "READY"
3. **Auto Click Search**: Tự động click vào button "Search"
4. **Wait for Video Button**: Đợi 3-4 giây button video xuất hiện
5. **Auto Click Video**: Tự động click button Video (icon 🎥)
6. **Notification**: Hiển thị thông báo thành công
7. **Resume**: Tiếp tục theo dõi countdown mới → Lặp lại từ bước 1

### 📊 Timeline:

```
Countdown = 0:00
    ↓
Click "Search" button
    ↓
Wait 3.5 seconds
    ↓
Look for Video button (check every 0.5s, max 10 attempts)
    ↓
Click "Video" button
    ↓
Wait 5 seconds
    ↓
Resume countdown monitoring
    ↓
Loop back to start ↻
```

## 🎨 Giao diện Popup

- **Toggle Switch**: Bật/tắt tính năng auto-click
- **Status Display**: Hiển thị trạng thái hiện tại
- **Info Section**: Hướng dẫn sử dụng

## 🛠️ Cấu trúc File

```
auto-click-extension/
├── manifest.json       # Cấu hình extension
├── content.js          # Script chính (monitor & auto-click)
├── popup.html          # Giao diện popup
├── popup.js            # Logic popup
├── icon16.png          # Icon 16x16
├── icon48.png          # Icon 48x48
├── icon128.png         # Icon 128x128
└── README.md           # Tài liệu
```

## 🔧 Tùy chỉnh

### Thay đổi thời gian kiểm tra

Mở `content.js` và sửa dòng:

```javascript
checkInterval = setInterval(() => {
  checkCountdownAndClick();
}, 1000); // Thay đổi 1000 (1 giây) thành giá trị khác
```

### Thay đổi selector của button

Mở `content.js` và sửa hàm `clickSearchButton()`:

```javascript
// Thêm selector mới
searchButton = document.querySelector('YOUR_CUSTOM_SELECTOR');
```

## ⚠️ Lưu ý

- Extension cần quyền truy cập trang web để hoạt động
- Nếu button bị disable, extension sẽ chờ đến khi nó được enable
- Extension sẽ tự động dừng sau khi click và khởi động lại sau 5 giây

## 🐛 Troubleshooting

### Extension không hoạt động?

1. **Kiểm tra Console**:
   - Nhấn F12 để mở DevTools
   - Vào tab Console
   - Tìm log `[Auto Click]`

2. **Kiểm tra Extension đã BẬT?**:
   - Click icon extension
   - Đảm bảo toggle switch đang ON

3. **Kiểm tra Countdown Element**:
   - Đảm bảo trang có element với class `.views-countdown`
   - Kiểm tra HTML structure có đúng không

4. **Reload Extension**:
   - Vào `chrome://extensions/`
   - Click nút "Reload" trên extension

### Console không có log?

Extension có thể chưa được load. Thử:
- Reload trang web (F5)
- Reload extension trong `chrome://extensions/`
- Kiểm tra lại host_permissions trong manifest.json

## 📝 Changelog

### Version 1.0.0 (2025-11-11)
- ✨ Release đầu tiên
- ✅ Tính năng monitor countdown
- ✅ Tính năng auto-click
- ✅ Popup UI bật/tắt
- ✅ Notification system

## 📄 License

MIT License - Free to use and modify

## 👨‍💻 Developer

Made with ❤️ for AI Quest Learning Path

---

**🎉 Chúc bạn sử dụng extension hiệu quả!**

