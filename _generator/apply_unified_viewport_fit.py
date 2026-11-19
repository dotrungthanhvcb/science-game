#!/usr/bin/env python3
"""
Unified Figma AI Design System & Viewport-Fit Responsive System
Fixes:
1. Unified Color Theme (Electric Cyan #06B6D4, Deep Slate #0F172A, Amber #F59E0B, White #FFFFFF)
2. Smooth Responsive Scaling on all screen sizes
3. 100vh Viewport-Fit for Home Screen and Quiz Screen (ZERO SCROLLING on laptops and desktops)
"""

import re
import os

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. UNIFIED DESIGN SYSTEM VARIABLES & BASE BODY RULES
target_root = """  :root {
    --primary: #4361EE;
    --primary-light: #EEF2FF;
    --primary-hover: #3A0CA3;
    --success: #2EC4B6;
    --success-bg: #E8F8F5;
    --danger: #E71D36;
    --danger-bg: #FDE8EA;
    --warning: #FF9F1C;
    --warning-bg: #FFF8EB;
    --text: #2B2D42;
    --text-muted: #64748B;
    --card-bg: #FFFFFF;
    --border-rad: 20px;
    --shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }

  body {
    background: linear-gradient(135deg, #3A0CA3 0%, #4361EE 50%, #4CC9F0 100%);
    min-height: 100vh;
    padding: clamp(8px, 1.5vw, 18px);
    display: flex;
    justify-content: center;
    align-items: flex-start;
    color: var(--text);
  }

  /* FULL WIDTH RESPONSIVE WRAPPER (TỐI ƯU TOÀN DIỆN CHO LAPTOP & IPAD) */
  .main-wrapper {
    width: 100%;
    max-width: 1120px;
  }"""

replacement_root = """  /* =========================================================================
     1. UNIFIED FIGMA AI DESIGN TOKENS (ELECTRIC CYAN, COSMIC SLATE, WARM AMBER)
     ========================================================================= */
  :root {
    /* Brand Primary: Electric Cyan */
    --primary: #06B6D4;
    --primary-hover: #0891B2;
    --primary-dark: #0E7490;
    --primary-shadow: #155E75;
    --primary-light: #ECFEFF;
    --primary-border: #BAE6FD;

    /* Secondary: Deep Cosmic Slate */
    --dark: #0F172A;
    --dark-surface: #1E293B;
    --dark-border: #334155;
    
    /* Text Hierarchy */
    --text: #0F172A;
    --text-main: #0F172A;
    --text-muted: #64748B;
    --text-light: #94A3B8;

    /* Gamification Accent: Warm Amber / Gold Stars */
    --warning: #F59E0B;
    --warning-bg: #FEF3C7;
    --accent-gold: #F59E0B;
    --accent-gold-dark: #D97706;
    --accent-gold-shadow: #92400E;

    /* Status: Emerald Success & Crimson Danger */
    --success: #10B981;
    --success-bg: #ECFDF5;
    --danger: #EF4444;
    --danger-bg: #FEF2F2;

    /* Surfaces & Elevation */
    --card-bg: #FFFFFF;
    --border-rad: 24px;
    --shadow: 0 16px 36px -10px rgba(15, 23, 42, 0.25);
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }

  body {
    background: #0B0F19 radial-gradient(ellipse 90% 60% at 50% -20%, #1E293B 0%, #0B0F19 100%) !important;
    min-height: 100vh;
    padding: 10px 14px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--text-main);
    overflow-x: hidden;
  }

  .main-wrapper {
    width: 100%;
    max-width: 1100px;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
  }"""

if target_root in html:
    html = html.replace(target_root, replacement_root)
    print("Replaced :root and base body successfully!")
else:
    print("Target root not found verbatim, checking regex...")
    pattern_root = r':root\s*\{[\s\S]*?max-width:\s*1120px;\s*\}'
    html = re.sub(pattern_root, replacement_root, html, count=1)
    print("Replaced :root via regex!")

