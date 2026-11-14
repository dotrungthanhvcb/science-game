#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# =========================================================================
# 1. BẢNG VÀNG: XÓA HOÀN TOÀN DỮ LIỆU RÁC (sampleFriends)
# =========================================================================
old_leaderboard_func_pattern = re.compile(r'function fetchLeaderboardFromCloud\(\) \{.*?renderLeaderboardList\(cachedLeaderboard\);\s*\}', re.DOTALL)

new_leaderboard_func = """function fetchLeaderboardFromCloud() {
  const listElem = document.getElementById('lead-players-list');
  if (listElem) {
    listElem.innerHTML = '<div style="text-align:center; padding:30px; color:#64748B;">⏳ Đang tải bảng vàng từ kết quả thi thực tế...</div>';
  }

  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  
  // Tổng hợp dữ liệu THỰC TẾ từ Lịch sử làm bài (TUYỆT ĐỐI KHÔNG DÙNG DỮ LIỆU MẪU / RÁC)
  const localHist = getLocalHistory();
  const playerMap = {};

  // Chỉ lấy học sinh có tên thực tế, không lấy tên rác
  localHist.forEach(r => {
    const name = (r.studentName || '').trim();
    if (name && name !== 'Học sinh' && name !== 'Quản Trị Viên (Admin)') {
      if (!playerMap[name]) {
        playerMap[name] = {
          name: name,
          studentClass: r.studentClass || 'Lớp 2',
          totalTests: 0,
          highestScore: 0,
          badge: '🌱 Tân Binh'
        };
      }
      playerMap[name].totalTests++;
      const s = parseFloat(String(r.score10 || r.score || '0').split('/')[0]) || 0;
      playerMap[name].highestScore = Math.max(playerMap[name].highestScore, s);
      if (playerMap[name].highestScore >= 9.5) playerMap[name].badge = '👑 Đại Kiện Tướng';
      else if (playerMap[name].highestScore >= 8.5) playerMap[name].badge = '🥇 Học Sinh Xuất Sắc';
      else if (playerMap[name].highestScore >= 7.0) playerMap[name].badge = '🥈 Ong Chăm Chỉ';
    }
  });

  cachedLeaderboard = Object.values(playerMap);
  cachedLeaderboard.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
  renderLeaderboardList(cachedLeaderboard);

  // Cập nhật thêm từ cloud nếu có mạng
  if (scriptUrl) {
    fetch(`${scriptUrl}?action=getLeaderboard`)
      .then(res => res.json())
      .then(data => {
        if (data && data.leaderboard && data.leaderboard.length > 0) {
          data.leaderboard.forEach(p => {
            if (p.name && p.name !== 'Học sinh' && p.name !== 'Quản Trị Viên (Admin)') {
              if (!playerMap[p.name]) {
                playerMap[p.name] = p;
              } else {
                playerMap[p.name].totalTests = Math.max(playerMap[p.name].totalTests, p.totalTests || 0);
                playerMap[p.name].highestScore = Math.max(playerMap[p.name].highestScore, p.highestScore || 0);
              }
            }
          });
          cachedLeaderboard = Object.values(playerMap);
          cachedLeaderboard.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
          renderLeaderboardList(cachedLeaderboard);
        }
      })
      .catch(err => console.log('Leaderboard cloud note', err));
  }
}"""

if old_leaderboard_func_pattern.search(content):
    content = old_leaderboard_func_pattern.sub(new_leaderboard_func, content)
    print("1. Cleaned up Leaderboard: Removed all sampleFriends mock data.")
else:
    print("WARNING: fetchLeaderboardFromCloud pattern not matched!")

# =========================================================================
# 2. XÓA BỎ NÚT "XÓA LỊCH SỬ" TRÊN MÀN HÌNH LỊCH SỬ
# =========================================================================
old_clear_btn = '<button class="btn-source-action" onclick="clearHistoryData()" style="color:#B91C1C; border-color:#FCA5A5;">🗑️ Xóa Lịch Sử</button>'
if old_clear_btn in content:
    content = content.replace(old_clear_btn, "")
    print("2. Removed 'Xóa Lịch Sử' button completely.")
else:
    print("WARNING: old_clear_btn not found!")

