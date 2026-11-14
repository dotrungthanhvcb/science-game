#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ---------------------------------------------------------------------------
# 1. NÚT "TẮT NHẠC / BẬT NHẠC": Chuyển thành nút viên thuốc ngang
# ---------------------------------------------------------------------------
old_music_btn = """      <!-- NÚT BẬT TẮT NHẠC NỀN -->
      <button class="header-circle-btn" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung">
        <span id="music-icon"><i data-lucide="volume-2" style="width:18px; height:18px; stroke-width:2.5;"></i></span>
      </button>"""

new_music_btn = """      <!-- NÚT BẬT TẮT NHẠC NỀN (VIÊN THUỐC NGANG CHỐNG TRÀN CHỮ) -->
      <button class="inline-flex items-center gap-2 px-4 py-2 rounded-full whitespace-nowrap header-music-pill" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc nền tập trung" style="background:#1C2038; color:#FFFFFF; border:2px solid #2D3357; border-bottom:4px solid #0D0F1B; font-weight:800; font-size:0.85rem; cursor:pointer;">
        <i data-lucide="volume-x" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Bật Nhạc</span>
      </button>"""

if old_music_btn in content:
    content = content.replace(old_music_btn, new_music_btn, 1)
    print("1. Replaced music-btn in header with horizontal pill button")
else:
    print("Warning: old_music_btn not found")

# Update playMusic and stopMusic functions to maintain 1 line pill format with Lucide icons
old_play_music = """function playMusic() {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    isMusicPlaying = true;
    const btn = document.getElementById('music-btn');
    if (btn) {
      btn.classList.add('playing');
      btn.innerHTML = '<span>⏸️</span><span>Tắt Nhạc</span>';
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
    }"""

if old_play_music in content:
    content = content.replace(old_play_music, new_play_music, 1)
    print("1b. Updated playMusic() with Lucide volume-2 icon")
else:
    print("Warning: old_play_music not found")

old_stop_music = """function stopMusic() {
  isMusicPlaying = false;
  clearInterval(musicTimer);
  const btn = document.getElementById('music-btn');
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = '<span>🎵</span><span>Bật Nhạc</span>';
  }
}"""

new_stop_music = """function stopMusic() {
  isMusicPlaying = false;
  clearInterval(musicTimer);
  const btn = document.getElementById('music-btn');
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = '<i data-lucide="volume-x" style="width:18px; height:18px; stroke-width:2.5;"></i><span>Bật Nhạc</span>';
    refreshLucideIcons();
  }
}"""

if old_stop_music in content:
    content = content.replace(old_stop_music, new_stop_music, 1)
    print("1c. Updated stopMusic() with Lucide volume-x icon")
else:
    print("Warning: old_stop_music not found")

# ---------------------------------------------------------------------------
# 2. KHUNG ĐỒNG HỒ ĐẾM GIỜ TRONG MÀN HÌNH CHƠI: Thêm class inline-flex flex-row items-center gap-2 whitespace-nowrap
# ---------------------------------------------------------------------------
old_timer_html = """      <div class="timer-pill" id="quiz-timer">
        <i data-lucide="clock" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span id="timer-text">00:00</span>
      </div>"""

new_timer_html = """      <div class="timer-pill inline-flex flex-row items-center gap-2 whitespace-nowrap" id="quiz-timer" style="display:inline-flex; flex-direction:row; align-items:center; gap:8px; white-space:nowrap;">
        <i data-lucide="clock" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span id="timer-text">00:00</span>
      </div>"""

if old_timer_html in content:
    content = content.replace(old_timer_html, new_timer_html, 1)
    print("2. Added inline-flex flex-row items-center gap-2 whitespace-nowrap to quiz-timer")
else:
    print("Warning: old_timer_html not found")

# ---------------------------------------------------------------------------
# 3. THẺ "BẠN ĐỒNG HÀNH": Đặt flex items-center gap-3 để avatar tách biệt bên trái
# ---------------------------------------------------------------------------
old_mascot_hero = """      <!-- BẠN ĐỒNG HÀNH NGAY TRÊN HERO -->
      <div onclick="openMascotPickerModal()" style="display:inline-flex; align-items:center; gap:10px; background:white; border:2px solid #F5D6C6; padding:8px 18px; border-radius:9999px; cursor:pointer; box-shadow:0 4px 14px rgba(245, 214, 198, 0.4); transition:transform 0.2s;" title="Bấm để chọn bạn đồng hành khoa học!">
        <div id="welcome-mascot-svg-wrap" style="width:40px; height:40px;"></div>
        <div style="text-align:left;">
          <div style="font-size:0.72rem; color:#64748B; font-weight:700;">BẠN ĐỒNG HÀNH</div>
          <div style="font-size:0.9rem; font-weight:900; color:#1C2038;" id="welcome-mascot-name">Giáo Sư Cú Vọ ▾</div>
        </div>
      </div>"""

new_mascot_hero = """      <!-- BẠN ĐỒNG HÀNH NGAY TRÊN HERO (FLEXBOX CHUẨN KHÔNG ĐÈ CHỮ) -->
      <div onclick="openMascotPickerModal()" class="flex items-center gap-3 cursor-pointer select-none" style="display:inline-flex; align-items:center; gap:12px; background:white; border:2px solid #F5D6C6; padding:8px 20px 8px 10px; border-radius:9999px; box-shadow:0 4px 14px rgba(245, 214, 198, 0.4); transition:transform 0.2s;" title="Bấm để chọn bạn đồng hành khoa học!">
        <div id="welcome-mascot-svg-wrap" class="shrink-0 flex items-center justify-center overflow-hidden rounded-full" style="width:44px; height:44px; min-width:44px; max-width:44px; border-radius:50%; background:#FCECE4; overflow:hidden; display:flex; align-items:center; justify-content:center; flex-shrink:0;"></div>
        <div style="text-align:left; display:flex; flex-direction:column; gap:2px;">
          <div style="font-size:0.72rem; color:#64748B; font-weight:700; text-transform:uppercase; letter-spacing:0.04em;">BẠN ĐỒNG HÀNH</div>
          <div style="font-size:0.92rem; font-weight:900; color:#1C2038; white-space:nowrap;" id="welcome-mascot-name">Giáo Sư Cú Vọ ▾</div>
        </div>
      </div>"""

if old_mascot_hero in content:
    content = content.replace(old_mascot_hero, new_mascot_hero, 1)
    print("3. Updated welcome-mascot card to flex items-center gap-3 with separate avatar")
else:
    print("Warning: old_mascot_hero not found")

# Fix welcomeSvgWrap size call in updateAllMascotsUI from 75 to 42px
old_mascot_ui_call = """  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 75);"""

new_mascot_ui_call = """  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 42);"""

if old_mascot_ui_call in content:
    content = content.replace(old_mascot_ui_call, new_mascot_ui_call, 1)
    print("3b. Updated welcomeSvgWrap render size to 42px")
else:
    print("Warning: old_mascot_ui_call not found")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Step 2 micro fixes applied cleanly!")
