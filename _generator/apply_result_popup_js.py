import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. New functions for Result Popup Modal
result_modal_funcs = """
// =========================================================================
// MODAL POPUP BÁO KẾT QUẢ BÀI THI (RESULT POPUP MODAL)
// =========================================================================
function openQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (!modal) return;
  refreshLucideIcons();
  modal.classList.add('active');
  const isEn = (currentLanguageMode === 'en');
  
  // Tag
  const modalResTag = document.getElementById('modal-res-tag');
  if (modalResTag) modalResTag.textContent = isEn ? '🎉 MISSION ACCOMPLISHED' : '🎉 BÁO CÁO KẾT QUẢ BÀI THI';
  
  const total = currentDeck.length;
  const wrongCount = total - correctCount;
  const score10 = ((correctCount / total) * 10).toFixed(1);
  const pct = Math.round((correctCount / total) * 100);
  const minutes = Math.floor(elapsedSeconds / 60);
  const seconds = elapsedSeconds % 60;
  const timeStr = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

  // Metrics
  const modalResScore = document.getElementById('modal-res-score');
  if (modalResScore) modalResScore.textContent = `${score10}/10`;
  const modalResCorrect = document.getElementById('modal-res-correct');
  if (modalResCorrect) modalResCorrect.textContent = `${correctCount}/${total}`;
  const modalResWrong = document.getElementById('modal-res-wrong');
  if (modalResWrong) modalResWrong.textContent = `${wrongCount}/${total}`;
  const modalResTime = document.getElementById('modal-res-time');
  if (modalResTime) modalResTime.textContent = timeStr;

  // Metric Labels
  const lblScore = document.getElementById('modal-lbl-score');
  if (lblScore) lblScore.textContent = isEn ? 'Score' : 'Điểm số';
  const lblCorrect = document.getElementById('modal-lbl-correct');
  if (lblCorrect) lblCorrect.textContent = isEn ? 'Correct ✅' : 'Đúng ✅';
  const lblWrong = document.getElementById('modal-lbl-wrong');
  if (lblWrong) lblWrong.textContent = isEn ? 'Wrong ❌' : 'Sai ❌';
  const lblTime = document.getElementById('modal-lbl-time');
  if (lblTime) lblTime.textContent = isEn ? 'Time' : 'Thời gian';

  // Stars, Trophy & Title
  const modalResTitle = document.getElementById('modal-res-title');
  const modalResDesc = document.getElementById('modal-res-desc');
  const modalResStars = document.getElementById('modal-res-stars');
  const modalResIcon = document.getElementById('modal-res-icon');
  const modalSpeech = document.getElementById('modal-mascot-speech');

  const m = (typeof MASCOTS !== 'undefined') ? (MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0]) : { name: 'Giáo Sư Cú Vọ', name_en: 'Prof. Owl' };
  const mName = isEn ? (m.name_en || m.name) : m.name;

  if (pct >= 90) {
    if (modalResIcon) modalResIcon.textContent = '🏆';
    if (modalResStars) modalResStars.textContent = '⭐⭐⭐';
    if (modalResTitle) modalResTitle.textContent = isEn ? 'Absolute Perfection!' : 'Xuất sắc tuyệt đối!';
    if (modalResDesc) modalResDesc.textContent = isEn ? `Score: ${score10}/10 points (${correctCount}/${total} questions). Brilliant scientific thinking!` : `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Tư duy khoa học và phản xạ cực kỳ vượt trội!`;
    if (modalSpeech) modalSpeech.textContent = isEn ? `Outstanding score! ${mName} is so proud of you! 🏆` : `Bé đạt điểm xuất sắc tuyệt đối luôn, ${mName} tự hào về bé quá! 🏆`;
  } else if (pct >= 80) {
    if (modalResIcon) modalResIcon.textContent = '🎉';
    if (modalResStars) modalResStars.textContent = '⭐⭐';
    if (modalResTitle) modalResTitle.textContent = isEn ? 'Great Job!' : 'Làm bài rất tốt!';
    if (modalResDesc) modalResDesc.textContent = isEn ? `Score: ${score10}/10 points (${correctCount}/${total} questions). Great grasp of science concepts!` : `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Bé nắm rất vững kiến thức!`;
    if (modalSpeech) modalSpeech.textContent = isEn ? `Great performance! Keep up the good work! 🎉` : `Bé làm bài rất tốt! Cùng giữ vững phong độ này nhé! 🎉`;
  } else if (pct >= 65) {
    if (modalResIcon) modalResIcon.textContent = '👍';
    if (modalResStars) modalResStars.textContent = '⭐';
    if (modalResTitle) modalResTitle.textContent = isEn ? 'Good Effort!' : 'Kết quả Khá tốt!';
    if (modalResDesc) modalResDesc.textContent = isEn ? `Score: ${score10}/10 points (${correctCount}/${total} questions). Review missed questions to learn more!` : `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu). Xem lại câu sai để nhớ sâu hơn nhé!`;
    if (modalSpeech) modalSpeech.textContent = isEn ? `Good job! Review incorrect answers to improve further! 👍` : `Bé đạt kết quả khá tốt trên trung bình rồi đó! Xem lại câu sai để tiến bộ nha! 👍`;
  } else if (pct >= 50) {
    if (modalResIcon) modalResIcon.textContent = '📖';
    if (modalResStars) modalResStars.textContent = '🌱';
    if (modalResTitle) modalResTitle.textContent = isEn ? 'Fair Score - Keep Practicing!' : 'Mức Trung Bình - Cần cố gắng!';
    if (modalResDesc) modalResDesc.textContent = isEn ? `Score: ${score10}/10 points (${correctCount}/${total} questions). Check missed answers to improve!` : `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu). Bé xem kỹ lời giải câu sai để tiến bộ nhé!`;
    if (modalSpeech) modalSpeech.textContent = isEn ? `Fair score! Review the detailed answers to brush up! 📖` : `Bé xem kỹ lời giải thích chi tiết của các câu sai để ôn lại nhé! 📖`;
  } else {
    if (modalResIcon) modalResIcon.textContent = '💪';
    if (modalResStars) modalResStars.textContent = '⚡';
    if (modalResTitle) modalResTitle.textContent = isEn ? 'Needs Practice - Never Give Up!' : 'Chưa đạt - Đừng nản lòng nhé!';
    if (modalResDesc) modalResDesc.textContent = isEn ? `Score: ${score10}/10 points (${correctCount}/${total} questions). Review answers and try again!` : `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu). Hãy xem lại câu sai và thi lại nhé!`;
    if (modalSpeech) modalSpeech.textContent = isEn ? `Do not worry! Review the explanations and take another try! 💪` : `Đừng buồn nhé, xem giải thích câu sai để hiểu bài rồi thi lại nào! 💪`;
  }

  // Buttons visibility & text
  const btnReviewWrong = document.getElementById('btn-modal-review-wrong');
  const btnReviewWrongText = document.getElementById('btn-modal-review-wrong-text');
  const btnReplayWrong = document.getElementById('btn-modal-replay-wrong');
  if (wrongCount > 0) {
    if (btnReviewWrong) btnReviewWrong.style.display = 'flex';
    if (btnReviewWrongText) btnReviewWrongText.textContent = isEn ? `❌ Review ${wrongCount} Mistake${wrongCount > 1 ? 's' : ''}` : `❌ Xem Lại ${wrongCount} Câu Sai`;
    if (btnReplayWrong) btnReplayWrong.style.display = 'flex';
  } else {
    if (btnReviewWrong) btnReviewWrong.style.display = 'none';
    if (btnReplayWrong) btnReplayWrong.style.display = 'none';
  }

  const btnReviewAllText = document.getElementById('btn-modal-review-all-text');
  if (btnReviewAllText) btnReviewAllText.textContent = isEn ? '📑 Review All Answers' : '📑 Xem Toàn Bộ Bài Làm';
  const btnCardModeText = document.getElementById('btn-modal-card-mode-text');
  if (btnCardModeText) btnCardModeText.textContent = isEn ? '🃏 One-by-One' : '🃏 Từng câu một';
  const btnReplayWrongText = document.getElementById('btn-modal-replay-wrong-text');
  if (btnReplayWrongText) btnReplayWrongText.textContent = isEn ? 'Practice Mistakes' : 'Ôn câu sai';
  const btnLeadText = document.getElementById('btn-modal-lead-text');
  if (btnLeadText) btnLeadText.textContent = isEn ? 'Stars 🌟' : 'Bảng Sao 🌟';
  const btnBackHomeText = document.getElementById('btn-modal-back-home-text');
  if (btnBackHomeText) btnBackHomeText.textContent = isEn ? 'Close & View Detailed Scorecard ➔' : 'Đóng & Xem Bảng Điểm Chi Tiết ➔';

  refreshLucideIcons();
}

function closeQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (modal) modal.classList.remove('active');
}

function replayMistakesFromModal() {
  closeQuizResultModal();
  replayMistakes();
}

function openLeaderboardFromModal() {
  closeQuizResultModal();
  openLeaderboardModal();
}
"""

