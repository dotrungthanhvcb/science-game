# -*- coding: utf-8 -*-
"""
Script cập nhật logic JS trong index.html:
- Quản lý Master Pool hợp nhất (questions_500.js + questions.json + ALL_QUESTIONS)
- Bộ lọc Multi-select nguồn (5 nguồn chuẩn + 'Khác')
- Chọn tất cả / Bỏ chọn tất cả
- Tự động đếm và hiển thị số lượng câu hỏi khả dụng
- Vô hiệu hóa nút Bắt đầu khi bỏ chọn hết nguồn + thông báo cảnh báo
- Hiển thị badge nguồn trên câu hỏi trong bài thi
"""
import re

INDEX_HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Đoạn mã JS mới thay thế và bổ sung cho Master Pool & Bộ lọc Nguồn
JS_SOURCE_ENGINE = """
// =========================================================================
// HỆ THỐNG QUẢN LÝ MASTER POOL & 5 NGUỒN HỌC LIỆU CHUẨN + KHÁC
// =========================================================================
const SOURCE_CONFIG = [
  { id: "SGK Việt Nam (GDPT 2018)", name: "SGK Việt Nam (GDPT 2018)", icon: "📗", desc: "Môn TN&XH & Khoa học (Lớp 1-5)", defaultSelected: true },
  { id: "Trạng Nguyên & Violympic", name: "Trạng Nguyên & Violympic", icon: "🏆", desc: "Câu ngắn gọn, phản xạ tư duy nhanh", defaultSelected: true },
  { id: "Kangaroo Khoa học (IKSC)", name: "Kangaroo Khoa học (IKSC)", icon: "🦘", desc: "Tư duy quan sát, logic thực tế", defaultSelected: true },
  { id: "IXL & Khan Academy", name: "IXL & Khan Academy", icon: "🌐", desc: "Phân loại khoa học chuẩn quốc tế", defaultSelected: true },
  { id: "National Geographic Kids", name: "National Geographic Kids", icon: "🦁", desc: "Fun facts, thiên nhiên kỳ thú & vũ trụ", defaultSelected: true },
  { id: "Khác", name: "Khác (Kho câu hỏi cũ)", icon: "📦", desc: "Ngân hàng câu hỏi trước đây", defaultSelected: false }
];

let selectedSources = new Set([
  "SGK Việt Nam (GDPT 2018)",
  "Trạng Nguyên & Violympic",
  "Kangaroo Khoa học (IKSC)",
  "IXL & Khan Academy",
  "National Geographic Kids"
]);

let MASTER_POOL = [];

function getSourceIcon(sourceName) {
  if (!sourceName) return '💡';
  if (sourceName.includes('SGK')) return '📗';
  if (sourceName.includes('Trạng Nguyên') || sourceName.includes('Violympic')) return '🏆';
  if (sourceName.includes('Kangaroo') || sourceName.includes('IKSC')) return '🦘';
  if (sourceName.includes('IXL') || sourceName.includes('Khan')) return '🌐';
  if (sourceName.includes('National') || sourceName.includes('Geographic')) return '🦁';
  return '📦';
}

function normalizeQuestion(q, defaultSource) {
  const text = q.question || q.q || "";
  let opts = q.options;
  if (!opts || opts.length < 4) {
    opts = [q.a || "", q.b || "", q.c || "", q.d || ""];
  }
  let cIdx = q.correctIndex;
  if (cIdx === undefined || cIdx === null) {
    const letter = (q.ans || "A").trim().toUpperCase();
    cIdx = letter === 'B' ? 1 : (letter === 'C' ? 2 : (letter === 'D' ? 3 : 0));
  }
  const ansLetter = ['A', 'B', 'C', 'D'][cIdx];
  const sourceName = q.source || defaultSource || "Khác";
  
  let age = q.age || "7-8";
  if (q.grade) {
    age = q.grade <= 2 ? "6-7" : (q.grade <= 3 ? "7-8" : "8-9");
  }
  
  let diffNum = q.diff || (q.difficulty === 'easy' ? 1 : (q.difficulty === 'medium' ? 2 : 3));

  return {
    id: q.id,
    q: text,
    question: text,
    options: opts,
    a: opts[0],
    b: opts[1],
    c: opts[2],
    d: opts[3],
    correctIndex: cIdx,
    ans: ansLetter,
    source: sourceName,
    topic: q.topic || "Khác",
    sub: q.sub || "",
    age: age,
    diff: diffNum,
    difficulty: q.difficulty || (diffNum === 1 ? 'easy' : (diffNum === 2 ? 'medium' : 'hard')),
    grade: q.grade || (diffNum === 1 ? 2 : (diffNum === 2 ? 3 : 4)),
    explain: q.explain || "",
    img: q.img || "",
    type: q.type || "MC"
  };
}

function initMasterPool() {
  const pool = [];
  const seenIds = new Set();

  // 1. Nạp từ window.QUESTIONS_500 (nếu có từ questions_500.js)
  if (window.QUESTIONS_500 && Array.isArray(window.QUESTIONS_500)) {
    window.QUESTIONS_500.forEach(q => {
      const norm = normalizeQuestion(q, q.source);
      if (!seenIds.has(norm.id)) {
        seenIds.add(norm.id);
        pool.push(norm);
      }
    });
  }

  // 2. Nạp từ ALL_QUESTIONS (từ questions.js, gán source = 'Khác')
  if (typeof ALL_QUESTIONS !== 'undefined' && Array.isArray(ALL_QUESTIONS)) {
    ALL_QUESTIONS.forEach(q => {
      const norm = normalizeQuestion(q, "Khác");
      if (!seenIds.has(norm.id)) {
        seenIds.add(norm.id);
        pool.push(norm);
      }
    });
  }

  MASTER_POOL = pool;

  // 3. Nếu chạy trên web server (Vercel/HTTP), thử nạp questions.json cập nhật
  if (window.location.protocol.startsWith('http')) {
    fetch('questions.json')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data) && data.length > 0) {
          data.forEach(q => {
            const norm = normalizeQuestion(q, q.source);
            const idx = MASTER_POOL.findIndex(item => item.id === norm.id);
            if (idx !== -1) {
              MASTER_POOL[idx] = norm;
            } else {
              MASTER_POOL.push(norm);
            }
          });
          renderSourceChips();
          updatePoolCountDisplay();
        }
      })
      .catch(e => console.log('Fetch questions.json note:', e));
  }
}

function renderSourceChips() {
  const container = document.getElementById('source-chips-container');
  if (!container) return;
  container.innerHTML = '';

  SOURCE_CONFIG.forEach(src => {
    // Đếm số câu hỏi của nguồn này trong MASTER_POOL
    const count = MASTER_POOL.filter(q => {
      if (src.id === "Khác") {
        return q.source === "Khác" || !q.source || q.source === "Khác (Kho câu hỏi cũ)";
      }
      return q.source === src.id;
    }).length;

    const isSelected = selectedSources.has(src.id);
    const chip = document.createElement('div');
    chip.className = `source-toggle-chip ${isSelected ? 'selected' : ''}`;
    chip.onclick = () => toggleSource(src.id);

    chip.innerHTML = `
      <div class="source-chip-top">
        <div class="source-chip-icon-title">
          <span class="source-chip-icon">${src.icon}</span>
          <span class="source-chip-title">${src.name}</span>
        </div>
        <span class="source-chip-badge">${count} câu</span>
      </div>
      <div class="source-chip-desc">${src.desc}</div>
      <div class="source-chip-checkbox-row">
        <div class="source-checkbox-indicator">${isSelected ? '✓' : ''}</div>
      </div>
    `;
    container.appendChild(chip);
  });
}

function toggleSource(sourceId) {
  if (selectedSources.has(sourceId)) {
    selectedSources.delete(sourceId);
  } else {
    selectedSources.add(sourceId);
  }
  renderSourceChips();
  updatePoolCountDisplay();
}

function selectAllSources(isSelectAll) {
  if (isSelectAll) {
    SOURCE_CONFIG.forEach(s => selectedSources.add(s.id));
  } else {
    selectedSources.clear();
  }
  renderSourceChips();
  updatePoolCountDisplay();
}
"""

