#!/usr/bin/env python3
import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. HELPER: refreshLucideIcons()
refresh_func = """
function refreshLucideIcons() {
  if (typeof lucide !== 'undefined' && lucide.createIcons) {
    lucide.createIcons();
  }
}
"""

if "function refreshLucideIcons()" not in content:
    content = content.replace("<script>", "<script>\n" + refresh_func, 1)
    print("1. Added refreshLucideIcons() helper")

# 2. UPDATE SOURCE_CONFIG & getSourceIcon
old_source_config = """const SOURCE_CONFIG = [
  { id: "SGK Việt Nam (GDPT 2018)", name: "SGK Việt Nam (GDPT 2018)", icon: "📗", desc: "Môn TN&XH & Khoa học (Lớp 1-5)", defaultSelected: true },
  { id: "Trạng Nguyên & Violympic", name: "Trạng Nguyên & Violympic", icon: "🏆", desc: "Câu ngắn gọn, phản xạ tư duy nhanh", defaultSelected: true },
  { id: "Kangaroo Khoa học (IKSC)", name: "Kangaroo Khoa học (IKSC)", icon: "🦘", desc: "Tư duy quan sát, logic thực tế", defaultSelected: true },
  { id: "IXL & Khan Academy", name: "IXL & Khan Academy", icon: "🌐", desc: "Phân loại khoa học chuẩn quốc tế", defaultSelected: true },
  { id: "National Geographic Kids", name: "National Geographic Kids", icon: "🦁", desc: "Fun facts, thiên nhiên kỳ thú & vũ trụ", defaultSelected: true },
  { id: "Khác", name: "Khác (Kho câu hỏi cũ)", icon: "📦", desc: "Ngân hàng câu hỏi trước đây", defaultSelected: false }
];"""

new_source_config = """const SOURCE_CONFIG = [
  { 
    id: "SGK Việt Nam (GDPT 2018)", 
    name: "SGK Việt Nam (GDPT 2018)", 
    lucide: "book-open", 
    pastelBg: "#D1FAE5", 
    iconColor: "#059669", 
    desc: "Môn TN&XH & Khoa học (Lớp 1-5)", 
    defaultSelected: true 
  },
  { 
    id: "Trạng Nguyên & Violympic", 
    name: "Trạng Nguyên & Violympic", 
    lucide: "award", 
    pastelBg: "#FEF3C7", 
    iconColor: "#D97706", 
    desc: "Câu ngắn gọn, phản xạ tư duy nhanh", 
    defaultSelected: true 
  },
  { 
    id: "Kangaroo Khoa học (IKSC)", 
    name: "Kangaroo Khoa học (IKSC)", 
    lucide: "compass", 
    pastelBg: "#FFEDD5", 
    iconColor: "#EA580C", 
    desc: "Tư duy quan sát, logic thực tế", 
    defaultSelected: true 
  },
  { 
    id: "IXL & Khan Academy", 
    name: "IXL & Khan Academy", 
    lucide: "globe", 
    pastelBg: "#DBEAFE", 
    iconColor: "#2563EB", 
    desc: "Phân loại khoa học chuẩn quốc tế", 
    defaultSelected: true 
  },
  { 
    id: "National Geographic Kids", 
    name: "National Geographic Kids", 
    lucide: "sparkles", 
    pastelBg: "#CCFBF1", 
    iconColor: "#0D9488", 
    desc: "Fun facts, thiên nhiên kỳ thú & vũ trụ", 
    defaultSelected: true 
  },
  { 
    id: "Khác", 
    name: "Khác (Kho câu hỏi cũ)", 
    lucide: "package", 
    pastelBg: "#F3E8FF", 
    iconColor: "#7C3AED", 
    desc: "Ngân hàng câu hỏi trước đây", 
    defaultSelected: false 
  }
];"""

if old_source_config in content:
    content = content.replace(old_source_config, new_source_config, 1)
    print("2. Updated SOURCE_CONFIG with Lucide icons and pastel colors")
else:
    print("Warning: old_source_config not found")

