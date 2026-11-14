/**
 * 🎓 GOOGLE APPS SCRIPT - TỰ ĐỘNG LƯU KẾT QUẢ & QUẢN LÝ TÀI KHOẢN HỌC SINH + PHÂN QUYỀN ADMIN
 * 
 * File Google Sheets mục tiêu: Ket_Qua_Thi_Khoa_Hoc
 * Link mở trực tiếp: https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit
 * ID File: 1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc
 * 
 * Cấu trúc 12 Cột Chuẩn:
 * 1. Mã lần thi (ID) | 2. Ngày thi | 3. Giờ thi | 4. Tên học sinh | 5. Lớp | 6. Ngôn ngữ
 * 7. Nguồn đề thi | 8. Tổng số câu | 9. Số câu đúng | 10. Số câu sai | 11. Điểm số | 12. Thời gian làm bài
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

    // 1. LẤY BẢNG VÀNG HOẶC DANH SÁCH NGƯỜI DÙNG QUẢN TRỊ (ADMIN)
    if (action === "getLeaderboard" || action === "getUsers") {
      const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
        "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
      ]);
      const data = accountSheet.getDataRange().getDisplayValues();
      const userMap = {};

      // Đọc từ bảng Tai_Khoan
      for (let i = 1; i < data.length; i++) {
        const row = data[i];
        const u = String(row[1] || "").trim().toLowerCase();
        if (u) {
          userMap[u] = {
            registeredAt: String(row[0] || ""),
            username: u,
            name: String(row[3] || row[1]),
            studentClass: String(row[4] || "Lớp 2"),
            totalTests: Number(row[5] || 0),
            highestScore: Number(row[6] || 0),
            badge: String(row[7] || "🌱 Tân Binh")
          };
        }
      }

      // Quét thêm bảng kết quả thi để bổ sung các học sinh đã từng thi (như Na thối, Bố Na...)
      const resultSheet = spreadsheet.getSheets()[0];
      const resData = resultSheet.getDataRange().getDisplayValues();
      for (let j = 1; j < resData.length; j++) {
        const rName = String(resData[j][3] || "").trim();
        const rClass = String(resData[j][4] || "Lớp 2").trim();
        const rScoreStr = String(resData[j][10] || "0");
        const rScore = parseFloat(rScoreStr.split("/")[0]) || 0;
        const rDate = String(resData[j][1] || "");

        if (rName && rName !== "Học sinh") {
          const key = rName.toLowerCase();
          if (!userMap[key]) {
            userMap[key] = {
              registeredAt: rDate || "14/11/2026",
              username: key.replace(/\s+/g, ""),
              name: rName,
              studentClass: rClass,
              totalTests: 0,
              highestScore: 0,
              badge: "🌱 Tân Binh"
            };
          }
          userMap[key].totalTests = (userMap[key].totalTests || 0) + 1;
          userMap[key].highestScore = Math.max(userMap[key].highestScore || 0, rScore);
          if (userMap[key].highestScore >= 9.5) userMap[key].badge = "👑 Đại Kiện Tướng";
          else if (userMap[key].highestScore >= 8.5) userMap[key].badge = "🥇 Học Sinh Xuất Sắc";
          else if (userMap[key].highestScore >= 7.0) userMap[key].badge = "🥈 Ong Chăm Chỉ";
        }
      }

      const userList = Object.values(userMap);
      userList.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        users: userList,
        leaderboard: userList.slice(0, 30)
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

    // 1. ĐĂNG KÝ TÀI KHOẢN MỚI
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

      if (username === "admin") {
        return ContentService.createTextOutput(JSON.stringify({
          status: "error", message: "Tên đăng nhập [admin] là tài khoản quản trị hệ thống, không thể đăng ký mới!"
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
        user: { username, studentName, studentClass, role: "student", totalTests: 0, highestScore: 0, badge: "🌱 Tân Binh" }
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 2. ĐĂNG NHẬP (HỖ TRỢ TÀI KHOẢN ADMIN ĐẶC QUYỀN)
    if (action === "login") {
      const username = String(payload.username || "").trim().toLowerCase();
      const pin = String(payload.pin || "").trim();

      // KIỂM TRA ĐẶC QUYỀN ADMIN
      if (username === "admin" && pin === "11081993") {
        return ContentService.createTextOutput(JSON.stringify({
          status: "success",
          user: {
            username: "admin",
            studentName: "Quản Trị Viên (Admin)",
            studentClass: "Toàn Trường",
            role: "admin",
            totalTests: 999,
            highestScore: 10,
            badge: "👑 Quản Trị Viên"
          }
        })).setMimeType(ContentService.MimeType.JSON);
      }

      const data = accountSheet.getDataRange().getDisplayValues();
      for (let i = 1; i < data.length; i++) {
        if (String(data[i][1]).trim().toLowerCase() === username && String(data[i][2]).trim() === pin) {
          return ContentService.createTextOutput(JSON.stringify({
            status: "success",
            user: {
              username: String(data[i][1]),
              studentName: String(data[i][3]),
              studentClass: String(data[i][4]),
              role: "student",
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

    // 3. LƯU KẾT QUẢ THI (12 CỘT CHUẨN + CHỐNG TRÙNG LẶP TUYỆT ĐỐI)
    const resultSheet = spreadsheet.getSheets()[0];
    
    // Tách ngày và giờ
    const fullTimestamp = String(payload.timestamp || new Date().toLocaleString("vi-VN")).trim();
    let quizDate = String(payload.quizDate || "").trim();
    let quizTime = String(payload.quizTime || "").trim();

    if (!quizDate || !quizTime) {
      const parts = fullTimestamp.split(" ");
      if (parts.length >= 2) {
        quizTime = parts[0];
        quizDate = parts[1];
      } else {
        quizDate = new Date().toLocaleDateString("vi-VN");
        quizTime = new Date().toLocaleTimeString("vi-VN");
      }
    }

    const quizId = String(payload.quizId || "QUIZ-" + quizTime.replace(/[:]/g, "")).trim();
    const studentName = String(payload.studentName || "Học sinh").trim();
    const studentClass = String(payload.studentClass || "Lớp 2").trim();
    
    // Ngôn ngữ chính xác
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
    if (!score || score === "" || totalQuestions === "" || (studentName === "Học sinh" && !score)) {
      return ContentService.createTextOutput(JSON.stringify({
        status: "skipped", message: "Bỏ qua dòng trống hoặc dữ liệu thử nghiệm."
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // CHỐNG TRÙNG LẶP TUYỆT ĐỐI THEO MÃ ID HOẶC (NGÀY + GIỜ + TÊN HỌC SINH)
    const existingData = resultSheet.getDataRange().getDisplayValues();
    let isDuplicate = false;
    for (let i = 1; i < existingData.length; i++) {
      const rowId = String(existingData[i][0]).trim();
      const rowDate = String(existingData[i][1]).trim();
      const rowTime = String(existingData[i][2]).trim();
      const rowName = String(existingData[i][3]).trim();

      if (rowId === quizId || (rowDate === quizDate && rowTime === quizTime && rowName === studentName)) {
        isDuplicate = true;
        break;
      }
    }

    if (!isDuplicate) {
      // TỰ ĐỘNG KHỚP CỘT CHUẨN XÁC THEO TÊN TIÊU ĐỀ
      const lastCol = Math.max(resultSheet.getLastColumn(), 12);
      const headers = resultSheet.getRange(1, 1, 1, lastCol).getDisplayValues()[0];
      const rowData = [];

      headers.forEach(h => {
        const col = String(h).trim().toLowerCase();
        if (col.includes("mã") || col.includes("id")) {
          rowData.push(quizId);
        } else if (col.includes("ngày") || col === "date") {
          rowData.push(quizDate);
        } else if (col.includes("giờ") || col === "time") {
          rowData.push(quizTime);
        } else if (col.includes("thời gian nộp") || col.includes("timestamp")) {
          rowData.push(fullTimestamp);
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

      // Cập nhật số bài thi và điểm cao nhất cho tài khoản học sinh
      if (username && username !== "admin") {
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
      message: isDuplicate ? "Bản ghi đã tồn tại, tránh ghi trùng lặp!" : "Đã lưu kết quả thi thành công!",
      quizId: quizId
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
