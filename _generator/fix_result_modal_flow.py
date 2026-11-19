import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Enhance CSS for .modal-overlay and .modal-box
target_modal_css = """  /* MODALS */
  .modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    padding: 20px;
  }
  .modal-overlay.active { display: flex; }"""

repl_modal_css = """  /* MODALS */
  .modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 99999 !important;
    padding: 16px;
    overflow-y: auto;
  }
  .modal-overlay.active {
    display: flex !important;
    opacity: 1 !important;
    visibility: visible !important;
  }"""

if target_modal_css in html:
    html = html.replace(target_modal_css, repl_modal_css)
    print("1. Modal CSS updated successfully.")
else:
    print("Warning: target_modal_css not found.")

# 2. Add quiz-pre-review-wrap under btn-next in quiz-screen
target_btn_next = """        <div class="pt-2 w-full">
          <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer" id="btn-next" onclick="goNextQuestion()">
            <span id="btn-next-text">TIẾP TỤC HÀNH TRÌNH</span>
            <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
          </button>
        </div>"""

repl_btn_next = """        <div class="pt-2 w-full">
          <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer" id="btn-next" onclick="goNextQuestion()">
            <span id="btn-next-text">TIẾP TỤC HÀNH TRÌNH</span>
            <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
          </button>
          <div class="text-center mt-2.5" id="quiz-pre-review-wrap" style="display:none;">
            <button type="button" class="text-xs font-bold text-slate-500 hover:text-cyan-700 transition inline-flex items-center gap-1 cursor-pointer bg-transparent border-0" onclick="openReviewBeforeSubmit()">
              <i data-lucide="clipboard-list" style="width:14px; height:14px;"></i>
              <span id="quiz-pre-review-text">🔍 Xem lại các câu vừa làm trước khi nộp</span>
            </button>
          </div>
        </div>"""

if target_btn_next in html:
    html = html.replace(target_btn_next, repl_btn_next)
    print("2. Added quiz-pre-review-wrap successfully.")
else:
    print("Warning: target_btn_next not found.")

# 3. Update displayQuestion for btnNext and isLast
target_display_next = """      if (isLast) {
        btnNext.innerHTML = isEn 
          ? '<i data-lucide="list-checks" style="width:18px; height:18px; stroke-width:2.5;"></i> <span id="btn-next-text">Review & Submit</span>'
          : '<i data-lucide="list-checks" style="width:18px; height:18px; stroke-width:2.5;"></i> <span id="btn-next-text">Xem lại & Nộp bài</span>';
        btnNext.classList.add('btn-last-step');
        btnNext.onclick = openReviewBeforeSubmit;
      } else {
        btnNext.innerHTML = isEn
          ? '<span id="btn-next-text">Next Question</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>'
          : '<span id="btn-next-text">Câu tiếp theo</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>';
        btnNext.classList.remove('btn-last-step');
        btnNext.onclick = goNextQuestion;
      }"""

repl_display_next = """      if (isLast) {
        btnNext.innerHTML = isEn 
          ? '<i data-lucide="send" style="width:18px; height:18px; stroke-width:2.5;"></i> <span id="btn-next-text">Submit & View Results 🚀</span>'
          : '<i data-lucide="send" style="width:18px; height:18px; stroke-width:2.5;"></i> <span id="btn-next-text">Nộp Bài & Xem Điểm 🚀</span>';
        btnNext.className = 'btn-3d btn-3d-emerald w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer btn-last-step visible';
        btnNext.onclick = submitAndFinishQuiz;
        const preRev = document.getElementById('quiz-pre-review-wrap');
        if (preRev) preRev.style.display = 'block';
      } else {
        btnNext.innerHTML = isEn
          ? '<span id="btn-next-text">Next Question</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>'
          : '<span id="btn-next-text">Câu tiếp theo</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>';
        btnNext.className = 'btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer';
        if (userAnswersMap && userAnswersMap[q.id]) {
          btnNext.classList.add('visible');
        } else {
          btnNext.classList.remove('visible');
        }
        btnNext.onclick = goNextQuestion;
        const preRev = document.getElementById('quiz-pre-review-wrap');
        if (preRev) preRev.style.display = 'none';
      }"""

if target_display_next in html:
    html = html.replace(target_display_next, repl_display_next)
    print("3. Updated displayQuestion btnNext isLast successfully.")
else:
    print("Warning: target_display_next not found.")

# 4. Update goNextQuestion
target_gonext = """function goNextQuestion() {
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
}"""

repl_gonext = """function goNextQuestion() {
  if (currentIndex === currentDeck.length - 1) {
    submitAndFinishQuiz();
    return;
  }
  currentIndex++;
  if (currentIndex < currentDeck.length) {
    displayQuestion();
  } else {
    submitAndFinishQuiz();
  }
}"""

if target_gonext in html:
    html = html.replace(target_gonext, repl_gonext)
    print("4. Updated goNextQuestion successfully.")
else:
    print("Warning: target_gonext not found.")

# 5. In submitAndFinishQuiz, trigger openQuizResultModal immediately
target_submit_timeout = """  // 6. POPUP BÁO KẾT QUẢ BÀI THI RÕ RÀNG NGAY KHI NỘP BÀI (RESULT POPUP MODAL)
  setTimeout(() => {
    openQuizResultModal();
  }, 220);"""