old_get_source_icon = """function getSourceIcon(sourceName) {
  if (!sourceName) return '💡';
  if (sourceName.includes('SGK')) return '📗';
  if (sourceName.includes('Trạng Nguyên') || sourceName.includes('Violympic')) return '🏆';
  if (sourceName.includes('Kangaroo') || sourceName.includes('IKSC')) return '🦘';
  if (sourceName.includes('IXL') || sourceName.includes('Khan')) return '🌐';
  if (sourceName.includes('National') || sourceName.includes('Geographic')) return '🦁';
  return '📦';
}"""

new_get_source_icon = """function getSourceIcon(sourceName) {
  if (!sourceName) return '<i data-lucide="lightbulb" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  if (sourceName.includes('SGK')) return '<i data-lucide="book-open" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  if (sourceName.includes('Trạng Nguyên') || sourceName.includes('Violympic')) return '<i data-lucide="award" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  if (sourceName.includes('Kangaroo') || sourceName.includes('IKSC')) return '<i data-lucide="compass" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  if (sourceName.includes('IXL') || sourceName.includes('Khan')) return '<i data-lucide="globe" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  if (sourceName.includes('National') || sourceName.includes('Geographic')) return '<i data-lucide="sparkles" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
  return '<i data-lucide="package" style="width:16px; height:16px; display:inline-block; vertical-align:middle; margin-right:4px;"></i>';
}"""

if old_get_source_icon in content:
    content = content.replace(old_get_source_icon, new_get_source_icon, 1)
    print("3. Updated getSourceIcon() with Lucide icons")
else:
    print("Warning: old_get_source_icon not found")

# 3. UPDATE renderSourceChips()
old_render_source_chips = """function renderSourceChips() {
  const container = document.getElementById('source-chips-container');
  if (!container) return;
  container.innerHTML = '';

  SOURCE_CONFIG.forEach(src => {
    // Đếm số câu hỏi của nguồn này trong MASTER_POOL
    const count = MASTER_POOL.filter(q => {
      if (src.id === "Khác") {
        return q.source === "Khác" || !q.source || q.source === "Khác (Kho câu hỏi cũ)";
      }
      return q.source === src.id;
    }).length;

    const isSelected = selectedSources.has(src.id);
    const chip = document.createElement('div');
    chip.className = `source-toggle-chip ${isSelected ? 'selected' : ''}`;
    chip.onclick = () => toggleSource(src.id);

    chip.innerHTML = `
      <div class="source-chip-top">
        <div class="source-chip-icon-title">
          <span class="source-chip-icon">${src.icon}</span>
          <span class="source-chip-title">${src.name}</span>
        </div>
        <span class="source-chip-badge">${count} câu</span>
      </div>
      <div class="source-chip-desc">${src.desc}</div>
      <div class="source-chip-checkbox-row">
        <div class="source-checkbox-indicator">${isSelected ? '✓' : ''}</div>
      </div>
    `;
    container.appendChild(chip);
  });
  syncTargetSourceDropdown();
}"""

new_render_source_chips = """function renderSourceChips() {
  const container = document.getElementById('source-chips-container');
  if (!container) return;
  container.innerHTML = '';

  SOURCE_CONFIG.forEach(src => {
    const count = MASTER_POOL.filter(q => {
      if (src.id === "Khác") {
        return q.source === "Khác" || !q.source || q.source === "Khác (Kho câu hỏi cũ)";
      }
      return q.source === src.id;
    }).length;

    const isSelected = selectedSources.has(src.id);
    const chip = document.createElement('div');
    chip.className = `source-toggle-chip ${isSelected ? 'selected' : ''}`;
    chip.onclick = () => toggleSource(src.id);

    chip.innerHTML = `
      <div class="source-chip-top" style="display:flex; align-items:center; justify-content:space-between; gap:10px;">
        <div class="source-chip-icon-title" style="display:flex; align-items:center; gap:12px;">
          <div style="width:44px; height:44px; border-radius:50%; background:${src.pastelBg}; color:${src.iconColor}; display:flex; align-items:center; justify-content:center; flex-shrink:0; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            <i data-lucide="${src.lucide}" style="width:24px; height:24px; stroke-width:2.5;"></i>
          </div>
          <div style="font-weight:800; font-size:0.96rem; color:#1C2038;">${src.name}</div>
        </div>
        <span class="source-chip-badge" style="background:#FCECE4; color:#1C2038; font-weight:800; font-size:0.75rem; padding:4px 10px; border-radius:9999px; white-space:nowrap;">${count} câu</span>
      </div>
      <div class="source-chip-desc" style="font-size:0.82rem; color:#64748B; line-height:1.45; margin-top:8px;">${src.desc}</div>
      <div class="source-chip-checkbox-row" style="display:flex; justify-content:flex-end; margin-top:8px;">
        <div class="source-checkbox-indicator" style="width:24px; height:24px; border-radius:7px; display:flex; align-items:center; justify-content:center; background:${isSelected ? '#10B981' : '#F1F5F9'}; color:white; font-size:0.85rem; font-weight:900;">
          ${isSelected ? '<i data-lucide="check" style="width:16px; height:16px; stroke-width:3;"></i>' : ''}
        </div>
      </div>
    `;
    container.appendChild(chip);
  });
  syncTargetSourceDropdown();
  refreshLucideIcons();
}"""

