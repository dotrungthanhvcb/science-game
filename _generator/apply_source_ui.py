# -*- coding: utf-8 -*-
"""
Script nâng cấp index.html đáp ứng trọn vẹn NHIỆM VỤ 2:
1. Bộ lọc chọn Nguồn đề thi (Multi-select) với 5 nguồn chuẩn + 1 nguồn 'Khác'
2. Nút tiện ích 'Chọn tất cả' / 'Bỏ chọn tất cả'
3. Mặc định chọn 5 nguồn chuẩn
4. Hiển thị số lượng câu khả dụng, vô hiệu hóa nút Bắt đầu nếu bỏ chọn hết
5. Hiển thị nhãn nhỏ (badge) nguồn câu hỏi trong khi thi
6. Đảm bảo chạy mượt cả trên web server (Vercel) và file:// offline
"""
import re

INDEX_HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Thêm <script src="questions_500.js"></script> nếu chưa có
if 'questions_500.js' not in html:
    html = html.replace(
        '<script src="questions.js"></script>',
        '<script src="questions_500.js"></script>\n<script src="questions.js"></script>'
    )

# 2. Thêm CSS cho Bộ lọc Nguồn & Badge nguồn trong quiz
SOURCE_CSS = """
  /* =========================================================================
     BỘ LỌC CHỌN NGUỒN CÂU HỎI (5 NGUỒN CHUẨN + KHÁC) & BADGE NGUỒN
     ========================================================================= */
  .source-filter-card {
    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
    border: 2px solid #E2E8F0;
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  }
  .source-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 14px;
  }
  .source-header-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--dark);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .source-action-btns {
    display: flex;
    gap: 8px;
  }
  .btn-source-action {
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    color: #475569;
    padding: 6px 12px;
    border-radius: 10px;
    font-size: 0.82rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .btn-source-action:hover {
    background: #EEF2FF;
    border-color: var(--primary);
    color: var(--primary);
    transform: translateY(-1px);
  }
  .source-chips-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 12px;
  }
  .source-toggle-chip {
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: 14px;
    padding: 12px 14px;
    cursor: pointer;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    user-select: none;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .source-toggle-chip:hover {
    border-color: #A5B4FC;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(67, 97, 238, 0.08);
  }
  .source-toggle-chip.selected {
    border-color: var(--primary);
    background: linear-gradient(135deg, #FFFFFF 0%, #F5F7FF 100%);
    box-shadow: 0 4px 14px rgba(67, 97, 238, 0.16);
  }
  .source-chip-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
  }
  .source-chip-icon-title {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .source-chip-icon {
    font-size: 1.3rem;
  }
  .source-chip-title {
    font-weight: 800;
    font-size: 0.95rem;
    color: var(--dark);
  }
  .source-chip-badge {
    background: #E2E8F0;
    color: #475569;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 10px;
    transition: all 0.2s ease;
  }
  .source-toggle-chip.selected .source-chip-badge {
    background: #EEF2FF;
    color: var(--primary);
  }
  .source-chip-desc {
    font-size: 0.8rem;
    color: #64748B;
    line-height: 1.35;
    margin-bottom: 8px;
  }
  .source-chip-checkbox-row {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 6px;
  }
  .source-checkbox-indicator {
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 2px solid #CBD5E1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    color: white;
    font-weight: bold;
    transition: all 0.2s ease;
  }
  .source-toggle-chip.selected .source-checkbox-indicator {
    background: var(--primary);
    border-color: var(--primary);
  }
  .source-status-summary {
    margin-top: 12px;
    padding: 10px 14px;
    border-radius: 10px;
    background: #EEF2FF;
    border-left: 4px solid var(--primary);
    font-size: 0.88rem;
    font-weight: 700;
    color: #3730A3;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.3s ease;
  }
  .source-status-summary.warning {
    background: #FEF2F2;
    border-left-color: #EF4444;
    color: #B91C1C;
  }
  .btn-start:disabled, .btn-start.disabled-btn {
    opacity: 0.45 !important;
    cursor: not-allowed !important;
    pointer-events: none !important;
    filter: grayscale(0.85);
    box-shadow: none !important;
  }
  /* BADGE NGUỒN TRONG GIAO DIỆN LÀM BÀI */
  .badge-source {
    background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
    color: #4338CA;
    border: 1.5px solid #C7D2FE;
    font-weight: 800;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 2px 6px rgba(67, 97, 238, 0.08);
  }
"""

