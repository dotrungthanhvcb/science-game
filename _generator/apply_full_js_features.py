# -*- coding: utf-8 -*-
"""
Script cập nhật logic JS trong index.html:
- Loại bỏ triệt để thông báo đúng/sai và mascot khen sớm ở từng câu
- 4 chế độ nhạc nền tập trung (Lofi, Piano, Baroque Alpha, Upbeat)
- Thang nhận xét điểm số 5 bậc chuẩn xác
- Tính năng Lưu, Tìm kiếm, Lọc và Thống kê Lịch sử bài thi
"""
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# =========================================================================
# THAY THẾ BỘ MÁY NHẠC NỀN CŨ BẰNG HỆ THỐNG 4 BẢN NHẠC TẬP TRUNG
# =========================================================================
NEW_MUSIC_ENGINE = """
// =========================================================================
// HỆ THỐNG 4 BẢN NHẠC NỀN TẬP TRUNG KHI HỌC / LÀM BÀI THI (WEB AUDIO API)
// =========================================================================
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
let isMusicPlaying = false;
let musicStep = 0;
let musicTimer = null;
let currentMusicTrack = 'lofi'; // lofi | piano | baroque | upbeat

// 1. TRACK LOFI CHILL FOCUS (60 BPM - Thư giãn, chống mỏi mệt)
const lofiChords = [
  [349.23, 440.00, 523.25, 659.25], // Fmaj7
  [329.63, 392.00, 493.88, 587.33], // Em7
  [293.66, 349.23, 440.00, 523.25], // Dm7
  [261.63, 329.63, 392.00, 493.88]  // Cmaj7
];
const lofiBass = [174.61, 164.81, 146.83, 130.81];

// 2. TRACK PIANO MOZART FOCUS (Cổ điển trong trẻo, kích thích tư duy)
const pianoNotes = [
  523.25, 659.25, 783.99, 1046.50, 783.99, 659.25,
  587.33, 698.46, 880.00, 1174.66, 880.00, 698.46,
  493.88, 587.33, 783.99, 987.77,  783.99, 587.33,
  523.25, 659.25, 783.99, 1046.50, 783.99, 659.25
];

// 3. TRACK BAROQUE ALPHA FLOW (60 BPM - Kích hoạt sóng não Alpha)
const baroqueArp = [
  261.63, 329.63, 392.00, 523.25, 392.00, 329.63,
  220.00, 261.63, 329.63, 440.00, 329.63, 261.63,
  174.61, 220.00, 261.63, 349.23, 261.63, 220.00,
  196.00, 246.94, 293.66, 392.00, 293.66, 246.94
];

// 4. TRACK UPBEAT GAME SHOW (128 BPM - Hào hứng, phản xạ nhanh)
const upbeatMelody = [
  587.33, 0, 587.33, 659.25, 698.46, 0, 659.25, 587.33,
  523.25, 0, 523.25, 587.33, 659.25, 0, 587.33, 523.25,
  466.16, 0, 466.16, 523.25, 587.33, 0, 523.25, 466.16,
  440.00, 523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 0
];
const upbeatBass = [146.83, 146.83, 116.54, 116.54, 130.81, 130.81, 146.83, 146.83];

function changeMusicTrack(trackKey) {
  currentMusicTrack = trackKey;
  if (isMusicPlaying) {
    stopMusic();
    playMusic();
  }
}

function toggleMusic() {
  if (isMusicPlaying) {
    stopMusic();
  } else {
    playMusic();
  }
}

function playMusic() {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    isMusicPlaying = true;
    const btn = document.getElementById('music-btn');
    if (btn) {
      btn.classList.add('playing');
      btn.innerHTML = '<span>⏸️</span><span>Tắt Nhạc</span>';
    }

    musicStep = 0;
    // Chu kỳ nhịp theo từng thể loại
    let intervalMs = 250;
    if (currentMusicTrack === 'upbeat') intervalMs = 125;
    else if (currentMusicTrack === 'lofi') intervalMs = 300;
    else if (currentMusicTrack === 'piano') intervalMs = 220;
    else if (currentMusicTrack === 'baroque') intervalMs = 260;

    musicTimer = setInterval(() => {
      if (!isMusicPlaying) return;
      playTrackStep();
    }, intervalMs);
  } catch(e) {
    console.log('Audio init note', e);
  }
}

function stopMusic() {
  isMusicPlaying = false;
  clearInterval(musicTimer);
  const btn = document.getElementById('music-btn');
  if (btn) {
    btn.classList.remove('playing');
    btn.innerHTML = '<span>🎵</span><span>Bật Nhạc</span>';
  }
}

function playTrackStep() {
  const now = audioCtx.currentTime;

  if (currentMusicTrack === 'lofi') {
    // LOFI: Pad hợp âm ấm áp + bass mượt mà
    if (musicStep % 4 === 0) {
      const chordIdx = Math.floor(musicStep / 4) % lofiChords.length;
      const chord = lofiChords[chordIdx];
      chord.forEach(freq => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now);
        gain.gain.setValueAtTime(0.012, now);
        gain.gain.exponentialRampToValueAtTime(0.0005, now + 1.1);
        osc.start(now);
        osc.stop(now + 1.15);
      });
      // Bass ấm
      const bOsc = audioCtx.createOscillator();
      const bGain = audioCtx.createGain();
      bOsc.connect(bGain);
      bGain.connect(audioCtx.destination);
      bOsc.type = 'triangle';
      bOsc.frequency.setValueAtTime(lofiBass[chordIdx], now);
      bGain.gain.setValueAtTime(0.035, now);
      bGain.gain.exponentialRampToValueAtTime(0.001, now + 1.1);
      bOsc.start(now);
      bOsc.stop(now + 1.15);
    }
  } else if (currentMusicTrack === 'piano') {
    // PIANO CỔ ĐIỂN: Nốt piano arpeggio thanh thoát
    const pNote = pianoNotes[musicStep % pianoNotes.length];
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(pNote, now);
    gain.gain.setValueAtTime(0.03, now);
    gain.gain.exponentialRampToValueAtTime(0.0005, now + 0.65);
    osc.start(now);
    osc.stop(now + 0.7);
  } else if (currentMusicTrack === 'baroque') {
    // BAROQUE SÓNG NÃO: Giai điệu mượt mà 60 BPM
    const bNote = baroqueArp[musicStep % baroqueArp.length];
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.type = 'sine';
    osc.frequency.setValueAtTime(bNote, now);
    gain.gain.setValueAtTime(0.025, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
    osc.start(now);
    osc.stop(now + 0.55);
  } else {
    // UPBEAT GAME SHOW
    if (musicStep % 2 === 0) {
      const bIdx = Math.floor(musicStep / 2) % upbeatBass.length;
      const bOsc = audioCtx.createOscillator();
      const bGain = audioCtx.createGain();
      bOsc.connect(bGain);
      bGain.connect(audioCtx.destination);
      bOsc.type = 'sawtooth';
      bOsc.frequency.setValueAtTime(upbeatBass[bIdx], now);
      bGain.gain.setValueAtTime(0.03, now);
      bGain.gain.exponentialRampToValueAtTime(0.001, now + 0.18);
      bOsc.start(now);
      bOsc.stop(now + 0.2);
    }
    const note = upbeatMelody[musicStep % upbeatMelody.length];
    if (note > 0) {
      const sOsc = audioCtx.createOscillator();
      const sGain = audioCtx.createGain();
      sOsc.connect(sGain);
      sGain.connect(audioCtx.destination);
      sOsc.type = 'square';
      sOsc.frequency.setValueAtTime(note, now);
      sGain.gain.setValueAtTime(0.02, now);
      sGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.12);
      sOsc.start(now);
      sOsc.stop(now + 0.14);
    }
  }

  musicStep++;
}
"""

