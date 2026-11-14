#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. IMPORT GOOGLE FONTS (Nunito & Fredoka - Khan Academy Kids signature fonts)
font_link = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;600;700;800;900;1000&display=swap" rel="stylesheet">"""

if "family=Fredoka" not in content:
    content = content.replace("<head>", "<head>\n" + font_link, 1)
    print("1. Added Google Fonts (Fredoka & Nunito).")

# 2. KHAN ACADEMY KIDS CSS OVERHAUL
khan_css = """
  /* =======================================================================
     KHAN ACADEMY KIDS DESIGN LANGUAGE (VIBRANT, PLAYFUL, ROUNDED & FRIENDLY)
     ======================================================================= */
  * { 
    box-sizing: border-box; 
    margin: 0; 
    padding: 0; 
    font-family: 'Nunito', system-ui, -apple-system, sans-serif; 
  }

  h1, h2, h3, h4, .btn-start, .section-title, .home-card-header, .welcome-title, .home-mascot-name {
    font-family: 'Fredoka', 'Nunito', sans-serif !important;
  }

  body {
    background: linear-gradient(180deg, #BAE6FD 0%, #E0F2FE 25%, #F0FDF4 65%, #FEF9C3 100%) !important;
    background-attachment: fixed;
    min-height: 100vh;
    padding: clamp(10px, 2vw, 24px);
    display: flex;
    justify-content: center;
    align-items: flex-start;
    color: #1E293B;
  }

  /* KHAN KIDS APP HEADER */
  .app-header {
    background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
    border-radius: 24px !important;
    padding: 12px 20px !important;
    box-shadow: 0 8px 24px rgba(2, 132, 199, 0.25), 0 2px 6px rgba(0,0,0,0.06) !important;
    border: 3px solid rgba(255, 255, 255, 0.4) !important;
    margin-bottom: 18px !important;
  }
  .header-titles h1 {
    font-family: 'Fredoka', sans-serif !important;
    font-size: clamp(1.4rem, 3.2vw, 2rem) !important;
    color: white !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.15) !important;
    letter-spacing: 0.5px;
  }
  .header-titles p {
    color: #E0F2FE !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
  }

  /* KHAN KIDS CLOUD CARDS */
  .screen, .welcome-card, .quiz-card, .history-container {
    background: #FFFFFF !important;
    border-radius: 28px !important;
    border: 3px solid #E0F2FE !important;
    box-shadow: 0 12px 36px rgba(14, 165, 233, 0.12), 0 2px 8px rgba(0,0,0,0.04) !important;
    padding: clamp(16px, 2.5vw, 28px) !important;
  }

  /* KHAN KIDS CHUNKY 3D BUTTONS */
  .btn-start {
    background: #10B981 !important;
    color: white !important;
    border: 2.5px solid #059669 !important;
    border-bottom: 6px solid #047857 !important;
    border-radius: 9999px !important;
    font-family: 'Fredoka', sans-serif !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    padding: 14px 32px !important;
    box-shadow: 0 8px 20px rgba(16, 185, 129, 0.35) !important;
    cursor: pointer !important;
    transition: all 0.12s ease !important;
    letter-spacing: 0.5px;
  }
  .btn-start:hover {
    background: #059669 !important;
    transform: translateY(-2px);
    box-shadow: 0 12px 24px rgba(16, 185, 129, 0.4) !important;
  }
  .btn-start:active {
    transform: translateY(4px) !important;
    border-bottom-width: 2px !important;
    box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3) !important;
  }

  /* NAVIGATION PILL BUTTONS */
  .btn-nav-history {
    border-radius: 9999px !important;
    font-weight: 800 !important;
    border: 2px solid rgba(255,255,255,0.6) !important;
    border-bottom: 3.5px solid rgba(0,0,0,0.15) !important;
    padding: 7px 14px !important;
    transition: all 0.15s ease !important;
    font-size: 0.82rem !important;
  }
  .btn-nav-history:active {
    transform: translateY(2px) !important;
    border-bottom-width: 1.5px !important;
  }

  /* QUIZ CHOICE OPTIONS (KHAN KIDS CHUNKY CARDS) */
  .choice-option {
    border-radius: 20px !important;
    border: 2.5px solid #E2E8F0 !important;
    border-bottom: 5px solid #CBD5E1 !important;
    background: #FFFFFF !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    padding: 14px 18px !important;
    transition: all 0.15s ease !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03) !important;
  }
  .choice-option:hover {
    border-color: #38BDF8 !important;
    background: #F0F9FF !important;
    transform: translateY(-2px);
  }
  .choice-option.selected {
    border-color: #0284C7 !important;
    border-bottom-color: #0369A1 !important;
    background: #E0F2FE !important;
    color: #0369A1 !important;
  }
  .choice-letter {
    background: #E0F2FE !important;
    color: #0284C7 !important;
    border-radius: 12px !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 700 !important;
  }
  .choice-option.selected .choice-letter {
    background: #0284C7 !important;
    color: white !important;
  }

  /* HERO MASCOT CARD (HOME SCREEN) */
  .home-hero-card {
    background: linear-gradient(135deg, #E0F2FE 0%, #F0F9FF 100%) !important;
    border: 2.5px solid #BAE6FD !important;
    border-radius: 24px !important;
    box-shadow: 0 8px 20px rgba(2, 132, 199, 0.08) !important;
  }
  .home-card {
    border-radius: 22px !important;
    border: 2.5px solid #E2E8F0 !important;
  }
  .home-card-header {
    background: #F8FAFC !important;
    font-family: 'Fredoka', sans-serif !important;
    font-size: 1.05rem !important;
    color: #0F172A !important;
  }
  .home-pill {
    border-radius: 9999px !important;
    font-weight: 800 !important;
    border-bottom: 3.5px solid #CBD5E1 !important;
  }
  .home-pill.active {
    background: #0284C7 !important;
    border-color: #0284C7 !important;
    border-bottom-color: #0369A1 !important;
    color: white !important;
  }
  .topic-pill {
    border-radius: 16px !important;
    font-weight: 800 !important;
  }
  .topic-pill.selected {
    background: #0284C7 !important;
    color: white !important;
  }
"""