# =========================================================================
# 3. FIX PHÂN QUYỀN GUEST: KHÔNG CHO PHÉP GUEST XEM FULL LIST
# =========================================================================
old_guest_logic = """  } else {
    // ⚠️ CHẾ ĐỘ KHÁCH
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="guest-badge-banner">
          <div>
            ⚠️ <strong>CHẾ ĐỘ KHÁCH:</strong> Đang xem bài thi làm trên thiết bị này. <button onclick="openAuthModal()" style="border:none; background:transparent; color:#B45309; text-decoration:underline; font-weight:800; cursor:pointer;">Đăng nhập ngay</button> để lưu giữ huy hiệu và thành tích riêng của bé!
          </div>
          <button onclick="openAuthModal()" class="btn-source-action" style="background:#FEF3C7; color:#B45309; border-color:#FDE68A; font-weight:800; font-size:0.75rem;">
            👤 Đăng Nhập
          </button>
        </div>
      `;
    }
    if (studentSelect) studentSelect.style.display = 'none';
    historyList = allHistory;
  }"""

new_guest_logic = """  } else {
    // 🔒 CHẾ ĐỘ KHÁCH: BẢO MẬT TUYỆT ĐỐI - KHÔNG CHO PHÉP XEM BÀI THI CỦA CÁC BẠN KHÁC
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="guest-badge-banner">
          <div>
            🔒 <strong>CHẾ ĐỘ KHÁCH (GUEST):</strong> Bạn cần đăng nhập để xem kết quả và bảng thống kê bài thi cá nhân.
          </div>
          <button onclick="openAuthModal()" class="btn-source-action" style="background:linear-gradient(135deg, #4361EE, #3A0CA3); color:white; border:none; font-weight:800; font-size:0.8rem; padding:6px 14px; border-radius:8px; box-shadow:0 2px 8px rgba(67, 97, 238, 0.3);">
            👤 Đăng Nhập Ngay
          </button>
        </div>
      `;
    }
    if (studentSelect) studentSelect.style.display = 'none';
    // Khách chỉ được xem bài thi ẩn danh trong phiên này, TUYỆT ĐỐI không xem bài của học sinh khác
    historyList = allHistory.filter(r => !r.username && r.studentName === 'Học sinh');
  }"""

if old_guest_logic in content:
    content = content.replace(old_guest_logic, new_guest_logic, 1)
    print("3. Fixed Guest permission: Guest can no longer view full list.")
else:
    print("WARNING: old_guest_logic not found!")

# Cập nhật thông báo khi danh sách trống ở chế độ khách
old_empty_history = """  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:24px; color:#64748B;">
      ${totalTests === 0 ? 'Chưa có bài thi nào thuộc tài khoản này. Hãy bắt đầu một bài thi nhé!' : 'Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.'}
    </td></tr>`;
    return;
  }"""

new_empty_history = """  if (filtered.length === 0) {
    if (!isAdm && (!acc || !acc.username)) {
      tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:36px 20px; color:#64748B;">
        <div style="font-size:2.2rem; margin-bottom:8px;">🔒</div>
        <div style="font-weight:800; color:var(--dark); font-size:1.05rem; margin-bottom:6px;">Chế Độ Khách - Chưa Có Quyền Xem Lịch Sử Học Sinh</div>
        <div style="font-size:0.88rem; max-width:480px; margin:0 auto 16px auto; color:#64748B; line-height:1.45;">
          Để bảo vệ quyền riêng tư, học sinh chỉ xem được bài thi của chính mình, và Quản trị viên (Admin) mới có quyền xem toàn bộ danh sách.
        </div>
        <button onclick="openAuthModal()" class="btn-source-action" style="background:linear-gradient(135deg, #4361EE, #3A0CA3); color:white; border:none; padding:10px 22px; font-weight:800; border-radius:10px; font-size:0.88rem; cursor:pointer; box-shadow:0 2px 8px rgba(67, 97, 238, 0.3);">
          👤 Đăng Nhập Tài Khoản Ngay
        </button>
      </td></tr>`;
      return;
    }
    tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:24px; color:#64748B;">
      ${totalTests === 0 ? 'Chưa có bài thi nào thuộc tài khoản này. Hãy bắt đầu một bài thi nhé!' : 'Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.'}
    </td></tr>`;
    return;
  }"""

