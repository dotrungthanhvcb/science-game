import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update startQuiz to prevent language revert
target_start_lang = """  const langSelect = document.getElementById('language-mode-select');
  if (langSelect) {
    currentLanguageMode = langSelect.value;
  }
  currentSessionLanguageMode = currentLanguageMode;"""

repl_start_lang = """  const savedLang = localStorage.getItem('science_quiz_lang_mode');
  if (savedLang) {
    currentLanguageMode = savedLang;
  }
  const langSelect = document.getElementById('language-mode-select');
  if (langSelect) {
    if (currentLanguageMode) langSelect.value = currentLanguageMode;
    else currentLanguageMode = langSelect.value;
  }
  currentSessionLanguageMode = currentLanguageMode;"""

if target_start_lang in html:
    html = html.replace(target_start_lang, repl_start_lang)
    print("1. startQuiz language mode preservation updated.")
else:
    print("Warning: target_start_lang not found.")

# 2. Update Result Screen title and description in applyLanguageToUI
target_res_lang = """  // 5. Result Screen
  const resTitle = document.getElementById('res-title');
  if (resTitle && (resTitle.textContent === 'Bé Làm Tốt Lắm!' || resTitle.textContent === 'Great Job Explorer!')) {
    resTitle.textContent = isEn ? 'Great Job Explorer!' : 'Bé Làm Tốt Lắm!';
  }"""

repl_res_lang = """  // 5. Result Screen Title & Description Bilingual Translation
  const resTitle = document.getElementById('res-title');
  if (resTitle) {
    const t = resTitle.textContent.trim();
    if (t.includes('Chưa đạt') || t.includes('Needs Practice')) {
      resTitle.textContent = isEn ? 'Needs Practice - Never Give Up!' : 'Chưa đạt yêu cầu - Đừng nản lòng nhé!';
    } else if (t.includes('Mức Trung Bình') || t.includes('Fair Score')) {
      resTitle.textContent = isEn ? 'Fair Score - Keep Practicing!' : 'Mức Trung Bình - Cần ôn luyện thêm!';
    } else if (t.includes('Khá tốt') || t.includes('Good Effort')) {
      resTitle.textContent = isEn ? 'Good Effort!' : 'Kết quả Khá tốt!';
    } else if (t.includes('rất tốt') || t.includes('Great Job')) {
      resTitle.textContent = isEn ? 'Great Job!' : 'Làm bài rất tốt!';
    } else if (t.includes('Xuất sắc') || t.includes('Absolute Perfection')) {
      resTitle.textContent = isEn ? 'Absolute Perfection!' : 'Xuất sắc tuyệt đối!';
    } else if (t === 'Bé Làm Tốt Lắm!' || t === 'Great Job Explorer!') {
      resTitle.textContent = isEn ? 'Great Job Explorer!' : 'Bé Làm Tốt Lắm!';
    }
  }

  const resDesc = document.getElementById('res-desc');
  if (resDesc) {
    const d = resDesc.textContent.trim();
    if (d === 'Bé đã hoàn thành xuất sắc bài thi hôm nay!' || d === 'You have successfully completed today\\'s science quiz mission!') {
      resDesc.textContent = isEn ? 'You have successfully completed today\\'s science quiz mission!' : 'Bé đã hoàn thành xuất sắc bài thi hôm nay!';
    } else {
      const mMatch = d.match(/(\\d+\\.?\\d*)\\/10\\s*.*?\\((\\d+)\\/(\\d+)/);
      if (mMatch) {
        const sc10 = mMatch[1];
        const scCorrect = mMatch[2];
        const scTotal = mMatch[3];
        const scPct = Math.round((parseInt(scCorrect) / parseInt(scTotal)) * 100);

        if (scPct >= 90) {
          resDesc.textContent = isEn 
            ? `You scored ${sc10}/10 points (${scCorrect}/${scTotal} questions)! Outstanding scientific thinking and reflexes!`
            : `Bé đạt ${sc10}/10 điểm (${scCorrect}/${scTotal} câu)! Tư duy khoa học và phản xạ cực kỳ vượt trội!`;
        } else if (scPct >= 80) {
          resDesc.textContent = isEn
            ? `You scored ${sc10}/10 points (${scCorrect}/${scTotal} questions)! You have a solid grasp of science concepts!`
            : `Bé đạt ${sc10}/10 điểm (${scCorrect}/${scTotal} câu)! Bé nắm rất vững kiến thức, chỉ cần cẩn thận một vài câu nữa là đạt điểm tối đa!`;
        } else if (scPct >= 65) {
          resDesc.textContent = isEn
            ? `You scored ${sc10}/10 points (${scCorrect}/${scTotal} questions), above average. Review explanations to learn even more!`
            : `Bé đạt ${sc10}/10 điểm (${scCorrect}/${scTotal} câu), trên mức trung bình. Hãy xem lại phần giải thích các câu sai để nhớ sâu hơn nhé!`;
        } else if (scPct >= 50) {
          resDesc.textContent = isEn
            ? `You scored ${sc10}/10 points (${scCorrect}/${scTotal} questions). Review explanations of missed questions to understand better!`
            : `Bé đạt ${sc10}/10 điểm (${scCorrect}/${scTotal} câu). Bé đã đạt mức trung bình, nhưng cần xem kỹ lời giải thích của các câu sai để hiểu bài hơn nhé!`;
        } else {
          resDesc.textContent = isEn
            ? `You scored ${sc10}/10 points (${scCorrect}/${scTotal} questions). Click "Review Explanations" to master the concepts and try again!`
            : `Bé đạt ${sc10}/10 điểm (${scCorrect}/${scTotal} câu, chưa đạt mức trung bình). Đừng buồn nhé, hãy bấm "Xem lại chi tiết" để học lại đáp án đúng và thi lại lượt mới nào!`;
        }
      }
    }
  }

  // Also sync with modal-res-title and modal-res-desc
  const modalResTitle = document.getElementById('modal-res-title');
  if (modalResTitle && resTitle) {
    modalResTitle.textContent = resTitle.textContent;
  }
  const modalResDesc = document.getElementById('modal-res-desc');
  if (modalResDesc && resDesc) {
    modalResDesc.textContent = resDesc.textContent;
  }"""