# Tìm khối code nhạc cũ và thay thế
pattern_music = r'// =========================================================================\s*// BẢN NHẠC GAME SHOW QUIZ[\s\S]*?function stopMusic\(\)\s*\{[\s\S]*?\}'
match_music = re.search(pattern_music, html)
if match_music:
    html = html[:match_music.start()] + NEW_MUSIC_ENGINE.strip() + html[match_music.end():]
    print("✅ Đã nâng cấp hệ thống 4 bản nhạc nền thành công!")

# =========================================================================
# THAY THẾ MASCOT MOOD: LOẠI BỎ TRIỆT ĐỂ KHEN SỚM ĐÚNG/SAI
# =========================================================================
NEW_MASCOT_CODE = """
// =========================================================================
// LINH VẬT BO BO - ĐỒNG HÀNH TRUNG TÍNH (KHÔNG LỘ ĐÚNG/SAI TRƯỚC KHI NỘP)
// =========================================================================
function setMascotMood(mood, customText) {
  const bubble = document.getElementById('mascot-speech');
  const mouth = document.getElementById('mascot-mouth');
  if (!bubble || !mouth) return;

  if (mood === 'thinking') {
    mouth.setAttribute('d', 'M42 62 Q50 68 58 62');
    bubble.textContent = customText || 'Bé đọc kỹ câu hỏi nhé, Bo Bo tin bé làm được! 🌟';
  } else if (mood === 'selected' || (mood === 'happy' && !isQuizSubmitted)) {
    // Khi đang làm bài thi: Phản hồi trung tính ghi nhận lựa chọn, KHÔNG lộ đúng/sai
    mouth.setAttribute('d', 'M40 60 Q50 70 60 60');
    const neutralMessages = [
      'Đã ghi nhận đáp án! Bé có thể sửa lại hoặc sang câu tiếp theo nhé. 📝',
      'Lựa chọn đã được lưu! Bé hãy tự tin làm tiếp câu sau nào. 🌟',
      'Bé đã chọn xong! Cứ bình tĩnh suy nghĩ và tiếp tục nhé. 🚀',
      'Câu trả lời đã lưu tạm thời. Nộp bài xong mới biết kết quả bé nhé! 💡'
    ];
    bubble.textContent = customText || neutralMessages[Math.floor(Math.random() * neutralMessages.length)];
  } else if (mood === 'finished') {
    // Sau khi đã nộp bài chính thức
    mouth.setAttribute('d', 'M38 58 Q50 78 62 58');
    bubble.textContent = customText || 'Chúc mừng bé đã hoàn thành bài thi hôm nay! 🎉';
  } else if (mood === 'sad') {
    mouth.setAttribute('d', 'M42 68 Q50 60 58 68');
    bubble.textContent = customText || 'Đừng nản lòng nhé, xem giải thích chi tiết để hiểu sâu hơn nè! 💪';
  }
}
"""

