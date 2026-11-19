#!/usr/bin/env python3
"""
Fix 3 issues requested by user:
1. Centered pill and bright white/cyan text for:
   "THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM" + Fix black question text in bilingual mode
2. Button "Câu tiếp theo" no longer sticky overlapping option D (normal document flow with generous spacing)
3. Prominent Quit/Thoát button with confirmation modal -> returns to Home
"""

import re
import sys

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# =========================================================================
# 1. UPGRADE TOP MISSION HEADER IN QUIZ-SCREEN (ADD PROMINENT THOÁT BUTTON)
# =========================================================================
old_top_header = """    <!-- TOP MISSION HEADER (CHẾ ĐỘ THÁM HIỂM VŨ TRỤ) -->
    <div class="flex items-center justify-between gap-3 mb-4 shrink-0 flex-wrap">
      
      <div class="flex items-center gap-2">
        <button type="button" onclick="askQuitQuiz()" class="w-9 h-9 rounded-full bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 shadow-sm transition" title="Quay lại Phòng Lab">
          <i data-lucide="x" style="width:18px; height:18px; stroke-width:3;"></i>
        </button>
        <button type="button" onclick="pauseQuiz()" class="px-3 py-1.5 rounded-full bg-white border border-slate-200 text-xs font-bold text-slate-600 hover:bg-slate-100 shadow-sm transition flex items-center gap-1">
          <i data-lucide="pause" style="width:14px; height:14px;"></i>
          <span>Tạm dừng</span>
        </button>
      </div>"""

new_top_header = """    <!-- TOP MISSION HEADER (CHẾ ĐỘ THÁM HIỂM VŨ TRỤ) -->
    <div class="flex items-center justify-between gap-3 mb-4 shrink-0 flex-wrap">
      
      <div class="flex items-center gap-2">
        <button type="button" onclick="askQuitQuiz()" class="px-3.5 py-1.5 rounded-full bg-rose-50 border-2 border-rose-300 hover:bg-rose-100 text-rose-700 text-xs font-black flex items-center gap-1.5 shadow-xs transition cursor-pointer" title="Dừng bài thi để về Trang Chủ">
          <i data-lucide="log-out" style="width:14px; height:14px; stroke-width:2.5;"></i>
          <span>Thoát</span>
        </button>
        <button type="button" onclick="pauseQuiz()" class="px-3 py-1.5 rounded-full bg-white border border-slate-200 text-xs font-bold text-slate-600 hover:bg-slate-100 shadow-sm transition flex items-center gap-1">
          <i data-lucide="pause" style="width:14px; height:14px;"></i>
          <span>Tạm dừng</span>
        </button>
      </div>"""

if old_top_header in text:
    text = text.replace(old_top_header, new_top_header)
    print("Upgraded top header with prominent Thoát button.")

# =========================================================================
# 2. FIX QUESTION CARD: CENTERED BADGE + CLEAN LAYOUT
# =========================================================================
old_cosmic_card = """    <!-- DEEP COSMIC QUESTION CARD (FIGMA AI SCREEN 2 QUESTION CARD) -->
    <div class="bg-gradient-to-b from-indigo-950 to-slate-900 text-white rounded-3xl p-5 md:p-6 border-2 border-indigo-800/60 shadow-xl relative overflow-hidden mb-4">
      <div class="relative z-10 flex flex-col gap-2.5">
        <span class="text-[10px] font-black tracking-widest text-cyan-400 uppercase">THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM</span>
        <h2 class="font-baloo text-lg md:text-xl font-bold leading-snug text-white" id="question-text">
          Đang tải nội dung câu hỏi...
        </h2>
        <div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm" id="q-img-wrap" style="display:none;">
          <img id="question-img" src="" alt="Minh họa" style="width:100%; max-height:220px; object-fit:contain; display:block; margin:0 auto;">
        </div>
      </div>
      
      <!-- Watermark Saturn Icon -->
      <div class="absolute -right-4 -bottom-4 text-7xl opacity-20 pointer-events-none select-none">
        🪐
      </div>
    </div>"""

new_cosmic_card = """    <!-- DEEP COSMIC QUESTION CARD (FIGMA AI SCREEN 2 QUESTION CARD) -->
    <div class="bg-gradient-to-b from-indigo-950 to-slate-900 text-white rounded-3xl p-5 md:p-6 border-2 border-indigo-800/60 shadow-xl relative overflow-hidden mb-4">
      <div class="relative z-10 flex flex-col gap-3">
        <!-- Huy hiệu thể loại ở chính giữa thẻ -->
        <div class="flex items-center justify-center text-center">
          <span class="inline-flex items-center justify-center text-[11px] font-black tracking-wider text-cyan-300 bg-cyan-950/80 border border-cyan-400/40 px-3.5 py-1 rounded-full uppercase shadow-xs">
            ✨ THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM ✨
          </span>
        </div>
        <h2 class="font-baloo text-lg md:text-xl font-bold leading-snug text-white text-center md:text-left" id="question-text">
          Đang tải nội dung câu hỏi...
        </h2>
        <div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm mx-auto" id="q-img-wrap" style="display:none;">
          <img id="question-img" src="" alt="Minh họa" style="width:100%; max-height:200px; object-fit:contain; display:block; margin:0 auto;">
        </div>
      </div>
      
      <!-- Watermark Saturn Icon -->
      <div class="absolute -right-4 -bottom-4 text-7xl opacity-20 pointer-events-none select-none">
        🪐
      </div>
    </div>"""

