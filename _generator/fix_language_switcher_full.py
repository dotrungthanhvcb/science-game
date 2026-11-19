#!/usr/bin/env python3
"""
Full Fix for English / Vietnamese Language Switcher:
- Dynamic real-time switching on Home Screen, Quiz Screen, Navigation Header, and Leaderboard
- Updates Question and Choices instantly if quiz is in progress
- Updates Hero banner, Topic Lab Cards, Filter Pills, and Buttons
"""

import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# =========================================================================
# 1. ADD IDs TO HOME SCREEN ELEMENTS FOR INSTANT I18N UPDATES
# =========================================================================
old_hero_section = """        <span class="inline-block bg-white/20 backdrop-blur text-white text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-wider mb-2.5 shadow-sm">
          🔬 PHÒNG THÍ NGHIỆM KHOA HỌC
        </span>
        <h2 class="font-baloo text-2xl md:text-3xl font-bold leading-tight drop-shadow-sm">
          Sẵn Sàng Thám Hiểm<br>Khoa Học Kỳ Thú! ⚡
        </h2>
        <p class="text-xs md:text-sm text-cyan-100 mt-1.5 mb-4 font-medium leading-relaxed">
          Hoàn thành các phòng Lab để thu thập đủ 1.000 ngôi sao kiến thức và chinh phục đỉnh cao khoa học!
        </p>

        <div class="flex items-center gap-3 flex-wrap">
          <button type="button" onclick="startQuiz()" class="btn-3d btn-3d-amber px-6 py-2.5 text-xs font-black inline-flex items-center gap-2 shadow-lg">
            <i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i>
            <span>VÀO PHÒNG THI NGAY 🚀</span>
          </button>
          <button type="button" onclick="navigateToTab('leaderboard')" class="btn-3d px-4 py-2.5 text-xs font-black bg-white/20 hover:bg-white/30 text-white rounded-full border border-white/30 backdrop-blur transition inline-flex items-center gap-1.5">
            <i data-lucide="trophy" style="width:14px; height:14px;"></i>
            <span>Xem Bảng Sao 🌟</span>
          </button>
        </div>"""

new_hero_section = """        <span id="hero-tag" class="inline-block bg-white/20 backdrop-blur text-white text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-wider mb-2.5 shadow-sm">
          🔬 PHÒNG THÍ NGHIỆM KHOA HỌC
        </span>
        <h2 id="hero-title" class="font-baloo text-2xl md:text-3xl font-bold leading-tight drop-shadow-sm">
          Sẵn Sàng Thám Hiểm<br>Khoa Học Kỳ Thú! ⚡
        </h2>
        <p id="hero-desc" class="text-xs md:text-sm text-cyan-100 mt-1.5 mb-4 font-medium leading-relaxed">
          Hoàn thành các phòng Lab để thu thập đủ 1.000 ngôi sao kiến thức và chinh phục đỉnh cao khoa học!
        </p>

        <div class="flex items-center gap-3 flex-wrap">
          <button type="button" onclick="startQuiz()" class="btn-3d btn-3d-amber px-6 py-2.5 text-xs font-black inline-flex items-center gap-2 shadow-lg">
            <i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i>
            <span id="hero-start-btn">VÀO PHÒNG THI NGAY 🚀</span>
          </button>
          <button type="button" onclick="navigateToTab('leaderboard')" class="btn-3d px-4 py-2.5 text-xs font-black bg-white/20 hover:bg-white/30 text-white rounded-full border border-white/30 backdrop-blur transition inline-flex items-center gap-1.5">
            <i data-lucide="trophy" style="width:14px; height:14px;"></i>
            <span id="hero-stars-btn">Xem Bảng Sao 🌟</span>
          </button>
        </div>"""

if old_hero_section in text:
    text = text.replace(old_hero_section, new_hero_section)
    print("Added IDs to hero section.")