# Tìm vị trí bắt đầu các hàm logic cần thay thế:
# Thay thế getFilteredPool, updatePoolCountDisplay, window.onload, startQuiz, displayQuestion

NEW_LOGIC_FUNCTIONS = """
function getFilteredPool() {
  const poolSource = MASTER_POOL.length > 0 ? MASTER_POOL : (typeof ALL_QUESTIONS !== 'undefined' ? ALL_QUESTIONS : []);
  
  return poolSource.filter(q => {
    // 1. Kiểm tra bộ lọc nguồn
    const qSrc = q.source || "Khác";
    let matchSource = false;
    for (let s of selectedSources) {
      if (s === "Khác" && (qSrc === "Khác" || qSrc === "Khác (Kho câu hỏi cũ)")) {
        matchSource = true;
        break;
      }
      if (qSrc === s) {
        matchSource = true;
        break;
      }
    }
    if (!matchSource) return false;

    // 2. Kiểm tra bộ lọc độ tuổi
    if (selectedAge !== 'all' && q.age !== selectedAge) return false;

    // 3. Kiểm tra bộ lọc độ khó
    if (selectedDiff !== 'all' && String(q.diff) !== selectedDiff) return false;

    // 4. Kiểm tra bộ lọc chủ đề
    if (selectedTopic !== 'all' && q.topic !== selectedTopic) return false;

    return true;
  });
}

function updatePoolCountDisplay() {
  const pool = getFilteredPool();
  const sizeVal = document.getElementById('quiz-size').value;
  const requested = sizeVal === 'all' ? pool.length : parseInt(sizeVal);
  const textElem = document.getElementById('pool-count-text');
  const sourceSummaryElem = document.getElementById('source-summary-text');
  const sourceSummaryBox = document.getElementById('source-summary-banner');
  const btnStart = document.querySelector('.btn-start');

  // Đếm tổng số câu thuộc các nguồn đang chọn
  const totalInSelectedSources = MASTER_POOL.filter(q => {
    const qSrc = q.source || "Khác";
    for (let s of selectedSources) {
      if (s === "Khác" && (qSrc === "Khác" || qSrc === "Khác (Kho câu hỏi cũ)")) return true;
      if (qSrc === s) return true;
    }
    return false;
  }).length;

  // XỬ LÝ KHI NGƯỜI DÙNG BỎ CHỌN TẤT CẢ NGUỒN (0 nguồn)
  if (selectedSources.size === 0) {
    if (sourceSummaryBox) {
      sourceSummaryBox.className = 'source-status-summary warning';
    }
    if (sourceSummaryElem) {
      sourceSummaryElem.textContent = '⚠️ Bé hoặc phụ huynh vui lòng chọn ít nhất 1 nguồn đề thi để bắt đầu!';
    }
    if (textElem) {
      textElem.textContent = 'Chưa có câu hỏi nào sẵn sàng vì chưa có nguồn đề thi nào được chọn.';
    }
    if (btnStart) {
      btnStart.disabled = true;
      btnStart.classList.add('disabled-btn');
    }
    return;
  }

  // CÓ CHỌN NGUỒN HỢP LỆ
  if (sourceSummaryBox) {
    sourceSummaryBox.className = 'source-status-summary';
  }
  if (sourceSummaryElem) {
    sourceSummaryElem.textContent = `Đang chọn: ${totalInSelectedSources} câu hỏi khả dụng từ ${selectedSources.size} nguồn đề thi.`;
  }
  if (btnStart) {
    btnStart.disabled = false;
    btnStart.classList.remove('disabled-btn');
  }

  if (pool.length >= requested) {
    textElem.textContent = `Bộ lọc hiện có ${pool.length} câu phù hợp. Đảm bảo chọn đủ ${requested} câu cho lượt thi này!`;
  } else if (pool.length > 0) {
    textElem.textContent = `Bộ lọc có ${pool.length} câu. Chế độ thông minh (Smart Fallback) sẽ bổ sung thêm ${requested - pool.length} câu liên quan cùng nguồn để bé làm đủ ${requested} câu!`;
  } else {
    textElem.textContent = `Không có câu nào khớp với tất cả bộ lọc tuổi/chủ đề hiện tại. Hãy mở rộng chủ đề hoặc độ tuổi!`;
  }
}
"""