pattern_mascot = r'function setMascotMood\(mood, customText\)\s*\{[\s\S]*?\n\}'
match_mascot = re.search(pattern_mascot, html)
if match_mascot:
    html = html[:match_mascot.start()] + NEW_MASCOT_CODE.strip() + html[match_mascot.end():]
    print("✅ Đã cập nhật Mascot trung tính, loại bỏ hoàn toàn khen sớm!")

# =========================================================================
# CẬP NHẬT THANG NHẬN XÉT ĐIỂM SỐ CHUẨN XÁC + LƯU LỊCH SỬ BÀI THI
# =========================================================================
OLD_SUBMIT_LOGIC = """  // 4. Hiển thị lên màn hình kết quả (result-screen)
  document.getElementById('res-score').textContent = `${score10}/10 (${pct}%)`;
  document.getElementById('res-correct').textContent = `${correctCount}/${total}`;
  const resWrongElem = document.getElementById('res-wrong');
  if (resWrongElem) resWrongElem.textContent = `${wrongCount}/${total}`;
  document.getElementById('res-time').textContent = timeStr;

  let stars = '⭐';
  let icon = '👏';
  let title = 'Cố gắng ở lượt sau nhé!';
  if (pct >= 90) {
    stars = '⭐⭐⭐';
    icon = '🏆';
    title = 'Xuất sắc tuyệt đối!';
    fireConfetti();
    playSound('correct');
  } else if (pct >= 75) {
    stars = '⭐⭐';
    icon = '🎉';
    title = 'Bé làm rất tốt!';
    fireConfetti();
    playSound('correct');
  } else if (pct >= 50) {
    stars = '⭐';
    icon = '💪';
    title = 'Tiến bộ rõ rệt!';
    playSound('correct');
  }

  document.getElementById('res-stars').textContent = stars;
  document.getElementById('res-icon').textContent = icon;
  document.getElementById('res-title').textContent = title;"""