if old_empty_history in content:
    content = content.replace(old_empty_history, new_empty_history, 1)
    print("3b. Updated empty history state for Guest.")

# =========================================================================
# 4 & 5. CẤU TRÚC LẠI MÀN HOME: 2 CỘT GỌN GÀNG + BẠN ĐỒNG HÀNH NGAY TRÊN HOME
# =========================================================================

# Thêm CSS cho giao diện Home mới
home_css = """
  /* =======================================================================
     GIAO DIỆN HOME SCREEN HIỆN ĐẠI & GỌN GÀNG (2 CỘT + MASCOT HERO CARD)
     ======================================================================= */
  .home-hero-card {
    background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
    border: 1.5px solid #C7D2FE;
    border-radius: 18px;
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    margin-bottom: 18px;
    box-shadow: 0 4px 14px rgba(67, 97, 238, 0.08);
    flex-wrap: wrap;
  }
  .home-mascot-card {
    display: flex;
    align-items: center;
    gap: 14px;
    cursor: pointer;
    background: white;
    padding: 10px 16px;
    border-radius: 14px;
    border: 1.5px solid #C7D2FE;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    transition: all 0.2s ease;
    flex: 1;
    min-width: 280px;
  }
  .home-mascot-card:hover {
    transform: translateY(-2px);
    border-color: var(--primary);
    box-shadow: 0 6px 16px rgba(67, 97, 238, 0.15);
  }
  .home-mascot-avatar {
    width: 58px;
    height: 58px;
    flex-shrink: 0;
    animation: floatMascot 2.5s ease-in-out infinite;
  }
  .home-mascot-info {
    flex: 1;
  }
  .home-mascot-name {
    font-size: 1.05rem;
    font-weight: 900;
    color: var(--primary);
  }
  .btn-change-mascot {
    font-size: 0.72rem;
    font-weight: 800;
    color: #4361EE;
    background: #EEF2FF;
    padding: 2px 8px;
    border-radius: 6px;
    border: 1px solid #C7D2FE;
  }
  .home-mascot-title {
    font-size: 0.76rem;
    font-weight: 700;
    color: #64748B;
  }
  .home-mascot-speech {
    font-size: 0.8rem;
    color: #334155;
    font-weight: 600;
    margin-top: 3px;
    line-height: 1.35;
  }

  .home-profile-quick {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
  }
  .home-quick-field {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .home-quick-field label {
    font-size: 0.75rem;
    font-weight: 800;
    color: #475569;
    text-transform: uppercase;
  }
  .home-quick-field input, .home-quick-field select {
    padding: 7px 10px;
    border-radius: 10px;
    border: 1.5px solid #CBD5E1;
    font-size: 0.85rem;
    font-weight: 700;
    outline: none;
    background: white;
  }
  .home-quick-field input:focus, .home-quick-field select:focus {
    border-color: var(--primary);
  }

  /* 2-COLUMN MAIN GRID */
  .home-main-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 18px;
  }
  @media (max-width: 820px) {
    .home-main-grid {
      grid-template-columns: 1fr;
    }
  }

  .home-card {
    background: white;
    border: 1.5px solid #E2E8F0;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  }
  .home-card-header {
    background: #F8FAFC;
    padding: 10px 14px;
    font-weight: 800;
    font-size: 0.95rem;
    color: var(--dark);
    border-bottom: 1.5px solid #E2E8F0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .home-form-body {
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .config-row-compact {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }
  .config-row-compact label {
    font-size: 0.84rem;
    font-weight: 700;
    color: #334155;
    flex: 1;
  }
  .config-row-compact select {
    flex: 1.2;
    padding: 6px 10px;
    border-radius: 8px;
    border: 1.5px solid #CBD5E1;
    font-size: 0.82rem;
    font-weight: 600;
    outline: none;
    background: white;
  }
  .home-pills-row {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }
  .home-pill {
    flex: 1;
    min-width: 70px;
    padding: 6px 10px;
    border-radius: 10px;
    border: 1.5px solid #E2E8F0;
    background: #F8FAFC;
    font-size: 0.78rem;
    font-weight: 700;
    color: #475569;
    cursor: pointer;
    transition: all 0.2s;
    text-align: center;
  }
  .home-pill:hover {
    border-color: var(--primary);
    color: var(--primary);
  }
  .home-pill.active {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
    box-shadow: 0 2px 6px rgba(67, 97, 238, 0.3);
  }

  .topics-grid-compact {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(115px, 1fr));
    gap: 6px;
  }
  .topics-grid-compact .topic-pill {
    padding: 6px 8px;
    font-size: 0.76rem;
    border-radius: 8px;
  }

  /* ACCORDION SHEETS */
  .home-sheets-accordion {
    border: 1.5px dashed #CBD5E1;
    border-radius: 10px;
    padding: 8px 12px;
    background: #FAFAFA;
    margin-top: 4px;
  }
  .home-sheets-toggle {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 700;
    color: #475569;
  }
  .home-action-bar {
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
    background: white;
    border: 1.5px solid #E2E8F0;
    border-radius: 16px;
    padding: 12px 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }
"""

