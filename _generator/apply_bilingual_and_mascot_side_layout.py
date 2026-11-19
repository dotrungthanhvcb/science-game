#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re, shutil

BASE_DIR = '/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz'
HTML_FILE = os.path.join(BASE_DIR, 'index.html')
BAK_FILE = os.path.join(BASE_DIR, 'index.html.bak_bilingual_side')

print("Starting Bilingual Upgrade & Quiz Mascot Side Layout...")
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup
shutil.copyfile(HTML_FILE, BAK_FILE)
print(f"Created backup at {BAK_FILE}")

# -------------------------------------------------------------
# STEP 1: Add missing IDs in Header
# -------------------------------------------------------------
# Tagline
content = content.replace(
    '<div class="text-[11px] text-slate-400">Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú</div>',
    '<div class="text-[11px] text-slate-400" id="header-tagline">Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú</div>'
)

# Music button text
old_music_btn = """<button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-200 transition" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc">
        <i data-lucide="volume-x" style="width:14px; height:14px;"></i>
        <span>Nhạc</span>
      </button>"""
new_music_btn = """<button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-200 transition" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc">
        <i data-lucide="volume-x" style="width:14px; height:14px;"></i>
        <span id="music-btn-text">Nhạc</span>
      </button>"""
if old_music_btn in content:
    content = content.replace(old_music_btn, new_music_btn)
else:
    content = re.sub(
        r'(<button[^>]*id=["\']music-btn["\'][^>]*>.*?<i[^>]*></i>\s*)<span>Nhạc</span>',
        r'\1<span id="music-btn-text">Nhạc</span>',
        content,
        flags=re.DOTALL
    )

# -------------------------------------------------------------
# STEP 2: Add missing IDs on Home Screen (labels, section titles)
# -------------------------------------------------------------
content = content.replace(
    '<span class="text-[10px] bg-cyan-100 text-cyan-800 font-extrabold px-2 py-0.5 rounded-full">Đổi bạn ▾</span>',
    '<span class="text-[10px] bg-cyan-100 text-cyan-800 font-extrabold px-2 py-0.5 rounded-full" id="home-mascot-change-badge">Đổi bạn ▾</span>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-600">👤 Tên bé:</label>',
    '<label class="text-xs font-bold text-slate-600" id="label-user-name">👤 Tên bé:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-600">🏫 Lớp:</label>',
    '<label class="text-xs font-bold text-slate-600" id="label-student-class">🏫 Lớp:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-600">🌐 Chế độ:</label>',
    '<label class="text-xs font-bold text-slate-600" id="label-lang-mode">🌐 Chế độ:</label>'
)

content = content.replace(
    '<span class="text-xs font-bold uppercase tracking-wider text-cyan-700 bg-cyan-100 px-2.5 py-0.5 rounded-full">6 Labs Đã Sẵn Sàng</span>',
    '<span class="text-xs font-bold uppercase tracking-wider text-cyan-700 bg-cyan-100 px-2.5 py-0.5 rounded-full" id="home-section-sub">6 Labs Đã Sẵn Sàng</span>'
)

content = content.replace(
    '<h3 class="font-baloo font-bold text-lg md:text-xl text-slate-900 leading-tight">CHỌN PHÒNG THÍ NGHIỆM & BẮT ĐẦU</h3>',
    '<h3 class="font-baloo font-bold text-lg md:text-xl text-slate-900 leading-tight" id="home-section-title">CHỌN PHÒNG THÍ NGHIỆM & BẮT ĐẦU</h3>'
)

content = content.replace(
    '<span class="text-xs font-black text-slate-600 shrink-0">Lọc chủ đề:</span>',
    '<span class="text-xs font-black text-slate-600 shrink-0" id="home-filter-label">Lọc chủ đề:</span>'
)

# -------------------------------------------------------------
# STEP 3: Overhaul Quiz Screen Layout (Place Mascot Companion on SIDE)
# -------------------------------------------------------------
# Let's inspect quiz screen structure:
# From top mission header to bottom next button
old_quiz_regex = re.compile(
    r'(<div class="quiz-card screen[^"]*" id="quiz-screen"[^>]*>)(.*?)(</div>\s*<div class="quiz-card screen" id="result-screen">)',
    re.DOTALL
)

quiz_match = old_quiz_regex.search(content)
if not quiz_match:
    print("ERROR: Could not locate quiz-screen container in index.html")
    sys.exit(1)