repl_submit_timeout = """  // 6. POPUP BÁO KẾT QUẢ BÀI THI RÕ RÀNG NGAY KHI NỘP BÀI (RESULT POPUP MODAL)
  openQuizResultModal();"""

if target_submit_timeout in html:
    html = html.replace(target_submit_timeout, repl_submit_timeout)
    print("5. Trigger openQuizResultModal immediately updated.")
else:
    print("Warning: target_submit_timeout not found.")

# 6. Update openQuizResultModal to force style.display='flex' and mascot avatar
target_open_modal = """function openQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (!modal) return;
  refreshLucideIcons();
  modal.classList.add('active');"""

repl_open_modal = """function openQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (!modal) return;
  modal.style.display = 'flex';
  modal.classList.add('active');
  refreshLucideIcons();"""

if target_open_modal in html:
    html = html.replace(target_open_modal, repl_open_modal)
    print("6. openQuizResultModal forced style.display updated.")
else:
    print("Warning: target_open_modal not found.")

# 7. Update closeQuizResultModal
target_close_modal = """function closeQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (modal) modal.classList.remove('active');
}"""

repl_close_modal = """function closeQuizResultModal() {
  const modal = document.getElementById('modal-quiz-result');
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
  }
  showScreen('result-screen');
}

function openWrongReviewFromModal() {
  closeQuizResultModal();
  openReviewScreen('wrong', 'list');
}

function openAllReviewFromModal() {
  closeQuizResultModal();
  openReviewScreen('all', 'list');
}

function openCardReviewFromModal() {
  closeQuizResultModal();
  const filter = (wrongList && wrongList.length > 0) ? 'wrong' : 'all';
  openReviewScreen(filter, 'card');
}"""

if target_close_modal in html:
    html = html.replace(target_close_modal, repl_close_modal)
    print("7. closeQuizResultModal and modal review handlers updated.")
else:
    print("Warning: target_close_modal not found.")

# 8. Update button onclicks in modal-quiz-result HTML
target_modal_buttons = """        <button type="button" class="btn-3d btn-3d-rose py-2.5 px-3 text-xs font-black shadow-sm flex items-center justify-center gap-1.5" id="btn-modal-review-wrong" onclick="openReviewScreen('wrong', 'list')">
          <i data-lucide="alert-circle" style="width:15px; height:15px;"></i>
          <span id="btn-modal-review-wrong-text">❌ Xem Lại Câu Sai</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2.5 px-3 text-xs font-black shadow-sm flex items-center justify-center gap-1.5" id="btn-modal-review-all" onclick="openReviewScreen('all', 'list')">
          <i data-lucide="list-checks" style="width:15px; height:15px;"></i>
          <span id="btn-modal-review-all-text">📑 Xem Toàn Bộ Bài Làm</span>
        </button>
      </div>

      <!-- Row 2: Card Mode Quick Review + Play Again / Replay Mistakes -->
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button type="button" class="btn-3d py-2 px-2.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1" onclick="openReviewScreen(wrongList.length > 0 ? 'wrong' : 'all', 'card')" title="Xem chi tiết từng câu dạng thẻ lật">"""

repl_modal_buttons = """        <button type="button" class="btn-3d btn-3d-rose py-2.5 px-3 text-xs font-black shadow-sm flex items-center justify-center gap-1.5" id="btn-modal-review-wrong" onclick="openWrongReviewFromModal()">
          <i data-lucide="alert-circle" style="width:15px; height:15px;"></i>
          <span id="btn-modal-review-wrong-text">❌ Xem Lại Câu Sai</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2.5 px-3 text-xs font-black shadow-sm flex items-center justify-center gap-1.5" id="btn-modal-review-all" onclick="openAllReviewFromModal()">
          <i data-lucide="list-checks" style="width:15px; height:15px;"></i>
          <span id="btn-modal-review-all-text">📑 Xem Toàn Bộ Bài Làm</span>
        </button>
      </div>

      <!-- Row 2: Card Mode Quick Review + Play Again / Replay Mistakes -->
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button type="button" class="btn-3d py-2 px-2.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1" onclick="openCardReviewFromModal()" title="Xem chi tiết từng câu dạng thẻ lật">"""

if target_modal_buttons in html:
    html = html.replace(target_modal_buttons, repl_modal_buttons)
    print("8. modal-quiz-result button handlers updated.")
else:
    print("Warning: target_modal_buttons not found.")

# 9. Update applyLanguageToUI for quiz-pre-review-text
target_lang_pre = """  // Review Screen
  const revScreenTitle = document.getElementById('rev-screen-title');"""

repl_lang_pre = """  const quizPreRevText = document.getElementById('quiz-pre-review-text');
  if (quizPreRevText) quizPreRevText.textContent = isEn ? '🔍 Review answers before submitting' : '🔍 Xem lại các câu vừa làm trước khi nộp';

  // Review Screen
  const revScreenTitle = document.getElementById('rev-screen-title');"""

if target_lang_pre in html:
    html = html.replace(target_lang_pre, repl_lang_pre)
    print("9. applyLanguageToUI quizPreRevText updated.")
else:
    print("Warning: target_lang_pre not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished applying fix_result_modal_flow.py!")
