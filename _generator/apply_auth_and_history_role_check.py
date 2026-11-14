#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. UPDATE submitLogin() WITH DIRECT ADMIN RECOGNITION
old_login_block = """  // Kiểm tra tài khoản đã lưu trên máy
  const currentAcc = getStoredAccount();
  if (currentAcc && currentAcc.username.toLowerCase() === username && currentAcc.pin === pin) {
    updateHeaderAuthDisplay();
    closeAuthModal();
    alert(`Chào mừng bé ${currentAcc.studentName || username} đã quay trở lại! ⭐`);
    return;
  }"""

new_login_block = """  // KIỂM TRA ĐẶC QUYỀN ADMIN (MẬT KHẨU 11081993)
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
    alert('👑 Đăng nhập Quản Trị Viên (Admin) thành công! Bạn có quyền xem toàn bộ lịch sử thi và quản lý danh sách học sinh.');
    return;
  }

  // Kiểm tra tài khoản đã lưu trên máy
  const currentAcc = getStoredAccount();
  if (currentAcc && currentAcc.username.toLowerCase() === username && currentAcc.pin === pin) {
    updateHeaderAuthDisplay();
    updateAdminHeaderUI();
    closeAuthModal();
    alert(`Chào mừng bé ${currentAcc.studentName || username} đã quay trở lại! ⭐`);
    return;
  }"""

if old_login_block in content:
    content = content.replace(old_login_block, new_login_block, 1)
    print("1. Updated submitLogin() with Admin recognition.")
else:
    print("WARNING: old_login_block not found!")

# 2. UPDATE updateHeaderAuthDisplay() TO STYLIZE ADMIN DISTINCTIVELY
old_auth_display = """  if (acc && acc.username) {
    container.innerHTML = `
      <div onclick="openAuthModal()" style="display:inline-flex; align-items:center; gap:6px; background:#EEF2FF; color:var(--primary); padding:6px 12px; border-radius:10px; border:1.5px solid #C7D2FE; cursor:pointer; font-weight:800; font-size:0.82rem;" title="Xem hồ sơ cá nhân">
        <span>🦁</span>
        <span>${acc.studentName || acc.username}</span>
        <span style="background:var(--primary); color:white; padding:1px 6px; border-radius:6px; font-size:0.75rem;">${acc.studentClass || 'Lớp 2'}</span>
      </div>
    `;"""

new_auth_display = """  if (acc && acc.username) {
    const isAdm = (acc.username === 'admin' || acc.role === 'admin');
    const badgeBg = isAdm ? '#FEF2F2' : '#EEF2FF';
    const badgeColor = isAdm ? '#991B1B' : 'var(--primary)';
    const badgeBorder = isAdm ? '#FECACA' : '#C7D2FE';
    const avatarIcon = isAdm ? '👑' : '🦁';
    const tagText = isAdm ? 'Admin' : (acc.studentClass || 'Lớp 2');
    const tagBg = isAdm ? '#DC2626' : 'var(--primary)';

    container.innerHTML = `
      <div onclick="openAuthModal()" style="display:inline-flex; align-items:center; gap:6px; background:${badgeBg}; color:${badgeColor}; padding:6px 12px; border-radius:10px; border:1.5px solid ${badgeBorder}; cursor:pointer; font-weight:800; font-size:0.82rem;" title="Xem hồ sơ">
        <span>${avatarIcon}</span>
        <span>${acc.studentName || acc.username}</span>
        <span style="background:${tagBg}; color:white; padding:1px 6px; border-radius:6px; font-size:0.75rem;">${tagText}</span>
      </div>
    `;"""

if old_auth_display in content:
    content = content.replace(old_auth_display, new_auth_display, 1)
    print("2. Updated updateHeaderAuthDisplay() with Admin styling.")
else:
    print("WARNING: old_auth_display not found!")

# 3. UPDATE renderHistoryTable() WITH COMPLETE PHÂN QUYỀN
pos_rh = content.find("function renderHistoryTable() {")
pos_rh_end = content.find("function viewHistoryDetail(", pos_rh)