new_quiz_screen_html = """<div class="quiz-card screen animate-screen-in" id="quiz-screen" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:28px; padding:20px;">
    
    <!-- TOP MISSION HEADER (CHẾ ĐỘ THÁM HIỂM VŨ TRỤ) -->
    <div class="flex items-center justify-between gap-3 mb-4 shrink-0 flex-wrap">
      
      <div class="flex items-center gap-2">
        <button type="button" onclick="askQuitQuiz()" id="btn-quiz-quit" class="px-3.5 py-1.5 rounded-full bg-rose-50 border-2 border-rose-300 hover:bg-rose-100 text-rose-700 text-xs font-black flex items-center gap-1.5 shadow-xs transition cursor-pointer" title="Dừng bài thi để về Trang Chủ">
          <i data-lucide="log-out" style="width:14px; height:14px; stroke-width:2.5;"></i>
          <span id="quiz-quit-text">Thoát</span>
        </button>
        <button type="button" onclick="pauseQuiz()" id="btn-quiz-pause" class="px-3 py-1.5 rounded-full bg-white border border-slate-200 text-xs font-bold text-slate-600 hover:bg-slate-100 shadow-sm transition flex items-center gap-1">
          <i data-lucide="pause" style="width:14px; height:14px;"></i>
          <span id="quiz-pause-text">Tạm dừng</span>
        </button>
      </div>

      <!-- ROCKET PROGRESS BAR -->
      <div class="flex-1 min-w-[180px] max-w-md flex items-center gap-2.5">
        <div class="flex-1 bg-slate-200 h-3.5 rounded-full overflow-hidden p-0.5 border border-slate-300">
          <div class="progress-fill bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-600 h-full rounded-full transition-all duration-300" id="progress-fill" style="width: 10%;"></div>
        </div>
        <span class="text-xs font-black text-slate-700 font-baloo whitespace-nowrap animate-pulse-rocket" id="question-number">Câu 1/15 🚀</span>
      </div>

      <!-- COUNTDOWN TIMER PILL -->
      <div class="bg-white border-2 border-indigo-200 px-3.5 py-1 rounded-full text-xs font-black text-indigo-900 flex items-center gap-1.5 shadow-sm" id="quiz-timer">
        <i data-lucide="clock" style="width:14px; height:14px; stroke-width:2.5;"></i>
        <span id="timer-text">00:00</span>
      </div>

    </div>

    <!-- MISSION BADGE ROW & XP -->
    <div class="flex items-center justify-between px-1 mb-3.5">
      <div class="flex items-center gap-2 flex-wrap">
        <span class="text-[11px] font-black bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full border border-indigo-200 flex items-center gap-1.5" id="badge-topic-age">
          <span>🚀</span> <span>Vũ Trụ & Thời Tiết</span>
        </span>
        <span class="text-[11px] font-bold bg-slate-100 text-slate-700 px-2.5 py-0.5 rounded-full border border-slate-200" id="badge-source">
          📗 SGK Việt Nam
        </span>
      </div>
      <span class="text-xs font-extrabold text-amber-600 flex items-center gap-1 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200" id="badge-xp">
        <span>⭐</span> +20 XP
      </span>
    </div>

    <!-- 2-COLUMN RESPONSIVE LAYOUT (QUESTION & CHOICES ON LEFT, COMPANION MASCOT ON RIGHT) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">

      <!-- LEFT / MAIN COLUMN (lg:col-span-8): QUESTION CARD, 4 CHOICES, EXPLANATION, NEXT BUTTON -->
      <div class="lg:col-span-8 flex flex-col gap-3.5 order-2 lg:order-1">

        <!-- DEEP COSMIC QUESTION CARD (FIGMA AI SCREEN 2 QUESTION CARD) -->
        <div class="bg-gradient-to-b from-indigo-950 to-slate-900 text-white rounded-3xl p-5 md:p-6 border-2 border-indigo-800/60 shadow-xl relative overflow-hidden">
          <div class="relative z-10 flex flex-col gap-3">
            <!-- Huy hiệu thể loại ở chính giữa thẻ -->
            <div class="flex items-center justify-center text-center">
              <span id="mission-badge-tag" class="inline-flex items-center justify-center text-[11px] font-black tracking-wider text-cyan-300 bg-cyan-950/80 border border-cyan-400/40 px-3.5 py-1 rounded-full uppercase shadow-xs">
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
        </div>

        <!-- 4 TACTILE 3D OPTION CARDS (A, B, C, D) -->
        <div class="flex flex-col gap-2.5" id="choices-list">
          <!-- Render động qua renderMultipleChoice(q) -->
        </div>

        <!-- TỰ LUẬN (SA BOX) -->
        <div class="sa-box bg-white p-4 rounded-2xl border-2 border-slate-200" id="sa-box" style="display:none;">
          <input type="text" class="sa-input w-full p-3 rounded-xl border border-slate-300 font-bold text-sm mb-2" id="sa-input-field" placeholder="Gõ câu trả lời của bé vào đây..." autocomplete="off">
          <button type="button" class="btn-3d btn-3d-cyan px-4 py-2 text-xs font-bold" id="btn-sa-submit" onclick="submitShortAnswer()">Kiểm tra đáp án</button>
        </div>

        <!-- GIẢI THÍCH KHOA HỌC (💡 SỰ THẬT KHOA HỌC) -->
        <div class="explanation-card bg-amber-50/90 border-2 border-amber-300 rounded-2xl p-4 text-xs font-medium text-amber-950 shadow-sm" id="explanation-card" style="display:none;"></div>

        <!-- BOTTOM ACTION BUTTON (TIẾP TỤC HÀNH TRÌNH / NEXT QUESTION) -->
        <div class="pt-2 w-full">
          <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl cursor-pointer" id="btn-next" onclick="goNextQuestion()">
            <span id="btn-next-text">TIẾP TỤC HÀNH TRÌNH</span>
            <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
          </button>
        </div>

      </div>

      <!-- RIGHT / SIDE COLUMN (lg:col-span-4): MASCOT COMPANION DEDICATED PANEL (BÊN CẠNH) -->
      <div class="lg:col-span-4 order-1 lg:order-2">
        <div class="sticky top-20 bg-gradient-to-br from-white via-cyan-50/30 to-indigo-50/30 border-2 border-cyan-200/80 rounded-3xl p-4 md:p-5 shadow-lg flex flex-col gap-3.5">
          
          <!-- Header pill bạn đồng hành -->
          <div class="flex items-center justify-between pb-1 border-b border-cyan-100">
            <span class="text-[10px] font-black uppercase tracking-wider text-cyan-800 bg-cyan-100 px-2.5 py-0.5 rounded-full" id="quiz-companion-label">
              🌟 BẠN ĐỒNG HÀNH
            </span>
            <span class="text-[10px] font-bold text-slate-500 flex items-center gap-1 cursor-pointer hover:text-cyan-700 transition" onclick="openMascotPickerModal()" id="quiz-change-mascot-btn" title="Bấm để chọn bạn đồng hành khác">
              <span>Đổi bạn</span> <span>▾</span>
            </span>
          </div>

          <!-- Avatar & Mascot Info -->
          <div class="flex items-center gap-3.5 cursor-pointer select-none" onclick="onMascotClick()" title="Bấm vào bạn đồng hành để nghe lời động viên!">
            <div id="quiz-mascot-svg-wrap" class="w-16 h-16 rounded-2xl bg-white border-2 border-cyan-300 shadow-md flex items-center justify-center text-4xl shrink-0 animate-mascot-float">
              🦉
            </div>
            <div>
              <div class="font-baloo font-bold text-base text-slate-900 leading-tight" id="quiz-mascot-name">
                Giáo Sư Cú Vọ
              </div>
              <div class="text-[11px] font-extrabold text-cyan-600 mt-0.5" id="quiz-mascot-role">
                Bác Học Thông Thái
              </div>
              <div class="text-[10px] text-slate-400 font-semibold flex items-center gap-1 mt-0.5" id="quiz-mascot-tap-hint">
                <span>👆 Bấm vào tớ để nghe mách nước!</span>
              </div>
            </div>
          </div>

          <!-- Interactive Speech Bubble -->
          <div class="relative bg-white border-2 border-cyan-200 rounded-2xl p-3.5 shadow-sm">
            <div class="text-xs text-slate-700 font-bold leading-relaxed" id="mascot-speech">
              Bé đọc kỹ câu hỏi nhé, chúng mình cùng nhau đạt điểm 10 nào! 🌟
            </div>
            <!-- Bubble Arrow pointing up towards avatar -->
            <div class="absolute -top-2 left-6 w-3 h-3 bg-white border-t-2 border-l-2 border-cyan-200 rotate-45"></div>
          </div>

          <!-- Live Mission Metrics (Streak & Star XP) -->
          <div class="grid grid-cols-2 gap-2 pt-1 border-t border-cyan-100">
            <div class="bg-cyan-50/80 rounded-xl p-2 text-center border border-cyan-100">
              <div class="text-[10px] font-bold text-cyan-800" id="quiz-stat-combo-label">🔥 Chuỗi đúng</div>
              <div class="font-baloo font-black text-sm text-cyan-700" id="quiz-mascot-streak-count">0 Liên tiếp</div>
            </div>
            <div class="bg-amber-50/80 rounded-xl p-2 text-center border border-amber-100">
              <div class="text-[10px] font-bold text-amber-800" id="quiz-stat-score-label">⭐ Sao tích lũy</div>
              <div class="font-baloo font-black text-sm text-amber-600" id="quiz-mascot-score-count">+0 XP</div>
            </div>
          </div>

        </div>
      </div>

    </div>

  </div>"""