if "function openQuizResultModal" not in content:
    content = content.replace("function finishQuiz() {", result_modal_funcs + "\nfunction finishQuiz() {")
    print("Added openQuizResultModal, closeQuizResultModal, replayMistakesFromModal")

# 2. Update submitAndFinishQuiz to pop up openQuizResultModal() and update res screen buttons
old_finish_end = """  showScreen('result-screen');

  // 5. TỰ ĐỘNG GỬI KẾT QUẢ VỀ GOOGLE SHEETS
  sendDataToAppsScript(total, correctCount, wrongCount, `${score10}/10 (${pct}%)`, timeStr, currentRecordId);
}"""

new_finish_end = """  showScreen('result-screen');

  // Cập nhật nút xem lại câu sai trên Result Screen
  const btnResReviewWrong = document.getElementById('btn-res-review-wrong');
  const btnResReviewWrongText = document.getElementById('btn-res-review-wrong-text');
  if (btnResReviewWrong) {
    if (wrongCount > 0) {
      btnResReviewWrong.style.display = 'flex';
      if (btnResReviewWrongText) {
        btnResReviewWrongText.textContent = isEn ? `XEM LẠI ${wrongCount} CÂU SAI ❌` : `XEM LẠI ${wrongCount} CÂU SAI ❌`;
      }
    } else {
      btnResReviewWrong.style.display = 'none';
    }
  }

  // 5. TỰ ĐỘNG GỬI KẾT QUẢ VỀ GOOGLE SHEETS
  sendDataToAppsScript(total, correctCount, wrongCount, `${score10}/10 (${pct}%)`, timeStr, currentRecordId);

  // 6. POPUP BÁO KẾT QUẢ BÀI THI RÕ RÀNG NGAY KHI NỘP BÀI (RESULT POPUP MODAL)
  setTimeout(() => {
    openQuizResultModal();
  }, 220);
}"""

