#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re, shutil

BASE_DIR = '/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz'
HTML_FILE = os.path.join(BASE_DIR, 'index.html')
BAK_FILE = os.path.join(BASE_DIR, 'index.html.bak_fix_img')

print("Starting Fix: Eng Mode Remaining Strings & Broken Image...")
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

shutil.copyfile(HTML_FILE, BAK_FILE)
print(f"Created backup at {BAK_FILE}")

# =========================================================================
# 1. FIX BROKEN IMAGE: REMOVE CSS DISPLAY:FLEX !IMPORTANT & ENSURE ROBUST HIDING
# =========================================================================

# 1a. Remove the old .question-img-card CSS rule that forced display: flex !important
old_css_img_card = """.question-img-card {
      max-height: 130px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      background: #F8FAFC !important;
      border-radius: 16px !important;
      overflow: hidden !important;
      border: 1px solid #E2E8F0 !important;
    }"""

new_css_img_card = """.question-img-card {
      max-height: 180px !important;
      border-radius: 16px !important;
      overflow: hidden !important;
    }
    .question-img-card.hidden,
    .question-img-card[style*="display: none"],
    #q-img-wrap.hidden,
    #q-img-wrap[style*="display: none"] {
      display: none !important;
    }"""

if old_css_img_card in content:
    content = content.replace(old_css_img_card, new_css_img_card)
    print("Fixed CSS .question-img-card forced flex/background rule.")
else:
    # Use regex replacement if whitespace differed
    content = re.sub(
        r'\.question-img-card\s*\{[^}]*max-height:\s*130px\s*!important;[^}]*display:\s*flex\s*!important;[^}]*\}',
        new_css_img_card,
        content
    )
    print("Replaced CSS .question-img-card with regex.")

# 1b. Update HTML of #q-img-wrap and #question-img
old_html_img = """<div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm mx-auto" id="q-img-wrap" style="display:none;">
              <img id="question-img" src="" alt="Minh họa" style="width:100%; max-height:200px; object-fit:contain; display:block; margin:0 auto;">
            </div>"""

new_html_img = """<div class="question-img-card mt-2 rounded-2xl overflow-hidden border border-indigo-700/50 bg-slate-900/60 max-w-sm mx-auto hidden" id="q-img-wrap" style="display:none !important;">
              <img id="question-img" src="" alt="" style="width:100%; max-height:200px; object-fit:contain; display:block; margin:0 auto;">
            </div>"""

if old_html_img in content:
    content = content.replace(old_html_img, new_html_img)
    print("Updated #q-img-wrap HTML.")
else:
    content = re.sub(
        r'<div[^>]*id=["\']q-img-wrap["\'][^>]*>.*?<img[^>]*id=["\']question-img["\'][^>]*>.*?</div>',
        new_html_img,
        content,
        flags=re.DOTALL
    )
    print("Updated #q-img-wrap HTML with regex.")

# =========================================================================
# 2. DEFINE GLOBAL TOPIC_EN_MAP & SOURCE_EN_MAP WITH ALL 11 TOPICS
# =========================================================================
global_dicts_code = """
// =========================================================================
// BILINGUAL EN/VI TOPIC & SOURCE DICTIONARIES
// =========================================================================
const TOPIC_EN_MAP = {
  'Động Vật': 'Animal Kingdom',
  'Thực Vật': 'Plants & Nature',
  'Vũ Trụ & Thời Tiết': 'Space & Weather',
  'Cơ Thể Người': 'Human Body & Health',
  'Con người & Sức khỏe': 'Human Body & Health',
  'Địa Lý Việt Nam': 'Geography & Earth',
  'Lịch Sử & Văn Hóa': 'History & Culture',
  'Vật Chất & Hiện Tượng': 'Matter & Physics',
  'Vật chất & Năng lượng': 'Matter & Energy',
  'Vật lý & Năng lượng': 'Physics & Energy',
  'Thực vật & Động vật': 'Plants & Animals',
  'Trái Đất & Bầu trời': 'Earth & Sky'
};

const SOURCE_EN_MAP = {
  'SGK Việt Nam (GDPT 2018)': 'National Curriculum (MOET)',
  'SGK Việt Nam': 'National Curriculum (MOET)',
  'Trạng Nguyên & Violympic': 'National Science Olympiad',
  'Kangaroo Khoa học (IKSC)': 'IKSC Kangaroo Science',
  'IXL & Khan Academy Khoa học': 'IXL & Khan Science',
  'IXL & Khan Academy': 'IXL & Khan Science',
  'National Geographic Kids': 'NatGeo Kids',
  'Khác': 'General Science'
};
"""

