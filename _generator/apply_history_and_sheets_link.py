# -*- coding: utf-8 -*-
"""
Script cập nhật 3 yêu cầu:
1. Sửa filter ở bảng lịch sử: bỏ filter nguồn đề, thay bằng filter độ khó/độ tuổi và filter số lượng câu hỏi
2. Tính năng xem lại nhanh bài thi từ lịch sử (modal chi tiết từng câu kèm đáp án thí sinh chọn, đáp án đúng, giải thích)
3. Tích hợp link mở Google Sheets & Drive trên giao diện
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. CẬP NHẬT GIAO DIỆN BỘ LỌC VÀ NÚT DRIVE Ở HISTORY SCREEN
OLD_HISTORY_BAR = """      <div class="history-header-bar">
        <h2 style="font-size:1.35rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
          <span>📊</span>
          <span>Lịch Sử Bài Thi & Bảng Thống Kê</span>
        </h2>
        <div style="display:flex; gap:8px;">
          <button class="btn-source-action" onclick="showScreen('home-screen')" style="font-weight:700;">🏠 Về Trang Chủ</button>
          <button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>
        </div>
      </div>"""

NEW_HISTORY_BAR = """      <div class="history-header-bar">
        <h2 style="font-size:1.35rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
          <span>📊</span>
          <span>Lịch Sử Bài Thi & Bảng Thống Kê</span>
        </h2>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <a href="https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49" target="_blank" class="btn-source-action" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">📄 Mở Google Sheets (Drive) ↗</a>
          <button class="btn-source-action" onclick="showScreen('home-screen')" style="font-weight:700;">🏠 Về Trang Chủ</button>
          <button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>
        </div>
      </div>"""

if OLD_HISTORY_BAR in html:
    html = html.replace(OLD_HISTORY_BAR, NEW_HISTORY_BAR)

OLD_FILTER_BAR = """      <!-- THANH TÌM KIẾM & BỘ LỌC -->
      <div class="history-filter-bar">
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh, lớp, nguồn đề..." oninput="renderHistoryTable()">
        <select class="history-filter-select" id="history-filter-level" onchange="renderHistoryTable()">
          <option value="all">🌟 Tất cả mức điểm</option>
          <option value="high">🏆 Xuất sắc (≥ 9.0 điểm)</option>
          <option value="medium">👍 Khá tốt (6.5 - 8.9 điểm)</option>
          <option value="low">📖 Cần cố gắng (&lt; 6.5 điểm)</option>
        </select>
        <select class="history-filter-select" id="history-filter-src" onchange="renderHistoryTable()">
          <option value="all">📚 Tất cả nguồn đề</option>
          <option value="SGK">SGK Việt Nam</option>
          <option value="Trạng Nguyên">Trạng Nguyên & Violympic</option>
          <option value="Kangaroo">Kangaroo Khoa học</option>
          <option value="IXL">IXL & Khan</option>
          <option value="National">NatGeo Kids</option>
        </select>
      </div>"""

NEW_FILTER_BAR = """      <!-- THANH TÌM KIẾM & BỘ LỌC THEO SỐ CÂU, ĐỘ KHÓ, MỨC ĐIỂM -->
      <div class="history-filter-bar">
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh, lớp..." oninput="renderHistoryTable()">
        
        <!-- BỘ LỌC THEO SỐ LƯỢNG CÂU HỎI -->
        <select class="history-filter-select" id="history-filter-size" onchange="renderHistoryTable()">
          <option value="all">🔢 Tất cả số câu</option>
          <option value="5">5 câu (Khởi động)</option>
          <option value="10">10 câu (Nhanh)</option>
          <option value="15">15 câu (Chuẩn thi)</option>
          <option value="20">20 câu (Thử thách)</option>
          <option value="25">25 câu (Nâng cao)</option>
          <option value="30">30 câu (Học bổng)</option>
          <option value="50">50 câu (Đại hội)</option>
        </select>

        <!-- BỘ LỌC THEO ĐỘ KHÓ / ĐỘ TUỔI -->
        <select class="history-filter-select" id="history-filter-diff" onchange="renderHistoryTable()">
          <option value="all">🎚️ Tất cả độ khó</option>
          <option value="1">⭐ Mức 1: Dễ (6 - 7 tuổi)</option>
          <option value="2">⭐⭐ Mức 2: Vừa (7 - 8 tuổi)</option>
          <option value="3">⭐⭐⭐ Mức 3: Khó (8 - 9 tuổi)</option>
          <option value="mixed">🌟 Hỗn hợp đa cấp độ</option>
        </select>

        <!-- BỘ LỌC THEO MỨC ĐIỂM -->
        <select class="history-filter-select" id="history-filter-level" onchange="renderHistoryTable()">
          <option value="all">🎯 Tất cả mức điểm</option>
          <option value="high">🏆 Xuất sắc (≥ 9.0 điểm)</option>
          <option value="medium">👍 Khá tốt (6.5 - 8.9 điểm)</option>
          <option value="low">📖 Cần cố gắng (&lt; 6.5 điểm)</option>
        </select>
      </div>"""

if OLD_FILTER_BAR in html:
    html = html.replace(OLD_FILTER_BAR, NEW_FILTER_BAR)

# Thay đổi tiêu đề bảng lịch sử để có cột "Thao Tác" xem lại chi tiết
OLD_THEAD = """          <thead>
            <tr>
              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Nguồn Đề Thi</th>
              <th style="text-align:center;">Số Câu</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
            </tr>
          </thead>"""

NEW_THEAD = """          <thead>
            <tr>
              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Loại Đề Thi</th>
              <th style="text-align:center;">Đúng / Tổng</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
              <th style="text-align:center;">Xem Lại Bài</th>
            </tr>
          </thead>"""

if OLD_THEAD in html:
    html = html.replace(OLD_THEAD, NEW_THEAD)

# 2. THÊM MODAL XEM LẠI NHANH BÀI THI TỪ LỊCH SỬ
MODAL_HISTORY_DETAIL_HTML = """
<!-- MODAL XEM LẠI NHANH CHI TIẾT BÀI THI TỪ LỊCH SỬ -->
<div class="modal-overlay" id="modal-history-detail">
  <div class="modal-box" style="max-width: 720px; max-height: 88vh; display:flex; flex-direction:column; text-align:left; padding: 20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1.5px solid #E2E8F0; padding-bottom:12px;">
      <div>
        <div style="font-size:1.25rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
          <span>📋</span>
          <span id="hist-modal-title">Chi Tiết Bài Làm</span>
        </div>
        <div style="font-size:0.85rem; color:#64748B; margin-top:4px;" id="hist-modal-sub">
          Đang tải dữ liệu...
        </div>
      </div>
      <button onclick="closeHistoryDetailModal()" style="background:#F1F5F9; border:none; width:34px; height:34px; border-radius:50%; font-size:18px; font-weight:bold; cursor:pointer; color:#64748B;">✕</button>
    </div>

    <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:10px 14px; margin-bottom:12px; display:flex; gap:16px; flex-wrap:wrap; font-size:0.88rem;" id="hist-modal-summary">
      <!-- Thống kê nhanh: Điểm, Số câu đúng, Thời gian -->
    </div>

    <div style="overflow-y:auto; flex:1; padding-right:6px;" id="hist-modal-questions-list">
      <!-- Danh sách các câu hỏi hiển thị ở đây -->
    </div>

    <div style="margin-top:14px; text-align:right; border-top:1.5px solid #E2E8F0; padding-top:10px;">
      <button class="btn-source-action" onclick="closeHistoryDetailModal()" style="font-weight:700; padding:8px 22px;">Đóng</button>
    </div>
  </div>
