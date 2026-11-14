#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. FIX MUSIC BUTTON: PILL BUTTON & LUCIDE ICONS (VOLUME-2 / VOLUME-X)
# ---------------------------------------------------------------------------
old_music_header_btn = """      <!-- NÚT BẬT TẮT NHẠC NỀN -->
      <button class="header-circle-btn" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung">
        <span id="music-icon"><i data-lucide="volume-2" style="width:18px; height:18px; stroke-width:2.5;"></i></span>
      </button>"""

new_music_header_btn = """      <!-- NÚT BẬT TẮT NHẠC NỀN DẠNG VIÊN THUỐC NGANG -->
      <button class="music-pill-btn" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung">
        <i data-lucide="volume-x" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Bật Nhạc</span>
      </button>"""

if old_music_header_btn in content:
    content = content.replace(old_music_header_btn, new_music_header_btn, 1)
    print("1. Updated music button in header to music-pill-btn")
else:
    print("Warning: old_music_header_btn not found")

# Update playMusic and stopMusic functions
old_play_music = """function playMusic() {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    isMusicPlaying = true;
    const btn = document.getElementById('music-btn');
    if (btn) {
      btn.classList.add('playing');
      btn.innerHTML = '<span>⏸️</span><span>Tắt Nhạc</span>';
    }

    musicStep = 0;
    // Chu kỳ nhịp theo từng thể loại
    let intervalMs = 250;
    if (currentMusicTrack === 'upbeat') intervalMs = 125;
    else if (currentMusicTrack === 'lofi') intervalMs = 300;
    else if (currentMusicTrack === 'piano') intervalMs = 220;
    else if (currentMusicTrack === 'baroque') intervalMs = 260;

    musicTimer = setInterval(() => {
      if (!isMusicPlaying) return;
      playTrackStep();
    }, intervalMs);
  } catch(e) {
    console.log('Audio init note', e);
  }
}

function stopMusic() {
  isMusicPlaying = false;
  clearInterval(musicTimer);
  const btn = document.getElementById('music-btn');
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = '<span>🎵</span><span>Bật Nhạc</span>';
  }
}"""

new_play_music = """function playMusic() {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    isMusicPlaying = true;
    const btn = document.getElementById('music-btn');
    if (btn) {
      btn.classList.add('playing');
      btn.innerHTML = '<i data-lucide="volume-2" style="width:18px; height:18px; stroke-width:2.5; color:#FDE047;"></i><span>Tắt Nhạc</span>';
      refreshLucideIcons();
    }

    musicStep = 0;
    let intervalMs = 250;
    if (currentMusicTrack === 'upbeat') intervalMs = 125;
    else if (currentMusicTrack === 'lofi') intervalMs = 300;
    else if (currentMusicTrack === 'piano') intervalMs = 220;
    else if (currentMusicTrack === 'baroque') intervalMs = 260;

    musicTimer = setInterval(() => {
      if (!isMusicPlaying) return;
      playTrackStep();
    }, intervalMs);
  } catch(e) {
    console.log('Audio init note', e);
  }
}

function stopMusic() {
  isMusicPlaying = false;
  clearInterval(musicTimer);
  const btn = document.getElementById('music-btn');
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = '<i data-lucide="volume-x" style="width:18px; height:18px; stroke-width:2.5;"></i><span>Bật Nhạc</span>';
    refreshLucideIcons();
  }
}"""

if old_play_music in content:
    content = content.replace(old_play_music, new_play_music, 1)
    print("2. Updated playMusic() and stopMusic() with Lucide icons and single line pill format")
else:
    print("Warning: old_play_music not found")

# ---------------------------------------------------------------------------
# 2. FIX MASCOT CARD: HORIZONTAL FLEXBOX WITH SEPARATE AVATAR AND TEXT
# ---------------------------------------------------------------------------
old_mascot_pill_html = """      <!-- BẠN ĐỒNG HÀNH NGAY TRÊN HERO -->
      <div onclick="openMascotPickerModal()" style="display:inline-flex; align-items:center; gap:10px; background:white; border:2px solid #F5D6C6; padding:8px 18px; border-radius:9999px; cursor:pointer; box-shadow:0 4px 14px rgba(245, 214, 198, 0.4); transition:transform 0.2s;" title="Bấm để chọn bạn đồng hành khoa học!">
        <div id="welcome-mascot-svg-wrap" style="width:40px; height:40px;"></div>
        <div style="text-align:left;">
          <div style="font-size:0.72rem; color:#64748B; font-weight:700;">BẠN ĐỒNG HÀNH</div>
          <div style="font-size:0.9rem; font-weight:900; color:#1C2038;" id="welcome-mascot-name">Giáo Sư Cú Vọ ▾</div>
        </div>
      </div>"""

