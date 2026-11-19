import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add .btn-3d-rose CSS
btn_3d_rose_css = """  .btn-3d-rose {
    background: linear-gradient(180deg, #F43F5E 0%, #E11D48 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #BE123C !important;
    border-bottom: 5px solid #9F1239 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 20px -4px rgba(244, 63, 94, 0.4) !important;
  }
  .btn-3d-rose:hover {
    filter: brightness(1.06);
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .btn-3d-rose:active {
    border-bottom-width: 1px !important;
    margin-top: 4px;
    transform: translateY(3px);
  }
"""

if ".btn-3d-rose" not in content:
    content = content.replace(".btn-3d-emerald:active {", btn_3d_rose_css + "\n  .btn-3d-emerald:active {")
    print("Added .btn-3d-rose CSS")

# 2. Update action-buttons on #result-screen
old_res_actions = """    <div class="action-buttons flex flex-col gap-3 my-4">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        <button type="button" class="btn-3d btn-3d-cyan py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" onclick="openReviewScreen()">
          <i data-lucide="eye" style="width:16px; height:16px;"></i>
          <span id="btn-review-detail-text">XEM LẠI CHI TIẾT BÀI LÀM</span>
        </button>
        <button type="button" class="btn-3d btn-3d-amber py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" onclick="openLeaderboardModal()">
          <i data-lucide="trophy" style="width:16px; height:16px;"></i>
          <span id="btn-view-stars-text">XEM BẢNG SAO TUẦN NÀY 🌟</span>
        </button>
      </div>

      <div class="flex items-center justify-center gap-2 flex-wrap">
        <button type="button" class="btn-3d btn-3d-purple py-2 px-3.5 text-xs font-bold" onclick="replayMistakes()" id="btn-replay-wrong">
          <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i>
          <span id="btn-replay-wrong-text">Ôn lại câu sai</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" onclick="launchFireworks()" title="Bắn pháo hoa ăn mừng">
          <span id="lead-fireworks-btn-text">🎊 Bắn Pháo Hoa</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:14px; height:14px;"></i>
          <span>Lịch Sử</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100" onclick="syncAllHistoryToSheets()">
          <i data-lucide="cloud" style="width:14px; height:14px;"></i>
          <span>Đồng bộ Sheets</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2 px-4 text-xs font-bold" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:14px; height:14px;"></i>
          <span>Về Phòng Lab</span>
        </button>
      </div>
    </div>"""

new_res_actions = """    <div class="action-buttons flex flex-col gap-3 my-4">
      <!-- Nút xem lại câu sai nổi bật & xem toàn bộ bài làm -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5" id="res-screen-primary-btns">
        <button type="button" class="btn-3d btn-3d-rose py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" id="btn-res-review-wrong" onclick="openReviewScreen('wrong', 'list')">
          <i data-lucide="alert-circle" style="width:16px; height:16px;"></i>
          <span id="btn-res-review-wrong-text">XEM LẠI CÂU SAI ❌</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" id="btn-res-review-all" onclick="openReviewScreen('all', 'list')">
          <i data-lucide="list-checks" style="width:16px; height:16px;"></i>
          <span id="btn-review-detail-text">XEM LẠI TOÀN BỘ BÀI LÀM</span>
        </button>
      </div>

      <div class="flex items-center justify-center gap-2 flex-wrap">
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="openReviewScreen('all', 'card')" title="Xem từng câu một kèm giải thích chi tiết">
          <i data-lucide="layers" style="width:14px; height:14px;"></i>
          <span id="btn-res-card-mode-text">🃏 Từng câu một</span>
        </button>
        <button type="button" class="btn-3d btn-3d-purple py-2 px-3.5 text-xs font-bold flex items-center gap-1.5" onclick="replayMistakes()" id="btn-replay-wrong">
          <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i>
          <span id="btn-replay-wrong-text">Ôn lại câu sai</span>
        </button>
        <button type="button" class="btn-3d btn-3d-amber py-2 px-3.5 text-xs font-bold shadow-xs flex items-center gap-1.5" onclick="openLeaderboardModal()">
          <i data-lucide="trophy" style="width:14px; height:14px;"></i>
          <span id="btn-view-stars-text">Bảng Sao 🌟</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="openQuizResultModal()" title="Mở lại bảng báo cáo kết quả">
          <i data-lucide="award" style="width:14px; height:14px;"></i>
          <span id="btn-reopen-result-modal-text">Báo cáo kết quả</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:14px; height:14px;"></i>
          <span>Lịch Sử</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2 px-4 text-xs font-bold flex items-center gap-1.5" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:14px; height:14px;"></i>
          <span>Về Phòng Lab</span>
        </button>
      </div>
    </div>"""

