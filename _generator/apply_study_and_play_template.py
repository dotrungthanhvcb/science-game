#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. ADD MONTSERRAT GOOGLE FONT (from Fonts.txt in the template)
font_link = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700;1,900&display=swap" rel="stylesheet">"""

if "family=Montserrat" not in content:
    content = content.replace("<head>", "<head>\n" + font_link, 1)
    print("1. Added Montserrat font.")

# 2. OVERHAUL CSS TO THE EXACT TEMPLATE THEME (STUDY & PLAY - DARK NAVY OUTER, PEACH CREAM CANVAS)
template_css = """
  /* =======================================================================
     STUDY & PLAY TEMPLATE THEME (BASED ON 7604738.JPG & MONTSERRAT FONT)
     ======================================================================= */
  * { 
    box-sizing: border-box; 
    margin: 0; 
    padding: 0; 
    font-family: 'Montserrat', system-ui, -apple-system, sans-serif !important; 
  }

  :root {
    --primary: #1C2038;
    --primary-light: #F7EAE1;
    --primary-hover: #2C3258;
    --bg-dark: #1F2238;
    --canvas-bg: #FFFDF9;
    --peach-border: #F5D6C6;
    --peach-pill: #F0D5C5;
    --peach-pill-hover: #E7C5B2;
    --text-dark: #1C2038;
    --text-muted: #5B6376;
    --card-bg: #FFFFFF;
    --radius-canvas: 32px;
  }

  body {
    background-color: var(--bg-dark) !important;
    background-image: 
      radial-gradient(circle at 10% 20%, rgba(245, 214, 198, 0.05) 0%, transparent 20%),
      radial-gradient(circle at 90% 80%, rgba(245, 214, 198, 0.05) 0%, transparent 20%);
    min-height: 100vh;
    padding: clamp(12px, 2.5vw, 32px);
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--text-dark);
  }

  /* KHUNG CANVAS CHÍNH (CANVAS BOARD DẠNG TABLET BO TRÒN) */
  .main-wrapper {
    width: 100%;
    max-width: 1220px;
    background: var(--canvas-bg);
    border-radius: var(--radius-canvas);
    border: 4px solid var(--peach-border);
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.4), 0 8px 24px rgba(0,0,0,0.15);
    padding: clamp(18px, 2.8vw, 36px);
    position: relative;
    overflow: hidden;
  }

  /* NỀN LƯỢN SÓNG PEACH MỀM MẠI CỦA TEMPLATE */
  .main-wrapper::before {
    content: '';
    position: absolute;
    top: -60px;
    left: -80px;
    width: 320px;
    height: 320px;
    background: #FCECE4;
    border-radius: 46% 54% 60% 40% / 50% 40% 60% 50%;
    z-index: 0;
    pointer-events: none;
    opacity: 0.85;
  }
  .main-wrapper::after {
    content: '';
    position: absolute;
    top: -50px;
    right: -80px;
    width: 340px;
    height: 340px;
    background: #FCECE4;
    border-radius: 54% 46% 40% 60% / 40% 60% 40% 60%;
    z-index: 0;
    pointer-events: none;
    opacity: 0.85;
  }

  /* THANH HEADER CHUẨN TEMPLATE (YOUR LOGO + NAV LINKS + CIRCULAR BUTTONS) */
  .app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 0 18px 0;
    border-bottom: 2px solid #F5E5DC;
    margin-bottom: 20px;
    position: relative;
    z-index: 10;
    gap: 16px;
    flex-wrap: wrap;
    background: transparent !important;
    box-shadow: none !important;
    border-radius: 0 !important;
  }

  .template-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 900;
    font-size: 1.35rem;
    color: #1C2038;
    letter-spacing: -0.5px;
    text-transform: uppercase;
  }

  .template-nav-links {
    display: flex;
    align-items: center;
    gap: clamp(12px, 2vw, 28px);
    list-style: none;
    flex-wrap: wrap;
  }
  .template-nav-item {
    font-size: 0.95rem;
    font-weight: 700;
    color: #1C2038;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 6px 10px;
    border-radius: 8px;
  }
  .template-nav-item:hover {
    color: #E76F51;
    background: #FDF1EA;
  }
  .template-nav-item.active {
    color: #1C2038;
    font-weight: 900;
  }

  .template-header-circles {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .header-circle-btn {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #1C2038;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    cursor: pointer;
    transition: transform 0.2s, background 0.2s;
    border: none;
    box-shadow: 0 4px 10px rgba(28, 32, 56, 0.2);
  }
  .header-circle-btn:hover {
    transform: scale(1.1);
    background: #E76F51;
  }

  /* KHUNG NỘI DUNG CHÍNH (RELATIVE TRÊN CANVAS) */
  .screen, .welcome-card, .quiz-card, .history-container {
    position: relative;
    z-index: 5;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
  }

  /* TEMPLATE HERO BANNER (STUDY & PLAY) */
  .template-hero-box {
    text-align: center;
    max-width: 780px;
    margin: 10px auto 20px auto;
    position: relative;
    z-index: 5;
  }
  .template-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FCECE4;
    color: #1C2038;
    border: 1.5px solid #F5D6C6;
    padding: 6px 18px;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 800;
    margin-bottom: 18px;
    letter-spacing: 0.5px;
  }
  .template-hero-title {
    font-size: clamp(3.2rem, 7.5vw, 5.2rem);
    font-weight: 900;
    color: #1C2038;
    line-height: 0.95;
    text-transform: uppercase;
    letter-spacing: -2px;
    margin-bottom: 18px;
  }
  .template-hero-title span {
    display: block;
  }
  .template-hero-desc {
    font-size: clamp(0.95rem, 1.8vw, 1.12rem);
    color: #525866;
    font-weight: 500;
    line-height: 1.65;
    max-width: 620px;
    margin: 0 auto 28px auto;
  }

  /* NÚT BẤM "READ MORE >" CỦA TEMPLATE */
  .template-btn-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: var(--peach-pill);
    color: #1C2038;
    border: none;
    border-radius: 9999px;
    font-size: 1.12rem;
    font-weight: 800;
    padding: 16px 42px;
    cursor: pointer;
    transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
    box-shadow: 0 4px 14px rgba(240, 213, 197, 0.7);
    letter-spacing: 0.2px;
  }
  .template-btn-pill:hover {
    background: var(--peach-pill-hover);
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 22px rgba(240, 213, 197, 0.9);
  }
  .template-btn-pill:active {
    transform: translateY(1px);
  }

  .template-btn-dark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: #1C2038;
    color: white;
    border: none;
    border-radius: 9999px;
    font-size: 1.05rem;
    font-weight: 800;
    padding: 14px 34px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 6px 18px rgba(28, 32, 56, 0.25);
  }
  .template-btn-dark:hover {
    background: #2C3258;
    transform: translateY(-2px);
  }

  /* GIAO DIỆN HOME & QUIZ THEO PHONG CÁCH TEMPLATE */
  .home-hero-card {
    background: #FFF8F4 !important;
    border: 2px solid #F5D6C6 !important;
    border-radius: 24px !important;
    box-shadow: 0 6px 18px rgba(245, 214, 198, 0.25) !important;
  }
  .home-card {
    background: #FFFFFF !important;
    border: 2px solid #F5D6C6 !important;
    border-radius: 20px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03) !important;
  }
  .home-card-header {
    background: #FFF2EB !important;
    font-weight: 800 !important;
    color: #1C2038 !important;
    border-bottom: 2px solid #F5D6C6 !important;
    font-size: 0.95rem !important;
  }
  .home-pill {
    border-radius: 9999px !important;
    font-weight: 700 !important;
    border: 1.5px solid #F5D6C6 !important;
    background: #FFFDF9 !important;
    color: #1C2038 !important;
  }
  .home-pill.active {
    background: #1C2038 !important;
    color: white !important;
    border-color: #1C2038 !important;
  }
  .topic-pill {
    border-radius: 14px !important;
    font-weight: 700 !important;
    border: 1.5px solid #F5D6C6 !important;
    background: #FFFDF9 !important;
    color: #1C2038 !important;
  }
  .topic-pill.selected {
    background: #1C2038 !important;
    color: white !important;
    border-color: #1C2038 !important;
  }

  /* NÚT CHỌN ĐÁP ÁN TRONG BÀI THI */
  .choice-option {
    border-radius: 18px !important;
    border: 2px solid #F5D6C6 !important;
    background: #FFFFFF !important;
    color: #1C2038 !important;
    font-weight: 700 !important;
  }
  .choice-option:hover {
    border-color: #E76F51 !important;
    background: #FFF8F4 !important;
  }
  .choice-option.selected {
    border-color: #1C2038 !important;
    background: #FCECE4 !important;
    color: #1C2038 !important;
  }
  .choice-letter {
    background: #FCECE4 !important;
    color: #1C2038 !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
  }
  .choice-option.selected .choice-letter {
    background: #1C2038 !important;
    color: white !important;
  }

  /* CÁC ĐỒ CHƠI HÌNH VẼ DECOR THEO TEMPLATE (TUYỆT ĐẸP TRÊN DESKTOP) */
  .template-deco {
    position: absolute;
    z-index: 1;
    pointer-events: none;
    transition: transform 0.3s ease;
  }
  @media (max-width: 992px) {
    .template-deco {
      display: none;
    }
  }
"""