new_mascot_pill_html = """      <!-- BẠN ĐỒNG HÀNH NGAY TRÊN HERO (CHUẨN FLEXBOX NGANG TÁCH BIỆT) -->
      <div class="welcome-mascot-pill" onclick="openMascotPickerModal()" title="Bấm để chọn bạn đồng hành khoa học!">
        <div class="welcome-mascot-avatar" id="welcome-mascot-svg-wrap"></div>
        <div class="welcome-mascot-text">
          <div class="welcome-mascot-label">BẠN ĐỒNG HÀNH</div>
          <div class="welcome-mascot-title" id="welcome-mascot-name">Giáo Sư Cú Vọ ▾</div>
        </div>
      </div>"""

if old_mascot_pill_html in content:
    content = content.replace(old_mascot_pill_html, new_mascot_pill_html, 1)
    print("3. Updated welcome-mascot-pill markup")
else:
    print("Warning: old_mascot_pill_html not found")

# Fix welcomeSvgWrap size call in updateAllMascotsUI
old_mascot_ui_call = """  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 75);"""

new_mascot_ui_call = """  // 1. Welcome screen (kích thước avatar 48px chuẩn khít khung)
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 48);"""

if old_mascot_ui_call in content:
    content = content.replace(old_mascot_ui_call, new_mascot_ui_call, 1)
    print("4. Updated welcomeSvgWrap render size to 48px")
else:
    print("Warning: old_mascot_ui_call not found")

# ---------------------------------------------------------------------------
# 3. BACKGROUND DECORATIONS (STUDY & PLAY 4-CORNER ORGANIC BLOBS & DETAILED SVGS)
# ---------------------------------------------------------------------------
# Remove old template-deco blocks from welcome screen
old_deco_block_pattern = r"<!-- DECORATIONS FROM TEMPLATE -->[\s\S]*?<!-- Cánh diều sắc màu \+ Cầu vồng \(Phải dưới\) -->[\s\S]*?</div>\s*</div>"

# Check if old deco block exists
content = re.sub(
    r"<!-- DECORATIONS FROM TEMPLATE -->[\s\S]*?<!-- Cánh diều sắc màu \+ Cầu vồng \(Phải dưới\) -->\s*<div class=\"template-deco\"[\s\S]*?</div>\s*</div>",
    "<!-- CÁC HỌA TIẾT NỀN ĐÃ ĐƯỢC CHUYỂN THÀNH BACKGROUND-DECORATIONS ĐẦY ĐỦ Ở LAYER CHUNG -->",
    content
)
print("5. Removed old clipped template-deco from welcome screen")