if old_res_actions in content:
    content = content.replace(old_res_actions, new_res_actions)
    print("Updated action-buttons on #result-screen")
else:
    print("Warning: old_res_actions not found")

# 3. Update #review-screen HTML
old_review_screen = """  <div class="quiz-card screen" id="review-screen">
    <div class="review-header-bar">
      <h3 style="font-size:1.25rem; font-weight:800;">🔍 Xem Lại Chi Tiết Bài Làm</h3>
      <div class="review-view-toggle">
        <button class="toggle-btn active" id="btn-view-list" onclick="switchReviewMode('list')">📑 Dạng danh sách</button>
        <button class="toggle-btn" id="btn-view-card" onclick="switchReviewMode('card')">🃏 Từng câu một</button>
      </div>
    </div>

    <div class="review-filters">
      <button class="review-filter-btn active" onclick="filterReviewItems('all', this)">Tất cả (<span id="rev-count-all">0</span>)</button>
      <button class="review-filter-btn" onclick="filterReviewItems('correct', this)">Đúng ✅ (<span id="rev-count-correct">0</span>)</button>
      <button class="review-filter-btn" onclick="filterReviewItems('wrong', this)">Sai ❌ (<span id="rev-count-wrong">0</span>)</button>
    </div>

    <div id="review-list-view">
      <div class="review-list-container" id="review-list-items"></div>
    </div>

    <div id="review-card-view" style="display:none;">
      <div class="review-item-card" id="card-view-item"></div>
      <div class="card-view-nav">
        <button class="control-btn" onclick="navCardReview(-1)">⬅️ Câu trước</button>
        <span id="card-nav-indicator" style="font-weight:700; font-size:0.9rem;">Câu 1/15</span>
        <button class="control-btn" onclick="navCardReview(1)">Câu sau ➡️</button>
      </div>
    </div>

    <div style="margin-top:16px;">
      <button class="btn-primary-action" style="width:100%;" onclick="showScreen('result-screen')">⬅️ Quay lại bảng điểm</button>
    </div>
  </div>"""

