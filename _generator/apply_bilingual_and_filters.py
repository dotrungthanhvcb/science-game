#!/usr/bin/env python3
import re

HTML_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Section 4 HTML config-box: Grade dropdown, Target Source dropdown, Language dropdown
old_sec4_block = """      <div class="config-row">
        <label>👤 Tên bé ôn tập:</label>
        <input type="text" id="user-name" placeholder="Bé Minh" value="Bé Yêu">
      </div>

      <div class="config-row">
        <label>🏫 Lớp của bé:</label>
        <input type="text" id="student-class" placeholder="Lớp 2A" value="Lớp 2">
      </div>"""

new_sec4_block = """      <div class="config-row">
        <label>👤 Tên bé ôn tập:</label>
        <input type="text" id="user-name" placeholder="Bé Minh" value="Bé Yêu">
      </div>

      <div class="config-row">
        <label>🏫 Chọn Lớp học để ôn tập sát trình độ:</label>
        <select id="student-class" onchange="onClassGradeChange()">
          <option value="all">🌟 Tất cả các lớp (Lớp 1 - 5 tổng hợp)</option>
          <option value="1">🎒 Lớp 1 (Kiến thức nhận biết cơ bản - 6 tuổi)</option>
          <option value="2" selected>🌱 Lớp 2 (Quan sát & Khám phá - 7 tuổi)</option>
          <option value="3">🌿 Lớp 3 (Khoa học thường thức - 8 tuổi)</option>
          <option value="4">🔬 Lớp 4 (Vật chất & Năng lượng - 9 tuổi)</option>
          <option value="5">🚀 Lớp 5 (Hệ thống Khoa học chuẩn - 10 tuổi)</option>
          <option value="6">🏆 Lớp 6 (Nâng cao & Ôn thi học bổng)</option>
        </select>
      </div>

      <div class="config-row">
        <label>📚 Nguồn đề thi mục tiêu:</label>
        <select id="target-source-select" onchange="onTargetSourceDropdownChange()">
          <option value="all" selected>🌟 Tất cả các nguồn (Kết hợp đa dạng 500 câu)</option>
          <option value="Trạng Nguyên & Violympic">🏆 Trạng Nguyên & Violympic (Phản xạ tư duy nhanh)</option>
          <option value="SGK Việt Nam (GDPT 2018)">📗 SGK Việt Nam (GDPT 2018) (Chuẩn bộ mới Kết nối/Chân trời)</option>
          <option value="Kangaroo Khoa học (IKSC)">🦘 Kangaroo Khoa học (IKSC) (Tư duy logic thực tế)</option>
          <option value="IXL & Khan Academy">🌐 IXL & Khan Academy (Khoa học chuẩn quốc tế)</option>
          <option value="National Geographic Kids">🦁 National Geographic Kids (Thế giới kỳ thú & Vũ trụ)</option>
          <option value="Khác">🧩 Khác (Kho câu hỏi mở rộng)</option>
        </select>
      </div>

      <div class="config-row">
        <label>🌐 Chế độ ngôn ngữ đề thi:</label>
        <select id="language-mode-select" onchange="onLanguageModeChange()">
          <option value="vi" selected>🇻🇳 Tiếng Việt (Chuẩn)</option>
          <option value="bilingual">🌐 Song ngữ Anh - Việt (Bilingual: English + Tiếng Việt)</option>
          <option value="en">🇬🇧 Tiếng Anh (English Only)</option>
        </select>
      </div>"""

assert old_sec4_block in html, "Could not find old_sec4_block in index.html"
html = html.replace(old_sec4_block, new_sec4_block)

# 2. Update normalizeQuestion to preserve English fields
old_norm = """  return {
    id: q.id,
    q: text,
    question: text,
    options: opts,
    a: opts[0],
    b: opts[1],
    c: opts[2],
    d: opts[3],
    correctIndex: cIdx,
    ans: ansLetter,
    source: sourceName,
    topic: q.topic || "Khác",
    sub: q.sub || "",
    age: age,
    diff: diffNum,
    difficulty: q.difficulty || (diffNum === 1 ? 'easy' : (diffNum === 2 ? 'medium' : 'hard')),
    grade: q.grade || (diffNum === 1 ? 2 : (diffNum === 2 ? 3 : 4)),
    explain: q.explain || "",
    img: q.img || "",
    type: q.type || "MC"
  };"""

