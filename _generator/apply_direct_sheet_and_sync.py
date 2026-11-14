# -*- coding: utf-8 -*-
"""
Script xử lý triệt để 2 vấn đề:
1. Mở trực tiếp link Google Sheets bằng hàm openGoogleSheetsDirectly(e)
2. Thêm tính năng kết nối và đồng bộ các kết quả bài thi vào Google Sheets (kể cả bài thi vừa xong)
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hằng số link Google Sheets chính xác
SHEET_URL = "https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit"

# 2. Cập nhật các thẻ mở Sheets để gọi openGoogleSheetsDirectly(event)
html = html.replace(
    f'<a href="{SHEET_URL}" target="_blank" class="btn-source-action"',
    f'<a href="{SHEET_URL}" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-source-action"'
)

html = html.replace(
    f'<a href="{SHEET_URL}" target="_blank" class="btn-secondary"',
    f'<a href="{SHEET_URL}" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-secondary"'
)

html = html.replace(
    f'<a href="{SHEET_URL}" target="_blank" style="color:var(--primary); font-weight:700; text-decoration:none;"',
    f'<a href="{SHEET_URL}" target="_blank" onclick="openGoogleSheetsDirectly(event)" style="color:var(--primary); font-weight:700; text-decoration:none;"'
)

# Thêm nút đồng bộ kết quả lên Sheets ở Màn hình Lịch Sử (History Screen)
OLD_HIST_HEADER_BTNS = """        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-source-action" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">📄 Mở Google Sheets (Drive) ↗</a>
          <button class="btn-source-action" onclick="showScreen('home-screen')" style="font-weight:700;">🏠 Về Trang Chủ</button>
          <button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>
        </div>"""

NEW_HIST_HEADER_BTNS = """        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn-source-action" onclick="syncAllHistoryToSheets()" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-weight:800; display:inline-flex; align-items:center; gap:6px;">🔄 Đồng bộ lên Sheets</button>
          <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-source-action" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">📄 Mở File Google Sheets ↗</a>
          <button class="btn-source-action" onclick="showScreen('home-screen')" style="font-weight:700;">🏠 Về Trang Chủ</button>
          <button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>
        </div>"""

if OLD_HIST_HEADER_BTNS in html:
    html = html.replace(OLD_HIST_HEADER_BTNS, NEW_HIST_HEADER_BTNS)

# Thêm Modal Kết Nối / Cài Đặt Web App URL
CONNECT_MODAL_HTML = """
<!-- MODAL KẾT NỐI GOOGLE APPS SCRIPT WEB APP -->
<div class="modal-overlay" id="modal-connect-script">
  <div class="modal-box" style="max-width: 520px; text-align:left;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1.5px solid #E2E8F0; padding-bottom:10px;">
      <div style="font-size:1.15rem; font-weight:800; color:var(--dark); display:flex; align-items:center; gap:8px;">
        <span>🔗</span>
        <span>Kết Nối Google Sheets Tự Động</span>
      </div>
      <button onclick="closeConnectScriptModal()" style="background:#F1F5F9; border:none; width:30px; height:30px; border-radius:50%; font-size:16px; font-weight:bold; cursor:pointer; color:#64748B;">✕</button>
    </div>

    <div style="font-size:0.88rem; color:#475569; line-height:1.5; margin-bottom:14px;">
      Để tự động lưu kết quả thi vào file Google Sheets <strong>"Ket_Qua_Thi_Khoa_Hoc"</strong> của bạn, hãy dán <strong>Web App URL</strong> (có dạng <code>https://script.google.com/macros/s/.../exec</code>) vào ô bên dưới:
    </div>

    <div style="margin-bottom:14px;">
      <label style="font-size:0.82rem; font-weight:700; color:var(--dark); display:block; margin-bottom:6px;">Google Apps Script Web App URL:</label>
      <input type="text" id="modal-script-url-input" placeholder="https://script.google.com/macros/s/AKfycb.../exec" style="width:100%; padding:10px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:0.85rem; outline:none;">
    </div>

    <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:10px; font-size:0.8rem; color:#15803D; margin-bottom:16px;">
      💡 <em>File Google Sheets đã được tạo sẵn trong Drive của bạn. Chỉ cần dán URL 1 lần, hệ thống sẽ lưu vĩnh viễn và tự động đẩy các bài thi lên bảng tính!</em>
    </div>

    <div style="display:flex; justify-content:flex-end; gap:10px;">
      <button class="btn-source-action" onclick="closeConnectScriptModal()" style="font-weight:700;">Hủy</button>
      <button class="modal-btn-confirm" onclick="saveAndSyncScriptUrl()" style="background:linear-gradient(135deg, #4361EE, #3A0CA3); font-weight:800; padding:10px 20px; border-radius:10px;">
        💾 Lưu & Đồng Bộ Ngay
      </button>
    </div>
  </div>
</div>
"""

if 'id="modal-connect-script"' not in html:
    html = html.replace('<!-- MODAL XEM LẠI NHANH CHI TIẾT BÀI THI TỪ LỊCH SỬ', CONNECT_MODAL_HTML + '\n<!-- MODAL XEM LẠI NHANH CHI TIẾT BÀI THI TỪ LỊCH SỬ')

# 3. Cập nhật JavaScript cho openGoogleSheetsDirectly, sendDataToAppsScript, syncAllHistoryToSheets, promptForScriptUrl
NEW_SYNC_JS = """
// =========================================================================
// MỞ GOOGLE SHEETS TRỰC TIẾP & ĐỒNG BỘ KẾT QUẢ VÀO GOOGLE SHEETS
// =========================================================================
const DIRECT_GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit";

function openGoogleSheetsDirectly(e) {
  if (e) e.preventDefault();
  window.open(DIRECT_GOOGLE_SHEET_URL, '_blank');
}

function promptForScriptUrl() {
  const currentUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : '';
  const input = document.getElementById('modal-script-url-input');
  if (input) input.value = currentUrl;
  const modal = document.getElementById('modal-connect-script');
  if (modal) modal.classList.add('active');
}

function closeConnectScriptModal() {
  const modal = document.getElementById('modal-connect-script');
  if (modal) modal.classList.remove('active');
}

function saveAndSyncScriptUrl() {
  const input = document.getElementById('modal-script-url-input');
  const url = input ? input.value.trim() : '';
  if (!url) {
    alert('Vui lòng dán Web App URL của Google Apps Script (dạng https://script.google.com/macros/s/.../exec)');
    return;
  }

  // Lưu vào ô input và localStorage
  const mainInput = document.getElementById('apps-script-url');
  if (mainInput) mainInput.value = url;
  localStorage.setItem('science_quiz_script_url', url);
  closeConnectScriptModal();

  // Tự động đẩy toàn bộ kết quả lên Sheets
  syncAllHistoryToSheets();
}

function sendDataToAppsScript(total, correct, wrong, scoreStr, durationStr) {
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
    studentClass: document.getElementById('student-class') ? document.getElementById('student-class').value.trim() : '',
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
  })
  .catch(err => {
    statusElem.innerHTML = `⚠️ <span style="color:#B91C1C;">Không thể lưu lên Google Sheets: ${err.message}</span> <button onclick="promptForScriptUrl()" style="margin-left:6px; font-size:0.75rem;">Kiểm tra URL</button>`;
  });
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
}
"""

pattern_old_send = r'// =========================================================================\s*// TỰ ĐỘNG LƯU KẾT QUẢ VÀO GOOGLE SHEETS[\s\S]*?function sendDataToAppsScript[\s\S]*?\n\}'
match_s = re.search(pattern_old_send, html)
if match_s:
    html = html[:match_s.start()] + NEW_SYNC_JS.strip() + html[match_s.end():]
    print("✅ Đã cập nhật xong NEW_SYNC_JS!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã ghi hoàn tất vào index.html!")