if '.source-filter-card' not in html:
    html = html.replace('</style>', SOURCE_CSS + '\n</style>')

# 3. Thêm Giao diện Chọn Nguồn vào home-screen
SOURCE_HTML = """
    <!-- ================================================================= -->
    <!-- 1. BỘ LỌC CHỌN NGUỒN CÂU HỎI (5 NGUỒN CHUẨN + KHÁC) -->
    <!-- ================================================================= -->
    <div class="source-filter-card">
      <div class="source-header-row">
        <div class="source-header-title">
          <span>📖</span>
          <span>1. Chọn Nguồn Đề Thi (Học liệu chuẩn)</span>
        </div>
        <div class="source-action-btns">
          <button type="button" class="btn-source-action" onclick="selectAllSources(true)">✓ Chọn tất cả</button>
          <button type="button" class="btn-source-action" onclick="selectAllSources(false)">✕ Bỏ chọn tất cả</button>
        </div>
      </div>
      <div class="source-chips-grid" id="source-chips-container">
        <!-- Render động qua renderSourceChips() -->
      </div>
      <div class="source-status-summary" id="source-summary-banner">
        <span id="source-summary-icon">💡</span>
        <span id="source-summary-text">Đang tải và cập nhật số lượng câu hỏi...</span>
      </div>
    </div>
"""

# Đổi số thứ tự các mục tiếp theo trong home-screen
# Mục 1. Chọn Độ Tuổi -> 2. Chọn Độ Tuổi
# Mục 2. Chọn Độ Khó Câu Hỏi -> 3. Chọn Độ Khó Câu Hỏi
# Mục 3. Chọn Chủ Đề Ôn Luyện -> 4. Chọn Chủ Đề Ôn Luyện
# Mục 4. Tùy Chọn Luyện Tập & Số Câu -> 5. Tùy Chọn Luyện Tập & Số Câu
if 'source-filter-card' not in html:
    # Chèn SOURCE_HTML ngay sau <div class="quiz-card screen active" id="home-screen">
    target_home_screen = '<div class="quiz-card screen active" id="home-screen">'
    html = html.replace(target_home_screen, target_home_screen + '\n' + SOURCE_HTML)
    html = html.replace('<div class="section-title">👶 1. Chọn Độ Tuổi</div>', '<div class="section-title">👶 2. Chọn Độ Tuổi</div>')
    html = html.replace('<div class="section-title">🎚️ 2. Chọn Độ Khó Câu Hỏi</div>', '<div class="section-title">🎚️ 3. Chọn Độ Khó Câu Hỏi</div>')
    html = html.replace('<div class="section-title">📚 3. Chọn Chủ Đề Ôn Luyện</div>', '<div class="section-title">📚 4. Chọn Chủ Đề Ôn Luyện</div>')
    html = html.replace('<div class="section-title">⚙️ 4. Tùy Chọn Luyện Tập & Số Câu</div>', '<div class="section-title">⚙️ 5. Tùy Chọn Luyện Tập & Số Câu</div>')

# 4. Thêm Badge Nguồn trong màn hình quiz-screen
TARGET_BADGE_ROW = """    <div class="question-badge-row">
      <span id="question-number">Câu 1/15</span>
      <span id="badge-topic-age" style="color:var(--primary);">Động Vật • Độ tuổi 6-7</span>
    </div>"""

REPLACEMENT_BADGE_ROW = """    <div class="question-badge-row">
      <span id="question-number">Câu 1/15</span>
      <span id="badge-source" class="badge-source">📗 Nguồn: SGK Việt Nam</span>
      <span id="badge-topic-age" style="color:var(--primary);">Động Vật • Độ tuổi 6-7</span>
    </div>"""

if 'id="badge-source"' not in html:
    html = html.replace(TARGET_BADGE_ROW, REPLACEMENT_BADGE_ROW)

with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã cập nhật thành công CSS, HTML cho Bộ lọc Nguồn và Badge câu hỏi!")
