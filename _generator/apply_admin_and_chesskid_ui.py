#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# =========================================================================
# 1. ADD CSS STYLES FOR ADMIN, BANNERS, MASCOTS, AND CHESSKID EFFECTS
# =========================================================================
custom_css = """
  /* =======================================================================
     CHESSKID & ADMIN MANAGEMENT STYLES
     ======================================================================= */
  .admin-badge-banner {
    background: linear-gradient(135deg, #FEF2F2, #FEE2E2);
    border: 1.5px solid #FECACA;
    color: #991B1B;
    padding: 10px 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.88rem;
    font-weight: 600;
  }
  .student-badge-banner {
    background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
    border: 1.5px solid #BFDBFE;
    color: #1E40AF;
    padding: 10px 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.88rem;
    font-weight: 600;
  }
  .guest-badge-banner {
    background: linear-gradient(135deg, #FFFBEB, #FEF3C7);
    border: 1.5px solid #FDE68A;
    color: #92400E;
    padding: 10px 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    font-size: 0.85rem;
  }

  /* MASCOT CARD & COMPANION */
  .mascot-interactive {
    cursor: pointer;
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .mascot-interactive:hover {
    transform: scale(1.08) rotate(3deg);
  }
  .mascot-interactive:active {
    transform: scale(0.95);
  }

  .mascot-picker-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 12px;
    margin: 16px 0;
  }
  .mascot-card {
    background: white;
    border: 2px solid #E2E8F0;
    border-radius: 16px;
    padding: 12px 8px;
    text-align: center;
    cursor: pointer;
    transition: all 0.25s ease;
  }
  .mascot-card:hover {
    border-color: var(--primary);
    transform: translateY(-4px);
    box-shadow: 0 8px 16px rgba(67, 97, 238, 0.15);
  }
  .mascot-card.active {
    border-color: var(--primary);
    background: #EEF2FF;
    box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.25);
  }
  .mascot-card-svg {
    width: 64px;
    height: 64px;
    margin: 0 auto 8px auto;
  }
  .mascot-card-name {
    font-weight: 800;
    font-size: 0.88rem;
    color: var(--dark);
  }
  .mascot-card-title {
    font-size: 0.72rem;
    color: #64748B;
    margin-top: 2px;
  }

  /* USER MANAGEMENT TABLE */
  .user-mgmt-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 10px;
    margin-bottom: 16px;
  }
  .user-mgmt-stat-card {
    background: white;
    border: 1.5px solid #E2E8F0;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
  }
  .user-mgmt-stat-val {
    font-size: 1.35rem;
    font-weight: 900;
    color: var(--primary);
  }
  .user-mgmt-stat-lbl {
    font-size: 0.75rem;
    color: #64748B;
    font-weight: 700;
    margin-top: 2px;
  }
"""

if "CHESSKID & ADMIN MANAGEMENT STYLES" not in content:
    content = content.replace("</style>", custom_css + "\n</style>", 1)
    print("1. Added Custom CSS.")
else:
    print("1. Custom CSS already present.")

# =========================================================================
# 2. ADD USER MANAGEMENT BUTTON TO HEADER
# =========================================================================
old_header_btns = """      <!-- NÚT MỜI BẠN BÈ -->
      <button class="btn-nav-history" onclick="shareGameLink()" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC;" title="Chia sẻ link game cho bạn bè cùng chơi">
        <span>📤</span>
        <span>Mời Bạn</span>
      </button>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->"""

new_header_btns = """      <!-- NÚT MỜI BẠN BÈ -->
      <button class="btn-nav-history" onclick="shareGameLink()" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC;" title="Chia sẻ link game cho bạn bè cùng chơi">
        <span>📤</span>
        <span>Mời Bạn</span>
      </button>

      <!-- NÚT QUẢN LÝ USER (ADMIN) -->
      <button class="btn-nav-history" id="btn-header-user-mgmt" onclick="openUserManagementModal()" style="background:#FEF2F2; color:#DC2626; border-color:#FECACA; font-weight:800;" title="Quản lý danh sách học sinh tham gia">
        <span>👥</span>
        <span id="btn-user-mgmt-label">Quản Lý User</span>
      </button>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->"""

if old_header_btns in content:
    content = content.replace(old_header_btns, new_header_btns, 1)
    print("2. Added User Management button in Header.")
else:
    print("WARNING: old_header_btns not found!")