if old_finish_end in content:
    content = content.replace(old_finish_end, new_finish_end)
    print("Updated submitAndFinishQuiz to trigger openQuizResultModal")
else:
    print("Warning: old_finish_end not found exactly")

# 3. Upgrade openReviewScreen, switchReviewMode, renderListReview, renderCardReview
old_review_block = """function openReviewScreen() {
  refreshLucideIcons();
  reviewFilter = 'all';
  reviewMode = 'list';
  reviewCardIndex = 0;

  document.getElementById('rev-count-all').textContent = sessionAnswers.length;
  document.getElementById('rev-count-correct').textContent = sessionAnswers.filter(a => a.isCorrect).length;
  document.getElementById('rev-count-wrong').textContent = sessionAnswers.filter(a => !a.isCorrect).length;

  document.querySelectorAll('.review-filter-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.review-filter-btn')[0].classList.add('active');

  applyReviewFilter();
  showScreen('review-screen');
}

function switchReviewMode(mode) {
  reviewMode = mode;
  document.getElementById('btn-view-list').classList.toggle('active', mode === 'list');
  document.getElementById('btn-view-card').classList.toggle('active', mode === 'card');

  document.getElementById('review-list-view').style.display = mode === 'list' ? 'block' : 'none';
  document.getElementById('review-card-view').style.display = mode === 'card' ? 'block' : 'none';

  if (mode === 'card') {
    reviewCardIndex = 0;
    renderCardReview();
  }
}

function filterReviewItems(filter, btn) {
  reviewFilter = filter;
  document.querySelectorAll('.review-filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  applyReviewFilter();
}

function applyReviewFilter() {
  if (reviewFilter === 'correct') {
    filteredReviewItems = sessionAnswers.filter(a => a.isCorrect);
  } else if (reviewFilter === 'wrong') {
    filteredReviewItems = sessionAnswers.filter(a => !a.isCorrect);
  } else {
    filteredReviewItems = [...sessionAnswers];
  }

  renderListReview();
  if (reviewMode === 'card') {
    reviewCardIndex = 0;
    renderCardReview();
  }
}

function renderListReview() {
  const container = document.getElementById('review-list-items');
  container.innerHTML = '';

  if (filteredReviewItems.length === 0) {
    container.innerHTML = '<div style="text-align:center; padding:20px; color:var(--text-muted);">Không có câu hỏi nào trong mục này.</div>';
    return;
  }

  filteredReviewItems.forEach((item, idx) => {
    const q = item.question;
    const card = document.createElement('div');
    card.className = `review-item-card ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;

    card.innerHTML = `
      <div class="review-card-header">
        <span>Câu ${idx + 1} (${q.topic} - Mức ${q.diff})</span>
        <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'};">
          ${item.isCorrect ? '✅ Đúng' : '❌ Chưa đúng'}
        </span>
      </div>
      <div class="review-q-text">
        ${currentLanguageMode === 'bilingual' ? `<div style="font-weight:800; margin-bottom:4px;">${q.q_en || q.q}</div><div style="font-size:0.92em; color:#475569;">${q.q}</div>` : (currentLanguageMode === 'en' ? (q.q_en || q.q) : q.q)}
      </div>
      <div class="review-answers-box">
        <div><strong>Bé đã chọn:</strong> <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">${item.userAnswerText}</span></div>
        ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>Đáp án đúng:</strong> <span style="color:var(--success); font-weight:700;">${getCorrectAnswerText(q)}</span></div>` : ''}
      </div>
      <div class="review-explain-box">
        <strong>💡 Giải thích:</strong> ${currentLanguageMode === 'bilingual' ? `<div><em>${q.explain_en || q.explain}</em></div><div style="margin-top:3px;">${q.explain}</div>` : (currentLanguageMode === 'en' ? (q.explain_en || q.explain) : q.explain)}
      </div>
    `;
    container.appendChild(card);
  });
}

function renderCardReview() {
  const container = document.getElementById('card-view-item');
  if (filteredReviewItems.length === 0) {
    container.innerHTML = '<div style="text-align:center; padding:20px; color:var(--text-muted);">Không có câu hỏi nào.</div>';
    return;
  }

  const item = filteredReviewItems[reviewCardIndex];
  const q = item.question;
  const total = filteredReviewItems.length;

  document.getElementById('card-nav-indicator').textContent = `Câu ${reviewCardIndex + 1} / ${total}`;

  container.className = `review-item-card ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;
  container.innerHTML = `
    <div class="review-card-header">
      <span>${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}</span>
      <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'};">
        ${item.isCorrect ? '✅ Trả lời Đúng' : '❌ Trả lời Sai'}
      </span>
    </div>
    ${q.img ? `<div class="question-img-card" style="margin-bottom:10px; height:140px;"><img src="${q.img}"></div>` : ''}
    <div class="review-q-text">${q.q}</div>
    <div class="review-answers-box">
      <div><strong>Bé chọn:</strong> <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">${item.userAnswerText}</span></div>
      ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>Đáp án đúng:</strong> <span style="color:var(--success); font-weight:700;">${getCorrectAnswerText(q)}</span></div>` : ''}
    </div>
    <div class="review-explain-box">
      <strong>💡 Vì sao lại thế nhỉ?</strong><br>${q.explain}
    </div>
  `;
}"""

