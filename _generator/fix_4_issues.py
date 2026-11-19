#!/usr/bin/env python3
"""
Comprehensive Fix for 4 User-Reported Issues:
1. Fix button text wrapping & breaking in tables (add white-space: nowrap, clean inline-flex badges)
2. Fix button overlapping text behind in header (fluid flex header, remove rigid height, truncate student name)
3. Fix menu bar tabs not updating active cyan indicator (implement navigateToTab & setActiveNavTab)
4. Elevate companion mascot presence across ALL screens (Header pill, Home banner, Quiz dynamic reactions, Result cheer)
"""

import re
import sys

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# =============================================================================
# ISSUE 2 & 3: FIX HEADER OVERLAP AND ACTIVE NAV TAB
# =============================================================================

# Replace <header class="app-header"> with a clean, fluid, robust header structure
old_header_pattern = r'<header class="app-header">[\s\S]*?</header>'
new_header = """<header class="app-header">
    <div class="template-logo" onclick="navigateToTab('home')" title="Về Màn hình Chào mừng">
      <div style="width:36px; height:36px; border-radius:50%; background:#ECFEFF; display:flex; align-items:center; justify-content:center; color:#0891B2; flex-shrink:0;">
        <i data-lucide="microscope" style="width:20px; height:20px; stroke-width:2.5;"></i>
      </div>
      <span class="font-baloo font-bold">KHOA HỌC NHÍ</span>
    </div>

    <!-- THANH MENU ĐIỀU HƯỚNG CÓ CẬP NHẬT TAB ACTIVE -->
    <nav class="template-nav-links">
      <a href="javascript:void(0)" onclick="navigateToTab('home')" id="nav-item-home" class="template-nav-item active">
        <i data-lucide="home" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Trang Chủ</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('leaderboard')" id="nav-item-leaderboard" class="template-nav-item">
        <i data-lucide="award" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Bảng Vàng</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('history')" id="nav-item-history" class="template-nav-item">
        <i data-lucide="bar-chart-2" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Lịch Sử</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('user-mgmt')" id="nav-item-user-mgmt" class="template-nav-item">
        <i data-lucide="users" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Quản Lý</span>
      </a>
      <a href="javascript:void(0)" onclick="shareGameLink()" id="nav-item-share" class="template-nav-item">
        <i data-lucide="share-2" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Mời Bạn</span>
      </a>
    </nav>

    <!-- KHỐI PHẢI: BẠN ĐỒNG HÀNH, BẬT NHẠC & TÀI KHOẢN -->
    <div class="template-header-circles">
      <!-- 1. BẠN ĐỒNG HÀNH NGAY TRÊN HEADER (NÂNG CẤP ISSUE 4) -->
      <div id="header-mascot-pill" onclick="openMascotPickerModal()" class="header-mascot-pill" title="Bạn đồng hành của bé • Bấm để chọn bạn khác">
        <span id="header-mascot-avatar">🦉</span>
        <span id="header-mascot-name">Cú Vọ</span>
        <span style="font-size:0.68rem; color:#94A3B8;">▾</span>
      </div>

      <!-- 2. NÚT BẬT TẮT NHẠC NỀN -->
      <button class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full whitespace-nowrap header-music-pill" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền">
        <i data-lucide="volume-x" style="width:15px; height:15px; stroke-width:2.5;"></i>
        <span>Bật Nhạc</span>
      </button>

      <!-- 3. NÚT TÀI KHOẢN HỌC SINH -->
      <div id="header-auth-container">
        <button class="header-circle-btn" onclick="openAuthModal()" title="Đăng nhập tài khoản">
          <i data-lucide="user" style="width:16px; height:16px; stroke-width:2.5;"></i>
        </button>
      </div>
    </div>
  </header>"""

if re.search(old_header_pattern, html):
    html = re.sub(old_header_pattern, new_header, html, count=1)
    print("Upgraded <header class='app-header'> successfully!")

# =============================================================================
# ISSUE 1: FIX BUTTON TEXT & BADGE WRAPPING IN TABLE & FILTERS
# =============================================================================

