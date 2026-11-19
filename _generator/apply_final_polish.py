import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update button text in result screen buttons (lines 4616-4623)
target_result_btns = """        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:14px; height:14px;"></i>
          <span>Lịch Sử</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2 px-4 text-xs font-bold flex items-center gap-1.5" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:14px; height:14px;"></i>
          <span>Về Phòng Lab</span>
        </button>"""

repl_result_btns = """        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:14px; height:14px;"></i>
          <span id="btn-res-hist-text">Lịch Sử</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2 px-4 text-xs font-bold flex items-center gap-1.5" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:14px; height:14px;"></i>
          <span id="btn-res-home-text">Về Phòng Lab</span>
        </button>"""

if target_result_btns in html:
    html = html.replace(target_result_btns, repl_result_btns)
    print("Updated result screen history & home buttons successfully.")
else:
    print("Warning: target_result_btns not found.")

# 2. Fix submitAndFinishQuiz line 7393
target_wrong_txt = """      if (btnResReviewWrongText) {
        btnResReviewWrongText.textContent = isEn ? `XEM LẠI ${wrongCount} CÂU SAI ❌` : `XEM LẠI ${wrongCount} CÂU SAI ❌`;
      }"""

repl_wrong_txt = """      if (btnResReviewWrongText) {
        btnResReviewWrongText.textContent = isEn ? `REVIEW ${wrongCount} MISTAKE${wrongCount > 1 ? 'S' : ''} ❌` : `XEM LẠI ${wrongCount} CÂU SAI ❌`;
      }"""

if target_wrong_txt in html:
    html = html.replace(target_wrong_txt, repl_wrong_txt)
    print("Fixed submitAndFinishQuiz wrongCount English text successfully.")
else:
    print("Warning: target_wrong_txt not found.")

# 3. Add thorough translations into applyLanguageToUI
target_lang_block = """  const btnReviewDetail = document.getElementById('btn-review-detail-text');
  if (btnReviewDetail) btnReviewDetail.textContent = isEn ? 'REVIEW QUIZ ANSWERS' : 'XEM LẠI CHI TIẾT BÀI LÀM';
  const btnViewStars = document.getElementById('btn-view-stars-text');
  if (btnViewStars) btnViewStars.textContent = isEn ? 'VIEW STARS HALL 🌟' : 'XEM BẢNG SAO TUẦN NÀY 🌟';
  const btnReplayWrong = document.getElementById('btn-replay-wrong-text');
  if (btnReplayWrong) btnReplayWrong.textContent = isEn ? 'Practice Wrong Answers' : 'Ôn lại câu sai';"""