new_review_screen = """  <div class="quiz-card screen" id="review-screen">
    <div class="review-header-bar flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-200">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🔍</span>
        <div>
          <h3 class="font-baloo font-bold text-lg text-slate-900 leading-snug" id="rev-screen-title">Xem Lại Chi Tiết Bài Làm</h3>
          <p class="text-xs text-slate-500 font-medium" id="rev-screen-subtitle">Xem nhanh toàn bộ câu hỏi hoặc duyệt từng câu để ôn kỹ kiến thức</p>
        </div>
      </div>
      <div class="review-view-toggle bg-slate-200 p-1 rounded-xl flex items-center gap-1 shadow-inner">
        <button class="toggle-btn active px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5" id="btn-view-list" onclick="switchReviewMode('list')">
          <i data-lucide="list" style="width:14px; height:14px;"></i>
          <span id="btn-view-list-text">📑 Dạng danh sách</span>
        </button>
        <button class="toggle-btn px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5" id="btn-view-card" onclick="switchReviewMode('card')">
          <i data-lucide="layers" style="width:14px; height:14px;"></i>
          <span id="btn-view-card-text">🃏 Từng câu một</span>
        </button>
      </div>
    </div>

    <!-- Bộ lọc Tất cả / Câu đúng / Câu sai -->
    <div class="review-filters flex items-center gap-2 my-3 flex-wrap">
      <button class="review-filter-btn active" data-filter="all" onclick="filterReviewItems('all', this)">
        <span id="rev-filter-all-label">Tất cả</span> (<span id="rev-count-all">0</span>)
      </button>
      <button class="review-filter-btn" data-filter="correct" onclick="filterReviewItems('correct', this)" style="border-color:#A7F3D0; color:#047857;">
        <span id="rev-filter-correct-label">Đúng ✅</span> (<span id="rev-count-correct">0</span>)
      </button>
      <button class="review-filter-btn" data-filter="wrong" onclick="filterReviewItems('wrong', this)" style="border-color:#FECACA; color:#B91C1C; font-weight:800;">
        <span id="rev-filter-wrong-label">Sai ❌</span> (<span id="rev-count-wrong">0</span>)
      </button>
    </div>

    <!-- 1. Dạng danh sách (List View) -->
    <div id="review-list-view">
      <div class="review-list-container" id="review-list-items"></div>
    </div>

    <!-- 2. Dạng từng câu một (Card View) -->
    <div id="review-card-view" style="display:none;">
      <div id="card-view-item"></div>
      <div class="card-view-nav flex items-center justify-between mt-3.5 pt-3 border-t border-slate-200">
        <button class="control-btn px-3 py-1.5 text-xs font-bold flex items-center gap-1 rounded-xl bg-white border border-slate-300 text-slate-700 hover:bg-slate-50" onclick="navCardReview(-1)">
          <i data-lucide="chevron-left" style="width:15px; height:15px;"></i>
          <span id="card-btn-prev">Câu trước</span>
        </button>
        <span id="card-nav-indicator" class="font-baloo font-extrabold text-sm text-cyan-800 bg-cyan-50 border border-cyan-200 px-3 py-1 rounded-full">Câu 1/15</span>
        <button class="control-btn px-3 py-1.5 text-xs font-bold flex items-center gap-1 rounded-xl bg-white border border-slate-300 text-slate-700 hover:bg-slate-50" onclick="navCardReview(1)">
          <span id="card-btn-next">Câu sau</span>
          <i data-lucide="chevron-right" style="width:15px; height:15px;"></i>
        </button>
      </div>
    </div>

    <!-- Footer Controls -->
    <div class="mt-4 flex flex-wrap gap-2.5 justify-between items-center pt-3 border-t border-slate-200">
      <button type="button" class="btn-3d py-2.5 px-4 text-xs font-black bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 flex items-center gap-1.5" onclick="showScreen('result-screen')">
        <i data-lucide="arrow-left" style="width:16px; height:16px;"></i>
        <span id="btn-rev-back-score-text">Quay lại bảng điểm</span>
      </button>
      <div class="flex items-center gap-2 flex-wrap">
        <button type="button" class="btn-3d btn-3d-purple py-2.5 px-4 text-xs font-black flex items-center gap-1.5" id="btn-rev-replay-wrong" onclick="replayMistakes()">
          <i data-lucide="rotate-ccw" style="width:16px; height:16px;"></i>
          <span id="btn-rev-replay-wrong-text">Ôn lại câu sai</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2.5 px-4 text-xs font-black flex items-center gap-1.5" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:16px; height:16px;"></i>
          <span id="btn-rev-back-home-text">Về Phòng Lab</span>
        </button>
      </div>
    </div>
  </div>"""

if old_review_screen in content:
    content = content.replace(old_review_screen, new_review_screen)
    print("Updated #review-screen HTML structure")
else:
    print("Warning: old_review_screen not found")

