#!/usr/bin/env python3
"""
Apply Figma AI Design Template (Topics Science lab, Quiz Space explorer, Leaderboard Weekly stars)
to index.html with production-grade Typography (Baloo 2 + Be Vietnam Pro) and Tactile 3D UI.
"""

import re
import os
import sys

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD GOOGLE FONTS (Baloo 2 & Be Vietnam Pro)
old_font = '<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&display=swap" rel="stylesheet">'
new_font = '''<!-- GOOGLE FONTS: BALOO 2 (CUTE BOUNCY HEADINGS) & BE VIETNAM PRO (CRISP UI & BODY) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Be+Vietnam+Pro:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'''

if old_font in html:
    html = html.replace(old_font, new_font)
elif "Baloo+2" not in html:
    html = html.replace("</head>", f"  {new_font}\n</head>")

# 2. ADD COMPREHENSIVE FIGMA AI CSS STYLES TO <style>
figma_ai_css = """
  /* =========================================================================
     FIGMA AI DESIGN SYSTEM: TYPOGRAPHY, 3D TACTILE BUTTONS & MODERN SCIENCE LAB
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
  .template-btn-pill, 
  .btn-3d, 
  .home-card-header, 
  .timer-pill, 
  .result-headline, 
  .badge-source,
  .template-logo span,
  .btn-next-step {
    font-family: 'Baloo 2', 'Be Vietnam Pro', cursive, sans-serif !important;
    letter-spacing: -0.015em;
  }

  /* TACTILE 3D BUTTONS */
  .btn-3d {
    position: relative;
    transition: all 0.12s ease;
    user-select: none;
    cursor: pointer;
  }
  .btn-3d:active {
    transform: translateY(3px);
  }

  /* Nút Bắt Đầu 3D Cyan (Figma AI Style) */
  .btn-start, .template-btn-pill {
    background: linear-gradient(180deg, #06B6D4 0%, #0891B2 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #0E7490 !important;
    border-bottom: 5px solid #155E75 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
    box-shadow: 0 10px 25px -5px rgba(6, 182, 212, 0.4) !important;
    transition: all 0.12s ease !important;
  }
  .btn-start:hover, .template-btn-pill:hover {
    filter: brightness(1.08);
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .btn-start:active, .template-btn-pill:active {
    transform: translateY(3px);
    border-bottom-width: 2px !important;
  }

  /* Nút Tiếp Theo 3D */
  .btn-next-step {
    background: linear-gradient(180deg, #06B6D4 0%, #0891B2 100%) !important;
    color: #FFFFFF !important;
    border: 2px solid #0E7490 !important;
    border-bottom: 5px solid #155E75 !important;
    border-radius: 9999px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 20px -4px rgba(6, 182, 212, 0.35) !important;
  }
  .btn-next-step:hover {
    filter: brightness(1.08);
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .btn-next-step:active {
    transform: translateY(3px);
    border-bottom-width: 2px !important;
  }

  /* THẺ ĐÁP ÁN TRẮC NGHIỆM 3D (CHỐNG TRÀN CHỮ, BẤM LÚN CHÂN THỰC) */
  .choice-option {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    padding: 12px 18px !important;
    min-height: 64px !important;
    height: auto !important;
    background: #FFFFFF !important;
    border: 2px solid #E2E8F0 !important;
    border-bottom: 5px solid #CBD5E1 !important;
    border-radius: 20px !important;
    transition: all 0.12s ease !important;
    cursor: pointer !important;
    user-select: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    white-space: normal !important;
    word-break: break-word !important;
  }
  .choice-option:hover {
    border-color: #38BDF8 !important;
    background: #F0F9FF !important;
    transform: translateY(-2px);
    border-bottom-width: 6px !important;
  }
  .choice-option:active {
    transform: translateY(3px);
    border-bottom-width: 2px !important;
  }
  .choice-option.selected {
    border-color: #06B6D4 !important;
    background: #ECFEFF !important;
    border-bottom: 5px solid #0891B2 !important;
    color: #0E7490 !important;
  }
  .choice-letter {
    width: 36px !important;
    height: 36px !important;
    min-width: 36px !important;
    border-radius: 12px !important;
    background: #F1F5F9 !important;
    color: #475569 !important;
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 1px solid #E2E8F0 !important;
  }
  .choice-option.selected .choice-letter {
    background: #06B6D4 !important;
    color: #FFFFFF !important;
    border-color: #0891B2 !important;
  }

  /* THẺ CHỦ ĐỀ PHÒNG LAB (TOPICS SCIENCE LAB STYLE) */
  .topic-pill {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 10px 14px !important;
    background: #FFFFFF !important;
    border: 2px solid #F1F5F9 !important;
    border-bottom: 4px solid #E2E8F0 !important;
    border-radius: 18px !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    color: #1E293B !important;
  }
  .topic-pill:hover {
    border-color: #38BDF8 !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 18px -4px rgba(6, 182, 212, 0.18) !important;
  }
  .topic-pill.selected {
    border-color: #06B6D4 !important;
    background: #ECFEFF !important;
    border-bottom: 4px solid #0891B2 !important;
    color: #0891B2 !important;
    font-weight: 800 !important;
  }

  /* THANH HEADER ĐIỀU HƯỚNG HIỆN ĐẠI (FIGMA AI GLOSSY DARK PILL) */
  .app-header {
    background: #0F172A !important;
    border: 1.5px solid #1E293B !important;
    border-bottom: 4px solid #020617 !important;
    border-radius: 9999px !important;
    padding: 10px 24px !important;
    box-shadow: 0 12px 30px -8px rgba(15, 23, 42, 0.35) !important;
    color: #FFFFFF !important;
  }
  .template-logo span {
    color: #38BDF8 !important;
    font-weight: 800 !important;
    letter-spacing: 0.02em !important;
  }
  .template-nav-item {
    color: #94A3B8 !important;
    font-weight: 700 !important;
    padding: 6px 14px !important;
    border-radius: 9999px !important;
    transition: all 0.12s ease !important;
  }
  .template-nav-item:hover {
    color: #FFFFFF !important;
    background: rgba(255, 255, 255, 0.08) !important;
  }
  .template-nav-item.active {
    color: #FFFFFF !important;
    background: #0891B2 !important;
    box-shadow: 0 2px 8px rgba(8, 145, 178, 0.4) !important;
  }

  /* KHUNG CÂU HỎI VŨ TRỤ (QUIZ SPACE EXPLORER STYLE) */
  .question-title {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.35rem !important;
    line-height: 1.4 !important;
    color: #0F172A !important;
    margin-bottom: 16px !important;
  }

  /* PODIUM TOP 1, 2, 3 (LEADERBOARD WEEKLY STARS STYLE) */
  .podium-container {
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 12px;
    padding: 20px 0 10px 0;
  }
  .podium-block-1st {
    background: linear-gradient(180deg, #FDE047 0%, #F59E0B 100%);
    border-top: 3px solid #FEF08A;
    border-radius: 18px 18px 0 0;
    box-shadow: 0 8px 20px rgba(245, 158, 11, 0.3);
  }
  .podium-block-2nd {
    background: linear-gradient(180deg, #E2E8F0 0%, #94A3B8 100%);
    border-top: 3px solid #F8FAFC;
    border-radius: 16px 16px 0 0;
  }
  .podium-block-3rd {
    background: linear-gradient(180deg, #FED7AA 0%, #EA580C 100%);
    border-top: 3px solid #FFEDD5;
    border-radius: 16px 16px 0 0;
  }
"""

