#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FIX getTopicSvg TO USE DYNAMIC GRADIENTS PER TOPIC
old_get_topic_svg_pattern = r"function getTopicSvg\(topic\)\s*\{[\s\S]*?return 'data:image/svg\+xml;utf8,' \+ encodeURIComponent\(svg\);\s*\}"

new_get_topic_svg = """function getTopicSvg(topic) {
  let c1 = '#4361EE';
  let c2 = '#4CC9F0';
  let iconEmoji = '🔬';
  let title = 'Khoa Học Vui';
  let subtitle = 'Đấu Trường Khoa Học Tiểu Học';

  if (topic === 'Động Vật') {
    c1 = '#FF5E62';
    c2 = '#FFA07A';
    iconEmoji = '🦁';
    title = 'Thế Giới Động Vật';
    subtitle = 'Tập tính, thức ăn & sinh thái tự nhiên';
  } else if (topic === 'Thực Vật') {
    c1 = '#10B981';
    c2 = '#059669';
    iconEmoji = '🌿';
    title = 'Thế Giới Thực Vật';
    subtitle = 'Cây xanh, quang hợp & các loài hoa';
  } else if (topic === 'Vũ Trụ & Thời Tiết') {
    c1 = '#3A0CA3';
    c2 = '#4361EE';
    iconEmoji = '🚀';
    title = 'Vũ Trụ & Thời Tiết';
    subtitle = 'Hệ Mặt Trời, các vì sao & khí hậu';
  } else if (topic === 'Cơ Thể Người') {
    c1 = '#E11D48';
    c2 = '#F43F5E';
    iconEmoji = '🫀';
    title = 'Cơ Thể Người & Sức Khỏe';
    subtitle = 'Các giác quan, dinh dưỡng & bảo vệ sức khỏe';
  } else if (topic === 'Địa Lý Việt Nam') {
    c1 = '#0284C7';
    c2 = '#06B6D4';
    iconEmoji = '🗺️';
    title = 'Địa Lý Non Sông Việt Nam';
    subtitle = 'Sông ngòi, đồi núi & các miền di sản';
  } else if (topic === 'Lịch Sử & Văn Hóa') {
    c1 = '#D97706';
    c2 = '#F59E0B';
    iconEmoji = '📜';
    title = 'Lịch Sử & Văn Hóa';
    subtitle = 'Danh nhân, phát minh & cội nguồn lịch sử';
  } else if (topic === 'Vật Chất & Hiện Tượng') {
    c1 = '#7C3AED';
    c2 = '#A855F7';
    iconEmoji = '⚡';
    title = 'Vật Lý & Năng Lượng';
    subtitle = 'Ánh sáng, âm thanh, nam châm & lực';
  }

  const gradId = 'grad_' + Math.abs((topic || 'all').split('').reduce((a,b)=>{a=((a<<5)-a)+b.charCodeAt(0);return a&a},0));

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340">
    <defs>
      <linearGradient id="${gradId}" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:${c1};stop-opacity:1" />
        <stop offset="100%" style="stop-color:${c2};stop-opacity:1" />
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#${gradId})" rx="20"/>
    <circle cx="300" cy="130" r="75" fill="rgba(255,255,255,0.22)"/>
    <circle cx="300" cy="130" r="88" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="8 6"/>
    <text x="50%" y="155" font-size="70" text-anchor="middle" dominant-baseline="middle">${iconEmoji}</text>
    <text x="50%" y="248" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" text-anchor="middle">${title}</text>
    <text x="50%" y="284" font-family="'Nunito', sans-serif" font-weight="700" font-size="14" fill="rgba(255,255,255,0.9)" text-anchor="middle">${subtitle}</text>
  </svg>`;

  return 'data:image/svg+xml;utf8,' + encodeURIComponent(svg);
}"""

content = re.sub(old_get_topic_svg_pattern, new_get_topic_svg, content, count=1)
print("1. Updated getTopicSvg with dynamic topic gradients")

# 2. EXTRACT 4 CORNER BACKGROUND DECORATIONS HTML
bg_decorations_standalone = """  <!-- =====================================================================
       HỆ THỐNG HỌA TIẾT NỀN CHUẨN MẪU THIẾT KẾ GỐC (FIXED INSET-0 Z-0)
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
          <path d="M78 78 Q92 108 104 110 Q92 95 86 85 Z" fill="#EF4444"/>
          <path d="M72 74 Q85 102 96 106 Q84 90 78 80 Z" fill="#F59E0B"/>
          <polygon points="42,50 20,68 40,74" fill="#8B5CF6" stroke="#7C3AED" stroke-width="2"/>
          <polygon points="70,22 88,44 82,64" fill="#8B5CF6" stroke="#7C3AED" stroke-width="2"/>
          <path d="M76 18 C56 24 38 42 36 68 L68 68 C68 48 86 30 76 18 Z" fill="#06B6D4" stroke="#0891B2" stroke-width="2.5" transform="rotate(45 55 55)"/>
          <polygon points="30,12 42,26 18,36" fill="#EF4444" stroke="#DC2626" stroke-width="2"/>
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
  </div>"""

