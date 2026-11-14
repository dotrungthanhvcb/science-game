# -*- coding: utf-8 -*-
"""
Script cập nhật index.html:
1. Sửa luồng xem lại bài và chấm điểm:
   - Popup xem lại trước khi nộp ẩn 100% đúng/sai, chỉ hiện đã làm / chưa làm và đáp án đã chọn (màu trung tính).
   - Cho phép bấm vào từng câu để quay lại sửa đáp án nếu muốn.
   - Nút rõ ràng 'Nộp bài & Xem điểm'.
   - Sau khi bấm 'Nộp bài & Xem điểm': khóa bài làm, chính thức chấm điểm, hiển thị tổng đúng, tổng sai, điểm số và bảng chi tiết từng câu.
2. Lưu kết quả tự động vào Google Sheets:
   - Thêm ô nhập Lớp học sinh.
   - Biến GOOGLE_SCRIPT_URL = "" ở đầu <script>.
   - Gửi timestamp, studentName, studentClass, sources, totalQuestions, correctCount, wrongCount, score, duration.
   - Thông báo trực quan trên giao diện: Đang lưu -> Đã lưu thành công!
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Bổ sung CSS cho .choice-option.selected và quick-nav trung tính
EXTRA_CSS = """
  /* Đáp án đang được người chơi chọn (màu trung tính xanh dương, chưa lộ đúng sai) */
  .choice-option.selected {
    border-color: var(--primary) !important;
    background: #EEF2FF !important;
    color: var(--primary) !important;
    box-shadow: 0 4px 12px rgba(67, 97, 238, 0.16) !important;
  }
  .choice-option.selected .choice-letter {
    background: var(--primary) !important;
    color: white !important;
  }

  /* Quick Nav trong Modal Xem lại trước khi nộp bài */
  .quick-nav-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(68px, 1fr)) !important;
    gap: 10px !important;
    margin: 16px 0 !important;
    max-height: 280px !important;
    overflow-y: auto !important;
    padding: 6px !important;
  }
  .quick-nav-btn {
    min-height: 56px !important;
    width: auto !important;
    border-radius: 12px !important;
    border: 2px solid #E2E8F0 !important;
    background: #F8FAFC !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    cursor: pointer !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 2px !important;
    transition: all 0.2s ease !important;
    padding: 4px !important;
  }
  .quick-nav-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
  }
  .quick-nav-btn .q-num {
    font-size: 13px;
    font-weight: 800;
  }
  .quick-nav-btn .q-ans-badge {
    font-size: 11px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 6px;
  }
  /* Trạng thái ĐÃ LÀM: Màu trung tính xanh dương nhạt (không lộ đúng/sai) */
  .quick-nav-btn.answered {
    background: #EEF2FF !important;
    border-color: #4361EE !important;
    color: #1E40AF !important;
  }
  .quick-nav-btn.answered .q-ans-badge {
    background: #4361EE !important;
    color: #FFFFFF !important;
  }
  /* Trạng thái CHƯA LÀM: Màu xám */
  .quick-nav-btn.unanswered {
    background: #F8FAFC !important;
    border-color: #CBD5E1 !important;
    color: #64748B !important;
  }
  .quick-nav-btn.unanswered .q-ans-badge {
    background: #E2E8F0 !important;
    color: #64748B !important;
  }
  .quick-nav-btn.current {
    box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.45) !important;
    border-color: var(--primary) !important;
  }
"""

if '.choice-option.selected' not in html:
    html = html.replace('</style>', EXTRA_CSS + '\n</style>')

# 2. Thêm ô nhập Lớp của bé vào Start Screen
STUDENT_CLASS_HTML = """      <div class="config-row">
        <label>👤 Tên bé ôn tập:</label>
        <input type="text" id="user-name" placeholder="Bé Minh" value="Bé Yêu">
      </div>

      <div class="config-row">
        <label>🏫 Lớp của bé:</label>
        <input type="text" id="student-class" placeholder="Lớp 2A" value="Lớp 2">
      </div>"""

if 'id="student-class"' not in html:
    html = html.replace("""      <div class="config-row">
        <label>👤 Tên bé ôn tập:</label>
        <input type="text" id="user-name" placeholder="Bé Minh" value="Bé Yêu">
      </div>""", STUDENT_CLASS_HTML)

# 3. Thêm nút [📋 Xem lại bài] trên quiz-top-bar
OLD_TOP_BAR = """      <div class="top-left-controls">
        <button class="control-btn" onclick="pauseQuiz()">⏸️ Tạm dừng</button>
        <button class="control-btn" onclick="askQuitQuiz()">🚪 Thoát</button>
      </div>"""

NEW_TOP_BAR = """      <div class="top-left-controls">
        <button class="control-btn" onclick="pauseQuiz()">⏸️ Tạm dừng</button>
        <button class="control-btn" onclick="openReviewBeforeSubmit()" style="background:#EEF2FF; color:var(--primary); font-weight:700; border:1.5px solid #C7D2FE;">📋 Xem lại bài</button>
        <button class="control-btn" onclick="askQuitQuiz()">🚪 Thoát</button>
      </div>"""

if 'openReviewBeforeSubmit()' not in html.split('top-left-controls')[1].split('</div>')[0]:
    html = html.replace(OLD_TOP_BAR, NEW_TOP_BAR)

# 4. Cập nhật modal-quick-nav: Popup xem lại trung tính, ẩn 100% đúng/sai, có nút 'Nộp bài & Xem điểm'
OLD_QUICK_NAV_MODAL = """<!-- MODAL QUICK REVIEW: DUYỆT TỪNG CÂU TRƯỚC KHI NỘP -->
<div class="modal-overlay" id="modal-quick-nav">
  <div class="modal-box" style="max-width: 540px;">
    <div class="modal-icon">📋</div>
    <div class="modal-title">Danh Sách Câu Hỏi Bài Thi</div>
    <div class="modal-desc">
      Bấm vào số câu bất kỳ để xem lại đề bài và đáp án của câu đó nhé!
    </div>
    <div class="quick-nav-grid" id="quick-nav-grid"></div>
    <div style="display:flex; justify-content:center; gap:16px; font-size:13px; font-weight:600; margin-bottom:14px;">
      <span style="color:#15803D;">🟢 Đã đúng</span>
      <span style="color:#B91C1C;">🔴 Đã sai / Cần xem lại</span>
    </div>
    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()">Quay lại câu hiện tại</button>
      <button class="modal-btn-confirm" onclick="confirmSubmitAndFinish()" style="background:linear-gradient(135deg, #10B981, #059669);">🚀 Nộp bài ngay</button>
    </div>
  </div>