if old_render_source_chips in content:
    content = content.replace(old_render_source_chips, new_render_source_chips, 1)
    print("4. Updated renderSourceChips() with pastel badges and Lucide icons")
else:
    print("Warning: old_render_source_chips not found")

# 4. UPDATE TOPIC_CONFIG & renderTopics()
old_topic_config = """const TOPIC_CONFIG = [
  { id: 'all', name: 'Tất Cả', icon: '🌟' },
  { id: 'Động Vật', name: 'Động Vật', icon: '🦁' },
  { id: 'Thực Vật', name: 'Thực Vật', icon: '🌿' },
  { id: 'Vũ Trụ & Thời Tiết', name: 'Vũ Trụ & Thời Tiết', icon: '🌍' },
  { id: 'Cơ Thể Người', name: 'Cơ Thể Người', icon: '🫀' },
  { id: 'Địa Lý Việt Nam', name: 'Địa Lý VN', icon: '🗺️' },
  { id: 'Lịch Sử & Văn Hóa', name: 'Lịch Sử & Văn Hóa', icon: '📜' },
  { id: 'Vật Chất & Hiện Tượng', name: 'Vật Lý & Năng Lượng', icon: '🧲' }
];"""

new_topic_config = """const TOPIC_CONFIG = [
  { id: 'all', name: 'Tất Cả', lucide: 'sparkles' },
  { id: 'Động Vật', name: 'Động Vật', lucide: 'paw-print' },
  { id: 'Thực Vật', name: 'Thực Vật', lucide: 'sprout' },
  { id: 'Vũ Trụ & Thời Tiết', name: 'Vũ Trụ & Thời Tiết', lucide: 'rocket' },
  { id: 'Cơ Thể Người', name: 'Cơ Thể Người', lucide: 'heart-pulse' },
  { id: 'Địa Lý Việt Nam', name: 'Địa Lý VN', lucide: 'map-pin' },
  { id: 'Lịch Sử & Văn Hóa', name: 'Lịch Sử & Văn Hóa', lucide: 'landmark' },
  { id: 'Vật Chất & Hiện Tượng', name: 'Vật Lý & Năng Lượng', lucide: 'atom' }
];"""

if old_topic_config in content:
    content = content.replace(old_topic_config, new_topic_config, 1)
    print("5. Updated TOPIC_CONFIG with Lucide icon keys")
else:
    print("Warning: old_topic_config not found")

old_render_topics = """function renderTopics() {
  const container = document.getElementById('topics-list');
  container.innerHTML = '';
  TOPIC_CONFIG.forEach(t => {
    const pill = document.createElement('div');
    pill.className = `topic-pill ${t.id === selectedTopic ? 'selected' : ''}`;
    pill.onclick = () => selectTopic(t.id, pill);
    pill.innerHTML = `<span class="icon">${t.icon}</span><span>${t.name}</span>`;
    container.appendChild(pill);
  });
}"""

