# -*- coding: utf-8 -*-
"""
Script cập nhật logic JS trong index.html:
- Biến cấu hình GOOGLE_SCRIPT_URL = ""
- Biến userAnswersMap và isQuizSubmitted
- displayQuestion, renderMultipleChoice, handleChoiceSelect, setupShortAnswer, submitShortAnswer
- goNextQuestion, openReviewBeforeSubmit, renderQuickNavGrid, jumpToQuestion
- submitAndFinishQuiz, sendDataToAppsScript, saveSettings, loadSavedSettings
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Thêm GOOGLE_SCRIPT_URL ngay đầu <script>
if 'const GOOGLE_SCRIPT_URL' not in html:
    html = html.replace('<script>', '<script>\n// CẤU HÌNH GOOGLE APPS SCRIPT WEB APP URL\nconst GOOGLE_SCRIPT_URL = "";\n')

# 2. Thêm userAnswersMap và isQuizSubmitted vào danh sách biến STATE VARIABLES
OLD_STATE_VARS = """// STATE VARIABLES
let selectedAge = 'all';
let selectedDiff = 'all';
let selectedTopic = 'all';
let currentDeck = [];
let currentIndex = 0;
let correctCount = 0;
let wrongList = [];
let sessionAnswers = [];
let timerInterval = null;
let startTime = null;
let elapsedSeconds = 0;
let isPaused = false;"""

NEW_STATE_VARS = """// STATE VARIABLES
let selectedAge = 'all';
let selectedDiff = 'all';
let selectedTopic = 'all';
let currentDeck = [];
let currentIndex = 0;
let correctCount = 0;
let wrongList = [];
let sessionAnswers = [];
let timerInterval = null;
let startTime = null;
let elapsedSeconds = 0;
let isPaused = false;

// QUẢN LÝ BÀI THI & BẢO MẬT ĐÁP ÁN (ẨN ĐÚNG/SAI ĐẾN KHI NỘP BÀI)
let userAnswersMap = {}; // Lưu { [qId]: { chosenKey, chosenText } }
let isQuizSubmitted = false; // Đã nộp bài hay chưa (khóa bài làm khi true)"""

if OLD_STATE_VARS in html:
    html = html.replace(OLD_STATE_VARS, NEW_STATE_VARS)

# 3. Cập nhật saveSettings và loadSavedSettings cho student-class và GOOGLE_SCRIPT_URL
OLD_SETTINGS = """function loadSavedSettings() {
  const url = localStorage.getItem('science_quiz_script_url');
  if (url) document.getElementById('apps-script-url').value = url;
  const name = localStorage.getItem('science_quiz_kid_name');
  if (name) document.getElementById('user-name').value = name;
}

function saveSettings() {
  localStorage.setItem('science_quiz_script_url', document.getElementById('apps-script-url').value.trim());
  localStorage.setItem('science_quiz_kid_name', document.getElementById('user-name').value.trim());
}"""

NEW_SETTINGS = """function loadSavedSettings() {
  const url = localStorage.getItem('science_quiz_script_url');
  if (url) {
    document.getElementById('apps-script-url').value = url;
  } else if (typeof GOOGLE_SCRIPT_URL !== 'undefined' && GOOGLE_SCRIPT_URL) {
    document.getElementById('apps-script-url').value = GOOGLE_SCRIPT_URL;
  }
  const name = localStorage.getItem('science_quiz_kid_name');
  if (name) document.getElementById('user-name').value = name;
  const sClass = localStorage.getItem('science_quiz_kid_class');
  if (sClass && document.getElementById('student-class')) document.getElementById('student-class').value = sClass;
}

function saveSettings() {
  localStorage.setItem('science_quiz_script_url', document.getElementById('apps-script-url').value.trim());
  localStorage.setItem('science_quiz_kid_name', document.getElementById('user-name').value.trim());
  if (document.getElementById('student-class')) {
    localStorage.setItem('science_quiz_kid_class', document.getElementById('student-class').value.trim());
  }
}"""

if OLD_SETTINGS in html:
    html = html.replace(OLD_SETTINGS, NEW_SETTINGS)