if "FIGMA AI DESIGN SYSTEM" not in html:
    html = html.replace("</style>", f"{figma_ai_css}\n</style>")

# 3. UPGRADE LEADERBOARD FUNCTION: RENDER PODIUM TOP 1, 2, 3 IF AT LEAST 3 PLAYERS
podium_render_code = """function renderLeaderboardList(players) {
  const listElem = document.getElementById('lead-players-list');
  if (!listElem) return;

  if (players.length === 0) {
    listElem.innerHTML = '<div style="text-align:center; padding:30px; color:#64748B;">Chưa có bạn nào trong lớp này. Bé hãy là người đầu tiên ghi danh nhé!</div>';
    return;
  }

  let html = '';

  // NẾU CÓ TỪ 3 BẠN TRỞ LÊN: VẼ BỤC VINH QUANG PODIUM CHUẨN FIGMA AI (LEADERBOARD WEEKLY STARS)
  if (players.length >= 3) {
    const p1 = players[0];
    const p2 = players[1];
    const p3 = players[2];

    html += `
      <div class="podium-container" style="display:flex; align-items:flex-end; justify-content:center; gap:10px; margin-bottom:18px; padding-top:12px;">
        <!-- HẠNG 2: BẠC -->
        <div style="display:flex; flex-direction:column; align-items:center; width:95px;">
          <div style="width:48px; height:48px; border-radius:50%; border:2px solid #CBD5E1; background:#F1F5F9; display:flex; align-items:center; justify-content:center; font-size:22px; margin-bottom:4px; box-shadow:0 3px 8px rgba(0,0,0,0.06);">
            🥈
          </div>
          <div style="font-family:'Baloo 2', sans-serif; font-weight:800; font-size:0.88rem; color:#1E293B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:90px; text-align:center;">
            ${p2.name}
          </div>
          <div style="font-size:0.75rem; font-weight:800; color:#0284C7; margin-bottom:4px;">
            ${p2.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-block-2nd" style="width:100%; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Baloo 2', sans-serif; font-weight:800;">
            <span style="font-size:1.2rem;">2</span>
            <span style="font-size:0.68rem; opacity:0.9;">Á QUÂN</span>
          </div>
        </div>

        <!-- HẠNG 1: VÀNG (QUÁN QUÂN) -->
        <div style="display:flex; flex-direction:column; align-items:center; width:115px; margin-top:-16px;">
          <div style="position:relative;">
            <span style="position:absolute; top:-14px; left:50%; transform:translateX(-50%); font-size:16px;">👑</span>
            <div style="width:58px; height:58px; border-radius:50%; border:3px solid #F59E0B; background:#FEF3C7; display:flex; align-items:center; justify-content:center; font-size:26px; margin-bottom:4px; box-shadow:0 6px 14px rgba(245, 158, 11, 0.35); ring:4px; ring-color:rgba(253, 224, 71, 0.5);">
              🥇
            </div>
          </div>
          <div style="font-family:'Baloo 2', sans-serif; font-weight:800; font-size:0.95rem; color:#92400E; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:110px; text-align:center;">
            ${p1.name}
          </div>
          <div style="font-size:0.8rem; font-weight:900; color:#D97706; margin-bottom:4px;">
            ${p1.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-block-1st" style="width:100%; height:95px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#78350F; font-family:'Baloo 2', sans-serif; font-weight:900;">
            <span style="font-size:1.5rem;">1</span>
            <span style="font-size:0.75rem; letter-spacing:0.04em;">QUÁN QUÂN</span>
          </div>
        </div>

        <!-- HẠNG 3: ĐỒNG -->
        <div style="display:flex; flex-direction:column; align-items:center; width:95px;">
          <div style="width:48px; height:48px; border-radius:50%; border:2px solid #EA580C; background:#FFEDD5; display:flex; align-items:center; justify-content:center; font-size:22px; margin-bottom:4px; box-shadow:0 3px 8px rgba(0,0,0,0.06);">
            🥉
          </div>
          <div style="font-family:'Baloo 2', sans-serif; font-weight:800; font-size:0.88rem; color:#1E293B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:90px; text-align:center;">
            ${p3.name}
          </div>
          <div style="font-size:0.75rem; font-weight:800; color:#0284C7; margin-bottom:4px;">
            ${p3.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-block-3rd" style="width:100%; height:55px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:'Baloo 2', sans-serif; font-weight:800;">
            <span style="font-size:1.1rem;">3</span>
            <span style="font-size:0.68rem; opacity:0.9;">HẠNG BA</span>
          </div>
        </div>
      </div>
    `;
  }

  // DANH SÁCH CÁC HẠNG TIẾP THEO (TỪ TOP 4 TRỞ ĐI HOẶC TOÀN BỘ NẾU DƯỚI 3 BẠN)
  const listStartIndex = players.length >= 3 ? 3 : 0;
  const remainingPlayers = players.slice(listStartIndex, 25);

  remainingPlayers.forEach((p, rIdx) => {
    const idx = listStartIndex + rIdx;
    let rankBadge = `${idx + 1}`;
    let rankStyle = "background:#F1F5F9; color:#475569;";
    if (idx === 0) {
      rankBadge = "🥇";
      rankStyle = "background:#FEF3C7; color:#B45309; font-size:1.3rem;";
    } else if (idx === 1) {
      rankBadge = "🥈";
      rankStyle = "background:#F1F5F9; color:#475569; font-size:1.2rem;";
    } else if (idx === 2) {
      rankBadge = "🥉";
      rankStyle = "background:#FFEDD5; color:#9A3412; font-size:1.1rem;";
    }

    html += `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:12px 16px; background:white; border:2px solid #F1F5F9; border-bottom:3px solid #E2E8F0; border-radius:16px; margin-bottom:8px; box-shadow:0 2px 6px rgba(0,0,0,0.02); transition:transform 0.1s ease;">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:36px; height:36px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-family:'Baloo 2', sans-serif; font-weight:800; font-size:0.95rem; ${rankStyle}">
            ${rankBadge}
          </div>
          <div>
            <div style="font-family:'Baloo 2', sans-serif; font-weight:800; color:#0F172A; font-size:0.95rem;">${p.name}</div>
            <div style="font-size:0.75rem; color:#64748B; display:flex; gap:6px; align-items:center; margin-top:2px;">
              <span style="background:#F8FAFC; border:1px solid #E2E8F0; padding:1px 6px; border-radius:4px; font-weight:700;">${p.studentClass || 'Lớp 2'}</span>
              <span>• ${p.totalTests || 1} bài đã thi</span>
            </div>
          </div>
        </div>

        <div style="text-align:right;">
          <div style="font-family:'Baloo 2', sans-serif; font-size:1.15rem; font-weight:900; color:#0891B2;">${p.highestScore || 0}<span style="font-size:0.75rem; color:#64748B;">/10</span></div>
          <div style="font-size:0.72rem; font-weight:800; color:#F59E0B;">⭐ ${p.badge || 'Xuất Sắc'}</div>
        </div>
      </div>
    `;
  });

  listElem.innerHTML = html;
  refreshLucideIcons();
}"""

# Replace renderLeaderboardList
pattern_lb = r'function renderLeaderboardList\(players\)\s*\{[\s\S]*?\n\}'
if re.search(pattern_lb, html):
    html = re.sub(pattern_lb, podium_render_code, html, count=1)
    print("Upgraded renderLeaderboardList with Top 3 Podium!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied Figma AI design system to index.html successfully!")