content = old_quiz_regex.sub(new_quiz_screen_html + r'\n\n  <div class="quiz-card screen" id="result-screen">', content, count=1)
print("Quiz Screen layout updated to 2-column with companion on SIDE.")

# -------------------------------------------------------------
# STEP 4: Add IDs in Result Screen, Leaderboard Modal, Quit Modal, Pause Modal
# -------------------------------------------------------------
# Result Screen Stat Labels
content = content.replace(
    '<div class="summary-stat-lbl">ĐIỂM SỐ</div>',
    '<div class="summary-stat-lbl" id="stat-score-lbl">ĐIỂM SỐ</div>'
)
content = content.replace(
    '<div class="summary-stat-lbl">CÂU ĐÚNG ✅</div>',
    '<div class="summary-stat-lbl" id="stat-correct-lbl">CÂU ĐÚNG ✅</div>'
)
content = content.replace(
    '<div class="summary-stat-lbl">CÂU SAI ❌</div>',
    '<div class="summary-stat-lbl" id="stat-wrong-lbl">CÂU SAI ❌</div>'
)
content = content.replace(
    '<div class="summary-stat-lbl">THỜI GIAN ⏱️</div>',
    '<div class="summary-stat-lbl" id="stat-time-lbl">THỜI GIAN ⏱️</div>'
)

# Result Screen Buttons
content = content.replace(
    '<span>XEM LẠI CHI TIẾT BÀI LÀM</span>',
    '<span id="btn-review-detail-text">XEM LẠI CHI TIẾT BÀI LÀM</span>'
)
content = content.replace(
    '<span>XEM BẢNG SAO TUẦN NÀY 🌟</span>',
    '<span id="btn-view-stars-text">XEM BẢNG SAO TUẦN NÀY 🌟</span>'
)
content = content.replace(
    '<span>Ôn lại câu sai</span>',
    '<span id="btn-replay-wrong-text">Ôn lại câu sai</span>'
)

# Quit Modal
content = content.replace(
    '<div class="font-baloo font-bold text-xl text-slate-900 mb-2">Dừng Bài Thi?</div>',
    '<div class="font-baloo font-bold text-xl text-slate-900 mb-2" id="quit-modal-title">Dừng Bài Thi?</div>'
)
content = content.replace(
    '<div class="text-xs text-slate-600 font-medium mb-5 leading-relaxed">Bé có chắc muốn dừng bài thám hiểm này để về Trang Chủ không? Điểm số lượt thi này sẽ không được lưu nếu thoát ngang.</div>',
    '<div class="text-xs text-slate-600 font-medium mb-5 leading-relaxed" id="quit-modal-desc">Bé có chắc muốn dừng bài thám hiểm này để về Trang Chủ không? Điểm số lượt thi này sẽ không được lưu nếu thoát ngang.</div>'
)
content = content.replace(
    'onclick="closeQuitModal()">\n        Tiếp tục làm\n      </button>',
    'onclick="closeQuitModal()" id="quit-modal-cancel">\n        Tiếp tục làm\n      </button>'
)
content = content.replace(
    'onclick="confirmQuit()">\n        Đồng ý thoát ➔\n      </button>',
    'onclick="confirmQuit()" id="quit-modal-confirm">\n        Đồng ý thoát ➔\n      </button>'
)

# Pause Modal
content = content.replace(
    '<div class="modal-title">Đang Tạm Dừng Bài Thi</div>',
    '<div class="modal-title" id="pause-modal-title">Đang Tạm Dừng Bài Thi</div>'
)
content = content.replace(
    '<div class="modal-desc">Đồng hồ đã đóng băng. Bé hãy nghỉ ngơi chớp mắt, uống một ngụm nước rồi cùng Bo Bo tiếp tục nhé!</div>',
    '<div class="modal-desc" id="pause-modal-desc">Đồng hồ đã đóng băng. Bé hãy nghỉ ngơi chớp mắt, uống một ngụm nước rồi cùng Bo Bo tiếp tục nhé!</div>'
)
content = content.replace(
    '<button class="modal-btn-confirm" onclick="resumeQuiz()">▶️ Tiếp tục làm bài</button>',
    '<button class="modal-btn-confirm" id="pause-modal-resume" onclick="resumeQuiz()">▶️ Tiếp tục làm bài</button>'
)

# Leaderboard Modal
old_lead_head = """<div class="font-baloo font-bold text-lg md:text-xl text-slate-900 flex items-center gap-2 leading-tight">
          <span>Bảng Sao Tuần Này</span>
          <span class="text-amber-500 animate-bounce">🌟</span>
        </div>
        <div class="text-xs text-slate-500 font-medium">Top nhà thám hiểm nhí xuất sắc nhất tuần</div>"""

new_lead_head = """<div class="font-baloo font-bold text-lg md:text-xl text-slate-900 flex items-center gap-2 leading-tight" id="lead-title">
          <span>Bảng Sao Tuần Này</span>
          <span class="text-amber-500 animate-bounce">🌟</span>
        </div>
        <div class="text-xs text-slate-500 font-medium" id="lead-sub">Top nhà thám hiểm nhí xuất sắc nhất tuần</div>"""

if old_lead_head in content:
    content = content.replace(old_lead_head, new_lead_head)

content = content.replace(
    '<span class="text-xs font-bold text-slate-600">Lọc:</span>',
    '<span class="text-xs font-bold text-slate-600" id="lead-filter-label">Lọc:</span>'
)
content = content.replace(
    '<span>🎊 Bắn Pháo Hoa</span>',
    '<span id="lead-fireworks-btn-text">🎊 Bắn Pháo Hoa</span>'
)
content = content.replace(
    '<div class="text-[9px] text-indigo-300 uppercase font-black tracking-wider">VỊ TRÍ CỦA BẠN</div>',
    '<div class="text-[9px] text-indigo-300 uppercase font-black tracking-wider" id="lead-user-rank-label">VỊ TRÍ CỦA BẠN</div>'
)
content = content.replace(
    '<div class="text-[9px] text-indigo-300 font-bold">Kỷ Lục Tuần Này</div>',
    '<div class="text-[9px] text-indigo-300 font-bold" id="lead-user-record-label">Kỷ Lục Tuần Này</div>'
)
content = content.replace(
    '<span>BẮN PHÁO HOA ĂN MỪNG 🎊</span>',
    '<span id="lead-grand-fireworks-text">BẮN PHÁO HOA ĂN MỪNG 🎊</span>'
)