if "STUDY & PLAY TEMPLATE THEME" not in content:
    content = content.replace("</style>", template_css + "\n</style>", 1)
    print("2. Injected Study & Play template CSS.")

# 3. REWRITE HEADER IN HTML ACCORDING TO TEMPLATE NAVBAR
old_header_pattern = re.compile(r'<header class="app-header">.*?</header>', re.DOTALL)

new_header_html = """<header class="app-header">
    <div class="template-logo" onclick="showScreen('welcome-screen')" title="Về Màn hình Chào mừng">
      <span>🔬</span>
      <span>KHOA HỌC NHÍ</span>
    </div>

    <nav class="template-nav-links">
      <a href="javascript:void(0)" onclick="showScreen('home-screen')" class="template-nav-item active">Trang Chủ</a>
      <a href="javascript:void(0)" onclick="openLeaderboardModal()" class="template-nav-item">Bảng Vàng 🏆</a>
      <a href="javascript:void(0)" onclick="openHistoryScreen()" class="template-nav-item">Lịch Sử 📊</a>
      <a href="javascript:void(0)" onclick="openUserManagementModal()" class="template-nav-item" id="nav-item-user-mgmt">Quản Lý 👥</a>
      <a href="javascript:void(0)" onclick="shareGameLink()" class="template-nav-item">Mời Bạn 📤</a>
    </nav>

    <div class="template-header-circles">
      <!-- NÚT BẬT TẮT NHẠC NỀN -->
      <button class="header-circle-btn" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung">
        <span id="music-icon">🎵</span>
      </button>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->
      <div id="header-auth-container">
        <button class="header-circle-btn" onclick="openAuthModal()" title="Đăng nhập tài khoản">
          <span>👤</span>
        </button>
      </div>
    </div>
  </header>"""