# New unified background-decorations layer with 4 detailed corners
bg_decorations_html = """  <!-- =====================================================================
       HỆ THỐNG HỌA TIẾT NỀN CHUẨN MẪU THIẾT KẾ GỐC (STUDY & PLAY)
       ===================================================================== -->
  <div class="background-decorations" aria-hidden="true">
    <!-- GÓC TRÊN TRÁI: Kẹo mút xoắn hồng trắng, nơ đỏ, các ngôi sao -->
    <div class="deco-corner deco-tl">
      <svg class="deco-blob-svg" viewBox="0 0 340 340" fill="none">
        <path d="M0 0 L340 0 C310 90 280 180 200 240 C130 295 60 320 0 340 Z" fill="#FCECE4"/>
        <path d="M0 0 L250 0 C225 70 200 135 150 180 C95 230 40 250 0 260 Z" fill="#F8D8C9" opacity="0.45"/>
      </svg>
      <div class="deco-items">
        <!-- Kẹo mút xoắn hồng trắng -->
        <svg width="125" height="125" viewBox="0 0 120 120" fill="none" class="animate-float-slow">
          <line x1="45" y1="80" x2="16" y2="112" stroke="#78350F" stroke-width="7" stroke-linecap="round"/>
          <circle cx="72" cy="50" r="40" fill="#FF7096" stroke="#E11D48" stroke-width="3"/>
          <path d="M72 10 C94 10 112 28 112 50 C112 36 94 22 72 22 C50 22 32 36 32 50 C32 64 50 78 72 78 C94 78 106 64 106 50" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" fill="none"/>
          <path d="M72 22 C84 22 94 32 94 50 C94 62 84 72 72 72 C60 72 50 62 50 50 C50 38 60 32 72 32" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" fill="none"/>
          <circle cx="72" cy="50" r="6" fill="#FFFFFF"/>
        </svg>

        <!-- Chiếc nơ đỏ -->
        <svg width="88" height="72" viewBox="0 0 88 72" fill="none" class="animate-float-alt" style="margin-top:-18px; margin-left:14px;">
          <path d="M34 38 L18 68 L36 60 L44 70 L42 40" fill="#DC2626"/>
          <path d="M54 38 L70 68 L52 60 L44 70 L46 40" fill="#DC2626"/>
          <path d="M44 32 C30 12 10 22 15 36 C20 48 35 40 44 34 Z" fill="#EF4444" stroke="#B91C1C" stroke-width="2"/>
          <path d="M44 32 C58 12 78 22 73 36 C68 48 53 40 44 34 Z" fill="#EF4444" stroke="#B91C1C" stroke-width="2"/>
          <ellipse cx="44" cy="33" rx="8" ry="7" fill="#B91C1C"/>
          <ellipse cx="44" cy="33" rx="6" ry="5" fill="#EF4444"/>
        </svg>

        <!-- Ngôi sao đỏ & hồng -->
        <svg width="32" height="32" viewBox="0 0 32 32" style="position:absolute; top:20px; left:120px;">
          <polygon points="16,2 20,11 30,12 23,19 25,29 16,24 7,29 9,19 2,12 12,11" fill="#EF4444"/>
        </svg>
        <svg width="20" height="20" viewBox="0 0 20 20" style="position:absolute; top:90px; left:125px;">
          <polygon points="10,1 12,7 18,7 13,12 15,18 10,14 5,18 7,12 2,7 8,7" fill="#F87171"/>
        </svg>
      </div>
    </div>

    <!-- GÓC DƯỚI TRÁI: Ô tô cam, bút sáp xanh, hộp quà thắt nơ vàng -->
    <div class="deco-corner deco-bl">
      <svg class="deco-blob-svg" viewBox="0 0 340 340" fill="none">
        <path d="M0 340 L0 0 C60 25 130 50 200 110 C275 170 300 240 340 340 Z" fill="#FCECE4"/>
        <path d="M0 340 L0 80 C40 105 100 125 150 170 C200 220 220 270 240 340 Z" fill="#F8D8C9" opacity="0.45"/>
      </svg>
      <div class="deco-items">
        <!-- Ô tô đồ chơi màu cam -->
        <svg width="135" height="85" viewBox="0 0 135 85" fill="none" class="animate-float-slow">
          <rect x="15" y="34" width="105" height="32" rx="10" fill="#EA580C" stroke="#C2410C" stroke-width="2.5"/>
          <path d="M34 34 L48 14 L88 14 L100 34 Z" fill="#C2410C"/>
          <path d="M38 32 L50 16 L66 16 L66 32 Z" fill="#38BDF8"/>
          <path d="M70 32 L70 16 L84 16 L96 32 Z" fill="#38BDF8"/>
          <circle cx="38" cy="66" r="13" fill="#1E293B"/>
          <circle cx="38" cy="66" r="6" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
          <circle cx="94" cy="66" r="13" fill="#1E293B"/>
          <circle cx="94" cy="66" r="6" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
          <circle cx="118" cy="42" r="4" fill="#FEF08A"/>
        </svg>

        <div style="display:flex; align-items:flex-end; gap:6px; margin-top:-8px;">
          <!-- Bút sáp màu xanh -->
          <svg width="78" height="34" viewBox="0 0 78 34" fill="none" style="transform: rotate(-14deg);">
            <path d="M14 8 L66 8 L66 26 L14 26 Z" fill="#0284C7"/>
            <path d="M14 8 L2 17 L14 26 Z" fill="#0369A1"/>
            <rect x="24" y="8" width="28" height="18" fill="#38BDF8"/>
            <line x1="28" y1="8" x2="28" y2="26" stroke="#0284C7" stroke-width="2"/>
            <line x1="46" y1="8" x2="46" y2="26" stroke="#0284C7" stroke-width="2"/>
          </svg>

          <!-- Hộp quà tím thắt nơ vàng -->
          <svg width="86" height="80" viewBox="0 0 86 80" fill="none" class="animate-float-alt">
            <rect x="14" y="30" width="58" height="44" rx="7" fill="#7C3AED" stroke="#6D28D9" stroke-width="2"/>
            <rect x="37" y="30" width="12" height="44" fill="#FBBF24"/>
            <rect x="10" y="20" width="66" height="14" rx="4" fill="#EC4899" stroke="#DB2777" stroke-width="2"/>
            <rect x="37" y="20" width="12" height="14" fill="#FBBF24"/>
            <path d="M43 20 C33 4 20 12 34 20 Z" fill="#F59E0B" stroke="#D97706" stroke-width="1.5"/>
            <path d="M43 20 C53 4 66 12 52 20 Z" fill="#F59E0B" stroke="#D97706" stroke-width="1.5"/>
            <circle cx="43" cy="20" r="3.5" fill="#D97706"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- GÓC TRÊN PHẢI: Chữ cái A, B, C và tên lửa xanh đỏ bay lên -->
    <div class="deco-corner deco-tr">
      <svg class="deco-blob-svg" viewBox="0 0 340 340" fill="none">
        <path d="M340 0 L0 0 C25 80 55 170 135 240 C205 295 275 320 340 340 Z" fill="#FCECE4"/>
        <path d="M340 0 L90 0 C115 65 135 130 185 180 C240 230 295 250 340 260 Z" fill="#F8D8C9" opacity="0.45"/>
      </svg>
      <div class="deco-items">
        <!-- Chữ cái A, B, C -->
        <div style="display:flex; gap:10px; align-items:center; justify-content:flex-end; margin-right:12px; margin-bottom:4px;">
          <span style="font-size:2rem; font-weight:900; color:#8B5CF6; transform:rotate(-10deg); display:inline-block; text-shadow:0 2px 4px rgba(139,92,246,0.25);">A</span>
          <span style="font-size:2.2rem; font-weight:900; color:#EC4899; transform:rotate(8deg); display:inline-block; text-shadow:0 2px 4px rgba(236,72,153,0.25);">B</span>
          <span style="font-size:1.9rem; font-weight:900; color:#F59E0B; transform:rotate(-6deg); display:inline-block; text-shadow:0 2px 4px rgba(245,158,11,0.25);">C</span>
        </div>

        <!-- Tên lửa không gian sắc nét đầy đủ cánh và lửa đuôi -->
        <svg width="125" height="125" viewBox="0 0 120 120" fill="none" class="animate-float-slow" style="transform: rotate(-10deg); margin-left:auto;">
          <!-- Lửa đuôi tên lửa -->
          <path d="M78 78 Q92 108 104 110 Q92 95 86 85 Z" fill="#EF4444"/>
          <path d="M72 74 Q85 102 96 106 Q84 90 78 80 Z" fill="#F59E0B"/>
          <!-- Cánh tên lửa -->
          <polygon points="42,50 20,68 40,74" fill="#8B5CF6" stroke="#7C3AED" stroke-width="2"/>
          <polygon points="70,22 88,44 82,64" fill="#8B5CF6" stroke="#7C3AED" stroke-width="2"/>
          <!-- Thân tên lửa -->
          <path d="M76 18 C56 24 38 42 36 68 L68 68 C68 48 86 30 76 18 Z" fill="#06B6D4" stroke="#0891B2" stroke-width="2.5" transform="rotate(45 55 55)"/>
          <!-- Mũi đỏ -->
          <polygon points="30,12 42,26 18,36" fill="#EF4444" stroke="#DC2626" stroke-width="2"/>
          <!-- Cửa sổ tròn -->
          <circle cx="52" cy="52" r="10" fill="#1E293B" stroke="#E2E8F0" stroke-width="2.5"/>
          <circle cx="55" cy="49" r="2.5" fill="#FFFFFF"/>
        </svg>

        <!-- Ngôi sao vàng -->
        <svg width="28" height="28" viewBox="0 0 28 28" style="position:absolute; top:20px; right:140px;">
          <polygon points="14,2 17,9 25,10 19,16 21,24 14,20 7,24 9,16 3,10 11,9" fill="#F59E0B"/>
        </svg>
      </div>
    </div>

    <!-- GÓC DƯỚI PHẢI: Thuyền buồm, cánh diều 4 màu đuôi nơ, cầu vồng 7 sắc có mây -->
    <div class="deco-corner deco-br">
      <svg class="deco-blob-svg" viewBox="0 0 340 340" fill="none">
        <path d="M340 340 L340 0 C280 25 210 50 140 110 C65 170 40 240 0 340 Z" fill="#FCECE4"/>
        <path d="M340 340 L340 80 C300 105 240 125 190 170 C140 220 120 270 100 340 Z" fill="#F8D8C9" opacity="0.45"/>
      </svg>
      <div class="deco-items">
        <!-- Thuyền buồm nhỏ -->
        <svg width="100" height="90" viewBox="0 0 100 90" fill="none" class="animate-float-slow" style="margin-left: 24px;">
          <path d="M14 58 L85 58 L75 75 L24 75 Z" fill="#B45309" stroke="#78350F" stroke-width="2"/>
          <line x1="17" y1="63" x2="82" y2="63" stroke="#F59E0B" stroke-width="2"/>
          <line x1="50" y1="16" x2="50" y2="58" stroke="#78350F" stroke-width="3"/>
          <polygon points="50,16 62,22 50,28" fill="#EF4444"/>
          <path d="M54 22 L84 52 L54 52 Z" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.8"/>
          <path d="M46 26 L24 52 L46 52 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.8"/>
        </svg>

        <div style="display:flex; align-items:center; gap:8px; margin-top:-6px;">
          <!-- Cánh diều 4 màu đuôi nơ bay lượn -->
          <svg width="90" height="115" viewBox="0 0 90 115" fill="none" class="animate-float-alt">
            <polygon points="38,6 65,33 38,33" fill="#EF4444"/>
            <polygon points="38,6 11,33 38,33" fill="#EC4899"/>
            <polygon points="38,33 65,33 38,64" fill="#06B6D4"/>
            <polygon points="38,33 11,33 38,64" fill="#F59E0B"/>
            <line x1="38" y1="6" x2="38" y2="64" stroke="#1E293B" stroke-width="1.8"/>
            <line x1="11" y1="33" x2="65" y2="33" stroke="#1E293B" stroke-width="1.8"/>
            <path d="M38 64 Q28 80 42 90 Q56 100 38 112" stroke="#0F172A" stroke-width="1.8" fill="none"/>
            <polygon points="32,75 42,75 37,80" fill="#EF4444"/>
            <polygon points="40,92 50,92 45,97" fill="#F59E0B"/>
            <polygon points="34,106 44,106 39,111" fill="#06B6D4"/>
          </svg>

          <!-- Cầu vồng 7 sắc hoàn chỉnh kèm mây trắng -->
          <svg width="115" height="95" viewBox="0 0 115 95" fill="none" class="animate-float-slow">
            <path d="M18 75 A46 46 0 0 1 102 75" stroke="#8B5CF6" stroke-width="5.5" fill="none"/>
            <path d="M23.5 75 A40.5 40.5 0 0 1 96.5 75" stroke="#3B82F6" stroke-width="5" fill="none"/>
            <path d="M28.5 75 A35.5 35.5 0 0 1 91.5 75" stroke="#06B6D4" stroke-width="5" fill="none"/>
            <path d="M33.5 75 A30.5 30.5 0 0 1 86.5 75" stroke="#FBBF24" stroke-width="5" fill="none"/>
            <path d="M38.5 75 A25.5 25.5 0 0 1 81.5 75" stroke="#F97316" stroke-width="5" fill="none"/>
            <path d="M43.5 75 A20.5 20.5 0 0 1 76.5 75" stroke="#EF4444" stroke-width="5" fill="none"/>
            <!-- Mây trắng -->
            <circle cx="26" cy="74" r="13" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
            <circle cx="38" cy="70" r="15" fill="#FFFFFF"/>
            <circle cx="50" cy="74" r="11" fill="#FFFFFF"/>
            <rect x="16" y="72" width="38" height="10" fill="#FFFFFF"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
"""