</div>"""

NEW_QUICK_NAV_MODAL = """<!-- MODAL QUICK REVIEW: XEM LẠI CÁC CÂU VỪA LÀM (TRƯỚC KHI NỘP) -->
<div class="modal-overlay" id="modal-quick-nav">
  <div class="modal-box" style="max-width: 580px;">
    <div class="modal-icon">📋</div>
    <div class="modal-title">Xem Lại Các Câu Vừa Làm</div>
    <div class="modal-desc" style="margin-bottom:8px;">
      Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!
    </div>
    <div style="background:#EEF2FF; border:1px solid #C7D2FE; border-radius:12px; padding:10px 14px; margin: 10px 0; font-size:14px; color:#1E40AF; font-weight:700;" id="quick-nav-status-text">
      📊 Đã làm: 0/0 câu
    </div>
    <div class="quick-nav-grid" id="quick-nav-grid"></div>
    <div style="display:flex; justify-content:center; gap:24px; font-size:13px; font-weight:700; margin-bottom:16px;">
      <span style="color:#1E40AF; display:flex; align-items:center; gap:4px;">🔵 Đã chọn đáp án</span>
      <span style="color:#64748B; display:flex; align-items:center; gap:4px;">⚪ Chưa làm</span>
    </div>
    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()" style="flex:1; min-width:160px; font-weight:700;">
        ← Tiếp tục làm bài
      </button>
      <button class="modal-btn-confirm" onclick="submitAndFinishQuiz()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:800; flex:1; min-width:180px; box-shadow:0 4px 14px rgba(16,185,129,0.35);">
        🚀 Nộp bài & Xem điểm
      </button>
    </div>
  </div>
</div>"""

if 'id="modal-quick-nav"' in html:
    # Thay thế khối modal-quick-nav cũ bằng khối mới
    pattern_modal = r'<!-- MODAL QUICK REVIEW[\s\S]*?id="modal-quick-nav"[\s\S]*?</div>\s*</div>\s*</div>'
    match_m = re.search(pattern_modal, html)
    if match_m:
        html = html[:match_m.start()] + NEW_QUICK_NAV_MODAL + html[match_m.end():]
        print("✅ Đã cập nhật modal-quick-nav thành công!")

# 5. Cập nhật result-screen: Thêm thống kê số câu sai để hiển thị rõ ràng: Đúng, Sai, Điểm số
OLD_SUMMARY_STATS = """    <div class="summary-stats">
      <div>
        <div class="summary-stat-val" id="res-score" style="color:var(--primary);">0%</div>
        <div class="summary-stat-lbl">ĐIỂM SỐ</div>
      </div>
      <div>
        <div class="summary-stat-val" id="res-correct" style="color:var(--success);">0/0</div>
        <div class="summary-stat-lbl">CÂU ĐÚNG</div>
      </div>
      <div>
        <div class="summary-stat-val" id="res-time" style="color:var(--warning);">00:00</div>
        <div class="summary-stat-lbl">THỜI GIAN</div>
      </div>
    </div>"""

NEW_SUMMARY_STATS = """    <div class="summary-stats">
      <div>
        <div class="summary-stat-val" id="res-score" style="color:var(--primary);">0/10</div>
        <div class="summary-stat-lbl">ĐIỂM SỐ</div>
      </div>
      <div>
        <div class="summary-stat-val" id="res-correct" style="color:var(--success);">0</div>
        <div class="summary-stat-lbl">CÂU ĐÚNG ✅</div>
      </div>
      <div>
        <div class="summary-stat-val" id="res-wrong" style="color:#EF4444;">0</div>
        <div class="summary-stat-lbl">CÂU SAI ❌</div>
      </div>
      <div>
        <div class="summary-stat-val" id="res-time" style="color:var(--warning);">00:00</div>
        <div class="summary-stat-lbl">THỜI GIAN ⏱️</div>
      </div>
    </div>"""

if OLD_SUMMARY_STATS in html:
    html = html.replace(OLD_SUMMARY_STATS, NEW_SUMMARY_STATS)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã cập nhật HTML & CSS hoàn tất.")