if "GIAO DIỆN HOME SCREEN HIỆN ĐẠI & GỌN GÀNG" not in content:
    content = content.replace("</style>", home_css + "\n</style>", 1)
    print("4a. Added Home screen compact styles.")

# Thay thế khối HTML của home-screen
pos_home = content.find('id="home-screen">')
pos_quiz = content.find('id="quiz-screen">')

if pos_home != -1 and pos_quiz != -1:
    pos_home_end = content.rfind('</div>', pos_home, pos_quiz) + 6
    
    new_home_html = """id="home-screen">
    <!-- KHỐI 1: BẠN ĐỒNG HÀNH KHOA HỌC & HỒ SƠ NHANH CỦA BÉ -->
    <div class="home-hero-card">
      <div class="home-mascot-card" onclick="openMascotPickerModal()" title="Bấm để chọn Bạn đồng hành khoa học yêu thích!">
        <div class="home-mascot-avatar" id="home-mascot-svg-wrap"></div>
        <div class="home-mascot-info">
          <div style="display:flex; align-items:center; gap:6px;">
            <span class="home-mascot-name" id="home-mascot-name">Giáo Sư Cú Vọ</span>
            <span class="btn-change-mascot">Đổi bạn ▾</span>
          </div>
          <div class="home-mascot-title" id="home-mascot-title">Bác Học Thông Thái</div>
          <div class="home-mascot-speech" id="home-mascot-speech">"Chào bạn! Cùng tớ chinh phục đỉnh cao khoa học hôm nay nhé! 🚀"</div>
        </div>
      </div>

      <div class="home-profile-quick">
        <div class="home-quick-field">
          <label>👤 Tên bé:</label>
          <input type="text" id="user-name" placeholder="Bé Yêu" value="Bé Yêu" style="width:120px;">
        </div>
        <div class="home-quick-field">
          <label>🏫 Khối lớp:</label>
          <select id="student-class" onchange="onClassGradeChange()">
            <option value="all">🌟 Tất cả (Lớp 1-5)</option>
            <option value="1">🎒 Lớp 1 (6t)</option>
            <option value="2" selected>🌱 Lớp 2 (7t)</option>
            <option value="3">🌿 Lớp 3 (8t)</option>
            <option value="4">🔬 Lớp 4 (9t)</option>
            <option value="5">🚀 Lớp 5 (10t)</option>
            <option value="6">🏆 Lớp 6 (Nâng cao)</option>
          </select>
        </div>
        <div class="home-quick-field">
          <label>🌐 Ngôn ngữ:</label>
          <select id="language-mode-select" onchange="onLanguageModeChange()">
            <option value="vi" selected>🇻🇳 Tiếng Việt</option>
            <option value="bilingual">🌐 Song ngữ Anh-Việt</option>
            <option value="en">🇬🇧 Tiếng Anh</option>
          </select>
        </div>
      </div>
    </div>

    <!-- KHỐI 2: 2 CỘT GỌN GÀNG -->
    <div class="home-main-grid">
      <!-- CỘT 1: CẤU HÌNH ĐỀ THI -->
      <div class="home-card">
        <div class="home-card-header">
          <span>⚙️</span>
          <span>1. Quy Cách Đề Thi</span>
        </div>
        <div class="home-form-body">
          <div class="config-row-compact">
            <label>🔢 Số lượng câu:</label>
            <select id="quiz-size" onchange="updatePoolCountDisplay()">
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

          <div class="config-row-compact">
            <label>📚 Nguồn đề thi:</label>
            <select id="target-source-select" onchange="onTargetSourceDropdownChange()">
              <option value="all" selected>🌟 Tất cả nguồn (Đa dạng 500 câu)</option>
              <option value="Trạng Nguyên & Violympic">🏆 Trạng Nguyên & Violympic</option>
              <option value="SGK Việt Nam (GDPT 2018)">📗 SGK Việt Nam (GDPT 2018)</option>
              <option value="Kangaroo Khoa học (IKSC)">🦘 Kangaroo Khoa học (IKSC)</option>
              <option value="IXL & Khan Academy">🌐 IXL & Khan Academy</option>
              <option value="National Geographic Kids">🦁 National Geographic Kids</option>
              <option value="Khác">🧩 Khác (Mở rộng)</option>
            </select>
          </div>

          <div class="config-row-compact">
            <label>🧠 Chế độ lặp lại:</label>
            <select id="review-ratio" onchange="updatePoolCountDisplay()">
              <option value="random" selected>🎲 Ngẫu nhiên chuẩn</option>
              <option value="mistakes">🔄 Ưu tiên câu từng làm sai</option>
              <option value="unseen">🆕 Chỉ câu chưa từng làm</option>
              <option value="reviewed">🔁 Củng cố trí nhớ</option>
            </select>
          </div>

          <div style="margin-top: 6px;">
            <label style="font-size:0.82rem; font-weight:800; color:var(--dark); display:block; margin-bottom:6px;">🎚️ Độ khó câu hỏi:</label>
            <div class="home-pills-row">
              <button type="button" class="home-pill active" onclick="selectDiff('all', this)">🌟 Hỗn hợp</button>
              <button type="button" class="home-pill" onclick="selectDiff('1', this)">⭐ Dễ</button>
              <button type="button" class="home-pill" onclick="selectDiff('2', this)">⭐⭐ Vừa</button>
              <button type="button" class="home-pill" onclick="selectDiff('3', this)">⭐⭐⭐ Khó</button>
            </div>
          </div>

          <!-- KẾT NỐI SHEETS THU GỌN -->
          <div class="home-sheets-accordion">
            <div class="home-sheets-toggle" onclick="toggleSheetsAccordion()">
              <span>🔗 Kết nối Google Sheets</span>
              <span id="sheets-toggle-icon">▾</span>
            </div>
            <div id="home-sheets-content" style="display:none; margin-top:8px;">
              <div style="display:flex; gap:6px; align-items:center;">
                <input type="text" id="apps-script-url" placeholder="URL Google Apps Script..." style="flex:1; font-size:0.8rem; padding:6px 10px; border-radius:6px; border:1px solid #CBD5E1;" oninput="localStorage.setItem('science_quiz_script_url', this.value.trim())">
                <button type="button" onclick="saveScriptUrlAndSyncFromHome()" style="background:var(--primary); color:white; border:none; padding:7px 12px; border-radius:6px; font-weight:700; cursor:pointer; font-size:0.75rem; white-space:nowrap;">
                  💾 Lưu & Đồng Bộ
                </button>
              </div>
              <div style="display:flex; justify-content:space-between; margin-top:6px; font-size:0.75rem;">
                <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" style="color:var(--primary); font-weight:700; text-decoration:none;">📄 Mở Google Sheets ↗</a>
                <a href="javascript:void(0)" onclick="promptForScriptUrl()" style="color:#6366F1; text-decoration:underline;">❓ Hướng dẫn kết nối</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- CỘT 2: CHỦ ĐỀ & ĐỘ TUỔI -->
      <div class="home-card">
        <div class="home-card-header">
          <span>📚</span>
          <span>2. Chủ Đề & Độ Tuổi</span>
        </div>
        <div class="home-form-body">
          <div>
            <label style="font-size:0.82rem; font-weight:800; color:var(--dark); display:block; margin-bottom:6px;">👶 Phù hợp lứa tuổi:</label>
            <div class="home-pills-row">
              <button type="button" class="home-pill active" onclick="selectAge('all', this)">🌟 Tất cả</button>
              <button type="button" class="home-pill" onclick="selectAge('6-7', this)">🌱 6 - 7 tuổi</button>
              <button type="button" class="home-pill" onclick="selectAge('7-8', this)">🌿 7 - 8 tuổi</button>
              <button type="button" class="home-pill" onclick="selectAge('8-9', this)">🚀 8 - 9 tuổi</button>
            </div>
          </div>

          <div style="margin-top: 6px;">
            <label style="font-size:0.82rem; font-weight:800; color:var(--dark); display:block; margin-bottom:6px;">🔬 Chọn chủ đề ôn luyện:</label>
            <div class="topics-grid-compact" id="topics-list"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- KHỐI 3: THANH BẮT ĐẦU -->
    <div class="home-action-bar">
      <div class="pool-status-banner" id="pool-count-banner" style="margin-bottom:0; flex:1;">
        <span>💡</span>
        <span id="pool-count-text">Đang có 100 câu hỏi sẵn sàng cho lượt thi này.</span>
      </div>
      <button class="btn-start" onclick="startQuiz()" style="margin-top:0; min-width:240px;">🚀 BẮT ĐẦU ÔN LUYỆN</button>
    </div>
  </div>"""

    content = content[:pos_home] + new_home_html + content[pos_home_end:]
    print("4b. Restructured Home Screen HTML layout successfully.")