# Insert global dicts right after <script>
content = content.replace('<script>', '<script>\n' + global_dicts_code, 1)

# =========================================================================
# 3. UPGRADE displayQuestion() FOR CLEAN IMAGE HANDLING & TOPIC TRANSLATION
# =========================================================================
old_display_img_logic = """  // Chỉ hiển thị ảnh minh họa khi câu hỏi thực sự có trường img hợp lệ
  const imgElem = document.getElementById('question-img');
  const imgWrap = document.getElementById('q-img-wrap');
  if (imgElem && imgWrap) {
    if (q.img && q.img.trim()) {
      imgElem.onerror = function() {
        this.onerror = null;
        imgWrap.style.display = 'none';
      };
      imgElem.src = q.img;
      imgWrap.style.display = 'block';
    } else {
      imgWrap.style.display = 'none';
    }
  }"""

new_display_img_logic = """  // Chỉ hiển thị ảnh minh họa khi câu hỏi thực sự có trường img hợp lệ và load thành công
  const imgElem = document.getElementById('question-img');
  const imgWrap = document.getElementById('q-img-wrap');
  if (imgElem && imgWrap) {
    imgWrap.style.setProperty('display', 'none', 'important');
    imgWrap.classList.add('hidden');
    imgElem.src = '';

    if (q.img && typeof q.img === 'string' && q.img.trim().length > 5 && (q.img.startsWith('http://') || q.img.startsWith('https://') || q.img.startsWith('data:image/'))) {
      const cleanUrl = q.img.trim();
      imgElem.onload = function() {
        imgWrap.style.setProperty('display', 'block', 'important');
        imgWrap.classList.remove('hidden');
      };
      imgElem.onerror = function() {
        this.onerror = null;
        imgWrap.style.setProperty('display', 'none', 'important');
        imgWrap.classList.add('hidden');
      };
      imgElem.src = cleanUrl;
    }
  }"""

if old_display_img_logic in content:
    content = content.replace(old_display_img_logic, new_display_img_logic)
    print("Upgraded displayQuestion image loading logic.")
else:
    # Replace via regex
    content = re.sub(
        r'\s*// Chỉ hiển thị ảnh minh họa khi câu hỏi thực sự có trường img hợp lệ.*?imgWrap\.style\.display\s*=\s*[\'"]none[\'"];\s*\}\s*\}',
        '\n' + new_display_img_logic,
        content,
        flags=re.DOTALL
    )
    print("Replaced displayQuestion image loading logic via regex.")

# Ensure displayQuestion uses TOPIC_EN_MAP and SOURCE_EN_MAP
content = re.sub(
    r'const sourceEnMap = \{.*?\};\s*const badgeSource = document\.getElementById\(\'badge-source\'\);',
    "const badgeSource = document.getElementById('badge-source');",
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'const topicEnMap = \{.*?\};\s*const topicText = isEn \?',
    "const topicText = isEn ?",
    content,
    flags=re.DOTALL
)

content = content.replace(
    "const srcName = isEn ? (sourceEnMap[rawSrc] || rawSrc) : rawSrc;",
    "const srcName = isEn ? (SOURCE_EN_MAP[rawSrc] || rawSrc) : rawSrc;"
)