# 4. Cập nhật startQuiz: reset userAnswersMap, isQuizSubmitted
pattern_start_quiz = r'function startQuiz\(\)\s*\{[\s\S]*?displayQuestion\(\);\s*startTimer\(\);\s*\}'
NEW_START_QUIZ = """function startQuiz() {
  saveSettings();
  let pool = getFilteredPool();
  const sizeVal = document.getElementById('quiz-size').value;
  const targetCount = sizeVal === 'all' ? pool.length : parseInt(sizeVal);

  // SMART FALLBACK
  if (pool.length < targetCount && sizeVal !== 'all') {
    const needed = targetCount - pool.length;
    let fallbackCandidates = MASTER_POOL.filter(q => {
      if (pool.includes(q)) return false;
      const qSrc = q.source || "Khác";
      for (let s of selectedSources) {
        if (s === "Khác" && (qSrc === "Khác" || qSrc === "Khác (Kho câu hỏi cũ)")) return true;
        if (qSrc === s) return true;
      }
      return false;
    });
    if (fallbackCandidates.length < needed) {
      const extraCandidates = MASTER_POOL.filter(q => !pool.includes(q) && !fallbackCandidates.includes(q));
      fallbackCandidates = [...fallbackCandidates, ...extraCandidates];
    }
    const bonus = [...fallbackCandidates].sort(() => Math.random() - 0.5).slice(0, needed);
    pool = [...pool, ...bonus];
  }

  // TỈ LỆ ÔN TẬP
  const ratio = document.getElementById('review-ratio').value;
  const stats = getQuestionStats();

  if (ratio === 'unseen') {
    const unseen = pool.filter(q => !stats[q.id] || stats[q.id].seen === 0);
    if (unseen.length > 0) pool = unseen;
  } else if (ratio === 'reviewed') {
    const reviewed = pool.filter(q => stats[q.id] && stats[q.id].seen > 0);
    if (reviewed.length > 0) pool = reviewed;
  } else if (ratio === 'mistakes') {
    const wrongPool = pool.filter(q => stats[q.id] && stats[q.id].wrong > stats[q.id].correct);
    const otherPool = pool.filter(q => !wrongPool.includes(q));
    const half = Math.floor(targetCount / 2);
    const selWrong = [...wrongPool].sort(() => Math.random() - 0.5).slice(0, half);
    const selOther = [...otherPool].sort(() => Math.random() - 0.5).slice(0, targetCount - selWrong.length);
    pool = [...selWrong, ...selOther];
  }

  // Shuffle đề thi
  pool = [...pool].sort(() => Math.random() - 0.5);

  if (sizeVal !== 'all' && pool.length > targetCount) {
    pool = pool.slice(0, targetCount);
  }

  currentDeck = pool;
  currentIndex = 0;
  correctCount = 0;
  wrongList = [];
  sessionAnswers = [];
  userAnswersMap = {};
  isQuizSubmitted = false;

  showScreen('quiz-screen');
  displayQuestion();
  startTimer();
}"""

match_sq = re.search(pattern_start_quiz, html)
if match_sq:
    html = html[:match_sq.start()] + NEW_START_QUIZ + html[match_sq.end():]
    print("✅ Đã cập nhật startQuiz!")

