#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. REPLACE QUIZ SCREEN MASCOT
pos = content.find('class="mascot-container"')
if pos != -1:
    pos2 = content.find('<!-- HÌNH ẢNH CHUẨN XÁC', pos)
    old_mascot_block = content[pos:pos2]
    new_mascot_block = """class="mascot-container mascot-interactive" onclick="onMascotClick()" title="Bấm vào tớ để nghe sự thật khoa học kỳ thú!">
          <div id="quiz-mascot-svg-wrap" class="mascot-avatar" style="display:flex; align-items:center; justify-content:center;"></div>
          <div class="mascot-bubble" id="mascot-speech">Bé đọc kỹ câu hỏi nhé, chúng mình cùng nhau đạt điểm 10 nào! 🌟</div>
        </div>

        """
    content = content[:pos] + new_mascot_block + content[pos2:]
    print("1. Replaced quiz mascot block with interactive dynamic wrap.")

# 2. INSERT COMPLETE JAVASCRIPT LOGIC BEFORE </script>
js_code = """
// =========================================================================
// HỆ THỐNG 5 BẠN ĐỒNG HÀNH KHOA HỌC (CHESSKID STYLE) & HIỆU ỨNG ÂM THANH
// =========================================================================
const MASCOTS = [
  {
    id: 'hoot',
    name: 'Giáo Sư Cú Vọ',
    title: 'Bác Học Thông Thái',
    color: '#4361EE',
    desc: 'Bậc thầy lý luận khoa học, luôn yêu thích hiện tượng tự nhiên và giải thích chi tiết!',
    avatar: '🦉'
  },
  {
    id: 'robosci',
    name: 'Bé Rô-Bốt Sci-Bot',
    title: 'Siêu Trí Tuệ AI',
    color: '#06D6A0',
    desc: 'Người bạn công nghệ đáng yêu với đôi mắt LED biểu cảm và ăng-ten bắt sóng!',
    avatar: '🤖'
  },
  {
    id: 'dino',
    name: 'Khủng Long Dino',
    title: 'Thám Hiểm Sinh Thái',
    color: '#10B981',
    desc: 'Chú khủng long mũ tai bèo dũng cảm, am hiểu muôn loài động thực vật trên Trái Đất!',
    avatar: '🦖'
  },
  {
    id: 'astrocat',
    name: 'Mèo Kitty Astro',
    title: 'Phi Hành Gia Vũ Trụ',
    color: '#8B5CF6',
    desc: 'Cô mèo du hành vũ trụ, thích ngắm các hành tinh, Mặt Trời và dải ngân hà rực rỡ!',
    avatar: '🐱'
  },
  {
    id: 'foxie',
    name: 'Cáo Nhỏ Foxie',
    title: 'Thám Tử Khoa Học',
    color: '#F97316',
    desc: 'Nhanh nhẹn, mắt sáng, luôn mang theo kính lúp để quan sát các thí nghiệm kỳ thú!',
    avatar: '🦊'
  }
];

let currentMascotId = localStorage.getItem('science_quiz_mascot_id') || 'hoot';

function renderMascotSvg(id, size = 64, mood = 'happy') {
  if (id === 'robosci') {
    return `
      <svg viewBox="0 0 100 100" style="width:${size}px; height:${size}px;">
        <rect x="20" y="26" width="60" height="52" rx="16" fill="#06D6A0" stroke="#059669" stroke-width="3"/>
        <line x1="50" y1="26" x2="50" y2="12" stroke="#059669" stroke-width="4"/>
        <circle cx="50" cy="10" r="6" fill="#FBBF24" stroke="#D97706" stroke-width="2"/>
        <rect x="28" y="38" width="44" height="24" rx="8" fill="#0F172A"/>
        <circle cx="39" cy="50" r="5" fill="#38BDF8"/>
        <circle cx="61" cy="50" r="5" fill="#38BDF8"/>
        <circle cx="41" cy="48" r="2" fill="white"/>
        <circle cx="63" cy="48" r="2" fill="white"/>
        <path d="M42 68 Q50 74 58 68" stroke="#0F172A" stroke-width="3" stroke-linecap="round" fill="none"/>
        <circle cx="15" cy="52" r="5" fill="#34D399"/>
        <circle cx="85" cy="52" r="5" fill="#34D399"/>
      </svg>
    `;
  }
  if (id === 'dino') {
    return `
      <svg viewBox="0 0 100 100" style="width:${size}px; height:${size}px;">
        <circle cx="50" cy="52" r="38" fill="#10B981" stroke="#047857" stroke-width="3"/>
        <!-- Mũ thám hiểm -->
        <path d="M22 36 Q50 18 78 36" fill="#D97706" stroke="#92400E" stroke-width="3"/>
        <ellipse cx="50" cy="36" rx="34" ry="7" fill="#F59E0B" stroke="#92400E" stroke-width="2"/>
        <ellipse cx="38" cy="52" rx="5" ry="7" fill="#0F172A"/>
        <ellipse cx="62" cy="52" rx="5" ry="7" fill="#0F172A"/>
        <circle cx="40" cy="49" r="2" fill="white"/>
        <circle cx="64" cy="49" r="2" fill="white"/>
        <ellipse cx="28" cy="58" rx="5" ry="3" fill="#F87171" opacity="0.6"/>
        <ellipse cx="72" cy="58" rx="5" ry="3" fill="#F87171" opacity="0.6"/>
        <path d="M42 66 Q50 76 58 66" stroke="#047857" stroke-width="3" stroke-linecap="round" fill="none"/>
      </svg>
    `;
  }
  if (id === 'astrocat') {
    return `
      <svg viewBox="0 0 100 100" style="width:${size}px; height:${size}px;">
        <!-- Mũ bảo hiểm vũ trụ -->
        <circle cx="50" cy="50" r="42" fill="#F1F5F9" stroke="#94A3B8" stroke-width="3"/>
        <!-- Tai mèo -->
        <polygon points="26,30 38,15 44,30" fill="#F472B6" stroke="#DB2777" stroke-width="2"/>
        <polygon points="74,30 62,15 56,30" fill="#F472B6" stroke="#DB2777" stroke-width="2"/>
        <!-- Mặt mèo -->
        <circle cx="50" cy="52" r="28" fill="white"/>
        <ellipse cx="40" cy="49" rx="4" ry="6" fill="#1E293B"/>
        <ellipse cx="60" cy="49" rx="4" ry="6" fill="#1E293B"/>
        <circle cx="41" cy="47" r="1.5" fill="white"/>
        <circle cx="61" cy="47" r="1.5" fill="white"/>
        <polygon points="50,56 47,59 53,59" fill="#F43F5E"/>
        <path d="M46 62 Q50 65 54 62" stroke="#475569" stroke-width="2" fill="none"/>
        <!-- Ánh bóng kính phi hành -->
        <path d="M22 36 A36 36 0 0 1 78 36" stroke="white" stroke-width="3" fill="none" opacity="0.8"/>
      </svg>
    `;
  }
  if (id === 'foxie') {
    return `
      <svg viewBox="0 0 100 100" style="width:${size}px; height:${size}px;">
        <polygon points="20,44 26,16 46,34" fill="#EA580C" stroke="#C2410C" stroke-width="2"/>
        <polygon points="80,44 74,16 54,34" fill="#EA580C" stroke="#C2410C" stroke-width="2"/>
        <polygon points="26,40 29,22 42,34" fill="#FED7AA"/>
        <polygon points="74,40 71,22 58,34" fill="#FED7AA"/>
        <!-- Đầu cáo -->
        <polygon points="18,48 50,82 82,48 50,32" fill="#F97316"/>
        <polygon points="18,48 50,82 35,55" fill="white"/>
        <polygon points="82,48 50,82 65,55" fill="white"/>
        <circle cx="36" cy="48" r="4.5" fill="#1E293B"/>
        <circle cx="64" cy="48" r="4.5" fill="#1E293B"/>
        <circle cx="37" cy="46" r="1.5" fill="white"/>
        <circle cx="65" cy="46" r="1.5" fill="white"/>
        <circle cx="50" cy="74" r="4" fill="#1E293B"/>
      </svg>
    `;
  }
  // Mặc định: Giáo Sư Cú Vọ (Hoot)
  return `
    <svg viewBox="0 0 100 100" style="width:${size}px; height:${size}px;">
      <ellipse cx="50" cy="54" rx="38" ry="36" fill="#3A0CA3" stroke="#4361EE" stroke-width="3"/>
      <!-- Mũ cử nhân -->
      <polygon points="50,10 86,22 50,34 14,22" fill="#1E1B4B" stroke="#4361EE" stroke-width="2"/>
      <circle cx="50" cy="22" r="3.5" fill="#FBBF24"/>
      <line x1="50" y1="22" x2="78" y2="30" stroke="#FBBF24" stroke-width="2.5"/>
      <!-- Kính mắt to tròn bác học -->
      <circle cx="38" cy="50" r="13" fill="#EEF2FF" stroke="#FBBF24" stroke-width="3.5"/>
      <circle cx="62" cy="50" r="13" fill="#EEF2FF" stroke="#FBBF24" stroke-width="3.5"/>
      <line x1="51" y1="50" x2="49" y2="50" stroke="#FBBF24" stroke-width="3.5"/>
      <circle cx="38" cy="50" r="5" fill="#1E1B4B"/>
      <circle cx="62" cy="50" r="5" fill="#1E1B4B"/>
      <circle cx="39" cy="48" r="1.8" fill="white"/>
      <circle cx="63" cy="48" r="1.8" fill="white"/>
      <!-- Mỏ cú -->
      <polygon points="50,56 45,67 55,67" fill="#F59E0B"/>
      <!-- Nơ cổ -->
      <polygon points="44,78 56,78 50,82" fill="#EF4444"/>
    </svg>
  `;
}

// BỘ TỔNG HỢP ÂM THANH WEB AUDIO API (KHÔNG CẦN FILE AUDIO NGOÀI, SIÊU MƯỢT)
let kidAudioCtx = null;
function getKidAudioCtx() {
  if (!kidAudioCtx) {
    const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
    kidAudioCtx = new AudioCtxClass();
  }
  if (kidAudioCtx.state === 'suspended') {
    kidAudioCtx.resume();
  }
  return kidAudioCtx;
}

function playKidSound(type) {
  try {
    const ctx = getKidAudioCtx();
    const now = ctx.currentTime;
    if (type === 'click') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(480, now);
      osc.frequency.exponentialRampToValueAtTime(800, now + 0.08);
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.08);
    } else if (type === 'correct') {
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, now + idx * 0.06);
        gain.gain.setValueAtTime(0.18, now + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.06 + 0.22);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + idx * 0.06);
        osc.stop(now + idx * 0.06 + 0.22);
      });
    } else if (type === 'wrong') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(320, now);
      osc.frequency.exponentialRampToValueAtTime(220, now + 0.25);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.25);
    } else if (type === 'fanfare') {
      const melody = [
        { f: 523.25, t: 0, d: 0.12 },
        { f: 659.25, t: 0.12, d: 0.12 },
        { f: 783.99, t: 0.24, d: 0.12 },
        { f: 1046.50, t: 0.36, d: 0.4 }
      ];
      melody.forEach(n => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(n.f, now + n.t);
        gain.gain.setValueAtTime(0.22, now + n.t);
        gain.gain.exponentialRampToValueAtTime(0.01, now + n.t + n.d);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + n.t);
        osc.stop(now + n.t + n.d);
      });
    }
  } catch(err) {
    // Audio context may require user interaction
  }
}

// BÍ MẬT KHOA HỌC KỲ THÚ DÀNH CHO BÉ KHI BẤM VÀO MASCOT
const SCIENCE_FACTS = [
  "Bé có biết: Trái tim của tôm nằm ở trên đầu của nó không? 🦐",
  "Bé có biết: Bạch tuộc có tới 3 trái tim và máu của chúng có màu xanh lam! 🐙",
  "Bé có biết: Mặt Trời to gấp 1.300.000 lần Trái Đất của chúng ta! ☀️",
  "Bé có biết: Chuột túi Kangaroo không thể đi lùi được! 🦘",
  "Bé có biết: Cây tre có thể mọc cao gần 1 mét chỉ trong một ngày! 🎋",
  "Bé có biết: Ong mật vỗ cánh tới 200 lần mỗi giây để bay đó! 🐝",
  "Bé có biết: Thác nước sâu nhất lại nằm dưới đáy biển đại dương! 🌊",
  "Bé có biết: Sao Kim là hành tinh nóng nhất trong Hệ Mặt Trời! 🪐",
  "Bé có biết: Da của loài gấu Bắc Cực thực chất có màu đen kịt để giữ nhiệt! 🐻‍❄️",
  "Bé có biết: Chim ruồi là loài chim duy nhất có thể bay lùi về phía sau! 🐦"
];

function onMascotClick() {
  playKidSound('click');
  const fact = SCIENCE_FACTS[Math.floor(Math.random() * SCIENCE_FACTS.length)];
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  const bubble = document.getElementById('mascot-speech');
  if (bubble) {
    bubble.innerHTML = `<strong>💡 ${m.name} mách bạn:</strong><br>${fact}`;
  }
}

function updateAllMascotsUI() {
  const m = MASCOTS.find(x => x.id === currentMascotId) || MASCOTS[0];
  const welcomeSvgWrap = document.getElementById('welcome-mascot-svg-wrap');
  if (welcomeSvgWrap) welcomeSvgWrap.innerHTML = renderMascotSvg(m.id, 75);
  const welcomeName = document.getElementById('welcome-mascot-name');
  if (welcomeName) welcomeName.textContent = m.name;

  const quizSvgWrap = document.getElementById('quiz-mascot-svg-wrap');
  if (quizSvgWrap) quizSvgWrap.innerHTML = renderMascotSvg(m.id, 52);
}

function openMascotPickerModal() {
  playKidSound('click');
  const modal = document.getElementById('modal-mascot-picker');
  const grid = document.getElementById('mascot-picker-grid');
  if (grid) {
    grid.innerHTML = MASCOTS.map(m => `
      <div class="mascot-card ${m.id === currentMascotId ? 'active' : ''}" onclick="selectMascot('${m.id}')">
        <div class="mascot-card-svg">${renderMascotSvg(m.id, 64)}</div>
        <div class="mascot-card-name">${m.name}</div>
        <div class="mascot-card-title">${m.title}</div>
      </div>
    `).join('');
  }
  if (modal) modal.classList.add('active');
}

function selectMascot(id) {
  playKidSound('click');
  currentMascotId = id;
  localStorage.setItem('science_quiz_mascot_id', id);
  updateAllMascotsUI();
  openMascotPickerModal(); // Re-render active state
}

function closeMascotPickerModal() {
  const modal = document.getElementById('modal-mascot-picker');
  if (modal) modal.classList.remove('active');
}


// =========================================================================
// PHÂN QUYỀN ADMIN (ROLE-BASED ACCESS CONTROL) & QUẢN LÝ USER
// =========================================================================
function isAdmin() {
  const acc = getStoredAccount();
  return !!(acc && (acc.username === 'admin' || acc.role === 'admin'));
}

// BẬT / TẮT HIỂN THỊ MENU VÀ NÚT QUẢN TRỊ VIÊN
function updateAdminHeaderUI() {
  const adminBtn = document.getElementById('btn-header-user-mgmt');
  const isAdm = isAdmin();
  if (adminBtn) {
    if (isAdm) {
      adminBtn.style.display = 'inline-flex';
      adminBtn.style.background = '#FEF2F2';
      adminBtn.style.borderColor = '#FCA5A5';
      adminBtn.style.color = '#B91C1C';
    } else {
      // Vẫn cho phép bấm vào để mở hộp thoại nhập pass Admin
      adminBtn.style.display = 'inline-flex';
    }
  }
}

// MỞ QUẢN LÝ USER DÀNH CHO ADMIN
function openUserManagementModal() {
  playKidSound('click');
  if (!isAdmin()) {
    const pass = prompt('👑 Khu vực Quản Trị Viên (Admin).\\nVui lòng nhập Mật khẩu Admin:');
    if (pass === '11081993') {
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
      alert('✅ Xác thực Admin thành công! Chào mừng Quản trị viên.');
    } else {
      if (pass !== null) alert('❌ Mật khẩu Quản trị viên không chính xác!');
      return;
    }
  }

  const modal = document.getElementById('modal-user-management');
  if (modal) modal.classList.add('active');
  renderUserManagementTable();
  fetchUsersFromCloud();
}

function closeUserManagementModal() {
  const modal = document.getElementById('modal-user-management');
  if (modal) modal.classList.remove('active');
}

// TỔNG HỢP DANH SÁCH USER TỪ TẤT CẢ NGUỒN (LỊCH SỬ THI + TAI_KHOAN)
let cachedUsersList = [];

function getAllUsersAggregated() {
  const userMap = {};
  
  // 1. Từ tài khoản hiện hành
  const currentAcc = getStoredAccount();
  if (currentAcc && currentAcc.username && currentAcc.username !== 'admin') {
    userMap[currentAcc.username.toLowerCase()] = {
      registeredAt: '14/11/2026',
      username: currentAcc.username,
      name: currentAcc.studentName || currentAcc.username,
      studentClass: currentAcc.studentClass || 'Lớp 2',
      totalTests: currentAcc.totalTests || 0,
      highestScore: currentAcc.highestScore || 0,
      badge: currentAcc.badge || '🌱 Tân Binh'
    };
  }

  // 2. Quét từ toàn bộ lịch sử thi đã thực hiện
  const historyList = getLocalHistory();
  historyList.forEach(r => {
    const name = (r.studentName || 'Học sinh').trim();
    if (name && name !== 'Học sinh' && name !== 'Quản Trị Viên (Admin)') {
      const uKey = (r.username || name).toLowerCase();
      if (!userMap[uKey]) {
        userMap[uKey] = {
          registeredAt: r.quizDate || '14/11/2026',
          username: r.username || uKey.replace(/\\s+/g, ''),
          name: name,
          studentClass: r.studentClass || 'Lớp 2',
          totalTests: 0,
          highestScore: 0,
          badge: '🌱 Tân Binh'
        };
      }
      userMap[uKey].totalTests++;
      const scoreNum = parseFloat(String(r.score10 || r.score || '0').split('/')[0]) || 0;
      userMap[uKey].highestScore = Math.max(userMap[uKey].highestScore, scoreNum);
      if (userMap[uKey].highestScore >= 9.5) userMap[uKey].badge = '👑 Đại Kiện Tướng';
      else if (userMap[uKey].highestScore >= 8.5) userMap[uKey].badge = '🥇 Học Sinh Xuất Sắc';
      else if (userMap[uKey].highestScore >= 7.0) userMap[uKey].badge = '🥈 Ong Chăm Chỉ';
    }
  });

  // 3. Gộp với cache từ cloud (nếu có)
  cachedUsersList.forEach(u => {
    const key = (u.username || u.name).toLowerCase();
    if (!userMap[key]) {
      userMap[key] = u;
    } else {
      userMap[key].totalTests = Math.max(userMap[key].totalTests, u.totalTests || 0);
      userMap[key].highestScore = Math.max(userMap[key].highestScore, u.highestScore || 0);
    }
  });

  return Object.values(userMap);
}

function renderUserManagementTable() {
  const users = getAllUsersAggregated();
  const searchInput = document.getElementById('mgmt-search-input');
  const filterClass = document.getElementById('mgmt-filter-class');
  const search = searchInput ? searchInput.value.toLowerCase().trim() : '';
  const cVal = filterClass ? filterClass.value : 'all';

  // Thống kê tổng quan
  const totalUsers = users.length;
  const totalTests = users.reduce((acc, u) => acc + (u.totalTests || 0), 0);
  const maxScore = users.length > 0 ? Math.max(...users.map(u => u.highestScore || 0)).toFixed(1) : '0.0';
  let mostActive = users.length > 0 ? [...users].sort((a,b) => (b.totalTests||0) - (a.totalTests||0))[0] : null;

  document.getElementById('mgmt-stat-users').textContent = totalUsers;
  document.getElementById('mgmt-stat-tests').textContent = totalTests;
  document.getElementById('mgmt-stat-high').textContent = `${maxScore}/10`;
  document.getElementById('mgmt-stat-active').textContent = mostActive ? `${mostActive.name} (${mostActive.totalTests} bài)` : 'Chưa có';

  // Lọc theo search và lớp
  const filtered = users.filter(u => {
    if (search && !u.name.toLowerCase().includes(search) && !u.username.toLowerCase().includes(search)) return false;
    if (cVal !== 'all' && !String(u.studentClass).includes(cVal)) return false;
    return true;
  });

  const tbody = document.getElementById('user-mgmt-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding:24px; color:#64748B;">Không tìm thấy người dùng nào phù hợp.</td></tr>`;
    return;
  }

  filtered.forEach((u, idx) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td style="text-align:center; font-size:1.25rem;">🦁</td>
      <td style="font-family:monospace; font-weight:700; color:var(--primary); font-size:0.82rem;">@${u.username}</td>
      <td style="font-weight:700; color:var(--dark);">${u.name}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${u.studentClass || 'Lớp 2'}</span></td>
      <td style="color:#64748B; font-size:0.8rem;">${u.registeredAt || '14/11/2026'}</td>
      <td style="text-align:center; font-weight:700; color:#1E40AF;">${u.totalTests || 0} bài</td>
      <td style="text-align:center; font-weight:800; color:#047857;">${u.highestScore || 0}/10</td>
      <td><span style="font-size:0.8rem; font-weight:700;">${u.badge || '🌱 Tân Binh'}</span></td>
      <td style="text-align:center;">
        <button class="btn-source-action" onclick="viewStudentHistoryFromMgmt('${u.name}')" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-size:0.75rem; padding:3px 8px; font-weight:800;" title="Xem các bài thi của học sinh này">
          🔍 Xem bài thi
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function viewStudentHistoryFromMgmt(studentName) {
  closeUserManagementModal();
  openHistoryScreen();
  const select = document.getElementById('history-filter-student');
  if (select) {
    select.value = studentName;
    renderHistoryTable();
  }
}

function fetchUsersFromCloud() {
  const scriptUrl = document.getElementById('apps-script-url') ? document.getElementById('apps-script-url').value.trim() : (typeof GOOGLE_SCRIPT_URL !== 'undefined' ? GOOGLE_SCRIPT_URL : '');
  if (!scriptUrl) return;

  fetch(`${scriptUrl}?action=getUsers`)
    .then(r => r.json())
    .then(data => {
      if (data && data.users) {
        cachedUsersList = data.users;
        renderUserManagementTable();
      }
    })
    .catch(err => console.log('Fetch cloud users note', err));
}
"""

pos_script = content.rfind('</script>')
if pos_script != -1:
    content = content[:pos_script] + "\n" + js_code + "\n" + content[pos_script:]
    print("2. Appended Mascots, Sound Synthesizer & Admin JS code.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html fully updated!")
