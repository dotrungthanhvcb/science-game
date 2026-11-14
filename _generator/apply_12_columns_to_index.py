#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. ADD SESSION STATE VARIABLES
target_state_vars = "let isQuizSubmitted = false; // Đã nộp bài hay chưa (khóa bài làm khi true)"
replacement_state_vars = """let isQuizSubmitted = false; // Đã nộp bài hay chưa (khóa bài làm khi true)

// SESSION TRACKING VARIABLES (LƯU CHÍNH XÁC ID, NGÀY, GIỜ, NGÔN NGỮ KHI BẮT ĐẦU BÀI THI)
let currentSessionQuizId = '';
let currentSessionDate = '';
let currentSessionTime = '';
let currentSessionLanguageMode = 'vi';
let currentSessionLangLabel = 'Tiếng Việt';"""

if target_state_vars in content:
    content = content.replace(target_state_vars, replacement_state_vars, 1)
    print("1. Added session tracking state variables.")
else:
    print("WARNING: target_state_vars not found!")

# 2. UPDATE startQuiz() TO LOCK IN SESSION VARIABLES
target_start_quiz = """function startQuiz() {
  saveSettings();
  let pool = getFilteredPool();"""

replacement_start_quiz = """function startQuiz() {
  saveSettings();

  // Khóa thông tin bài thi tại thời điểm bắt đầu
  const now = new Date();
  currentSessionDate = now.toLocaleDateString('vi-VN');
  currentSessionTime = now.toLocaleTimeString('vi-VN');
  currentSessionQuizId = 'QUIZ-' + currentSessionTime.replace(/[:]/g, '');

  const langSelect = document.getElementById('language-mode-select');
  if (langSelect) {
    currentLanguageMode = langSelect.value;
  }
  currentSessionLanguageMode = currentLanguageMode;
  currentSessionLangLabel = currentLanguageMode === 'bilingual' ? 'Song ngữ Anh - Việt' : (currentLanguageMode === 'en' ? 'Tiếng Anh' : 'Tiếng Việt');

  let pool = getFilteredPool();"""

if target_start_quiz in content:
    content = content.replace(target_start_quiz, replacement_start_quiz, 1)
    print("2. Updated startQuiz() to lock session variables.")
else:
    print("WARNING: target_start_quiz not found!")

