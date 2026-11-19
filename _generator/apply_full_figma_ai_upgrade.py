#!/usr/bin/env python3
"""
Overhaul index.html into the complete Figma AI Template matching:
https://science-game-sigma.vercel.app/preview_figma_ai.html
- Frame 1: Topics · Science lab
- Frame 2: Quiz · Space explorer
- Frame 3: Leaderboard · Weekly stars with Fireworks animation
"""

import re
import sys
import subprocess

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# =========================================================================
# 1. UPGRADE HEADER TO FIGMA AI DESIGN TEMPLATE
# =========================================================================
new_header = """<header class="app-header w-full bg-slate-900/95 backdrop-blur border border-slate-800 text-white px-4 py-3 sticky top-0 z-50 shadow-xl rounded-2xl mb-4" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
    <div class="flex items-center gap-2.5 cursor-pointer" onclick="navigateToTab('home')" title="Về Phòng Thí Nghiệm">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center text-xl shadow-md shrink-0">
        ✨
      </div>
      <div>
        <div class="font-baloo font-bold text-base text-cyan-400 tracking-wide flex items-center gap-1.5 leading-tight">
          <span>BÉ NA SCIENCE LAB</span>
          <span class="text-[9px] bg-cyan-500/20 text-cyan-300 border border-cyan-400/30 px-2 py-0.5 rounded-full font-black uppercase">Figma AI</span>
        </div>
        <div class="text-[11px] text-slate-400">Phòng Thí Nghiệm & Thám Hiểm Khoa Học Kỳ Thú</div>
      </div>
    </div>

    <!-- THANH MENU 3 KHUNG HÌNH CHÍNH FIGMA AI + LỊCH SỬ & QUẢN LÝ -->
    <nav class="template-nav-links flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
      <a href="javascript:void(0)" onclick="navigateToTab('home')" id="nav-item-home" class="template-nav-item active px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
        <i data-lucide="flask-conical" style="width:14px; height:14px;"></i>
        <span>1. Topics · Lab</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('quiz')" id="nav-item-quiz" class="template-nav-item px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
        <i data-lucide="rocket" style="width:14px; height:14px;"></i>
        <span>2. Quiz · Space</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('leaderboard')" id="nav-item-leaderboard" class="template-nav-item px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
        <i data-lucide="trophy" style="width:14px; height:14px;"></i>
        <span>3. Stars · Bảng Sao 🌟</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('history')" id="nav-item-history" class="template-nav-item px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
        <i data-lucide="clock" style="width:14px; height:14px;"></i>
        <span>Lịch Sử</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateToTab('user-mgmt')" id="nav-item-user-mgmt" class="template-nav-item px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
        <i data-lucide="shield" style="width:14px; height:14px;"></i>
        <span>Quản Lý</span>
      </a>
    </nav>

    <!-- KHỐI PHẢI: NGÔN NGỮ VI/EN, NHẠC NỀN & BẠN ĐỒNG HÀNH -->
    <div class="template-header-circles flex items-center gap-2">
      <!-- VI / EN SWITCHER (FIGMA AI STYLE) -->
      <div class="flex items-center bg-slate-950 p-0.5 rounded-xl border border-slate-700 text-xs shadow-inner">
        <button type="button" onclick="toggleLang('vi')" id="lang-btn-vi" class="px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1">
          <span>🇻🇳</span> <span>VI</span>
        </button>
        <button type="button" onclick="toggleLang('en')" id="lang-btn-en" class="px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1">
          <span>🇬🇧</span> <span>EN</span>
        </button>
      </div>

      <!-- BẬT/TẮT NHẠC NỀN -->
      <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-200 transition" id="music-btn" onclick="toggleMusic()" title="Bật/Tắt nhạc">
        <i data-lucide="volume-x" style="width:14px; height:14px;"></i>
        <span>Nhạc</span>
      </button>

      <!-- BẠN ĐỒNG HÀNH & PROFILE -->
      <div id="header-mascot-pill" onclick="openMascotPickerModal()" class="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 px-2.5 py-1 rounded-xl cursor-pointer transition select-none" title="Bạn đồng hành của bé • Bấm để chọn bạn khác">
        <span id="header-mascot-avatar" class="text-base">🦉</span>
        <div class="flex flex-col text-left">
          <div class="font-baloo font-bold text-xs text-white leading-tight flex items-center gap-1">
            <span id="header-mascot-name" style="max-width:80px; text-overflow:ellipsis; overflow:hidden; white-space:nowrap;">Bé Na</span>
            <span class="text-[9px] bg-cyan-500/20 text-cyan-300 font-extrabold px-1.5 py-0.2 rounded-full">Lv.3</span>
          </div>
        </div>
      </div>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->
      <div id="header-auth-container">
        <button type="button" class="w-8 h-8 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white flex items-center justify-center transition" onclick="openAuthModal()" title="Đăng nhập tài khoản">
          <i data-lucide="user" style="width:15px; height:15px;"></i>
        </button>
      </div>
    </div>
  </header>"""

content = re.sub(r'<header class=\"app-header\">.*?</header>', new_header, content, count=1, flags=re.DOTALL)