new_render_topics = """function renderTopics() {
  const container = document.getElementById('topics-list');
  if (!container) return;
  container.innerHTML = '';
  TOPIC_CONFIG.forEach(t => {
    const pill = document.createElement('div');
    pill.className = `topic-pill ${t.id === selectedTopic ? 'selected' : ''}`;
    pill.onclick = () => selectTopic(t.id, pill);
    pill.innerHTML = `
      <span class="icon" style="display:inline-flex; align-items:center; justify-content:center;">
        <i data-lucide="${t.lucide}" style="width:18px; height:18px; stroke-width:2.5;"></i>
      </span>
      <span>${t.name}</span>
    `;
    container.appendChild(pill);
  });
  refreshLucideIcons();
}"""

if old_render_topics in content:
    content = content.replace(old_render_topics, new_render_topics, 1)
    print("6. Updated renderTopics() with Lucide icons")
else:
    print("Warning: old_render_topics not found")

# 5. UPDATE renderMultipleChoice() WITH CHECK ICON AND INNER TEXT WRAPPER
old_render_mc = """function renderMultipleChoice(q) {
  const container = document.getElementById('choices-list');
  container.innerHTML = '';
  const options = [
    { key: 'A', text: q.a },
    { key: 'B', text: q.b },
    { key: 'C', text: q.c },
    { key: 'D', text: q.d }
  ];

  const currentSelection = userAnswersMap[q.id] ? userAnswersMap[q.id].chosenKey : null;

  options.forEach(opt => {
    if (!opt.text) return;
    const btn = document.createElement('button');
    btn.className = 'choice-option';
    
    // Nếu câu này đã được chọn -> Highlight bằng màu trung tính xanh dương
    if (currentSelection === opt.key) {
      btn.classList.add('selected');
    }

    let choiceContent = '';
    if (currentLanguageMode === 'bilingual') {
      const optIdx = ['A','B','C','D'].indexOf(opt.key);
      const enText = (q.options_en && q.options_en[optIdx]) || (q[opt.key.toLowerCase() + '_en']) || opt.text;
      const viText = opt.text;
      choiceContent = `
        <div style="text-align:left; flex:1;">
          <div style="font-weight:700; color:var(--dark); font-size:0.95rem; line-height:1.35;">${enText}</div>
          <div style="font-size:0.85rem; color:#64748B; font-weight:500; margin-top:2px;">${viText}</div>
        </div>
      `;
    } else if (currentLanguageMode === 'en') {
      const optIdx = ['A','B','C','D'].indexOf(opt.key);
      const enText = (q.options_en && q.options_en[optIdx]) || (q[opt.key.toLowerCase() + '_en']) || opt.text;
      choiceContent = `<span>${enText}</span>`;
    } else {
      choiceContent = `<span>${opt.text}</span>`;
    }
    btn.innerHTML = `<span class="choice-letter">${opt.key}</span>${choiceContent}`;
    
    // Nếu bài chưa nộp thì luôn cho phép click / đổi đáp án
    if (!isQuizSubmitted) {
      btn.onclick = () => handleChoiceSelect(opt.key, opt.text, btn);
    } else {
      btn.disabled = true;
    }
    
    container.appendChild(btn);
  });
}"""