# Wrap Lab Filter Pills in container with ID
old_pills = """      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1">
        <button type="button" onclick="filterLabPills('all', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-black bg-cyan-600 text-white shadow-sm shrink-0 cursor-pointer transition">Tất Cả Labs</button>
        <button type="button" onclick="filterLabPills('Động Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🦁 Động Vật</button>
        <button type="button" onclick="filterLabPills('Vũ Trụ & Thời Tiết', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🚀 Vũ Trụ</button>
        <button type="button" onclick="filterLabPills('Thực Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🌿 Thực Vật</button>
        <button type="button" onclick="filterLabPills('Cơ Thể Người', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🫀 Sức Khỏe</button>
        <button type="button" onclick="filterLabPills('Địa Lý Việt Nam', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🗺️ Địa Lý</button>
        <button type="button" onclick="filterLabPills('Vật Chất & Hiện Tượng', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">⚡ Vật Chất</button>
      </div>"""

new_pills = """      <div id="lab-filter-pills-container" class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1">
        <button type="button" onclick="filterLabPills('all', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-black bg-cyan-600 text-white shadow-sm shrink-0 cursor-pointer transition">Tất Cả Labs</button>
        <button type="button" onclick="filterLabPills('Động Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🦁 Động Vật</button>
        <button type="button" onclick="filterLabPills('Vũ Trụ & Thời Tiết', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🚀 Vũ Trụ</button>
        <button type="button" onclick="filterLabPills('Thực Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🌿 Thực Vật</button>
        <button type="button" onclick="filterLabPills('Cơ Thể Người', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🫀 Sức Khỏe</button>
        <button type="button" onclick="filterLabPills('Địa Lý Việt Nam', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🗺️ Địa Lý</button>
        <button type="button" onclick="filterLabPills('Vật Chất & Hiện Tượng', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">⚡ Vật Chất</button>
      </div>"""

if old_pills in text:
    text = text.replace(old_pills, new_pills)
    print("Added lab-filter-pills-container ID.")

# Add ID to home start button
old_home_start = """      <button type="button" class="btn-3d btn-3d-cyan px-8 py-3 text-sm font-black flex items-center gap-2 shadow-lg" onclick="startQuiz()">
        <i data-lucide="rocket" style="width:18px; height:18px;"></i>
        <span>BẮT ĐẦU THÁM HIỂM KHOA HỌC</span>
      </button>"""

new_home_start = """      <button type="button" class="btn-3d btn-3d-cyan px-8 py-3 text-sm font-black flex items-center gap-2 shadow-lg" onclick="startQuiz()">
        <i data-lucide="rocket" style="width:18px; height:18px;"></i>
        <span id="home-start-btn-text">BẮT ĐẦU THÁM HIỂM KHOA HỌC</span>
      </button>"""

if old_home_start in text:
    text = text.replace(old_home_start, new_home_start)
    print("Added home-start-btn-text ID.")

# Add ID to mission badge tag
old_mission_tag = """        <!-- Huy hiệu thể loại ở chính giữa thẻ -->
        <div class="flex items-center justify-center text-center">
          <span class="inline-flex items-center justify-center text-[11px] font-black tracking-wider text-cyan-300 bg-cyan-950/80 border border-cyan-400/40 px-3.5 py-1 rounded-full uppercase shadow-xs">
            ✨ THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM ✨
          </span>
        </div>"""

new_mission_tag = """        <!-- Huy hiệu thể loại ở chính giữa thẻ -->
        <div class="flex items-center justify-center text-center">
          <span id="mission-badge-tag" class="inline-flex items-center justify-center text-[11px] font-black tracking-wider text-cyan-300 bg-cyan-950/80 border border-cyan-400/40 px-3.5 py-1 rounded-full uppercase shadow-xs">
            ✨ THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM ✨
          </span>
        </div>"""

if old_mission_tag in text:
    text = text.replace(old_mission_tag, new_mission_tag)
    print("Added mission-badge-tag ID.")