# =========================================================================
# 2. UPGRADE HOME SCREEN TO FIGMA AI FRAME 1: TOPICS · SCIENCE LAB
# =========================================================================
new_home_screen = """<div class="quiz-card screen animate-screen-in" id="home-screen" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:28px; padding:20px;">
    
    <!-- 1. SCIENCE LAB HERO BANNER (CHUẨN FIGMA AI SCREEN 1) -->
    <div class="bg-gradient-to-br from-cyan-500 via-blue-600 to-indigo-700 text-white rounded-3xl p-5 md:p-6 relative overflow-hidden shadow-xl mb-5">
      <div class="relative z-10 max-w-xl">
        <span class="inline-block bg-white/20 backdrop-blur text-white text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-wider mb-2.5 shadow-sm">
          🔬 PHÒNG THÍ NGHIỆM KHOA HỌC
        </span>
        <h2 class="font-baloo text-2xl md:text-3xl font-bold leading-tight drop-shadow-sm">
          Sẵn Sàng Thám Hiểm<br>Khoa Học Kỳ Thú! ⚡
        </h2>
        <p class="text-xs md:text-sm text-cyan-100 mt-1.5 mb-4 font-medium leading-relaxed">
          Hoàn thành các phòng Lab để thu thập đủ 1.000 ngôi sao kiến thức và chinh phục đỉnh cao khoa học!
        </p>

        <div class="flex items-center gap-3 flex-wrap">
          <button type="button" onclick="startQuiz()" class="btn-3d btn-3d-amber px-6 py-2.5 text-xs font-black inline-flex items-center gap-2 shadow-lg">
            <i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i>
            <span>VÀO PHÒNG THI NGAY 🚀</span>
          </button>
          <button type="button" onclick="navigateToTab('leaderboard')" class="btn-3d px-4 py-2.5 text-xs font-black bg-white/20 hover:bg-white/30 text-white rounded-full border border-white/30 backdrop-blur transition inline-flex items-center gap-1.5">
            <i data-lucide="trophy" style="width:14px; height:14px;"></i>
            <span>Xem Bảng Sao 🌟</span>
          </button>
        </div>
      </div>

      <!-- Floating Lab Illustration -->
      <div class="absolute -right-2 -bottom-3 text-7xl md:text-8xl select-none opacity-85 drop-shadow animate-float-lab pointer-events-none">
        🧪
      </div>
    </div>

    <!-- 2. BẠN ĐỒNG HÀNH & HỒ SƠ NHANH CỦA BÉ -->
    <div class="home-hero-card mb-5 bg-white border-2 border-slate-100 rounded-2xl p-4 shadow-sm flex items-center justify-between flex-wrap gap-4">
      <div class="home-mascot-card flex items-center gap-3 cursor-pointer select-none" onclick="openMascotPickerModal()" title="Bấm để chọn Bạn đồng hành khoa học yêu thích!">
        <div class="w-12 h-12 rounded-2xl bg-cyan-50 border-2 border-cyan-200 flex items-center justify-center text-3xl shadow-inner animate-mascot-float" id="home-mascot-svg-wrap">🦉</div>
        <div class="home-mascot-info">
          <div class="flex items-center gap-2">
            <span class="font-baloo font-bold text-sm text-slate-900" id="home-mascot-name">Giáo Sư Cú Vọ</span>
            <span class="text-[10px] bg-cyan-100 text-cyan-800 font-extrabold px-2 py-0.5 rounded-full">Đổi bạn ▾</span>
          </div>
          <div class="text-[11px] text-cyan-600 font-bold" id="home-mascot-title">Bác Học Thông Thái</div>
          <div class="text-xs text-slate-500 italic mt-0.5" id="home-mascot-speech">"Chào bạn! Cùng tớ chinh phục đỉnh cao khoa học hôm nay nhé! 🚀"</div>
        </div>
      </div>

      <div class="home-profile-quick flex items-center gap-3 flex-wrap">
        <div class="flex items-center gap-1.5 bg-slate-50 border border-slate-200 px-3 py-1.5 rounded-xl">
          <label class="text-xs font-bold text-slate-600">👤 Tên bé:</label>
          <input type="text" id="user-name" placeholder="Bé Yêu" value="Bé Yêu" style="width:95px; background:transparent; font-weight:700; font-size:12px; outline:none; border:none;">
        </div>
        <div class="flex items-center gap-1.5 bg-slate-50 border border-slate-200 px-3 py-1.5 rounded-xl">
          <label class="text-xs font-bold text-slate-600">🏫 Lớp:</label>
          <select id="student-class" onchange="onClassGradeChange()" style="background:transparent; font-weight:700; font-size:12px; outline:none; border:none; cursor:pointer;">
            <option value="all">🌟 Tất cả (Lớp 1-5)</option>
            <option value="1">🎒 Lớp 1 (6t)</option>
            <option value="2" selected>🌱 Lớp 2 (7t)</option>
            <option value="3">🌿 Lớp 3 (8t)</option>
            <option value="4">🔬 Lớp 4 (9t)</option>
            <option value="5">🚀 Lớp 5 (10t)</option>
            <option value="6">🏆 Lớp 6 (Nâng cao)</option>
          </select>
        </div>
        <div class="flex items-center gap-1.5 bg-slate-50 border border-slate-200 px-3 py-1.5 rounded-xl">
          <label class="text-xs font-bold text-slate-600">🌐 Ngôn ngữ:</label>
          <select id="language-mode-select" onchange="onLanguageModeChange()" style="background:transparent; font-weight:700; font-size:12px; outline:none; border:none; cursor:pointer;">
            <option value="vi" selected>🇻🇳 Tiếng Việt</option>
            <option value="bilingual">🌐 Song ngữ Anh-Việt</option>
            <option value="en">🇬🇧 Tiếng Anh</option>
          </select>
        </div>
      </div>
    </div>

    <!-- 3. LAB FILTER PILLS (FIGMA AI SCREEN 1) -->
    <div class="mb-4">
      <div class="flex items-center justify-between mb-2">
        <h3 class="font-baloo font-bold text-base text-slate-900 flex items-center gap-2">
          <span>🔬</span>
          <span>Chọn Phòng Thí Nghiệm & Bắt Đầu</span>
        </h3>
        <span class="text-xs font-bold text-cyan-600">6 Labs Đã Sẵn Sàng</span>
      </div>
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1">
        <button type="button" onclick="filterLabPills('all', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-black bg-cyan-600 text-white shadow-sm shrink-0 cursor-pointer transition">Tất Cả Labs</button>
        <button type="button" onclick="filterLabPills('Động Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🦁 Động Vật</button>
        <button type="button" onclick="filterLabPills('Vũ Trụ & Thời Tiết', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🚀 Vũ Trụ</button>
        <button type="button" onclick="filterLabPills('Thực Vật', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🌿 Thực Vật</button>
        <button type="button" onclick="filterLabPills('Cơ Thể Người', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🫀 Sức Khỏe</button>
        <button type="button" onclick="filterLabPills('Địa Lý Việt Nam', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">🗺️ Địa Lý</button>
        <button type="button" onclick="filterLabPills('Vật Chất & Hiện Tượng', this)" class="lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition">⚡ Vật Chất</button>
      </div>
    </div>

    <!-- 4. 6 TOPIC LAB CARDS (FIGMA AI SCREEN 1 CARDS) -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5 mb-6" id="figma-topic-cards-container">
      
      <!-- Lab 1: Động Vật -->
      <div onclick="startTopicLab('Động Vật')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="Động Vật" title="Bấm để vào thi Lab Động Vật ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-amber-100 border border-amber-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            🦁
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Thế Giới Động Vật</div>
            <div class="text-[11px] text-slate-500 font-medium">Động vật hoang dã, côn trùng, tập tính</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">180 Câu</span>
              <span class="text-[10px] font-extrabold text-cyan-600">● Sẵn sàng thi</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-cyan-600 text-white flex items-center justify-center shrink-0 shadow-sm hover:scale-105 transition">
          <i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i>
        </div>
      </div>

      <!-- Lab 2: Vũ Trụ -->
      <div onclick="startTopicLab('Vũ Trụ & Thời Tiết')" class="topic-lab-card p-3.5 flex items-center justify-between border-cyan-400 bg-cyan-50/20" data-topic="Vũ Trụ & Thời Tiết" title="Bấm để vào thi Lab Vũ Trụ ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-indigo-100 border border-indigo-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            🚀
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Vũ Trụ & Thời Tiết</div>
            <div class="text-[11px] text-slate-500 font-medium">Hệ Mặt Trời, sao Hỏa, các hành tinh</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-indigo-100 text-indigo-800 px-2 py-0.5 rounded-full">180 Câu</span>
              <span class="text-[10px] font-extrabold text-cyan-600">● Sẵn sàng thi</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-indigo-600 text-white flex items-center justify-center shrink-0 shadow-sm hover:scale-105 transition">
          <i data-lucide="play" style="width:14px; height:14px; fill:currentColor;"></i>
        </div>
      </div>

      <!-- Lab 3: Thực Vật -->
      <div onclick="startTopicLab('Thực Vật')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="Thực Vật" title="Bấm để vào thi Lab Thực Vật ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-100 border border-emerald-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            🌿
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Thực Vật & Tự Nhiên</div>
            <div class="text-[11px] text-slate-500 font-medium">Quang hợp, hạt mầm, rừng xanh</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">120 Câu</span>
              <span class="text-[10px] font-extrabold text-emerald-600">✓ Đã mở</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center shrink-0 hover:scale-105 transition">
          <i data-lucide="arrow-right" style="width:15px; height:15px;"></i>
        </div>
      </div>

      <!-- Lab 4: Cơ Thể Người -->
      <div onclick="startTopicLab('Cơ Thể Người')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="Cơ Thể Người" title="Bấm để vào thi Lab Cơ Thể Người ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-rose-100 border border-rose-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            🫀
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Cơ Thể Người & Y Sinh</div>
            <div class="text-[11px] text-slate-500 font-medium">5 giác quan, tuần hoàn máu & sức khỏe</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-rose-100 text-rose-800 px-2 py-0.5 rounded-full">140 Câu</span>
              <span class="text-[10px] font-extrabold text-emerald-600">✓ Đã mở</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center shrink-0 hover:scale-105 transition">
          <i data-lucide="arrow-right" style="width:15px; height:15px;"></i>
        </div>
      </div>

      <!-- Lab 5: Địa Lý VN -->
      <div onclick="startTopicLab('Địa Lý Việt Nam')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="Địa Lý Việt Nam" title="Bấm để vào thi Lab Địa Lý ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-teal-100 border border-teal-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            🗺️
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Địa Lý Non Sông VN</div>
            <div class="text-[11px] text-slate-500 font-medium">Sông Hồng, Trường Sơn, danh lam thắng cảnh</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-teal-100 text-teal-800 px-2 py-0.5 rounded-full">160 Câu</span>
              <span class="text-[10px] font-extrabold text-emerald-600">✓ Đã mở</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center shrink-0 hover:scale-105 transition">
          <i data-lucide="arrow-right" style="width:15px; height:15px;"></i>
        </div>
      </div>

      <!-- Lab 6: Vật Chất & Hiện Tượng -->
      <div onclick="startTopicLab('Vật Chất & Hiện Tượng')" class="topic-lab-card p-3.5 flex items-center justify-between" data-topic="Vật Chất & Hiện Tượng" title="Bấm để vào thi Lab Vật Chất ngay">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-2xl bg-purple-100 border border-purple-200 flex items-center justify-center text-2xl shadow-inner shrink-0">
            ⚡
          </div>
          <div>
            <div class="font-baloo font-bold text-sm text-slate-900 leading-snug">Vật Chất & Hiện Tượng</div>
            <div class="text-[11px] text-slate-500 font-medium">Âm thanh, ánh sáng, nam châm & chuyển động</div>
            <div class="flex items-center gap-2 mt-1">
              <span class="text-[10px] font-extrabold bg-purple-100 text-purple-800 px-2 py-0.5 rounded-full">150 Câu</span>
              <span class="text-[10px] font-extrabold text-emerald-600">✓ Đã mở</span>
            </div>
          </div>
        </div>
        <div class="w-9 h-9 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center shrink-0 hover:scale-105 transition">
          <i data-lucide="arrow-right" style="width:15px; height:15px;"></i>
        </div>
      </div>

    </div>

    <!-- 5. TÙY CHỌN NÂNG CAO (QUY CÁCH ĐỀ THI & GOOGLE SHEETS) -->
    <details class="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm mb-5" id="home-config-details">
      <summary class="font-baloo font-bold text-sm text-slate-800 cursor-pointer flex items-center justify-between select-none">
        <span class="flex items-center gap-2">
          <span>⚙️</span>
          <span>Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>
        </span>
        <span class="text-xs text-cyan-600 font-bold">Mở rộng ▾</span>
      </summary>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 pt-3 border-t border-slate-100">
        <!-- Cột 1: Cấu hình câu hỏi -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">🔢 Số lượng câu hỏi:</label>
            <select id="quiz-size" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
              <option value="5">5 câu (Khởi động)</option>
              <option value="10">10 câu (Nhanh)</option>
              <option value="15" selected>15 câu (Chuẩn thi)</option>
              <option value="20">20 câu (Thử thách)</option>
              <option value="25">25 câu (Nâng cao)</option>
              <option value="30">30 câu (Mô phỏng thi)</option>
              <option value="50">50 câu (Đại hội tri thức)</option>
              <option value="all">Toàn bộ câu có</option>
            </select>
          </div>

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">📚 Nguồn đề thi:</label>
            <select id="target-source-select" onchange="onTargetSourceDropdownChange()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs max-w-[200px]">
              <option value="all" selected>🌟 Tất cả nguồn (Đa dạng 500 câu)</option>
              <option value="Trạng Nguyên & Violympic">🏆 Trạng Nguyên & Violympic</option>
              <option value="SGK Việt Nam (GDPT 2018)">📗 SGK Việt Nam (GDPT 2018)</option>
              <option value="Kangaroo Khoa học (IKSC)">🦘 Kangaroo Khoa học (IKSC)</option>
              <option value="IXL & Khan Academy">🌐 IXL & Khan Academy</option>
              <option value="National Geographic Kids">🦁 National Geographic Kids</option>
              <option value="Khác">🧩 Khác (Mở rộng)</option>
            </select>
          </div>

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">🧠 Chế độ lặp lại:</label>
            <select id="review-ratio" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
              <option value="random" selected>🎲 Ngẫu nhiên chuẩn</option>
              <option value="mistakes">🔄 Ưu tiên câu từng làm sai</option>
              <option value="unseen">🆕 Chỉ câu chưa từng làm</option>
              <option value="reviewed">🔁 Củng cố trí nhớ</option>
            </select>
          </div>

          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5">🎚️ Độ khó câu hỏi:</label>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectDiff('all', this)">🌟 Hỗn hợp</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('1', this)">⭐ Dễ</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('2', this)">⭐⭐ Vừa</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('3', this)">⭐⭐⭐ Khó</button>
            </div>
          </div>
        </div>

        <!-- Cột 2: Độ tuổi & Kết nối Google Sheets -->
        <div class="flex flex-col gap-3">
          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5">👶 Phù hợp lứa tuổi:</label>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectAge('all', this)">🌟 Tất cả</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('6-7', this)">🌱 6 - 7 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('7-8', this)">🌿 7 - 8 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('8-9', this)">🚀 8 - 9 tuổi</button>
            </div>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl mt-1">
            <div class="flex items-center justify-between mb-1.5">
              <span class="text-xs font-bold text-slate-800 flex items-center gap-1">
                <span>🔗</span> Kết nối Google Sheets Tự Động
              </span>
              <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="text-[11px] font-bold text-cyan-600 hover:underline">Mở File ↗</a>
            </div>
            <div class="flex items-center gap-1.5">
              <input type="text" id="apps-script-url" placeholder="Dán Web App URL Google Apps Script..." class="flex-1 text-xs px-2.5 py-1.5 rounded-lg border border-slate-300" oninput="localStorage.setItem('science_quiz_script_url', this.value.trim())">
              <button type="button" onclick="saveScriptUrlAndSyncFromHome()" class="btn-3d btn-3d-cyan px-3 py-1.5 text-xs font-bold shrink-0">
                Lưu & Đồng Bộ
              </button>
            </div>
          </div>
        </div>
      </div>
    </details>

    <!-- 6. KHỐI ACTION BAR DƯỚI CÙNG -->
    <div class="home-action-bar flex items-center justify-between gap-4 flex-wrap bg-white p-4 border border-slate-200 rounded-2xl shadow-sm">
      <div class="pool-status-banner flex items-center gap-2 text-xs font-bold text-slate-600" id="pool-count-banner">
        <span class="text-base">💡</span>
        <span id="pool-count-text">Đang có 100 câu hỏi sẵn sàng cho lượt thi này.</span>
      </div>
      <button type="button" class="btn-3d btn-3d-cyan px-8 py-3 text-sm font-black flex items-center gap-2 shadow-lg" onclick="startQuiz()">
        <i data-lucide="rocket" style="width:18px; height:18px;"></i>
        <span>BẮT ĐẦU THÁM HIỂM KHOA HỌC</span>
      </button>
    </div>

  </div>"""