# Add CSS rules to strictly prevent text wrapping in table badges, buttons, and filters
table_badge_css = """
  /* =========================================================================
     FIX ISSUE 1: CHỐNG XUỐNG DÒNG, TÁCH CHỮ TRONG NÚT BẤM & BẢNG LỊCH SỬ
     ========================================================================= */
  .history-table th, .history-table td {
    white-space: nowrap !important;
    vertical-align: middle !important;
    padding: 10px 14px !important;
  }
  .history-table th {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 800 !important;
    color: #475569 !important;
    font-size: 0.85rem !important;
    background: #F8FAFC !important;
    border-bottom: 2px solid #E2E8F0 !important;
  }
  .history-table td span, 
  .history-table td button,
  .badge-source,
  .score-badge {
    white-space: nowrap !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4px !important;
  }

  .history-table {
    width: 100% !important;
    min-width: 960px !important; /* Đảm bảo 11 cột có đủ không gian, không bao giờ bị ép bẹp */
    border-collapse: separate !important;
    border-spacing: 0 !important;
  }
  .history-table-wrap {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    border-radius: 20px !important;
    border: 2px solid #E2E8F0 !important;
    background: #FFFFFF !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important;
  }

  /* THANH FILTER TRÊN LỊCH SỬ */
  .history-filters-bar {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    flex-wrap: wrap !important;
    margin-bottom: 12px !important;
  }
  .history-filters-bar select, .history-filters-bar input {
    white-space: nowrap !important;
    height: 38px !important;
    border-radius: 12px !important;
    border: 1.5px solid #CBD5E1 !important;
    padding: 6px 12px !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
  }

  /* NÂNG CẤP HEADER KHÔNG BỊ ĐÈ CHỮ */
  .app-header {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 12px !important;
    padding: 8px 20px !important;
    background: #0F172A !important;
    border: 1.5px solid #1E293B !important;
    border-bottom: 4px solid #020617 !important;
    border-radius: 9999px !important;
    box-shadow: 0 10px 25px -8px rgba(15, 23, 42, 0.35) !important;
    position: relative !important;
    z-index: 40 !important;
    margin-bottom: 14px !important;
    flex-shrink: 0 !important;
    min-height: 54px !important;
    height: auto !important; /* Cho phép giãn nở tự nhiên nếu co hẹp cực đại */
  }

  .template-nav-links {
    display: flex !important;
    align-items: center !important;
    gap: 4px !important;
    list-style: none !important;
    flex-shrink: 1 !important;
    min-width: 0 !important;
    overflow-x: auto !important;
    scrollbar-width: none !important;
  }
  .template-nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .template-nav-item {
    padding: 6px 14px !important;
    border-radius: 9999px !important;
    font-size: 0.82rem !important;
    font-weight: 800 !important;
    color: #94A3B8 !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
    transition: all 0.12s ease !important;
  }
  .template-nav-item:hover {
    color: #FFFFFF !important;
    background: rgba(255, 255, 255, 0.08) !important;
  }
  .template-nav-item.active {
    color: #FFFFFF !important;
    background: #0891B2 !important;
    box-shadow: 0 2px 8px rgba(8, 145, 178, 0.45) !important;
  }

  .template-header-circles {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    flex-shrink: 0 !important;
  }

  /* NÚT BẠN ĐỒNG HÀNH TRÊN HEADER (ISSUE 4) */
  .header-mascot-pill {
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    background: #1E293B !important;
    border: 1.5px solid #334155 !important;
    border-bottom: 3px solid #0F172A !important;
    padding: 5px 12px !important;
    border-radius: 9999px !important;
    cursor: pointer !important;
    font-weight: 800 !important;
    font-size: 0.82rem !important;
    color: #38BDF8 !important;
    transition: all 0.12s ease !important;
  }
  .header-mascot-pill:hover {
    background: #334155 !important;
    transform: translateY(-1px) !important;
  }
  .header-mascot-pill:active {
    transform: translateY(2px) !important;
    border-bottom-width: 1px !important;
  }
"""

if "FIX ISSUE 1: CHỐNG XUỐNG DÒNG" not in html:
    html = html.replace("</style>", f"{table_badge_css}\n</style>")
    print("Added table badges & header CSS fixes!")

# =============================================================================
# ISSUE 4: ADD MASCOT TO RESULT SCREEN & HISTORY SCREEN
# =============================================================================