content = content.replace(
    "const topicText = isEn ? (topicEnMap[q.topic] || q.topic) : q.topic;",
    "const topicText = isEn ? (TOPIC_EN_MAP[q.topic] || q.topic) : q.topic;"
)

# =========================================================================
# 4. UPGRADE REVIEW SCREEN FUNCTIONS (renderListReview, renderCardReview, getCorrectAnswerText)
# =========================================================================
content = content.replace(
    "<span>Câu ${idx + 1} (${q.topic} - Mức ${q.diff})</span>",
    "<span>${currentLanguageMode === 'en' ? 'Question' : 'Câu'} ${idx + 1} (${(currentLanguageMode === 'en' ? TOPIC_EN_MAP[q.topic] : q.topic) || q.topic} - ${currentLanguageMode === 'en' ? 'Level' : 'Mức'} ${q.diff})</span>"
)

content = content.replace(
    "${item.isCorrect ? '✅ Đúng' : '❌ Chưa đúng'}",
    "${item.isCorrect ? (currentLanguageMode === 'en' ? '✅ Correct' : '✅ Đúng') : (currentLanguageMode === 'en' ? '❌ Incorrect' : '❌ Chưa đúng')}"
)

content = content.replace(
    "<div><strong>Bé đã chọn:</strong>",
    "<div><strong>${currentLanguageMode === 'en' ? 'Your choice:' : 'Bé đã chọn:'}</strong>"
)

content = content.replace(
    "<div><strong>Bé chọn:</strong>",
    "<div><strong>${currentLanguageMode === 'en' ? 'Your choice:' : 'Bé chọn:'}</strong>"
)

content = content.replace(
    "<strong>Đáp án đúng:</strong>",
    "<strong>${currentLanguageMode === 'en' ? 'Correct answer:' : 'Đáp án đúng:'}</strong>"
)

content = content.replace(
    "<strong>💡 Giải thích:</strong>",
    "<strong>💡 ${currentLanguageMode === 'en' ? 'Explanation:' : 'Giải thích:'}</strong>"
)

content = content.replace(
    "<strong>💡 Vì sao lại thế nhỉ?</strong>",
    "<strong>💡 ${currentLanguageMode === 'en' ? 'Science Explanation:' : 'Vì sao lại thế nhỉ?'}</strong>"
)

content = content.replace(
    "<span>${q.topic} • Độ tuổi ${q.age} • Mức ${q.diff}</span>",
    "<span>${(currentLanguageMode === 'en' ? TOPIC_EN_MAP[q.topic] : q.topic) || q.topic} • ${currentLanguageMode === 'en' ? 'Age ' + q.age : 'Độ tuổi ' + q.age} • ${currentLanguageMode === 'en' ? 'Level ' + q.diff : 'Mức ' + q.diff}</span>"
)

content = content.replace(
    "${item.isCorrect ? '✅ Trả lời Đúng' : '❌ Trả lời Sai'}",
    "${item.isCorrect ? (currentLanguageMode === 'en' ? '✅ Correct Answer' : '✅ Trả lời Đúng') : (currentLanguageMode === 'en' ? '❌ Incorrect Answer' : '❌ Trả lời Sai')}"
)

# getCorrectAnswerText bilingual
old_correct_ans_func = """function getCorrectAnswerText(q) {
  if (q.type === 'MC') {
    if (q.ans === 'A') return `A. ${q.a}`;
    if (q.ans === 'B') return `B. ${q.b}`;
    if (q.ans === 'C') return `C. ${q.c}`;
    if (q.ans === 'D') return `D. ${q.d}`;
  }
  return q.ans.split('|')[0];
}"""

