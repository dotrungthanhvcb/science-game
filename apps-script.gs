/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ THI KHOA HỌC
 * 
 * File Google Sheets mục tiêu: Ket_Qua_Thi_Khoa_Hoc
 * Link mở trực tiếp: https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit
 * ID File: 1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc
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
    "File Google Sheets kết quả: https://docs.google.com/spreadsheets/d/" + TARGET_SPREADSHEET_ID + "/edit"
  );
}