else:
    print("WARNING: Home screen pos not matched!")

# =========================================================================
# 5. CẬP NHẬT JAVASCRIPT: selectAge, selectDiff, updateAllMascotsUI, toggleSheetsAccordion
# =========================================================================
js_updates = """
function toggleSheetsAccordion() {
  const content = document.getElementById('home-sheets-content');
  const icon = document.getElementById('sheets-toggle-icon');
  if (!content) return;
  const isHidden = (content.style.display === 'none' || !content.style.display);
  content.style.display = isHidden ? 'block' : 'none';
  if (icon) icon.textContent = isHidden ? '▴' : '▾';
}

function selectAge(age, elem) {
  selectedAge = age;
  if (elem && elem.parentElement) {
    elem.parentElement.querySelectorAll('.home-pill, .filter-chip').forEach(c => c.classList.remove('active', 'selected'));
    elem.classList.add('active', 'selected');
  }
  updatePoolCountDisplay();
}

function selectDiff(diff, elem) {
  selectedDiff = diff;
  if (elem && elem.parentElement) {
    elem.parentElement.querySelectorAll('.home-pill, .filter-chip').forEach(c => c.classList.remove('active', 'selected'));
    elem.classList.add('active', 'selected');
  }
  updatePoolCountDisplay();
}
"""

if "function toggleSheetsAccordion" not in content:
    pos_sc = content.rfind('</script>')
    content = content[:pos_sc] + "\n" + js_updates + "\n" + content[pos_sc:]
    print("5a. Appended JS helper functions.")

# Cập nhật updateAllMascotsUI để bao gồm cả Home screen
old_update_mascots = """function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 75);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = m.name;

  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 52);
}"""

new_update_mascots = """function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  
  // 1. Welcome screen
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 75);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = m.name;

  // 2. Home screen (Mascot ngay trên Menu Home)
  const homeSvgWrap = document.getElementById('home-mascot-svg-wrap');
  if (homeSvgWrap) homeSvgWrap.innerHTML = renderMascotSvg(m.id, 58);
  const homeName = document.getElementById('home-mascot-name');
  if (homeName) homeName.textContent = m.name;
  const homeTitle = document.getElementById('home-mascot-title');
  if (homeTitle) homeTitle.textContent = m.title;

  // 3. Quiz screen
  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 52);
}"""

if old_update_mascots in content:
    content = content.replace(old_update_mascots, new_update_mascots, 1)
    print("5b. Updated updateAllMascotsUI to sync Home Screen mascot.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("All 5 user requests successfully processed and applied to index.html!")