# 3. UPDATE submitAndFinishQuiz() TO SAVE SESSION ID, DATE, TIME & ACCURATE LANGUAGE
old_finish_block = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  const currentRecordId = 'REC_' + Date.now();
  const currentLangLabel = currentLanguageMode === 'bilingual' ? 'Song ngữ Anh - Việt' : (currentLanguageMode === 'en' ? 'Tiếng Anh' : 'Tiếng Việt');
  saveQuizToLocalHistory({
    id: currentRecordId,
    syncedToSheets: false,
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    language: currentLangLabel,"""

new_finish_block = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  const currentRecordId = currentSessionQuizId || ('QUIZ-' + Date.now());
  saveQuizToLocalHistory({
    id: currentRecordId,
    quizId: currentSessionQuizId,
    quizDate: currentSessionDate,
    quizTime: currentSessionTime,
    syncedToSheets: false,
    timestamp: `${currentSessionTime} ${currentSessionDate}`,
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    language: currentSessionLangLabel,"""

if old_finish_block in content:
    content = content.replace(old_finish_block, new_finish_block, 1)
    print("3. Updated submitAndFinishQuiz() with session variables.")
else:
    print("WARNING: old_finish_block not found!")

# 4. UPDATE sendDataToAppsScript() TO SEND quizId, quizDate, quizTime, language
old_send_block = """  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;
  const currentLangLabel = currentLanguageMode === 'bilingual' ? 'Song ngữ Anh - Việt' : (currentLanguageMode === 'en' ? 'Tiếng Anh' : 'Tiếng Việt');
  const payload = {
    action: 'submitScore',
    username: storedAcc ? storedAcc.username : '',
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name') ? document.getElementById('user-name').value.trim() : 'Học sinh',
    studentClass: (function() {
      const elem = document.getElementById('student-class');
      if (!elem) return 'Lớp 2';
      const val = elem.value;
      if (val === 'all') return 'Lớp 1 - 5 (Hỗn hợp)';
      return 'Lớp ' + val;
    })(),
    language: currentLangLabel,"""

new_send_block = """  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;
  const qDate = currentSessionDate || new Date().toLocaleDateString('vi-VN');
  const qTime = currentSessionTime || new Date().toLocaleTimeString('vi-VN');
  const qId = currentSessionQuizId || ('QUIZ-' + qTime.replace(/[:]/g, ''));
  const qLang = currentSessionLangLabel || (currentLanguageMode === 'bilingual' ? 'Song ngữ Anh - Việt' : (currentLanguageMode === 'en' ? 'Tiếng Anh' : 'Tiếng Việt'));

  const payload = {
    action: 'submitScore',
    quizId: qId,
    quizDate: qDate,
    quizTime: qTime,
    username: storedAcc ? storedAcc.username : '',
    timestamp: `${qTime} ${qDate}`,
    studentName: document.getElementById('user-name') ? document.getElementById('user-name').value.trim() : 'Học sinh',
    studentClass: (function() {
      const elem = document.getElementById('student-class');
      if (!elem) return 'Lớp 2';
      const val = elem.value;
      if (val === 'all') return 'Lớp 1 - 5 (Hỗn hợp)';
      return 'Lớp ' + val;
    })(),
    language: qLang,"""

if old_send_block in content:
    content = content.replace(old_send_block, new_send_block, 1)
    print("4. Updated sendDataToAppsScript() with quizId, quizDate, quizTime.")
else:
    print("WARNING: old_send_block not found!")

# 5. UPDATE syncAllHistoryToSheets() PAYLOAD
old_sync_item = """  unsyncedList.forEach((r, idx) => {
    const payload = {
      action: 'submitScore',
      username: storedAcc ? storedAcc.username : '',
      timestamp: r.timestamp,
      studentName: r.studentName,
      studentClass: r.studentClass || '',
      language: r.language || 'Tiếng Việt',"""

new_sync_item = """  unsyncedList.forEach((r, idx) => {
    const parts = (r.timestamp || "").split(" ");
    const qTime = r.quizTime || (parts.length >= 2 ? parts[0] : new Date().toLocaleTimeString("vi-VN"));
    const qDate = r.quizDate || (parts.length >= 2 ? parts[1] : new Date().toLocaleDateString("vi-VN"));
    const qId = r.quizId || r.id || ("QUIZ-" + qTime.replace(/[:]/g, ""));

    const payload = {
      action: 'submitScore',
      quizId: qId,
      quizDate: qDate,
      quizTime: qTime,
      username: storedAcc ? storedAcc.username : '',
      timestamp: r.timestamp,
      studentName: r.studentName,
      studentClass: r.studentClass || '',
      language: r.language || 'Tiếng Việt',"""

if old_sync_item in content:
    content = content.replace(old_sync_item, new_sync_item, 1)
    print("5. Updated syncAllHistoryToSheets() payload.")
else:
    print("WARNING: old_sync_item not found!")

# 6. UPDATE getLocalHistory() WITH DATA REPAIR & MIGRATION
old_get_local = """function getLocalHistory() {
  try {
    const raw = localStorage.getItem(HISTORY_STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch(e) {
    return [];
  }
}"""

new_get_local = """function getLocalHistory() {
  try {
    const raw = localStorage.getItem(HISTORY_STORAGE_KEY);
    let list = raw ? JSON.parse(raw) : [];
    let changed = false;
    list.forEach(r => {
      // Tự động phân tách Ngày, Giờ và Mã ID nếu chưa có
      if (r.timestamp && (!r.quizDate || !r.quizTime || !r.quizId)) {
        const parts = String(r.timestamp).split(' ');
        if (parts.length >= 2) {
          if (!r.quizTime) r.quizTime = parts[0];
          if (!r.quizDate) r.quizDate = parts[1];
        }
        if (!r.quizId) {
          const t = r.quizTime || (parts.length >= 2 ? parts[0] : '');
          r.quizId = 'QUIZ-' + t.replace(/[:]/g, '');
        }
        changed = true;
      }
      // Khắc phục các bản ghi lịch sử đặc biệt theo yêu cầu người dùng
      if (r.timestamp && r.timestamp.includes('10:50:06') && r.language !== 'Tiếng Anh') {
        r.language = 'Tiếng Anh';
        changed = true;
      }
      if (r.timestamp && r.timestamp.includes('11:00:20') && r.language !== 'Song ngữ Anh - Việt') {
        r.language = 'Song ngữ Anh - Việt';
        changed = true;
      }
    });
    if (changed) {
      localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(list));
    }
    return list;
  } catch(e) {
    return [];
  }
}"""

if old_get_local in content:
    content = content.replace(old_get_local, new_get_local, 1)
    print("6. Updated getLocalHistory() with auto-migration.")
else:
    print("WARNING: old_get_local not found!")

# 7. UPDATE HISTORY TABLE HTML HEADER
old_thead = """          <thead>
            <tr>
              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Ngôn Ngữ</th>
              <th>Loại Đề Thi</th>
              <th style="text-align:center;">Đúng / Tổng</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
              <th style="text-align:center;">Xem Lại Bài</th>
            </tr>
          </thead>"""

new_thead = """          <thead>
            <tr>
              <th style="white-space:nowrap;">Mã ID</th>
              <th style="white-space:nowrap;">Ngày Thi</th>
              <th style="white-space:nowrap;">Giờ Thi</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Ngôn Ngữ</th>
              <th>Loại Đề Thi</th>
              <th style="text-align:center;">Đúng / Tổng</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
              <th style="text-align:center;">Xem Lại</th>
            </tr>
          </thead>"""

if old_thead in content:
    content = content.replace(old_thead, new_thead, 1)
    print("7. Updated history table thead in HTML.")
else:
    print("WARNING: old_thead not found!")

# 8. UPDATE renderHistoryTable() ROWS AND COLSPAN
old_tbody_empty = 'tbody.innerHTML = `<tr><td colspan="8"'
new_tbody_empty = 'tbody.innerHTML = `<tr><td colspan="11"'
if old_tbody_empty in content:
    content = content.replace(old_tbody_empty, new_tbody_empty, 1)

old_tr_render = """    tr.innerHTML = `
      <td style="font-weight:600; color:#475569;">${r.timestamp}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td><span style="background:#F0FDF4; color:#15803D; border:1px solid #BBF7D0; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>
      <td style="text-align:center; font-weight:700;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center;"><span class="score-badge ${badgeClass}">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:600; color:#64748B;">⏱️ ${r.duration || '00:00'}</td>
      <td style="text-align:center;">
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-size:0.78rem; padding:4px 10px; font-weight:800;">
          🔍 Xem bài làm
        </button>
      </td>
    `;"""

new_tr_render = """    const parts = (r.timestamp || "").split(" ");
    const rowTime = r.quizTime || (parts.length >= 2 ? parts[0] : "");
    const rowDate = r.quizDate || (parts.length >= 2 ? parts[1] : r.timestamp || "");
    const rowId = r.quizId || r.id || (rowTime ? "QUIZ-" + rowTime.replace(/[:]/g, "") : "QUIZ");

    tr.innerHTML = `
      <td><span style="font-family:monospace; font-weight:700; color:var(--primary); font-size:0.75rem; background:#EEF2FF; padding:2px 6px; border-radius:4px;">${rowId}</span></td>
      <td style="font-weight:600; color:#334155; white-space:nowrap;">${rowDate}</td>
      <td style="font-weight:600; color:#64748B; white-space:nowrap;">${rowTime}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td><span style="background:${r.language === 'Tiếng Anh' ? '#F0F9FF' : (r.language === 'Song ngữ Anh - Việt' ? '#FAF5FF' : '#F0FDF4')}; color:${r.language === 'Tiếng Anh' ? '#0369A1' : (r.language === 'Song ngữ Anh - Việt' ? '#7E22CE' : '#15803D')}; border:1px solid ${r.language === 'Tiếng Anh' ? '#BAE6FD' : (r.language === 'Song ngữ Anh - Việt' ? '#E9D5FF' : '#BBF7D0')}; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>
      <td style="text-align:center; font-weight:700;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center;"><span class="score-badge ${badgeClass}">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:600; color:#64748B; white-space:nowrap;">⏱️ ${r.duration || '00:00'}</td>
      <td style="text-align:center;">
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-size:0.78rem; padding:4px 10px; font-weight:800; white-space:nowrap;">
          🔍 Xem lại
        </button>
      </td>
    `;"""

if old_tr_render in content:
    content = content.replace(old_tr_render, new_tr_render, 1)
    print("8. Updated renderHistoryTable() rows.")
else:
    print("WARNING: old_tr_render not found!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating index.html!")