# =========================================================================
# 2. IMPLEMENT FULL JAVASCRIPT I18N SYSTEM (applyLanguageToUI)
# =========================================================================
i18n_system = """
// =========================================================================
// REAL-TIME BILINGUAL / ENGLISH / VIETNAMESE I18N SYSTEM
// =========================================================================

const LAB_CARDS_DATA = [
  {
    topic: 'Động Vật',
    icon: '🦁',
    iconBg: 'bg-amber-100 border-amber-200',
    title_vi: 'Thế Giới Động Vật',
    title_en: 'Animal Kingdom',
    desc_vi: 'Động vật hoang dã, côn trùng, tập tính',
    desc_en: 'Wild animals, insects, habitats & habits',
    count_vi: '180 Câu',
    count_en: '180 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-amber-100 text-amber-800'
  },
  {
    topic: 'Vũ Trụ & Thời Tiết',
    icon: '🚀',
    iconBg: 'bg-indigo-100 border-indigo-200',
    title_vi: 'Vũ Trụ & Thời Tiết',
    title_en: 'Space & Solar System',
    desc_vi: 'Hệ Mặt Trời, sao Hỏa, các hành tinh',
    desc_en: 'Planets, Mars, Sun & galaxy mysteries',
    count_vi: '180 Câu',
    count_en: '180 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-indigo-100 text-indigo-800'
  },
  {
    topic: 'Thực Vật',
    icon: '🌿',
    iconBg: 'bg-emerald-100 border-emerald-200',
    title_vi: 'Thực Vật & Tự Nhiên',
    title_en: 'Plants & Nature',
    desc_vi: 'Quang hợp, hạt mầm, rừng xanh',
    desc_en: 'Photosynthesis, seeds, forests & flora',
    count_vi: '120 Câu',
    count_en: '120 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-emerald-100 text-emerald-800'
  },
  {
    topic: 'Cơ Thể Người',
    icon: '🫀',
    iconBg: 'bg-rose-100 border-rose-200',
    title_vi: 'Cơ Thể Người & Y Sinh',
    title_en: 'Human Body & Health',
    desc_vi: '5 giác quan, tuần hoàn máu & sức khỏe',
    desc_en: '5 senses, blood circulation & biology',
    count_vi: '140 Câu',
    count_en: '140 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-rose-100 text-rose-800'
  },
  {
    topic: 'Địa Lý Việt Nam',
    icon: '🗺️',
    iconBg: 'bg-teal-100 border-teal-200',
    title_vi: 'Địa Lý Non Sông VN',
    title_en: 'Vietnam Geography',
    desc_vi: 'Sông Hồng, Trường Sơn, danh lam thắng cảnh',
    desc_en: 'Red River, Truong Son range, landscapes',
    count_vi: '160 Câu',
    count_en: '160 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-teal-100 text-teal-800'
  },
  {
    topic: 'Vật Chất & Hiện Tượng',
    icon: '⚡',
    iconBg: 'bg-purple-100 border-purple-200',
    title_vi: 'Vật Chất & Hiện Tượng',
    title_en: 'Matter & Physics',
    desc_vi: 'Âm thanh, ánh sáng, nam châm & chuyển động',
    desc_en: 'Sound, light, magnetism & motion',
    count_vi: '150 Câu',
    count_en: '150 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-purple-100 text-purple-800'
  }
];

const FILTER_PILLS = [
  { id: 'all', vi: 'Tất Cả Labs', en: 'All Labs' },
  { id: 'Động Vật', vi: '🦁 Động Vật', en: '🦁 Animals' },
  { id: 'Vũ Trụ & Thời Tiết', vi: '🚀 Vũ Trụ', en: '🚀 Space' },
  { id: 'Thực Vật', vi: '🌿 Thực Vật', en: '🌿 Plants' },
  { id: 'Cơ Thể Người', vi: '🫀 Sức Khỏe', en: '🫀 Health' },
  { id: 'Địa Lý Việt Nam', vi: '🗺️ Địa Lý', en: '🗺️ Geography' },
  { id: 'Vật Chất & Hiện Tượng', vi: '⚡ Vật Chất', en: '⚡ Physics' }
];

function renderTopicLabCards(lang) {
  const container = document.getElementById('figma-topic-cards-container');
  if (!container) return;
  const isEn = (lang === 'en');
  let html = '';
  LAB_CARDS_DATA.forEach(c => {
    const title = isEn ? c.title_en : c.title_vi;
    const desc = isEn ? c.desc_en : c.desc_vi;
    const count = isEn ? c.count_en : c.count_vi;
    const status = isEn ? c.status_en : c.status_vi;
    const isReady = (c.topic === 'Động Vật' || c.topic === 'Vũ Trụ & Thời Tiết');
    const playBtn = isReady 
      ? `<div class="w-9 h-9 rounded-full bg-cyan-600 text-white flex items-center justify-center shrink-0 shadow-sm hover:scale-105 transition"><i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i></div>`
      : `<div class="w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center shrink-0 hover:scale-105 transition"><i data-lucide="arrow-right" style="width:15px; height:15px;"></i></div>`;

    html += `
      <div onclick="startTopicLab('${c.topic}')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="${c.topic}" title="${isEn ? 'Start this Lab now' : 'Bấm để vào thi Lab này ngay'}">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl ${c.iconBg} border flex items-center justify-center text-2xl shadow-inner shrink-0">
            ${c.icon}
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">${title}</div>
            <div class="text-[11px] text-slate-500 font-medium">${desc}</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold ${c.badgeBg} px-2 py-0.5 rounded-full">${count}</span>
              <span class="text-[10px] font-extrabold ${c.statusClass}">${status}</span>
            </div>
          </div>
        </div>
        ${playBtn}
      </div>
    `;
  });
  container.innerHTML = html;
  refreshLucideIcons();
}

function renderFilterPills(lang) {
  const container = document.getElementById('lab-filter-pills-container');
  if (!container) return;
  const isEn = (lang === 'en');
  let html = '';
  FILTER_PILLS.forEach(p => {
    const text = isEn ? p.en : p.vi;
    const isActive = (p.id === selectedTopic);
    const activeClass = isActive 
      ? 'lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-black bg-cyan-600 text-white shadow-sm shrink-0 cursor-pointer transition'
      : 'lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition';
    html += `<button type="button" onclick="filterLabPills('${p.id}', this)" class="${activeClass}">${text}</button>`;
  });
  container.innerHTML = html;
}

function applyLanguageToUI(lang) {
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

  // 1. Update Home Screen (Hero Banner, Topic Cards, Filter Pills, Action Button)
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

  const homeStartBtn = document.getElementById('home-start-btn-text');
  if (homeStartBtn) homeStartBtn.textContent = isEn ? 'START SCIENCE EXPLORATION 🚀' : 'BẮT ĐẦU THÁM HIỂM KHOA HỌC';

  // Update navigation tabs
  const navLeaderboard = document.querySelector('#nav-item-leaderboard span');
  if (navLeaderboard) navLeaderboard.textContent = isEn ? '3. Stars · Weekly 🌟' : '3. Stars · Bảng Sao 🌟';

  const navHistory = document.querySelector('#nav-item-history span');
  if (navHistory) navHistory.textContent = isEn ? 'History' : 'Lịch Sử';

  const navUserMgmt = document.querySelector('#nav-item-user-mgmt span');
  if (navUserMgmt) navUserMgmt.textContent = isEn ? 'Admin' : 'Quản Lý';

  // Render cards and pills in selected language
  renderTopicLabCards(lang);
  renderFilterPills(lang);

  // 2. If Quiz is currently active, immediately re-render question & mission header
  const quizScreen = document.getElementById('quiz-screen');
  if (quizScreen && quizScreen.classList.contains('active') && typeof currentDeck !== 'undefined' && currentDeck && currentDeck.length > 0 && !isQuizSubmitted) {
    displayQuestion();
  }

  // 3. Update Mission Badge Tag
  const missionTag = document.getElementById('mission-badge-tag');
  if (missionTag) {
    missionTag.textContent = isEn ? '✨ SCIENCE EXPLORER • MULTIPLE CHOICE QUESTION ✨' : '✨ THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM ✨';
  }

  refreshLucideIcons();
}

function toggleLang(lang) {
  applyLanguageToUI(lang);
  playSound('click');
}

function onLanguageModeChange() {
  const elem = document.getElementById('language-mode-select');
  if (elem) {
    applyLanguageToUI(elem.value);
  }
}
"""