# Remove previous background-decorations from within main-wrapper if present
content = re.sub(r"<div class=\"background-decorations\"[\s\S]*?</div>\s*</div>\s*</div>\s*</div>", "", content)
content = re.sub(r"<div class=\"main-wrapper\">\s*", "", content, count=1)
# Remove closing </div> of main-wrapper near end
content = re.sub(r"</div>\s*<!-- =====================================================================\s*MODAL:", "<!-- =====================================================================\n       MODAL:", content)

# Remove the empty welcome-screen entirely!
content = re.sub(
    r"<!-- =====================================================================\s*0\. WELCOME SCREEN[\s\S]*?<!-- =====================================================================\s*1\. HOME SCREEN",
    "<!-- =====================================================================\n       1. HOME SCREEN",
    content
)
print("2. Removed empty welcome screen")

# Ensure #home-screen has class="quiz-card screen active"
content = re.sub(r'<div class="quiz-card screen"\s+id="home-screen">', '<div class="quiz-card screen active" id="home-screen">', content)
print("3. Made home-screen active by default")

# 3. ADD SOURCE CHIPS CONTAINER TO HOME SCREEN
# Check if source-chips-container is in home-screen
if 'id="source-chips-container"' not in content:
    source_chips_section = """          <!-- BỘ LỌC CHỌN 1 HOẶC NHIỀU NGUỒN CÂU HỎI KÈM SỐ LƯỢNG KHẢ DỤNG -->
          <div style="margin-top: 10px; margin-bottom: 10px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <label style="font-size:0.88rem; font-weight:800; color:#1C2038;">📚 Nguồn học liệu (Chọn 1 hoặc nhiều nguồn):</label>
              <button type="button" onclick="selectAllSources()" style="background:#FCECE4; color:#1C2038; border:1px solid #F5D6C6; font-size:0.75rem; font-weight:800; padding:4px 10px; border-radius:9999px; cursor:pointer;">
                ✓ Chọn tất cả
              </button>
            </div>
            <div id="source-chips-container" class="source-chips-grid"></div>
          </div>
"""
    # Insert right before "Chế độ lặp lại"
    content = content.replace('<div class="config-row-compact">\n            <label>🧠 Chế độ lặp lại:</label>', source_chips_section + '          <div class="config-row-compact">\n            <label>🧠 Chế độ lặp lại:</label>', 1)
    print("4. Inserted source-chips-container into home-screen")

# 4. WRAP IN CLEAN VERTICAL LAYOUT:
# <body>
#   <div class="background-decorations">...</div>
#   <div class="app-layout">
#     <header class="app-header">...</header>
#     <main class="main-content-area">...screens...</main>
#   </div>
#   ...modals...
# </body>

# Wrap header and screens:
# Replace <body> with <body>\n + bg_decorations_standalone + \n<div class="app-layout w-full max-w-6xl mx-auto flex flex-col items-center px-4 py-4 relative z-10">\n
content = re.sub(r"<body[^>]*>", "<body>\n" + bg_decorations_standalone + '\n  <div class="app-layout">\n', content, count=1)

# Ensure <header class="app-header"> is inside app-layout, then <main class="main-content-area"> begins right after </header>
content = re.sub(r"(</header>)", r"\1\n\n    <!-- KHU VỰC NỘI DUNG CHÍNH (XẾP DỌC BÊN DƯỚI HEADER) -->\n    <main class=\"main-content-area\">\n", content, count=1)

# Close </main> and </div> (app-layout) right before the modals!
content = re.sub(r"(\s*<!-- =====================================================================\s*MODAL: QUẢN LÝ DANH SÁCH USER)", r"\n    </main>\n  </div>\n\1", content, count=1)
print("5. Wrapped layout into vertical body > app-layout > header + main")

