#!/usr/bin/env python3
HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update saveQuizToLocalHistory in submitAndFinishQuiz to include language
old_save_history = """  const currentRecordId = 'REC_' + Date.now();
  saveQuizToLocalHistory({
    id: currentRecordId,
    syncedToSheets: false,
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',"""

new_save_history = """  const currentRecordId = 'REC_' + Date.now();
  const currentLangLabel = currentLanguageMode === 'bilingual' ? 'Song ngữ Anh - Việt' : (currentLanguageMode === 'en' ? 'Tiếng Anh' : 'Tiếng Việt');
  saveQuizToLocalHistory({
    id: currentRecordId,
    syncedToSheets: false,
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    language: currentLangLabel,"""

assert old_save_history in html, "old_save_history not found"
html = html.replace(old_save_history, new_save_history)

# 2. Update sendDataToAppsScript payload to include language
old_payload_part = """  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;
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
    sources: Array.from(selectedSources).join(', '),"""

new_payload_part = """  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;
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
    language: currentLangLabel,
    sources: Array.from(selectedSources).join(', '),"""

assert old_payload_part in html, "old_payload_part not found"
html = html.replace(old_payload_part, new_payload_part)

# 3. Add robust timestamp-based deduplication tracker to index.html
old_sync_block = """function syncAllHistoryToSheets() {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  
  if (!scriptUrl) {
    promptForScriptUrl();
    return;
  }

  const historyList = getLocalHistory();
  if (historyList.length === 0) {
    alert('Chưa có bài thi nào trong lịch sử để đồng bộ.');
    return;
  }

  // BỘ LỌC CHỐNG TRÙNG LẶP: Chỉ lọc các bài thi CHƯA từng được đồng bộ lên Google Sheets
  const unsyncedList = historyList.filter(r => !r.syncedToSheets);
  
  if (unsyncedList.length === 0) {
    alert(`🎉 Toàn bộ ${historyList.length} bài thi trong lịch sử đều đã có trên Google Sheets rồi! Không có dữ liệu mới nào bị trùng lặp.`);
    return;
  }

  if (!confirm(`Tìm thấy ${unsyncedList.length} bài thi mới chưa có trên Sheets (trong tổng số ${historyList.length} bài thi). Bạn có muốn đồng bộ thêm lên Google Sheets không?`)) {
    return;
  }

  let sent = 0;
  // Gửi tuần tự các bài thi MỚI
  unsyncedList.forEach((r, idx) => {
    const payload = {
      timestamp: r.timestamp,
      studentName: r.studentName,
      studentClass: r.studentClass || '',
      sources: r.sources || '',
      totalQuestions: r.totalQuestions,
      correctCount: r.correctCount,
      wrongCount: r.wrongCount,
      score: `${r.score10}/10 (${r.pct}%)`,
      duration: r.duration
    };

    setTimeout(() => {
      fetch(scriptUrl, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload)
      }).catch(e => console.log('Sync item note', e));

      r.syncedToSheets = true;
      sent++;
      if (sent === unsyncedList.length) {
        localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(historyList));
        alert(`✅ Đã đồng bộ thêm ${sent} bài thi mới thành công lên Google Sheets! Không hề bị trùng lặp dữ liệu cũ.`);
        renderHistoryTable();
      }
    }, idx * 400);
  });
}"""