# -------------------------------------------------------------
# STEP 5: Upgrade MASCOTS Data with English Names & Descriptions
# -------------------------------------------------------------
old_mascots_regex = re.compile(r'const MASCOTS = \[.*?\];\s*let currentMascotId', re.DOTALL)
new_mascots_code = """const MASCOTS = [
  {
    id: 'hoot',
    name: 'Giáo Sư Cú Vọ',
    name_en: 'Wise Professor Owl',
    title: 'Bác Học Thông Thái',
    title_en: 'Wise Scholar',
    color: '#4361EE',
    desc: 'Bậc thầy lý luận khoa học, luôn yêu thích hiện tượng tự nhiên và giải thích chi tiết!',
    desc_en: 'Master of science logic, natural phenomena and crystal-clear explanations!',
    avatar: '🦉'
  },
  {
    id: 'robosci',
    name: 'Bé Rô-Bốt Sci-Bot',
    name_en: 'Sci-Bot AI',
    title: 'Siêu Trí Tuệ AI',
    title_en: 'AI Super Mind',
    color: '#06D6A0',
    desc: 'Người bạn công nghệ đáng yêu với đôi mắt LED biểu cảm và ăng-ten bắt sóng!',
    desc_en: 'Adorable high-tech buddy with expressive LED eyes and smart antenna!',
    avatar: '🤖'
  },
  {
    id: 'dino',
    name: 'Khủng Long Dino',
    name_en: 'Dino Explorer',
    title: 'Thám Hiểm Sinh Thái',
    title_en: 'Eco Explorer',
    color: '#10B981',
    desc: 'Chú khủng long mũ tai bèo dũng cảm, am hiểu muôn loài động thực vật trên Trái Đất!',
    desc_en: 'Brave explorer dino with deep knowledge of Earth\\'s plants and wildlife!',
    avatar: '🦖'
  },
  {
    id: 'astrocat',
    name: 'Mèo Kitty Astro',
    name_en: 'Astro Kitty',
    title: 'Phi Hành Gia Vũ Trụ',
    title_en: 'Space Astronaut',
    color: '#8B5CF6',
    desc: 'Cô mèo du hành vũ trụ, thích ngắm các hành tinh, Mặt Trời và dải ngân hà rực rỡ!',
    desc_en: 'Galaxy voyager kitty fascinated by planets, the Sun, and starry nebulae!',
    avatar: '🐱'
  },
  {
    id: 'foxie',
    name: 'Cáo Nhỏ Foxie',
    name_en: 'Foxie Detective',
    title: 'Thám Tử Khoa Học',
    title_en: 'Science Detective',
    color: '#F97316',
    desc: 'Nhanh nhẹn, mắt sáng, luôn mang theo kính lúp để quan sát các thí nghiệm kỳ thú!',
    desc_en: 'Sharp and quick-witted detective, always carrying a magnifier for fun discoveries!',
    avatar: '🦊'
  }
];

const SCIENCE_FACTS_EN = [
  "Did you know: A shrimp\\'s heart is actually located in its head! 🦐",
  "Did you know: Octopuses have 3 hearts and their blood is royal blue! 🐙",
  "Did you know: The Sun is about 1,300,000 times larger than planet Earth! ☀️",
  "Did you know: Kangaroos cannot walk backwards due to their tail and muscular legs! 🦘",
  "Did you know: Bamboo can grow almost 1 meter (35 inches) in a single day! 🎋",
  "Did you know: Honeybees flap their wings 200 times per second to fly! 🐝",
  "Did you know: The world\\'s largest waterfall is actually deep under the ocean! 🌊",
  "Did you know: Venus is the hottest planet in the Solar System, not Mercury! 🪐",
  "Did you know: Polar bears have black skin underneath their white fur to trap heat! 🐻‍❄️",
  "Did you know: Hummingbirds are the only birds that can fly backwards and upside down! 🐦"
];

let currentMascotId"""

if old_mascots_regex.search(content):
    content = old_mascots_regex.sub(new_mascots_code, content, count=1)
    print("MASCOTS array upgraded with bilingual support & SCIENCE_FACTS_EN added.")
else:
    print("WARNING: Could not find MASCOTS array.")

# -------------------------------------------------------------
# STEP 6: Upgrade updateAllMascotsUI, setMascotMood, onMascotClick
# -------------------------------------------------------------
old_mascot_funcs_regex = re.compile(
    r'function onMascotClick\(\)\s*\{.*?function openMascotPickerModal\(\)',
    re.DOTALL
)