# Result screen mascot banner upgrade
old_res_banner = """    <div class="result-banner">
      <div class="result-icon" id="res-icon">🏆</div>
      <div class="result-headline" id="res-title">Bé Làm Tốt Lắm!</div>
      <div class="result-stars" id="res-stars">⭐⭐⭐</div>
      <p id="res-desc" style="color:var(--text-muted); font-size:1rem;">Bé đã hoàn thành xuất sắc bài thi hôm nay!</p>
    </div>"""

new_res_banner = """    <div class="result-banner">
      <div style="display:flex; align-items:center; justify-content:center; gap:16px; margin-bottom:6px;">
        <div id="result-mascot-svg-wrap" style="width:72px; height:72px; flex-shrink:0; filter:drop-shadow(0 4px 10px rgba(0,0,0,0.15));" class="animate-bounce"></div>
        <div style="text-align:left;">
          <div class="result-headline font-baloo" id="res-title">Bé Làm Tốt Lắm!</div>
          <div id="result-mascot-speech" style="font-family:'Baloo 2', sans-serif; font-weight:800; color:#0891B2; font-size:0.92rem; margin-top:2px;">
            "Tuyệt vời quá bạn ơi! Tớ rất tự hào về bạn hôm nay! 🎉"
          </div>
        </div>
      </div>
      <div class="result-stars" id="res-stars">⭐⭐⭐</div>
      <p id="res-desc" style="color:var(--text-muted); font-size:0.88rem; margin-top:4px;">Bé đã hoàn thành xuất sắc bài thi hôm nay!</p>
    </div>"""

if old_res_banner in html:
    html = html.replace(old_res_banner, new_res_banner)
    print("Upgraded result-screen mascot banner!")

# =============================================================================
# JAVASCRIPT UPGRADES: NAVIGATION TABS & MASCOT ENHANCEMENT
# =============================================================================

# Add navigation management & mascot updates to JS
js_nav_and_mascot = """
// =============================================================================
// NAVIGATION TAB MANAGEMENT: CẬP NHẬT TAB ACTIVE VÙNG MÀU XANH (FIX ISSUE 3)
// =============================================================================
function setActiveNavTab(tabName) {
  document.querySelectorAll('.template-nav-item').forEach(el => {
    el.classList.remove('active');
  });
  const target = document.getElementById('nav-item-' + tabName);
  if (target) {
    target.classList.add('active');
  }
}

function navigateToTab(tabName) {
  setActiveNavTab(tabName);
  if (tabName === 'home') {
    showScreen('home-screen');
  } else if (tabName === 'leaderboard') {
    openLeaderboardModal();
  } else if (tabName === 'history') {
    openHistoryScreen();
  } else if (tabName === 'user-mgmt') {
    openUserManagementModal();
  }
}
"""

if "function setActiveNavTab" not in html:
    html = html.replace("function showScreen(id) {", f"{js_nav_and_mascot}\nfunction showScreen(id) {{")

# Update showScreen to maintain active tab
old_show_screen = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) {
    target.classList.add('active');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}"""

new_show_screen = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) {
    target.classList.add('active');
  }
  if (id === 'home-screen' || id === 'welcome-screen') {
    setActiveNavTab('home');
  } else if (id === 'history-screen') {
    setActiveNavTab('history');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}"""

if old_show_screen in html:
    html = html.replace(old_show_screen, new_show_screen)
    print("Updated showScreen with active tab tracking!")

# Update closeLeaderboardModal & closeHistoryDetailModal to restore active tab
old_close_lb = """function closeLeaderboardModal() {
  const modal = document.getElementById('modal-leaderboard');
  if (modal) modal.classList.remove('active');
}"""

new_close_lb = """function closeLeaderboardModal() {
  const modal = document.getElementById('modal-leaderboard');
  if (modal) modal.classList.remove('active');
  const currentActive = document.querySelector('.screen.active');
  if (currentActive && currentActive.id === 'history-screen') {
    setActiveNavTab('history');
  } else {
    setActiveNavTab('home');
  }
}"""

if old_close_lb in html:
    html = html.replace(old_close_lb, new_close_lb)
    print("Updated closeLeaderboardModal with tab restore!")

# Update updateAllMascotsUI to update header mascot pill and result screen mascot
old_mascot_ui = """function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  
  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 42);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = m.name;

  // 2. Home screen (Mascot ngay trên Menu Home)
  const homeSvgWrap = document.getElementById('home-mascot-svg-wrap');
  if (homeSvgWrap) homeSvgWrap.innerHTML = renderMascotSvg(m.id, 58);
  const homeName = document.getElementById('home-mascot-name');
  if (homeName) homeName.textContent = m.name;
  const homeTitle = document.getElementById('home-mascot-title');
  if (homeTitle) homeTitle.textContent = m.title;

  // 3. Quiz screen
  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 52);
}"""