# 2. ADD COMPREHENSIVE VIEWPORT-FIT AND UNIFIED RESPONSIVE RULES AT THE END OF <style>
viewport_fit_css = """
  /* =========================================================================
     2. VIEWPORT-FIT ARCHITECTURE: ZERO SCROLLING ON DESKTOPS, LAPTOPS & TABLETS
     ========================================================================= */

  /* Áp dụng cho màn hình Laptop & Desktop (Chiều cao >= 620px và Chiều rộng >= 768px) */
  @media (min-height: 620px) and (min-width: 768px) {
    body {
      height: 100vh !important;
      max-height: 100vh !important;
      overflow: hidden !important;
      padding: 10px 18px !important;
    }

    .main-wrapper {
      height: 100% !important;
      max-height: calc(100vh - 20px) !important;
      overflow: hidden !important;
      justify-content: space-between !important;
    }

    /* Header cố định chiều cao gọn gàng */
    .app-header {
      height: 52px !important;
      min-height: 52px !important;
      margin-bottom: 8px !important;
      flex-shrink: 0 !important;
      padding: 6px 20px !important;
    }

    /* Màn hình active chiếm trọn không gian còn lại mà không sinh scrollbar */
    .screen.active {
      flex: 1 1 0% !important;
      min-height: 0 !important;
      display: flex !important;
      flex-direction: column !important;
      overflow: hidden !important;
      padding: 12px 20px !important;
      border-radius: 24px !important;
    }

    /* -------------------------------------------------------------------------
       HOME SCREEN VIEWPORT-FIT: TỐI ƯU GỌN GÀNG VỪA KHÍT 1 KHUNG NHÌN
       ------------------------------------------------------------------------- */
    #home-screen.active {
      justify-content: space-between !important;
    }

    /* Khối bạn đồng hành & profile nhanh trên Home */
    .home-hero-card {
      padding: 10px 18px !important;
      margin-bottom: 8px !important;
      flex-shrink: 0 !important;
      border-radius: 18px !important;
      min-height: auto !important;
    }
    .home-mascot-avatar {
      width: 44px !important;
      height: 44px !important;
      min-width: 44px !important;
    }
    .home-mascot-name {
      font-size: 0.95rem !important;
    }
    .home-mascot-title {
      font-size: 0.72rem !important;
    }
    .home-mascot-speech {
      display: none !important; /* Ẩn câu thoại dài trên desktop để vừa khít màn hình */
    }
    .home-quick-field {
      font-size: 0.78rem !important;
    }
    .home-quick-field select, .home-quick-field input {
      padding: 4px 8px !important;
      font-size: 0.8rem !important;
      height: 32px !important;
    }

    /* Khối chính 2 cột: Cấu hình đề thi & Chủ đề */
    .home-main-grid {
      flex: 1 1 0% !important;
      min-height: 0 !important;
      margin-bottom: 8px !important;
      gap: 12px !important;
      grid-template-columns: 1fr 1.15fr !important;
      overflow: hidden !important;
    }

    .home-card {
      display: flex !important;
      flex-direction: column !important;
      min-height: 0 !important;
      border-radius: 18px !important;
      overflow: hidden !important;
    }
    .home-card-header {
      padding: 8px 14px !important;
      font-size: 0.92rem !important;
      flex-shrink: 0 !important;
    }
    .home-form-body {
      flex: 1 1 0% !important;
      min-height: 0 !important;
      overflow-y: auto !important;
      padding: 10px 14px !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
    }
    .config-row-compact {
      margin-bottom: 6px !important;
      font-size: 0.82rem !important;
    }
    .config-row-compact select {
      padding: 4px 8px !important;
      height: 32px !important;
      font-size: 0.82rem !important;
    }
    .home-pills-row {
      gap: 5px !important;
    }
    .home-pill {
      padding: 5px 10px !important;
      font-size: 0.78rem !important;
    }

    /* Lưới 6 chủ đề phòng Lab: 2 cột hoặc 3 cột nhỏ gọn */
    .topics-grid-compact {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 6px !important;
    }
    .topic-pill {
      padding: 7px 10px !important;
      font-size: 0.82rem !important;
      border-radius: 14px !important;
      gap: 8px !important;
    }

    /* Thanh hành động bắt đầu thi */
    .home-action-bar {
      padding: 6px 14px !important;
      margin-top: 0 !important;
      flex-shrink: 0 !important;
      gap: 12px !important;
    }
    .pool-status-banner {
      font-size: 0.8rem !important;
      padding: 6px 12px !important;
    }
    .btn-start {
      padding: 10px 24px !important;
      font-size: 1rem !important;
      min-width: 200px !important;
      height: 48px !important;
    }

    /* -------------------------------------------------------------------------
       QUIZ SCREEN VIEWPORT-FIT: TỐI ƯU PHÒNG THI VỪA KHÍT 1 KHUNG NHÌN
       ------------------------------------------------------------------------- */
    #quiz-screen.active {
      justify-content: space-between !important;
      padding: 12px 20px !important;
    }

    .quiz-top-bar {
      margin-bottom: 6px !important;
      flex-shrink: 0 !important;
    }
    .control-btn {
      padding: 6px 12px !important;
      font-size: 0.82rem !important;
      height: 34px !important;
    }
    .timer-pill {
      padding: 5px 14px !important;
      font-size: 0.95rem !important;
      height: 34px !important;
    }

    .progress-track {
      height: 8px !important;
      margin-bottom: 6px !important;
      flex-shrink: 0 !important;
    }
    .question-badge-row {
      margin-bottom: 6px !important;
      font-size: 0.82rem !important;
      flex-shrink: 0 !important;
    }

    /* Layout 2 cột: Trái (Minh họa) + Phải (Câu hỏi & 4 Đáp án) */
    .quiz-layout-grid {
      flex: 1 1 0% !important;
      min-height: 0 !important;
      display: grid !important;
      grid-template-columns: 190px 1fr !important;
      gap: 16px !important;
      overflow: hidden !important;
      align-items: stretch !important;
    }

    .quiz-left-panel {
      display: flex !important;
      flex-direction: column !important;
      justify-content: center !important;
      gap: 8px !important;
      overflow: hidden !important;
    }
    .mascot-container {
      padding: 6px !important;
      margin-bottom: 0 !important;
    }
    .mascot-bubble {
      font-size: 0.78rem !important;
      padding: 6px 10px !important;
      line-height: 1.3 !important;
    }
    .question-img-card {
      max-height: 130px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      background: #F8FAFC !important;
      border-radius: 16px !important;
      overflow: hidden !important;
      border: 1px solid #E2E8F0 !important;
    }
    .question-img-card img {
      max-height: 120px !important;
      max-width: 100% !important;
      object-fit: contain !important;
    }

    .quiz-right-panel {
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      min-height: 0 !important;
      overflow: hidden !important;
    }

    .question-title {
      font-size: clamp(1.05rem, 1.4vw, 1.25rem) !important;
      line-height: 1.35 !important;
      margin-bottom: 8px !important;
      color: #0F172A !important;
      flex-shrink: 0 !important;
      max-height: 80px !important;
      overflow-y: auto !important;
    }

    /* 4 Đáp Án Dạng 2x2 Grid Luôn Nằm Vừa Khít */
    .choices-container {
      display: grid !important;
      grid-template-columns: 1fr 1fr !important;
      gap: 8px !important;
      margin-bottom: 6px !important;
      flex-shrink: 0 !important;
    }
    .choice-option {
      min-height: 48px !important;
      height: auto !important;
      padding: 8px 12px !important;
      gap: 10px !important;
      border-radius: 16px !important;
    }
    .choice-letter {
      width: 30px !important;
      height: 30px !important;
      min-width: 30px !important;
      font-size: 0.95rem !important;
    }
    .choice-text-inner {
      font-size: 0.86rem !important;
      line-height: 1.3 !important;
    }

    .explanation-card {
      padding: 6px 12px !important;
      font-size: 0.8rem !important;
      margin-top: 4px !important;
      border-radius: 12px !important;
      flex-shrink: 0 !important;
    }

    .btn-next-step {
      padding: 10px 24px !important;
      font-size: 0.95rem !important;
      height: 44px !important;
      margin-top: 4px !important;
      flex-shrink: 0 !important;
    }
  }

  /* ---------------------------------------------------------------------------
     3. RESPONSIVE MOBILE & TABLET (MÀN HÌNH NHỎ HOẶC XOAY DỌC)
     --------------------------------------------------------------------------- */
  @media (max-width: 767px) {
    body {
      padding: 8px !important;
      min-height: 100vh !important;
      height: auto !important;
      overflow-y: auto !important;
    }
    .main-wrapper {
      max-width: 100% !important;
    }
    .app-header {
      padding: 8px 14px !important;
      border-radius: 20px !important;
      flex-direction: column !important;
      gap: 8px !important;
    }
    .template-nav-links {
      overflow-x: auto !important;
      width: 100% !important;
      justify-content: flex-start !important;
      padding-bottom: 4px !important;
    }
    .home-main-grid {
      grid-template-columns: 1fr !important;
    }
    .quiz-layout-grid {
      grid-template-columns: 1fr !important;
    }
    .choices-container {
      grid-template-columns: 1fr !important;
    }
  }
"""

if "VIEWPORT-FIT ARCHITECTURE" not in html:
    html = html.replace("</style>", f"{viewport_fit_css}\n</style>")
    print("Added Viewport-Fit architecture to CSS!")

# Write updated HTML
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved index.html successfully!")
