#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re, shutil

BASE_DIR = '/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz'
HTML_FILE = os.path.join(BASE_DIR, 'index.html')

print("Starting master update: User fixes (Figma AI -> Khoa học kì thú, fast loading, bilingual, broken image fix)...")
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. RENAME APP TO "Khoa học kì thú" & REMOVE "Figma AI"
# -------------------------------------------------------------
# Replace page title
content = content.replace(
    '<title>🔬 Khoa Học Vui - Đấu Trường Nhí 100 Câu</title>',
    '<title>🔬 Khoa Học Kì Thú - Đấu Trường Nhí 1000 Câu</title>'
)

# Header Logo & Title
old_header_title = """<div class="font-baloo font-bold text-base text-cyan-400 tracking-wide flex items-center gap-1.5 leading-tight">
          <span>BÉ NA SCIENCE LAB</span>
          <span class="text-[9px] bg-cyan-500/20 text-cyan-300 border border-cyan-400/30 px-2 py-0.5 rounded-full font-black uppercase">Figma AI</span>
        </div>"""

new_header_title = """<div class="font-baloo font-bold text-base text-cyan-400 tracking-wide flex items-center gap-1.5 leading-tight">
          <span id="app-title">KHOA HỌC KÌ THÚ</span>
        </div>"""

content = content.replace(old_header_title, new_header_title)

# Header tagline ID
content = content.replace(
    '<div class="text-[11px] text-slate-400">Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú</div>',
    '<div class="text-[11px] text-slate-400" id="header-tagline">Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú</div>'
)

# Music button ID
content = content.replace(
    '<button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-200 transition" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc">\n        <i data-lucide="volume-x" style="width:14px; height:14px;"></i>\n        <span>Nhạc</span>\n      </button>',
    '<button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-200 transition" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc">\n        <i data-lucide="volume-x" style="width:14px; height:14px;"></i>\n        <span id="music-btn-text">Nhạc</span>\n      </button>'
)

# -------------------------------------------------------------
# 2. FIX BROKEN IMAGE: REMOVE CSS DISPLAY:FLEX !IMPORTANT & ENSURE ROBUST HIDING
# -------------------------------------------------------------
old_css_img_card = """.question-img-card {
      max-height: 130px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      background: #F8FAFC !important;
      border-radius: 16px !important;
      overflow: hidden !important;
      border: 1px solid #E2E8F0 !important;
    }"""

new_css_img_card = """.question-img-card {
      max-height: 180px !important;
      border-radius: 16px !important;
      overflow: hidden !important;
    }
    .question-img-card.hidden,
    .question-img-card[style*="display: none"],
    #q-img-wrap.hidden,
    #q-img-wrap[style*="display: none"] {
      display: none !important;
    }"""

if old_css_img_card in content:
    content = content.replace(old_css_img_card, new_css_img_card)
else:
    content = re.sub(
        r'\.question-img-card\s*\{[^}]*max-height:\s*130px\s*!important;[^}]*display:\s*flex\s*!important;[^}]*\}',
        new_css_img_card,
        content
    )

# Fix HTML of q-img-wrap
old_q_img_html = """<div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm mx-auto" id="q-img-wrap" style="display:none;">
              <img id="question-img" src="" alt="Minh họa" style="width:100%; max-height:200px; object-fit:contain; display:block; margin:0 auto;">
            </div>"""

new_q_img_html = """<div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm mx-auto hidden" id="q-img-wrap" style="display:none !important;">
              <img id="question-img" src="" alt="" style="width:100%; max-height:200px; object-fit:contain; display:block; margin:0 auto;">
            </div>"""

if old_q_img_html in content:
    content = content.replace(old_q_img_html, new_q_img_html)
else:
    content = re.sub(
        r'<div[^>]*id=["\']q-img-wrap["\'][^>]*>.*?<img[^>]*id=["\']question-img["\'][^>]*>.*?</div>',
        new_q_img_html,
        content,
        flags=re.DOTALL
    )