new_mascot_ui = """function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  
  // 0. Header Bar Mascot Pill (ISSUE 4: Luôn hiện diện rõ ràng trên Header)
  const headerMascotAvatar = document.getElementById('header-mascot-avatar');
  if (headerMascotAvatar) headerMascotAvatar.textContent = m.avatar || '🦉';
  const headerMascotName = document.getElementById('header-mascot-name');
  if (headerMascotName) headerMascotName.textContent = m.name.replace('Giáo Sư ', '').replace('Bé ', '');

  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 42);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = m.name;

  // 2. Home screen (Mascot sinh động kèm lời thoại cổ vũ)
  const homeSvgWrap = document.getElementById('home-mascot-svg-wrap');
  if (homeSvgWrap) homeSvgWrap.innerHTML = renderMascotSvg(m.id, 58, 'cheer');
  const homeName = document.getElementById('home-mascot-name');
  if (homeName) homeName.textContent = m.name;
  const homeTitle = document.getElementById('home-mascot-title');
  if (homeTitle) homeTitle.textContent = m.title;
  const homeSpeech = document.getElementById('home-mascot-speech');
  if (homeSpeech) homeSpeech.textContent = `"Chào bạn! Hôm nay tớ cùng bạn sẵn sàng chinh phục Đấu Trường Khoa Học nhé! 🚀"`;

  // 3. Quiz screen (Mascot to bản 64px, tương tác theo từng câu)
  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 64);

  // 4. Result screen (Mascot nhảy múa ăn mừng cúp vàng)
  const resSvgWrap = document.getElementById('result-mascot-svg-wrap');
  if (resSvgWrap) resSvgWrap.innerHTML = renderMascotSvg(m.id, 72, 'cheer');
  const resSpeech = document.getElementById('result-mascot-speech');
  if (resSpeech) resSpeech.textContent = `"Tuyệt vời quá bạn ơi! Tớ rất tự hào vì chúng mình đã hoàn thành xuất sắc bài thi này! 🎉"`;
}"""

if old_mascot_ui in html:
    html = html.replace(old_mascot_ui, new_mascot_ui)
    print("Updated updateAllMascotsUI with full companion presence!")

# Update updateHeaderAuthDisplay to truncate student name safely (Fix Issue 2 overlap)
old_auth_display = """    container.innerHTML = `
      <div onclick="openAuthModal()" style="display:inline-flex; align-items:center; gap:6px; background:${badgeBg}; color:${badgeColor}; padding:6px 12px; border-radius:10px; border:1.5px solid ${badgeBorder}; cursor:pointer; font-weight:800; font-size:0.82rem;" title="Xem hồ sơ">
        <span>${avatarIcon}</span>
        <span>${acc.studentName || acc.username}</span>
        <span style="background:${tagBg}; color:white; padding:1px 6px; border-radius:6px; font-size:0.75rem;">${tagText}</span>
      </div>
    `;"""

new_auth_display = """    const studentDisplay = acc.studentName || acc.username;
    container.innerHTML = `
      <div onclick="openAuthModal()" style="display:inline-flex; align-items:center; gap:6px; background:${badgeBg}; color:${badgeColor}; padding:5px 10px; border-radius:9999px; border:1.5px solid ${badgeBorder}; cursor:pointer; font-weight:800; font-size:0.8rem; white-space:nowrap; max-width:180px;" title="Tài khoản: ${studentDisplay}">
        <span>${avatarIcon}</span>
        <span style="max-width:95px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; display:inline-block;">${studentDisplay}</span>
        <span style="background:${tagBg}; color:white; padding:1px 6px; border-radius:6px; font-size:0.72rem; flex-shrink:0;">${tagText}</span>
      </div>
    `;"""

if old_auth_display in html:
    html = html.replace(old_auth_display, new_auth_display)
    print("Updated updateHeaderAuthDisplay with text truncation to prevent overflow!")