content = re.sub(r'<div class=\"quiz-card screen\" id=\"home-screen\">.*?(?=<div class=\"quiz-card screen\" id=\"quiz-screen\">)', new_home_screen + "\n\n  ", content, count=1, flags=re.DOTALL)

# =========================================================================
# 3. UPGRADE QUIZ SCREEN TO FIGMA AI FRAME 2: QUIZ · SPACE EXPLORER
# =========================================================================
new_quiz_screen = """<div class="quiz-card screen animate-screen-in" id="quiz-screen" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:28px; padding:20px;">
    
    <!-- TOP MISSION HEADER (CHẾ ĐỘ THÁM HIỂM VŨ TRỤ) -->
    <div class="flex items-center justify-between gap-3 mb-4 shrink-0 flex-wrap">
      
      <div class="flex items-center gap-2">
        <button type="button" onclick="askQuitQuiz()" class="w-9 h-9 rounded-full bg-white border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 shadow-sm transition" title="Quay lại Phòng Lab">
          <i data-lucide="x" style="width:18px; height:18px; stroke-width:3;"></i>
        </button>
        <button type="button" onclick="pauseQuiz()" class="px-3 py-1.5 rounded-full bg-white border border-slate-200 text-xs font-bold text-slate-600 hover:bg-slate-100 shadow-sm transition flex items-center gap-1">
          <i data-lucide="pause" style="width:14px; height:14px;"></i>
          <span>Tạm dừng</span>
        </button>
      </div>

      <!-- ROCKET PROGRESS BAR -->
      <div class="flex-1 min-w-[180px] max-w-md flex items-center gap-2.5">
        <div class="flex-1 bg-slate-200 h-3.5 rounded-full overflow-hidden p-0.5 border border-slate-300">
          <div class="progress-fill bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-600 h-full rounded-full transition-all duration-300" id="progress-fill" style="width: 10%;"></div>
        </div>
        <span class="text-xs font-black text-slate-700 font-baloo whitespace-nowrap animate-pulse-rocket" id="question-number">Câu 1/15 🚀</span>
      </div>

      <!-- COUNTDOWN TIMER PILL -->
      <div class="bg-white border-2 border-indigo-200 px-3.5 py-1 rounded-full text-xs font-black text-indigo-900 flex items-center gap-1.5 shadow-sm" id="quiz-timer">
        <i data-lucide="clock" style="width:14px; height:14px; stroke-width:2.5;"></i>
        <span id="timer-text">00:00</span>
      </div>

    </div>

    <!-- MISSION BADGE ROW & XP -->
    <div class="flex items-center justify-between px-1 mb-3">
      <div class="flex items-center gap-2 flex-wrap">
        <span class="text-[11px] font-black bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full border border-indigo-200 flex items-center gap-1.5" id="badge-topic-age">
          <span>🚀</span> <span>Vũ Trụ & Thời Tiết</span>
        </span>
        <span class="text-[11px] font-bold bg-slate-100 text-slate-700 px-2.5 py-0.5 rounded-full border border-slate-200" id="badge-source">
          📗 SGK Việt Nam
        </span>
      </div>
      <span class="text-xs font-extrabold text-amber-600 flex items-center gap-1 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200">
        <span>⭐</span> +20 XP
      </span>
    </div>

    <!-- DEEP COSMIC QUESTION CARD (FIGMA AI SCREEN 2 QUESTION CARD) -->
    <div class="bg-gradient-to-b from-indigo-950 to-slate-900 text-white rounded-3xl p-5 md:p-6 border-2 border-indigo-800/60 shadow-xl relative overflow-hidden mb-4">
      <div class="relative z-10 flex flex-col gap-2.5">
        <span class="text-[10px] font-black tracking-widest text-cyan-400 uppercase">THÁM HIỂM KHOA HỌC • CÂU HỎI TRẮC NGHIỆM</span>
        <h2 class="font-baloo text-lg md:text-xl font-bold leading-snug text-white" id="question-text">
          Đang tải nội dung câu hỏi...
        </h2>
        <div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm" id="q-img-wrap" style="display:none;">
          <img id="question-img" src="" alt="Minh họa" style="width:100%; max-height:220px; object-fit:contain; display:block; margin:0 auto;">
        </div>
      </div>
      
      <!-- Watermark Saturn Icon -->
      <div class="absolute -right-4 -bottom-4 text-7xl opacity-20 pointer-events-none select-none">
        🪐
      </div>
    </div>

    <!-- 4 TACTILE 3D OPTION CARDS (A, B, C, D) -->
    <div class="flex flex-col gap-2.5 mb-4" id="choices-list">
      <!-- Render động qua renderMultipleChoice(q) -->
    </div>

    <!-- TỰ LUẬN (SA BOX) -->
    <div class="sa-box bg-white p-4 rounded-2xl border-2 border-slate-200 mb-4" id="sa-box" style="display:none;">
      <input type="text" class="sa-input w-full p-3 rounded-xl border border-slate-300 font-bold text-sm mb-2" id="sa-input-field" placeholder="Gõ câu trả lời của bé vào đây..." autocomplete="off">
      <button type="button" class="btn-3d btn-3d-cyan px-4 py-2 text-xs font-bold" onclick="submitShortAnswer()">Kiểm tra đáp án</button>
    </div>

    <!-- MASCOT COMPANION LIVE DIALOGUE -->
    <div class="flex items-center gap-3 bg-white border border-slate-200 rounded-2xl p-3 mb-4 shadow-sm cursor-pointer select-none" onclick="onMascotClick()" title="Bấm vào tớ để nghe bạn đồng hành cổ vũ!">
      <div id="quiz-mascot-svg-wrap" class="w-10 h-10 rounded-xl bg-cyan-50 flex items-center justify-center text-2xl shrink-0 animate-mascot-float">🦉</div>
      <div class="text-xs text-slate-700 font-bold flex-1" id="mascot-speech">Bé đọc kỹ câu hỏi nhé, chúng mình cùng nhau đạt điểm 10 nào! 🌟</div>
    </div>

    <!-- GIẢI THÍCH KHOA HỌC (💡 SỰ THẬT KHOA HỌC) -->
    <div class="explanation-card bg-amber-50/90 border-2 border-amber-300 rounded-2xl p-4 mb-4 text-xs font-medium text-amber-950 shadow-sm" id="explanation-card" style="display:none;"></div>

    <!-- BOTTOM ACTION BUTTON -->
    <div class="sticky bottom-2 z-20">
      <button type="button" class="btn-3d btn-3d-cyan w-full py-3.5 text-sm font-black flex items-center justify-center gap-2 shadow-xl" id="btn-next" onclick="goNextQuestion()">
        <span>TIẾP TỤC HÀNH TRÌNH</span>
        <i data-lucide="arrow-right" style="width:16px; height:16px;"></i>
      </button>
    </div>

  </div>"""