NEW_SUBMIT_LOGIC = """  // 4. Hiển thị lên màn hình kết quả (result-screen)
  document.getElementById('res-score').textContent = `${score10}/10 (${pct}%)`;
  document.getElementById('res-correct').textContent = `${correctCount}/${total}`;
  const resWrongElem = document.getElementById('res-wrong');
  if (resWrongElem) resWrongElem.textContent = `${wrongCount}/${total}`;
  document.getElementById('res-time').textContent = timeStr;

  // THANG ĐÁNH GIÁ 5 BẬC SƯ PHẠM CHUẨN XÁC
  let stars = '⭐';
  let icon = '👏';
  let title = '';
  let desc = '';

  if (pct >= 90) {
    // 9.0 - 10.0: Xuất sắc
    stars = '⭐⭐⭐';
    icon = '🏆';
    title = 'Xuất sắc tuyệt đối!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Tư duy khoa học và phản xạ cực kỳ vượt trội!`;
    fireConfetti();
    playSound('correct');
    setMascotMood('finished', 'Bé đạt điểm xuất sắc tuyệt đối luôn, Bo Bo tự hào về bé quá! 🏆');
  } else if (pct >= 80) {
    // 8.0 - 8.9: Rất tốt
    stars = '⭐⭐';
    icon = '🎉';
    title = 'Làm bài rất tốt!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Bé nắm rất vững kiến thức, chỉ cần cẩn thận một vài câu nữa là đạt điểm tối đa!`;
    fireConfetti();
    playSound('correct');
    setMascotMood('finished', 'Bé làm bài rất tốt! Cùng giữ vững phong độ này nhé! 🎉');
  } else if (pct >= 65) {
    // 6.5 - 7.9: Khá tốt
    stars = '⭐';
    icon = '👍';
    title = 'Kết quả Khá tốt!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu), trên mức trung bình. Hãy xem lại phần giải thích các câu sai để nhớ sâu hơn nhé!`;
    playSound('correct');
    setMascotMood('finished', 'Bé đạt kết quả khá tốt trên trung bình rồi đó! Xem lại câu sai để tiến bộ nha! 👍');
  } else if (pct >= 50) {
    // 5.0 - 6.4: Trung bình (Cần cố gắng, không khen quá mức)
    stars = '🌱';
    icon = '📖';
    title = 'Mức Trung Bình - Cần ôn luyện thêm!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu). Bé đã đạt mức trung bình, nhưng cần xem kỹ lời giải thích của các câu sai để hiểu bài hơn nhé!`;
    setMascotMood('finished', 'Bé mới đạt mức trung bình thôi nè, hãy xem kỹ lời giải thích chi tiết để ôn lại nhé! 📖');
  } else {
    // Dưới 50% (< 5.0): Chưa đạt
    stars = '💪';
    icon = '⚡';
    title = 'Chưa đạt yêu cầu - Đừng nản lòng nhé!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu, chưa đạt mức trung bình). Đừng buồn nhé, hãy bấm "Xem lại chi tiết" để học lại đáp án đúng và thi lại lượt mới nào!`;
    setMascotMood('sad', 'Lượt này chưa đạt điểm trung bình rồi, nhưng không sao, hãy xem giải thích để hiểu bài rồi thi lại nhé! 💪');
  }

  document.getElementById('res-stars').textContent = stars;
  document.getElementById('res-icon').textContent = icon;
  document.getElementById('res-title').textContent = title;
  const resDescElem = document.getElementById('res-desc');
  if (resDescElem) resDescElem.textContent = desc;

  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (LOCALSTORAGE)
  saveQuizToLocalHistory({
    id: 'REC_' + Date.now(),
    timestamp: new Date().toLocaleString('vi-VN'),
    studentName: document.getElementById('user-name').value.trim() || 'Học sinh',
    studentClass: document.getElementById('student-class') ? document.getElementById('student-class').value.trim() : '',
    sources: Array.from(selectedSources).join(', '),
    totalQuestions: total,
    correctCount: correctCount,
    wrongCount: wrongCount,
    score10: parseFloat(score10),
    pct: pct,
    duration: timeStr
  });"""

if OLD_SUBMIT_LOGIC in html:
    html = html.replace(OLD_SUBMIT_LOGIC, NEW_SUBMIT_LOGIC)
    print("✅ Đã cập nhật thang nhận xét điểm số 5 bậc sư phạm chuẩn!")