new_mascot_funcs_code = """function onMascotClick() {
  playKidSound('click');
  const isEn = (currentLanguageMode === 'en');
  const facts = isEn ? SCIENCE_FACTS_EN : SCIENCE_FACTS;
  const fact = facts[Math.floor(Math.random() * facts.length)];
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  const mName = isEn ? (m.name_en || m.name) : m.name;
  const bubble = document.getElementById('mascot-speech');
  if (bubble) {
    bubble.innerHTML = isEn 
      ? `<strong>💡 ${mName} tip:</strong><br>${fact}`
      : `<strong>💡 ${mName} mách bạn:</strong><br>${fact}`;
  }
}

function setMascotMood(mood, customText) {
  const bubble = document.getElementById('mascot-speech');
  const mouth = document.getElementById('mascot-mouth');
  if (!bubble) return;
  const isEn = (currentLanguageMode === 'en');

  if (mouth) {
    if (mood === 'thinking') mouth.setAttribute('d', 'M42 62 Q50 68 58 62');
    else if (mood === 'happy' || mood === 'selected') mouth.setAttribute('d', 'M40 60 Q50 70 60 60');
    else if (mood === 'finished') mouth.setAttribute('d', 'M38 58 Q50 78 62 58');
  }

  if (mood === 'thinking') {
    bubble.textContent = customText || (isEn ? 'Read carefully, I know you can do it! 🌟' : 'Bé đọc kỹ câu hỏi nhé, Bo Bo tin bé làm được! 🌟');
  } else if (mood === 'selected' || (mood === 'happy' && !isQuizSubmitted)) {
    const neutralVI = [
      'Đã ghi nhận đáp án! Bé có thể sửa lại hoặc sang câu tiếp theo nhé. 📝',
      'Lựa chọn đã được lưu! Bé hãy tự tin làm tiếp câu sau nào. 🌟',
      'Bé đã chọn xong! Cứ bình tĩnh suy nghĩ và tiếp tục nhé. 🚀',
      'Câu trả lời đã lưu tạm thời. Nộp bài xong mới biết kết quả bé nhé! 💡'
    ];
    const neutralEN = [
      'Answer recorded! You can change it or move to the next question. 📝',
      'Choice saved! Stay confident for the next question. 🌟',
      'Choice recorded! Keep calm and continue your mission. 🚀',
      'Answer saved temporarily. Score will be revealed upon submit! 💡'
    ];
    const msgs = isEn ? neutralEN : neutralVI;
    bubble.textContent = customText || msgs[Math.floor(Math.random() * msgs.length)];
  } else if (mood === 'finished') {
    bubble.textContent = customText || (isEn ? 'Congratulations on finishing the quiz! Check out your score! 🎉' : 'Chúc mừng bé đã hoàn thành bài thi! Cùng xem điểm số nào! 🎉');
  } else {
    if (customText) bubble.textContent = customText;
  }
}

function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  const isEn = (currentLanguageMode === 'en');
  
  const mName = isEn ? (m.name_en || m.name) : m.name;
  const mTitle = isEn ? (m.title_en || m.title) : m.title;

  // 0. Header Bar Mascot Pill (ISSUE 4: Luôn hiện diện rõ ràng trên Header)
  const headerMascotAvatar = document.getElementById('header-mascot-avatar');
  if (headerMascotAvatar) headerMascotAvatar.textContent = m.avatar || '🦉';
  const headerMascotName = document.getElementById('header-mascot-name');
  if (headerMascotName) {
    const shortName = isEn 
      ? (m.name_en ? m.name_en.replace('Wise Professor ', '').replace('Dr. ', '') : m.name)
      : m.name.replace('Giáo Sư ', '').replace('Bé ', '');
    headerMascotName.textContent = shortName;
  }

  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 42);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = mName;

  // 2. Home screen (Mascot sinh động kèm lời thoại cổ vũ)
  const homeSvgWrap = document.getElementById('home-mascot-svg-wrap');
  if (homeSvgWrap) homeSvgWrap.innerHTML = renderMascotSvg(m.id, 58, 'cheer');
  const homeName = document.getElementById('home-mascot-name');
  if (homeName) homeName.textContent = mName;
  const homeTitle = document.getElementById('home-mascot-title');
  if (homeTitle) homeTitle.textContent = mTitle;
  const homeSpeech = document.getElementById('home-mascot-speech');
  if (homeSpeech) {
    homeSpeech.textContent = isEn 
      ? `"Hi there! I am ready to explore fascinating science with you today! 🚀"`
      : `"Chào bạn! Hôm nay tớ cùng bạn sẵn sàng chinh phục Đấu Trường Khoa Học nhé! 🚀"`;
  }

  // 3. Quiz screen (Mascot to bản 64px ở BÊN CẠNH câu hỏi, tương tác theo từng câu)
  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 64);
  const quizMascotName = document.getElementById('quiz-mascot-name');
  if (quizMascotName) quizMascotName.textContent = mName;
  const quizMascotRole = document.getElementById('quiz-mascot-role');
  if (quizMascotRole) quizMascotRole.textContent = mTitle;

  // 4. Result screen (Mascot nhảy múa ăn mừng cúp vàng)
  const resSvgWrap = document.getElementById('result-mascot-svg-wrap');
  if (resSvgWrap) resSvgWrap.innerHTML = renderMascotSvg(m.id, 72, 'cheer');
  const resSpeech = document.getElementById('result-mascot-speech');
  if (resSpeech) {
    resSpeech.textContent = isEn
      ? `"Awesome job my friend! I am so proud of our wonderful science adventure! 🎉"`
      : `"Tuyệt vời quá bạn ơi! Tớ rất tự hào vì chúng mình đã hoàn thành xuất sắc bài thi này! 🎉"`;
  }
}

function openMascotPickerModal()"""

if old_mascot_funcs_regex.search(content):
    content = old_mascot_funcs_regex.sub(new_mascot_funcs_code, content, count=1)
    print("Mascot functions updated with bilingual and side-companion support.")
else:
    print("WARNING: Could not find old mascot functions regex.")

# -------------------------------------------------------------
# STEP 7: Upgrade displayQuestion and handleChoiceSelect
# -------------------------------------------------------------
old_display_q_regex = re.compile(
    r'function displayQuestion\(\)\s*\{.*?const qTextElem = document\.getElementById\(\'question-text\'\);',
    re.DOTALL
)

new_display_q_top = """function displayQuestion() {
  const q = currentDeck[currentIndex];
  const total = currentDeck.length;
  const isLast = (currentIndex === total - 1);

  const isEn = (currentLanguageMode === 'en');
  const isBi = (currentLanguageMode === 'bilingual');

  const qNumPrefix = isEn ? 'Question' : 'Câu';
  document.getElementById('question-number').textContent = `${qNumPrefix} ${currentIndex + 1} / ${total} 🚀`;

  const sourceEnMap = {
    'SGK Việt Nam (GDPT 2018)': 'National Curriculum (MOET)',
    'SGK Việt Nam': 'National Curriculum (MOET)',
    'Trạng Nguyên & Violympic': 'National Science Olympiad',
    'Kangaroo Khoa học (IKSC)': 'IKSC Kangaroo Science',
    'IXL & Khan Academy Khoa học': 'IXL & Khan Science',
    'IXL & Khan Academy': 'IXL & Khan Science',
    'National Geographic Kids': 'NatGeo Kids',
    'Khác': 'General Science'
  };

  const badgeSource = document.getElementById('badge-source');
  if (badgeSource) {
    const rawSrc = q.source || 'Khoa học';
    const srcName = isEn ? (sourceEnMap[rawSrc] || rawSrc) : rawSrc;
    badgeSource.innerHTML = `${getSourceIcon(q.source)} ${isEn ? 'Source' : 'Nguồn'}: ${srcName}`;
  }

  const topicEnMap = {
    'Động Vật': 'Animal Kingdom',
    'Thực Vật': 'Plants & Nature',
    'Vũ Trụ & Thời Tiết': 'Space & Solar System',
    'Cơ Thể Người': 'Human Body & Health',
    'Con người & Sức khỏe': 'Human Body & Health',
    'Địa Lý Việt Nam': 'Geography & Earth',
    'Lịch Sử & Văn Hóa': 'History & Culture',
    'Vật Chất & Hiện Tượng': 'Physics & Matter'
  };
  const topicText = isEn ? (topicEnMap[q.topic] || q.topic) : q.topic;
  const gradeText = isEn ? (q.grade ? `Grade ${q.grade}` : (q.age ? `Grade ${q.age}` : 'Elementary')) : (q.grade ? `Lớp ${q.grade}` : (q.age ? `Lớp ${q.age}` : 'Tiểu học'));
  const diffText = isEn ? `Level ${q.diff}` : `Mức ${q.diff}`;
  document.getElementById('badge-topic-age').textContent = `${topicText} • ${gradeText} • ${diffText}`;

  // Cập nhật chỉ số tương tác thời gian thực trên panel bạn đồng hành bên cạnh
  const answeredCount = Object.keys(userAnswersMap).length;
  const streakCountElem = document.getElementById('quiz-mascot-streak-count');
  if (streakCountElem) {
    streakCountElem.textContent = isEn ? `${answeredCount} Done` : `${answeredCount} Đã làm`;
  }
  const scoreCountElem = document.getElementById('quiz-mascot-score-count');
  if (scoreCountElem) {
    scoreCountElem.textContent = `+${answeredCount * 20} XP`;
  }

  const qTextElem = document.getElementById('question-text');"""