new_review_block = """function openReviewScreen(filter = 'all', mode = 'list') {
  refreshLucideIcons();
  closeQuizResultModal();
  closeQuickNavModal();
  closeConfirmSubmitModal();

  reviewFilter = filter;
  reviewMode = mode;
  reviewCardIndex = 0;

  const totalAnswers = sessionAnswers.length;
  const correctAnswers = sessionAnswers.filter(a => a.isCorrect).length;
  const wrongAnswers = sessionAnswers.filter(a => !a.isCorrect).length;

  const countAll = document.getElementById('rev-count-all');
  if (countAll) countAll.textContent = totalAnswers;
  const countCorrect = document.getElementById('rev-count-correct');
  if (countCorrect) countCorrect.textContent = correctAnswers;
  const countWrong = document.getElementById('rev-count-wrong');
  if (countWrong) countWrong.textContent = wrongAnswers;

  // Active filter button
  document.querySelectorAll('.review-filter-btn').forEach(b => {
    b.classList.remove('active');
    const f = b.getAttribute('data-filter');
    if (f === filter) b.classList.add('active');
  });

  // Switch view mode
  switchReviewMode(mode);
  applyReviewFilter();
  showScreen('review-screen');
}

function switchReviewMode(mode) {
  reviewMode = mode;
  const btnList = document.getElementById('btn-view-list');
  const btnCard = document.getElementById('btn-view-card');
  if (btnList) btnList.classList.toggle('active', mode === 'list');
  if (btnCard) btnCard.classList.toggle('active', mode === 'card');

  const listView = document.getElementById('review-list-view');
  const cardView = document.getElementById('review-card-view');
  if (listView) listView.style.display = mode === 'list' ? 'block' : 'none';
  if (cardView) cardView.style.display = mode === 'card' ? 'block' : 'none';

  if (mode === 'card') {
    reviewCardIndex = 0;
    renderCardReview();
  } else {
    renderListReview();
  }
  refreshLucideIcons();
}

function filterReviewItems(filter, btn) {
  reviewFilter = filter;
  document.querySelectorAll('.review-filter-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  applyReviewFilter();
}

function applyReviewFilter() {
  if (reviewFilter === 'correct') {
    filteredReviewItems = sessionAnswers.filter(a => a.isCorrect);
  } else if (reviewFilter === 'wrong') {
    filteredReviewItems = sessionAnswers.filter(a => !a.isCorrect);
  } else {
    filteredReviewItems = [...sessionAnswers];
  }

  if (reviewMode === 'card') {
    reviewCardIndex = 0;
    renderCardReview();
  } else {
    renderListReview();
  }
}

function renderListReview() {
  const container = document.getElementById('review-list-items');
  if (!container) return;
  container.innerHTML = '';

  const isEn = (currentLanguageMode === 'en');
  const isBilingual = (currentLanguageMode === 'bilingual');

  if (filteredReviewItems.length === 0) {
    container.innerHTML = `<div style="text-align:center; padding:32px; color:var(--text-muted); font-weight:700;">${isEn ? 'No questions in this category.' : 'Không có câu hỏi nào trong mục này.'}</div>`;
    return;
  }

  filteredReviewItems.forEach((item, idx) => {
    const q = item.question;
    const card = document.createElement('div');
    card.className = `review-item-card ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;

    const topicText = isEn ? (TOPIC_EN_MAP[q.topic] || q.topic) : q.topic;
    const statusBadge = item.isCorrect 
      ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-100 text-emerald-800">${isEn ? '✅ Correct' : '✅ Trả lời Đúng'}</span>`
      : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-black bg-rose-100 text-rose-800">${isEn ? '❌ Incorrect' : '❌ Trả lời Sai'}</span>`;

    let qTextHtml = '';
    if (isBilingual) {
      qTextHtml = `<div class="font-extrabold text-slate-900 text-sm mb-1">${q.q_en || q.q}</div><div class="text-xs text-slate-600 font-medium">${q.q}</div>`;
    } else if (isEn) {
      qTextHtml = `<div class="font-extrabold text-slate-900 text-sm">${q.q_en || q.q}</div>`;
    } else {
      qTextHtml = `<div class="font-extrabold text-slate-900 text-sm">${q.q}</div>`;
    }

    const explainContent = isBilingual 
      ? `<div><em class="text-slate-800 font-medium">${q.explain_en || q.explain}</em></div><div class="text-slate-600 mt-1">${q.explain}</div>` 
      : (isEn ? (q.explain_en || q.explain) : q.explain);

    card.innerHTML = `
      <div class="review-card-header flex items-center justify-between pb-2 border-b border-slate-100">
        <span class="text-xs font-bold text-slate-700">${isEn ? 'Question' : 'Câu'} ${idx + 1} • ${topicText} (${isEn ? 'Level' : 'Mức'} ${q.diff || 1})</span>
        ${statusBadge}
      </div>
      <div class="review-q-text my-2.5">${qTextHtml}</div>
      <div class="review-answers-box bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 text-xs">
        <div><strong>${isEn ? 'Your choice:' : 'Bé đã chọn:'}</strong> <span style="color:${item.isCorrect ? '#059669' : '#E11D48'}; font-weight:800;">${item.userAnswerText}</span></div>
        ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>${isEn ? 'Correct answer:' : 'Đáp án đúng:'}</strong> <span style="color:#059669; font-weight:800;">${getCorrectAnswerText(q)}</span></div>` : ''}
      </div>
      <div class="review-explain-box mt-2 p-2.5 rounded-xl bg-cyan-50/70 border border-cyan-200/80 text-xs text-slate-700 leading-relaxed">
        <div class="font-black text-cyan-900 mb-0.5 flex items-center gap-1">
          <span>💡</span> <span>${isEn ? 'Scientific Explanation' : 'Giải thích khoa học:'}</span>
        </div>
        <div>${explainContent}</div>
      </div>
    `;
    container.appendChild(card);
  });
  refreshLucideIcons();
}

function renderCardReview() {
  const container = document.getElementById('card-view-item');
  if (!container) return;

  const isEn = (currentLanguageMode === 'en');
  const isBilingual = (currentLanguageMode === 'bilingual');

  if (filteredReviewItems.length === 0) {
    container.innerHTML = `<div style="text-align:center; padding:32px; color:var(--text-muted); font-weight:700;">${isEn ? 'No questions in this category.' : 'Không có câu hỏi nào trong mục này.'}</div>`;
    const indicator = document.getElementById('card-nav-indicator');
    if (indicator) indicator.textContent = '0 / 0';
    return;
  }

  if (reviewCardIndex < 0) reviewCardIndex = 0;
  if (reviewCardIndex >= filteredReviewItems.length) reviewCardIndex = filteredReviewItems.length - 1;

  const item = filteredReviewItems[reviewCardIndex];
  const q = item.question;
  const total = filteredReviewItems.length;

  const indicator = document.getElementById('card-nav-indicator');
  if (indicator) {
    indicator.textContent = isEn ? `Question ${reviewCardIndex + 1} / ${total}` : `Câu ${reviewCardIndex + 1} / ${total}`;
  }

  const topicText = isEn ? (TOPIC_EN_MAP[q.topic] || q.topic) : q.topic;
  const gradeText = isEn ? (q.grade ? `Grade ${q.grade}` : 'Elementary') : (q.grade ? `Lớp ${q.grade}` : 'Tiểu học');
  const diffText = isEn ? `Level ${q.diff || 1}` : `Mức ${q.diff || 1}`;
  const statusBadge = item.isCorrect 
    ? `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-100 text-emerald-800">${isEn ? '✅ Correct' : '✅ Trả lời Đúng'}</span>`
    : `<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-black bg-rose-100 text-rose-800">${isEn ? '❌ Incorrect' : '❌ Trả lời Sai'}</span>`;

  let qTextHtml = '';
  if (isBilingual) {
    qTextHtml = `<div class="font-extrabold text-slate-900 text-base mb-1">${q.q_en || q.q}</div><div class="text-xs text-slate-600 font-medium">${q.q}</div>`;
  } else if (isEn) {
    qTextHtml = `<div class="font-extrabold text-slate-900 text-base">${q.q_en || q.q}</div>`;
  } else {
    qTextHtml = `<div class="font-extrabold text-slate-900 text-base">${q.q}</div>`;
  }

  // Visual Multiple Choice 4 Options Cards
  let choicesHtml = '';
  if (q.type === 'MC') {
    const keys = ['A', 'B', 'C', 'D'];
    const opts = q.options || [q.a, q.b, q.c, q.d];
    const optsEn = q.options_en || [q.a_en || q.a, q.b_en || q.b, q.c_en || q.c, q.d_en || q.d];

    choicesHtml = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-2 my-3">';
    keys.forEach((key, kIdx) => {
      const optText = isEn ? optsEn[kIdx] : opts[kIdx];
      const isUserChoice = (item.userAnswerKey === key);
      const isCorrectChoice = (q.ans === key);

      let optClass = 'p-2.5 rounded-xl border text-xs font-bold flex items-center justify-between ';
      let badge = '';

      if (isCorrectChoice) {
        optClass += 'bg-emerald-50 border-emerald-400 text-emerald-950 shadow-xs ring-2 ring-emerald-300';
        badge = `<span class="text-[10px] font-black px-1.5 py-0.5 rounded bg-emerald-600 text-white shrink-0">${isEn ? 'Correct Answer' : 'Đáp án đúng'}</span>`;
      } else if (isUserChoice && !item.isCorrect) {
        optClass += 'bg-rose-50 border-rose-400 text-rose-950 shadow-xs ring-2 ring-rose-300';
        badge = `<span class="text-[10px] font-black px-1.5 py-0.5 rounded bg-rose-600 text-white shrink-0">${isEn ? 'Your Choice' : 'Bé đã chọn'}</span>`;
      } else {
        optClass += 'bg-slate-50/80 border-slate-200 text-slate-600';
      }

      choicesHtml += `
        <div class="${optClass}">
          <div class="flex items-center gap-2 pr-1">
            <span class="w-5 h-5 rounded-full ${isCorrectChoice ? 'bg-emerald-500 text-white' : (isUserChoice ? 'bg-rose-500 text-white' : 'bg-slate-200 text-slate-700')} flex items-center justify-center text-[10px] font-black shrink-0">${key}</span>
            <span class="leading-snug">${optText}</span>
          </div>
          ${badge}
        </div>
      `;
    });
    choicesHtml += '</div>';
  } else {
    choicesHtml = `
      <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 my-3 text-xs">
        <div><strong>${isEn ? 'Your choice:' : 'Bé đã nhập:'}</strong> <span style="color:${item.isCorrect ? '#059669' : '#E11D48'}; font-weight:800;">${item.userAnswerText}</span></div>
        ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>${isEn ? 'Correct answer:' : 'Đáp án đúng:'}</strong> <span style="color:#059669; font-weight:800;">${getCorrectAnswerText(q)}</span></div>` : ''}
      </div>
    `;
  }

  const explainContent = isBilingual 
    ? `<div><em class="text-slate-800 font-medium">${q.explain_en || q.explain}</em></div><div class="text-slate-600 mt-1">${q.explain}</div>` 
    : (isEn ? (q.explain_en || q.explain) : q.explain);

  container.className = `review-item-card ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;
  container.innerHTML = `
    <div class="review-card-header flex items-center justify-between pb-2 border-b border-slate-100">
      <span class="text-xs font-bold text-slate-600">${topicText} • ${gradeText} • ${diffText}</span>
      ${statusBadge}
    </div>
    ${q.img ? `<div class="question-img-card my-2.5 rounded-xl overflow-hidden border border-slate-200" style="max-height:160px;"><img src="${q.img}" style="width:100%; height:100%; object-fit:cover;" onerror="handleImgError(this)"></div>` : ''}
    <div class="review-q-text my-2.5">${qTextHtml}</div>
    ${choicesHtml}
    <div class="review-explain-box mt-3 p-3 rounded-xl bg-cyan-50/70 border border-cyan-200/80 text-xs text-slate-700 leading-relaxed">
      <div class="font-black text-cyan-900 mb-1 flex items-center gap-1">
        <span>💡</span> <span>${isEn ? 'Scientific Explanation' : 'Giải thích khoa học:'}</span>
      </div>
      <div>${explainContent}</div>
    </div>
  `;
  refreshLucideIcons();
}"""

