#!/usr/bin/env python3
"""
Full Transition of index.html to the Figma AI template preview:
https://science-game-sigma.vercel.app/preview_figma_ai.html
- Frame 1: Topics · Science lab (Hero banner, filter pills, 6 lab cards, exam config, floating lab 🧪)
- Frame 2: Quiz · Space explorer (Rocket progress bar, timer pill, cosmic question card, tactile 3D option cards A/B/C/D, live mascot reaction, explanation drawer)
- Frame 3: Leaderboard · Weekly stars (Shimmering 3D podium 🥇 Gold with crown 👑, 🥈 Silver, 🥉 Bronze, ranked list, sticky user card, and grand multi-burst fireworks animation)
- Result screen with celebration fireworks confetti and dancing mascot
- Preserves all 1,000 questions, student auth, admin privileges, sheets sync, and history.
"""

import re
import sys
import subprocess

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# =========================================================================
# 1. UPGRADE HEAD & CSS
# =========================================================================

# Ensure Baloo 2 + Be Vietnam Pro Google Fonts
fonts_link = """<!-- GOOGLE FONTS: BALOO 2 & BE VIETNAM PRO -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Be+Vietnam+Pro:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">"""

if "Baloo+2" not in html:
    html = html.replace("</head>", f"  {fonts_link}\n</head>")

# Ensure canvas-confetti, lucide, tailwind
scripts_to_ensure = """
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
"""

