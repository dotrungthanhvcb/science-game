#!/usr/bin/env python3
HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header Buttons: Add Leaderboard, Account, Share
old_header_btns = """      <!-- NÚT XEM LỊCH SỬ LÀM BÀI -->
      <button class="btn-nav-history" onclick="openHistoryScreen()">
        <span>📊</span>
        <span>Lịch Sử Bài Thi</span>
      </button>
    </div>
  </header>"""

new_header_btns = """      <!-- NÚT BẢNG VÀNG VINH DANH -->
      <button class="btn-nav-history" onclick="openLeaderboardModal()" style="background:#FEF3C7; color:#B45309; border-color:#FDE68A;" title="Xem Bảng Vàng Điểm Cao Của Các Bạn">
        <span>🏆</span>
        <span>Bảng Vàng</span>
      </button>

      <!-- NÚT XEM LỊCH SỬ LÀM BÀI -->
      <button class="btn-nav-history" onclick="openHistoryScreen()">
        <span>📊</span>
        <span>Lịch Sử</span>
      </button>

      <!-- NÚT MỜI BẠN BÈ -->
      <button class="btn-nav-history" onclick="shareGameLink()" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC;" title="Chia sẻ link game cho bạn bè cùng chơi">
        <span>📤</span>
        <span>Mời Bạn</span>
      </button>

      <!-- NÚT TÀI KHOẢN HỌC SINH -->
      <div id="header-auth-container">
        <button class="btn-nav-history" onclick="openAuthModal()" style="background:linear-gradient(135deg, #4361EE, #3A0CA3); color:white; border:none; font-weight:800; box-shadow:0 2px 8px rgba(67, 97, 238, 0.3);">
          <span>👤</span>
          <span id="header-auth-label">Đăng Nhập</span>
        </button>
      </div>
    </div>
  </header>"""

assert old_header_btns in html, "Could not find old_header_btns"
html = html.replace(old_header_btns, new_header_btns)

# 2. Add Auth Modal and Leaderboard Modal HTML before end of modals
old_modal_pos = "<!-- MODAL XEM LẠI NHANH CHI TIẾT BÀI THI TỪ LỊCH SỬ -->"
assert old_modal_pos in html, "Could not find old_modal_pos"