# -------------------------------------------------------------
# 3. ADD MISSING IDS IN HOME SCREEN & MODALS
# -------------------------------------------------------------
content = content.replace(
    '<span>Chọn Phòng Thí Nghiệm & Bắt Đầu</span>',
    '<span id="home-section-title">Chọn Phòng Thí Nghiệm & Bắt Đầu</span>'
)
content = content.replace(
    '<span class="text-xs font-bold text-cyan-600">6 Labs Đã Sẵn Sàng</span>',
    '<span class="text-xs font-bold text-cyan-600" id="home-section-sub">6 Labs Đã Sẵn Sàng</span>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-600">🌐 Ngôn ngữ:</label>',
    '<label class="text-xs font-bold text-slate-600" id="label-lang-mode">🌐 Ngôn ngữ:</label>'
)
content = content.replace(
    '<span>Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>',
    '<span id="home-config-summary-text">Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>'
)
content = content.replace(
    '<span class="text-[10px] bg-slate-200 text-slate-700 font-extrabold px-2 py-0.5 rounded-full">Mở rộng ▾</span>',
    '<span class="text-[10px] bg-slate-200 text-slate-700 font-extrabold px-2 py-0.5 rounded-full" id="home-config-badge">Mở rộng ▾</span>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🔢 Số lượng câu hỏi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-size">🔢 Số lượng câu hỏi:</label>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-700">📚 Nguồn đề thi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-source">📚 Nguồn đề thi:</label>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🧠 Chế độ lặp lại:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-ratio">🧠 Chế độ lặp lại:</label>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🎚️ Độ khó câu hỏi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-diff">🎚️ Độ khó câu hỏi:</label>'
)
content = content.replace(
    '<label class="text-xs font-bold text-slate-700">👶 Phù hợp lứa tuổi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-age">👶 Phù hợp lứa tuổi:</label>'
)

# Leaderboard Fireworks Button
content = content.replace(
    '<span>🎊 Bắn Pháo Hoa</span>',
    '<span id="lead-fireworks-btn-text">🎊 Bắn Pháo Hoa</span>'
)

# -------------------------------------------------------------
# 4. INSERT GLOBAL TOPIC_EN_MAP & SOURCE_EN_MAP AT TOP OF SCRIPT
# -------------------------------------------------------------
global_maps = """
// =========================================================================
// BILINGUAL EN/VI TOPIC & SOURCE DICTIONARIES (FULL 11 TOPICS)
// =========================================================================
const TOPIC_EN_MAP = {
  'Động Vật': 'Animal Kingdom',
  'Thực Vật': 'Plants & Nature',
  'Vũ Trụ & Thời Tiết': 'Space & Weather',
  'Cơ Thể Người': 'Human Body & Health',
  'Con người & Sức khỏe': 'Human Body & Health',
  'Địa Lý Việt Nam': 'Geography & Earth',
  'Lịch Sử & Văn Hóa': 'History & Culture',
  'Vật Chất & Hiện Tượng': 'Matter & Physics',
  'Vật chất & Năng lượng': 'Matter & Energy',
  'Vật lý & Năng lượng': 'Physics & Energy',
  'Thực vật & Động vật': 'Plants & Animals',
  'Trái Đất & Bầu trời': 'Earth & Sky'
};

const SOURCE_EN_MAP = {
  'SGK Việt Nam (GDPT 2018)': 'National Curriculum (MOET)',
  'SGK Việt Nam': 'National Curriculum (MOET)',
  'Trạng Nguyên & Violympic': 'National Science Olympiad',
  'Kangaroo Khoa học (IKSC)': 'IKSC Kangaroo Science',
  'IXL & Khan Academy Khoa học': 'IXL & Khan Science',
  'IXL & Khan Academy': 'IXL & Khan Science',
  'National Geographic Kids': 'NatGeo Kids',
  'Khác': 'General Science'
};
"""

content = content.replace('<script>', '<script>\n' + global_maps, 1)

# -------------------------------------------------------------
# 5. FIX displayQuestion(): ENSURE ROBUST TRY-CATCH & INSTANT RENDERING
# -------------------------------------------------------------
# Replace displayQuestion completely to prevent any runtime error from halting question loading
old_display_q_regex = re.compile(
    r'function displayQuestion\(\)\s*\{.*?(?=\nfunction handleChoiceSelect)',
    re.DOTALL
)

