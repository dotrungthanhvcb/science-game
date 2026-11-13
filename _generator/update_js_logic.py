# -*- coding: utf-8 -*-
with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Hàm getTopicSvg
svg_functions = """
// =========================================================================
// VECTOR SVG FALLBACK MINH HỌA THEO 7 CHỦ ĐỀ KHOA HỌC (100% KHÔNG BAO GIỜ VỠ ẢNH)
// =========================================================================
function getTopicSvg(topic) {
  let bgGradient = '#4361EE';
  let iconEmoji = '🔬';
  let title = 'Khoa Học Vui';

  if (topic === 'Động Vật') {
    bgGradient = 'linear-gradient(135deg, #FF6B6B 0%, #FFA07A 100%)';
    iconEmoji = '🦁';
    title = 'Thế Giới Động Vật';
  } else if (topic === 'Thực Vật') {
    bgGradient = 'linear-gradient(135deg, #10B981 0%, #059669 100%)';
    iconEmoji = '🌿';
    title = 'Thế Giới Thực Vật';
  } else if (topic === 'Vũ Trụ & Thời Tiết') {
    bgGradient = 'linear-gradient(135deg, #3A0CA3 0%, #4361EE 100%)';
    iconEmoji = '🌍';
    title = 'Vũ Trụ & Thời Tiết';
  } else if (topic === 'Cơ Thể Người') {
    bgGradient = 'linear-gradient(135deg, #EF4444 0%, #F43F5E 100%)';
    iconEmoji = '🫀';
    title = 'Cơ Thể Người & Sức Khỏe';
  } else if (topic === 'Địa Lý Việt Nam') {
    bgGradient = 'linear-gradient(135deg, #0284C7 0%, #06B6D4 100%)';
    iconEmoji = '🗺️';
    title = 'Địa Lý Non Sông Việt Nam';
  } else if (topic === 'Lịch Sử & Văn Hóa') {
    bgGradient = 'linear-gradient(135deg, #D97706 0%, #F59E0B 100%)';
    iconEmoji = '📜';
    title = 'Lịch Sử & Văn Hóa';
  } else if (topic === 'Vật Chất & Hiện Tượng') {
    bgGradient = 'linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%)';
    iconEmoji = '🧲';
    title = 'Vật Chất & Hiện Tượng';
  }

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340">
    <defs>
      <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#4361EE;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#4CC9F0;stop-opacity:1" />
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#grad)" rx="16"/>
    <circle cx="300" cy="140" r="75" fill="rgba(255,255,255,0.2)"/>
    <text x="50%" y="165" font-size="70" text-anchor="middle" dominant-baseline="middle">${iconEmoji}</text>
    <text x="50%" y="260" font-family="'Segoe UI', sans-serif" font-weight="700" font-size="22" fill="#FFFFFF" text-anchor="middle">${title}</text>
    <text x="50%" y="295" font-family="'Segoe UI', sans-serif" font-weight="600" font-size="14" fill="rgba(255,255,255,0.85)" text-anchor="middle">Đấu Trường Khoa Học 1.000 Câu • Antigravity</text>
  </svg>`;

  return 'data:image/svg+xml;utf8,' + encodeURIComponent(svg);
}

function handleImgError(img) {
  img.onerror = null;
  const q = currentDeck[currentIndex] || {};
  img.src = getTopicSvg(q.topic);
}
"""

if 'function getTopicSvg' not in text:
    text = text.replace('// STATE VARIABLES', svg_functions + '\n\n// STATE VARIABLES')
    print("Added getTopicSvg and handleImgError")

# 2. Thay thế displayQuestion
old_display = """function displayQuestion() {
  const q = currentDeck[currentIndex];
  const total = currentDeck.length;

  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
  document.getElementById('badge-topic-age').textContent = `${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}`;
  document.getElementById('question-text').textContent = q.q;

  // Ảnh minh họa chuẩn xác
  const imgElem = document.getElementById('question-img');
  const imgWrap = document.getElementById('q-img-wrap');
  if (q.img) {
    imgElem.src = q.img;
    imgWrap.style.display = 'block';
  } else {
    imgWrap.style.display = 'none';
  }

  setMascotMood('thinking', `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`);

  const pct = (currentIndex / total) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';

  const expCard = document.getElementById('explanation-card');
  expCard.className = 'explanation-card';
  expCard.style.display = 'none';

  document.getElementById('btn-next').classList.remove('visible');

  if (q.type === 'MC') {
    document.getElementById('choices-list').style.display = 'grid';
    document.getElementById('sa-box').style.display = 'none';
    renderMultipleChoice(q);
  } else {
    document.getElementById('choices-list').style.display = 'none';
    document.getElementById('sa-box').style.display = 'block';
    setupShortAnswer(q);
  }
}"""