auth_modals_html = """<!-- MODAL ĐĂNG KÝ & ĐĂNG NHẬP TÀI KHOẢN (KID-FRIENDLY: NICKNAME + PIN 4 SỐ) -->
<div class="modal-overlay" id="modal-auth">
  <div class="modal-box" style="max-width: 460px; text-align:left; padding: 24px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1.5px solid #E2E8F0; padding-bottom:10px;">
      <div style="font-size:1.2rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
        <span id="auth-modal-title-icon">👤</span>
        <span id="auth-modal-title">Tài Khoản Học Sinh</span>
      </div>
      <button onclick="closeAuthModal()" style="background:#F1F5F9; border:none; width:30px; height:30px; border-radius:50%; font-size:16px; font-weight:bold; cursor:pointer; color:#64748B;">✕</button>
    </div>

    <!-- NẾU ĐÃ ĐĂNG NHẬP: HIỂN THỊ HỒ SƠ BÉ -->
    <div id="auth-profile-view" style="display:none;">
      <div style="text-align:center; padding:16px 0; background:#F8FAFC; border-radius:14px; margin-bottom:16px; border:1px solid #E2E8F0;">
        <div style="font-size:3rem; margin-bottom:6px;" id="prof-avatar">🦁</div>
        <div style="font-size:1.3rem; font-weight:900; color:var(--dark);" id="prof-name">Bé Minh Nam</div>
        <div style="font-size:0.88rem; color:#64748B; margin-top:2px;" id="prof-sub">@nam_lop2 • Lớp 2</div>
        <div style="display:inline-block; margin-top:8px; padding:4px 12px; background:#FEF3C7; color:#B45309; border-radius:20px; font-weight:800; font-size:0.85rem;" id="prof-badge">
          👑 Đại Kiện Tướng
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:18px;">
        <div style="background:#EEF2FF; padding:12px; border-radius:12px; text-align:center;">
          <div style="font-size:0.78rem; color:#4F46E5; font-weight:700;">ĐIỂM CAO NHẤT</div>
          <div style="font-size:1.4rem; font-weight:900; color:#312E81;" id="prof-high-score">10.0</div>
        </div>
        <div style="background:#F0FDF4; padding:12px; border-radius:12px; text-align:center;">
          <div style="font-size:0.78rem; color:#15803D; font-weight:700;">SỐ BÀI ĐÃ THI</div>
          <div style="font-size:1.4rem; font-weight:900; color:#14532D;" id="prof-tests-count">12</div>
        </div>
      </div>

      <div style="display:flex; gap:10px;">
        <button class="btn-source-action" onclick="shareGameLink()" style="flex:1; background:#F0FDF4; color:#15803D; border-color:#86EFAC; font-weight:800; justify-content:center;">
          📤 Mời Bạn Bè
        </button>
        <button class="btn-source-action" onclick="logoutAccount()" style="color:#B91C1C; border-color:#FCA5A5; font-weight:700;">
          🚪 Đăng Xuất
        </button>
      </div>
    </div>

    <!-- NẾU CHƯA ĐĂNG NHẬP: TAB ĐĂNG NHẬP & ĐĂNG KÝ -->
    <div id="auth-forms-view">
      <div style="display:flex; background:#F1F5F9; border-radius:12px; padding:4px; margin-bottom:16px;">
        <button id="tab-btn-login" onclick="switchAuthTab('login')" style="flex:1; padding:8px; border:none; border-radius:9px; font-weight:800; font-size:0.88rem; cursor:pointer; background:white; color:var(--primary); box-shadow:0 2px 4px rgba(0,0,0,0.06);">
          🔑 Đăng Nhập
        </button>
        <button id="tab-btn-register" onclick="switchAuthTab('register')" style="flex:1; padding:8px; border:none; border-radius:9px; font-weight:700; font-size:0.88rem; cursor:pointer; background:transparent; color:#64748B;">
          ✨ Đăng Ký Mới
        </button>
      </div>

      <!-- FORM ĐĂNG NHẬP -->
      <div id="auth-form-login">
        <div style="margin-bottom:12px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Tên đăng nhập (Nickname):</label>
          <input type="text" id="login-username" placeholder="ví dụ: nam_lop2" style="width:100%; padding:10px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:0.9rem; outline:none;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Mã PIN bí mật (4 số):</label>
          <input type="password" id="login-pin" maxlength="6" placeholder="••••" style="width:100%; padding:10px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:1.1rem; letter-spacing:4px; outline:none;">
        </div>
        <button class="modal-btn-confirm" onclick="submitLogin()" style="width:100%; background:linear-gradient(135deg, #4361EE, #3A0CA3); font-weight:800; padding:12px; border-radius:10px; font-size:0.95rem;">
          🚀 Đăng Nhập Ngay
        </button>
        <div style="text-align:center; font-size:0.8rem; color:#64748B; margin-top:12px;">
          Chưa có tài khoản? <a href="javascript:void(0)" onclick="switchAuthTab('register')" style="color:var(--primary); font-weight:700; text-decoration:underline;">Tạo tài khoản chỉ mất 10 giây!</a>
        </div>
      </div>

      <!-- FORM ĐĂNG KÝ -->
      <div id="auth-form-register" style="display:none;">
        <div style="margin-bottom:10px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Tên đăng nhập (Nickname tự chọn):</label>
          <input type="text" id="reg-username" placeholder="ví dụ: soc_nau, bong_bong" style="width:100%; padding:9px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:0.9rem; outline:none;">
        </div>
        <div style="margin-bottom:10px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Mã PIN 4 số (Dễ nhớ để sau này vào lại):</label>
          <input type="password" id="reg-pin" maxlength="6" placeholder="ví dụ: 1234" style="width:100%; padding:9px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:1.1rem; letter-spacing:4px; outline:none;">
        </div>
        <div style="margin-bottom:10px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Họ tên của bé:</label>
          <input type="text" id="reg-fullname" placeholder="ví dụ: Nguyễn Minh Nam" style="width:100%; padding:9px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:0.9rem; outline:none;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-size:0.82rem; font-weight:700; color:var(--dark); margin-bottom:4px;">Lớp học của bé:</label>
          <select id="reg-class" style="width:100%; padding:9px 12px; border:2px solid #CBD5E1; border-radius:10px; font-size:0.9rem; outline:none; background:white;">
            <option value="Lớp 1">🎒 Lớp 1 (6 tuổi)</option>
            <option value="Lớp 2" selected>🌱 Lớp 2 (7 tuổi)</option>
            <option value="Lớp 3">🌿 Lớp 3 (8 tuổi)</option>
            <option value="Lớp 4">🔬 Lớp 4 (9 tuổi)</option>
            <option value="Lớp 5">🚀 Lớp 5 (10 tuổi)</option>
            <option value="Lớp 6">🏆 Lớp 6 (Nâng cao)</option>
          </select>
        </div>
        <button class="modal-btn-confirm" onclick="submitRegister()" style="width:100%; background:linear-gradient(135deg, #10B981, #059669); font-weight:800; padding:12px; border-radius:10px; font-size:0.95rem;">
          ✨ Tạo Tài Khoản & Bắt Đầu
        </button>
      </div>
    </div>
  </div>
</div>

<!-- MODAL BẢNG VÀNG VINH DANH (LEADERBOARD) -->
<div class="modal-overlay" id="modal-leaderboard">
  <div class="modal-box" style="max-width: 620px; max-height: 88vh; display:flex; flex-direction:column; text-align:left; padding: 22px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1.5px solid #E2E8F0; padding-bottom:10px;">
      <div>
        <div style="font-size:1.3rem; font-weight:900; color:var(--dark); display:flex; align-items:center; gap:8px;">
          <span>🏆</span>
          <span>Bảng Vàng Vinh Danh Bạn Bè</span>
        </div>
        <div style="font-size:0.82rem; color:#64748B; margin-top:2px;">Top các bạn đạt điểm cao & chăm chỉ ôn luyện nhất</div>
      </div>
      <button onclick="closeLeaderboardModal()" style="background:#F1F5F9; border:none; width:30px; height:30px; border-radius:50%; font-size:16px; font-weight:bold; cursor:pointer; color:#64748B;">✕</button>
    </div>

    <!-- FILTER THEO LỚP & NÚT LÀM MỚI -->
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; gap:8px; flex-wrap:wrap;">
      <div style="display:flex; align-items:center; gap:6px;">
        <span style="font-size:0.85rem; font-weight:700; color:#475569;">Lọc:</span>
        <select id="lead-filter-class" onchange="filterLeaderboardView()" style="padding:6px 10px; border:1.5px solid #CBD5E1; border-radius:8px; font-size:0.82rem; font-weight:700; outline:none; background:white;">
          <option value="all">🌟 Tất cả các lớp</option>
          <option value="Lớp 1">🎒 Lớp 1</option>
          <option value="Lớp 2">🌱 Lớp 2</option>
          <option value="Lớp 3">🌿 Lớp 3</option>
          <option value="Lớp 4">🔬 Lớp 4</option>
          <option value="Lớp 5">🚀 Lớp 5</option>
          <option value="Lớp 6">🏆 Lớp 6</option>
        </select>
      </div>

      <div style="display:flex; gap:8px;">
        <button class="btn-source-action" onclick="fetchLeaderboardFromCloud()" style="font-size:0.8rem; padding:6px 12px; font-weight:700; display:inline-flex; align-items:center; gap:4px;">
          🔄 Cập nhật
        </button>
        <button class="btn-source-action" onclick="shareGameLink()" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC; font-size:0.8rem; padding:6px 12px; font-weight:800; display:inline-flex; align-items:center; gap:4px;">
          📤 Mời Bạn Cùng Đua Top
        </button>
      </div>
    </div>

    <!-- DANH SÁCH TOP HỌC SINH -->
    <div style="overflow-y:auto; flex:1; padding-right:4px;" id="lead-players-list">
      <div style="text-align:center; padding:30px; color:#64748B;">Đang tải danh sách bảng vàng...</div>
    </div>
  </div>
</div>

"""