new_display_q_func = """function displayQuestion() {
  try {
    if (!currentDeck || currentDeck.length === 0) {
      if (typeof MASTER_POOL !== 'undefined' && MASTER_POOL.length > 0) {
        currentDeck = MASTER_POOL.slice(0, 10);
      } else {
        return;
      }
    }

    if (currentIndex >= currentDeck.length) {
      currentIndex = currentDeck.length - 1;
    }
    const q = currentDeck[currentIndex] || {};
    const total = currentDeck.length;
    const isLast = (currentIndex === total - 1);

    const isEn = (currentLanguageMode === 'en');
    const isBi = (currentLanguageMode === 'bilingual');

    // 1. Question Number Pill
    const qNumPrefix = isEn ? 'Question' : 'Câu';
    const qNumElem = document.getElementById('question-number');
    if (qNumElem) {
      qNumElem.textContent = `${qNumPrefix} ${currentIndex + 1} / ${total} 🚀`;
    }

    // 2. Source Badge
    const badgeSource = document.getElementById('badge-source');
    if (badgeSource) {
      const rawSrc = q.source || 'Khoa học';
      const srcName = isEn ? (SOURCE_EN_MAP[rawSrc] || rawSrc) : rawSrc;
      badgeSource.innerHTML = `${getSourceIcon(q.source)} ${isEn ? 'Source' : 'Nguồn'}: ${srcName}`;
    }

    // 3. Topic & Grade Badge
    const badgeTopicAge = document.getElementById('badge-topic-age');
    if (badgeTopicAge) {
      const topicText = isEn ? (TOPIC_EN_MAP[q.topic] || q.topic || 'Science') : (q.topic || 'Khoa học');
      const gradeText = isEn ? (q.grade ? `Grade ${q.grade}` : (q.age ? `Grade ${q.age}` : 'Elementary')) : (q.grade ? `Lớp ${q.grade}` : (q.age ? `Lớp ${q.age}` : 'Tiểu học'));
      const diffText = isEn ? `Level ${q.diff || 1}` : `Mức ${q.diff || 1}`;
      badgeTopicAge.textContent = `${topicText} • ${gradeText} • ${diffText}`;
    }

    // 4. Mascot Companion Stats
    const answeredCount = Object.keys(userAnswersMap || {}).length;
    const streakCountElem = document.getElementById('quiz-mascot-streak-count');
    if (streakCountElem) {
      streakCountElem.textContent = isEn ? `${answeredCount} Done` : `${answeredCount} Đã làm`;
    }
    const scoreCountElem = document.getElementById('quiz-mascot-score-count');
    if (scoreCountElem) {
      scoreCountElem.textContent = `+${answeredCount * 20} XP`;
    }

    // 5. Question Text (Render immediately without delay)
    const qTextElem = document.getElementById('question-text');
    if (qTextElem) {
      if (isBi) {
        const enText = q.q_en || q.question_en || q.q || '';
        const viText = q.q || '';
        qTextElem.innerHTML = `
          <div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; margin-bottom:8px; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${enText}</div>
          <div style="font-size:1.02rem; color:#7DD3FC; font-weight:700; line-height:1.45; border-top:1px dashed rgba(255,255,255,0.25); padding-top:8px;">${viText}</div>
        `;
      } else if (isEn) {
        qTextElem.innerHTML = `<div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${q.q_en || q.question_en || q.q || ''}</div>`;
      } else {
        qTextElem.innerHTML = `<div style="font-size:1.18rem; font-weight:800; color:#FFFFFF; line-height:1.45; text-shadow:0 1px 3px rgba(0,0,0,0.5);">${q.q || ''}</div>`;
      }
    }

    // 6. Question Image (Clean async load - NEVER show broken placeholder)
    const imgElem = document.getElementById('question-img');
    const imgWrap = document.getElementById('q-img-wrap');
    if (imgElem && imgWrap) {
      imgWrap.style.setProperty('display', 'none', 'important');
      imgWrap.classList.add('hidden');
      imgElem.src = '';

      if (q.img && typeof q.img === 'string' && q.img.trim().length > 5 && (q.img.startsWith('http://') || q.img.startsWith('https://') || q.img.startsWith('data:image/'))) {
        const cleanUrl = q.img.trim();
        imgElem.onload = function() {
          imgWrap.style.setProperty('display', 'block', 'important');
          imgWrap.classList.remove('hidden');
        };
        imgElem.onerror = function() {
          this.onerror = null;
          imgWrap.style.setProperty('display', 'none', 'important');
          imgWrap.classList.add('hidden');
        };
        imgElem.src = cleanUrl;
      }
    }

    // 7. Mascot Cheer Dialogue
    setMascotMood('thinking', isEn 
      ? (isLast ? 'This is the final question! Review carefully when done! 🌟' : `Let\\'s explore question ${currentIndex + 1} together! 🚀`)
      : (isLast ? 'Bé ơi, đây là câu cuối cùng rồi! Làm xong bé kiểm tra lại nhé!' : `Bé ơi, cùng trả lời câu ${currentIndex + 1} nào!`));

    // 8. Progress Fill
    const pct = total > 0 ? (currentIndex / total) * 100 : 0;
    const progressFill = document.getElementById('progress-fill');
    if (progressFill) progressFill.style.width = pct + '%';

    // 9. Hide Explanation
    const expCard = document.getElementById('explanation-card');
    if (expCard) {
      expCard.className = 'explanation-card';
      expCard.style.setProperty('display', 'none', 'important');
    }

    // 10. Next Button
    const btnNext = document.getElementById('btn-next');
    if (btnNext) {
      if (userAnswersMap && userAnswersMap[q.id]) {
        btnNext.classList.add('visible');
      } else {
        btnNext.classList.remove('visible');
      }

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
      }
    }

    // 11. Render Choices
    if (q.type === 'SA') {
      const choicesList = document.getElementById('choices-list');
      if (choicesList) choicesList.style.display = 'none';
      const saBox = document.getElementById('sa-box');
      if (saBox) saBox.style.display = 'block';
      setupShortAnswer(q);
    } else {
      const saBox = document.getElementById('sa-box');
      if (saBox) saBox.style.display = 'none';
      const choicesList = document.getElementById('choices-list');
      if (choicesList) choicesList.style.display = 'flex';
      renderMultipleChoice(q);
    }

    refreshLucideIcons();
  } catch (err) {
    console.error('displayQuestion error handled:', err);
  }
}"""