if old_display_q_regex.search(content):
    content = old_display_q_regex.sub(new_display_q_top, content, count=1)
    print("displayQuestion top logic updated with sourceEnMap and live stats.")
else:
    print("WARNING: Could not find displayQuestion top logic regex.")

# Update mascot cheer in displayQuestion
content = content.replace(
    "setMascotMood('thinking', isLast ? 'Bé ơi, đây là câu cuối cùng rồi! Làm xong bé kiểm tra lại nhé!' : `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`);",
    "setMascotMood('thinking', isEn ? (isLast ? 'This is the final question! Review carefully when done! 🌟' : `Let\\'s explore question ${currentIndex + 1} together! 🚀`) : (isLast ? 'Bé ơi, đây là câu cuối cùng rồi! Làm xong bé kiểm tra lại nhé!' : `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`));"
)

# Update Next button in displayQuestion
old_next_btn_code = """  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = isEn 
      ? '<i data-lucide="list-checks" style="width:18px; height:18px; stroke-width:2.5;"></i> <span>Review & Submit</span>'
      : '<i data-lucide="list-checks" style="width:18px; height:18px; stroke-width:2.5;"></i> <span>Xem lại & Nộp bài</span>';
    btnNext.classList.add('btn-last-step');
    btnNext.onclick = openReviewBeforeSubmit;
  } else {
    btnNext.innerHTML = isEn
      ? '<span>Next Question</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>'
      : '<span>Câu tiếp theo</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>';
    btnNext.classList.remove('btn-last-step');
    btnNext.onclick = goNextQuestion;
  }"""