# 4. Add #modal-quiz-result HTML
modal_quiz_result_html = """
<!-- =====================================================================
     MODAL POPUP BÁO KẾT QUẢ BÀI THI (RESULT POPUP MODAL)
     ===================================================================== -->
<div class="modal-overlay" id="modal-quiz-result">
  <div class="modal-box" style="max-width: 540px; padding: 22px; text-align: center; border-radius: 28px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); border: 3px solid #E0F2FE;">
    
    <!-- Top Close Button & Tag -->
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
      <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cyan-100 text-cyan-800 text-xs font-black" id="modal-res-tag">
        🎉 BÁO CÁO KẾT QUẢ BÀI THI
      </div>
      <button onclick="closeQuizResultModal()" style="background:#F1F5F9; border:none; width:32px; height:32px; border-radius:50%; font-size:16px; font-weight:bold; cursor:pointer; color:#64748B; display:flex; align-items:center; justify-content:center;">✕</button>
    </div>

    <!-- Trophy / Mascot Visual -->
    <div style="position:relative; display:inline-block; margin: 4px auto 10px;">
      <div id="modal-res-icon" style="font-size: 3.8rem; filter: drop-shadow(0 6px 16px rgba(245,158,11,0.35));" class="animate-bounce">🏆</div>
      <div id="modal-res-stars" style="font-size: 1.5rem; margin-top: -6px;">⭐⭐⭐</div>
    </div>

    <!-- Headline & Speech Feedback -->
    <h3 class="font-baloo font-black text-2xl text-slate-900 leading-tight" id="modal-res-title">
      Xuất sắc tuyệt đối!
    </h3>
    <p class="text-xs text-slate-500 font-medium mt-1 px-4" id="modal-res-desc">
      Bé đã hoàn thành xuất sắc lượt thi hôm nay!
    </p>

    <!-- Score & Metrics Cards -->
    <div class="grid grid-cols-4 gap-2 my-3.5 p-2.5 bg-slate-50 border border-slate-200/80 rounded-2xl text-center">
      <div class="p-1.5 bg-white rounded-xl shadow-xs border border-slate-100">
        <div class="text-[10px] font-extrabold text-slate-400 uppercase" id="modal-lbl-score">Điểm số</div>
        <div class="font-baloo font-black text-lg text-cyan-600 leading-snug" id="modal-res-score">10/10</div>
      </div>
      <div class="p-1.5 bg-white rounded-xl shadow-xs border border-emerald-100">
        <div class="text-[10px] font-extrabold text-emerald-600 uppercase" id="modal-lbl-correct">Đúng ✅</div>
        <div class="font-baloo font-black text-lg text-emerald-600 leading-snug" id="modal-res-correct">15</div>
      </div>
      <div class="p-1.5 bg-white rounded-xl shadow-xs border border-rose-100">
        <div class="text-[10px] font-extrabold text-rose-500 uppercase" id="modal-lbl-wrong">Sai ❌</div>
        <div class="font-baloo font-black text-lg text-rose-500 leading-snug" id="modal-res-wrong">0</div>
      </div>
      <div class="p-1.5 bg-white rounded-xl shadow-xs border border-amber-100">
        <div class="text-[10px] font-extrabold text-amber-600 uppercase" id="modal-lbl-time">Thời gian</div>
        <div class="font-baloo font-black text-lg text-amber-600 leading-snug" id="modal-res-time">02:30</div>
      </div>
    </div>

    <!-- Mascot Encouragement Box -->
    <div class="bg-cyan-50/70 border border-cyan-200 rounded-xl p-2.5 mb-3.5 text-left flex items-center gap-3">
      <div id="modal-mascot-avatar" style="font-size:1.8rem; flex-shrink:0;">🦉</div>
      <div class="text-xs text-cyan-900 font-bold leading-relaxed" id="modal-mascot-speech">
        "Tuyệt vời quá bạn ơi! Tớ rất tự hào về bạn hôm nay! 🎉"
      </div>
    </div>

    <!-- Quick Action Buttons -->
    <div class="flex flex-col gap-2.5">
      <!-- Row 1: Review Wrong Questions (If wrong > 0) + Review All -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="modal-review-actions-row">
        <button type="button" class="btn-3d btn-3d-rose py-2.5 px-3 text-xs font-black shadow-sm flex items-center justify-center gap-1.5" id="btn-modal-review-wrong" onclick="openReviewScreen('wrong', 'list')">
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
        <button type="button" class="btn-3d py-2 px-2.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1" onclick="openReviewScreen(wrongList.length > 0 ? 'wrong' : 'all', 'card')" title="Xem chi tiết từng câu dạng thẻ lật">
          <i data-lucide="layers" style="width:14px; height:14px;"></i>
          <span id="btn-modal-card-mode-text">🃏 Từng câu một</span>
        </button>
        <button type="button" class="btn-3d btn-3d-purple py-2 px-2.5 text-xs font-bold flex items-center justify-center gap-1" id="btn-modal-replay-wrong" onclick="replayMistakesFromModal()">
          <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i>
          <span id="btn-modal-replay-wrong-text">Ôn câu sai</span>
        </button>
        <button type="button" class="btn-3d btn-3d-amber py-2 px-2.5 text-xs font-bold flex items-center justify-center gap-1 col-span-2 sm:col-span-1" onclick="openLeaderboardFromModal()">
          <i data-lucide="trophy" style="width:14px; height:14px;"></i>
          <span id="btn-modal-lead-text">Bảng Sao 🌟</span>
        </button>
      </div>

      <!-- Row 3: Return to Lab / Home -->
      <button type="button" class="btn-3d py-2 px-4 text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 flex items-center justify-center gap-1.5 rounded-xl mt-0.5" onclick="closeQuizResultModal()">
        <i data-lucide="arrow-right" style="width:14px; height:14px;"></i>
        <span id="btn-modal-back-home-text">Đóng & Xem Bảng Điểm Chi Tiết ➔</span>
      </button>
    </div>

  </div>
</div>
"""

if "id=\"modal-quiz-result\"" not in content:
    content = content.replace("<!-- MODAL QUICK REVIEW: XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP) -->", modal_quiz_result_html + "\n<!-- MODAL QUICK REVIEW: XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP) -->")
    print("Added #modal-quiz-result HTML")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML template additions complete.")