if target_res_lang in html:
    html = html.replace(target_res_lang, repl_res_lang)
    print("2. res-title and res-desc bilingual translation updated.")
else:
    print("Warning: target_res_lang not found.")

# 3. Add modal-quick-nav translation IDs
target_quick_nav = """<!-- MODAL QUICK REVIEW: XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP) -->
<div class="modal-overlay" id="modal-quick-nav">
  <div class="modal-box" style="max-width: 580px;">
    <div class="modal-icon">📋</div>
    <div class="modal-title">Xem Lại Các Câu Vừa Làm</div>
    <div class="modal-desc" style="margin-bottom:8px;">
      Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!
    </div>
    <div style="background:#EEF2FF; border:1px solid #C7D2FE; border-radius:12px; padding:10px 14px; margin: 10px 0; font-size:14px; color:#1E40AF; font-weight:700;" id="quick-nav-status-text">
      📊 Đã làm: 0/0 câu
    </div>
    <div class="quick-nav-grid" id="quick-nav-grid"></div>
    <div style="display:flex; justify-content:center; gap:24px; font-size:13px; font-weight:700; margin-bottom:16px;">
      <span style="color:#1E40AF; display:flex; align-items:center; gap:4px;">🔵 Đã chọn đáp án</span>
      <span style="color:#64748B; display:flex; align-items:center; gap:4px;">⚪ Chưa làm</span>
    </div>
    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()" style="flex:1; min-width:160px; font-weight:700; display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="arrow-left" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Tiếp tục làm bài</span>
      </button>
      <button class="modal-btn-confirm" onclick="submitAndFinishQuiz()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:800; flex:1; min-width:180px; box-shadow:0 4px 14px rgba(16,185,129,0.35); display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="send" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Nộp bài & Xem điểm</span>
      </button>
    </div>
  </div>
</div>"""

repl_quick_nav = """<!-- MODAL QUICK REVIEW: XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP) -->
<div class="modal-overlay" id="modal-quick-nav">
  <div class="modal-box" style="max-width: 580px;">
    <div class="modal-icon">📋</div>
    <div class="modal-title" id="quick-nav-modal-title">Xem Lại Các Câu Vừa Làm</div>
    <div class="modal-desc" id="quick-nav-modal-desc" style="margin-bottom:8px;">
      Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!
    </div>
    <div style="background:#EEF2FF; border:1px solid #C7D2FE; border-radius:12px; padding:10px 14px; margin: 10px 0; font-size:14px; color:#1E40AF; font-weight:700;" id="quick-nav-status-text">
      📊 Đã làm: 0/0 câu
    </div>
    <div class="quick-nav-grid" id="quick-nav-grid"></div>
    <div style="display:flex; justify-content:center; gap:24px; font-size:13px; font-weight:700; margin-bottom:16px;">
      <span style="color:#1E40AF; display:flex; align-items:center; gap:4px;" id="quick-nav-legend-answered">🔵 Đã chọn đáp án</span>
      <span style="color:#64748B; display:flex; align-items:center; gap:4px;" id="quick-nav-legend-unanswered">⚪ Chưa làm</span>
    </div>
    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()" style="flex:1; min-width:160px; font-weight:700; display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="arrow-left" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span id="quick-nav-btn-cancel-text">Tiếp tục làm bài</span>
      </button>
      <button class="modal-btn-confirm" onclick="submitAndFinishQuiz()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:800; flex:1; min-width:180px; box-shadow:0 4px 14px rgba(16,185,129,0.35); display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="send" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span id="quick-nav-btn-submit-text">Nộp bài & Xem điểm</span>
      </button>
    </div>
  </div>
</div>"""

if target_quick_nav in html:
    html = html.replace(target_quick_nav, repl_quick_nav)
    print("3. modal-quick-nav HTML IDs updated.")
else:
    print("Warning: target_quick_nav not found.")

