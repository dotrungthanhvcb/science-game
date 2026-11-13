# -*- coding: utf-8 -*-
import re

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Thêm CSS cho nút câu cuối cùng và modal duyệt câu
css_addition = """
  /* NÚT CÂU HỎI CUỐI CÙNG & HIỆU ỨNG NỔI BẬT */
  .btn-next-step.btn-last-step {
    background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4) !important;
    animation: pulseLastBtn 1.8s infinite;
  }
  @keyframes pulseLastBtn {
    0% { transform: scale(1); }
    50% { transform: scale(1.02); }
    100% { transform: scale(1); }
  }

  /* MODAL KIỂM TRA LẠI BÀI THI */
  .quick-nav-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(48px, 1fr));
    gap: 10px;
    margin: 16px 0;
    max-height: 240px;
    overflow-y: auto;
    padding: 6px;
  }
  .quick-nav-btn {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    border: 2px solid #E2E8F0;
    background: #F8FAFC;
    font-weight: 700;
    font-size: 15px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
  }
  .quick-nav-btn:hover {
    border-color: var(--primary);
    transform: translateY(-2px);
  }
  .quick-nav-btn.correct {
    background: #DCFCE7;
    border-color: #22C55E;
    color: #15803D;
  }
  .quick-nav-btn.wrong {
    background: #FEE2E2;
    border-color: #EF4444;
    color: #B91C1C;
  }
  .quick-nav-btn.current {
    box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.4);
    border-color: var(--primary);
  }
"""

if '.btn-next-step.btn-last-step' not in html:
    html = html.replace('</style>', css_addition + '\n</style>')
    print("Added CSS for last button and quick nav")

# 2. Thêm option 100 câu vào dropdown #quiz-size
if '100 câu' not in html:
    html = html.replace('<option value="50">50 câu (Đại hội tri thức)</option>',
                        '<option value="50">50 câu (Đại hội tri thức)</option>\n          <option value="100">100 câu (Đại đấu trường Khoa Học 1.000 câu)</option>')
    print("Added 100 questions option to select")

# 3. Thêm Modal Xác nhận nộp bài và Modal Lưới câu hỏi
modals_html = """
<!-- MODAL XÁC NHẬN CÂU HỎI CUỐI CÙNG -->
<div class="modal-overlay" id="modal-confirm-submit">
  <div class="modal-box" style="max-width: 480px;">
    <div class="modal-icon">🏁</div>
    <div class="modal-title">Bé đã đến câu cuối cùng rồi!</div>
    <div class="modal-desc">
      Bé đã hoàn thành tất cả các câu hỏi trong lượt ôn này.<br>
      Bé có muốn kiểm tra lại bài thi trước khi nộp không?
    </div>
    <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:14px; padding:12px; margin: 14px 0; font-size:15px; color:#166534; font-weight:700;" id="confirm-status-text">
      ✅ Đã hoàn thành toàn bộ câu hỏi!
    </div>
    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="openReviewBeforeSubmit()" style="background:#EEF2FF; color:var(--primary); border:2px solid var(--primary); font-weight:700; flex:1; min-width:180px;">
        🔍 Xem lại các câu vừa làm
      </button>
      <button class="modal-btn-confirm" onclick="confirmSubmitAndFinish()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:700; flex:1; min-width:160px;">
        🚀 Nộp bài & Xem điểm
      </button>
    </div>
  </div>
</div>

<!-- MODAL QUICK REVIEW: DUYỆT TỪNG CÂU TRƯỚC KHI NỘP -->
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
</div>
"""

if 'id="modal-confirm-submit"' not in html:
    # Chèn trước modal-pause
    html = html.replace('<div class="modal-overlay" id="modal-pause">', modals_html + '\n<div class="modal-overlay" id="modal-pause">')
    print("Added confirm submit modal and quick nav modal")

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved HTML with new CSS and Modals")