if old_cosmic_card in text:
    text = text.replace(old_cosmic_card, new_cosmic_card)
    print("Upgraded cosmic card with centered badge.")

# =========================================================================
# 3. FIX BOTTOM BUTTON OVERLAPPING OPTION D (NO MORE STICKY OVER OPTIONS)
# =========================================================================
old_sticky_btn = """    <!-- BOTTOM ACTION BUTTON -->
    <div class="sticky bottom-2 z-20">
      <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl" id="btn-next" onclick="goNextQuestion()">
        <span>TIẾP TỤC HÀNH TRÌNH</span>
        <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
      </button>
    </div>"""

new_flow_btn = """    <!-- BOTTOM ACTION BUTTON (KHÔNG STICKY ĐÈ LÊN ĐÁP ÁN D) -->
    <div class="mt-6 mb-2 w-full">
      <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer" id="btn-next" onclick="goNextQuestion()">
        <span>TIẾP TỤC HÀNH TRÌNH</span>
        <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
      </button>
    </div>"""

if old_sticky_btn in text:
    text = text.replace(old_sticky_btn, new_flow_btn)
    print("Replaced sticky bottom button with normal flow button.")

# =========================================================================
# 4. FIX QUESTION TEXT COLOR IN JAVASCRIPT (BRIGHT WHITE ON DARK BACKGROUND)
# =========================================================================
old_q_render = """  const qTextElem = document.getElementById('question-text');
  if (currentLanguageMode === 'bilingual') {
    const enText = q.q_en || q.question_en || q.q;
    const viText = q.q;
    qTextElem.innerHTML = `
      <div style="font-size:1.15rem; font-weight:800; color:var(--dark); line-height:1.45; margin-bottom:8px;">${enText}</div>
      <div style="font-size:0.95rem; color:#475569; font-weight:600; line-height:1.45; border-top:1.5px dashed #E2E8F0; padding-top:8px;">${viText}</div>
    `;
  } else if (currentLanguageMode === 'en') {
    qTextElem.textContent = q.q_en || q.question_en || q.q;
  } else {
    qTextElem.textContent = q.q;
  }

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
  imgWrap.style.display = 'block';"""

new_q_render = """  const qTextElem = document.getElementById('question-text');
  if (currentLanguageMode === 'bilingual') {
    const enText = q.q_en || q.question_en || q.q;
    const viText = q.q;
    qTextElem.innerHTML = `
      <div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; margin-bottom:8px; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${enText}</div>
      <div style="font-size:1.02rem; color:#7DD3FC; font-weight:700; line-height:1.45; border-top:1px dashed rgba(255,255,255,0.25); padding-top:8px;">${viText}</div>
    `;
  } else if (currentLanguageMode === 'en') {
    qTextElem.innerHTML = `<div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${q.q_en || q.question_en || q.q}</div>`;
  } else {
    qTextElem.innerHTML = `<div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${q.q}</div>`;
  }

  // Chỉ hiển thị ảnh minh họa khi câu hỏi thực sự có trường img hợp lệ
  const imgElem = document.getElementById('question-img');
  const imgWrap = document.getElementById('q-img-wrap');
  if (imgElem && imgWrap) {
    if (q.img && q.img.trim()) {
      imgElem.onerror = function() {
        this.onerror = null;
        imgWrap.style.display = 'none';
      };
      imgElem.src = q.img;
      imgWrap.style.display = 'block';
    } else {
      imgWrap.style.display = 'none';
    }
  }"""

if old_q_render in text:
    text = text.replace(old_q_render, new_q_render)
    print("Fixed question text color to bright white & cyan, hidden empty image box.")

# =========================================================================
# 5. ADD QUIT/THOÁT FUNCTIONS (askQuitQuiz, closeQuitModal, confirmQuit)
# =========================================================================
quit_functions = """
// =========================================================================
// THOÁT BÀI THI & HỘP THOẠI XÁC NHẬN (CONFIRM BOX)
// =========================================================================
function askQuitQuiz() {
  const modal = document.getElementById('modal-quit');
  if (modal) {
    modal.classList.add('active');
  } else {
    if (confirm("Bé có chắc muốn dừng bài thi để về Trang Chủ không? Kết quả hiện tại sẽ không được lưu.")) {
      confirmQuit();
    }
  }
  playSound('click');
}

function closeQuitModal() {
  const modal = document.getElementById('modal-quit');
  if (modal) modal.classList.remove('active');
  playSound('click');
}

function confirmQuit() {
  closeQuitModal();
  clearInterval(timerInterval);
  isQuizSubmitted = true;
  showScreen('home-screen');
  playSound('click');
}
"""

if "function askQuitQuiz()" not in text:
    text = text.replace("function openLeaderboardModal() {", quit_functions + "\nfunction openLeaderboardModal() {")
    print("Added askQuitQuiz, closeQuitModal, and confirmQuit functions.")

# Write updated file
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("All 3 fixes applied successfully!")