new_render_mc = """function renderMultipleChoice(q) {
  const container = document.getElementById('choices-list');
  container.innerHTML = '';
  const options = [
    { key: 'A', text: q.a },
    { key: 'B', text: q.b },
    { key: 'C', text: q.c },
    { key: 'D', text: q.d }
  ];

  const currentSelection = userAnswersMap[q.id] ? userAnswersMap[q.id].chosenKey : null;

  options.forEach(opt => {
    if (!opt.text) return;
    const btn = document.createElement('button');
    btn.className = 'choice-option' + (currentSelection === opt.key ? ' selected' : '');
    
    let choiceContent = '';
    if (currentLanguageMode === 'bilingual') {
      const optIdx = ['A','B','C','D'].indexOf(opt.key);
      const enText = (q.options_en && q.options_en[optIdx]) || (q[opt.key.toLowerCase() + '_en']) || opt.text;
      const viText = opt.text;
      choiceContent = `
        <div class="choice-text-inner">
          <div style="font-weight:800; color:var(--dark); font-size:1rem; line-height:1.4;">${enText}</div>
          <div style="font-size:0.9rem; color:#64748B; font-weight:600; margin-top:2px; line-height:1.4;">${viText}</div>
        </div>
      `;
    } else if (currentLanguageMode === 'en') {
      const optIdx = ['A','B','C','D'].indexOf(opt.key);
      const enText = (q.options_en && q.options_en[optIdx]) || (q[opt.key.toLowerCase() + '_en']) || opt.text;
      choiceContent = `<div class="choice-text-inner" style="font-weight:700; font-size:0.98rem; line-height:1.4;">${enText}</div>`;
    } else {
      choiceContent = `<div class="choice-text-inner" style="font-weight:700; font-size:0.98rem; line-height:1.4;">${opt.text}</div>`;
    }
    btn.innerHTML = `
      <span class="choice-letter">${opt.key}</span>
      ${choiceContent}
      <span class="choice-check-icon">
        <i data-lucide="check-circle-2" style="width:24px; height:24px; stroke-width:2.5;"></i>
      </span>
    `;
    
    if (!isQuizSubmitted) {
      btn.onclick = () => handleChoiceSelect(opt.key, opt.text, btn);
    } else {
      btn.disabled = true;
    }
    
    container.appendChild(btn);
  });
  refreshLucideIcons();
}"""

if old_render_mc in content:
    content = content.replace(old_render_mc, new_render_mc, 1)
    print("7. Updated renderMultipleChoice() with check-circle-2 icon and inner text wrapper")
else:
    print("Warning: old_render_mc not found")

# 6. UPDATE displayQuestion() FOR ANIMATION REFLOW & LUCIDE
old_display_btn_next = """  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = '📋 Xem lại & Nộp bài';
    btnNext.classList.add('btn-last-step');
    btnNext.onclick = openReviewBeforeSubmit;
  } else {
    btnNext.innerHTML = 'Câu tiếp theo ➔';
    btnNext.classList.remove('btn-last-step');
    btnNext.onclick = goNextQuestion;
  }

  // Ẩn ảnh minh họa nếu là câu tự luận
  if (q.type === 'SA') {
    imgWrap.style.display = 'none';
    document.getElementById('choices-list').style.display = 'none';
    document.getElementById('sa-box').style.display = 'block';
    setupShortAnswer(q);
  } else {
    document.getElementById('choices-list').style.display = 'grid';
    document.getElementById('sa-box').style.display = 'none';
    renderMultipleChoice(q);
  }
}"""

new_display_btn_next = """  // Đổi chữ nút theo trạng thái câu cuối cùng
  if (isLast) {
    btnNext.innerHTML = '<span>📋 Xem lại & Nộp bài</span>';
    btnNext.classList.add('btn-last-step');
    btnNext.onclick = openReviewBeforeSubmit;
  } else {
    btnNext.innerHTML = '<span>Câu tiếp theo</span> <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>';
    btnNext.classList.remove('btn-last-step');
    btnNext.onclick = goNextQuestion;
  }

  // KÍCH HOẠT HIỆU ỨNG CHUYỂN CẢNH MƯỢT MÀ CHO CÂU HỎI MỚI (FADE-IN + SLIDE-UP 0.35s)
  const quizGrid = document.querySelector('.quiz-layout-grid') || document.getElementById('quiz-screen');
  if (quizGrid) {
    quizGrid.classList.remove('animate-question');
    void quizGrid.offsetWidth;
    quizGrid.classList.add('animate-question');
  }

  // Ẩn ảnh minh họa nếu là câu tự luận
  if (q.type === 'SA') {
    imgWrap.style.display = 'none';
    document.getElementById('choices-list').style.display = 'none';
    document.getElementById('sa-box').style.display = 'block';
    setupShortAnswer(q);
  } else {
    document.getElementById('choices-list').style.display = 'grid';
    document.getElementById('sa-box').style.display = 'none';
    renderMultipleChoice(q);
  }

  refreshLucideIcons();
}"""

if old_display_btn_next in content:
    content = content.replace(old_display_btn_next, new_display_btn_next, 1)
    print("8. Updated displayQuestion() with animate-question trigger & refreshLucideIcons")