content = re.sub(r'<div class=\"quiz-card screen\" id=\"quiz-screen\">.*?(?=<div class=\"quiz-card screen\" id=\"result-screen\">)', new_quiz_screen + "\n\n  ", content, count=1, flags=re.DOTALL)

# =========================================================================
# 4. UPGRADE LEADERBOARD MODAL TO FIGMA AI FRAME 3: LEADERBOARD · WEEKLY STARS
# =========================================================================
new_leaderboard_modal = """<div class="modal-overlay" id="modal-leaderboard">
  <div class="modal-box w-full max-w-xl max-h-[90vh] bg-[#F8FAFC] rounded-3xl p-5 shadow-2xl flex flex-col border-4 border-slate-800 text-left relative overflow-hidden">
    
    <!-- Top Modal Header -->
    <div class="flex items-center justify-between pb-3 border-b border-slate-200 shrink-0">
      <div>
        <div class="font-baloo font-bold text-lg md:text-xl text-slate-900 flex items-center gap-2 leading-tight">
          <span>Bảng Sao Tuần Này</span>
          <span class="text-amber-500 animate-bounce">🌟</span>
        </div>
        <div class="text-xs text-slate-500 font-medium">Top nhà thám hiểm nhí xuất sắc nhất tuần</div>
      </div>
      <button type="button" onclick="closeLeaderboardModal()" class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 hover:bg-slate-300 font-black flex items-center justify-center transition">✕</button>
    </div>

    <!-- Filter & Fireworks Quick Bar -->
    <div class="flex items-center justify-between py-2.5 gap-2 flex-wrap shrink-0">
      <div class="flex items-center gap-2">
        <span class="text-xs font-bold text-slate-600">Lọc:</span>
        <select id="lead-filter-class" onchange="filterLeaderboardView()" class="px-2.5 py-1 bg-white border border-slate-300 rounded-xl text-xs font-bold text-slate-800 outline-none">
          <option value="all">🌟 Tất cả các lớp</option>
          <option value="Lớp 1">🎒 Lớp 1</option>
          <option value="Lớp 2">🌱 Lớp 2</option>
          <option value="Lớp 3">🌿 Lớp 3</option>
          <option value="Lớp 4">🔬 Lớp 4</option>
          <option value="Lớp 5">🚀 Lớp 5</option>
          <option value="Lớp 6">🏆 Lớp 6</option>
        </select>
      </div>

      <div class="flex items-center gap-2">
        <button type="button" class="btn-3d btn-3d-amber px-3 py-1.5 text-xs font-black inline-flex items-center gap-1.5 shadow" onclick="launchFireworks()" title="Bắn pháo hoa ăn mừng">
          <span>🎊 Bắn Pháo Hoa</span>
        </button>
        <button type="button" class="px-2.5 py-1.5 bg-white border border-slate-200 hover:bg-slate-100 rounded-xl text-xs font-bold text-slate-700 transition" onclick="fetchLeaderboardFromCloud()">
          🔄
        </button>
      </div>
    </div>

    <!-- SCROLLABLE LIST WITH PODIUM -->
    <div class="flex-1 overflow-y-auto no-scrollbar py-2" id="lead-players-list">
      <div class="text-center py-8 text-slate-500 text-xs">Đang tải danh sách bảng vàng...</div>
    </div>

    <!-- STICKY CURRENT USER POSITION CARD AT BOTTOM -->
    <div class="p-3 bg-gradient-to-r from-indigo-900 to-slate-900 text-white rounded-2xl flex items-center justify-between shadow-lg border border-indigo-700/50 mt-3 shrink-0">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-full bg-amber-400 text-slate-950 font-baloo font-black flex items-center justify-center text-xs shadow">
          #1
        </div>
        <div>
          <div class="text-[9px] text-indigo-300 uppercase font-black tracking-wider">VỊ TRÍ CỦA BẠN</div>
          <div class="text-xs font-black text-white" id="lead-current-user-name">Bé Na (Thanh Do Trung)</div>
        </div>
      </div>
      <div class="text-right">
        <div class="text-sm font-baloo font-black text-amber-300" id="lead-current-user-stars">2,450 ⭐</div>
        <div class="text-[9px] text-indigo-300 font-bold">Kỷ Lục Tuần Này</div>
      </div>
    </div>

    <!-- GRAND CELEBRATION BUTTON -->
    <button type="button" onclick="launchFireworks()" class="btn-3d btn-3d-amber w-full py-2.5 text-xs font-black mt-2 shrink-0 flex items-center justify-center gap-2">
      <span>BẮN PHÁO HOA ĂN MỪNG 🎊</span>
    </button>

  </div>
</div>"""