# 5. INJECT COMPREHENSIVE VERTICAL LAYOUT CSS OVERRIDE BEFORE </style>
vertical_layout_css = """
  /* =========================================================================
     KHÔI PHỤC BỐ CỤC XẾP DỌC CHUẨN & CHỐNG ÉP BẸP MÀN HÌNH
     ========================================================================= */
  html, body {
    width: 100% !important;
    min-height: 100vh !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: #FFF6ED !important;
    color: #1C2038 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: flex-start !important;
    overflow-x: hidden !important;
  }

  /* LỚP NỀN HỌA TIẾT TOÀN MÀN HÌNH (FIXED INSET-0 Z-0 TÁCH BIỆT) */
  .background-decorations {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    pointer-events: none !important;
    z-index: 0 !important;
    overflow: hidden !important;
  }
  .deco-corner {
    position: absolute !important;
    pointer-events: none !important;
    z-index: 0 !important;
    width: 280px !important;
    height: 280px !important;
  }
  .deco-tl { top: 0 !important; left: 0 !important; }
  .deco-bl { bottom: 0 !important; left: 0 !important; }
  .deco-tr { top: 0 !important; right: 0 !important; }
  .deco-br { bottom: 0 !important; right: 0 !important; }
  .deco-blob-svg {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 0 !important;
  }
  .deco-items {
    position: relative !important;
    z-index: 1 !important;
    padding: 10px !important;
  }

  /* KHUNG CHỨA TOÀN TRANG (FLEX-DIRECTION COLUMN, CĂN GIỮA) */
  .app-layout {
    width: 100% !important;
    max-width: 1140px !important;
    margin: 0 auto !important;
    padding: 16px 20px 40px !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    position: relative !important;
    z-index: 10 !important;
    box-sizing: border-box !important;
  }

  /* THANH HEADER TRÊN CÙNG TRẢI DÀI THEO CHIỀU NGANG */
  .app-header {
    width: 100% !important;
    max-width: 1140px !important;
    margin: 0 0 20px 0 !important;
    background: #FFFFFF !important;
    border: 2px solid #F5D6C6 !important;
    border-bottom: 5px solid #E2A68C !important;
    border-radius: 9999px !important;
    padding: 10px 24px !important;
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: center !important;
    box-shadow: 0 6px 20px rgba(28, 32, 56, 0.08) !important;
    box-sizing: border-box !important;
    position: relative !important;
    z-index: 10 !important;
  }

  /* KHU VỰC NỘI DUNG CHÍNH (XẾP DỌC BÊN DƯỚI HEADER) */
  .main-content-area {
    width: 100% !important;
    max-width: 1060px !important;
    margin: 0 auto !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    position: relative !important;
    z-index: 10 !important;
    box-sizing: border-box !important;
  }

  /* KHUNG BÀI THI & TRANG CHỦ (.quiz-card) */
  .quiz-card {
    width: 100% !important;
    max-width: 1060px !important;
    background: #FFFFFF !important;
    border-radius: 28px !important;
    border: 3px solid #F5D6C6 !important;
    box-shadow: 0 16px 40px rgba(28, 32, 56, 0.1) !important;
    padding: clamp(20px, 2.5vw, 36px) !important;
    box-sizing: border-box !important;
    margin: 0 auto !important;
  }

  .screen {
    display: none !important;
    width: 100% !important;
  }
  .screen.active {
    display: block !important;
    width: 100% !important;
  }

  /* GRID NGUỒN CÂU HỎI TRÊN MÀN HOME */
  .source-chips-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
    gap: 12px !important;
    width: 100% !important;
  }

  /* ĐỒNG HỒ ĐẾM GIỜ NẰM THẲNG 1 HÀNG */
  .timer-pill {
    display: inline-flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    white-space: nowrap !important;
    background: #FFF8EB !important;
    color: #D97706 !important;
    border: 2px solid #FCD34D !important;
    border-bottom: 4px solid #F59E0B !important;
    border-radius: 9999px !important;
    padding: 8px 18px !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    letter-spacing: 0.05em !important;
    flex-shrink: 0 !important;
  }

  /* CHỐNG VỠ CHỮ TRÊN CÁC NÚT ĐÁP ÁN (TUYỆT ĐỐI KHÔNG CẮT ĐÔI TỪ) */
  .choice-option, .choice-text-inner, .question-title, button {
    word-break: break-words !important;
    overflow-wrap: break-word !important;
    white-space: normal !important;
    hyphens: manual !important;
  }

  /* RESPONSIVE TRÊN MOBILE */
  @media (max-width: 900px) {
    .deco-corner {
      transform: scale(0.65);
      opacity: 0.3;
    }
    .deco-tl { transform-origin: top left; }
    .deco-tr { transform-origin: top right; }
    .deco-bl { transform-origin: bottom left; }
    .deco-br { transform-origin: bottom right; }
    .app-header {
      border-radius: 20px !important;
      padding: 12px 16px !important;
      gap: 10px !important;
      flex-wrap: wrap !important;
    }
  }
  @media (max-width: 640px) {
    .deco-corner {
      display: none !important;
    }
    .app-layout {
      padding: 8px 10px 24px !important;
    }
  }
"""

content = content.replace("</style>", vertical_layout_css + "\n</style>", 1)
print("6. Injected vertical layout CSS rules before </style>")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Overhaul script finished successfully!")