# Kiểm tra thay thế window.onload
OLD_ONLOAD = """window.onload = function() {
  renderTopics();
  loadSavedSettings();
  updatePoolCountDisplay();
};"""

NEW_ONLOAD = """window.onload = function() {
  initMasterPool();
  renderSourceChips();
  renderTopics();
  loadSavedSettings();
  updatePoolCountDisplay();
};"""

# Kiểm tra thay thế trong displayQuestion để cập nhật badge nguồn
OLD_DISPLAY_BADGE = """  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
  document.getElementById('badge-topic-age').textContent = `${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}`;"""

NEW_DISPLAY_BADGE = """  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
  const badgeSource = document.getElementById('badge-source');
  if (badgeSource) {
    badgeSource.innerHTML = `${getSourceIcon(q.source)} Nguồn: ${q.source || 'Khoa học'}`;
  }
  document.getElementById('badge-topic-age').textContent = `${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}`;"""

# Áp dụng các thay đổi
if 'HỆ THỐNG QUẢN LÝ MASTER POOL & 5 NGUỒN' not in html:
    # Chèn JS_SOURCE_ENGINE ngay sau thẻ <script> đầu tiên
    html = html.replace('<script>\n// =========================================================================', '<script>\n' + JS_SOURCE_ENGINE + '\n// =========================================================================')

if OLD_ONLOAD in html:
    html = html.replace(OLD_ONLOAD, NEW_ONLOAD)

# Thay thế getFilteredPool & updatePoolCountDisplay
pattern_get_pool = r'function getFilteredPool\(\)\s*\{[\s\S]*?function updatePoolCountDisplay\(\)\s*\{[\s\S]*?\n\}'
match = re.search(pattern_get_pool, html)
if match:
    html = html[:match.start()] + NEW_LOGIC_FUNCTIONS.strip() + html[match.end():]
    print("✅ Đã thay thế getFilteredPool và updatePoolCountDisplay thành công!")

if OLD_DISPLAY_BADGE in html:
    html = html.replace(OLD_DISPLAY_BADGE, NEW_DISPLAY_BADGE)
    print("✅ Đã cập nhật hiển thị badge nguồn trong displayQuestion()!")

with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã hoàn tất cập nhật toàn bộ logic JavaScript vào index.html!")