content = re.sub(r'<div class=\"modal-overlay\" id=\"modal-leaderboard\">.*?(?=<div class=\"modal-overlay\" id=\"modal-history-detail\">)', new_leaderboard_modal + "\n\n", content, count=1, flags=re.DOTALL)

# =========================================================================
# 5. ADD JAVASCRIPT HELPER FUNCTIONS: FIREWORKS, QUICK LAB START, LANG SWITCHER
# =========================================================================
js_helpers = """
// =========================================================================
// FIGMA AI ANIMATIONS & INTERACTIVE HELPERS
// =========================================================================

// Grand Multi-Burst Fireworks Confetti Celebration
function launchFireworks() {
  playSound('correct');
  try {
    const count = 180;
    const defaults = {
      origin: { y: 0.65 },
      colors: ['#06B6D4', '#F59E0B', '#8B5CF6', '#10B981', '#EC4899', '#FBBF24']
    };

    function fire(particleRatio, opts) {
      confetti(Object.assign({}, defaults, opts, {
        particleCount: Math.floor(count * particleRatio)
      }));
    }

    fire(0.25, { spread: 26, startVelocity: 55 });
    fire(0.2, { spread: 60 });
    fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
    fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
    fire(0.1, { spread: 120, startVelocity: 45 });

    // Side celebratory cannons
    setTimeout(() => {
      confetti({ particleCount: 60, angle: 60, spread: 60, origin: { x: 0.05, y: 0.65 }, colors: defaults.colors });
      confetti({ particleCount: 60, angle: 120, spread: 60, origin: { x: 0.95, y: 0.65 }, colors: defaults.colors });
    }, 220);

    // Golden stars shower
    setTimeout(() => {
      confetti({
        particleCount: 40,
        spread: 100,
        origin: { y: 0.4 },
        shapes: ['star'],
        colors: ['#F59E0B', '#FBBF24', '#FDE047']
      });
    }, 450);
  } catch(e) {}
}

// Quick Start Topic Lab from Figma AI Card
function startTopicLab(topicName) {
  selectedTopic = topicName;
  saveSettings();
  showScreen('home-screen');
  startQuiz();
}

// Filter Topic Lab Pills on Home Screen
function filterLabPills(topicId, btnElem) {
  document.querySelectorAll('.lab-filter-pill').forEach(b => {
    b.className = 'lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-bold bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 shrink-0 cursor-pointer transition';
  });
  if (btnElem) {
    btnElem.className = 'lab-filter-pill px-3.5 py-1.5 rounded-full text-xs font-black bg-cyan-600 text-white shadow-sm shrink-0 cursor-pointer transition';
  }
  selectedTopic = topicId;
  document.querySelectorAll('.topic-lab-card').forEach(card => {
    const cardTopic = card.getAttribute('data-topic');
    if (topicId === 'all' || cardTopic === topicId || (cardTopic && cardTopic.includes(topicId))) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
  updatePoolCountDisplay();
}

// 1-Click VI / EN Language Switcher
function toggleLang(lang) {
  const select = document.getElementById('language-mode-select');
  if (select) {
    select.value = lang;
    onLanguageModeChange();
  }
  const btnVi = document.getElementById('lang-btn-vi');
  const btnEn = document.getElementById('lang-btn-en');
  if (btnVi && btnEn) {
    if (lang === 'vi') {
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    } else {
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    }
  }
  playSound('click');
}
"""

