/**
 * 🎓 Science Quiz - Google Apps Script
 * Kết nối game HTML Quiz với Google Sheets
 * 
 * CÁCH SỬ DỤNG:
 * 1. Mở Google Sheets đã tạo
 * 2. Vào Extensions > Apps Script
 * 3. Dán toàn bộ code này vào editor
 * 4. Thay SPREADSHEET_ID bên dưới bằng ID thực của Sheets
 * 5. Click Deploy > New deployment > Web App
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 6. Copy Web App URL và dán vào game HTML
 */

// ═══════════════════════════════════════
// CẤU HÌNH — Thay bằng Spreadsheet ID thực
// ═══════════════════════════════════════
const SPREADSHEET_ID = 'THAY_BANG_SPREADSHEET_ID_THUC';

const SHEET_QUESTIONS = 'Ngân Hàng Câu Hỏi';
const SHEET_LOG       = 'Nhật Ký Luyện Tập';
const SHEET_WRONG     = 'Câu Hỏi Sai';

// ═══════════════════════════════════════
// HANDLER CHÍNH — xử lý GET và POST
// ═══════════════════════════════════════
function doGet(e) {
  const action = e.parameter.action;

  if (action === 'getQuestions') {
    return getQuestions(e);
  }

  // Default: trả về trang test
  return ContentService.createTextOutput(JSON.stringify({ status: 'ok', message: 'Science Quiz API hoạt động!' }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  try {
    const payload = JSON.parse(e.postData.contents);
    const action = payload.action;

    if (action === 'saveResult') {
      return saveResult(payload.data);
    }
    if (action === 'saveWrongQuestion') {
      return saveWrongQuestion(payload.data);
    }

    return jsonResponse({ ok: false, error: 'Unknown action' });
  } catch (err) {
    return jsonResponse({ ok: false, error: err.toString() });
  }
}

// ═══════════════════════════════════════
// LẤY CÂU HỎI từ Google Sheets
// ═══════════════════════════════════════
function getQuestions(e) {
  try {
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = ss.getSheetByName(SHEET_QUESTIONS);
    const data = sheet.getDataRange().getValues();

    if (data.length <= 1) {
      return jsonResponse({ questions: [], total: 0 });
    }

    // Header: ID, Chủ Đề, Chủ Đề Con, Câu Hỏi, Loại, A, B, C, D, Đáp Án Đúng, Độ Khó, Giải Thích, Nguồn
    const questions = data.slice(1).map(row => ({
      id:      row[0]  || '',
      topic:   row[1]  || '',
      sub:     row[2]  || '',
      q:       row[3]  || '',
      type:    row[4]  || 'MC',
      a:       row[5]  || '',
      b:       row[6]  || '',
      c:       row[7]  || '',
      d:       row[8]  || '',
      ans:     row[9]  || '',
      diff:    row[10] || 1,
      explain: row[11] || '',
      source:  row[12] || '',
    })).filter(q => q.q && q.ans); // lọc các hàng trống

    return jsonResponse({ questions, total: questions.length });
  } catch (err) {
    return jsonResponse({ error: err.toString() });
  }
}

// ═══════════════════════════════════════
// LƯU KẾT QUẢ vào Nhật Ký Luyện Tập
// ═══════════════════════════════════════
function saveResult(data) {
  try {
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = ss.getSheetByName(SHEET_LOG);

    sheet.appendRow([
      data.datetime,   // Ngày Giờ
      data.session,    // Phiên ID
      data.name,       // Tên Bé
      data.topic,      // Chủ Đề
      data.total,      // Tổng Câu
      data.correct,    // Đúng
      data.wrong,      // Sai
      data.pct,        // Điểm %
      data.time,       // Thời Gian (phút)
      data.wrongIds,   // Câu Sai (IDs)
    ]);

    // Cập nhật Dashboard tự động
    updateDashboard(ss, data);

    return jsonResponse({ ok: true, message: 'Đã lưu kết quả!' });
  } catch (err) {
    return jsonResponse({ ok: false, error: err.toString() });
  }
}

// ═══════════════════════════════════════
// LƯU CÂU HỎI SAI để ôn lại
// ═══════════════════════════════════════
function saveWrongQuestion(data) {
  try {
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = ss.getSheetByName(SHEET_WRONG);

    sheet.appendRow([
      data.datetime,
      data.questionId,
      data.questionText,
      data.userAnswer,
      data.correctAnswer,
    ]);

    return jsonResponse({ ok: true });
  } catch (err) {
    return jsonResponse({ ok: false, error: err.toString() });
  }
}

// ═══════════════════════════════════════
// CẬP NHẬT DASHBOARD
// ═══════════════════════════════════════
function updateDashboard(ss, latestData) {
  try {
    const logSheet = ss.getSheetByName(SHEET_LOG);
    const dashSheet = ss.getSheetByName('Dashboard');

    if (!dashSheet) return;

    const logData = logSheet.getDataRange().getValues();
    if (logData.length <= 1) return;

    const rows = logData.slice(1); // bỏ header
    const totalSessions = rows.length;
    const totalQuestions = rows.reduce((s, r) => s + (parseInt(r[4]) || 0), 0);
    const avgScore = rows.reduce((s, r) => s + (parseFloat(r[7]) || 0), 0) / totalSessions;
    const totalCorrect = rows.reduce((s, r) => s + (parseInt(r[5]) || 0), 0);

    // Thống kê theo chủ đề
    const topicStats = {};
    rows.forEach(r => {
      const topics = (r[3] || '').split(',');
      const pct = parseFloat(r[7]) || 0;
      topics.forEach(t => {
        t = t.trim();
        if (!t) return;
        if (!topicStats[t]) topicStats[t] = { sum: 0, count: 0 };
        topicStats[t].sum += pct;
        topicStats[t].count++;
      });
    });

    // Ghi vào Dashboard
    dashSheet.getRange('B3').setValue(totalSessions);
    dashSheet.getRange('B4').setValue(totalQuestions);
    dashSheet.getRange('B5').setValue(avgScore.toFixed(1));
    dashSheet.getRange('B6').setValue(totalCorrect);

    // Phân tích điểm yếu/mạnh theo chủ đề
    const topicRows = Object.entries(topicStats)
      .map(([topic, stat]) => [topic, (stat.sum / stat.count).toFixed(1) + '%', stat.count + ' phiên'])
      .sort((a, b) => parseFloat(a[1]) - parseFloat(b[1])); // sắp xếp điểm thấp lên trên

    if (topicRows.length > 0) {
      dashSheet.getRange('A9').setValue('📊 Điểm Trung Bình Theo Chủ Đề (thấp nhất lên đầu)');
      dashSheet.getRange('A10:C10').setValues([['Chủ Đề', 'Điểm TB', 'Số Phiên']]);
      dashSheet.getRange(11, 1, topicRows.length, 3).setValues(topicRows);
    }

    // Phiên mới nhất
    dashSheet.getRange('A17').setValue('📅 Phiên Học Gần Nhất');
    dashSheet.getRange('B18').setValue(latestData.datetime);
    dashSheet.getRange('B19').setValue(`${latestData.correct}/${latestData.total} câu đúng (${latestData.pct}%)`);
    dashSheet.getRange('B20').setValue(latestData.topic);

  } catch (err) {
    console.log('Dashboard update error:', err);
  }
}

// ═══════════════════════════════════════
// HELPER
// ═══════════════════════════════════════
function jsonResponse(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

// ═══════════════════════════════════════
// SETUP: Tạo header sheets tự động
// ═══════════════════════════════════════
function setupSheets() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);

  // Ngân Hàng Câu Hỏi header
  let sheet = ss.getSheetByName(SHEET_QUESTIONS);
  if (!sheet) sheet = ss.insertSheet(SHEET_QUESTIONS);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['ID','Chủ Đề','Chủ Đề Con','Câu Hỏi','Loại','Đáp Án A','Đáp Án B','Đáp Án C','Đáp Án D','Đáp Án Đúng','Độ Khó','Giải Thích','Nguồn']);
    sheet.getRange(1, 1, 1, 13).setBackground('#4285F4').setFontColor('#FFFFFF').setFontWeight('bold');
  }

  // Nhật Ký header
  sheet = ss.getSheetByName(SHEET_LOG);
  if (!sheet) sheet = ss.insertSheet(SHEET_LOG);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Ngày Giờ','Phiên ID','Tên Bé','Chủ Đề','Tổng Câu','Đúng','Sai','Điểm %','Thời Gian (phút)','Câu Sai (IDs)']);
    sheet.getRange(1, 1, 1, 10).setBackground('#34A853').setFontColor('#FFFFFF').setFontWeight('bold');
  }

  // Câu Hỏi Sai header
  sheet = ss.getSheetByName(SHEET_WRONG);
  if (!sheet) sheet = ss.insertSheet(SHEET_WRONG);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Ngày','Câu Hỏi ID','Câu Hỏi','Đáp Án Bé Chọn','Đáp Án Đúng']);
    sheet.getRange(1, 1, 1, 5).setBackground('#EA4335').setFontColor('#FFFFFF').setFontWeight('bold');
  }

  // Dashboard header
  sheet = ss.getSheetByName('Dashboard');
  if (!sheet) sheet = ss.insertSheet('Dashboard');
  sheet.getRange('A1').setValue('📊 DASHBOARD TIẾN BỘ ÔN LUYỆN');
  sheet.getRange('A1').setFontSize(16).setFontWeight('bold').setFontColor('#4285F4');
  sheet.getRange('A3').setValue('Tổng phiên học');
  sheet.getRange('A4').setValue('Tổng câu đã làm');
  sheet.getRange('A5').setValue('Điểm TB (%)');
  sheet.getRange('A6').setValue('Tổng câu đúng');

  SpreadsheetApp.getUi().alert('✅ Setup hoàn thành! Các sheet đã được tạo.');
}