if pos_rh != -1 and pos_rh_end != -1:
    new_render_history = """function renderHistoryTable() {
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
          <span style="font-size:1.25rem;">👑</span>
          <div style="flex:1;">
            <strong>QUYỀN QUẢN TRỊ VIÊN:</strong> Bạn đang xem TOÀN BỘ lịch sử bài thi và thống kê của tất cả học sinh.
          </div>
          <button onclick="openUserManagementModal()" class="btn-source-action" style="background:#B91C1C; color:white; border:none; padding:4px 10px; font-weight:800; font-size:0.75rem;">
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
    // 👤 HỌC SINH THƯỜNG: CHỈ XEM BÀI THI CỦA CHÍNH MÌNH
    if (roleBanner) {
      roleBanner.innerHTML = `
        <div class="student-badge-banner">
          <span style="font-size:1.25rem;">👤</span>
          <div>
            <strong>HỒ SƠ BÉ: ${acc.studentName || acc.username} (${acc.studentClass || 'Lớp 2'})</strong> • Bạn chỉ được xem kết quả và thống kê bài thi của chính mình.
          </div>
        </div>
      `;
    }
    if (studentSelect) studentSelect.style.display = 'none';

    const myUser = (acc.username || '').toLowerCase();
    const myName = (acc.studentName || '').toLowerCase();
    historyList = allHistory.filter(r => {
      const rUser = (r.username || '').toLowerCase();
      const rName = (r.studentName || '').toLowerCase();
      return (rUser && rUser === myUser) || (rName && rName === myName) || (myName && rName.includes(myName));
    });
  } else {
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
  }

  // 2. BỘ LỌC TÌM KIẾM, SỐ CÂU, ĐỘ KHÓ, MỨC ĐIỂM
  const searchInput = document.getElementById('history-search');
  const filterSize = document.getElementById('history-filter-size');
  const filterDiff = document.getElementById('history-filter-diff');
  const filterLevel = document.getElementById('history-filter-level');

  const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
  const sizeVal = filterSize ? filterSize.value : 'all';
  const diffVal = filterDiff ? filterDiff.value : 'all';
  const levelVal = filterLevel ? filterLevel.value : 'all';

  // Cập nhật Dashboard tổng quan (THEO PHÂN QUYỀN ĐÃ LỌC)
  const totalTests = historyList.length;
  document.getElementById('hist-total-tests').textContent = totalTests;

  if (totalTests > 0) {
    const sumScore = historyList.reduce((acc, r) => acc + (r.score10 || 0), 0);
    const avgScore = (sumScore / totalTests).toFixed(1);
    const sumPct = historyList.reduce((acc, r) => acc + (r.pct || 0), 0);
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
    tbody.innerHTML = `<tr><td colspan="11" style="text-align:center; padding:24px; color:#64748B;">
      ${totalTests === 0 ? 'Chưa có bài thi nào thuộc tài khoản này. Hãy bắt đầu một bài thi nhé!' : 'Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.'}
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
        <button class="btn-source-action" onclick="viewHistoryDetail('${r.id}')" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-size:0.78rem; padding:4px 10px; font-weight:800; white-space:nowrap;">
          🔍 Xem lại
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

"""
    content = content[:pos_rh] + new_render_history + content[pos_rh_end:]
    print("3. Replaced renderHistoryTable() with strict Role-based Access Control.")
else:
    print("WARNING: renderHistoryTable range not found!")

# 4. UPDATE window.onload TO INITIALIZE MASCOTS AND ADMIN UI
old_onload = """window.onload = function() {
  initMasterPool();
  renderSourceChips();
  renderTopics();
  loadSavedSettings();
  updatePoolCountDisplay();
};"""

new_onload = """window.onload = function() {
  initMasterPool();
  renderSourceChips();
  renderTopics();
  loadSavedSettings();
  updatePoolCountDisplay();
  updateHeaderAuthDisplay();
  updateAdminHeaderUI();
  updateAllMascotsUI();
};"""

if old_onload in content:
    content = content.replace(old_onload, new_onload, 1)
    print("4. Updated window.onload to initialize mascots and admin UI.")
else:
    print("WARNING: old_onload not found!")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html fully upgraded with Role-Based Access Control and ChessKid mascots!")
