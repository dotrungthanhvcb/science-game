/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ & QUẢN LÝ TÀI KHOẢN HỌC SINH
 * 
 * File Google Sheets mục tiêu: Ket_Qua_Thi_Khoa_Hoc
 * Link mở trực tiếp: https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit
 * ID File: 1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc
 */

const TARGET_SPREADSHEET_ID = "1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc";

/**
 * Hàm tiện ích: Lấy hoặc tạo mới Sheet nếu chưa tồn tại
 */
function getOrCreateSheet(spreadsheet, sheetName, headers) {
  let sheet = spreadsheet.getSheetByName(sheetName);
  if (!sheet) {
    sheet = spreadsheet.insertSheet(sheetName);
    if (headers && headers.length > 0) {
      sheet.appendRow(headers);
    }
  }
  return sheet;
}

/**
 * Xử lý yêu cầu GET: Kiểm tra trạng thái hoặc Lấy Bảng Xếp Hạng (Leaderboard)
 */
function doGet(e) {
  try {
    const action = (e && e.parameter && e.parameter.action) ? e.parameter.action : "";
    const spreadsheet = SpreadsheetApp.openById(TARGET_SPREADSHEET_ID);

    if (action === "getLeaderboard") {
      const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
        "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
      ]);
      const data = accountSheet.getDataRange().getValues();
      const players = [];
      for (let i = 1; i < data.length; i++) {
        const row = data[i];
        if (row[1]) {
          players.push({
            username: String(row[1]),
            name: String(row[3] || row[1]),
            studentClass: String(row[4] || "Lớp 2"),
            totalTests: Number(row[5] || 0),
            highestScore: Number(row[6] || 0),
            badge: String(row[7] || "⭐")
          });
        }
      }
      // Sắp xếp theo điểm cao nhất giảm dần, sau đó theo số bài thi
      players.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        leaderboard: players.slice(0, 25)
      })).setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(
      "✅ Google Apps Script Web App đang hoạt động bình thường!\n" +
      "File Google Sheets kết quả: https://docs.google.com/spreadsheets/d/" + TARGET_SPREADSHEET_ID + "/edit"
    );
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Xử lý yêu cầu POST: Đăng Ký, Đăng Nhập, Nộp Kết Quả
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

    const action = payload.action || "submitScore";
    const spreadsheet = SpreadsheetApp.openById(TARGET_SPREADSHEET_ID);
    const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
      "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
    ]);

    // 1. ĐĂNG KÝ TÀI KHOẢN MỚI
    if (action === "register") {
      const username = String(payload.username || "").trim().toLowerCase();
      const pin = String(payload.pin || "").trim();
      const studentName = String(payload.studentName || "").trim() || "Bé Khoa Học";
      const studentClass = String(payload.studentClass || "Lớp 2").trim();

      if (!username || !pin) {
        return ContentService.createTextOutput(JSON.stringify({
          status: "error",
          message: "Vui lòng nhập Tên đăng nhập và Mã PIN 4 số!"
        })).setMimeType(ContentService.MimeType.JSON);
      }

      // Kiểm tra xem username đã tồn tại chưa
      const data = accountSheet.getDataRange().getValues();
      for (let i = 1; i < data.length; i++) {
        if (String(data[i][1]).trim().toLowerCase() === username) {
          return ContentService.createTextOutput(JSON.stringify({
            status: "error",
            message: "Tên đăng nhập [" + username + "] đã có bạn dùng rồi! Bé hãy chọn tên khác nhé."
          })).setMimeType(ContentService.MimeType.JSON);
        }
      }

      // Thêm tài khoản mới
      const now = new Date().toLocaleString("vi-VN");
      accountSheet.appendRow([now, username, pin, studentName, studentClass, 0, 0, "🌱 Tân Binh"]);

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        message: "Chúc mừng bé đã tạo tài khoản thành công!",
        user: {
          username: username,
          studentName: studentName,
          studentClass: studentClass,
          totalTests: 0,
          highestScore: 0,
          badge: "🌱 Tân Binh"
        }
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 2. ĐĂNG NHẬP
    if (action === "login") {
      const username = String(payload.username || "").trim().toLowerCase();
      const pin = String(payload.pin || "").trim();

      const data = accountSheet.getDataRange().getValues();
      for (let i = 1; i < data.length; i++) {
        const rowUser = String(data[i][1]).trim().toLowerCase();
        const rowPin = String(data[i][2]).trim();
        if (rowUser === username && rowPin === pin) {
          return ContentService.createTextOutput(JSON.stringify({
            status: "success",
            message: "Đăng nhập thành công! Chào mừng bé trở lại.",
            user: {
              username: String(data[i][1]),
              studentName: String(data[i][3]),
              studentClass: String(data[i][4]),
              totalTests: Number(data[i][5] || 0),
              highestScore: Number(data[i][6] || 0),
              badge: String(data[i][7] || "⭐")
            }
          })).setMimeType(ContentService.MimeType.JSON);
        }
      }

      return ContentService.createTextOutput(JSON.stringify({
        status: "error",
        message: "Sai Tên đăng nhập hoặc Mã PIN rồi bé ơi! Bé kiểm tra lại nhé."
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 3. LẤY BẢNG XẾP HẠNG QUA POST
    if (action === "getLeaderboard") {
      const data = accountSheet.getDataRange().getValues();
      const players = [];
      for (let i = 1; i < data.length; i++) {
        const row = data[i];
        if (row[1]) {
          players.push({
            username: String(row[1]),
            name: String(row[3] || row[1]),
            studentClass: String(row[4] || "Lớp 2"),
            totalTests: Number(row[5] || 0),
            highestScore: Number(row[6] || 0),
            badge: String(row[7] || "⭐")
          });
        }
      }
      players.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        leaderboard: players.slice(0, 25)
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 4. LƯU KẾT QUẢ BÀI THI (DEFAULT)
    const resultSheet = spreadsheet.getSheets()[0]; // Sheet đầu tiên lưu kết quả bài thi
    const timestamp = payload.timestamp || new Date().toLocaleString("vi-VN");
    const studentName = payload.studentName || "Học sinh";
    const studentClass = payload.studentClass || "Chưa nhập";
    const sources = payload.sources || "Tất cả nguồn";
    const totalQuestions = payload.totalQuestions !== undefined ? payload.totalQuestions : "";
    const correctCount = payload.correctCount !== undefined ? payload.correctCount : "";
    const wrongCount = payload.wrongCount !== undefined ? payload.wrongCount : "";
    const score = payload.score || "";
    const duration = payload.duration || "";
    const username = String(payload.username || "").trim().toLowerCase();

    // BỘ LỌC CHỐNG TRÙNG LẶP (DEDUPLICATION):
    const existingData = resultSheet.getDataRange().getValues();
    let isDuplicate = false;
    for (let i = 1; i < existingData.length; i++) {
      const rowTime = String(existingData[i][0]).trim();
      const rowName = String(existingData[i][1]).trim();
      const rowScore = String(existingData[i][7]).trim();
      if (rowTime === String(timestamp).trim() && rowName === String(studentName).trim() && rowScore === String(score).trim()) {
        isDuplicate = true;
        break;
      }
    }

    if (!isDuplicate) {
      resultSheet.appendRow([
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

      // Cập nhật số bài thi và điểm cao nhất vào Tai_Khoan nếu có username
      if (username) {
        const accData = accountSheet.getDataRange().getValues();
        let numScore = 0;
        if (typeof score === "string" && score.includes("/")) {
          numScore = parseFloat(score.split("/")[0]) || 0;
        } else {
          numScore = parseFloat(score) || 0;
        }

        for (let i = 1; i < accData.length; i++) {
          if (String(accData[i][1]).trim().toLowerCase() === username) {
            const currentTests = Number(accData[i][5] || 0) + 1;
            const currentHigh = Math.max(Number(accData[i][6] || 0), numScore);
            let badge = "🌱 Tân Binh";
            if (currentHigh >= 9.5) badge = "👑 Đại Kiện Tướng";
            else if (currentHigh >= 8.5) badge = "🥇 Học Sinh Xuất Sắc";
            else if (currentHigh >= 7.0) badge = "🥈 Ong Chăm Chỉ";
            else if (currentTests >= 5) badge = "🚀 Tay Đua Kiên Trì";

            accountSheet.getRange(i + 1, 6).setValue(currentTests);
            accountSheet.getRange(i + 1, 7).setValue(currentHigh);
            accountSheet.getRange(i + 1, 8).setValue(badge);
            break;
          }
        }
      }
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: isDuplicate ? "Đã ghi nhận (bỏ qua trùng lặp)" : "Đã lưu kết quả thi thành công!",
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