if old_header_pattern.search(content):
    content = old_header_pattern.sub(new_header_html, content)
    print("3. Replaced Header with Template Navbar.")

# 4. REWRITE WELCOME SCREEN ACCORDING TO TEMPLATE HERO SECTION
old_welcome_pattern = re.compile(r'<div class="screen active" id="welcome-screen">.*?</div>\s*</div>\s*</div>\s*(?=<!-- ===|id="home-screen")', re.DOTALL)
if not old_welcome_pattern.search(content):
    old_welcome_pattern = re.compile(r'<div class="screen" id="welcome-screen">.*?</div>\s*</div>\s*</div>\s*(?=<!-- ===|id="home-screen")', re.DOTALL)

new_welcome_html = """<div class="screen active" id="welcome-screen">
    <div class="template-hero-box">
      <!-- DECORATIONS FROM TEMPLATE -->
      <!-- Kẹo mút xoắn hồng (Trái trên) -->
      <div class="template-deco" style="top: -10px; left: -100px;">
        <svg width="100" height="100" viewBox="0 0 100 100">
          <line x1="30" y1="70" x2="10" y2="90" stroke="#3A2E39" stroke-width="5" stroke-linecap="round"/>
          <circle cx="55" cy="45" r="34" fill="#FF8BA7" stroke="#E25C80" stroke-width="3"/>
          <path d="M55 11 A34 34 0 0 1 89 45 L55 45 Z" fill="#FFFFFF" opacity="0.9"/>
          <path d="M55 79 A34 34 0 0 1 21 45 L55 45 Z" fill="#FFFFFF" opacity="0.9"/>
          <polygon points="12,18 16,8 20,18 30,18 22,24 25,34 16,28 7,34 10,24 2,18" fill="#F87171"/>
        </svg>
      </div>

      <!-- Ô tô đồ chơi + Bút sáp màu (Trái dưới) -->
      <div class="template-deco" style="bottom: 10px; left: -110px;">
        <svg width="110" height="90" viewBox="0 0 110 90">
          <!-- Ô tô -->
          <rect x="20" y="30" width="70" height="28" rx="8" fill="#D97706"/>
          <path d="M35 30 L45 12 L75 12 L85 30 Z" fill="#B45309"/>
          <rect x="48" y="16" width="24" height="12" rx="3" fill="#60A5FA"/>
          <circle cx="36" cy="58" r="10" fill="#1E293B"/>
          <circle cx="36" cy="58" r="4" fill="#FBBF24"/>
          <circle cx="76" cy="58" r="10" fill="#1E293B"/>
          <circle cx="76" cy="58" r="4" fill="#FBBF24"/>
        </svg>
      </div>

      <!-- Tên lửa không gian (Phải trên) -->
      <div class="template-deco" style="top: 0px; right: -100px;">
        <svg width="105" height="105" viewBox="0 0 100 100">
          <path d="M65 15 C45 35 35 60 35 60 L60 60 C60 35 85 45 65 15 Z" fill="#06B6D4"/>
          <polygon points="65,15 70,8 75,18" fill="#F43F5E"/>
          <circle cx="52" cy="40" r="7" fill="#1E293B" stroke="#F1F5F9" stroke-width="2"/>
          <polygon points="35,60 25,75 40,70" fill="#8B5CF6"/>
          <polygon points="60,60 70,75 55,70" fill="#8B5CF6"/>
          <polygon points="42,65 48,82 54,65" fill="#F59E0B"/>
        </svg>
      </div>

      <!-- Cánh diều sắc màu + Cầu vồng (Phải dưới) -->
      <div class="template-deco" style="bottom: 0px; right: -110px;">
        <svg width="110" height="100" viewBox="0 0 110 100">
          <!-- Cầu vồng -->
          <path d="M45 80 A30 30 0 0 1 95 80" stroke="#8B5CF6" stroke-width="6" fill="none"/>
          <path d="M50 80 A25 25 0 0 1 90 80" stroke="#FBBF24" stroke-width="5" fill="none"/>
          <path d="M55 80 A20 20 0 0 1 85 80" stroke="#EF4444" stroke-width="5" fill="none"/>
          <!-- Cánh diều -->
          <polygon points="30,10 46,26 30,48 14,26" fill="#F59E0B"/>
          <polygon points="30,10 46,26 30,26" fill="#06B6D4"/>
          <polygon points="14,26 30,26 30,48" fill="#EC4899"/>
        </svg>
      </div>

      <!-- NỘI DUNG CHÍNH CHUẨN TEMPLATE -->
      <div class="template-hero-badge">🌟 ĐẤU TRƯỜNG KHOA HỌC TIỂU HỌC 2026</div>

      <h1 class="template-hero-title">
        <span>STUDY</span>
        <span>&amp; PLAY</span>
      </h1>

      <p class="template-hero-desc">
        Khám phá thế giới tự nhiên kỳ thú, rèn luyện tư duy logic và phản xạ cùng ngân hàng 500+ câu hỏi chuẩn SGK Việt Nam, Trạng Nguyên &amp; Kangaroo Khoa Học!
      </p>

      <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap; margin-bottom: 28px;">
        <button class="template-btn-pill" onclick="showScreen('home-screen')">
          Read More &gt;
        </button>
        <button class="template-btn-dark" onclick="openHistoryScreen()">
          📊 Xem Lịch Sử
        </button>
      </div>

      <!-- BẠN ĐỒNG HÀNH NGAY TRÊN HERO -->
      <div onclick="openMascotPickerModal()" style="display:inline-flex; align-items:center; gap:10px; background:white; border:2px solid #F5D6C6; padding:8px 18px; border-radius:9999px; cursor:pointer; box-shadow:0 4px 14px rgba(245, 214, 198, 0.4); transition:transform 0.2s;" title="Bấm để chọn bạn đồng hành khoa học!">
        <div id="welcome-mascot-svg-wrap" style="width:40px; height:40px;"></div>
        <div style="text-align:left;">
          <div style="font-size:0.72rem; color:#64748B; font-weight:700;">BẠN ĐỒNG HÀNH</div>
          <div style="font-size:0.9rem; font-weight:900; color:#1C2038;" id="welcome-mascot-name">Giáo Sư Cú Vọ ▾</div>
        </div>
      </div>
    </div>
  </div>"""

if old_welcome_pattern.search(content):
    content = old_welcome_pattern.sub(new_welcome_html, content)
    print("4. Replaced Welcome Screen with Template Hero.")
else:
    print("WARNING: Welcome screen pattern not matched!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Template restyling complete!")