if "KHAN ACADEMY KIDS DESIGN LANGUAGE" not in content:
    content = content.replace("</style>", khan_css + "\n</style>", 1)
    print("2. Added Khan Academy Kids CSS Design System.")

# 3. REWRITE submitLogin() TO SYNC STUDENT NAME DIRECTLY & FETCH REAL PROFILE
new_login_func = """function submitLogin() {
  const username = document.getElementById('login-username').value.trim().toLowerCase();
  const pin = document.getElementById('login-pin').value.trim();
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');

  if (!username || !pin) {
    alert('Vui lòng nhập Tên đăng nhập và Mã PIN!');
    return;
  }

  // 1. KIỂM TRA ĐẶC QUYỀN ADMIN (MẬT KHẨU 11081993)
  if (username === 'admin' && pin === '11081993') {
    const adminAcc = {
      username: 'admin',
      pin: '11081993',
      studentName: 'Quản Trị Viên (Admin)',
      studentClass: 'Toàn Trường',
      role: 'admin',
      totalTests: 999,
      highestScore: 10,
      badge: '👑 Quản Trị Viên'
    };
    localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(adminAcc));
    updateHeaderAuthDisplay();
    updateAdminHeaderUI();
    closeAuthModal();
    alert('👑 Đăng nhập Quản Trị Viên (Admin) thành công! Bạn có quyền xem toàn bộ lịch sử và quản lý học sinh.');
    return;
  }

  // 2. TÌM TÀI KHOẢN ĐÃ CÓ TRONG LOCALSTORAGE HOẶC TRONG DANH SÁCH USER
  const allUsers = (typeof getAllUsersAggregated === 'function') ? getAllUsersAggregated() : [];
  const foundUser = allUsers.find(u => u.username.toLowerCase() === username);

  const localSaved = getStoredAccount();
  let studentFullName = (localSaved && localSaved.username === username && localSaved.studentName) ? localSaved.studentName : (foundUser ? foundUser.name : username);
  let studentClass = (foundUser && foundUser.studentClass) ? foundUser.studentClass : 'Lớp 2';

  const newAcc = {
    username: username,
    pin: pin,
    studentName: studentFullName,
    studentClass: studentClass,
    role: 'student',
    totalTests: foundUser ? foundUser.totalTests : 0,
    highestScore: foundUser ? foundUser.highestScore : 0,
    badge: foundUser ? foundUser.badge : '⭐'
  };

  localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(newAcc));
  updateHeaderAuthDisplay();
  updateAdminHeaderUI();
  closeAuthModal();

  alert(`🎉 Chào mừng bé [${newAcc.studentName}] (@${username}) đã đăng nhập thành công!`);

  // Đồng bộ từ Cloud qua GET (trả về đúng profile từ Google Sheets)
  if (scriptUrl) {
    fetch(`${scriptUrl}?action=login&username=${encodeURIComponent(username)}&pin=${encodeURIComponent(pin)}`)
      .then(res => res.json())
      .then(data => {
        if (data && data.user) {
          const updated = {
            ...newAcc,
            studentName: data.user.studentName || newAcc.studentName,
            studentClass: data.user.studentClass || newAcc.studentClass,
            totalTests: data.user.totalTests || newAcc.totalTests,
            highestScore: data.user.highestScore || newAcc.highestScore,
            badge: data.user.badge || newAcc.badge
          };
          localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(updated));
          updateHeaderAuthDisplay();
        }
      })
      .catch(err => console.log('Login fetch note', err));

    // Đồng bộ ngay lịch sử bài thi của bé từ Sheets
    fetchHistoryFromCloud();
  }
}"""