new_next_btn_code = """  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
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

if old_next_btn_code in content:
    content = content.replace(old_next_btn_code, new_next_btn_code)

# Update handleChoiceSelect feedback
content = content.replace(
    "setMascotMood('happy', `Bé đã chọn [${chosenKey}]! Bé có thể đổi đáp án khác hoặc bấm \"Câu tiếp theo\" nhé.`);",
    """const isEn = (currentLanguageMode === 'en');
  setMascotMood('happy', isEn ? `You selected [${chosenKey}]! You can change it or click Next Question. 🌟` : `Bé đã chọn [${chosenKey}]! Bé có thể đổi đáp án khác hoặc bấm "Câu tiếp theo" nhé.`);
  const answeredCount = Object.keys(userAnswersMap).length;
  const streakCountElem = document.getElementById('quiz-mascot-streak-count');
  if (streakCountElem) streakCountElem.textContent = isEn ? `${answeredCount} Done` : `${answeredCount} Đã làm`;
  const scoreCountElem = document.getElementById('quiz-mascot-score-count');
  if (scoreCountElem) scoreCountElem.textContent = `+${answeredCount * 20} XP`;"""
)

# -------------------------------------------------------------
# STEP 8: Upgrade renderLeaderboardList Podium to be Bilingual
# -------------------------------------------------------------
content = content.replace(
    '<span class="text-[9px] opacity-90">Á QUÂN</span>',
    '<span class="text-[9px] opacity-90">${isEn ? \'RUNNER-UP\' : \'Á QUÂN\'}</span>'
)
content = content.replace(
    '<span class="text-[10px] tracking-wider font-extrabold">QUÁN QUÂN</span>',
    '<span class="text-[10px] tracking-wider font-extrabold">${isEn ? \'CHAMPION\' : \'QUÁN QUÂN\'}</span>'
)
content = content.replace(
    '<span class="text-[9px] opacity-90">QUÝ QUÂN</span>',
    '<span class="text-[9px] opacity-90">${isEn ? \'3RD PLACE\' : \'QUÝ QUÂN\'}</span>'
)
content = content.replace(
    'title="Bấm vào Quán quân để bắn pháo hoa ăn mừng!"',
    'title="${isEn ? \'Tap Champion to launch celebratory fireworks!\' : \'Bấm vào Quán quân để bắn pháo hoa ăn mừng!\'}"'
)

# -------------------------------------------------------------
# STEP 9: Upgrade updateHeaderAuthDisplay for English classes
# -------------------------------------------------------------
content = content.replace(
    "const tagText = isAdm ? 'Admin' : (acc.studentClass || 'Lớp 2');",
    """const isEn = (currentLanguageMode === 'en');
    let rawClass = acc.studentClass || 'Lớp 2';
    const tagText = isAdm ? 'Admin' : (isEn ? rawClass.replace('Lớp ', 'Grade ') : rawClass);"""
)

# -------------------------------------------------------------
# STEP 10: Replace applyLanguageToUI with Full Comprehensive Version
# -------------------------------------------------------------
old_apply_lang_regex = re.compile(
    r'function applyLanguageToUI\(lang\)\s*\{.*?refreshLucideIcons\(\);\s*\}',
    re.DOTALL
)

new_apply_lang_code = """function applyLanguageToUI(lang) {
  currentLanguageMode = lang;
  localStorage.setItem('science_quiz_lang_mode', lang);

  // Sync select dropdown if present
  const select = document.getElementById('language-mode-select');
  if (select && select.value !== lang) {
    select.value = lang;
  }

  // Update header VI/EN toggle buttons
  const btnVi = document.getElementById('lang-btn-vi');
  const btnEn = document.getElementById('lang-btn-en');
  if (btnVi && btnEn) {
    if (lang === 'vi') {
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    } else {
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    }
  }

  const isEn = (lang === 'en');

  // 1. Header Elements
  const headerTagline = document.getElementById('header-tagline');
  if (headerTagline) headerTagline.textContent = isEn ? 'Junior Science Lab & Explorations' : 'Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú';

  const navHome = document.querySelector('#nav-item-home span');
  if (navHome) navHome.textContent = isEn ? '1. Topics · Lab' : '1. Topics · Lab';

  const navQuiz = document.querySelector('#nav-item-quiz span');
  if (navQuiz) navQuiz.textContent = isEn ? '2. Quiz · Space' : '2. Quiz · Space';

  const navLeaderboard = document.querySelector('#nav-item-leaderboard span');
  if (navLeaderboard) navLeaderboard.textContent = isEn ? '3. Stars · Weekly 🌟' : '3. Stars · Bảng Sao 🌟';

  const navHistory = document.querySelector('#nav-item-history span');
  if (navHistory) navHistory.textContent = isEn ? 'History' : 'Lịch Sử';

  const navUserMgmt = document.querySelector('#nav-item-user-mgmt span');
  if (navUserMgmt) navUserMgmt.textContent = isEn ? 'Admin' : 'Quản Lý';

  const musicBtnText = document.getElementById('music-btn-text');
  if (musicBtnText) musicBtnText.textContent = isEn ? 'Music' : 'Nhạc';

  // 2. Home Screen
  const heroTag = document.getElementById('hero-tag');
  if (heroTag) heroTag.textContent = isEn ? '🔬 SCIENCE LABORATORY' : '🔬 PHÒNG THÍ NGHIỆM KHOA HỌC';
  
  const heroTitle = document.getElementById('hero-title');
  if (heroTitle) heroTitle.innerHTML = isEn ? 'Ready to Explore<br>Fascinating Science! ⚡' : 'Sẵn Sàng Thám Hiểm<br>Khoa Học Kỳ Thú! ⚡';
  
  const heroDesc = document.getElementById('hero-desc');
  if (heroDesc) heroDesc.textContent = isEn ? 'Complete lab missions to gather all 1,000 knowledge stars!' : 'Hoàn thành các phòng Lab để thu thập đủ 1.000 ngôi sao kiến thức và chinh phục đỉnh cao khoa học!';
  
  const heroStartBtn = document.getElementById('hero-start-btn');
  if (heroStartBtn) heroStartBtn.textContent = isEn ? 'ENTER MISSION NOW 🚀' : 'VÀO PHÒNG THI NGAY 🚀';

  const heroStarsBtn = document.getElementById('hero-stars-btn');
  if (heroStarsBtn) heroStarsBtn.textContent = isEn ? 'View Stars Board 🌟' : 'Xem Bảng Sao 🌟';

  // Home Mascot Card
  const homeMascotBadge = document.getElementById('home-mascot-change-badge');
  if (homeMascotBadge) homeMascotBadge.textContent = isEn ? 'Change ▾' : 'Đổi bạn ▾';

  // Home Quick Profile Form Labels
  const labelName = document.getElementById('label-user-name');
  if (labelName) labelName.textContent = isEn ? '👤 Name:' : '👤 Tên bé:';
  const labelClass = document.getElementById('label-student-class');
  if (labelClass) labelClass.textContent = isEn ? '🏫 Grade:' : '🏫 Lớp:';
  const labelLang = document.getElementById('label-lang-mode');
  if (labelLang) labelLang.textContent = isEn ? '🌐 Mode:' : '🌐 Chế độ:';

  // Update student class select options
  const classSelect = document.getElementById('student-class');
  if (classSelect) {
    const opts = classSelect.options;
    for (let i = 0; i < opts.length; i++) {
      const val = opts[i].value;
      if (val === 'all') {
        opts[i].textContent = isEn ? '🌟 All Grades' : '🌟 Tất cả các lớp';
      } else {
        const num = val.replace(/[^0-9]/g, '');
        opts[i].textContent = isEn ? `🎒 Grade ${num || val}` : `🎒 Lớp ${num || val}`;
      }
    }
  }

  // Home Section Headers
  const sectionTitle = document.getElementById('home-section-title');
  if (sectionTitle) sectionTitle.textContent = isEn ? 'SELECT LABORATORY & START' : 'CHỌN PHÒNG THÍ NGHIỆM & BẮT ĐẦU';
  const sectionSub = document.getElementById('home-section-sub');
  if (sectionSub) sectionSub.textContent = isEn ? '6 Labs Ready' : '6 Labs Đã Sẵn Sàng';
  const filterLabel = document.getElementById('home-filter-label');
  if (filterLabel) filterLabel.textContent = isEn ? 'Filter topics:' : 'Lọc chủ đề:';

  const homeStartBtn = document.getElementById('home-start-btn-text');
  if (homeStartBtn) homeStartBtn.textContent = isEn ? 'START SCIENCE EXPLORATION 🚀' : 'BẮT ĐẦU THÁM HIỂM KHOA HỌC 🚀';

  // Render cards and pills in selected language
  renderTopicLabCards(lang);
  renderFilterPills(lang);
  updateAllMascotsUI();
  updateHeaderAuthDisplay();

  // 3. Quiz Screen Top Buttons & Badges
  const quizQuitText = document.getElementById('quiz-quit-text');
  if (quizQuitText) quizQuitText.textContent = isEn ? 'Quit' : 'Thoát';

  const quizPauseText = document.getElementById('quiz-pause-text');
  if (quizPauseText) quizPauseText.textContent = isEn ? 'Pause' : 'Tạm dừng';

  const missionTag = document.getElementById('mission-badge-tag');
  if (missionTag) {
    missionTag.textContent = isEn ? '✨ SCIENCE EXPLORER • MULTIPLE CHOICE QUESTION ✨' : '✨ THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM ✨';
  }

  // Quiz Side Mascot Companion Panel
  const compLabel = document.getElementById('quiz-companion-label');
  if (compLabel) compLabel.textContent = isEn ? '🌟 COMPANION BUDDY' : '🌟 BẠN ĐỒNG HÀNH';

  const compChangeBtn = document.getElementById('quiz-change-mascot-btn');
  if (compChangeBtn) compChangeBtn.innerHTML = isEn ? '<span>Change</span> <span>▾</span>' : '<span>Đổi bạn</span> <span>▾</span>';

  const compTapHint = document.getElementById('quiz-mascot-tap-hint');
  if (compTapHint) compTapHint.innerHTML = isEn ? '<span>👆 Tap me for a hint!</span>' : '<span>👆 Bấm vào tớ để nghe mách nước!</span>';

  const statCombo = document.getElementById('quiz-stat-combo-label');
  if (statCombo) statCombo.textContent = isEn ? '🔥 Streak' : '🔥 Chuỗi đúng';

  const statScore = document.getElementById('quiz-stat-score-label');
  if (statScore) statScore.textContent = isEn ? '⭐ Star XP' : '⭐ Sao tích lũy';

  // SA Box
  const saInput = document.getElementById('sa-input-field');
  if (saInput) saInput.placeholder = isEn ? 'Type your answer here...' : 'Gõ câu trả lời của bé vào đây...';
  const btnSaSubmit = document.getElementById('btn-sa-submit');
  if (btnSaSubmit) btnSaSubmit.textContent = isEn ? 'Check Answer' : 'Kiểm tra đáp án';

  // 4. Modals: Quit, Pause, Leaderboard
  const quitTitle = document.getElementById('quit-modal-title');
  if (quitTitle) quitTitle.textContent = isEn ? 'Quit Mission?' : 'Dừng Bài Thi?';
  const quitDesc = document.getElementById('quit-modal-desc');
  if (quitDesc) quitDesc.textContent = isEn 
    ? 'Are you sure you want to stop this mission and return to Home? In-progress results will not be saved.' 
    : 'Bé có chắc muốn dừng bài thám hiểm này để về Trang Chủ không? Điểm số lượt thi này sẽ không được lưu nếu thoát ngang.';
  const quitCancel = document.getElementById('quit-modal-cancel');
  if (quitCancel) quitCancel.textContent = isEn ? 'Keep Playing' : 'Tiếp tục làm';
  const quitConfirm = document.getElementById('quit-modal-confirm');
  if (quitConfirm) quitConfirm.textContent = isEn ? 'Quit to Home ➔' : 'Đồng ý thoát ➔';

  const pauseTitle = document.getElementById('pause-modal-title');
  if (pauseTitle) pauseTitle.textContent = isEn ? 'Mission Paused' : 'Đang Tạm Dừng Bài Thi';
  const pauseDesc = document.getElementById('pause-modal-desc');
  if (pauseDesc) pauseDesc.textContent = isEn 
    ? 'Timer is paused! Take a short break, drink some water, and resume when ready!' 
    : 'Đồng hồ đã đóng băng. Bé hãy nghỉ ngơi chớp mắt, uống một ngụm nước rồi cùng bạn đồng hành tiếp tục nhé!';
  const pauseResume = document.getElementById('pause-modal-resume');
  if (pauseResume) pauseResume.textContent = isEn ? '▶️ Resume Mission' : '▶️ Tiếp tục làm bài';

  // Leaderboard Modal
  const leadTitle = document.getElementById('lead-title');
  if (leadTitle) leadTitle.innerHTML = isEn ? '<span>Weekly Stars Hall</span> <span class="text-amber-500 animate-bounce">🌟</span>' : '<span>Bảng Sao Tuần Này</span> <span class="text-amber-500 animate-bounce">🌟</span>';
  const leadSub = document.getElementById('lead-sub');
  if (leadSub) leadSub.textContent = isEn ? 'Top performing junior explorers of the week' : 'Top nhà thám hiểm nhí xuất sắc nhất tuần';
  const leadFilterLbl = document.getElementById('lead-filter-label');
  if (leadFilterLbl) leadFilterLbl.textContent = isEn ? 'Filter:' : 'Lọc:';

  const leadFilterClass = document.getElementById('lead-filter-class');
  if (leadFilterClass) {
    const opts = leadFilterClass.options;
    for (let i = 0; i < opts.length; i++) {
      const val = opts[i].value;
      if (val === 'all') {
        opts[i].textContent = isEn ? '🌟 All Grades' : '🌟 Tất cả các lớp';
      } else {
        const num = val.replace(/[^0-9]/g, '');
        opts[i].textContent = isEn ? `🎒 Grade ${num || val}` : `🎒 Lớp ${num || val}`;
      }
    }
  }

  const leadFwBtn = document.getElementById('lead-fireworks-btn-text');
  if (leadFwBtn) leadFwBtn.textContent = isEn ? '🎊 Celebrate 🎆' : '🎊 Bắn Pháo Hoa';

  const leadRankLbl = document.getElementById('lead-user-rank-label');
  if (leadRankLbl) leadRankLbl.textContent = isEn ? 'YOUR RANK' : 'VỊ TRÍ CỦA BẠN';

  const leadRecordLbl = document.getElementById('lead-user-record-label');
  if (leadRecordLbl) leadRecordLbl.textContent = isEn ? 'Weekly Record' : 'Kỷ Lục Tuần Này';

  const leadGrandBtn = document.getElementById('lead-grand-fireworks-text');
  if (leadGrandBtn) leadGrandBtn.textContent = isEn ? 'CELEBRATE WITH FIREWORKS 🎊' : 'BẮN PHÁO HOA ĂN MỪNG 🎊';

  // Leaderboard re-render if open
  const leadModal = document.getElementById('modal-leaderboard');
  if (leadModal && leadModal.classList.contains('active')) {
    filterLeaderboardView();
  }

  // 5. Result Screen
  const resTitle = document.getElementById('res-title');
  if (resTitle && (resTitle.textContent === 'Bé Làm Tốt Lắm!' || resTitle.textContent === 'Great Job Explorer!')) {
    resTitle.textContent = isEn ? 'Great Job Explorer!' : 'Bé Làm Tốt Lắm!';
  }
  const statScoreLbl = document.getElementById('stat-score-lbl');
  if (statScoreLbl) statScoreLbl.textContent = isEn ? 'SCORE' : 'ĐIỂM SỐ';
  const statCorrectLbl = document.getElementById('stat-correct-lbl');
  if (statCorrectLbl) statCorrectLbl.textContent = isEn ? 'CORRECT ✅' : 'CÂU ĐÚNG ✅';
  const statWrongLbl = document.getElementById('stat-wrong-lbl');
  if (statWrongLbl) statWrongLbl.textContent = isEn ? 'WRONG ❌' : 'CÂU SAI ❌';
  const statTimeLbl = document.getElementById('stat-time-lbl');
  if (statTimeLbl) statTimeLbl.textContent = isEn ? 'TIME ⏱️' : 'THỜI GIAN ⏱️';

  const btnReviewDetail = document.getElementById('btn-review-detail-text');
  if (btnReviewDetail) btnReviewDetail.textContent = isEn ? 'REVIEW QUIZ ANSWERS' : 'XEM LẠI CHI TIẾT BÀI LÀM';
  const btnViewStars = document.getElementById('btn-view-stars-text');
  if (btnViewStars) btnViewStars.textContent = isEn ? 'VIEW STARS HALL 🌟' : 'XEM BẢNG SAO TUẦN NÀY 🌟';
  const btnReplayWrong = document.getElementById('btn-replay-wrong-text');
  if (btnReplayWrong) btnReplayWrong.textContent = isEn ? 'Practice Wrong Answers' : 'Ôn lại câu sai';

  // 6. If Quiz is currently active, immediately re-render question & mission header
  const quizScreen = document.getElementById('quiz-screen');
  if (quizScreen && quizScreen.classList.contains('active') && typeof currentDeck !== 'undefined' && currentDeck && currentDeck.length > 0 && !isQuizSubmitted) {
    displayQuestion();
  }

  refreshLucideIcons();
}"""

if old_apply_lang_regex.search(content):
    content = old_apply_lang_regex.sub(new_apply_lang_code, content, count=1)
    print("applyLanguageToUI successfully replaced with comprehensive bilingual function.")
else:
    print("ERROR: Could not locate old applyLanguageToUI function.")
    sys.exit(1)

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated {HTML_FILE}. File size: {len(content)} bytes.")