# 4. Add modal-quick-nav translation into applyLanguageToUI
target_lang_pre = """  const quizPreRevText = document.getElementById('quiz-pre-review-text');
  if (quizPreRevText) quizPreRevText.textContent = isEn ? '🔍 Review answers before submitting' : '🔍 Xem lại các câu vừa làm trước khi nộp';"""

repl_lang_pre = """  const quizPreRevText = document.getElementById('quiz-pre-review-text');
  if (quizPreRevText) quizPreRevText.textContent = isEn ? '🔍 Review answers before submitting' : '🔍 Xem lại các câu vừa làm trước khi nộp';

  // Quick Review Modal Translation
  const qNavTitle = document.getElementById('quick-nav-modal-title');
  if (qNavTitle) qNavTitle.textContent = isEn ? 'Review Your Answers' : 'Xem Lại Các Câu Vừa Làm';
  const qNavDesc = document.getElementById('quick-nav-modal-desc');
  if (qNavDesc) {
    qNavDesc.innerHTML = isEn 
      ? 'Click any question to review or modify your answer. When ready, click <strong>"Submit & View Results"</strong>!'
      : 'Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!';
  }
  const qNavAns = document.getElementById('quick-nav-legend-answered');
  if (qNavAns) qNavAns.textContent = isEn ? '🔵 Answered' : '🔵 Đã chọn đáp án';
  const qNavUnans = document.getElementById('quick-nav-legend-unanswered');
  if (qNavUnans) qNavUnans.textContent = isEn ? '⚪ Unanswered' : '⚪ Chưa làm';
  const qNavBtnCancel = document.getElementById('quick-nav-btn-cancel-text');
  if (qNavBtnCancel) qNavBtnCancel.textContent = isEn ? 'Continue Quiz' : 'Tiếp tục làm bài';
  const qNavBtnSubmit = document.getElementById('quick-nav-btn-submit-text');
  if (qNavBtnSubmit) qNavBtnSubmit.textContent = isEn ? 'Submit & View Results' : 'Nộp bài & Xem điểm';"""

if target_lang_pre in html:
    html = html.replace(target_lang_pre, repl_lang_pre)
    print("4. applyLanguageToUI quick-nav modal translation added.")
else:
    print("Warning: target_lang_pre not found.")

# 5. Update renderQuickNavGrid for bilingual support
target_grid = """function renderQuickNavGrid() {
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
}"""

repl_grid = """function renderQuickNavGrid() {
  const container = document.getElementById('quick-nav-grid');
  if (!container) return;
  container.innerHTML = '';

  const total = currentDeck.length;
  let answeredCount = 0;
  const isEn = (currentLanguageMode === 'en');

  currentDeck.forEach((q, idx) => {
    const userAns = userAnswersMap[q.id];
    const btn = document.createElement('button');
    btn.className = 'quick-nav-btn';

    const qNumLabel = isEn ? `Q ${idx + 1}` : `Câu ${idx + 1}`;

    if (userAns && userAns.chosenKey) {
      answeredCount++;
      btn.classList.add('answered');
      let badgeText = userAns.chosenKey;
      if (badgeText === 'Tự luận') badgeText = isEn ? 'Written' : 'Đã viết';
      btn.innerHTML = `<span class="q-num">${qNumLabel}</span><span class="q-ans-badge">${badgeText}</span>`;
      btn.title = isEn ? `Question ${idx + 1}: Chosen [${badgeText}]` : `Câu ${idx + 1}: Đã chọn [${badgeText}]`;
    } else {
      btn.classList.add('unanswered');
      const blankText = isEn ? 'Blank' : 'Chưa làm';
      btn.innerHTML = `<span class="q-num">${qNumLabel}</span><span class="q-ans-badge">${blankText}</span>`;
      btn.title = isEn ? `Question ${idx + 1}: Unanswered` : `Câu ${idx + 1}: Chưa trả lời`;
    }

    if (idx === currentIndex) {
      btn.classList.add('current');
    }

    btn.onclick = () => jumpToQuestion(idx);
    container.appendChild(btn);
  });

  const statusElem = document.getElementById('quick-nav-status-text');
  if (statusElem) {
    if (answeredCount >= total) {
      statusElem.innerHTML = isEn 
        ? `📊 Answered: <strong>${answeredCount}/${total}</strong> questions <span style="color:#059669;">(All questions completed!)</span>`
        : `📊 Đã làm: <strong>${answeredCount}/${total}</strong> câu <span style="color:#059669;">(Đã hoàn thành tất cả các câu!)</span>`;
    } else {
      statusElem.innerHTML = isEn
        ? `📊 Answered: <strong>${answeredCount}/${total}</strong> questions <span style="color:#D97706;">(${total - answeredCount} unanswered)</span>`
        : `📊 Đã làm: <strong>${answeredCount}/${total}</strong> câu <span style="color:#D97706;">(Còn ${total - answeredCount} câu chưa trả lời)</span>`;
    }
  }
}"""

if target_grid in html:
    html = html.replace(target_grid, repl_grid)
    print("5. renderQuickNavGrid bilingual support updated.")
else:
    print("Warning: target_grid not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished apply_comprehensive_en_translation.py!")