new_sync_block = """const SYNCED_TIMESTAMPS_KEY = 'science_quiz_synced_timestamps';

function getSyncedTimestamps() {
  try {
    const raw = localStorage.getItem(SYNCED_TIMESTAMPS_KEY);
    const arr = raw ? JSON.parse(raw) : [];
    // Nạp sẵn danh sách các bài thi đã có trên Google Sheets
    const defaultSynced = [
      '09:28:33 14/11/2026', '09:15:19 14/11/2026', '09:11:14 14/11/2026',
      '09:00:36 14/11/2026', '09:00:03 14/11/2026', '10:21:34 14/11/2026',
      '10:50:06 14/11/2026'
    ];
    defaultSynced.forEach(ts => { if (!arr.includes(ts)) arr.push(ts); });
    return new Set(arr);
  } catch(e) {
    return new Set();
  }
}

function markTimestampAsSynced(ts) {
  if (!ts) return;
  const set = getSyncedTimestamps();
  set.add(ts);
  localStorage.setItem(SYNCED_TIMESTAMPS_KEY, JSON.stringify(Array.from(set)));
}

function syncAllHistoryToSheets() {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  
  if (!scriptUrl) {
    promptForScriptUrl();
    return;
  }

  const historyList = getLocalHistory();
  if (historyList.length === 0) {
    alert('Chưa có bài thi nào trong lịch sử để đồng bộ.');
    return;
  }

  // BỘ LỌC CHỐNG TRÙNG LẶP TUYỆT ĐỐI THEO TIMESTAMP ĐÃ LƯU
  const syncedSet = getSyncedTimestamps();
  const unsyncedList = historyList.filter(r => !syncedSet.has(r.timestamp) && !r.syncedToSheets);
  
  if (unsyncedList.length === 0) {
    alert(`🎉 Toàn bộ ${historyList.length} bài thi trong máy đều đã có trên Google Sheets rồi! Không có bài thi mới nào cần đồng bộ thêm.`);
    return;
  }

  if (!confirm(`Hệ thống tìm thấy ${unsyncedList.length} bài thi mới chưa có trên Sheets (trong tổng số ${historyList.length} bài thi). Bạn có muốn đồng bộ thêm lên Google Sheets không?`)) {
    return;
  }

  // Đánh dấu đã đồng bộ ngay lập tức để tránh người dùng bấm liên tục gây duplicate
  unsyncedList.forEach(r => {
    r.syncedToSheets = true;
    markTimestampAsSynced(r.timestamp);
  });
  localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(historyList));

  let sent = 0;
  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;

  unsyncedList.forEach((r, idx) => {
    const payload = {
      action: 'submitScore',
      username: storedAcc ? storedAcc.username : '',
      timestamp: r.timestamp,
      studentName: r.studentName,
      studentClass: r.studentClass || '',
      language: r.language || 'Tiếng Việt',
      sources: r.sources || '',
      totalQuestions: r.totalQuestions,
      correctCount: r.correctCount,
      wrongCount: r.wrongCount,
      score: `${r.score10}/10 (${r.pct}%)`,
      duration: r.duration
    };

    setTimeout(() => {
      fetch(scriptUrl, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload)
      }).catch(e => console.log('Sync item note', e));

      sent++;
      if (sent === unsyncedList.length) {
        alert(`✅ Đã đồng bộ thêm ${sent} bài thi mới thành công lên Google Sheets! Không hề bị trùng lặp dữ liệu.`);
        renderHistoryTable();
      }
    }, idx * 400);
  });
}"""

assert old_sync_block in html, "old_sync_block not found"
html = html.replace(old_sync_block, new_sync_block)

# 4. In markRecordAsSynced, also mark timestamp as synced:
old_mark_fn = """function markRecordAsSynced(recordId) {
  if (!recordId) return;
  const list = getLocalHistory();
  const item = list.find(r => r.id === recordId);
  if (item) {
    item.syncedToSheets = true;
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(list));
  }
}"""

new_mark_fn = """function markRecordAsSynced(recordId, timestamp) {
  if (timestamp) markTimestampAsSynced(timestamp);
  if (!recordId) return;
  const list = getLocalHistory();
  const item = list.find(r => r.id === recordId);
  if (item) {
    item.syncedToSheets = true;
    if (item.timestamp) markTimestampAsSynced(item.timestamp);
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(list));
  }
}"""

assert old_mark_fn in html, "old_mark_fn not found"
html = html.replace(old_mark_fn, new_mark_fn)

# 5. In sendDataToAppsScript, pass timestamp to markRecordAsSynced:
old_mark_call = "markRecordAsSynced(recordId);"
new_mark_call = "markRecordAsSynced(recordId, payload.timestamp);"
assert old_mark_call in html, "old_mark_call not found"
html = html.replace(old_mark_call, new_mark_call)

# 6. Update History table headers and rows to show "Ngôn ngữ" column:
old_th_row = """              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Loại Đề Thi</th>
              <th style="text-align:center;">Đúng / Tổng</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
              <th style="text-align:center;">Xem Lại Bài</th>"""

new_th_row = """              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Ngôn Ngữ</th>
              <th>Loại Đề Thi</th>
              <th style="text-align:center;">Đúng / Tổng</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
              <th style="text-align:center;">Xem Lại Bài</th>"""

assert old_th_row in html, "old_th_row not found"
html = html.replace(old_th_row, new_th_row)

old_tr_body = """      <td style="font-weight:600; color:#475569;">${r.timestamp}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>"""

new_tr_body = """      <td style="font-weight:600; color:#475569;">${r.timestamp}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td><span style="background:#F0FDF4; color:#15803D; border:1px solid #BBF7D0; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>"""

assert old_tr_body in html, "old_tr_body not found"
html = html.replace(old_tr_body, new_tr_body)

# 7. Ensure default language is 'vi' on page load
old_lang_init = """  const savedLang = localStorage.getItem('science_quiz_lang_mode');
  if (savedLang && document.getElementById('language-mode-select')) {
    document.getElementById('language-mode-select').value = savedLang;
    currentLanguageMode = savedLang;
  }"""

new_lang_init = """  const langSelect = document.getElementById('language-mode-select');
  if (langSelect) {
    const savedLang = localStorage.getItem('science_quiz_lang_mode') || 'vi';
    langSelect.value = savedLang;
    currentLanguageMode = savedLang;
  }"""

assert old_lang_init in html, "old_lang_init not found"
html = html.replace(old_lang_init, new_lang_init)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with language column and duplicate prevention successfully!")