if old_display_q_regex.search(content):
    content = old_display_q_regex.sub(new_display_q_func + '\n', content, count=1)
    print("Replaced displayQuestion with fast & robust try-catch version.")
else:
    print("WARNING: Could not find old displayQuestion regex.")

# -------------------------------------------------------------
# 6. FIX LEADERBOARD: ZERO-LATENCY INSTANT PODIUM & BILINGUAL
# -------------------------------------------------------------
old_lead_code_regex = re.compile(
    r'function fetchLeaderboardFromCloud\(\)\s*\{.*?function filterLeaderboardView',
    re.DOTALL
)

new_lead_code = """function renderLeaderboardList(players) {
  const listElem = document.getElementById('lead-players-list');
  if (!listElem) return;

  const isEn = (currentLanguageMode === 'en');

  if (!players || players.length === 0) {
    listElem.innerHTML = `<div style="text-align:center; padding:30px; color:#64748B;">${isEn ? 'No explorers yet for this grade. Be the first to join!' : 'Chưa có bạn nào trong lớp này. Bé hãy là người đầu tiên ghi danh nhé!'}</div>`;
    return;
  }

  let html = '';

  // NẾU CÓ TỪ 3 BẠN TRỞ LÊN: VẼ BỤC VINH QUANG PODIUM
  if (players.length >= 3) {
    const p1 = players[0];
    const p2 = players[1];
    const p3 = players[2];

    html += `
      <div class="podium-container flex items-end justify-center gap-2.5 mb-5 pt-3 select-none">
        
        <!-- HẠNG 2: BẠC -->
        <div class="flex flex-col items-center w-24">
          <div class="w-12 h-12 rounded-full border-2 border-slate-300 bg-slate-100 flex items-center justify-center text-xl mb-1 shadow-sm">
            🥈
          </div>
          <div class="font-baloo font-bold text-xs text-slate-900 truncate max-w-[85px] text-center">
            ${p2.name}
          </div>
          <div class="text-[11px] font-extrabold text-cyan-600 mb-1">
            ${p2.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-2nd w-full h-16 flex flex-col items-center justify-center text-white font-baloo font-black shadow-md">
            <span class="text-base">2</span>
            <span class="text-[9px] opacity-90">${isEn ? 'RUNNER-UP' : 'Á QUÂN'}</span>
          </div>
        </div>

        <!-- HẠNG 1: VÀNG (QUÁN QUÂN) -->
        <div class="flex flex-col items-center w-28 -mt-4 cursor-pointer" onclick="launchFireworks()" title="${isEn ? 'Tap Champion to celebrate with fireworks!' : 'Bấm vào Quán quân để bắn pháo hoa ăn mừng!'}">
          <div class="relative">
            <span class="absolute -top-3.5 left-1/2 -translate-x-1/2 text-base animate-bounce">👑</span>
            <div class="w-14 h-14 rounded-full border-3 border-amber-400 bg-amber-100 flex items-center justify-center text-2xl mb-1 shadow-lg ring-4 ring-amber-300/40">
              🥇
            </div>
          </div>
          <div class="font-baloo font-bold text-sm text-slate-900 truncate max-w-[95px] text-center">
            ${p1.name}
          </div>
          <div class="text-xs font-black text-amber-600 mb-1">
            ${p1.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-1st w-full h-24 flex flex-col items-center justify-center text-slate-950 font-baloo font-black shadow-xl">
            <span class="text-xl">1</span>
            <span class="text-[10px] tracking-wider font-extrabold">${isEn ? 'CHAMPION' : 'QUÁN QUÂN'}</span>
          </div>
        </div>

        <!-- HẠNG 3: ĐỒNG -->
        <div class="flex flex-col items-center w-24">
          <div class="w-12 h-12 rounded-full border-2 border-orange-300 bg-orange-100 flex items-center justify-center text-xl mb-1 shadow-sm">
            🥉
          </div>
          <div class="font-baloo font-bold text-xs text-slate-900 truncate max-w-[85px] text-center">
            ${p3.name}
          </div>
          <div class="text-[11px] font-extrabold text-orange-600 mb-1">
            ${p3.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-3rd w-full h-12 flex flex-col items-center justify-center text-white font-baloo font-black shadow-sm">
            <span class="text-base">3</span>
            <span class="text-[9px] opacity-90">${isEn ? '3RD PLACE' : 'QUÝ QUÂN'}</span>
          </div>
        </div>

      </div>
    `;
  }

  // DANH SÁCH XẾP HẠNG CÁC VỊ TRÍ TIẾP THEO
  html += '<div class="flex flex-col gap-2">';
  players.slice(players.length >= 3 ? 3 : 0).forEach((p, idx) => {
    const rank = (players.length >= 3 ? 4 : 1) + idx;
    html += `
      <div class="flex items-center justify-between p-3 rounded-2xl bg-white border border-slate-200 shadow-xs hover:border-cyan-300 transition">
        <div class="flex items-center gap-3">
          <span class="w-6 text-center font-baloo font-black text-xs text-slate-500">#${rank}</span>
          <div class="w-9 h-9 rounded-xl bg-slate-100 flex items-center justify-center text-lg">
            ${rank === 4 ? '🌟' : (rank === 5 ? '🚀' : '🔬')}
          </div>
          <div>
            <div class="font-baloo font-bold text-xs text-slate-900 leading-tight">${p.name}</div>
            <div class="text-[10px] text-slate-500 font-semibold">${p.studentClass || 'Lớp 2'} • ${p.badge || '🌱 Tân Binh'}</div>
          </div>
        </div>
        <div class="text-right">
          <div class="font-baloo font-black text-xs text-amber-600">${p.highestScore || 0}/10 ⭐</div>
          <div class="text-[9px] text-slate-400 font-bold">${p.totalTests || 1} ${isEn ? 'Missions' : 'Lượt thi'}</div>
        </div>
      </div>
    `;
  });
  html += '</div>';

  listElem.innerHTML = html;
}

function fetchLeaderboardFromCloud() {
  const isEn = (currentLanguageMode === 'en');
  
  // 1. Dữ liệu mặc định mẫu chất lượng cao để hiển thị NGAY LẬP TỨC 0ms
  const defaultStarExplorers = [
    { name: 'Bé Na (Thanh Do Trung)', studentClass: 'Lớp 2', totalTests: 15, highestScore: 10, badge: '👑 Đại Kiện Tướng' },
    { name: 'Minh Khôi', studentClass: 'Lớp 2', totalTests: 12, highestScore: 9.5, badge: '🥇 Học Sinh Xuất Sắc' },
    { name: 'Bảo An', studentClass: 'Lớp 3', totalTests: 10, highestScore: 9.0, badge: '🥈 Ong Chăm Chỉ' },
    { name: 'Tuệ Anh', studentClass: 'Lớp 1', totalTests: 8, highestScore: 8.5, badge: '🥈 Ong Chăm Chỉ' },
    { name: 'Hoàng Nam', studentClass: 'Lớp 4', totalTests: 6, highestScore: 8.0, badge: '🌱 Tân Binh' }
  ];

  // 2. Tổng hợp cùng dữ liệu THỰC TẾ từ máy
  const localHist = (typeof getLocalHistory === 'function') ? getLocalHistory() : [];
  const playerMap = {};

  defaultStarExplorers.forEach(p => {
    playerMap[p.name] = p;
  });

  localHist.forEach(r => {
    const name = (r.studentName || '').trim();
    if (name && name !== 'Học sinh' && name !== 'Quản Trị Viên (Admin)') {
      if (!playerMap[name]) {
        playerMap[name] = {
          name: name,
          studentClass: r.studentClass || 'Lớp 2',
          totalTests: 0,
          highestScore: 0,
          badge: '🌱 Tân Binh'
        };
      }
      playerMap[name].totalTests++;
      const s = parseFloat(String(r.score10 || r.score || '0').split('/')[0]) || 0;
      playerMap[name].highestScore = Math.max(playerMap[name].highestScore, s);
      if (playerMap[name].highestScore >= 9.5) playerMap[name].badge = '👑 Đại Kiện Tướng';
      else if (playerMap[name].highestScore >= 8.5) playerMap[name].badge = '🥇 Học Sinh Xuất Sắc';
      else if (playerMap[name].highestScore >= 7.0) playerMap[name].badge = '🥈 Ong Chăm Chỉ';
    }
  });

  cachedLeaderboard = Object.values(playerMap);
  cachedLeaderboard.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
  
  // Render ngay lập tức không để người dùng chờ đợi
  renderLeaderboardList(cachedLeaderboard);

  // 3. Nếu có cấu hình Apps Script Cloud, gọi bất đồng bộ với timeout 2.5s không làm đơ giao diện
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  if (scriptUrl && scriptUrl.startsWith('http')) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2500);
    fetch(`${scriptUrl}?action=getLeaderboard`, { signal: controller.signal })
      .then(res => res.json())
      .then(data => {
        clearTimeout(timeoutId);
        if (data && data.leaderboard && data.leaderboard.length > 0) {
          data.leaderboard.forEach(p => {
            if (p.name && p.name !== 'Học sinh' && p.name !== 'Quản Trị Viên (Admin)') {
              playerMap[p.name] = p;
            }
          });
          cachedLeaderboard = Object.values(playerMap);
          cachedLeaderboard.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
          renderLeaderboardList(cachedLeaderboard);
        }
      })
      .catch(() => {
        clearTimeout(timeoutId);
      });
  }
}

function filterLeaderboardView"""