new_norm = """  const q_en = q.q_en || q.question_en || text;
  const a_en = q.a_en || (q.options_en ? q.options_en[0] : opts[0]);
  const b_en = q.b_en || (q.options_en ? q.options_en[1] : opts[1]);
  const c_en = q.c_en || (q.options_en ? q.options_en[2] : opts[2]);
  const d_en = q.d_en || (q.options_en ? q.options_en[3] : opts[3]);
  const explain_en = q.explain_en || q.explain || "";

  return {
    id: q.id,
    q: text,
    question: text,
    q_en: q_en,
    question_en: q_en,
    options: opts,
    a: opts[0],
    b: opts[1],
    c: opts[2],
    d: opts[3],
    options_en: [a_en, b_en, c_en, d_en],
    a_en: a_en,
    b_en: b_en,
    c_en: c_en,
    d_en: d_en,
    correctIndex: cIdx,
    ans: ansLetter,
    source: sourceName,
    topic: q.topic || "Khác",
    sub: q.sub || "",
    age: age,
    diff: diffNum,
    difficulty: q.difficulty || (diffNum === 1 ? 'easy' : (diffNum === 2 ? 'medium' : 'hard')),
    grade: q.grade || (diffNum === 1 ? 2 : (diffNum === 2 ? 3 : 4)),
    explain: q.explain || "",
    explain_en: explain_en,
    img: q.img || "",
    type: q.type || "MC"
  };"""

assert old_norm in html, "Could not find old_norm in index.html"
html = html.replace(old_norm, new_norm)

# 3. Add JS state & handlers for language, grade, source sync
handlers_code = """
// BIẾN QUẢN LÝ NGÔN NGỮ & ĐỘ TUỔI / LỚP HỌC
let currentLanguageMode = 'vi'; // 'vi' | 'bilingual' | 'en'

function onLanguageModeChange() {
  const elem = document.getElementById('language-mode-select');
  if (elem) {
    currentLanguageMode = elem.value;
    localStorage.setItem('science_quiz_lang_mode', currentLanguageMode);
  }
}

function onClassGradeChange() {
  const elem = document.getElementById('student-class');
  if (elem) {
    localStorage.setItem('science_quiz_kid_class', elem.value);
    updatePoolCountDisplay();
  }
}

function onTargetSourceDropdownChange() {
  const selectElem = document.getElementById('target-source-select');
  if (!selectElem) return;
  const val = selectElem.value;
  
  if (val === 'all') {
    selectedSources = new Set(SOURCE_CONFIG.map(s => s.id));
  } else {
    selectedSources.clear();
    selectedSources.add(val);
  }

  renderSourceChips();
  updatePoolCountDisplay();
}

function syncTargetSourceDropdown() {
  const selectElem = document.getElementById('target-source-select');
  if (!selectElem) return;
  if (selectedSources.size === SOURCE_CONFIG.length) {
    selectElem.value = 'all';
  } else if (selectedSources.size === 1) {
    const singleSrc = Array.from(selectedSources)[0];
    let exists = false;
    for (let i = 0; i < selectElem.options.length; i++) {
      if (selectElem.options[i].value === singleSrc) {
        exists = true;
        break;
      }
    }
    selectElem.value = exists ? singleSrc : 'all';
  } else {
    selectElem.value = 'all';
  }
}
"""

# Insert handlers_code before renderSourceChips
target_pos = "function renderSourceChips() {"
assert target_pos in html, "Could not find renderSourceChips in index.html"
html = html.replace(target_pos, handlers_code + "\n" + target_pos)

# 4. In renderSourceChips, add syncTargetSourceDropdown() call at end
old_render_end = """    container.appendChild(chip);
  });
}"""

new_render_end = """    container.appendChild(chip);
  });
  syncTargetSourceDropdown();
}"""

assert old_render_end in html, "Could not find old_render_end in index.html"
html = html.replace(old_render_end, new_render_end)

# 5. In loadSavedSettings:
old_load_settings = """  const sClass = localStorage.getItem('science_quiz_kid_class');
  if (sClass && document.getElementById('student-class')) document.getElementById('student-class').value = sClass;"""

new_load_settings = """  const sClass = localStorage.getItem('science_quiz_kid_class');
  if (sClass && document.getElementById('student-class')) {
    document.getElementById('student-class').value = sClass;
  }
  const savedLang = localStorage.getItem('science_quiz_lang_mode');
  if (savedLang && document.getElementById('language-mode-select')) {
    document.getElementById('language-mode-select').value = savedLang;
    currentLanguageMode = savedLang;
  }"""

assert old_load_settings in html, "Could not find old_load_settings in index.html"
html = html.replace(old_load_settings, new_load_settings)

# 6. Update getFilteredPool to filter by Grade:
old_filter_age = """    // 2. Kiểm tra bộ lọc độ tuổi
    if (selectedAge !== 'all' && q.age !== selectedAge) return false;"""

new_filter_age = """    // 2. Kiểm tra bộ lọc Lớp học (Grade sát trình độ)
    const gradeSelect = document.getElementById('student-class');
    const selectedGrade = gradeSelect ? gradeSelect.value : 'all';
    if (selectedGrade !== 'all') {
      if (selectedGrade === '6') {
        // Lớp 6: Kiến thức nâng cao lớp 5 hoặc lớp 4-5 khó
        if (!(q.grade === 5 || (q.grade === 4 && q.diff >= 2))) return false;
      } else {
        const targetGradeNum = parseInt(selectedGrade);
        if (q.grade && q.grade !== targetGradeNum) return false;
      }
    }

    // Kiểm tra bộ lọc độ tuổi
    if (selectedAge !== 'all' && q.age !== selectedAge) return false;"""