new_correct_ans_func = """function getCorrectAnswerText(q) {
  const isEn = (currentLanguageMode === 'en');
  if (q.type === 'MC') {
    const textA = isEn ? (q.a_en || q.a) : q.a;
    const textB = isEn ? (q.b_en || q.b) : q.b;
    const textC = isEn ? (q.c_en || q.c) : q.c;
    const textD = isEn ? (q.d_en || q.d) : q.d;
    if (q.ans === 'A') return `A. ${textA}`;
    if (q.ans === 'B') return `B. ${textB}`;
    if (q.ans === 'C') return `C. ${textC}`;
    if (q.ans === 'D') return `D. ${textD}`;
  }
  return q.ans.split('|')[0];
}"""

if old_correct_ans_func in content:
    content = content.replace(old_correct_ans_func, new_correct_ans_func)
    print("Updated getCorrectAnswerText for bilingual answers.")

# =========================================================================
# 5. EXPAND applyLanguageToUI TO TRANSLATE HOME EXAM CONFIG & REVIEW MODAL
# =========================================================================
# Add IDs to home exam config labels
content = content.replace(
    '<span>Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>',
    '<span id="home-config-summary-text">Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>'
)

content = content.replace(
    '<span class="text-[10px] bg-slate-200 text-slate-700 font-extrabold px-2 py-0.5 rounded-full">Mở rộng ▾</span>',
    '<span class="text-[10px] bg-slate-200 text-slate-700 font-extrabold px-2 py-0.5 rounded-full" id="home-config-badge">Mở rộng ▾</span>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🔢 Số lượng câu hỏi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-size">🔢 Số lượng câu hỏi:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-700">📚 Nguồn đề thi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-source">📚 Nguồn đề thi:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🧠 Chế độ lặp lại:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-ratio">🧠 Chế độ lặp lại:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-700">🎚️ Độ khó câu hỏi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-diff">🎚️ Độ khó câu hỏi:</label>'
)

content = content.replace(
    '<label class="text-xs font-bold text-slate-700">👶 Phù hợp lứa tuổi:</label>',
    '<label class="text-xs font-bold text-slate-700" id="label-quiz-age">👶 Phù hợp lứa tuổi:</label>'
)

# Review Screen UI buttons
content = content.replace(
    '<span>📑 Dạng danh sách</span>',
    '<span id="btn-view-list-text">📑 Dạng danh sách</span>'
)
content = content.replace(
    '<span>🃏 Từng câu một</span>',
    '<span id="btn-view-card-text">🃏 Từng câu một</span>'
)
content = content.replace(
    '<span>⬅️ Quay lại bảng điểm</span>',
    '<span id="btn-back-score-text">⬅️ Quay lại bảng điểm</span>'
)
content = content.replace(
    '<span>⬅️ Câu trước</span>',
    '<span id="btn-card-prev-text">⬅️ Câu trước</span>'
)
content = content.replace(
    '<span>Câu sau ➡️</span>',
    '<span id="btn-card-next-text"><span>Câu sau ➡️</span></span>'
)

# Quick Nav Modal
content = content.replace(
    '<div class="modal-title">Xem Lại Các Câu Vừa Làm</div>',
    '<div class="modal-title" id="quick-nav-modal-title">Xem Lại Các Câu Vừa Làm</div>'
)
content = content.replace(
    'Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!',
    '<span id="quick-nav-modal-desc">Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!</span>'
)
content = content.replace(
    '<span>Tiếp tục làm bài</span>\n      </button>',
    '<span id="quick-nav-cancel-text">Tiếp tục làm bài</span>\n      </button>'
)
content = content.replace(
    '<span>Nộp bài & Xem điểm</span>\n      </button>',
    '<span id="quick-nav-submit-text">Nộp bài & Xem điểm</span>\n      </button>'
)