# =========================================================================
# THÊM CODE QUẢN LÝ LỊCH SỬ BÀI THI & THỐNG KÊ (SEARCH, FILTER, DASHBOARD)
# =========================================================================
HISTORY_JS_CODE = """
// =========================================================================
// QUẢN LÝ LỊCH SỬ BÀI THI & BẢNG THỐNG KÊ (SEARCH, FILTER, DASHBOARD)
// =========================================================================
const HISTORY_STORAGE_KEY = 'science_quiz_history_records';

function getLocalHistory() {
  try {
    const raw = localStorage.getItem(HISTORY_STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch(e) {
    return [];
  }
}

function saveQuizToLocalHistory(record) {
  try {
    const list = getLocalHistory();
    list.unshift(record); // Thêm vào đầu danh sách
    if (list.length > 200) list.pop(); // Giữ tối đa 200 bản ghi gần nhất
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(list));
  } catch(e) {
    console.log('Save history note', e);
  }
}

function openHistoryScreen() {
  renderHistoryTable();
  showScreen('history-screen');
}

function renderHistoryTable() {
  const historyList = getLocalHistory();
  const searchInput = document.getElementById('history-search');
  const filterLevel = document.getElementById('history-filter-level');
  const filterSrc = document.getElementById('history-filter-src');

  const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
  const levelVal = filterLevel ? filterLevel.value : 'all';
  const srcVal = filterSrc ? filterSrc.value : 'all';

  // 1. Cập nhật Dashboard tổng quan
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

  // 2. Lọc danh sách theo Search và Filter
  let filtered = historyList.filter(r => {
    // Search text
    if (searchTerm) {
      const matchName = (r.studentName || '').toLowerCase().includes(searchTerm);
      const matchClass = (r.studentClass || '').toLowerCase().includes(searchTerm);
      const matchSrc = (r.sources || '').toLowerCase().includes(searchTerm);
      if (!matchName && !matchClass && !matchSrc) return false;
    }

    // Filter theo điểm số
    if (levelVal === 'high' && r.score10 < 9.0) return false;
    if (levelVal === 'medium' && (r.score10 < 6.5 || r.score10 >= 9.0)) return false;
    if (levelVal === 'low' && r.score10 >= 6.5) return false;

    // Filter theo nguồn đề
    if (srcVal !== 'all') {
      if (!(r.sources || '').includes(srcVal)) return false;
    }

    return true;
  });

  // 3. Render bảng HTML
  const tbody = document.getElementById('history-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding:24px; color:#64748B;">
      ${totalTests === 0 ? 'Chưa có lượt thi nào được ghi lại. Hãy bắt đầu một bài thi đầu tiên nhé!' : 'Không tìm thấy kết quả nào khớp với bộ lọc tìm kiếm.'}
    </td></tr>`;
    return;
  }

  filtered.forEach((r, idx) => {
    const tr = document.createElement('tr');
    
    let badgeClass = 'medium';
    if (r.score10 >= 8.5) badgeClass = 'high';
    else if (r.score10 < 6.5) badgeClass = 'low';

    tr.innerHTML = `
      <td style="font-weight:600; color:#475569;">${r.timestamp}</td>
      <td style="font-weight:700; color:var(--dark);">${r.studentName || 'Bé'}</td>
      <td><span style="background:#F1F5F9; padding:2px 8px; border-radius:6px; font-weight:700; font-size:0.8rem;">${r.studentClass || 'Lớp 2'}</span></td>
      <td style="max-width:200px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; font-size:0.8rem; color:#475569;" title="${r.sources}">${r.sources || 'Tất cả'}</td>
      <td style="text-align:center; font-weight:700;"><span style="color:#15803D;">${r.correctCount}</span> / ${r.totalQuestions}</td>
      <td style="text-align:center;"><span class="score-badge ${badgeClass}">${r.score10}/10 (${r.pct}%)</span></td>
      <td style="text-align:center; font-weight:600; color:#64748B;">⏱️ ${r.duration || '00:00'}</td>
    `;
    tbody.appendChild(tr);
  });
}

function clearHistoryData() {
  if (confirm('Bé hoặc phụ huynh có chắc chắn muốn xóa toàn bộ lịch sử các lượt thi không?')) {
    localStorage.removeItem(HISTORY_STORAGE_KEY);
    renderHistoryTable();
  }
}
"""

if 'HISTORY_STORAGE_KEY' not in html:
    html = html.replace('function showScreen(id) {', HISTORY_JS_CODE + '\nfunction showScreen(id) {')

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Đã cập nhật xong toàn bộ code JavaScript cho 5 yêu cầu!")