# Additional Figma AI Design System CSS
figma_ai_css = """
  /* =========================================================================
     FIGMA AI DESIGN SYSTEM (PREVIEW_FIGMA_AI TEMPLATE MATCH)
     ========================================================================= */
  * {
    font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-tap-highlight-color: transparent;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }

  .font-baloo, h1, h2, h3, h4,
  .template-hero-title,
  .question-title,
  .btn-start,
  .btn-3d,
  .timer-pill,
  .result-headline,
  .badge-source,
  .template-logo span,
  .btn-next-step,
  .podium-title,
  .star-count,
  .hero-tag {
    font-family: 'Baloo 2', 'Be Vietnam Pro', cursive, sans-serif !important;
    letter-spacing: -0.015em;
  }

  /* TACTILE 3D BUTTONS */
  .btn-3d {
    position: relative;
    transition: all 0.12s ease;
    user-select: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .btn-3d:active {
    transform: translateY(3px);
  }

  .btn-3d-cyan {
    background: linear-gradient(180deg, #06B6D4 0%, #0891B2 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #0E7490 !important;
    border-bottom: 5px solid #155E75 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 20px -4px rgba(6, 182, 212, 0.4) !important;
  }
  .btn-3d-cyan:hover {
    filter: brightness(1.06);
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .btn-3d-cyan:active {
    border-bottom-width: 1px !important;
    margin-top: 4px;
    transform: translateY(3px);
  }

  .btn-3d-amber {
    background: linear-gradient(180deg, #F59E0B 0%, #D97706 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #B45309 !important;
    border-bottom: 5px solid #92400E !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 20px -4px rgba(245, 158, 11, 0.4) !important;
  }
  .btn-3d-amber:hover {
    filter: brightness(1.06);
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .btn-3d-amber:active {
    border-bottom-width: 1px !important;
    margin-top: 4px;
    transform: translateY(3px);
  }

  .btn-3d-purple {
    background: linear-gradient(180deg, #8B5CF6 0%, #7C3AED 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #6D28D9 !important;
    border-bottom: 5px solid #5B21B6 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
  }
  .btn-3d-purple:hover {
    filter: brightness(1.06);
  }
  .btn-3d-purple:active {
    border-bottom-width: 1px !important;
    margin-top: 4px;
    transform: translateY(3px);
  }

  .btn-3d-emerald {
    background: linear-gradient(180deg, #10B981 0%, #059669 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #047857 !important;
    border-bottom: 5px solid #065F46 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
  }
  .btn-3d-emerald:hover {
    filter: brightness(1.06);
  }
  .btn-3d-emerald:active {
    border-bottom-width: 1px !important;
    margin-top: 4px;
    transform: translateY(3px);
  }

  /* OPTION CARDS (3D TACTILE SELECTION) */
  .option-card-figma, .choice-option {
    background: #FFFFFF !important;
    border: 2px solid #E2E8F0 !important;
    border-bottom: 5px solid #CBD5E1 !important;
    border-radius: 20px !important;
    transition: all 0.12s ease !important;
    cursor: pointer !important;
    user-select: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    padding: 12px 18px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    text-align: left !important;
  }
  .option-card-figma:hover, .choice-option:hover {
    border-color: #38BDF8 !important;
    background: #F0F9FF !important;
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .option-card-figma:active, .choice-option:active {
    transform: translateY(3px);
    border-bottom-width: 2px !important;
  }
  .option-card-figma.selected, .choice-option.selected {
    border-color: #06B6D4 !important;
    background: #ECFEFF !important;
    border-bottom: 5px solid #0891B2 !important;
    color: #0E7490 !important;
  }
  .option-card-figma.correct, .choice-option.correct {
    border-color: #10B981 !important;
    background: #ECFDF5 !important;
    border-bottom: 5px solid #047857 !important;
    color: #065F46 !important;
  }
  .option-card-figma.wrong, .choice-option.wrong {
    border-color: #EF4444 !important;
    background: #FEF2F2 !important;
    border-bottom: 5px solid #B91C1C !important;
    color: #991B1B !important;
  }

  /* TOPIC LAB CARD */
  .topic-lab-card {
    background: #FFFFFF;
    border: 2px solid #F1F5F9;
    border-bottom: 4px solid #E2E8F0;
    border-radius: 24px;
    transition: all 0.15s ease;
    cursor: pointer;
  }
  .topic-lab-card:hover {
    transform: translateY(-3px);
    border-color: #38BDF8;
    box-shadow: 0 12px 24px -6px rgba(14, 165, 233, 0.15);
  }
  .topic-lab-card:active {
    transform: translateY(2px);
    border-bottom-width: 2px;
  }

  /* PODIUM ANIMATION (LEADERBOARD WEEKLY STARS) */
  .podium-1st {
    background: linear-gradient(180deg, #FDE047 0%, #F59E0B 100%) !important;
    border-top: 3px solid #FEF08A !important;
    box-shadow: inset 0 2px 4px rgba(255,255,255,0.5), 0 8px 20px rgba(245, 158, 11, 0.35) !important;
    border-radius: 16px 16px 0 0 !important;
  }
  .podium-2nd {
    background: linear-gradient(180deg, #E2E8F0 0%, #94A3B8 100%) !important;
    border-top: 3px solid #F8FAFC !important;
    border-radius: 16px 16px 0 0 !important;
  }
  .podium-3rd {
    background: linear-gradient(180deg, #FED7AA 0%, #EA580C 100%) !important;
    border-top: 3px solid #FFEDD5 !important;
    border-radius: 16px 16px 0 0 !important;
  }

  /* ANIMATIONS */
  @keyframes mascotFloat {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-7px) rotate(2deg); }
  }
  @keyframes mascotDance {
    0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
    25% { transform: translateY(-12px) rotate(-6deg) scale(1.08); }
    50% { transform: translateY(0) rotate(0deg) scale(1); }
    75% { transform: translateY(-12px) rotate(6deg) scale(1.08); }
  }
  @keyframes pulseRocket {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.12) translateX(3px); }
  }
  @keyframes floatLab {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-8px) rotate(-3deg); }
  }
  @keyframes screenFadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .animate-mascot-float {
    animation: mascotFloat 3s ease-in-out infinite;
  }
  .animate-mascot-dance {
    animation: mascotDance 0.8s ease-in-out infinite;
  }
  .animate-pulse-rocket {
    animation: pulseRocket 1.8s ease-in-out infinite;
  }
  .animate-float-lab {
    animation: floatLab 3.5s ease-in-out infinite;
  }
  .animate-screen-in {
    animation: screenFadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .no-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
"""

if "/* FIGMA AI DESIGN SYSTEM (PREVIEW_FIGMA_AI TEMPLATE MATCH) */" not in html:
    html = html.replace("</style>", f"{figma_ai_css}\n</style>")

# Write out progress
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Step 1: CSS and Fonts upgraded successfully.")