# =========================================================================
# 3. ADD MODALS: USER MANAGEMENT & MASCOT PICKER
# =========================================================================
modals_html = """
  <!-- =====================================================================
       MODAL: QUẢN LÝ DANH SÁCH USER (DÀNH CHO ADMIN)
       ===================================================================== -->
  <div class="modal-overlay" id="modal-user-management">
    <div class="modal-box" style="max-width: 860px; width: 95%;">
      <div class="modal-header">
        <h3 style="display:flex; align-items:center; gap:8px;">
          <span>👑</span>
          <span>Quản Lý Danh Sách Học Sinh Tham Gia</span>
        </h3>
        <button class="modal-close" onclick="closeUserManagementModal()">✕</button>
      </div>
      <div class="modal-body" style="padding: 16px 20px;">
        <div class="user-mgmt-stats">
          <div class="user-mgmt-stat-card">
            <div class="user-mgmt-stat-val" id="mgmt-stat-users">0</div>
            <div class="user-mgmt-stat-lbl">Học Sinh Tham Gia</div>
          </div>
          <div class="user-mgmt-stat-card">
            <div class="user-mgmt-stat-val" id="mgmt-stat-tests">0</div>
            <div class="user-mgmt-stat-lbl">Lượt Thi Đã Làm</div>
          </div>
          <div class="user-mgmt-stat-card">
            <div class="user-mgmt-stat-val" id="mgmt-stat-high">0.0</div>
            <div class="user-mgmt-stat-lbl">Điểm Kỷ Lục</div>
          </div>
          <div class="user-mgmt-stat-card">
            <div class="user-mgmt-stat-val" id="mgmt-stat-active" style="font-size:1.05rem;">Chưa có</div>
            <div class="user-mgmt-stat-lbl">Học Sinh Tích Cực Nhất</div>
          </div>
        </div>

        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:12px; align-items:center;">
          <input type="text" id="mgmt-search-input" class="history-search-input" placeholder="🔍 Tìm theo tên bé hoặc username..." oninput="renderUserManagementTable()" style="flex:1; min-width:200px;">
          <select id="mgmt-filter-class" class="history-filter-select" onchange="renderUserManagementTable()">
            <option value="all">🏫 Tất cả khối lớp</option>
            <option value="1">Lớp 1</option>
            <option value="2">Lớp 2</option>
            <option value="3">Lớp 3</option>
            <option value="4">Lớp 4</option>
            <option value="5">Lớp 5</option>
            <option value="6">Lớp 6</option>
          </select>
          <button class="btn-source-action" onclick="fetchUsersFromCloud()" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-weight:700;">
            🔄 Đồng bộ từ Sheets
          </button>
        </div>

        <div class="history-table-wrap" style="max-height: 420px; overflow-y: auto;">
          <table class="history-table">
            <thead>
              <tr>
                <th style="width:40px;">Avatar</th>
                <th>Nickname</th>
                <th>Họ Tên Bé</th>
                <th>Lớp</th>
                <th>Ngày Tham Gia</th>
                <th style="text-align:center;">Lượt Thi</th>
                <th style="text-align:center;">Điểm Cao Nhất</th>
                <th>Huy Hiệu</th>
                <th style="text-align:center;">Hành Động</th>
              </tr>
            </thead>
            <tbody id="user-mgmt-tbody">
              <!-- Render động qua renderUserManagementTable() -->
            </tbody>
          </table>
        </div>
      </div>
      <div class="modal-footer" style="display:flex; justify-content:space-between; align-items:center;">
        <span style="font-size:0.8rem; color:#64748B;">👑 Chế độ quản trị viên: Xem toàn diện mọi người dùng và lịch sử thi.</span>
        <button class="btn-modal-cancel" onclick="closeUserManagementModal()">Đóng</button>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       MODAL: CHỌN BẠN ĐỒNG HÀNH KHOA HỌC (CHESSKID STYLE)
       ===================================================================== -->
  <div class="modal-overlay" id="modal-mascot-picker">
    <div class="modal-box" style="max-width: 600px;">
      <div class="modal-header">
        <h3 style="display:flex; align-items:center; gap:8px;">
          <span>✨</span>
          <span>Chọn Bạn Đồng Hành Cùng Bé</span>
        </h3>
        <button class="modal-close" onclick="closeMascotPickerModal()">✕</button>
      </div>
      <div class="modal-body" style="padding: 16px 20px;">
        <p style="font-size:0.88rem; color:#475569; margin-bottom:12px;">
          Mỗi bạn đồng hành mang một phong cách học tập độc đáo, sẽ cổ vũ bé trong suốt các bài thi khoa học!
        </p>
        <div class="mascot-picker-grid" id="mascot-picker-grid">
          <!-- Render động qua renderMascotCards() -->
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-modal-submit" onclick="closeMascotPickerModal()" style="width:100%;">
          Xác Nhận & Bắt Đầu Học! 🚀
        </button>
      </div>
    </div>
  </div>
"""

if "id=\"modal-user-management\"" not in content:
    content = content.replace("<!-- =====================================================================", modals_html + "\n  <!-- =====================================================================", 1)
    print("3. Added User Management & Mascot Picker Modals.")
else:
    print("3. Modals already present.")

# =========================================================================
# 4. UPDATE HISTORY SCREEN WITH ADMIN FILTER AND BANNER
# =========================================================================
old_history_toolbar = """      <!-- THANH TÌM KIẾM & BỘ LỌC THÔNG MINH -->
      <div class="history-toolbar">
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh hoặc lớp..." oninput="renderHistoryTable()">
        
        <select class="history-filter-select" id="history-filter-size" onchange="renderHistoryTable()">"""

new_history_toolbar = """      <!-- BANNER PHÂN QUYỀN HỌC SINH / ADMIN -->
      <div id="history-role-banner"></div>

      <!-- THANH TÌM KIẾM & BỘ LỌC THÔNG MINH -->
      <div class="history-toolbar">
        <select class="history-filter-select" id="history-filter-student" onchange="renderHistoryTable()" style="display:none; border-color:#FECACA; background:#FEF2F2; color:#991B1B; font-weight:800;">
          <option value="all">👑 Tất cả học sinh (Admin View)</option>
        </select>
        <input type="text" class="history-search-input" id="history-search" placeholder="🔍 Tìm theo tên học sinh hoặc lớp..." oninput="renderHistoryTable()">
        
        <select class="history-filter-select" id="history-filter-size" onchange="renderHistoryTable()">"""

if old_history_toolbar in content:
    content = content.replace(old_history_toolbar, new_history_toolbar, 1)
    print("4. Added Role Banner & Student Filter to History toolbar.")
else:
    print("WARNING: old_history_toolbar not found!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML Structure updated successfully!")