# Add translations to applyLanguageToUI
apply_extra_code = """
  // Home Exam Config Details
  const homeCfgSumm = document.getElementById('home-config-summary-text');
  if (homeCfgSumm) homeCfgSumm.textContent = isEn ? 'Exam Settings & Google Sheets Sync' : 'Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets';

  const homeCfgBadge = document.getElementById('home-config-badge');
  if (homeCfgBadge) homeCfgBadge.textContent = isEn ? 'Expand ▾' : 'Mở rộng ▾';

  const lblQuizSize = document.getElementById('label-quiz-size');
  if (lblQuizSize) lblQuizSize.textContent = isEn ? '🔢 Number of Questions:' : '🔢 Số lượng câu hỏi:';

  const lblQuizSrc = document.getElementById('label-quiz-source');
  if (lblQuizSrc) lblQuizSrc.textContent = isEn ? '📚 Question Sources:' : '📚 Nguồn đề thi:';

  const lblQuizRatio = document.getElementById('label-quiz-ratio');
  if (lblQuizRatio) lblQuizRatio.textContent = isEn ? '🧠 Review Mode:' : '🧠 Chế độ lặp lại:';

  const lblQuizDiff = document.getElementById('label-quiz-diff');
  if (lblQuizDiff) lblQuizDiff.textContent = isEn ? '🎚️ Question Difficulty:' : '🎚️ Độ khó câu hỏi:';

  const lblQuizAge = document.getElementById('label-quiz-age');
  if (lblQuizAge) lblQuizAge.textContent = isEn ? '👶 Target Age:' : '👶 Phù hợp lứa tuổi:';

  // Review Screen Buttons
  const btnViewList = document.getElementById('btn-view-list-text');
  if (btnViewList) btnViewList.textContent = isEn ? '📑 List View' : '📑 Dạng danh sách';
  const btnViewCard = document.getElementById('btn-view-card-text');
  if (btnViewCard) btnViewCard.textContent = isEn ? '🃏 Card View' : '🃏 Từng câu một';
  const btnBackScore = document.getElementById('btn-back-score-text');
  if (btnBackScore) btnBackScore.textContent = isEn ? '⬅️ Back to Score' : '⬅️ Quay lại bảng điểm';
  const btnCardPrev = document.getElementById('btn-card-prev-text');
  if (btnCardPrev) btnCardPrev.textContent = isEn ? '⬅️ Previous' : '⬅️ Câu trước';
  const btnCardNext = document.getElementById('btn-card-next-text');
  if (btnCardNext) btnCardNext.textContent = isEn ? 'Next ➡️' : 'Câu sau ➡️';

  // Quick Nav Modal
  const qNavTitle = document.getElementById('quick-nav-modal-title');
  if (qNavTitle) qNavTitle.textContent = isEn ? 'Review Your Answers' : 'Xem Lại Các Câu Vừa Làm';
  const qNavDesc = document.getElementById('quick-nav-modal-desc');
  if (qNavDesc) qNavDesc.innerHTML = isEn 
    ? 'Click any question to review or edit your answers. When ready, click <strong>"Submit & Score"</strong>!' 
    : 'Bé bấm vào câu bất kỳ để xem lại đề bài hoặc sửa đáp án nếu muốn. Khi đã chắc chắn, bấm <strong>"Nộp bài & Xem điểm"</strong> nhé!';
  const qNavCancel = document.getElementById('quick-nav-cancel-text');
  if (qNavCancel) qNavCancel.textContent = isEn ? 'Back to Quiz' : 'Tiếp tục làm bài';
  const qNavSubmit = document.getElementById('quick-nav-submit-text');
  if (qNavSubmit) qNavSubmit.textContent = isEn ? 'Submit & Score' : 'Nộp bài & Xem điểm';
"""

# Insert apply_extra_code right before refreshLucideIcons() inside applyLanguageToUI
content = content.replace(
    'refreshLucideIcons();\n}',
    apply_extra_code + '\n  refreshLucideIcons();\n}'
)

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully wrote {HTML_FILE}. File size: {len(content)} bytes.")