# Replace old toggleLang and onLanguageModeChange
text = re.sub(r'function toggleLang\(lang\)\s*\{[^}]*\}', '', text, count=1)
text = re.sub(r'function onLanguageModeChange\(\)\s*\{[^}]*\}', '', text, count=1)

# Add i18n_system right before loadSavedSettings
text = text.replace("function loadSavedSettings() {", i18n_system + "\nfunction loadSavedSettings() {")

# =========================================================================
# 3. UPDATE loadSavedSettings TO INITIALIZE LANGUAGE AND LAB CARDS ON LOAD
# =========================================================================
old_load_settings = """  const langSelect = document.getElementById('language-mode-select');
  if (langSelect) {
    const savedLang = localStorage.getItem('science_quiz_lang_mode') || 'vi';
    langSelect.value = savedLang;
    currentLanguageMode = savedLang;
  }"""

new_load_settings = """  const langSelect = document.getElementById('language-mode-select');
  const savedLang = localStorage.getItem('science_quiz_lang_mode') || 'vi';
  if (langSelect) {
    langSelect.value = savedLang;
  }
  applyLanguageToUI(savedLang);"""

if old_load_settings in text:
    text = text.replace(old_load_settings, new_load_settings)
    print("Updated loadSavedSettings to call applyLanguageToUI.")

