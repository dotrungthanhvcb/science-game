#!/usr/bin/env python3
HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update saveQuizToLocalHistory in submitAndFinishQuiz to include recordId and pass it to sendDataToAppsScript
old_submit_save = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  saveQuizToLocalHistory({
    id: 'REC_' + Date.now(),
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',"""

new_submit_save = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  const currentRecordId = 'REC_' + Date.now();
  saveQuizToLocalHistory({
    id: currentRecordId,
    syncedToSheets: false,
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',"""

assert old_submit_save in html, "old_submit_save not found"
html = html.replace(old_submit_save, new_submit_save)

# 2. Update sendDataToAppsScript call in submitAndFinishQuiz
old_send_call = """  // 5. TỰ ĐỘNG GỬI KẾT QUẢ VỀ GOOGLE SHEETS
  sendDataToAppsScript(total, correctCount, wrongCount, `${score10}/10 (${pct}%)`, timeStr);"""

new_send_call = """  // 5. TỰ ĐỘNG GỬI KẾT QUẢ VỀ GOOGLE SHEETS
  sendDataToAppsScript(total, correctCount, wrongCount, `${score10}/10 (${pct}%)`, timeStr, currentRecordId);"""

assert old_send_call in html, "old_send_call not found"
html = html.replace(old_send_call, new_send_call)

# 3. Update sendDataToAppsScript definition to accept recordId and mark synced
old_send_def = """function sendDataToAppsScript(total, correct, wrong, scoreStr, durationStr) {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  const statusElem = document.getElementById('sync-status');
  if (!statusElem) return;

  if (!scriptUrl) {
    statusElem.innerHTML = `⚠️ <strong>Kết quả đã lưu an toàn trong máy.</strong> <button onclick="promptForScriptUrl()" style="margin-left:8px; padding:4px 12px; border-radius:8px; background:var(--primary); color:white; border:none; font-weight:700; cursor:pointer;">🔗 Kết nối Google Sheets để lưu lên bảng tính</button>`;
    return;
  }

  statusElem.innerHTML = '⏳ <span style="color:var(--primary); font-weight:700;">Đang tự động lưu kết quả vào Google Sheets...</span>';

  const payload = {
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name') ? document.getElementById('user-name').value.trim() : 'Học sinh',
    studentClass: (function() {
      const elem = document.getElementById('student-class');
      if (!elem) return 'Lớp 2';
      const val = elem.value;
      if (val === 'all') return 'Lớp 1 - 5 (Hỗn hợp)';
      return 'Lớp ' + val;
    })(),
    sources: Array.from(selectedSources).join(', '),
    totalQuestions: total,
    correctCount: correct,
    wrongCount: wrong,
    score: scoreStr,
    duration: durationStr
  };

  fetch(scriptUrl, {
    method: 'POST',
    mode: 'no-cors',
    headers: { 'Content-Type': 'text/plain;charset=utf-8' },
    body: JSON.stringify(payload)
  })
  .then(() => {
    statusElem.innerHTML = `✅ <span style="color:#15803D; font-weight:700;">Đã lưu kết quả thành công vào file Google Sheets!</span> <a href="${DIRECT_GOOGLE_SHEET_URL}" target="_blank" onclick="openGoogleSheetsDirectly(event)" style="margin-left:8px; color:var(--primary); font-weight:700;">[Xem bảng tính ↗]</a>`;
  })"""

new_send_def = """function markRecordAsSynced(recordId) {
  if (!recordId) return;
  const list = getLocalHistory();
  const item = list.find(r => r.id === recordId);
  if (item) {
    item.syncedToSheets = true;
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(list));
  }
}

function sendDataToAppsScript(total, correct, wrong, scoreStr, durationStr, recordId) {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  const statusElem = document.getElementById('sync-status');
  if (!statusElem) return;

  if (!scriptUrl) {
    statusElem.innerHTML = `⚠️ <strong>Kết quả đã lưu an toàn trong máy.</strong> <button onclick="promptForScriptUrl()" style="margin-left:8px; padding:4px 12px; border-radius:8px; background:var(--primary); color:white; border:none; font-weight:700; cursor:pointer;">🔗 Kết nối Google Sheets để lưu lên bảng tính</button>`;
    return;
  }

  statusElem.innerHTML = '⏳ <span style="color:var(--primary); font-weight:700;">Đang tự động lưu kết quả vào Google Sheets...</span>';

  const payload = {
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name') ? document.getElementById('user-name').value.trim() : 'Học sinh',
    studentClass: (function() {
      const elem = document.getElementById('student-class');
      if (!elem) return 'Lớp 2';
      const val = elem.value;
      if (val === 'all') return 'Lớp 1 - 5 (Hỗn hợp)';
      return 'Lớp ' + val;
    })(),
    sources: Array.from(selectedSources).join(', '),
    totalQuestions: total,
    correctCount: correct,
    wrongCount: wrong,
    score: scoreStr,
    duration: durationStr
  };

  fetch(scriptUrl, {
    method: 'POST',
    mode: 'no-cors',
    headers: { 'Content-Type': 'text/plain;charset=utf-8' },
    body: JSON.stringify(payload)
  })
  .then(() => {
    markRecordAsSynced(recordId);
    statusElem.innerHTML = `✅ <span style="color:#15803D; font-weight:700;">Đã lưu kết quả thành công vào file Google Sheets!</span> <a href="${DIRECT_GOOGLE_SHEET_URL}" target="_blank" onclick="openGoogleSheetsDirectly(event)" style="margin-left:8px; color:var(--primary); font-weight:700;">[Xem bảng tính ↗]</a>`;
  })"""

assert old_send_def in html, "old_send_def not found"
html = html.replace(old_send_def, new_send_def)

# 4. Update syncAllHistoryToSheets to ONLY send unsynced items
old_sync_all = """function syncAllHistoryToSheets() {
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

  if (!confirm(`Bạn có muốn gửi toàn bộ ${historyList.length} lượt thi trong lịch sử lên file Google Sheets không?`)) {
    return;
  }

  let sent = 0;
  // Gửi tuần tự các lượt thi
  historyList.forEach((r, idx) => {
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

      sent++;
      if (sent === historyList.length) {
        alert(`✅ Đã gửi thành công ${sent} bài thi lên Google Sheets! Bạn hãy mở file Sheets để xem nhé.`);
      }
    }, idx * 400);
  });
}"""

new_sync_all = """function syncAllHistoryToSheets() {
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

assert old_sync_all in html, "old_sync_all not found"
html = html.replace(old_sync_all, new_sync_all)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied deduplication to index.html successfully!")