else:
    print("Warning: old_display_btn_next not found")

# 7. UPDATE fireConfetti() WITH CANVAS-CONFETTI
old_fire_confetti = """function fireConfetti() {
  const colors = ['#4361EE', '#3A0CA3', '#7209B7', '#2EC4B6', '#FF9F1C', '#E71D36'];
  for (let i = 0; i < 60; i++) {
    const c = document.createElement('div');
    c.className = 'confetti';
    c.style.left = Math.random() * 100 + 'vw';
    c.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    c.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
    document.body.appendChild(c);
    setTimeout(() => c.remove(), 3200);
  }
}"""

new_fire_confetti = """function fireConfetti() {
  if (typeof confetti === 'function') {
    confetti({
      particleCount: 120,
      spread: 80,
      origin: { y: 0.6 }
    });
  }
}"""

if old_fire_confetti in content:
    content = content.replace(old_fire_confetti, new_fire_confetti, 1)
    print("9. Updated fireConfetti() to use canvas-confetti library")
else:
    print("Warning: old_fire_confetti not found")

# 8. UPDATE submitAndFinishQuiz() TO FIRE CONFETTI WHEN pct >= 50
old_eval_block = """  if (pct >= 90) {
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
  } else {"""

new_eval_block = """  // TỰ ĐỘNG BẮN PHÁO HOA KHI ĐẠT TỪ 50% ĐIỂM TRỞ LÊN
  if (pct >= 50) {
    fireConfetti();
  }

  if (pct >= 90) {
    // 9.0 - 10.0: Xuất sắc
    stars = '⭐⭐⭐';
    icon = '🏆';
    title = 'Xuất sắc tuyệt đối!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Tư duy khoa học và phản xạ cực kỳ vượt trội!`;
    playSound('correct');
    setMascotMood('finished', 'Bé đạt điểm xuất sắc tuyệt đối luôn, Bo Bo tự hào về bé quá! 🏆');
  } else if (pct >= 80) {
    // 8.0 - 8.9: Rất tốt
    stars = '⭐⭐';
    icon = '🎉';
    title = 'Làm bài rất tốt!';
    desc = `Bé đạt ${score10}/10 điểm (${correctCount}/${total} câu)! Bé nắm rất vững kiến thức, chỉ cần cẩn thận một vài câu nữa là đạt điểm tối đa!`;
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
  } else {"""

if old_eval_block in content:
    content = content.replace(old_eval_block, new_eval_block, 1)
    print("10. Updated submitAndFinishQuiz() evaluation block to fire confetti when pct >= 50")
else:
    print("Warning: old_eval_block not found")

# 9. UPDATE HTML BUTTONS WITH LUCIDE ICONS (WELCOME, HOME, RESULT, MODALS)
# Welcome screen buttons
old_welcome_btns = """      <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap; margin-bottom: 28px;">
        <button class="template-btn-pill" onclick="showScreen('home-screen')">
          Read More &gt;
        </button>
        <button class="template-btn-dark" onclick="openHistoryScreen()">
          📊 Xem Lịch Sử
        </button>
      </div>"""

new_welcome_btns = """      <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap; margin-bottom: 28px;">
        <button class="template-btn-pill" onclick="showScreen('home-screen')">
          <span>Vào Phòng Thi</span>
          <i data-lucide="arrow-right" style="width:18px; height:18px; stroke-width:2.5;"></i>
        </button>
        <button class="template-btn-dark" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Xem Lịch Sử</span>
        </button>
      </div>"""

if old_welcome_btns in content:
    content = content.replace(old_welcome_btns, new_welcome_btns, 1)
    print("11. Updated Welcome Screen buttons with Lucide icons")
else:
    print("Warning: old_welcome_btns not found")

# Home Screen Start button
old_home_start_btn = """<button class="btn-start" onclick="startQuiz()" style="margin-top:0; min-width:240px;">🚀 BẮT ĐẦU ÔN LUYỆN</button>"""
new_home_start_btn = """<button class="btn-start" onclick="startQuiz()" style="margin-top:0; min-width:240px;"><i data-lucide="rocket" style="width:24px; height:24px; stroke-width:2.5;"></i> <span>BẮT ĐẦU ÔN LUYỆN</span></button>"""