assert old_filter_age in html, "Could not find old_filter_age in index.html"
html = html.replace(old_filter_age, new_filter_age)

# 7. Update displayQuestion for Bilingual / English rendering:
old_display_q = """  document.getElementById('badge-topic-age').textContent = `${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}`;
  document.getElementById('question-text').textContent = q.q;"""

new_display_q = """  const gradeText = q.grade ? `Lớp ${q.grade}` : q.age;
  document.getElementById('badge-topic-age').textContent = `${q.topic} • ${gradeText} • Mức ${q.diff}`;
  
  const qTextElem = document.getElementById('question-text');
  if (currentLanguageMode === 'bilingual') {
    const enText = q.q_en || q.question_en || q.q;
    const viText = q.q;
    qTextElem.innerHTML = `
      <div style="font-size:1.15rem; font-weight:800; color:var(--dark); line-height:1.45; margin-bottom:8px;">${enText}</div>
      <div style="font-size:0.95rem; color:#475569; font-weight:600; line-height:1.45; border-top:1.5px dashed #E2E8F0; padding-top:8px;">${viText}</div>
    `;
  } else if (currentLanguageMode === 'en') {
    qTextElem.textContent = q.q_en || q.question_en || q.q;
  } else {
    qTextElem.textContent = q.q;
  }"""

assert old_display_q in html, "Could not find old_display_q in index.html"
html = html.replace(old_display_q, new_display_q)

# 8. Update renderMultipleChoice for Bilingual / English rendering:
old_render_mc = """    btn.innerHTML = `<span class="choice-letter">${opt.key}</span><span>${opt.text}</span>`;"""

new_render_mc = """    let choiceContent = '';
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
    btn.innerHTML = `<span class="choice-letter">${opt.key}</span>${choiceContent}`;"""

assert old_render_mc in html, "Could not find old_render_mc in index.html"
html = html.replace(old_render_mc, new_render_mc)

# 9. Update sendDataToAppsScript to format studentClass nicely
old_send_class = """    studentClass: document.getElementById('student-class') ? document.getElementById('student-class').value.trim() : '',"""

new_send_class = """    studentClass: (function() {
      const elem = document.getElementById('student-class');
      if (!elem) return 'Lớp 2';
      const val = elem.value;
      if (val === 'all') return 'Lớp 1 - 5 (Hỗn hợp)';
      return 'Lớp ' + val;
    })(),"""

assert old_send_class in html, "Could not find old_send_class in index.html"
html = html.replace(old_send_class, new_send_class)

# 10. Update renderListReview to support bilingual/English:
old_rev_item = """      <div class="review-q-text">${q.q}</div>
      <div class="review-answers-box">
        <div><strong>Bé đã chọn:</strong> <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">${item.userAnswerText}</span></div>
        ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>Đáp án đúng:</strong> <span style="color:var(--success); font-weight:700;">${getCorrectAnswerText(q)}</span></div>` : ''}
      </div>
      <div class="review-explain-box">
        <strong>💡 Giải thích:</strong> ${q.explain}
      </div>"""

new_rev_item = """      <div class="review-q-text">
        ${currentLanguageMode === 'bilingual' ? `<div style="font-weight:800; margin-bottom:4px;">${q.q_en || q.q}</div><div style="font-size:0.92em; color:#475569;">${q.q}</div>` : (currentLanguageMode === 'en' ? (q.q_en || q.q) : q.q)}
      </div>
      <div class="review-answers-box">
        <div><strong>Bé đã chọn:</strong> <span style="color:${item.isCorrect ? 'var(--success)' : 'var(--danger)'}; font-weight:700;">${item.userAnswerText}</span></div>
        ${!item.isCorrect ? `<div style="margin-top:4px;"><strong>Đáp án đúng:</strong> <span style="color:var(--success); font-weight:700;">${getCorrectAnswerText(q)}</span></div>` : ''}
      </div>
      <div class="review-explain-box">
        <strong>💡 Giải thích:</strong> ${currentLanguageMode === 'bilingual' ? `<div><em>${q.explain_en || q.explain}</em></div><div style="margin-top:3px;">${q.explain}</div>` : (currentLanguageMode === 'en' ? (q.explain_en || q.explain) : q.explain)}
      </div>"""

assert old_rev_item in html, "Could not find old_rev_item in index.html"
html = html.replace(old_rev_item, new_rev_item)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied bilingual mode, grade dropdown, and target source selector to index.html successfully!")