new_display = """function displayQuestion() {
  const q = currentDeck[currentIndex];
  const total = currentDeck.length;
  const isLast = (currentIndex === total - 1);

  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
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

  setMascotMood('thinking', isLast ? 'Bé ơi, đây là câu cuối cùng rồi đó! Cố lên nào!' : `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`);

  const pct = (currentIndex / total) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';

  const expCard = document.getElementById('explanation-card');
  expCard.className = 'explanation-card';
  expCard.style.display = 'none';

  const btnNext = document.getElementById('btn-next');
  btnNext.classList.remove('visible');

  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = '🏁 Hoàn thành & Nộp bài';
    btnNext.classList.add('btn-last-step');
  } else {
    btnNext.innerHTML = 'Câu tiếp theo ➔';
    btnNext.classList.remove('btn-last-step');
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
}"""

if old_display in text:
    text = text.replace(old_display, new_display)
    print("Replaced displayQuestion with new logic")

# 3. Thay thế goNextQuestion và bổ sung modal logic
old_gonext = """function goNextQuestion() {
  currentIndex++;
  if (currentIndex < currentDeck.length) {
    displayQuestion();
  } else {
    finishQuiz();
  }
}"""

new_gonext = """function goNextQuestion() {
  if (currentIndex === currentDeck.length - 1) {
    // Là câu cuối cùng -> Mở confirmation modal hỏi xem lại hay nộp ngay
    openConfirmSubmitModal();
    return;
  }
  currentIndex++;
  if (currentIndex < currentDeck.length) {
    displayQuestion();
  } else {
    openConfirmSubmitModal();
  }
}

// =========================================================================
// CONFIRMATION SUBMIT & QUICK REVIEW TRƯỚC KHI NỘP BÀI
// =========================================================================
function openConfirmSubmitModal() {
  const answered = sessionAnswers.length;
  const total = currentDeck.length;
  const correct = sessionAnswers.filter(a => a.isCorrect).length;
  const wrong = answered - correct;

  document.getElementById('confirm-status-text').innerHTML = 
    `📊 Đã làm: <strong>${answered}/${total}</strong> câu (Đúng: ${correct} • Chưa đúng: ${wrong})`;
  document.getElementById('modal-confirm-submit').classList.add('active');
  playSound('correct');
  setMascotMood('happy', 'Bé đã làm hết các câu hỏi rồi! Bé có muốn kiểm tra lại trước khi nộp không?');
}

function closeConfirmSubmitModal() {
  document.getElementById('modal-confirm-submit').classList.remove('active');
}

function confirmSubmitAndFinish() {
  closeConfirmSubmitModal();
  closeQuickNavModal();
  finishQuiz();
}

function openReviewBeforeSubmit() {
  closeConfirmSubmitModal();
  renderQuickNavGrid();
  document.getElementById('modal-quick-nav').classList.add('active');
}

function closeQuickNavModal() {
  document.getElementById('modal-quick-nav').classList.remove('active');
}

function renderQuickNavGrid() {
  const container = document.getElementById('quick-nav-grid');
  container.innerHTML = '';
  currentDeck.forEach((q, idx) => {
    const btn = document.createElement('button');
    btn.className = 'quick-nav-btn';
    btn.textContent = idx + 1;

    // Kiểm tra trạng thái đã làm
    const ans = sessionAnswers.find(a => a.question.id === q.id);
    if (ans) {
      btn.classList.add(ans.isCorrect ? 'correct' : 'wrong');
      btn.title = `Câu ${idx + 1}: ${ans.isCorrect ? 'Chính xác' : 'Cần xem lại'}`;
    } else {
      btn.title = `Câu ${idx + 1}: Chưa làm`;
    }

    if (idx === currentIndex) {
      btn.classList.add('current');
    }

    btn.onclick = () => jumpToQuestion(idx);
    container.appendChild(btn);
  });
}

function jumpToQuestion(idx) {
  closeQuickNavModal();
  currentIndex = idx;
  displayQuestion();

  // Hiển thị lại đáp án và giải thích của câu đó nếu đã làm
  const ans = sessionAnswers.find(a => a.question.id === currentDeck[currentIndex].id);
  if (ans) {
    const expCard = document.getElementById('explanation-card');
    expCard.className = `explanation-card ${ans.isCorrect ? 'correct' : 'wrong'}`;
    expCard.innerHTML = `<strong>${ans.isCorrect ? '🎉 Hoan hô! Chính xác!' : '💡 Vì sao lại thế nhỉ?'}</strong><br>${ans.question.explain}`;
    expCard.style.display = 'block';

    const btnNext = document.getElementById('btn-next');
    btnNext.classList.add('visible');
  }
}"""

if old_gonext in text:
    text = text.replace(old_gonext, new_gonext)
    print("Replaced goNextQuestion and added confirm modal functions")

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated index.html successfully!")