if old_review_block in content:
    content = content.replace(old_review_block, new_review_block)
    print("Replaced review screen JS functions with enhanced versions")
else:
    print("Warning: old_review_block not found exactly")

# 4. Update applyLanguageToUI to include review & modal strings
old_lang_ui = "  const btnReviewDetailText = document.getElementById('btn-review-detail-text');"
new_lang_ui = """  // Review & Result Modal Translations
  const btnResReviewWrongText = document.getElementById('btn-res-review-wrong-text');
  if (btnResReviewWrongText) {
    const wCount = (typeof wrongList !== 'undefined') ? wrongList.length : 0;
    btnResReviewWrongText.textContent = isEn ? `REVIEW INCORRECT (${wCount}) ❌` : `XEM LẠI CÂU SAI (${wCount}) ❌`;
  }
  const btnResCardModeText = document.getElementById('btn-res-card-mode-text');
  if (btnResCardModeText) btnResCardModeText.textContent = isEn ? '🃏 One-by-One' : '🃏 Từng câu một';
  const btnReopenResText = document.getElementById('btn-reopen-result-modal-text');
  if (btnReopenResText) btnReopenResText.textContent = isEn ? 'Report Summary' : 'Báo cáo kết quả';

  const revScreenTitle = document.getElementById('rev-screen-title');
  if (revScreenTitle) revScreenTitle.textContent = isEn ? 'Detailed Question Review' : 'Xem Lại Chi Tiết Bài Làm';
  const revScreenSub = document.getElementById('rev-screen-subtitle');
  if (revScreenSub) revScreenSub.textContent = isEn ? 'Quickly review all questions or browse card-by-card' : 'Xem nhanh toàn bộ câu hỏi hoặc duyệt từng câu để ôn kỹ kiến thức';

  const btnViewListText = document.getElementById('btn-view-list-text');
  if (btnViewListText) btnViewListText.textContent = isEn ? '📑 List View' : '📑 Dạng danh sách';
  const btnViewCardText = document.getElementById('btn-view-card-text');
  if (btnViewCardText) btnViewCardText.textContent = isEn ? '🃏 One-by-One' : '🃏 Từng câu một';

  const revFilterAll = document.getElementById('rev-filter-all-label');
  if (revFilterAll) revFilterAll.textContent = isEn ? 'All' : 'Tất cả';
  const revFilterCorrect = document.getElementById('rev-filter-correct-label');
  if (revFilterCorrect) revFilterCorrect.textContent = isEn ? 'Correct ✅' : 'Đúng ✅';
  const revFilterWrong = document.getElementById('rev-filter-wrong-label');
  if (revFilterWrong) revFilterWrong.textContent = isEn ? 'Incorrect ❌' : 'Sai ❌';

  const cardBtnPrev = document.getElementById('card-btn-prev');
  if (cardBtnPrev) cardBtnPrev.textContent = isEn ? 'Previous' : 'Câu trước';
  const cardBtnNext = document.getElementById('card-btn-next');
  if (cardBtnNext) cardBtnNext.textContent = isEn ? 'Next' : 'Câu sau';

  const btnRevBackScore = document.getElementById('btn-rev-back-score-text');
  if (btnRevBackScore) btnRevBackScore.textContent = isEn ? 'Back to Scorecard' : 'Quay lại bảng điểm';
  const btnRevReplayWrong = document.getElementById('btn-rev-replay-wrong-text');
  if (btnRevReplayWrong) btnRevReplayWrong.textContent = isEn ? 'Practice Mistakes' : 'Ôn lại câu sai';
  const btnRevBackHome = document.getElementById('btn-rev-back-home-text');
  if (btnRevBackHome) btnRevBackHome.textContent = isEn ? 'Back to Lab' : 'Về Phòng Lab';

  const btnReviewDetailText = document.getElementById('btn-review-detail-text');"""

if old_lang_ui in content:
    content = content.replace(old_lang_ui, new_lang_ui)
    print("Added review and result modal translations into applyLanguageToUI")
else:
    print("Warning: old_lang_ui not found")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("JS logic applied successfully.")
