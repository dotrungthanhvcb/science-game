#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. ADD BANNER AND STUDENT FILTER INTO history-screen
old_filter_bar = """        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh, lớp..." oninput="renderHistoryTable()">"""

new_filter_bar = """        <!-- BỘ LỌC HỌC SINH RIÊNG CHO QUẢN TRỊ VIÊN -->
        <select class="history-filter-select" id="history-filter-student" onchange="renderHistoryTable()" style="display:none; border-color:#FECACA; background:#FEF2F2; color:#991B1B; font-weight:800;">
          <option value="all">👑 Tất cả học sinh (Admin View)</option>
        </select>
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh, lớp..." oninput="renderHistoryTable()">"""

if old_filter_bar in content:
    content = content.replace(old_filter_bar, new_filter_bar, 1)
    print("1. Added student filter in history-screen filter bar.")

old_history_dash = """      <!-- DASHBOARD TỔNG QUAN -->
      <div class="history-dashboard-grid">"""

new_history_dash = """      <!-- BANNER PHÂN QUYỀN HỌC SINH / ADMIN -->
      <div id="history-role-banner"></div>

      <!-- DASHBOARD TỔNG QUAN -->
      <div class="history-dashboard-grid">"""

if old_history_dash in content:
    content = content.replace(old_history_dash, new_history_dash, 1)
    print("2. Added history role banner above dashboard.")

# 2. UPDATE WELCOME SCREEN MASCOT WITH INTERACTIVE PICKER
old_welcome_mascot = """      <div class="welcome-mascot-box">
        <svg viewBox="0 0 100 100" style="width:75px; height:75px;">
          <circle cx="50" cy="50" r="42" fill="#FFD166" stroke="#F4A261" stroke-width="3"/>
          <ellipse cx="36" cy="46" rx="5" ry="7" fill="#1D3557"/>
          <ellipse cx="64" cy="46" rx="5" ry="7" fill="#1D3557"/>
          <circle cx="38" cy="43" r="2" fill="white"/>
          <circle cx="66" cy="43" r="2" fill="white"/>
          <path d="M38 58 Q50 74 62 58" stroke="#E76F51" stroke-width="3" fill="#E76F51"/>
          <!-- Má hồng -->
          <circle cx="28" cy="54" r="5" fill="#FF8FAB" opacity="0.6"/>
          <circle cx="72" cy="54" r="5" fill="#FF8FAB" opacity="0.6"/>
          <!-- Tay vẫy chào -->
          <path d="M78 50 Q92 38 88 28 Q80 34 76 44" fill="#FFD166" stroke="#F4A261" stroke-width="2"/>
        </svg>
      </div>"""

new_welcome_mascot = """      <div class="welcome-mascot-box mascot-interactive" id="welcome-mascot-box" onclick="openMascotPickerModal()" title="Bấm để chọn bạn đồng hành khoa học yêu thích!">
        <div id="welcome-mascot-svg-wrap"></div>
      </div>
      <div onclick="openMascotPickerModal()" style="display:inline-flex; align-items:center; gap:6px; cursor:pointer; background:white; padding:4px 12px; border-radius:20px; border:1.5px solid #C7D2FE; margin-top:6px; box-shadow:0 2px 6px rgba(67, 97, 238, 0.1);">
        <span style="font-size:0.8rem; font-weight:800; color:var(--primary);">✨ Bạn Đồng Hành: <span id="welcome-mascot-name">Giáo Sư Cú Vọ</span> ▾</span>
      </div>"""

if old_welcome_mascot in content:
    content = content.replace(old_welcome_mascot, new_welcome_mascot, 1)
    print("3. Updated welcome screen mascot box.")

# 3. UPDATE QUIZ SCREEN MASCOT WITH DYNAMIC SVG AND ONCLICK
old_quiz_mascot = """        <div class="mascot-container">
          <svg class="mascot-avatar" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="42" fill="#FFD8B5" stroke="#FFAE73" stroke-width="2"/>
            <path d="M25 35 Q50 15 75 35 Q50 25 25 35 Z" fill="#6A4C93"/>
            <polygon points="50,15 45,28 55,28" fill="#FFCA3A"/>
            <circle cx="38" cy="48" r="5" fill="#1D3557"/>
            <circle cx="62" cy="48" r="5" fill="#1D3557"/>
            <circle cx="40" cy="46" r="1.5" fill="white"/>
            <circle cx="64" cy="46" r="1.5" fill="white"/>
            <path d="M40 60 Q50 70 60 60" stroke="#FF595E" stroke-width="3" fill="none" id="mascot-mouth"/>
          </svg>
          <div class="mascot-bubble" id="mascot-speech">Bé đọc kỹ câu hỏi nhé, Bo Bo tin bé làm được! 🌟</div>
        </div>"""

new_quiz_mascot = """        <div class="mascot-container mascot-interactive" onclick="onMascotClick()" title="Bấm vào tớ để nghe sự thật khoa học kỳ thú!">
          <div id="quiz-mascot-svg-wrap" class="mascot-avatar" style="display:flex; align-items:center; justify-content:center;"></div>
          <div class="mascot-bubble" id="mascot-speech">Bé đọc kỹ câu hỏi nhé, chúng mình cùng chinh phục đỉnh cao khoa học! 🌟</div>
        </div>"""

if old_quiz_mascot in content:
    content = content.replace(old_quiz_mascot, new_quiz_mascot, 1)
    print("4. Updated quiz screen mascot container.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML template replacements complete!")