</div>
"""

if 'id="modal-history-detail"' not in html:
    html = html.replace('<!-- MODAL QUICK REVIEW', MODAL_HISTORY_DETAIL_HTML + '\n<!-- MODAL QUICK REVIEW')

# 3. THÊM LINK GOOGLE SHEETS / DRIVE Ở START SCREEN VÀ RESULT SCREEN
OLD_APPS_CONFIG = """      <div class="config-row">
        <label>🌐 Google Apps Script URL (Lưu Sheets):</label>
        <input type="text" id="apps-script-url" placeholder="https://script.google.com/macros/s/...">
      </div>"""

NEW_APPS_CONFIG = """      <div class="config-row">
        <label>🌐 Google Apps Script URL (Lưu Sheets):</label>
        <input type="text" id="apps-script-url" placeholder="https://script.google.com/macros/s/...">
        <div style="font-size:0.8rem; margin-top:4px;">
          <a href="https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49" target="_blank" style="color:var(--primary); font-weight:700; text-decoration:none;">
            📂 Bấm vào đây để mở thư mục Google Drive chứa file Google Sheets kết quả ↗
          </a>
        </div>
      </div>"""

if OLD_APPS_CONFIG in html:
    html = html.replace(OLD_APPS_CONFIG, NEW_APPS_CONFIG)

OLD_RES_BUTTONS = """      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">🔄 Ôn lại câu sai</button>
        <button class="btn-secondary" onclick="openHistoryScreen()">📊 Xem Lịch Sử</button>
        <button class="btn-primary-action" onclick="backToHome()">🏠 Về Trang Chủ</button>
      </div>"""

NEW_RES_BUTTONS = """      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">🔄 Ôn lại câu sai</button>
        <button class="btn-secondary" onclick="openHistoryScreen()">📊 Xem Lịch Sử</button>
        <a href="https://drive.google.com/drive/u/0/folders/1CLlOjOjtK5Hohdqq-6hv9OBZZhaqmc49" target="_blank" class="btn-secondary" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#F0FDF4; color:#15803D; border-color:#86EFAC;">📄 Mở Google Sheets ↗</a>
        <button class="btn-primary-action" onclick="backToHome()">🏠 Về Trang Chủ</button>
      </div>"""

if OLD_RES_BUTTONS in html:
    html = html.replace(OLD_RES_BUTTONS, NEW_RES_BUTTONS)

# 4. CẬP NHẬT JAVASCRIPT: LƯU QUESTIONS DETAIL VÀ XỬ LÝ FILTER MỚI, MODAL XEM CHI TIẾT
OLD_SAVE_CALL = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (LOCALSTORAGE)
  saveQuizToLocalHistory({
    id: 'REC_' + Date.now(),
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    studentClass: document.getElementById('student-class') ? document.getElementById('student-class').value.trim() : '',
    sources: Array.from(selectedSources).join(', '),
    totalQuestions: total,
    correctCount: correctCount,
    wrongCount: wrongCount,
    score10: parseFloat(score10),
    pct: pct,
    duration: timeStr
  });"""