# 5. Cập nhật displayQuestion, renderMultipleChoice, handleChoiceSelect, setupShortAnswer, submitShortAnswer
# goNextQuestion, openConfirmSubmitModal, openReviewBeforeSubmit, renderQuickNavGrid, jumpToQuestion, finishQuiz
NEW_QUIZ_EXECUTION_CODE = """
// =========================================================================
// QUESTION RENDERING (VIEWPORT-FIT KHÔNG PHẢI CUỘN MÀN HÌNH)
// =========================================================================
function displayQuestion() {
  const q = currentDeck[currentIndex];
  const total = currentDeck.length;
  const isLast = (currentIndex === total - 1);

  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
  const badgeSource = document.getElementById('badge-source');
  if (badgeSource) {
    badgeSource.innerHTML = `${getSourceIcon(q.source)} Nguồn: ${q.source || 'Khoa học'}`;
  }
  document.getElementById('badge-topic-age').textContent = `${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}`;
  document.getElementById('question-text').textContent = q.q;

  // Xử lý ảnh minh họa thông minh + Fallback SVG chuyên biệt theo chủ đề khi lỗi
  const imgElem = document.getElementById('question-img');
  const imgWrap = document.getElementById('q-img-wrap');
  imgElem.onerror = function() {
    this.onerror = null;
    this.src = getTopicSvg(q.topic);
  };
  if (q.img) {
    imgElem.src = q.img;
  } else {
    imgElem.src = getTopicSvg(q.topic);
  }
  imgWrap.style.display = 'block';

  // Mascot động viên
  setMascotMood('thinking', isLast ? 'Bé ơi, đây là câu cuối cùng rồi! Làm xong bé kiểm tra lại nhé!' : `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`);

  const pct = (currentIndex / total) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';

  // ẨN HOÀN TOÀN THẺ GIẢI THÍCH TRƯỚC KHI NỘP BÀI (BẢO MẬT KỲ THI)
  const expCard = document.getElementById('explanation-card');
  expCard.className = 'explanation-card';
  expCard.style.display = 'none';

  const btnNext = document.getElementById('btn-next');
  // Nếu câu này đã được chọn trước đó -> hiển thị nút chuyển câu
  if (userAnswersMap[q.id]) {
    btnNext.classList.add('visible');
  } else {
    btnNext.classList.remove('visible');
  }

  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = '📋 Xem lại & Nộp bài';
    btnNext.classList.add('btn-last-step');
    btnNext.onclick = openReviewBeforeSubmit;
  } else {
    btnNext.innerHTML = 'Câu tiếp theo ➔';
    btnNext.classList.remove('btn-last-step');
    btnNext.onclick = goNextQuestion;
  }

  if (q.type === 'MC') {
    document.getElementById('choices-list').style.display = 'grid';
    document.getElementById('sa-box').style.display = 'none';
    renderMultipleChoice(q);
  } else {
    document.getElementById('choices-list').style.display = 'none';
    document.getElementById('sa-box').style.display = 'block';
    setupShortAnswer(q);
  }
}

function renderMultipleChoice(q) {
  const container = document.getElementById('choices-list');
  container.innerHTML = '';
  const options = [
    { key: 'A', text: q.a },
    { key: 'B', text: q.b },
    { key: 'C', text: q.c },
    { key: 'D', text: q.d }
  ];

  const currentSelection = userAnswersMap[q.id] ? userAnswersMap[q.id].chosenKey : null;

  options.forEach(opt => {
    if (!opt.text) return;
    const btn = document.createElement('button');
    btn.className = 'choice-option';
    
    // Nếu câu này đã được chọn -> Highlight bằng màu trung tính xanh dương
    if (currentSelection === opt.key) {
      btn.classList.add('selected');
    }

    btn.innerHTML = `<span class="choice-letter">${opt.key}</span><span>${opt.text}</span>`;
    
    // Nếu bài chưa nộp thì luôn cho phép click / đổi đáp án
    if (!isQuizSubmitted) {
      btn.onclick = () => handleChoiceSelect(opt.key, opt.text, btn);
    } else {
      btn.disabled = true;
    }
    
    container.appendChild(btn);
  });
}

function handleChoiceSelect(chosenKey, chosenText, chosenBtn) {
  if (isQuizSubmitted) return;

  const q = currentDeck[currentIndex];
  const allBtns = document.querySelectorAll('.choice-option');
  
  // Gỡ bỏ selected ở các nút khác và đánh dấu nút mới được chọn
  allBtns.forEach(b => b.classList.remove('selected'));
  chosenBtn.classList.add('selected');

  // Ghi nhận đáp án người chơi (CHƯA CHẤM ĐIỂM, CHƯA BÁO ĐÚNG/SAI)
  userAnswersMap[q.id] = {
    chosenKey: chosenKey,
    chosenText: chosenText
  };

  // Hiệu ứng âm thanh click vui tươi
  playSound('click');
  setMascotMood('happy', `Bé đã chọn [${chosenKey}]! Bé có thể đổi đáp án khác hoặc bấm "Câu tiếp theo" nhé.`);

  // Luôn hiển thị nút tiếp theo sau khi chọn
  const btnNext = document.getElementById('btn-next');
  btnNext.classList.add('visible');
}

function setupShortAnswer(q) {
  const input = document.getElementById('sa-input-field');
  const savedAns = userAnswersMap[q.id];
  input.value = savedAns ? savedAns.chosenText : '';
  input.disabled = isQuizSubmitted;
  input.className = 'sa-input' + (savedAns ? ' selected' : '');
  input.onkeypress = (e) => { if (e.key === 'Enter') submitShortAnswer(); };
  input.oninput = () => {
    const val = input.value.trim();
    if (val) {
      userAnswersMap[q.id] = { chosenKey: 'Tự luận', chosenText: val };
      document.getElementById('btn-next').classList.add('visible');
    }
  };
  setTimeout(() => input.focus(), 150);
}

function submitShortAnswer() {
  const input = document.getElementById('sa-input-field');
  const userText = input.value.trim();
  if (!userText || isQuizSubmitted) return;

  const q = currentDeck[currentIndex];
  userAnswersMap[q.id] = {
    chosenKey: 'Tự luận',
    chosenText: userText
  };

  playSound('click');
  setMascotMood('happy', 'Bé đã nhập câu trả lời xong! Bé có thể sửa lại hoặc bấm tiếp tục nhé.');
  document.getElementById('btn-next').classList.add('visible');
}

function goNextQuestion() {
  if (currentIndex === currentDeck.length - 1) {
    // Là câu cuối cùng -> Mở màn hình xem lại trước khi nộp
    openReviewBeforeSubmit();
    return;
  }
  currentIndex++;
  if (currentIndex < currentDeck.length) {
    displayQuestion();
  } else {
    openReviewBeforeSubmit();
  }
}

// =========================================================================
// POPUP XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP BÀI) - ẨN 100% ĐÚNG/SAI
// =========================================================================
function openReviewBeforeSubmit() {
  closeConfirmSubmitModal();
  renderQuickNavGrid();
  document.getElementById('modal-quick-nav').classList.add('active');
  playSound('click');
}

function closeQuickNavModal() {
  document.getElementById('modal-quick-nav').classList.remove('active');
}

function openConfirmSubmitModal() {
  openReviewBeforeSubmit();
}

function closeConfirmSubmitModal() {
  const modal = document.getElementById('modal-confirm-submit');
  if (modal) modal.classList.remove('active');
}

function confirmSubmitAndFinish() {
  submitAndFinishQuiz();
}

function renderQuickNavGrid() {
  const container = document.getElementById('quick-nav-grid');
  if (!container) return;
  container.innerHTML = '';

  const total = currentDeck.length;
  let answeredCount = 0;

  currentDeck.forEach((q, idx) => {
    const userAns = userAnswersMap[q.id];
    const btn = document.createElement('button');
    btn.className = 'quick-nav-btn';

    if (userAns && userAns.chosenKey) {
      answeredCount++;
      btn.classList.add('answered');
      const badgeText = userAns.chosenKey === 'Tự luận' ? 'Đã viết' : userAns.chosenKey;
      btn.innerHTML = `<span class="q-num">Câu ${idx + 1}</span><span class="q-ans-badge">${badgeText}</span>`;
      btn.title = `Câu ${idx + 1}: Đã chọn [${badgeText}]`;
    } else {
      btn.classList.add('unanswered');
      btn.innerHTML = `<span class="q-num">Câu ${idx + 1}</span><span class="q-ans-badge">Chưa làm</span>`;
      btn.title = `Câu ${idx + 1}: Chưa trả lời`;
    }

    if (idx === currentIndex) {
      btn.classList.add('current');
    }

    // Bấm vào câu bất kỳ để quay lại xem lại hoặc sửa đáp án
    btn.onclick = () => jumpToQuestion(idx);
    container.appendChild(btn);
  });

  // Cập nhật dòng trạng thái (TUYỆT ĐỐI KHÔNG LỘ ĐÚNG/SAI HOẶC ĐIỂM SỐ)
  const statusElem = document.getElementById('quick-nav-status-text');
  if (statusElem) {
    if (answeredCount >= total) {
      statusElem.innerHTML = `📊 Đã làm: <strong>${answeredCount}/${total}</strong> câu <span style="color:#059669;">(Đã hoàn thành tất cả các câu!)</span>`;
    } else {
      statusElem.innerHTML = `📊 Đã làm: <strong>${answeredCount}/${total}</strong> câu <span style="color:#D97706;">(Còn ${total - answeredCount} câu chưa trả lời)</span>`;
    }
  }
}

function jumpToQuestion(idx) {
  closeQuickNavModal();
  closeConfirmSubmitModal();
  currentIndex = idx;
  displayQuestion();
}

// =========================================================================
// CHÍNH THỨC NỘP BÀI & CHẤM ĐIỂM (SAU KHI BẤM 'NỘP BÀI & XEM ĐIỂM')
// =========================================================================
function submitAndFinishQuiz() {
  closeQuickNavModal();
  closeConfirmSubmitModal();
  
  // 1. Khóa bài làm (không cho phép sửa nữa)
  isQuizSubmitted = true;
  clearInterval(timerInterval);

  // 2. Chính thức chấm điểm từng câu
  correctCount = 0;
  wrongList = [];
  sessionAnswers = [];

  currentDeck.forEach(q => {
    const userAns = userAnswersMap[q.id];
    let isCorrect = false;
    let chosenKey = "Chưa làm";
    let chosenText = "Chưa trả lời";

    if (userAns) {
      chosenKey = userAns.chosenKey;
      chosenText = userAns.chosenText;

      if (q.type === 'MC') {
        isCorrect = (chosenKey === q.ans);
      } else {
        const validAnswers = (q.ans || '').toLowerCase().split('|').map(s => s.trim());
        const uText = chosenText.toLowerCase().trim();
        isCorrect = validAnswers.some(ans => uText === ans || (ans.length >= 3 && uText.includes(ans)));
      }
    }

    if (isCorrect) {
      correctCount++;
    } else {
      wrongList.push(q);
    }

    updateQuestionStat(q.id, isCorrect);

    sessionAnswers.push({
      question: q,
      userAnswerKey: chosenKey,
      userAnswerText: chosenText,
      isCorrect: isCorrect
    });
  });

  // 3. Tính điểm số & thời gian làm bài
  const total = currentDeck.length;
  const wrongCount = total - correctCount;
  const score10 = ((correctCount / total) * 10).toFixed(1);
  const pct = Math.round((correctCount / total) * 100);
  const minutes = Math.floor(elapsedSeconds / 60);
  const seconds = elapsedSeconds % 60;
  const timeStr = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

  // 4. Hiển thị lên màn hình kết quả (result-screen)
  document.getElementById('res-score').textContent = `${score10}/10 (${pct}%)`;
  document.getElementById('res-correct').textContent = `${correctCount}/${total}`;
  const resWrongElem = document.getElementById('res-wrong');
  if (resWrongElem) resWrongElem.textContent = `${wrongCount}/${total}`;
  document.getElementById('res-time').textContent = timeStr;

  let stars = '⭐';
  let icon = '👏';
  let title = 'Cố gắng ở lượt sau nhé!';
  if (pct >= 90) {
    stars = '⭐⭐⭐';
    icon = '🏆';
    title = 'Xuất sắc tuyệt đối!';
    fireConfetti();
    playSound('correct');
  } else if (pct >= 75) {
    stars = '⭐⭐';
    icon = '🎉';
    title = 'Bé làm rất tốt!';
    fireConfetti();
    playSound('correct');
  } else if (pct >= 50) {
    stars = '⭐';
    icon = '💪';
    title = 'Tiến bộ rõ rệt!';
    playSound('correct');
  }

  document.getElementById('res-stars').textContent = stars;
  document.getElementById('res-icon').textContent = icon;
  document.getElementById('res-title').textContent = title;

  const btnReplayWrong = document.getElementById('btn-replay-wrong');
  if (btnReplayWrong) {
    btnReplayWrong.style.display = wrongList.length > 0 ? 'block' : 'none';
  }

  showScreen('result-screen');

  // 5. TỰ ĐỘNG GỬI KẾT QUẢ VỀ GOOGLE SHEETS
  sendDataToAppsScript(total, correctCount, wrongCount, `${score10}/10 (${pct}%)`, timeStr);
}

function finishQuiz() {
  submitAndFinishQuiz();
}

// =========================================================================
// TỰ ĐỘNG LƯU KẾT QUẢ VÀO GOOGLE SHEETS TRONG GOOGLE DRIVE
// =========================================================================
function sendDataToAppsScript(total, correct, wrong, scoreStr, durationStr) {
  const scriptUrl = document.getElementById('apps-script-url').value.trim() || (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  const statusElem = document.getElementById('sync-status');
  if (!statusElem) return;

  if (!scriptUrl) {
    statusElem.innerHTML = '💡 <em>Chưa cài đặt URL Google Apps Script. Kết quả được lưu trên bộ nhớ máy của bạn.</em>';
    return;
  }

  statusElem.innerHTML = '⏳ <span style="color:var(--primary); font-weight:700;">Đang lưu kết quả vào Google Sheets...</span>';

  const payload = {
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
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
    statusElem.innerHTML = '✅ <span style="color:#15803D; font-weight:700;">Đã lưu kết quả thành công!</span>';
  })
  .catch(err => {
    statusElem.innerHTML = `⚠️ <span style="color:#B91C1C;">Không thể lưu lên Google Sheets: ${err.message}</span>`;
  });
}
"""

# Tìm đoạn code cũ từ `function displayQuestion()` đến `function openReviewScreen()`
pos_disp = html.find('function displayQuestion()')
pos_rev = html.find('function openReviewScreen()')

if pos_disp != -1 and pos_rev != -1:
    html = html[:pos_disp] + NEW_QUIZ_EXECUTION_CODE.strip() + '\n\n' + html[pos_rev:]
    print("✅ Đã thay thế toàn bộ khối xử lý Quiz, Review Modal và Chấm điểm!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã ghi thành công toàn bộ cập nhật vào index.html!")