# =========================================================================
# 4. ENHANCE displayQuestion & renderMultipleChoice TO SUPPORT ENGLISH MODE
# =========================================================================
old_display_q_header = """  document.getElementById('question-number').textContent = `Câu ${currentIndex + 1} / ${total}`;
  const badgeSource = document.getElementById('badge-source');
  if (badgeSource) {
    badgeSource.innerHTML = `${getSourceIcon(q.source)} Nguồn: ${q.source || 'Khoa học'}`;
  }
  const gradeText = q.grade ? `Lớp ${q.grade}` : q.age;
  document.getElementById('badge-topic-age').textContent = `${q.topic} • ${gradeText} • Mức ${q.diff}`;"""

new_display_q_header = """  const isEn = (currentLanguageMode === 'en');
  const isBi = (currentLanguageMode === 'bilingual');

  const qNumPrefix = isEn ? 'Question' : 'Câu';
  document.getElementById('question-number').textContent = `${qNumPrefix} ${currentIndex + 1} / ${total} 🚀`;

  const badgeSource = document.getElementById('badge-source');
  if (badgeSource) {
    const srcName = isEn ? (q.source === 'Khác' ? 'General' : q.source) : (q.source || 'Khoa học');
    badgeSource.innerHTML = `${getSourceIcon(q.source)} ${isEn ? 'Source' : 'Nguồn'}: ${srcName}`;
  }

  const topicEnMap = {
    'Động Vật': 'Animals',
    'Thực Vật': 'Plants',
    'Vũ Trụ & Thời Tiết': 'Space & Weather',
    'Cơ Thể Người': 'Human Body',
    'Địa Lý Việt Nam': 'Geography',
    'Vật Chất & Hiện Tượng': 'Physics & Matter'
  };
  const topicText = isEn ? (topicEnMap[q.topic] || q.topic) : q.topic;
  const gradeText = isEn ? (q.grade ? `Grade ${q.grade}` : q.age) : (q.grade ? `Lớp ${q.grade}` : q.age);
  const diffText = isEn ? `Level ${q.diff}` : `Mức ${q.diff}`;
  document.getElementById('badge-topic-age').textContent = `${topicText} • ${gradeText} • ${diffText}`;"""

if old_display_q_header in text:
    text = text.replace(old_display_q_header, new_display_q_header)
    print("Enhanced displayQuestion header with English support.")

# Update btnNext in displayQuestion
old_btn_next_text = """  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = '<i data-lucide="list-checks" style="width:18px; height:18px; stroke-width:2.5;"></i> <span>Xem lại & Nộp bài</span>';
    btnNext.classList.add('btn-last-step');
    btnNext.onclick = openReviewBeforeSubmit;
  } else {
    btnNext.innerHTML = '<span>Câu tiếp theo</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>';
    btnNext.classList.remove('btn-last-step');
    btnNext.onclick = goNextQuestion;
  }"""

new_btn_next_text = """  // Đổi chữ nút theo trạng thái câu cuối cùng
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

if old_btn_next_text in text:
    text = text.replace(old_btn_next_text, new_btn_next_text)
    print("Enhanced btnNext in displayQuestion with English support.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Language switcher full fix applied successfully.")