old_login_pattern = re.compile(r'function submitLogin\(\) \{.*?alert\(`Đã đăng nhập tài khoản \[@\$\{username\}\] thành công!`\);.*?\}\)', re.DOTALL)
if old_login_pattern.search(content):
    content = old_login_pattern.sub(new_login_func, content)
    print("3. Replaced submitLogin() with intelligent profile syncing.")

# 4. REWRITE renderHistoryTable() WITH ULTRA-SMART MATCHING AND CLOUD FETCH
new_render_history_func = """
// TỰ ĐỘNG KÉO KẾT QUẢ THI TỪ GOOGLE SHEETS VỀ MÁY
function fetchHistoryFromCloud() {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  if (!scriptUrl) return;

  fetch(`${scriptUrl}?action=getResults`)
    .then(res => res.json())
    .then(data => {
      if (data && data.results && data.results.length > 0) {
        const localList = getLocalHistory();
        let addedCount = 0;
        data.results.forEach(cloudItem => {
          const exists = localList.some(loc => 
            (loc.quizId && loc.quizId === cloudItem.quizId) || 
            (loc.timestamp && loc.timestamp === cloudItem.timestamp && loc.studentName === cloudItem.studentName)
          );
          if (!exists) {
            localList.push(cloudItem);
            addedCount++;
          }
        });
        if (addedCount > 0) {
          localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(localList));
          renderHistoryTable();
        }
      }
    })
    .catch(err => console.log('Fetch cloud results note', err));
}

function normalizeStringForMatch(str) {
  if (!str) return '';
  return str.toLowerCase()
    .normalize('NFD')
    .replace(/[\\u0300-\\u036f]/g, '')
    .replace(/[^a-z0-9]/g, '');
}

function renderHistoryTable() {
  const allHistory = getLocalHistory();
  const acc = getStoredAccount();
  const isAdm = isAdmin();

  // 1. CẬP NHẬT BANNER PHÂN QUYỀN & BỘ LỌC HỌC SINH
  const roleBanner = document.getElementById('history-role-banner');
  const studentSelect = document.getElementById('history-filter-student');
  let historyList = [];

  if (isAdm) {
    // 👑 QUYỀN ADMIN: Xem TOÀN BỘ bài thi của tất cả học sinh
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="admin-badge-banner">
          <span style="font-size:1.35rem;">👑</span>
          <div style="flex:1;">
            <strong>QUYỀN QUẢN TRỊ VIÊN:</strong> Bạn đang xem TOÀN BỘ lịch sử bài thi và thống kê của tất cả học sinh trong hệ thống.
          </div>
          <button onclick="openUserManagementModal()" class="btn-source-action" style="background:#B91C1C; color:white; border:none; padding:5px 12px; font-weight:800; font-size:0.78rem; border-radius:8px;">
            👥 Quản Lý User
          </button>
        </div>
      `;
    }
    if (studentSelect) {
      studentSelect.style.display = 'inline-block';
      const prevVal = studentSelect.value;
      const uniqueStudents = Array.from(new Set(allHistory.map(r => r.studentName || 'Học sinh'))).filter(Boolean);
      studentSelect.innerHTML = `<option value="all">👑 Tất cả học sinh (${uniqueStudents.length} bạn)</option>` +
        uniqueStudents.map(s => `<option value="${s}">👤 ${s}</option>`).join('');
      if (prevVal) studentSelect.value = prevVal;
    }

    const selStudent = studentSelect ? studentSelect.value : 'all';
    if (selStudent !== 'all') {
      historyList = allHistory.filter(r => (r.studentName || '') === selStudent);
    } else {
      historyList = allHistory;
    }
  } else if (acc && acc.username) {
    // 👤 HỌC SINH ĐĂNG NHẬP: THUẬT TOÁN SO KHỚP THÔNG MINH ĐA CHIỀU
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="student-badge-banner">
          <span style="font-size:1.35rem;">👤</span>
          <div style="flex:1;">
            <strong>HỒ SƠ BÉ: ${acc.studentName || acc.username} (${acc.studentClass || 'Lớp 2'})</strong> • Đang hiển thị kết quả ôn luyện của riêng bạn.
          </div>
          <button onclick="fetchHistoryFromCloud()" class="btn-source-action" style="background:white; color:#1E40AF; border-color:#BFDBFE; font-size:0.75rem; padding:4px 10px; font-weight:800; border-radius:8px;" title="Tải thêm bài thi từ Google Sheets về máy">
            🔄 Đồng bộ từ Cloud
          </button>
        </div>
      `;
    }
    if (studentSelect) studentSelect.style.display = 'none';

    const myUserNorm = normalizeStringForMatch(acc.username);
    const myNameNorm = normalizeStringForMatch(acc.studentName);

    historyList = allHistory.filter(r => {
      const rUserNorm = normalizeStringForMatch(r.username);
      const rNameNorm = normalizeStringForMatch(r.studentName);

      // 1. Trùng chính xác username hoặc studentName
      if (rUserNorm && rUserNorm === myUserNorm) return true;
      if (rNameNorm && rNameNorm === myNameNorm) return true;

      // 2. Trùng chuỗi không dấu (ví dụ "nathoi" khớp "Na thối", "Bé Na" khớp "Na thối")
      if (myUserNorm && (rNameNorm.includes(myUserNorm) || myUserNorm.includes(rNameNorm))) return true;
      if (myNameNorm && (rNameNorm.includes(myNameNorm) || myNameNorm.includes(rNameNorm))) return true;

      // 3. Nếu bài thi được làm trên chính thiết bị này của tài khoản
      if (r.username && r.username === acc.username) return true;

      return false;
    });

  } else {
    // 🔒 CHẾ ĐỘ KHÁCH: BẢO MẬT TUYỆT ĐỐI
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="guest-badge-banner">
          <div>
            🔒 <strong>CHẾ ĐỘ KHÁCH (GUEST):</strong> Bạn cần đăng nhập để xem lịch sử bài thi và bảng thống kê cá nhân của mình.
          </div>
          <button onclick="openAuthModal()" class="btn-source-action" style="background:linear-gradient(135deg, #0284C7, #0369A1); color:white; border:none; font-weight:800; font-size:0.8rem; padding:6px 14px; border-radius:8px; box-shadow:0 2px 8px rgba(2, 132, 199, 0.3);">
            👤 Đăng Nhập Ngay
          </button>
        </div>
      `;
    }
    if (studentSelect) studentSelect.style.display = 'none';
    historyList = allHistory.filter(r => !r.username && r.studentName === 'Học sinh');
  }

  // BỘ LỌC TÌM KIẾM, SỐ CÂU, ĐỘ KHÓ, MỨC ĐIỂM
  const searchInput = document.getElementById('history-search');
  const filterSize = document.getElementById('history-filter-size');
  const filterDiff = document.getElementById('history-filter-diff');
  const filterLevel = document.getElementById('history-filter-level');

  const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
  const sizeVal = filterSize ? filterSize.value : 'all';
  const diffVal = filterDiff ? filterDiff.value : 'all';
  const levelVal = filterLevel ? filterLevel.value : 'all';

  // Cập nhật Dashboard tổng quan
  const totalTests = historyList.length;
  document.getElementById('hist-total-tests').textContent = totalTests;

  if (totalTests > 0) {
    const sumScore = historyList.reduce((accItem, r) => accItem + (r.score10 || 0), 0);
    const avgScore = (sumScore / totalTests).toFixed(1);
    const sumPct = historyList.reduce((accItem, r) => accItem + (r.pct || 0), 0);
    const avgPct = Math.round(sumPct / totalTests);
    const maxScore = Math.max(...historyList.map(r => r.score10 || 0)).toFixed(1);

    document.getElementById('hist-avg-score').textContent = `${avgScore}/10`;
    document.getElementById('hist-avg-accuracy').textContent = `${avgPct}%`;
    document.getElementById('hist-highest-score').textContent = `${maxScore}/10`;
  } else {
    document.getElementById('hist-avg-score').textContent = '0.0';
    document.getElementById('hist-avg-accuracy').textContent = '0%';
    document.getElementById('hist-highest-score').textContent = '0.0';
  }

  let filtered = historyList.filter(r => {
    if (searchTerm) {
      const matchName = (r.studentName || '').toLowerCase().includes(searchTerm);
      const matchClass = (r.studentClass || '').toLowerCase().includes(searchTerm);
      if (!matchName && !matchClass) return false;
    }

    if (sizeVal !== 'all') {
      const targetSize = parseInt(sizeVal);
      if (r.totalQuestions !== targetSize) return false;
    }

    if (diffVal !== 'all') {
      if (diffVal === 'mixed') {
        if (r.diffVal && r.diffVal !== 'all') return false;
      } else {
        if (String(r.diffVal) !== diffVal) return false;
      }
    }

    if (levelVal === 'high' && r.score10 < 9.0) return false;
    if (levelVal === 'medium' && (r.score10 < 6.5 || r.score10 >= 9.0)) return false;
    if (levelVal === 'low' && r.score10 >= 6.5) return false;

    return true;
  });

  const tbody = document.getElementById('history-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (filtered.length === 0) {
    if (!isAdm && (!acc || !acc.username)) {
      tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:36px 20px; color:#64748B;">
        <div style="font-size:2.2rem; margin-bottom:8px;">🔒</div>
        <div style="font-weight:800; color:var(--dark); font-size:1.05rem; margin-bottom:6px;">Chế Độ Khách - Chưa Có Quyền Xem Lịch Sử Học Sinh</div>
        <div style="font-size:0.88rem; max-width:480px; margin:0 auto 16px auto; color:#64748B; line-height:1.45;">
          Để bảo vệ quyền riêng tư, học sinh chỉ xem được bài thi của chính mình, và Quản trị viên (Admin) mới có quyền xem toàn bộ danh sách.
        </div>
        <button onclick="openAuthModal()" class="btn-source-action" style="background:linear-gradient(135deg, #0284C7, #0369A1); color:white; border:none; padding:10px 22px; font-weight:800; border-radius:9999px; font-size:0.88rem; cursor:pointer; box-shadow:0 2px 8px rgba(2, 132, 199, 0.3);">
          👤 Đăng Nhập Tài Khoản Ngay
        </button>
      </td></tr>`;
      return;
    }

    if (acc && acc.username && !isAdm) {
      tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:32px 20px; color:#64748B;">
        <div style="font-size:2rem; margin-bottom:6px;">📝</div>
        <div style="font-weight:800; color:var(--dark); font-size:1rem; margin-bottom:6px;">Chưa Tìm Thấy Bài Thi Khớp Với Tên [${acc.studentName || acc.username}]</div>
        <div style="font-size:0.85rem; max-width:480px; margin:0 auto 14px auto; color:#64748B;">
          Nếu bạn đã làm bài thi trước khi tạo tài khoản (ví dụ tên "Na thối" hoặc "Bố Na"), hãy bấm nút bên dưới để đồng bộ từ Google Sheets hoặc cập nhật lại tên hiển thị nhé!
        </div>
        <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
          <button onclick="fetchHistoryFromCloud()" class="btn-source-action" style="background:#0284C7; color:white; border:none; padding:8px 16px; border-radius:9999px; font-weight:800;">
            🔄 Tải Lại Từ Google Sheets
          </button>
          <button onclick="promptLinkPastTests()" class="btn-source-action" style="background:#F0FDF4; color:#15803D; border-color:#86EFAC; padding:8px 16px; border-radius:9999px; font-weight:800;">
            ✏️ Liên Kết Tên Bài Thi Cũ
          </button>
        </div>
      </td></tr>`;
      return;
    }

    tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:24px; color:#64748B;">
      Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.
    </td></tr>`;
    return;
  }

  filtered.forEach((r, idx) => {
    const tr = document.createElement('tr');
    
    let badgeClass = 'medium';
    if (r.score10 >= 8.5) badgeClass = 'high';
    else if (r.score10 < 6.5) badgeClass = 'low';

    const diffDisplay = r.diffText || (r.diffVal === '1' ? 'Mức 1: Dễ' : (r.diffVal === '2' ? 'Mức 2: Vừa' : (r.diffVal === '3' ? 'Mức 3: Khó' : 'Hỗn hợp')));

    const parts = (r.timestamp || "").split(" ");
    const rowTime = r.quizTime || (parts.length >= 2 ? parts[0] : "");
    const rowDate = r.quizDate || (parts.length >= 2 ? parts[1] : r.timestamp || "");
    const rowId = r.quizId || r.id || (rowTime ? "QUIZ-" + rowTime.replace(/[:]/g, "") : "QUIZ");

    tr.innerHTML = `
      <td><span style="font-family:monospace; font-weight:700; color:var(--primary); font-size:0.75rem; background:#EEF2FF; padding:2px 6px; border-radius:4px;">${rowId}</span></td>
      <td style="font-weight:600; color:#334155; white-space:nowrap;">${rowDate}</td>
      <td style="font-weight:600; color:#64748B; white-space:nowrap;">${rowTime}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td><span style="background:${r.language === 'Tiếng Anh' ? '#F0F9FF' : (r.language === 'Song ngữ Anh - Việt' ? '#FAF5FF' : '#F0FDF4')}; color:${r.language === 'Tiếng Anh' ? '#0369A1' : (r.language === 'Song ngữ Anh - Việt' ? '#7E22CE' : '#15803D')}; border:1px solid ${r.language === 'Tiếng Anh' ? '#BAE6FD' : (r.language === 'Song ngữ Anh - Việt' ? '#E9D5FF' : '#BBF7D0')}; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.75rem;">${r.language || 'Tiếng Việt'}</span></td>
      <td>
        <span style="font-weight:700; color:var(--primary); font-size:0.82rem;">${r.totalQuestions} câu</span>
        <span style="color:#64748B; font-size:0.75rem; display:block;">${diffDisplay}</span>
      </td>
      <td style="text-align:center; font-weight:700;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center;"><span class="score-badge ${badgeClass}">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:600; color:#64748B; white-space:nowrap;">⏱️ ${r.duration || '00:00'}</td>
      <td style="text-align:center;">
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="background:#E0F2FE; color:#0284C7; border-color:#BAE6FD; font-size:0.78rem; padding:4px 10px; font-weight:800; white-space:nowrap; border-radius:9999px;">
          🔍 Xem lại
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function promptLinkPastTests() {
  const acc = getStoredAccount();
  if (!acc) return;
  const currentName = acc.studentName || acc.username;
  const newName = prompt(`Nhập Tên hoặc Biệt danh bạn đã dùng khi làm bài thi trước đây (hiện tại là "${currentName}"):`, currentName);
  if (newName && newName.trim()) {
    acc.studentName = newName.trim();
    localStorage.setItem(ACCOUNT_STORAGE_KEY, JSON.stringify(acc));
    updateHeaderAuthDisplay();
    renderHistoryTable();
    alert(`✅ Đã cập nhật tên bé thành "${newName.trim()}"! Hệ thống đang tải lại danh sách bài thi của bé.`);
  }
}
"""

pos_rf = content.find("function renderHistoryTable() {")
pos_rf_end = content.find("function viewHistoryDetail(", pos_rf)

if pos_rf != -1 and pos_rf_end != -1:
    content = content[:pos_rf] + new_render_history_func + "\n" + content[pos_rf_end:]
    print("4. Updated renderHistoryTable() with multi-match logic and cloud results fetcher.")

# 5. TRIGGER fetchHistoryFromCloud ON openHistoryScreen()
old_open_hist = """function openHistoryScreen() {
  renderHistoryTable();
  showScreen('history-screen');
}"""

new_open_hist = """function openHistoryScreen() {
  renderHistoryTable();
  showScreen('history-screen');
  if (typeof fetchHistoryFromCloud === 'function') {
    fetchHistoryFromCloud();
  }
}"""

if old_open_hist in content:
    content = content.replace(old_open_hist, new_open_hist, 1)
    print("5. Linked openHistoryScreen() to auto-fetch from Google Sheets.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Khan Academy Kids visual overhaul and History matching successfully applied!")
