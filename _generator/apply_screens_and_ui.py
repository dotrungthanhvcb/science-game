# -*- coding: utf-8 -*-
"""
Script triển khai 5 yêu cầu nâng cấp:
1. Loại bỏ thông báo đúng/sai và mascot khen sớm ở từng câu hỏi
2. Bổ sung 4 option nhạc nền tập trung khi học/làm việc (Lofi Chill, Piano cổ điển, Sóng não Alpha, Upbeat Game Show)
3. Thêm màn hình Welcome hoành tráng, bấm 'Bắt đầu' mới vào Home
4. Sửa thang nhận xét kết quả chuẩn xác theo điểm số (9-10 xuất sắc, 8-9 rất tốt, 6.5-7.9 khá, 5-6.4 trung bình cần cố gắng, <5 chưa đạt)
5. Tính năng xem Lịch sử làm bài - Bảng thống kê kèm Search, Filter, Dashboard
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# =========================================================================
# 1. CSS CHO WELCOME SCREEN, HISTORY SCREEN, MUSIC CONTROLLER, VÀ STATS
# =========================================================================
FEATURE_CSS = """
  /* =========================================================================
     WELCOME SCREEN & HERO STYLES
     ========================================================================= */
  .welcome-card {
    text-align: center;
    padding: 36px 20px;
    background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
    border-radius: 24px;
    border: 2px solid #E2E8F0;
    box-shadow: 0 12px 36px rgba(67, 97, 238, 0.08);
  }
  .welcome-mascot-box {
    margin: 0 auto 16px;
    width: 110px;
    height: 110px;
    background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 24px rgba(67, 97, 238, 0.15);
    border: 3px solid #C7D2FE;
    animation: floatMascot 3s ease-in-out infinite;
  }
  @keyframes floatMascot {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }
  .welcome-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #EEF2FF;
    color: var(--primary);
    border: 1.5px solid #C7D2FE;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 14px;
  }
  .welcome-title {
    font-size: 2.1rem;
    font-weight: 900;
    color: var(--dark);
    margin-bottom: 10px;
    line-height: 1.25;
  }
  .welcome-subtitle {
    font-size: 1.05rem;
    color: #475569;
    max-width: 620px;
    margin: 0 auto 26px;
    line-height: 1.55;
  }
  .welcome-highlights-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 14px;
    margin-bottom: 30px;
    text-align: left;
  }
  .welcome-highlight-card {
    background: white;
    border: 2px solid #E2E8F0;
    border-radius: 16px;
    padding: 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
  }
  .welcome-hl-icon {
    font-size: 1.8rem;
    line-height: 1;
  }
  .welcome-hl-title {
    font-weight: 800;
    font-size: 0.95rem;
    color: var(--dark);
    margin-bottom: 3px;
  }
  .welcome-hl-desc {
    font-size: 0.8rem;
    color: #64748B;
    line-height: 1.35;
  }
  .welcome-btn-row {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
  }
  .btn-welcome-start {
    background: linear-gradient(135deg, #4361EE 0%, #3A0CA3 100%);
    color: white;
    border: none;
    padding: 16px 36px;
    border-radius: 16px;
    font-size: 1.15rem;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(67, 97, 238, 0.35);
    transition: all 0.25s ease;
  }
  .btn-welcome-start:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 12px 30px rgba(67, 97, 238, 0.45);
  }
  .btn-welcome-history {
    background: white;
    color: var(--primary);
    border: 2px solid var(--primary);
    padding: 16px 26px;
    border-radius: 16px;
    font-size: 1.05rem;
    font-weight: 800;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .btn-welcome-history:hover {
    background: #EEF2FF;
    transform: translateY(-2px);
  }

  /* =========================================================================
     MUSIC CONTROLLER BAR
     ========================================================================= */
  .music-control-group {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.9);
    border: 1.5px solid #CBD5E1;
    border-radius: 12px;
    padding: 4px 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }
  .music-track-select {
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 5px 8px;
    font-size: 0.82rem;
    font-weight: 700;
    color: #334155;
    background: white;
    outline: none;
    cursor: pointer;
  }
  .btn-nav-history {
    background: #EEF2FF;
    color: var(--primary);
    border: 1.5px solid #C7D2FE;
    border-radius: 12px;
    padding: 7px 14px;
    font-size: 0.85rem;
    font-weight: 800;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }
  .btn-nav-history:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
    transform: translateY(-1px);
  }

  /* =========================================================================
     HISTORY SCREEN & DASHBOARD
     ========================================================================= */
  .history-container {
    padding: 4px;
  }
  .history-header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 12px;
  }
  .history-dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px;
    margin-bottom: 22px;
  }
  .history-stat-card {
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 14px;
    padding: 14px;
    text-align: center;
  }
  .history-stat-val {
    font-size: 1.6rem;
    font-weight: 900;
    color: var(--primary);
    line-height: 1.2;
  }
  .history-stat-lbl {
    font-size: 0.76rem;
    font-weight: 800;
    color: #64748B;
    text-transform: uppercase;
    margin-top: 4px;
  }
  .history-filter-bar {
    display: flex;
    gap: 10px;
    margin-bottom: 16px;
    flex-wrap: wrap;
    background: #F8FAFC;
    padding: 12px;
    border-radius: 14px;
    border: 1.5px solid #E2E8F0;
  }
  .history-search-input {
    flex: 2;
    min-width: 180px;
    padding: 8px 12px;
    border: 1.5px solid #CBD5E1;
    border-radius: 10px;
    font-size: 0.88rem;
    outline: none;
  }
  .history-search-input:focus {
    border-color: var(--primary);
  }
  .history-filter-select {
    flex: 1;
    min-width: 140px;
    padding: 8px 10px;
    border: 1.5px solid #CBD5E1;
    border-radius: 10px;
    font-size: 0.84rem;
    font-weight: 700;
    background: white;
    cursor: pointer;
  }
  .history-table-wrap {
    overflow-x: auto;
    border-radius: 14px;
    border: 1.5px solid #E2E8F0;
    background: white;
    max-height: 380px;
    overflow-y: auto;
  }
  .history-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
    text-align: left;
  }
  .history-table th {
    background: #EEF2FF;
    color: #3730A3;
    font-weight: 800;
    padding: 10px 12px;
    position: sticky;
    top: 0;
    z-index: 2;
  }
  .history-table td {
    padding: 10px 12px;
    border-bottom: 1px solid #F1F5F9;
  }
  .history-table tr:hover {
    background: #F8FAFC;
  }
  .score-badge {
    padding: 3px 8px;
    border-radius: 8px;
    font-weight: 800;
    font-size: 0.8rem;
    display: inline-block;
  }
  .score-badge.high { background: #DCFCE7; color: #15803D; }
  .score-badge.medium { background: #FEF3C7; color: #B45309; }
  .score-badge.low { background: #FEE2E2; color: #B91C1C; }
"""

if '.welcome-card' not in html:
    html = html.replace('</style>', FEATURE_CSS + '\n</style>')

# =========================================================================
# 2. CẬP NHẬT HEADER: THÊM BỘ CHỌN 4 BẢN NHẠC + NÚT LỊCH SỬ LÀM BÀI
# =========================================================================
OLD_HEADER = """  <header class="app-header">
    <div class="header-titles">
      <h1>🔬 Khoa Học Vui</h1>
      <p>Đấu trường 100 câu hỏi KHTN & Xã hội thi học bổng dành cho bé 7 tuổi</p>
    </div>
    <!-- NÚT BẬT NHẠC GAME SHOW SÔI ĐỘNG -->
    <button class="music-toggle-btn" id="music-btn" onclick="toggleMusic()">
      <span id="music-icon">🎵</span>
      <span id="music-text">Bật Nhạc Thi Đấu</span>
    </button>
  </header>"""

NEW_HEADER = """  <header class="app-header">
    <div class="header-titles" onclick="showScreen('welcome-screen')" style="cursor:pointer;" title="Về Màn hình Chào mừng">
      <h1>🔬 Đấu Trường Khoa Học Nhí</h1>
      <p>Ngân hàng 500+ câu hỏi chuẩn SGK, Trạng Nguyên & Kangaroo Khoa Học</p>
    </div>
    
    <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
      <!-- BỘ CHỌN 4 BẢN NHẠC NỀN TẬP TRUNG -->
      <div class="music-control-group">
        <select class="music-track-select" id="music-track-select" onchange="changeMusicTrack(this.value)">
          <option value="lofi" selected>🎧 1. Lofi Chill (60 BPM)</option>
          <option value="piano">🎹 2. Piano Mozart (Tập Trung)</option>
          <option value="baroque">🌊 3. Baroque Sóng Não Alpha</option>
          <option value="upbeat">⚡ 4. Game Show Hào Hứng</option>
        </select>
        <button class="music-toggle-btn" id="music-btn" onclick="toggleMusic()" style="margin:0; padding:6px 12px;">
          <span id="music-icon">🎵</span>
          <span id="music-text">Bật Nhạc</span>
        </button>
      </div>

      <!-- NÚT XEM LỊCH SỬ LÀM BÀI -->
      <button class="btn-nav-history" onclick="openHistoryScreen()">
        <span>📊</span>
        <span>Lịch Sử Bài Thi</span>
      </button>
    </div>
  </header>"""

if OLD_HEADER in html:
    html = html.replace(OLD_HEADER, NEW_HEADER)

# =========================================================================
# 3. THÊM MÀN HÌNH WELCOME SCREEN (TRƯỚC HOME-SCREEN)
# =========================================================================
WELCOME_SCREEN_HTML = """  <!-- =====================================================================
       0. WELCOME SCREEN (MÀN HÌNH CHÀO MỪNG - BẤM BẮT ĐẦU MỚI VÀO HOME)
       ===================================================================== -->
  <div class="quiz-card screen active" id="welcome-screen">
    <div class="welcome-card">
      <div class="welcome-mascot-box">
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
      </div>

      <div class="welcome-badge-pill">🌟 ĐẤU TRƯỜNG KHOA HỌC TIỂU HỌC 2026</div>
      <h1 class="welcome-title">🔬 Chào Mừng Bé Đến Với Đấu Trường Khoa Học!</h1>
      <p class="welcome-subtitle">
        Khám phá thế giới tự nhiên kỳ thú, rèn luyện phản xạ và tư duy logic.<br>
        Bám sát đề thi <strong>Trạng Nguyên, Kangaroo Khoa học (IKSC), IXL & SGK Việt Nam</strong>.
      </p>

      <div class="welcome-highlights-grid">
        <div class="welcome-highlight-card">
          <div class="welcome-hl-icon">📗</div>
          <div>
            <div class="welcome-hl-title">500+ Câu Hỏi Chuẩn</div>
            <div class="welcome-hl-desc">5 nhóm nguồn học liệu chọn lọc từ Lớp 1 đến Lớp 5.</div>
          </div>
        </div>
        <div class="welcome-highlight-card">
          <div class="welcome-hl-icon">🎧</div>
          <div>
            <div class="welcome-hl-title">Âm Nhạc Tập Trung</div>
            <div class="welcome-hl-desc">4 chế độ nhạc Lofi, Mozart Piano & Baroque kích thích trí nhớ.</div>
          </div>
        </div>
        <div class="welcome-highlight-card">
          <div class="welcome-hl-icon">📊</div>
          <div>
            <div class="welcome-hl-title">Lưu & Chấm Điểm Chuẩn</div>
            <div class="welcome-hl-desc">Nộp bài xong mới biết đáp án, lưu tự động Google Sheets.</div>
          </div>
        </div>
      </div>

      <div class="welcome-btn-row">
        <button class="btn-welcome-start" onclick="showScreen('home-screen')">
          🚀 BẮT ĐẦU NGAY ➔
        </button>
        <button class="btn-welcome-history" onclick="openHistoryScreen()">
          📊 Xem Lịch Sử Bài Thi
        </button>
      </div>
    </div>
  </div>
"""

# Bỏ class active ở home-screen nếu có, và chèn WELCOME_SCREEN_HTML ngay trước home-screen
if 'id="welcome-screen"' not in html:
    html = html.replace('<div class="quiz-card screen active" id="home-screen">', '<div class="quiz-card screen" id="home-screen">')
    html = html.replace('<!-- =====================================================================\n       1. HOME SCREEN', WELCOME_SCREEN_HTML + '\n  <!-- =====================================================================\n       1. HOME SCREEN')

# =========================================================================
# 4. THÊM MÀN HÌNH LỊCH SỬ LÀM BÀI (HISTORY SCREEN)
# =========================================================================
HISTORY_SCREEN_HTML = """  <!-- =====================================================================
       5. HISTORY SCREEN (BẢNG THỐNG KÊ & LỊCH SỬ LÀM BÀI CÓ SEARCH, FILTER)
       ===================================================================== -->
  <div class="quiz-card screen" id="history-screen">
    <div class="history-container">
      <div class="history-header-bar">
        <h2 style="font-size:1.35rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
          <span>📊</span>
          <span>Lịch Sử Bài Thi & Bảng Thống Kê</span>
        </h2>
        <div style="display:flex; gap:8px;">
          <button class="btn-source-action" onclick="showScreen('home-screen')" style="font-weight:700;">🏠 Về Trang Chủ</button>
          <button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>
        </div>
      </div>

      <!-- DASHBOARD TỔNG QUAN -->
      <div class="history-dashboard-grid">
        <div class="history-stat-card">
          <div class="history-stat-val" id="hist-total-tests">0</div>
          <div class="history-stat-lbl">LƯỢT ĐÃ THI</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-val" id="hist-avg-score" style="color:#059669;">0.0</div>
          <div class="history-stat-lbl">ĐIỂM TRUNG BÌNH</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-val" id="hist-avg-accuracy" style="color:var(--primary);">0%</div>
          <div class="history-stat-lbl">TỈ LỆ ĐÚNG</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-val" id="hist-highest-score" style="color:#D97706;">0.0</div>
          <div class="history-stat-lbl">KỶ LỤC ĐIỂM CAO</div>
        </div>
      </div>

      <!-- THANH TÌM KIẾM & BỘ LỌC -->
      <div class="history-filter-bar">
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh, lớp, nguồn đề..." oninput="renderHistoryTable()">
        <select class="history-filter-select" id="history-filter-level" onchange="renderHistoryTable()">
          <option value="all">🌟 Tất cả mức điểm</option>
          <option value="high">🏆 Xuất sắc (≥ 9.0 điểm)</option>
          <option value="medium">👍 Khá tốt (6.5 - 8.9 điểm)</option>
          <option value="low">📖 Cần cố gắng (&lt; 6.5 điểm)</option>
        </select>
        <select class="history-filter-select" id="history-filter-src" onchange="renderHistoryTable()">
          <option value="all">📚 Tất cả nguồn đề</option>
          <option value="SGK">SGK Việt Nam</option>
          <option value="Trạng Nguyên">Trạng Nguyên & Violympic</option>
          <option value="Kangaroo">Kangaroo Khoa học</option>
          <option value="IXL">IXL & Khan</option>
          <option value="National">NatGeo Kids</option>
        </select>
      </div>

      <!-- BẢNG LỊCH SỬ CHI TIẾT -->
      <div class="history-table-wrap">
        <table class="history-table">
          <thead>
            <tr>
              <th>Thời Gian</th>
              <th>Học Sinh</th>
              <th>Lớp</th>
              <th>Nguồn Đề Thi</th>
              <th style="text-align:center;">Số Câu</th>
              <th style="text-align:center;">Điểm Số</th>
              <th style="text-align:center;">Thời Gian</th>
            </tr>
          </thead>
          <tbody id="history-table-body">
            <!-- Render động qua renderHistoryTable() -->
          </tbody>
        </table>
      </div>
    </div>
  </div>
"""

if 'id="history-screen"' not in html:
    html = html.replace('<!-- =====================================================================\n       4. REVIEW SCREEN', HISTORY_SCREEN_HTML + '\n  <!-- =====================================================================\n       4. REVIEW SCREEN')

# Thêm nút xem lịch sử vào màn hình kết quả (result-screen)
OLD_RES_ACTIONS = """      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">🔄 Ôn lại câu sai</button>
        <button class="btn-primary-action" onclick="backToHome()">🏠 Về Trang Chủ</button>
      </div>"""

NEW_RES_ACTIONS = """      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">🔄 Ôn lại câu sai</button>
        <button class="btn-secondary" onclick="openHistoryScreen()">📊 Xem Lịch Sử</button>
        <button class="btn-primary-action" onclick="backToHome()">🏠 Về Trang Chủ</button>
      </div>"""

if OLD_RES_ACTIONS in html:
    html = html.replace(OLD_RES_ACTIONS, NEW_RES_ACTIONS)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã cập nhật xong cấu trúc HTML cho Welcome, History và Header!")