repl_lang_block = """  const btnReviewDetail = document.getElementById('btn-review-detail-text');
  if (btnReviewDetail) btnReviewDetail.textContent = isEn ? 'REVIEW QUIZ ANSWERS' : 'XEM LẠI CHI TIẾT BÀI LÀM';
  const btnViewStars = document.getElementById('btn-view-stars-text');
  if (btnViewStars) btnViewStars.textContent = isEn ? 'VIEW STARS HALL 🌟' : 'XEM BẢNG SAO TUẦN NÀY 🌟';
  const btnReplayWrong = document.getElementById('btn-replay-wrong-text');
  if (btnReplayWrong) btnReplayWrong.textContent = isEn ? 'Practice Wrong Answers' : 'Ôn lại câu sai';

  // 5b. Result Screen & Modals Enhanced Bilingual Translation
  const btnResReviewWrongText = document.getElementById('btn-res-review-wrong-text');
  if (btnResReviewWrongText) {
    const wrongCount = (typeof wrongList !== 'undefined' && wrongList) ? wrongList.length : 0;
    btnResReviewWrongText.textContent = isEn ? `REVIEW ${wrongCount > 0 ? wrongCount + ' ' : ''}MISTAKES ❌` : `XEM LẠI ${wrongCount > 0 ? wrongCount + ' ' : ''}CÂU SAI ❌`;
  }
  const btnResCardMode = document.getElementById('btn-res-card-mode-text');
  if (btnResCardMode) btnResCardMode.textContent = isEn ? '🃏 One-by-One' : '🃏 Từng câu một';
  const btnReopenResModal = document.getElementById('btn-reopen-result-modal-text');
  if (btnReopenResModal) btnReopenResModal.textContent = isEn ? 'Result Report' : 'Báo cáo kết quả';
  const btnResHist = document.getElementById('btn-res-hist-text');
  if (btnResHist) btnResHist.textContent = isEn ? 'History' : 'Lịch Sử';
  const btnResHome = document.getElementById('btn-res-home-text');
  if (btnResHome) btnResHome.textContent = isEn ? 'Home Lab' : 'Về Phòng Lab';
  const syncStatus = document.getElementById('sync-status');
  if (syncStatus) syncStatus.textContent = isEn ? '💡 Quiz results and history automatically saved to local storage' : '💡 Lịch sử câu hỏi đã tự động cập nhật vào trí nhớ của máy';

  // Result Popup Modal
  const modalResTag = document.getElementById('modal-res-tag');
  if (modalResTag) modalResTag.textContent = isEn ? '🎉 MISSION REPORT' : '🎉 BÁO CÁO KẾT QUẢ BÀI THI';
  const modalLblScore = document.getElementById('modal-lbl-score');
  if (modalLblScore) modalLblScore.textContent = isEn ? 'Score' : 'Điểm số';
  const modalLblCorrect = document.getElementById('modal-lbl-correct');
  if (modalLblCorrect) modalLblCorrect.textContent = isEn ? 'Correct ✅' : 'Đúng ✅';
  const modalLblWrong = document.getElementById('modal-lbl-wrong');
  if (modalLblWrong) modalLblWrong.textContent = isEn ? 'Wrong ❌' : 'Sai ❌';
  const modalLblTime = document.getElementById('modal-lbl-time');
  if (modalLblTime) modalLblTime.textContent = isEn ? 'Time' : 'Thời gian';
  const btnModalReviewWrong = document.getElementById('btn-modal-review-wrong-text');
  if (btnModalReviewWrong) {
    const wrongCount = (typeof wrongList !== 'undefined' && wrongList) ? wrongList.length : 0;
    btnModalReviewWrong.textContent = isEn ? `❌ Review ${wrongCount} Mistake${wrongCount > 1 ? 's' : ''}` : `❌ Xem Lại ${wrongCount} Câu Sai`;
  }
  const btnModalReviewAll = document.getElementById('btn-modal-review-all-text');
  if (btnModalReviewAll) btnModalReviewAll.textContent = isEn ? '📑 Review All Answers' : '📑 Xem Toàn Bộ Bài Làm';
  const btnModalCardMode = document.getElementById('btn-modal-card-mode-text');
  if (btnModalCardMode) btnModalCardMode.textContent = isEn ? '🃏 One-by-One' : '🃏 Từng câu một';
  const btnModalReplayWrong = document.getElementById('btn-modal-replay-wrong-text');
  if (btnModalReplayWrong) btnModalReplayWrong.textContent = isEn ? 'Practice Mistakes' : 'Ôn câu sai';
  const btnModalLead = document.getElementById('btn-modal-lead-text');
  if (btnModalLead) btnModalLead.textContent = isEn ? 'Stars 🌟' : 'Bảng Sao 🌟';
  const btnModalBackHome = document.getElementById('btn-modal-back-home-text');
  if (btnModalBackHome) btnModalBackHome.textContent = isEn ? 'Close & View Detailed Scorecard ➔' : 'Đóng & Xem Bảng Điểm Chi Tiết ➔';

  // Review Screen
  const revScreenTitle = document.getElementById('rev-screen-title');
  if (revScreenTitle) revScreenTitle.textContent = isEn ? 'Answer Review & Explanations' : 'Xem Lại Chi Tiết Bài Làm';
  const revScreenSubtitle = document.getElementById('rev-screen-subtitle');
  if (revScreenSubtitle) revScreenSubtitle.textContent = isEn ? 'Quick list review or step through one-by-one to master every concept' : 'Xem nhanh toàn bộ câu hỏi hoặc duyệt từng câu để ôn kỹ kiến thức';
  const btnViewListText = document.getElementById('btn-view-list-text');
  if (btnViewListText) btnViewListText.textContent = isEn ? '📑 List View' : '📑 Dạng danh sách';
  const btnViewCardText = document.getElementById('btn-view-card-text');
  if (btnViewCardText) btnViewCardText.textContent = isEn ? '🃏 Card View' : '🃏 Từng câu một';
  const revFilterAllLabel = document.getElementById('rev-filter-all-label');
  if (revFilterAllLabel) revFilterAllLabel.textContent = isEn ? 'All' : 'Tất cả';
  const revFilterCorrectLabel = document.getElementById('rev-filter-correct-label');
  if (revFilterCorrectLabel) revFilterCorrectLabel.textContent = isEn ? 'Correct ✅' : 'Đúng ✅';
  const revFilterWrongLabel = document.getElementById('rev-filter-wrong-label');
  if (revFilterWrongLabel) revFilterWrongLabel.textContent = isEn ? 'Wrong ❌' : 'Sai ❌';
  const cardBtnPrev = document.getElementById('card-btn-prev');
  if (cardBtnPrev) cardBtnPrev.textContent = isEn ? 'Previous' : 'Câu trước';
  const cardBtnNext = document.getElementById('card-btn-next');
  if (cardBtnNext) cardBtnNext.textContent = isEn ? 'Next' : 'Câu sau';
  const btnRevBackScore = document.getElementById('btn-rev-back-score-text');
  if (btnRevBackScore) btnRevBackScore.textContent = isEn ? 'Back to Scorecard' : 'Quay lại bảng điểm';
  const btnRevReplayWrong = document.getElementById('btn-rev-replay-wrong-text');
  if (btnRevReplayWrong) btnRevReplayWrong.textContent = isEn ? 'Practice Wrong Answers' : 'Ôn lại câu sai';
  const btnRevBackHome = document.getElementById('btn-rev-back-home-text');
  if (btnRevBackHome) btnRevBackHome.textContent = isEn ? 'Home Lab' : 'Về Phòng Lab';

  // If review screen is currently visible, refresh its items
  const revScreenEl = document.getElementById('review-screen');
  if (revScreenEl && revScreenEl.classList.contains('active') && typeof applyReviewFilter === 'function') {
    applyReviewFilter();
  }"""

if target_lang_block in html:
    html = html.replace(target_lang_block, repl_lang_block)
    print("Added bilingual translations into applyLanguageToUI successfully.")
else:
    print("Warning: target_lang_block not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished applying final polish.")
