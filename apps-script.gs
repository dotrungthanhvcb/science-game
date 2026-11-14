/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ & QUẢN LÝ TÀI KHOẢN HỌC SINH
 * 
 * File Google Sheets mục tiêu: Ket_Qua_Thi_Khoa_Hoc
 * Link mở trực tiếp: https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit
 * ID File: 1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc
 */

const TARGET_SPREADSHEET_ID = "1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc";

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

function doGet(e) {
  try {
    const action = (e && e.parameter && e.parameter.action) ? e.parameter.action : "";
    const spreadsheet = SpreadsheetApp.openById(TARGET_SPREADSHEET_ID);

    if (action === "getLeaderboard") {
      const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
        "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
      ]);
      const data = accountSheet.getDataRange().getDisplayValues();
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

    return ContentService.createTextOutput(
      "✅ Google Apps Script Web App đang hoạt động bình thường!\n" +
      "File Google Sheets kết quả: https://docs.google.com/spreadsheets/d/" + TARGET_SPREADSHEET_ID + "/edit"
    );
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doPost(e) {
  try {
    let payload = {};
    if (e && e.postData && e.postData.contents) {
      try { payload = JSON.parse(e.postData.contents); } catch (err) { payload = e.parameter || {}; }
    } else if (e && e.parameter) {
      payload = e.parameter;
    }

    const action = payload.action || "submitScore";
    const spreadsheet = SpreadsheetApp.openById(TARGET_SPREADSHEET_ID);
    const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
      "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
    ]);

    // 1. ĐĂNG KÝ
    if (action === "register") {
      const username = String(payload.username || "").trim().toLowerCase();
      const pin = String(payload.pin || "").trim();
      const studentName = String(payload.studentName || "").trim() || "Bé Khoa Học";
      const studentClass = String(payload.studentClass || "Lớp 2").trim();

      if (!username || !pin) {
        return ContentService.createTextOutput(JSON.stringify({
          status: "error", message: "Vui lòng nhập Tên đăng nhập và Mã PIN!"
        })).setMimeType(ContentService.MimeType.JSON);
      }

      const data = accountSheet.getDataRange().getDisplayValues();
      for (let i = 1; i < data.length; i++) {
        if (String(data[i][1]).trim().toLowerCase() === username) {
          return ContentService.createTextOutput(JSON.stringify({
            status: "error", message: "Tên đăng nhập [" + username + "] đã có bạn dùng rồi!"
          })).setMimeType(ContentService.MimeType.JSON);
        }
      }

      accountSheet.appendRow([new Date().toLocaleString("vi-VN"), username, pin, studentName, studentClass, 0, 0, "🌱 Tân Binh"]);
      return ContentService.createTextOutput(JSON.stringify({
        status: "success", message: "Tạo tài khoản thành công!",
        user: { username, studentName, studentClass, totalTests: 0, highestScore: 0, badge: "🌱 Tân Binh" }
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 2. ĐĂNG NHẬP
    if (action === "login") {
      const username = String(payload.username || "").trim().toLowerCase();
      const pin = String(payload.pin || "").trim();
      const data = accountSheet.getDataRange().getDisplayValues();
      for (let i = 1; i < data.length; i++) {
        if (String(data[i][1]).trim().toLowerCase() === username && String(data[i][2]).trim() === pin) {
          return ContentService.createTextOutput(JSON.stringify({
            status: "success",
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
        status: "error", message: "Sai Tên đăng nhập hoặc Mã PIN rồi bé ơi!"
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 3. LƯU KẾT QUẢ THI
    const resultSheet = spreadsheet.getSheets()[0];
    const timestamp = String(payload.timestamp || new Date().toLocaleString("vi-VN")).trim();
    const studentName = String(payload.studentName || "Học sinh").trim();
    const studentClass = String(payload.studentClass || "Lớp 2").trim();
    
    // Xử lý Ngôn ngữ
    let language = "Tiếng Việt";
    if (payload.language === "bilingual" || payload.language === "Song ngữ Anh - Việt") {
      language = "Song ngữ Anh - Việt";
    } else if (payload.language === "en" || payload.language === "Tiếng Anh") {
      language = "Tiếng Anh";
    } else if (payload.language) {
      language = String(payload.language).trim();
    }

    const sources = String(payload.sources || "Tất cả nguồn").trim();
    const totalQuestions = payload.totalQuestions !== undefined ? payload.totalQuestions : "";
    const correctCount = payload.correctCount !== undefined ? payload.correctCount : "";
    const wrongCount = payload.wrongCount !== undefined ? payload.wrongCount : "";
    const score = String(payload.score || "").trim();
    const duration = String(payload.duration || "").trim();
    const username = String(payload.username || "").trim().toLowerCase();

    // Bỏ qua nếu dòng rỗng hoặc không có điểm số thực tế
    if (!score || score === "" || totalQuestions === "" || studentName === "Học sinh" && !score) {
      return ContentService.createTextOutput(JSON.stringify({
        status: "skipped", message: "Bỏ qua dòng trống hoặc dữ liệu thử nghiệm."
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // CHỐNG TRÙNG LẶP TUYỆT ĐỐI BẰNG getDisplayValues()
    const existingData = resultSheet.getDataRange().getDisplayValues();
    let isDuplicate = false;
    for (let i = 1; i < existingData.length; i++) {
      const rowTime = String(existingData[i][0]).trim();
      const rowName = String(existingData[i][1]).trim();
      if (rowTime === timestamp && rowName === studentName) {
        isDuplicate = true;
        break;
      }
    }

    if (!isDuplicate) {
      // TỰ ĐỘNG KHỚP CỘT CHUẨN XÁC THEO TÊN TIÊU ĐỀ (KHÔNG BAO GIỜ BỊ LỆCH CỘT)
      const lastCol = Math.max(resultSheet.getLastColumn(), 10);
      const headers = resultSheet.getRange(1, 1, 1, lastCol).getDisplayValues()[0];
      const rowData = [];

      headers.forEach(h => {
        const col = String(h).trim().toLowerCase();
        if (col.includes("thời gian nộp") || col.includes("ngày giờ") || col === "timestamp") {
          rowData.push(timestamp);
        } else if (col.includes("tên") || col.includes("học sinh") || col === "studentname") {
          rowData.push(studentName);
        } else if (col.includes("lớp") || col === "class") {
          rowData.push(studentClass);
        } else if (col.includes("ngôn ngữ") || col === "language") {
          rowData.push(language);
        } else if (col.includes("nguồn") || col === "sources") {
          rowData.push(sources);
        } else if (col.includes("tổng") || col === "total") {
          rowData.push(totalQuestions);
        } else if (col.includes("đúng") || col === "correct") {
          rowData.push(correctCount);
        } else if (col.includes("sai") || col === "wrong") {
          rowData.push(wrongCount);
        } else if (col.includes("điểm") || col === "score") {
          rowData.push(score);
        } else if (col.includes("thời gian làm") || col.includes("duration")) {
          rowData.push(duration);
        } else {
          rowData.push("");
        }
      });

      resultSheet.appendRow(rowData);

      if (username) {
        const accData = accountSheet.getDataRange().getDisplayValues();
        let numScore = parseFloat(String(score).split("/")[0]) || 0;
        for (let i = 1; i < accData.length; i++) {
          if (String(accData[i][1]).trim().toLowerCase() === username) {
            const currentTests = Number(accData[i][5] || 0) + 1;
            const currentHigh = Math.max(Number(accData[i][6] || 0), numScore);
            let badge = "🌱 Tân Binh";
            if (currentHigh >= 9.5) badge = "👑 Đại Kiện Tướng";
            else if (currentHigh >= 8.5) badge = "🥇 Học Sinh Xuất Sắc";
            else if (currentHigh >= 7.0) badge = "🥈 Ong Chăm Chỉ";

            accountSheet.getRange(i + 1, 6).setValue(currentTests);
            accountSheet.getRange(i + 1, 7).setValue(currentHigh);
            accountSheet.getRange(i + 1, 8).setValue(badge);
            break;
          }
        }
      }
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: isDuplicate ? "skipped" : "success",
      message: isDuplicate ? "Bản ghi đã tồn tại, tránh ghi trùng lặp!" : "Đã lưu kết quả thi thành công!"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