NEW_SAVE_CALL = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  saveQuizToLocalHistory({
    id: 'REC_' + Date.now(),
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    studentClass: document.getElementById('student-class') ? document.getElementById('student-class').value.trim() : '',
    sources: Array.from(selectedSources).join(', '),
    diffVal: selectedDiff,
    diffText: (selectedDiff === '1' ? 'Mức 1: Dễ (6-7t)' : (selectedDiff === '2' ? 'Mức 2: Vừa (7-8t)' : (selectedDiff === '3' ? 'Mức 3: Khó (8-9t)' : 'Hỗn hợp'))),
    ageVal: selectedAge,
    quizSize: total,
    totalQuestions: total,
    correctCount: correctCount,
    wrongCount: wrongCount,
    score10: parseFloat(score10),
    pct: pct,
    duration: timeStr,
    questionsDetail: sessionAnswers.map((item, idx) => ({
      index: idx + 1,
      id: item.question.id,
      topic: item.question.topic,
      diff: item.question.diff,
      age: item.question.age,
      qText: item.question.q,
      userAnswerKey: item.userAnswerKey,
      userAnswerText: item.userAnswerText,
      correctAnswerKey: item.question.ans,
      correctAnswerText: getCorrectAnswerText(item.question),
      isCorrect: item.isCorrect,
      explain: item.question.explain,
      source: item.question.source || ''
    }))
  });"""

if OLD_SAVE_CALL in html:
    html = html.replace(OLD_SAVE_CALL, NEW_SAVE_CALL)

# Cập nhật renderHistoryTable và các hàm modal chi tiết
NEW_HISTORY_FUNCTIONS = """
function renderHistoryTable() {
  const historyList = getLocalHistory();
  const searchInput = document.getElementById('history-search');
  const filterSize = document.getElementById('history-filter-size');
  const filterDiff = document.getElementById('history-filter-diff');
  const filterLevel = document.getElementById('history-filter-level');

  const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
  const sizeVal = filterSize ? filterSize.value : 'all';
  const diffVal = filterDiff ? filterDiff.value : 'all';
  const levelVal = filterLevel ? filterLevel.value : 'all';

  // 1. Cập nhật Dashboard tổng quan
  const totalTests = historyList.length;
  document.getElementById('hist-total-tests').textContent = totalTests;

  if (totalTests > 0) {
    const sumScore = historyList.reduce((acc, r) => acc + (r.score10 || 0), 0);
    const avgScore = (sumScore / totalTests).toFixed(1);
    const sumPct = historyList.reduce((acc, r) => acc + (r.pct || 0), 0);
    const avgPct = Math.round(sumPct / totalTests);
    const maxScore = Math.max(...historyList.map(r => r.score10 || 0)).toFixed(1);

    document.getElementById('hist-avg-score').textContent = `${avgScore}/10`;
    document.getElementById('hist-avg-accuracy').textContent = `${avgPct}%`;
    document.getElementById('hist-highest-score').textContent = `${maxScore}/10`;
  } else {
    document.getElementById('hist-avg-score').textContent = '0.0';
    document.getElementById('hist-avg-accuracy').textContent = '0%';
    document.getElementById('hist-highest-score').textContent = '0.0';
  }

  // 2. Lọc danh sách theo Search, Số câu, Độ khó và Điểm số
  let filtered = historyList.filter(r => {
    // Search text (Tên bé, Lớp)
    if (searchTerm) {
      const matchName = (r.studentName || '').toLowerCase().includes(searchTerm);
      const matchClass = (r.studentClass || '').toLowerCase().includes(searchTerm);
      if (!matchName && !matchClass) return false;
    }

    // Filter theo số lượng câu hỏi
    if (sizeVal !== 'all') {
      const targetSize = parseInt(sizeVal);
      if (r.totalQuestions !== targetSize) return false;
    }

    // Filter theo độ khó / độ tuổi
    if (diffVal !== 'all') {
      if (diffVal === 'mixed') {
        if (r.diffVal && r.diffVal !== 'all') return false;
      } else {
        if (String(r.diffVal) !== diffVal) return false;
      }
    }

    // Filter theo mức điểm
    if (levelVal === 'high' && r.score10 < 9.0) return false;
    if (levelVal === 'medium' && (r.score10 < 6.5 || r.score10 >= 9.0)) return false;
    if (levelVal === 'low' && r.score10 >= 6.5) return false;

    return true;
  });

  // 3. Render bảng HTML
  const tbody = document.getElementById('history-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:24px; color:#64748B;">
      ${totalTests === 0 ? 'Chưa có lượt thi nào được ghi lại. Hãy bắt đầu một bài thi đầu tiên nhé!' : 'Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.'}
    </td></tr>`;
    return;
  }

  filtered.forEach((r, idx) => {
    const tr = document.createElement('tr');
    
    let badgeClass = 'medium';
    if (r.score10 >= 8.5) badgeClass = 'high';
    else if (r.score10 < 6.5) badgeClass = 'low';

    const diffDisplay = r.diffText || (r.diffVal === '1' ? 'Mức 1: Dễ' : (r.diffVal === '2' ? 'Mức 2: Vừa' : (r.diffVal === '3' ? 'Mức 3: Khó' : 'Hỗn hợp')));

    tr.innerHTML = `
      <td style="font-weight:600; color:#475569;">${r.timestamp}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
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
    `;
    tbody.appendChild(tr);
  });
}

function viewHistoryDetail(recordId) {
  const historyList = getLocalHistory();
  const record = historyList.find(r => r.id === recordId);
  if (!record) return;

  const modal = document.getElementById('modal-history-detail');
  const titleElem = document.getElementById('hist-modal-title');
  const subElem = document.getElementById('hist-modal-sub');
  const sumElem = document.getElementById('hist-modal-summary');
  const listElem = document.getElementById('hist-modal-questions-list');

  titleElem.textContent = `Chi Tiết Bài Thi: ${record.studentName} (${record.studentClass || 'Chưa rõ lớp'})`;
  subElem.textContent = `Thời gian nộp: ${record.timestamp} • Đề thi: ${record.totalQuestions} câu (${record.diffText || 'Hỗn hợp'})`;

  sumElem.innerHTML = `
    <div><strong>🎯 Điểm số:</strong> <span style="color:var(--primary); font-weight:800;">${record.score10}/10 (${record.pct}%)</span></div>
    <div><strong>✅ Đúng:</strong> <span style="color:#15803D; font-weight:800;">${record.correctCount} câu</span></div>
    <div><strong>❌ Sai:</strong> <span style="color:#EF4444; font-weight:800;">${record.wrongCount} câu</span></div>
    <div><strong>⏱️ Thời gian:</strong> <span style="font-weight:700;">${record.duration}</span></div>
  `;

  listElem.innerHTML = '';
  const details = record.questionsDetail || [];

  if (details.length === 0) {
    listElem.innerHTML = `<div style="text-align:center; padding:20px; color:#64748B;">
      Lượt thi này được làm từ phiên bản trước nên chưa lưu chi tiết từng câu. Các lượt thi mới sẽ hiển thị đầy đủ 100%!
    </div>`;
  } else {
    details.forEach(item => {
      const card = document.createElement('div');
      card.className = `review-item-card ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;
      card.style.marginBottom = '12px';

      card.innerHTML = `
        <div class="review-card-header">
          <span>Câu ${item.index} (${item.topic} - Mức ${item.diff}) ${item.source ? `<span style="font-size:0.75rem; background:#F1F5F9; color:#475569; padding:2px 6px; border-radius:6px; margin-left:6px;">${item.source}</span>` : ''}</span>
          <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:800;">
            ${item.isCorrect ? '✅ Đúng' : '❌ Chưa đúng'}
          </span>
        </div>
        <div class="review-q-text">${item.qText}</div>
        <div class="review-answers-box">
          <div><strong>Bé đã chọn:</strong> <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">${item.userAnswerText}</span></div>
          ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>Đáp án đúng:</strong> <span style="color:var(--success); font-weight:700;">${item.correctAnswerText}</span></div>` : ''}
        </div>
        <div class="review-explain-box">
          <strong>💡 Giải thích:</strong> ${item.explain || 'Không có giải thích chi tiết.'}
        </div>
      `;
      listElem.appendChild(card);
    });
  }

  modal.classList.add('active');
}

function closeHistoryDetailModal() {
  const modal = document.getElementById('modal-history-detail');
  if (modal) modal.classList.remove('active');
}
"""

pattern_old_history = r'function renderHistoryTable\(\)\s*\{[\s\S]*?function clearHistoryData\(\)\s*\{[\s\S]*?\}'
match_h = re.search(pattern_old_history, html)
if match_h:
    html = html[:match_h.start()] + NEW_HISTORY_FUNCTIONS.strip() + '\n\nfunction clearHistoryData() {\n  if (confirm("Bé hoặc phụ huynh có chắc chắn muốn xóa toàn bộ lịch sử các lượt thi không?")) {\n    localStorage.removeItem(HISTORY_STORAGE_KEY);\n    renderHistoryTable();\n  }\n}' + html[match_h.end():]
    print("✅ Đã cập nhật xong renderHistoryTable, viewHistoryDetail và Modal!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã hoàn tất cập nhật vào index.html!")
