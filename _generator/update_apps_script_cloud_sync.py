#!/usr/bin/env python3

APPS_SCRIPT_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/apps-script.gs"
SETUP_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/apps_script_setup.md"

with open(APPS_SCRIPT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ADD getResults AND GET login TO doGet
old_doget = """    if (action === "getLeaderboard" || action === "getUsers") {"""

new_doget = """    // 1. LẤY TOÀN BỘ KẾT QUẢ THI ĐỂ ĐỒNG BỘ VỀ CLIENT (CHO PHÉP HỌC SINH XEM BÀI CỦA MÌNH TRÊN MỌI THIẾT BỊ)
    if (action === "getResults") {
      const resultSheet = spreadsheet.getSheets()[0];
      const data = resultSheet.getDataRange().getDisplayValues();
      const results = [];
      for (let i = 1; i < data.length; i++) {
        const row = data[i];
        if (row[0] || row[1]) {
          results.push({
            id: String(row[0] || ""),
            quizId: String(row[0] || ""),
            quizDate: String(row[1] || ""),
            quizTime: String(row[2] || ""),
            timestamp: (String(row[2] || "") + " " + String(row[1] || "")).trim(),
            studentName: String(row[3] || "Học sinh"),
            studentClass: String(row[4] || "Lớp 2"),
            language: String(row[5] || "Tiếng Việt"),
            sources: String(row[6] || ""),
            totalQuestions: Number(row[7] || 0),
            correctCount: Number(row[8] || 0),
            wrongCount: Number(row[9] || 0),
            score: String(row[10] || "0/10"),
            score10: parseFloat(String(row[10] || "0").split("/")[0]) || 0,
            pct: parseInt((String(row[10] || "").match(/\\((\\d+)%\\)/) || [0, 0])[1]) || 0,
            duration: String(row[11] || "00:00"),
            syncedToSheets: true
          });
        }
      }
      return ContentService.createTextOutput(JSON.stringify({ status: "success", results: results }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // 2. ĐĂNG NHẬP QUA GET ĐỂ TRẢ VỀ DỮ LIỆU TÀI KHOẢN CHÍNH XÁC (KHÔNG BỊ CHẶN CORS)
    if (action === "login") {
      const username = String(e.parameter.username || "").trim().toLowerCase();
      const pin = String(e.parameter.pin || "").trim();

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

      const accountSheet = getOrCreateSheet(spreadsheet, "Tai_Khoan", [
        "Thời gian đăng ký", "Tên đăng nhập", "Mã PIN", "Họ tên bé", "Lớp", "Số bài thi", "Điểm cao nhất", "Huy hiệu"
      ]);
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

    // 3. LẤY BẢNG VÀNG HOẶC DANH SÁCH NGƯỜI DÙNG QUẢN TRỊ (ADMIN)
    if (action === "getLeaderboard" || action === "getUsers") {"""

if old_doget in content:
    content = content.replace(old_doget, new_doget, 1)
    print("1. Added getResults and GET login to apps-script.gs")

with open(APPS_SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

with open(SETUP_PATH, "w", encoding="utf-8") as f:
    f.write("# 📝 Hướng Dẫn Cập Nhật Google Apps Script (Đồng Bộ Hai Chiều & Phân Quyền)\n\n" +
            "```javascript\n" + content + "\n```\n")

print("apps-script.gs and apps_script_setup.md updated successfully!")