if old_home_start_btn in content:
    content = content.replace(old_home_start_btn, new_home_start_btn, 1)
    print("12. Updated Home Screen start button with Lucide rocket icon")
else:
    print("Warning: old_home_start_btn not found")

# Quiz top bar controls
old_quiz_top_bar = """    <div class="quiz-top-bar">
      <div class="top-left-controls">
        <button class="control-btn" onclick="pauseQuiz()">⏸️ Tạm dừng</button>
        <button class="control-btn" onclick="openReviewBeforeSubmit()" style="background:#EEF2FF; color:var(--primary); font-weight:700; border:1.5px solid #C7D2FE;">📋 Xem lại bài</button>
        <button class="control-btn" onclick="askQuitQuiz()">🚪 Thoát</button>
      </div>
      <div class="timer-pill" id="quiz-timer">⏱ 00:00</div>
    </div>"""

new_quiz_top_bar = """    <div class="quiz-top-bar">
      <div class="top-left-controls">
        <button class="control-btn" onclick="pauseQuiz()">
          <i data-lucide="pause" style="width:16px; height:16px; stroke-width:2.5;"></i>
          <span>Tạm dừng</span>
        </button>
        <button class="control-btn" onclick="openReviewBeforeSubmit()" style="background:#EEF2FF; color:var(--primary); font-weight:700; border:1.5px solid #C7D2FE;">
          <i data-lucide="list-checks" style="width:16px; height:16px; stroke-width:2.5;"></i>
          <span>Xem lại bài</span>
        </button>
        <button class="control-btn" onclick="askQuitQuiz()">
          <i data-lucide="log-out" style="width:16px; height:16px; stroke-width:2.5;"></i>
          <span>Thoát</span>
        </button>
      </div>
      <div class="timer-pill" id="quiz-timer">
        <i data-lucide="clock" style="width:16px; height:16px; stroke-width:2.5;"></i>
        <span id="timer-text">00:00</span>
      </div>
    </div>"""

if old_quiz_top_bar in content:
    content = content.replace(old_quiz_top_bar, new_quiz_top_bar, 1)
    print("13. Updated Quiz top bar controls with Lucide icons")
else:
    print("Warning: old_quiz_top_bar not found")

# Result Screen action buttons
old_result_actions = """    <div class="action-buttons">
      <button class="btn-highlight" onclick="openReviewScreen()">🔍 Xem lại chi tiết toàn bộ bài làm</button>
      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">🔄 Ôn lại câu sai</button>
        <button class="btn-secondary" onclick="openHistoryScreen()">📊 Xem Lịch Sử</button>
        <button class="btn-secondary" onclick="syncAllHistoryToSheets()" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-weight:800; display:inline-flex; align-items:center; justify-content:center; gap:6px;">🔄 Đồng bộ lên Sheets</button>
        <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-secondary" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#F0FDF4; color:#15803D; border-color:#86EFAC;">📄 Mở File Google Sheets ↗</a>
        <button class="btn-primary-action" onclick="backToHome()">🏠 Về Trang Chủ</button>
      </div>
    </div>"""

new_result_actions = """    <div class="action-buttons">
      <button class="btn-highlight" onclick="openReviewScreen()">
        <i data-lucide="eye" style="width:20px; height:20px; stroke-width:2.5;"></i>
        <span>Xem lại chi tiết toàn bộ bài làm</span>
      </button>
      <div class="action-row-buttons">
        <button class="btn-secondary" onclick="replayMistakes()" id="btn-replay-wrong">
          <i data-lucide="rotate-ccw" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Ôn lại câu sai</span>
        </button>
        <button class="btn-secondary" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Xem Lịch Sử</span>
        </button>
        <button class="btn-secondary" onclick="syncAllHistoryToSheets()" style="background:#EEF2FF; color:var(--primary); border-color:#C7D2FE; font-weight:800; display:inline-flex; align-items:center; justify-content:center; gap:6px;">
          <i data-lucide="cloud" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Đồng bộ lên Sheets</span>
        </button>
        <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="btn-secondary" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#F0FDF4; color:#15803D; border-color:#86EFAC;">
          <i data-lucide="file-spreadsheet" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Mở File Google Sheets ↗</span>
        </a>
        <button class="btn-primary-action" onclick="backToHome()">
          <i data-lucide="home" style="width:18px; height:18px; stroke-width:2.5;"></i>
          <span>Về Trang Chủ</span>
        </button>
      </div>
    </div>"""