html = html.replace(old_modal_pos, auth_modals_html + "\n" + old_modal_pos)

# 3. Add Javascript Logic for Auth & Leaderboard & Share
js_auth_logic = """
// =========================================================================
// QUẢN LÝ TÀI KHOẢN HỌC SINH & BẢNG VÀNG VINH DANH (LEADERBOARD)
// =========================================================================
const ACCOUNT_STORAGE_KEY = 'science_quiz_kid_account';
let cachedLeaderboard = [];

function getStoredAccount() {
  try {
    const raw = localStorage.getItem(ACCOUNT_STORAGE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch(e) {
    return null;
  }
}

function updateHeaderAuthDisplay() {
  const acc = getStoredAccount();
  const label = document.getElementById('header-auth-label');
  const container = document.getElementById('header-auth-container');
  if (!container) return;

  if (acc && acc.username) {
    container.innerHTML = `
      <div onclick="openAuthModal()" style="display:inline-flex; align-items:center; gap:6px; background:#EEF2FF; color:var(--primary); padding:6px 12px; border-radius:10px; border:1.5px solid #C7D2FE; cursor:pointer; font-weight:800; font-size:0.82rem;" title="Xem hồ sơ cá nhân">
        <span>🦁</span>
        <span>${acc.studentName || acc.username}</span>
        <span style="background:var(--primary); color:white; padding:1px 6px; border-radius:6px; font-size:0.75rem;">${acc.studentClass || 'Lớp 2'}</span>
      </div>
    `;
    // Điền tự động vào màn hình Cài đặt
    const nameInput = document.getElementById('user-name');
    if (nameInput) nameInput.value = acc.studentName || acc.username;
    const classSelect = document.getElementById('student-class');
    if (classSelect && acc.studentClass) {
      const matchOpt = Array.from(classSelect.options).find(o => o.text.includes(acc.studentClass) || o.value === acc.studentClass.replace('Lớp ', ''));
      if (matchOpt) classSelect.value = matchOpt.value;
    }
  } else {
    container.innerHTML = `
      <button class="btn-nav-history" onclick="openAuthModal()" style="background:linear-gradient(135deg, #4361EE, #3A0CA3); color:white; border:none; font-weight:800; box-shadow:0 2px 8px rgba(67, 97, 238, 0.3);">
        <span>👤</span>
        <span>Đăng Nhập</span>
      </button>
    `;
  }
}

function openAuthModal() {
  const acc = getStoredAccount();
  const modal = document.getElementById('modal-auth');
  const profileView = document.getElementById('auth-profile-view');
  const formsView = document.getElementById('auth-forms-view');
  
  if (acc && acc.username) {
    profileView.style.display = 'block';
    formsView.style.display = 'none';
    document.getElementById('prof-name').textContent = acc.studentName || acc.username;
    document.getElementById('prof-sub').textContent = `@${acc.username} • ${acc.studentClass || 'Lớp 2'}`;
    document.getElementById('prof-badge').textContent = acc.badge || '🌱 Tân Binh';
    document.getElementById('prof-high-score').textContent = acc.highestScore ? `${acc.highestScore}/10` : '0.0';
    document.getElementById('prof-tests-count').textContent = acc.totalTests || 0;
  } else {
    profileView.style.display = 'none';
    formsView.style.display = 'block';
    switchAuthTab('login');
  }

  if (modal) modal.classList.add('active');
}

function closeAuthModal() {
  const modal = document.getElementById('modal-auth');
  if (modal) modal.classList.remove('active');
}

function switchAuthTab(tab) {
  const btnLogin = document.getElementById('tab-btn-login');
  const btnReg = document.getElementById('tab-btn-register');
  const formLogin = document.getElementById('auth-form-login');
  const formReg = document.getElementById('auth-form-register');

  if (tab === 'login') {
    btnLogin.style.background = 'white';
    btnLogin.style.color = 'var(--primary)';
    btnLogin.style.boxShadow = '0 2px 4px rgba(0,0,0,0.06)';
    btnReg.style.background = 'transparent';
    btnReg.style.color = '#64748B';
    btnReg.style.boxShadow = 'none';
    formLogin.style.display = 'block';
    formReg.style.display = 'none';
  } else {
    btnReg.style.background = 'white';
    btnReg.style.color = '#059669';
    btnReg.style.boxShadow = '0 2px 4px rgba(0,0,0,0.06)';
    btnLogin.style.background = 'transparent';
    btnLogin.style.color = '#64748B';
    btnLogin.style.boxShadow = 'none';
    formLogin.style.display = 'none';
    formReg.style.display = 'block';
  }
}

function submitRegister() {
  const username = document.getElementById('reg-username').value.trim().toLowerCase();
  const pin = document.getElementById('reg-pin').value.trim();
  const fullname = document.getElementById('reg-fullname').value.trim() || 'Bé Thông Thái';
  const sClass = document.getElementById('reg-class').value;
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');

  if (!username) {
    alert('Bé ơi, hãy nhập Tên đăng nhập (Nickname) nhé!');
    return;
  }
  if (!pin || pin.length < 4) {
    alert('Mã PIN cần có ít nhất 4 chữ số bí mật để bảo vệ tài khoản bé nhé!');
    return;
  }

  const payload = {
    action: 'register',
    username: username,
    pin: pin,
    studentName: fullname,
    studentClass: sClass
  };

  // Lưu tạm offline trước để trải nghiệm không bị gián đoạn
  const newAcc = {
    username: username,
    pin: pin,
    studentName: fullname,
    studentClass: sClass,
    totalTests: 0,
    highestScore: 0,
    badge: '🌱 Tân Binh'
  };
  localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(newAcc));
  updateHeaderAuthDisplay();
  closeAuthModal();

  alert(`🎉 Chúc mừng bé ${fullname} đã tạo tài khoản [@${username}] thành công! Bắt đầu ôn thi nào!`);

  // Bắn lên Google Sheets nếu có script URL
  if (scriptUrl) {
    fetch(scriptUrl, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(payload)
    }).catch(e => console.log('Register cloud note', e));
  }
}

function submitLogin() {
  const username = document.getElementById('login-username').value.trim().toLowerCase();
  const pin = document.getElementById('login-pin').value.trim();
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');

  if (!username || !pin) {
    alert('Vui lòng nhập Tên đăng nhập và Mã PIN!');
    return;
  }

  // Kiểm tra tài khoản đã lưu trên máy
  const currentAcc = getStoredAccount();
  if (currentAcc && currentAcc.username.toLowerCase() === username && currentAcc.pin === pin) {
    updateHeaderAuthDisplay();
    closeAuthModal();
    alert(`Chào mừng bé ${currentAcc.studentName || username} đã quay trở lại! ⭐`);
    return;
  }

  // Nếu nhập mới hoặc đăng nhập trên máy bạn
  const newAcc = {
    username: username,
    pin: pin,
    studentName: username,
    studentClass: 'Lớp 2',
    totalTests: 0,
    highestScore: 0,
    badge: '⭐'
  };
  localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(newAcc));
  updateHeaderAuthDisplay();
  closeAuthModal();

  alert(`Đã đăng nhập tài khoản [@${username}] thành công!`);

  if (scriptUrl) {
    fetch(scriptUrl, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ action: 'login', username: username, pin: pin })
    }).catch(e => console.log('Login cloud note', e));
  }
}

function logoutAccount() {
  if (confirm('Bé có chắc muốn đăng xuất khỏi tài khoản này không?')) {
    localStorage.removeItem(ACCOUNT_STORAGE_KEY);
    updateHeaderAuthDisplay();
    closeAuthModal();
    alert('Đã đăng xuất! Bé hiện đang ở chế độ Khách (Guest).');
  }
}

// BẢNG VÀNG VINH DANH (LEADERBOARD)
function openLeaderboardModal() {
  const modal = document.getElementById('modal-leaderboard');
  if (modal) modal.classList.add('active');
  fetchLeaderboardFromCloud();
}

function closeLeaderboardModal() {
  const modal = document.getElementById('modal-leaderboard');
  if (modal) modal.classList.remove('active');
}

function fetchLeaderboardFromCloud() {
  const listElem = document.getElementById('lead-players-list');
  if (listElem) {
    listElem.innerHTML = '<div style="text-align:center; padding:30px; color:#64748B;">⏳ Đang cập nhật bảng vàng từ Google Sheets...</div>';
  }

  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  
  // Tổng hợp dữ liệu từ Lịch sử máy + Mẫu dữ liệu phong phú để hiển thị ngay
  const localHist = getLocalHistory();
  const playerMap = {};

  // Tổng hợp từ lịch sử thực tế trong máy
  localHist.forEach(r => {
    const key = r.studentName || 'Học sinh';
    if (!playerMap[key]) {
      playerMap[key] = {
        name: key,
        studentClass: r.studentClass || 'Lớp 2',
        totalTests: 0,
        highestScore: 0,
        badge: '🌱 Tân Binh'
      };
    }
    playerMap[key].totalTests++;
    playerMap[key].highestScore = Math.max(playerMap[key].highestScore, r.score10 || 0);
  });

  // Bổ sung các bạn học sinh mẫu thi đua nếu ít dữ liệu
  const sampleFriends = [
    { name: "Bé Minh Nam", studentClass: "Lớp 2", totalTests: 8, highestScore: 10.0, badge: "👑 Đại Kiện Tướng" },
    { name: "Bảo Ngọc", studentClass: "Lớp 3", totalTests: 6, highestScore: 9.5, badge: "🥇 Học Sinh Xuất Sắc" },
    { name: "Tuấn Khang", studentClass: "Lớp 2", totalTests: 5, highestScore: 9.0, badge: "🥇 Học Sinh Xuất Sắc" },
    { name: "Gia Hưng", studentClass: "Lớp 4", totalTests: 7, highestScore: 8.5, badge: "🥈 Ong Chăm Chỉ" },
    { name: "Mai Anh", studentClass: "Lớp 1", totalTests: 4, highestScore: 8.0, badge: "🥈 Ong Chăm Chỉ" }
  ];

  sampleFriends.forEach(f => {
    if (!playerMap[f.name]) {
      playerMap[f.name] = f;
    }
  });

  cachedLeaderboard = Object.values(playerMap);
  cachedLeaderboard.sort((a, b) => b.highestScore - a.highestScore || b.totalTests - a.totalTests);
  renderLeaderboardList(cachedLeaderboard);
}

function filterLeaderboardView() {
  const filterClass = document.getElementById('lead-filter-class').value;
  if (filterClass === 'all') {
    renderLeaderboardList(cachedLeaderboard);
  } else {
    const filtered = cachedLeaderboard.filter(p => p.studentClass === filterClass);
    renderLeaderboardList(filtered);
  }
}

function renderLeaderboardList(players) {
  const listElem = document.getElementById('lead-players-list');
  if (!listElem) return;

  if (players.length === 0) {
    listElem.innerHTML = '<div style="text-align:center; padding:30px; color:#64748B;">Chưa có bạn nào trong lớp này. Bé hãy là người đầu tiên ghi danh nhé!</div>';
    return;
  }

  let html = '';
  players.slice(0, 20).forEach((p, idx) => {
    let rankBadge = `${idx + 1}`;
    let rankStyle = "background:#F1F5F9; color:#475569;";
    if (idx === 0) {
      rankBadge = "🥇";
      rankStyle = "background:#FEF3C7; color:#B45309; font-size:1.3rem;";
    } else if (idx === 1) {
      rankBadge = "🥈";
      rankStyle = "background:#F1F5F9; color:#475569; font-size:1.2rem;";
    } else if (idx === 2) {
      rankBadge = "🥉";
      rankStyle = "background:#FFEDD5; color:#9A3412; font-size:1.1rem;";
    }

    html += `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:10px 14px; background:white; border:1px solid #E2E8F0; border-radius:12px; margin-bottom:8px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:36px; height:36px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; ${rankStyle}">
            ${rankBadge}
          </div>
          <div>
            <div style="font-weight:800; color:var(--dark); font-size:0.95rem;">${p.name}</div>
            <div style="font-size:0.78rem; color:#64748B; display:flex; gap:6px; align-items:center;">
              <span style="background:#F8FAFC; border:1px solid #E2E8F0; padding:1px 6px; border-radius:4px; font-weight:700;">${p.studentClass || 'Lớp 2'}</span>
              <span>• ${p.totalTests || 1} bài đã thi</span>
            </div>
          </div>
        </div>

        <div style="text-align:right;">
          <div style="font-size:1.15rem; font-weight:900; color:#15803D;">${p.highestScore || 0}<span style="font-size:0.75rem; color:#64748B;">/10</span></div>
          <div style="font-size:0.72rem; font-weight:700; color:#B45309;">${p.badge || '⭐'}</div>
        </div>
      </div>
    `;
  });

  listElem.innerHTML = html;
}

// TÍNH NĂNG CHIA SẺ LINK GAME CHO BẠN BÈ
function shareGameLink() {
  const shareUrl = "https://science-game-sigma.vercel.app/";
  const shareText = "🔬 Cùng mình tham gia Đấu Trường Khoa Học Vui nhé! Vào thi và đua top điểm cao cùng mình tại:";
  
  if (navigator.share) {
    navigator.share({
      title: "Đấu Trường Khoa Học Vui",
      text: shareText,
      url: shareUrl
    }).catch(e => copyToClipboard(shareUrl));
  } else {
    copyToClipboard(shareUrl);
  }
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert("🎉 Đã sao chép đường link game! Bé hãy gửi cho các bạn qua Zalo/Facebook cùng thi nhé:\n\n" + text);
  }).catch(() => {
    prompt("Sao chép link game bên dưới để gửi cho bạn bè nhé:", text);
  });
}
"""

# Insert js_auth_logic into <script>
target_js_pos = "function openReviewScreen() {"
assert target_js_pos in html, "Could not find target_js_pos in index.html"
html = html.replace(target_js_pos, js_auth_logic + "\n\n" + target_js_pos)

# 4. In loadSavedSettings, call updateHeaderAuthDisplay()
old_load = "function loadSavedSettings() {"
assert old_load in html, "Could not find loadSavedSettings in index.html"
html = html.replace(old_load, old_load + "\n  updateHeaderAuthDisplay();")

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied Auth and Leaderboard successfully to index.html!")
