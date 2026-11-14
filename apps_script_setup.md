# 📝 Hướng Dẫn Cài Đặt Google Apps Script Để Tự Động Lưu Kết Quả Thi

Hệ thống đã **tạo sẵn file Google Sheets** mang tên **`Ket_Qua_Thi_Khoa_Hoc`** ngay bên trong thư mục Google Drive của bạn:
- **Link trực tiếp mở file Google Sheets:**  
  👉 **[https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit](https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit)**
- **ID File Sheets:** `1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc`
- **Thư mục chứa:** [Google Drive Folder ID: `1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49`](https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49)

---

## BƯỚC 1: Mở Google Apps Script

1. Mở file Google Sheets trên: [Link mở Sheets](https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit)
2. Trên thanh menu của Google Sheets, chọn **`Tiện ích mở rộng` (Extensions)** > Chọn **`Apps Script`**.
   *(Hoặc truy cập trực tiếp: [script.google.com](https://script.google.com) rồi tạo dự án mới).*

---

## BƯỚC 2: Dán Mã Nguồn Google Apps Script

1. Xóa toàn bộ nội dung mẫu có sẵn trong file `Mã.gs` (Code.gs).
2. Sao chép và dán toàn bộ đoạn code dưới đây vào:

```javascript
/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ THI KHOA HỌC
 * File Google Sheets mục tiêu: Ket_Qua_Thi_Khoa_Hoc
 * Link mở trực tiếp: https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit
 */

const TARGET_SPREADSHEET_ID = "1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc";

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

    const spreadsheet = SpreadsheetApp.openById(TARGET_SPREADSHEET_ID);
    const sheet = spreadsheet.getActiveSheet();

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
    "File Google Sheets kết quả: https://docs.google.com/spreadsheets/d/" + TARGET_SPREADSHEET_ID + "/edit"
  );
}
```

3. Bấm biểu tượng 💾 **Lưu dự án** (Save project) hoặc nhấn tổ hợp phím `Ctrl + S` (hoặc `Cmd + S` trên Mac).

---

## BƯỚC 3: Triển Khai (Deploy) Dưới Dạng Web App

1. Ở góc trên bên phải, bấm vào nút màu xanh **`Triển khai` (Deploy)** > Chọn **`Tùy chọn triển khai mới...` (New deployment)**.
2. Bấm vào biểu tượng bánh răng ⚙️ bên cạnh dòng *Chọn loại* (Select type) > Chọn **`Ứng dụng web` (Web app)**.
3. Thiết lập 3 mục sau (bắt buộc đúng cấu hình):
   - **Mô tả (Description):** `V1 - Lưu kết quả thi Khoa Học`
   - **Thực thi dưới dạng (Execute as):** Chọn **`Tôi` (Me / email của bạn)**
   - **Người có quyền truy cập (Who has access):** Chọn **`Bất kỳ ai` (Anyone)**
     *(Để trang web game trên Vercel có thể gửi dữ liệu điểm về Google Drive mà không bị lỗi cấp quyền).*
4. Bấm nút **`Triển khai` (Deploy)**.
5. Google sẽ hiện hộp thoại yêu cầu cấp quyền:
   - Bấm **`Ủy quyền truy cập` (Authorize access)** > Chọn tài khoản Google của bạn.
   - Nếu thấy cảnh báo *"Google chưa xác minh ứng dụng này"*, bấm vào liên kết nhỏ **`Nâng cao` (Advanced)** ở góc dưới bên trái > Chọn **`Đi tới Dự án không có tiêu đề (không an toàn)`**.
   - Bấm **`Cho phép` (Allow)**.
6. Sau khi hoàn tất, sao chép chuỗi **URL ứng dụng web (Web App URL)**. Nó có dạng:
   `https://script.google.com/macros/s/AKfycbx.../exec`

---

## BƯỚC 4: Dán URL Vào Game

Bạn dán đường link URL vừa sao chép ở Bước 3 vào ô **`🌐 Google Apps Script URL (Lưu Sheets):`** ở màn hình bắt đầu của Game (hệ thống sẽ lưu vĩnh viễn trong máy).
Từ giờ, mỗi khi học sinh nộp bài thi, kết quả sẽ tự động được ghi thành 1 dòng mới vào file Google Sheets này!
