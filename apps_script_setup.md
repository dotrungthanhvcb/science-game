# 📝 Hướng Dẫn Cài Đặt Google Apps Script Để Tự Động Lưu Kết Quả Thi

Tài liệu này hướng dẫn cách kết nối game trắc nghiệm Khoa Học trên Web (Vercel) với Google Drive để **tự động lưu kết quả thi của bé vào một file Google Sheets** nằm chính xác bên trong thư mục Google Drive của bạn:
- **Thư mục lưu trữ:** [Google Drive Folder ID: `1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49`](https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49)
- **Tên file Google Sheets:** `Ket_Qua_Thi_Khoa_Hoc` (Script sẽ **tự động tạo mới** nếu chưa có, hoặc tự động tìm và ghi nối tiếp nếu đã có).

---

## BƯỚC 1: Mở Google Apps Script

1. Mở trình duyệt và truy cập: **[script.google.com](https://script.google.com)**
2. Đăng nhập bằng tài khoản Google sở hữu thư mục Drive trên.
3. Bấm vào nút **`+ Dự án mới`** (New project) ở góc trên bên trái.
4. Đổi tên dự án từ *"Dự án không có tiêu đề"* thành: **`Science Quiz Saver`**.

---

## BƯỚC 2: Dán Mã Nguồn Google Apps Script

1. Xóa toàn bộ nội dung mẫu có sẵn trong file `Mã.gs` (Code.gs).
2. Sao chép và dán toàn bộ đoạn code dưới đây vào:

```javascript
/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ THI KHOA HỌC
 * Thư mục Google Drive mục tiêu: ID 1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49
 * Tên file Google Sheets: Ket_Qua_Thi_Khoa_Hoc
 */

const TARGET_FOLDER_ID = "1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49";
const SPREADSHEET_NAME = "Ket_Qua_Thi_Khoa_Hoc";

/**
 * Xử lý yêu cầu POST gửi từ Game web (Vercel / Localhost)
 */
function doPost(e) {
  try {
    let payload = {};
    if (e && e.postData && e.postData.contents) {
      try {
        payload = JSON.parse(e.postData.contents);
      } catch (parseErr) {
        payload = e.parameter || {};
      }
    } else if (e && e.parameter) {
      payload = e.parameter;
    }

    const sheet = getOrCreateSpreadsheet();

    const timestamp = payload.timestamp || new Date().toLocaleString("vi-VN");
    const studentName = payload.studentName || "Học sinh";
    const studentClass = payload.studentClass || "Chưa nhập";
    const sources = payload.sources || "Tất cả nguồn";
    const totalQuestions = payload.totalQuestions !== undefined ? payload.totalQuestions : "";
    const correctCount = payload.correctCount !== undefined ? payload.correctCount : "";
    const wrongCount = payload.wrongCount !== undefined ? payload.wrongCount : "";
    const score = payload.score || "";
    const duration = payload.duration || "";

    // Ghi dòng dữ liệu mới vào Google Sheets
    sheet.appendRow([
      timestamp,
      studentName,
      studentClass,
      sources,
      totalQuestions,
      correctCount,
      wrongCount,
      score,
      duration
    ]);

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Đã lưu kết quả thi thành công!",
      timestamp: timestamp,
      studentName: studentName
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Xử lý kiểm tra GET kiểm tra trạng thái hoạt động của Web App
 */
function doGet(e) {
  return ContentService.createTextOutput(
    "✅ Google Apps Script Web App đang hoạt động bình thường!\n" +
    "Sẵn sàng nhận kết quả thi Khoa Học từ web game."
  );
}

/**
 * Tự động tìm hoặc tạo mới file Google Sheets 'Ket_Qua_Thi_Khoa_Hoc'
 * nằm chính xác bên trong thư mục Google Drive có ID 1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49
 */
function getOrCreateSpreadsheet() {
  const folder = DriveApp.getFolderById(TARGET_FOLDER_ID);
  const files = folder.getFilesByName(SPREADSHEET_NAME);
  let spreadsheet;

  if (files.hasNext()) {
    spreadsheet = SpreadsheetApp.open(files.next());
  } else {
    // Tự động tạo file Sheets mới bên trong thư mục đích
    spreadsheet = SpreadsheetApp.create(SPREADSHEET_NAME);
    const file = DriveApp.getFileById(spreadsheet.getId());
    folder.addFile(file);
    DriveApp.getRootFolder().removeFile(file);
  }

  let sheet = spreadsheet.getActiveSheet();
  
  // Khởi tạo dòng tiêu đề nếu sheet còn trống
  if (sheet.getLastRow() === 0) {
    const headers = [
      "Thời gian nộp bài",
      "Tên học sinh",
      "Lớp",
      "Nguồn đề thi",
      "Tổng số câu",
      "Số câu đúng",
      "Số câu sai",
      "Điểm số",
      "Thời gian làm bài"
    ];

    sheet.appendRow(headers);

    // Định dạng giao diện tiêu đề nổi bật
    const headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#4361EE")
               .setFontColor("#FFFFFF")
               .setFontWeight("bold")
               .setFontSize(11)
               .setHorizontalAlignment("center");
    
    sheet.setFrozenRows(1);
    sheet.setRowHeight(1, 35);
    sheet.getRange(2, 5, 1000, 5).setHorizontalAlignment("center");
  }

  return sheet;
}
```

3. Bấm biểu tượng 💾 **Lưu dự án** (Save project) hoặc nhấn tổ hợp phím `Ctrl + S` (hoặc `Cmd + S` trên Mac).

---

## BƯỚC 3: Triển Khai (Deploy) Dưới Dạng Web App

1. Ở góc trên bên phải, bấm vào nút màu xanh **`Triển khai` (Deploy)** > Chọn **`Tùy chọn triển khai mới...` (New deployment)**.
2. Bấm vào biểu tượng bánh răng ⚙️ bên cạnh dòng *Chọn loại* (Select type) > Chọn **`Ứng dụng web` (Web app)**.
3. Thiết lập các mục quan trọng sau (bắt buộc đúng cấu hình):
   - **Mô tả (Description):** `V1 - Lưu kết quả thi Khoa Học`
   - **Thực thi dưới dạng (Execute as):** Chọn **`Tôi` (Me / email của bạn)**
   - **Người có quyền truy cập (Who has access):** Chọn **`Bất kỳ ai` (Anyone)**
     *(Điều này cho phép trang web game trên Vercel có thể gửi dữ liệu điểm về Google Drive mà không bị lỗi cấp quyền).*
4. Bấm nút **`Triển khai` (Deploy)**.
5. Google sẽ hiện hộp thoại yêu cầu cấp quyền:
   - Bấm **`Ủy quyền truy cập` (Authorize access)** > Chọn tài khoản Google của bạn.
   - Nếu thấy cảnh báo *"Google chưa xác minh ứng dụng này"*, bấm vào liên kết nhỏ **`Nâng cao` (Advanced)** ở góc dưới bên trái > Chọn **`Đi tới Science Quiz Saver (không an toàn)`**.
   - Bấm **`Cho phép` (Allow)**.
6. Sau khi hoàn tất, sao chép chuỗi **URL ứng dụng web (Web App URL)**. Nó có dạng:
   `https://script.google.com/macros/s/AKfycbx.../exec`

---

## BƯỚC 4: Dán URL Vào Game

Bạn có 2 cách cực kỳ tiện lợi để gắn URL này:

- **Cách 1 (Nhanh nhất - Không cần sửa code):**
  1. Mở trang web game Khoa học (trên Vercel hoặc trình duyệt).
  2. Ở màn hình bắt đầu, tìm ô **`🌐 Google Apps Script URL (Lưu Sheets):`**.
  3. Dán đường link URL vừa copy ở Bước 3 vào ô này.
  4. Trình duyệt sẽ tự động lưu lại vĩnh viễn trong `localStorage`. Từ lượt thi sau bạn không cần nhập lại nữa!

- **Cách 2 (Cố định trong mã nguồn):**
  1. Mở file `index.html`.
  2. Tìm dòng số khoảng 375:
     ```javascript
     const GOOGLE_SCRIPT_URL = "";
     ```
  3. Dán URL của bạn vào giữa 2 dấu ngoặc kép:
     ```javascript
     const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx.../exec";
     ```
  4. Lưu file và đẩy lên GitHub (`git push`). Vercel sẽ tự động cập nhật cho mọi người chơi không cần nhập tay!