# Place background-decorations right after <div class="main-wrapper">
if '<div class="background-decorations"' not in content:
    content = content.replace('<div class="main-wrapper">', '<div class="main-wrapper">\n' + bg_decorations_html, 1)
    print("6. Inserted unified background-decorations at the top of main-wrapper")

# ---------------------------------------------------------------------------
# 4. INJECT CSS FOR MUSIC PILL, MASCOT PILL, AND BACKGROUND DECORATIONS
# ---------------------------------------------------------------------------
new_fixes_css = """
  /* =========================================================================
     FIXES: MUSIC PILL, MASCOT PILL & 4-CORNER BACKGROUND DECORATIONS
     ========================================================================= */
  
  /* 1. NÚT NHẠC VIÊN THUỐC NGANG (CHỐNG TRÀN CHỮ HOÀN TOÀN) */
  .music-pill-btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    white-space: nowrap !important;
    background: #1C2038 !important;
    color: #FFFFFF !important;
    border: 2px solid #2D3357 !important;
    border-bottom: 4px solid #0D0F1B !important;
    border-radius: 9999px !important;
    padding: 8px 18px !important;
    font-size: 0.88rem !important;
    font-weight: 800 !important;
    cursor: pointer !important;
    transition: transform 0.12s ease, box-shadow 0.12s ease, background-color 0.15s ease !important;
    user-select: none !important;
    flex-shrink: 0 !important;
    outline: none !important;
  }
  .music-pill-btn:hover {
    background: #2D3357 !important;
    transform: translateY(-2px);
    border-bottom-width: 5px !important;
  }
  .music-pill-btn:active {
    transform: translateY(3px);
    border-bottom-width: 1px !important;
  }
  .music-pill-btn.playing {
    background: #E76F51 !important;
    border-color: #D65A3D !important;
    border-bottom: 4px solid #A83E26 !important;
    color: #FFFFFF !important;
  }

  /* 2. THẺ BẠN ĐỒNG HÀNH (FLEXBOX NGANG TÁCH BIỆT KHÔNG ĐÈ CHỮ) */
  .welcome-mascot-pill {
    display: inline-flex !important;
    align-items: center !important;
    gap: 16px !important;
    background: #FFFFFF !important;
    border: 2px solid #F5D6C6 !important;
    border-bottom: 4px solid #E2A68C !important;
    padding: 8px 24px 8px 12px !important;
    border-radius: 9999px !important;
    cursor: pointer !important;
    box-shadow: 0 6px 20px rgba(245, 214, 198, 0.45) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    user-select: none !important;
    margin-top: 10px !important;
  }
  .welcome-mascot-pill:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 24px rgba(245, 214, 198, 0.6) !important;
  }
  .welcome-mascot-pill:active {
    transform: translateY(2px) !important;
    border-bottom-width: 1px !important;
  }
  .welcome-mascot-avatar {
    width: 52px !important;
    height: 52px !important;
    min-width: 52px !important;
    max-width: 52px !important;
    border-radius: 50% !important;
    background: #FCECE4 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    overflow: hidden !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
  }
  .welcome-mascot-avatar svg {
    width: 48px !important;
    height: 48px !important;
    display: block !important;
    margin: 0 auto !important;
  }
  .welcome-mascot-text {
    text-align: left !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
  }
  .welcome-mascot-label {
    font-size: 0.72rem !important;
    color: #64748B !important;
    font-weight: 800 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
  }
  .welcome-mascot-title {
    font-size: 1rem !important;
    font-weight: 900 !important;
    color: #1C2038 !important;
    white-space: nowrap !important;
  }

  /* 3. LỚP NỀN TRANG TRÍ CHUẨN TEMPLATE STUDY & PLAY */
  .background-decorations {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }
  .deco-corner {
    position: absolute;
    pointer-events: none;
    z-index: 0;
    width: 290px;
    height: 290px;
  }
  .deco-tl {
    top: 0;
    left: 0;
  }
  .deco-bl {
    bottom: 0;
    left: 0;
  }
  .deco-tr {
    top: 0;
    right: 0;
  }
  .deco-br {
    bottom: 0;
    right: 0;
  }
  .deco-blob-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
  }
  .deco-items {
    position: relative;
    z-index: 1;
    padding: 12px;
  }
  .animate-float-slow {
    animation: floatSlow 6s ease-in-out infinite;
  }
  .animate-float-alt {
    animation: floatAlt 7.5s ease-in-out infinite;
  }

  /* ĐẢM BẢO NỘI DUNG CHÍNH LUÔN NẰM TRÊN LAYER Z-10 */
  .app-header, .screen, .quiz-card, .modal-box, .template-hero-box {
    position: relative !important;
    z-index: 10 !important;
  }

  /* THÍCH ỨNG MOBILE: THU NHỎ DECO ĐỂ KHÔNG CHE KHUẤT NỘI DUNG */
  @media (max-width: 900px) {
    .deco-corner {
      transform: scale(0.65);
      opacity: 0.35;
    }
    .deco-tl { transform-origin: top left; }
    .deco-tr { transform-origin: top right; }
    .deco-bl { transform-origin: bottom left; }
    .deco-br { transform-origin: bottom right; }
  }
  @media (max-width: 600px) {
    .deco-corner {
      display: none;
    }
  }
"""

content = content.replace("</style>", new_fixes_css + "\n</style>", 1)
print("7. Injected CSS fixes before </style>")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("All fixes applied successfully!")
