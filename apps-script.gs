/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ THI KHOA HỌC
 * 
 * Thư mục Google Drive mục tiêu:
 * https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49
 * ID Thư mục: 1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49
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

    // Trả về JSON thông báo thành công
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
 * Xử lý yêu cầu GET kiểm tra trạng thái hoạt động của Web App
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
    // Tạo file Google Sheets mới ngay bên trong thư mục đích
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

    // Định dạng giao diện tiêu đề đẹp mắt
    const headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#4361EE")
               .setFontColor("#FFFFFF")
               .setFontWeight("bold")
               .setFontSize(11)
               .setHorizontalAlignment("center");
    
    sheet.setFrozenRows(1);
    sheet.setRowHeight(1, 35);

    // Căn giữa các cột số liệu
    sheet.getRange(2, 5, 1000, 5).setHorizontalAlignment("center");
  }

  return sheet;
}