if "// FIGMA AI ANIMATIONS & INTERACTIVE HELPERS" not in content:
    content = content.replace("function openLeaderboardModal() {", js_helpers + "\nfunction openLeaderboardModal() {")

# Ensure openLeaderboardModal auto-triggers fireworks
content = re.sub(
    r'function openLeaderboardModal\(\)\s*\{[^}]*\}',
    """function openLeaderboardModal() {
  const modal = document.getElementById('modal-leaderboard');
  if (modal) modal.classList.add('active');
  setActiveNavTab('leaderboard');
  fetchLeaderboardFromCloud();
  setTimeout(launchFireworks, 250);
}""",
    content,
    count=1
)

# Ensure submitAndFinishQuiz calls launchFireworks
content = content.replace("fireConfetti();", "launchFireworks();")

# Ensure renderLeaderboardList renders the grand 3D podium and sticky current user card
podium_render_replacement = """function renderLeaderboardList(players) {
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
      <div class="podium-container flex items-end justify-center gap-2.5 mb-5 pt-3 select-none">
        
        <!-- HẠNG 2: BẠC -->
        <div class="flex flex-col items-center w-24">
          <div class="w-12 h-12 rounded-full border-2 border-slate-300 bg-slate-100 flex items-center justify-center text-xl mb-1 shadow-sm">
            🥈
          </div>
          <div class="font-baloo font-bold text-xs text-slate-900 truncate max-w-[85px] text-center">
            ${p2.name}
          </div>
          <div class="text-[11px] font-extrabold text-cyan-600 mb-1">
            ${p2.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-2nd w-full h-16 flex flex-col items-center justify-center text-white font-baloo font-black shadow-md">
            <span class="text-base">2</span>
            <span class="text-[9px] opacity-90">Á QUÂN</span>
          </div>
        </div>

        <!-- HẠNG 1: VÀNG (QUÁN QUÂN) -->
        <div class="flex flex-col items-center w-28 -mt-4 cursor-pointer" onclick="launchFireworks()" title="Bấm vào Quán quân để bắn pháo hoa ăn mừng!">
          <div class="relative">
            <span class="absolute -top-3.5 left-1/2 -translate-x-1/2 text-base animate-bounce">👑</span>
            <div class="w-14 h-14 rounded-full border-3 border-amber-400 bg-amber-100 flex items-center justify-center text-2xl mb-1 shadow-lg ring-4 ring-amber-300/40">
              🥇
            </div>
          </div>
          <div class="font-baloo font-bold text-sm text-slate-900 truncate max-w-[95px] text-center">
            ${p1.name}
          </div>
          <div class="text-xs font-black text-amber-600 mb-1">
            ${p1.highestScore || 0}/10 🌟
          </div>
          <div class="podium-1st w-full h-24 flex flex-col items-center justify-center text-slate-950 font-baloo font-black shadow-xl">
            <span class="text-xl">1</span>
            <span class="text-[10px] tracking-wider font-extrabold">QUÁN QUÂN</span>
          </div>
        </div>

        <!-- HẠNG 3: ĐỒNG -->
        <div class="flex flex-col items-center w-24">
          <div class="w-12 h-12 rounded-full border-2 border-orange-300 bg-orange-100 flex items-center justify-center text-xl mb-1 shadow-sm">
            🥉
          </div>
          <div class="font-baloo font-bold text-xs text-slate-900 truncate max-w-[85px] text-center">
            ${p3.name}
          </div>
          <div class="text-[11px] font-extrabold text-orange-600 mb-1">
            ${p3.highestScore || 0}/10 ⭐
          </div>
          <div class="podium-3rd w-full h-12 flex flex-col items-center justify-center text-white font-baloo font-black shadow-md">
            <span class="text-sm">3</span>
            <span class="text-[9px] opacity-90">QUÝ QUÂN</span>
          </div>
        </div>

      </div>
    `;
  }

  // DANH SÁCH TỪ HẠNG 4 TRỞ ĐI
  html += '<div class="flex flex-col gap-2">';
  players.slice(3).forEach((p, idx) => {
    const rank = idx + 4;
    const mascotEmoji = p.mascot || '🦉';
    html += `
      <div class="flex items-center justify-between p-2.5 rounded-2xl bg-white border border-slate-100 shadow-2xs hover:bg-slate-50 transition">
        <div class="flex items-center gap-3">
          <span class="w-6 text-center font-baloo font-black text-slate-400 text-xs">${rank}</span>
          <span class="text-lg">${mascotEmoji}</span>
          <div>
            <div class="text-xs font-bold text-slate-800">${p.name}</div>
            <div class="text-[10px] text-slate-400 font-medium">${p.className || 'Học sinh'} • ${p.school || 'Khoa học nhí'}</div>
          </div>
        </div>
        <span class="text-xs font-black text-slate-700 bg-slate-50 border border-slate-200 px-2.5 py-1 rounded-full shadow-2xs">${p.highestScore || 0}/10 ⭐</span>
      </div>
    `;
  });
  html += '</div>';

  listElem.innerHTML = html;
}"""

content = re.sub(r'function renderLeaderboardList\(players\)\s*\{.*?\n\}', podium_render_replacement, content, count=1, flags=re.DOTALL)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Step 2-5: Full Figma AI Template upgrade applied successfully.")