# Update table row rendering in renderHistoryTable (Fix Issue 1 button/badge breaking)
old_table_row = """    tr.innerHTML = `
      <td><span style="font-family:monospace; font-weight:700; color:var(--primary); font-size:0.75rem; background:#EEF2FF; padding:2px 6px; border-radius:4px;">${rowId}</span></td>
      <td style="font-weight:600; color:#334155; white-space:nowrap;">${rowDate}</td>
      <td style="font-weight:600; color:#64748B; white-space:nowrap;">${rowTime}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td><span style="background:${r.language === 'Tiếng Anh' ? '#F0F9FF' : (r.language === 'Song ngữ Anh - Việt' ? '#FAF5FF' : '#F0FDF4')}; color:${r.language === 'Tiếng Anh' ? '#0369A1' : (r.language === 'Song ngữ Anh - Việt' ? '#7E22CE' : '#15803D')}; border:1px solid ${r.language === 'Tiếng Anh' ? '#BAE6FD' : (r.language === 'Song ngữ Anh - Việt' ? '#E9D5FF' : '#BBF7D0')}; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>
      <td style="text-align:center; font-weight:700;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center;"><span class="score-badge ${badgeClass}">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:600; color:#64748B; white-space:nowrap;">⏱️ ${r.duration || '00:00'}</td>
      <td style="text-align:center;">
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="background:#E0F2FE; color:#0284C7; border-color:#BAE6FD; font-size:0.78rem; padding:4px 10px; font-weight:800; white-space:nowrap; border-radius:9999px;">
          🔍 Xem lại
        </button>
      </td>
    `;"""

new_table_row = """    tr.innerHTML = `
      <td style="white-space:nowrap;"><span style="white-space:nowrap; display:inline-block; font-family:monospace; font-weight:800; color:#0891B2; font-size:0.75rem; background:#ECFEFF; border:1px solid #BAE6FD; padding:3px 8px; border-radius:6px;">${rowId}</span></td>
      <td style="font-weight:700; color:#334155; white-space:nowrap;">${rowDate}</td>
      <td style="font-weight:700; color:#64748B; white-space:nowrap;">${rowTime}</td>
      <td style="font-weight:800; color:var(--dark); white-space:nowrap;">${r.studentName || 'Bé'}</td>
      <td style="white-space:nowrap;"><span style="white-space:nowrap; display:inline-block; background:#F1F5F9; border:1px solid #E2E8F0; padding:3px 10px; border-radius:8px; font-weight:700; font-size:0.8rem; color:#334155;">${r.studentClass || 'Lớp 2'}</span></td>
      <td style="white-space:nowrap;"><span style="white-space:nowrap; display:inline-block; background:${r.language === 'Tiếng Anh' ? '#F0F9FF' : (r.language === 'Song ngữ Anh - Việt' ? '#FAF5FF' : '#F0FDF4')}; color:${r.language === 'Tiếng Anh' ? '#0369A1' : (r.language === 'Song ngữ Anh - Việt' ? '#7E22CE' : '#15803D')}; border:1px solid ${r.language === 'Tiếng Anh' ? '#BAE6FD' : (r.language === 'Song ngữ Anh - Việt' ? '#E9D5FF' : '#BBF7D0')}; padding:3px 10px; border-radius:8px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td style="white-space:nowrap;">
        <span style="font-weight:800; color:var(--primary); font-size:0.82rem; white-space:nowrap;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.72rem; display:block; white-space:nowrap;">${diffDisplay}</span>
      </td>
      <td style="text-align:center; font-weight:800; white-space:nowrap;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center; white-space:nowrap;"><span class="score-badge ${badgeClass}" style="white-space:nowrap; display:inline-block; padding:4px 10px; border-radius:8px; font-weight:800;">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:700; color:#64748B; white-space:nowrap;">⏱️ ${r.duration || '00:00'}</td>
      <td style="text-align:center; white-space:nowrap;">
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="white-space:nowrap; display:inline-flex; align-items:center; gap:4px; background:#E0F2FE; color:#0284C7; border:1px solid #BAE6FD; font-size:0.78rem; padding:5px 12px; font-weight:800; border-radius:9999px; cursor:pointer;">
          🔍 Xem lại
        </button>
      </td>
    `;"""

if old_table_row in html:
    html = html.replace(old_table_row, new_table_row)
    print("Updated table rows with strict white-space:nowrap!")

# Save updated HTML
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved all 4 fixes to index.html successfully!")
