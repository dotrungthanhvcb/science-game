#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. HEAD CDN INJECTION
# Ensure Tailwind, Nunito, Lucide, Canvas Confetti are in <head>
head_pattern = r"(<head>[\s\S]*?)(<script src=\"questions_500\.js\")"

new_head_libs = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="referrer" content="no-referrer">

  <!-- 1. TAILWIND CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- 2. GOOGLE FONT NUNITO (HỖ TRỢ TIẾNG VIỆT CHUẨN) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- 3. LUCIDE ICONS CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- 4. CANVAS CONFETTI CDN -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  """

content = re.sub(head_pattern, new_head_libs + r"\2", content, count=1)
print("1. Injected CDNs into <head>")

# 2. ADD COMPREHENSIVE DUOLINGO 3D TACTILE BUTTONS & NUNITO ENFORCEMENT & ANIMATIONS INTO <style>
tactile_css = """
  /* =========================================================================
     TACTILE 3D BUTTONS & FONT OVERRIDES (DUOLINGO STYLE & NUNITO ENFORCEMENT)
     ========================================================================= */
  *, body, button, input, select, textarea, div, p, span, h1, h2, h3, h4, h5, h6, a, label {
    font-family: 'Nunito', sans-serif !important;
  }

  /* Duolingo Tactile 3D Buttons Base */
  .btn-3d-base, 
  .template-btn-pill, 
  .template-btn-dark, 
  .btn-start, 
  .btn-next-step, 
  .btn-highlight, 
  .btn-secondary, 
  .btn-primary-action, 
  .btn-source-action, 
  .btn-check-sa, 
  .control-btn, 
  .choice-option, 
  .source-toggle-chip {
    transition: transform 0.12s cubic-bezier(0.34, 1.56, 0.64, 1), 
                box-shadow 0.12s ease, 
                border-bottom-width 0.12s ease, 
                background-color 0.15s ease,
                border-color 0.15s ease !important;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    outline: none;
  }

  /* 1. Nút Read More / Bắt đầu ở Hero (Peach Cream) */
  .template-btn-pill {
    background: #FCECE4 !important;
    color: #1C2038 !important;
    border: 2px solid #F5D6C6 !important;
    border-bottom: 5px solid #E2A68C !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    min-height: 48px !important;
    height: auto !important;
    padding: 12px 28px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
  }
  .template-btn-pill:hover {
    background: #FFF4EE !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
  }
  .template-btn-pill:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 2. Nút Dark Slate (Template Action) */
  .template-btn-dark, .btn-primary-action {
    background: #1C2038 !important;
    color: #FFFFFF !important;
    border: 2px solid #141729 !important;
    border-bottom: 5px solid #0D0F1B !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    min-height: 48px !important;
    height: auto !important;
    padding: 12px 28px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
  }
  .template-btn-dark:hover, .btn-primary-action:hover {
    background: #2D3357 !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
  }
  .template-btn-dark:active, .btn-primary-action:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 3. Nút BẮT ĐẦU ÔN LUYỆN (Green 3D Button) */
  .btn-start {
    background: #10B981 !important;
    color: #FFFFFF !important;
    border: 2px solid #059669 !important;
    border-bottom: 5px solid #047857 !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 1.1rem !important;
    min-height: 56px !important;
    height: auto !important;
    padding: 14px 32px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
  }
  .btn-start:hover {
    background: #059669 !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
    box-shadow: 0 10px 24px rgba(16, 185, 129, 0.35) !important;
  }
  .btn-start:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 4. Nút CÂU TIẾP THEO (Dark 3D Button) */
  .btn-next-step {
    background: #1C2038 !important;
    color: #FFFFFF !important;
    border: 2px solid #141729 !important;
    border-bottom: 5px solid #0D0F1B !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
    min-height: 52px !important;
    height: auto !important;
    padding: 14px 28px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    margin-top: 14px !important;
  }
  .btn-next-step:hover {
    background: #2D3357 !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
  }
  .btn-next-step:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 5. Nút NỔI BẬT / XEM LẠI BÀI (Blue 3D Button) */
  .btn-highlight {
    background: #3B82F6 !important;
    color: #FFFFFF !important;
    border: 2px solid #2563EB !important;
    border-bottom: 5px solid #1D4ED8 !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    min-height: 52px !important;
    height: auto !important;
    padding: 14px 28px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
  }
  .btn-highlight:hover {
    background: #2563EB !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
    box-shadow: 0 10px 24px rgba(59, 130, 246, 0.35) !important;
  }
  .btn-highlight:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 6. Nút SECONDARY (Peach / Neutral 3D Button) */
  .btn-secondary {
    background: #FCECE4 !important;
    color: #1C2038 !important;
    border: 2px solid #F5D6C6 !important;
    border-bottom: 5px solid #E2A68C !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    min-height: 48px !important;
    height: auto !important;
    padding: 12px 22px !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
  }
  .btn-secondary:hover {
    background: #FFF4EE !important;
    transform: translateY(-2px) !important;
    border-bottom-width: 6px !important;
  }
  .btn-secondary:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }

  /* 7. NÚT CHỌN ĐÁP ÁN (CHOICE OPTIONS A/B/C/D) - DUOLINGO 3D TACTILE */
  .choice-option {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    min-height: 64px !important;
    height: auto !important;
    padding: 14px 20px !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.45 !important;
    border-radius: 18px !important;
    background: #FFFFFF !important;
    border: 2px solid #F0D5C5 !important;
    border-bottom: 5px solid #D8B7A4 !important;
    color: #1C2038 !important;
    font-weight: 700 !important;
    text-align: left !important;
    position: relative !important;
    width: 100% !important;
  }
  .choice-option:hover:not(:disabled) {
    border-color: #E76F51 !important;
    border-bottom: 6px solid #C4573B !important;
    background: #FFFDFB !important;
    transform: translateY(-2px) !important;
  }
  .choice-option:active:not(:disabled) {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }
  .choice-option.selected {
    border-color: #1C2038 !important;
    border-bottom: 5px solid #0F1222 !important;
    background: #FCECE4 !important;
    color: #1C2038 !important;
    transform: scale(1.02) !important;
    box-shadow: 0 8px 24px rgba(28, 32, 56, 0.14) !important;
  }
  .choice-letter {
    width: 38px !important;
    height: 38px !important;
    min-width: 38px !important;
    border-radius: 12px !important;
    background: #FCECE4 !important;
    color: #1C2038 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-weight: 900 !important;
    font-size: 1.05rem !important;
    transition: all 0.15s ease !important;
    flex-shrink: 0 !important;
  }
  .choice-option.selected .choice-letter {
    background: #1C2038 !important;
    color: #FFFFFF !important;
  }
  .choice-text-inner {
    flex: 1 !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.45 !important;
  }
  .choice-check-icon {
    width: 28px !important;
    height: 28px !important;
    min-width: 28px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #10B981 !important;
    opacity: 0 !important;
    transform: scale(0.4) !important;
    transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    flex-shrink: 0 !important;
  }
  .choice-option.selected .choice-check-icon {
    opacity: 1 !important;
    transform: scale(1) !important;
  }

  /* 8. NGUỒN ĐỀ THI (SOURCE TOGGLE CHIP) */
  .source-toggle-chip {
    background: #FFFFFF !important;
    border: 2px solid #EFE4DC !important;
    border-bottom: 5px solid #D5C2B6 !important;
    border-radius: 18px !important;
    padding: 14px 16px !important;
    min-height: 84px !important;
    height: auto !important;
    white-space: normal !important;
    word-break: break-word !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    gap: 8px !important;
  }
  .source-toggle-chip:hover {
    border-color: #E76F51 !important;
    border-bottom: 6px solid #C4573B !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(231, 111, 81, 0.12) !important;
  }
  .source-toggle-chip:active {
    transform: translateY(4px) !important;
    border-bottom-width: 1px !important;
  }
  .source-toggle-chip.selected {
    border-color: #1C2038 !important;
    border-bottom: 5px solid #0F1222 !important;
    background: #FFFDF9 !important;
    box-shadow: 0 8px 24px rgba(28, 32, 56, 0.14) !important;
  }

  /* 9. NÚT ĐIỀU KHIỂN TRONG BÀI THI (CONTROL BTN) */
  .control-btn {
    background: #FFFFFF !important;
    border: 2px solid #E2E8F0 !important;
    border-bottom: 4px solid #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 8px 14px !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
  }
  .control-btn:hover {
    transform: translateY(-1px) !important;
    border-bottom-width: 5px !important;
  }
  .control-btn:active {
    transform: translateY(3px) !important;
    border-bottom-width: 1px !important;
  }

  /* 10. ANIMATIONS (TRANSITIONS & FLOATING) */
  @keyframes questionFadeSlide {
    0% {
      opacity: 0;
      transform: translateY(18px) scale(0.985);
    }
    100% {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }
  .animate-question {
    animation: questionFadeSlide 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }

  @keyframes floatSlow {
    0%, 100% {
      transform: translateY(0px) rotate(0deg);
    }
    50% {
      transform: translateY(-12px) rotate(3deg);
    }
  }
  @keyframes floatAlt {
    0%, 100% {
      transform: translateY(0px) rotate(0deg);
    }
    50% {
      transform: translateY(10px) rotate(-3deg);
    }
  }
  .template-deco:nth-child(odd) {
    animation: floatSlow 6s ease-in-out infinite;
  }
  .template-deco:nth-child(even) {
    animation: floatAlt 7.5s ease-in-out infinite;
  }
"""

content = content.replace("</style>", tactile_css + "\n</style>", 1)
print("2. Added tactile 3D styles and animations before </style>")

# 3. UPDATE HEADER HTML WITH LUCIDE ICONS
old_header = """  <header class="app-header">
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

new_header = """  <header class="app-header">
    <div class="template-logo" onclick="showScreen('welcome-screen')" title="Về Màn hình Chào mừng">
      <div style="width:38px; height:38px; border-radius:50%; background:#FCECE4; display:flex; align-items:center; justify-content:center; color:#E76F51; flex-shrink:0;">
        <i data-lucide="microscope" style="width:22px; height:22px; stroke-width:2.5;"></i>
      </div>
      <span>KHOA HỌC NHÍ</span>
    </div>

    <nav class="template-nav-links">
      <a href="javascript:void(0)" onclick="showScreen('home-screen')" class="template-nav-item active" style="display:inline-flex; align-items:center; gap:6px;">
        <i data-lucide="home" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span>Trang Chủ</span>
      </a>
      <a href="javascript:void(0)" onclick="openLeaderboardModal()" class="template-nav-item" style="display:inline-flex; align-items:center; gap:6px;">
        <i data-lucide="award" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span>Bảng Vàng</span>
      </a>
      <a href="javascript:void(0)" onclick="openHistoryScreen()" class="template-nav-item" style="display:inline-flex; align-items:center; gap:6px;">
        <i data-lucide="bar-chart-2" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span>Lịch Sử</span>
      </a>
      <a href="javascript:void(0)" onclick="openUserManagementModal()" class="template-nav-item" id="nav-item-user-mgmt" style="display:inline-flex; align-items:center; gap:6px;">
        <i data-lucide="users" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span>Quản Lý</span>
      </a>
      <a href="javascript:void(0)" onclick="shareGameLink()" class="template-nav-item" style="display:inline-flex; align-items:center; gap:6px;">
        <i data-lucide="share-2" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span>Mời Bạn</span>
      </a>
    </nav>

    <div class="template-header-circles">
      <!-- NÚT BẬT TẮT NHẠC NỀN -->
      <button class="header-circle-btn" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung">
        <span id="music-icon"><i data-lucide="volume-2" style="width:18px; height:18px; stroke-width:2.5;"></i></span>
      </button>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->
      <div id="header-auth-container">
        <button class="header-circle-btn" onclick="openAuthModal()" title="Đăng nhập tài khoản">
          <i data-lucide="user" style="width:18px; height:18px; stroke-width:2.5;"></i>
        </button>
      </div>
    </div>
  </header>"""

if old_header in content:
    content = content.replace(old_header, new_header, 1)
    print("3. Updated header HTML with Lucide icons")
else:
    print("Warning: old_header not found exactly!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved stage 1.")