if old_result_actions in content:
    content = content.replace(old_result_actions, new_result_actions, 1)
    print("14. Updated Result Screen action buttons with Lucide icons")
else:
    print("Warning: old_result_actions not found")

# Quick nav modal buttons
old_quick_nav_actions = """    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()" style="flex:1; min-width:160px; font-weight:700;">
        ← Tiếp tục làm bài
      </button>
      <button class="modal-btn-confirm" onclick="submitAndFinishQuiz()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:800; flex:1; min-width:180px; box-shadow:0 4px 14px rgba(16,185,129,0.35);">
        🚀 Nộp bài & Xem điểm
      </button>
    </div>"""

new_quick_nav_actions = """    <div class="modal-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <button class="modal-btn-cancel" onclick="closeQuickNavModal()" style="flex:1; min-width:160px; font-weight:700; display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="arrow-left" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Tiếp tục làm bài</span>
      </button>
      <button class="modal-btn-confirm" onclick="submitAndFinishQuiz()" style="background:linear-gradient(135deg, #10B981, #059669); font-weight:800; flex:1; min-width:180px; box-shadow:0 4px 14px rgba(16,185,129,0.35); display:inline-flex; align-items:center; justify-content:center; gap:8px;">
        <i data-lucide="send" style="width:18px; height:18px; stroke-width:2.5;"></i>
        <span>Nộp bài & Xem điểm</span>
      </button>
    </div>"""

if old_quick_nav_actions in content:
    content = content.replace(old_quick_nav_actions, new_quick_nav_actions, 1)
    print("15. Updated Quick Nav modal buttons with Lucide icons")
else:
    print("Warning: old_quick_nav_actions not found")

# 10. HOOK showScreen and window.onload to refreshLucideIcons()
old_show_screen = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}"""

new_show_screen = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) {
    target.classList.add('active');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}"""

if old_show_screen in content:
    content = content.replace(old_show_screen, new_show_screen, 1)
    print("16. Updated showScreen() with refreshLucideIcons()")
else:
    print("Warning: old_show_screen not found")

old_start_timer = """function startTimer() {
  clearInterval(timerInterval);
  const timerElem = document.getElementById('quiz-timer');
  timerInterval = setInterval(() => {
    if (!isPaused) {
      elapsedSeconds++;
      const m = Math.floor(elapsedSeconds / 60);
      const s = elapsedSeconds % 60;
      timerElem.textContent = `⏱ ${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
    }
  }, 1000);
}"""

new_start_timer = """function startTimer() {
  clearInterval(timerInterval);
  const timerElem = document.getElementById('timer-text');
  timerInterval = setInterval(() => {
    if (!isPaused) {
      elapsedSeconds++;
      const m = Math.floor(elapsedSeconds / 60);
      const s = elapsedSeconds % 60;
      if (timerElem) {
        timerElem.textContent = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
      } else {
        const fullTimer = document.getElementById('quiz-timer');
        if (fullTimer) fullTimer.textContent = `⏱ ${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
      }
    }
  }, 1000);
}"""

if old_start_timer in content:
    content = content.replace(old_start_timer, new_start_timer, 1)
    print("17. Updated startTimer() to preserve timer icon and update timer-text")
else:
    print("Warning: old_start_timer not found")

# Add DOMContentLoaded hook for Lucide Icons
dom_init_code = """
window.addEventListener('DOMContentLoaded', () => {
  refreshLucideIcons();
});
"""
if "window.addEventListener('DOMContentLoaded'" not in content:
    content = content.replace("</script>\n</body>", dom_init_code + "\n</script>\n</body>", 1)
    print("18. Added DOMContentLoaded hook for Lucide icons")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Stage 2 completed successfully!")