if old_lead_code_regex.search(content):
    content = old_lead_code_regex.sub(new_lead_code, content, count=1)
    print("Leaderboard upgraded to zero-latency instant render & robust bilingual.")
else:
    print("WARNING: Could not find old_lead_code_regex.")

# -------------------------------------------------------------
# 7. UPDATE applyLanguageToUI(): ADD APP TITLE, FIREWORKS BTN, EXAM CONFIG
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
  const appTitle = document.getElementById('app-title');
  if (appTitle) appTitle.textContent = isEn ? 'FASCINATING SCIENCE' : 'KHOA HỌC KÌ THÚ';

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

  // 2. Home Screen Hero Banner
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
  if (labelLang) labelLang.textContent = isEn ? '🌐 Mode:' : '🌐 Ngôn ngữ:';

  // Update language mode select options
  const langModeSelect = document.getElementById('language-mode-select');
  if (langModeSelect) {
    const opts = langModeSelect.options;
    for (let i = 0; i < opts.length; i++) {
      if (opts[i].value === 'vi') opts[i].textContent = isEn ? '🇻🇳 Vietnamese' : '🇻🇳 Tiếng Việt';
      else if (opts[i].value === 'bilingual') opts[i].textContent = isEn ? '🌐 Bilingual (En - Vi)' : '🌐 Song ngữ Anh-Việt';
      else if (opts[i].value === 'en') opts[i].textContent = isEn ? '🇬🇧 English' : '🇬🇧 Tiếng Anh';
    }
  }

  // Update student class select options
  const classSelect = document.getElementById('student-class');
  if (classSelect) {
    const opts = classSelect.options;
    for (let i = 0; i < opts.length; i++) {
      const val = opts[i].value;
      if (val === 'all') {
        opts[i].textContent = isEn ? '🌟 All Grades' : '🌟 Tất cả (Lớp 1-5)';
      } else {
        const num = val.replace(/[^0-9]/g, '');
        opts[i].textContent = isEn ? `🎒 Grade ${num || val}` : `🎒 Lớp ${num || val}`;
      }
    }
  }

  // Home Section Headers
  const sectionTitle = document.getElementById('home-section-title');
  if (sectionTitle) sectionTitle.textContent = isEn ? 'SELECT LABORATORY & START' : 'Chọn Phòng Thí Nghiệm & Bắt Đầu';
  const sectionSub = document.getElementById('home-section-sub');
  if (sectionSub) sectionSub.textContent = isEn ? '6 Labs Ready' : '6 Labs Đã Sẵn Sàng';
  const filterLabel = document.getElementById('home-filter-label');
  if (filterLabel) filterLabel.textContent = isEn ? 'Filter topics:' : 'Lọc chủ đề:';

  // Home Exam Config Details
  const homeCfgSumm = document.getElementById('home-config-summary-text');
  if (homeCfgSumm) homeCfgSumm.textContent = isEn ? 'Exam Settings & Google Sheets Sync' : 'Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets';
  const homeCfgBadge = document.getElementById('home-config-badge');
  if (homeCfgBadge) homeCfgBadge.textContent = isEn ? 'Expand ▾' : 'Mở rộng ▾';
  const lblQuizSize = document.getElementById('label-quiz-size');
  if (lblQuizSize) lblQuizSize.textContent = isEn ? '🔢 Number of Questions:' : '🔢 Số lượng câu hỏi:';
  const lblQuizSrc = document.getElementById('label-quiz-source');
  if (lblQuizSrc) lblQuizSrc.textContent = isEn ? '📚 Question Sources:' : '📚 Nguồn đề thi:';
  const lblQuizRatio = document.getElementById('label-quiz-ratio');
  if (lblQuizRatio) lblQuizRatio.textContent = isEn ? '🧠 Review Mode:' : '🧠 Chế độ lặp lại:';
  const lblQuizDiff = document.getElementById('label-quiz-diff');
  if (lblQuizDiff) lblQuizDiff.textContent = isEn ? '🎚️ Question Difficulty:' : '🎚️ Độ khó câu hỏi:';
  const lblQuizAge = document.getElementById('label-quiz-age');
  if (lblQuizAge) lblQuizAge.textContent = isEn ? '👶 Target Age:' : '👶 Phù hợp lứa tuổi:';

  const homeStartBtn = document.getElementById('home-start-btn-text');
  if (homeStartBtn) homeStartBtn.textContent = isEn ? 'START SCIENCE EXPLORATION 🚀' : 'BẮT ĐẦU THÁM HIỂM KHOA HỌC';

  // Render cards and pills in selected language
  renderTopicLabCards(lang);
  renderFilterPills(lang);
  updateAllMascotsUI();
  updateHeaderAuthDisplay();
  if (typeof updatePoolCount === 'function') updatePoolCount();

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
    print("Replaced applyLanguageToUI successfully.")
else:
    print("WARNING: Could not find old_apply_lang_regex.")

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Master update complete! File size: {len(content)} bytes.")
