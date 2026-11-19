import re

index_path = "/Users/thanhdo/.gemini/antigravity/scratch/science-quiz/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the HTML structure of #home-config-details
old_details_block = """    <!-- 5. TÙY CHỌN NÂNG CAO (QUY CÁCH ĐỀ THI & GOOGLE SHEETS) -->
    <details class="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm mb-5" id="home-config-details">
      <summary class="font-baloo font-bold text-sm text-slate-800 cursor-pointer flex items-center justify-between select-none">
        <span class="flex items-center gap-2">
          <span>⚙️</span>
          <span id="home-config-summary-text">Tùy Chỉnh Quy Cách Đề Thi & Kết Nối Google Sheets</span>
        </span>
        <span class="text-xs text-cyan-600 font-bold">Mở rộng ▾</span>
      </summary>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 pt-3 border-t border-slate-100">
        <!-- Cột 1: Cấu hình câu hỏi -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">🔢 Số lượng câu hỏi:</label>
            <select id="quiz-size" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
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

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">📚 Nguồn đề thi:</label>
            <select id="target-source-select" onchange="onTargetSourceDropdownChange()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs max-w-[200px]">
              <option value="all" selected>🌟 Tất cả nguồn (Đa dạng 500 câu)</option>
              <option value="Trạng Nguyên & Violympic">🏆 Trạng Nguyên & Violympic</option>
              <option value="SGK Việt Nam (GDPT 2018)">📗 SGK Việt Nam (GDPT 2018)</option>
              <option value="Kangaroo Khoa học (IKSC)">🦘 Kangaroo Khoa học (IKSC)</option>
              <option value="IXL & Khan Academy">🌐 IXL & Khan Academy</option>
              <option value="National Geographic Kids">🦁 National Geographic Kids</option>
              <option value="Khác">🧩 Khác (Mở rộng)</option>
            </select>
          </div>

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700">🧠 Chế độ lặp lại:</label>
            <select id="review-ratio" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
              <option value="random" selected>🎲 Ngẫu nhiên chuẩn</option>
              <option value="mistakes">🔄 Ưu tiên câu từng làm sai</option>
              <option value="unseen">🆕 Chỉ câu chưa từng làm</option>
              <option value="reviewed">🔁 Củng cố trí nhớ</option>
            </select>
          </div>

          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5">🎚️ Độ khó câu hỏi:</label>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectDiff('all', this)">🌟 Hỗn hợp</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('1', this)">⭐ Dễ</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('2', this)">⭐⭐ Vừa</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('3', this)">⭐⭐⭐ Khó</button>
            </div>
          </div>
        </div>

        <!-- Cột 2: Độ tuổi & Kết nối Google Sheets -->
        <div class="flex flex-col gap-3">
          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5">👶 Phù hợp lứa tuổi:</label>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectAge('all', this)">🌟 Tất cả</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('6-7', this)">🌱 6 - 7 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('7-8', this)">🌿 7 - 8 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('8-9', this)">🚀 8 - 9 tuổi</button>
            </div>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl mt-1">
            <div class="flex items-center justify-between mb-1.5">
              <span class="text-xs font-bold text-slate-800 flex items-center gap-1">
                <span>🔗</span> Kết nối Google Sheets Tự Động
              </span>
              <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="text-[11px] font-bold text-cyan-600 hover:underline">Mở File ↗</a>
            </div>
            <div class="flex items-center gap-1.5">
              <input type="text" id="apps-script-url" placeholder="Dán Web App URL Google Apps Script..." class="flex-1 text-xs px-2.5 py-1.5 rounded-lg border border-slate-300" oninput="localStorage.setItem('science_quiz_script_url', this.value.trim())">
              <button type="button" onclick="saveScriptUrlAndSyncFromHome()" class="btn-3d btn-3d-cyan px-3 py-1.5 text-xs font-bold shrink-0">
                Lưu & Đồng Bộ
              </button>
            </div>
          </div>
        </div>
      </div>
    </details>"""

new_details_block = """    <!-- 5. TÙY CHỌN NÂNG CAO (EXAM SETTINGS) -->
    <details class="bg-white border border-slate-200 rounded-2xl p-4 shadow-sm mb-5" id="home-config-details" open>
      <summary class="font-baloo font-bold text-sm text-slate-800 cursor-pointer flex items-center justify-between select-none">
        <span class="flex items-center gap-2">
          <span>⚙️</span>
          <span id="home-config-summary-text">Cài đặt bài thi</span>
        </span>
        <span class="text-xs text-cyan-600 font-bold" id="home-config-badge">Thu gọn ▴</span>
      </summary>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 pt-3 border-t border-slate-100">
        <!-- Cột 1: Cấu hình câu hỏi -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700" id="label-quiz-size">🔢 Số lượng câu hỏi:</label>
            <select id="quiz-size" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
              <option value="5" selected>5 câu (Khởi động)</option>
              <option value="10">10 câu (Nhanh)</option>
              <option value="15">15 câu (Chuẩn thi)</option>
              <option value="20">20 câu (Thử thách)</option>
              <option value="25">25 câu (Nâng cao)</option>
              <option value="30">30 câu (Mô phỏng thi)</option>
              <option value="50">50 câu (Đại hội tri thức)</option>
              <option value="all">Toàn bộ câu có</option>
            </select>
          </div>

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700" id="label-quiz-source">📚 Nguồn đề thi:</label>
            <select id="target-source-select" onchange="onTargetSourceDropdownChange()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs max-w-[200px]">
              <option value="all" selected>🌟 Tất cả nguồn (Đa dạng 500 câu)</option>
              <option value="Trạng Nguyên & Violympic">🏆 Trạng Nguyên & Violympic</option>
              <option value="SGK Việt Nam (GDPT 2018)">📗 SGK Việt Nam (GDPT 2018)</option>
              <option value="Kangaroo Khoa học (IKSC)">🦘 Kangaroo Khoa học (IKSC)</option>
              <option value="IXL & Khan Academy">🌐 IXL & Khan Academy</option>
              <option value="National Geographic Kids">🦁 National Geographic Kids</option>
              <option value="Khác">🧩 Khác (Mở rộng)</option>
            </select>
          </div>

          <div class="flex items-center justify-between text-xs">
            <label class="font-bold text-slate-700" id="label-quiz-ratio">🧠 Chế độ lặp lại:</label>
            <select id="review-ratio" onchange="updatePoolCountDisplay()" class="px-2.5 py-1 rounded-lg border border-slate-200 font-bold text-slate-800 text-xs">
              <option value="random" selected>🎲 Ngẫu nhiên chuẩn</option>
              <option value="mistakes">🔄 Ưu tiên câu từng làm sai</option>
              <option value="unseen">🆕 Chỉ câu chưa từng làm</option>
              <option value="reviewed">🔁 Củng cố trí nhớ</option>
            </select>
          </div>

          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5" id="label-quiz-diff">🎚️ Độ khó câu hỏi:</label>
            <div class="flex items-center gap-1.5 flex-wrap" id="diff-pills-container">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectDiff('all', this)" data-diff="all">🌟 Hỗn hợp</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('1', this)" data-diff="1">⭐ Dễ</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('2', this)" data-diff="2">⭐⭐ Vừa</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectDiff('3', this)" data-diff="3">⭐⭐⭐ Khó</button>
            </div>
          </div>
        </div>

        <!-- Cột 2: Độ tuổi & Kết nối Google Sheets -->
        <div class="flex flex-col gap-3">
          <div>
            <label class="text-xs font-bold text-slate-700 block mb-1.5" id="label-quiz-age">👶 Phù hợp lứa tuổi:</label>
            <div class="flex items-center gap-1.5 flex-wrap" id="age-pills-container">
              <button type="button" class="home-pill active px-3 py-1 rounded-full text-xs font-bold bg-cyan-600 text-white" onclick="selectAge('all', this)" data-age="all">🌟 Tất cả</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('6-7', this)" data-age="6-7">🌱 6 - 7 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('7-8', this)" data-age="7-8">🌿 7 - 8 tuổi</button>
              <button type="button" class="home-pill px-3 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200" onclick="selectAge('8-9', this)" data-age="8-9">🚀 8 - 9 tuổi</button>
            </div>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl mt-1">
            <div class="flex items-center justify-between mb-1.5">
              <span class="text-xs font-bold text-slate-800 flex items-center gap-1">
                <span>🔗</span> <span id="label-gsheets-title">Kết nối Google Sheets Tự Động</span>
              </span>
              <a href="https://docs.google.com/spreadsheets/d/1YW3md3WW_8vj5C2kjztqG7Si_TMidM6NEb9TwFCTNMc/edit" target="_blank" onclick="openGoogleSheetsDirectly(event)" class="text-[11px] font-bold text-cyan-600 hover:underline" id="label-gsheets-link">Mở File ↗</a>
            </div>
            <div class="flex items-center gap-1.5">
              <input type="text" id="apps-script-url" placeholder="Dán Web App URL Google Apps Script..." class="flex-1 text-xs px-2.5 py-1.5 rounded-lg border border-slate-300" oninput="localStorage.setItem('science_quiz_script_url', this.value.trim())">
              <button type="button" onclick="saveScriptUrlAndSyncFromHome()" class="btn-3d btn-3d-cyan px-3 py-1.5 text-xs font-bold shrink-0" id="btn-save-sync">
                Lưu & Đồng Bộ
              </button>
            </div>
          </div>
        </div>
      </div>
    </details>"""

assert old_details_block in html, "Could not find old_details_block in index.html"
html = html.replace(old_details_block, new_details_block)

# 2. Update applyLanguageToUI
old_lang_block = """  // Home Exam Config Details
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

  const homeStartBtn = document.getElementById('home-start-btn-text');
  if (homeStartBtn) homeStartBtn.textContent = isEn ? 'START SCIENCE EXPLORATION 🚀' : 'BẮT ĐẦU THÁM HIỂM KHOA HỌC';

  // Render cards and pills in selected language
  renderTopicLabCards(lang);
  renderTopics(lang);
  renderFilterPills(lang);
  updateAllMascotsUI();
  updateHeaderAuthDisplay();
  if (typeof updatePoolCount === 'function') updatePoolCount();"""

new_lang_block = """  // Home Exam Config Details
  const homeCfgSumm = document.getElementById('home-config-summary-text');
  if (homeCfgSumm) homeCfgSumm.textContent = isEn ? 'Exam Settings' : 'Cài đặt bài thi';
  const homeCfgBadge = document.getElementById('home-config-badge');
  const detailsElem = document.getElementById('home-config-details');
  const isDetailsOpen = detailsElem ? detailsElem.open : true;
  if (homeCfgBadge) {
    homeCfgBadge.textContent = isDetailsOpen ? (isEn ? 'Collapse ▴' : 'Thu gọn ▴') : (isEn ? 'Expand ▾' : 'Mở rộng ▾');
  }
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

  // Dropdown options: quiz-size
  const quizSizeSelect = document.getElementById('quiz-size');
  if (quizSizeSelect) {
    const sizeMap = {
      '5': isEn ? '5 questions (Warm-up)' : '5 câu (Khởi động)',
      '10': isEn ? '10 questions (Quick)' : '10 câu (Nhanh)',
      '15': isEn ? '15 questions (Standard Exam)' : '15 câu (Chuẩn thi)',
      '20': isEn ? '20 questions (Challenge)' : '20 câu (Thử thách)',
      '25': isEn ? '25 questions (Advanced)' : '25 câu (Nâng cao)',
      '30': isEn ? '30 questions (Mock Exam)' : '30 câu (Mô phỏng thi)',
      '50': isEn ? '50 questions (Grand Trivia)' : '50 câu (Đại hội tri thức)',
      'all': isEn ? 'All Available Questions' : 'Toàn bộ câu có'
    };
    Array.from(quizSizeSelect.options).forEach(opt => {
      if (sizeMap[opt.value]) opt.textContent = sizeMap[opt.value];
    });
  }

  // Dropdown options: target-source-select
  const targetSrcSelect = document.getElementById('target-source-select');
  if (targetSrcSelect) {
    const srcMap = {
      'all': isEn ? '🌟 All Sources (500+ diverse)' : '🌟 Tất cả nguồn (Đa dạng 500 câu)',
      'Trạng Nguyên & Violympic': isEn ? '🏆 Trang Nguyen & Violympic' : '🏆 Trạng Nguyên & Violympic',
      'SGK Việt Nam (GDPT 2018)': isEn ? '📗 Vietnam Textbook (GDPT 2018)' : '📗 SGK Việt Nam (GDPT 2018)',
      'Kangaroo Khoa học (IKSC)': isEn ? '🦘 IKSC Science Kangaroo' : '🦘 Kangaroo Khoa học (IKSC)',
      'IXL & Khan Academy': isEn ? '🌐 IXL & Khan Academy' : '🌐 IXL & Khan Academy',
      'National Geographic Kids': isEn ? '🦁 National Geographic Kids' : '🦁 National Geographic Kids',
      'Khác': isEn ? '🧩 Other (Extended)' : '🧩 Khác (Mở rộng)'
    };
    Array.from(targetSrcSelect.options).forEach(opt => {
      if (srcMap[opt.value]) opt.textContent = srcMap[opt.value];
    });
  }

  // Dropdown options: review-ratio
  const reviewRatioSelect = document.getElementById('review-ratio');
  if (reviewRatioSelect) {
    const ratioMap = {
      'random': isEn ? '🎲 Standard Random' : '🎲 Ngẫu nhiên chuẩn',
      'mistakes': isEn ? '🔄 Prioritize Mistakes' : '🔄 Ưu tiên câu từng làm sai',
      'unseen': isEn ? '🆕 Unseen Questions Only' : '🆕 Chỉ câu chưa từng làm',
      'reviewed': isEn ? '🔁 Memory Reinforcement' : '🔁 Củng cố trí nhớ'
    };
    Array.from(reviewRatioSelect.options).forEach(opt => {
      if (ratioMap[opt.value]) opt.textContent = ratioMap[opt.value];
    });
  }

  // Difficulty buttons
  const diffMap = {
    'all': isEn ? '🌟 Mixed' : '🌟 Hỗn hợp',
    '1': isEn ? '⭐ Easy' : '⭐ Dễ',
    '2': isEn ? '⭐⭐ Medium' : '⭐⭐ Vừa',
    '3': isEn ? '⭐⭐⭐ Hard' : '⭐⭐⭐ Khó'
  };
  document.querySelectorAll('#home-config-details button[data-diff]').forEach(btn => {
    const d = btn.getAttribute('data-diff');
    if (d && diffMap[d]) btn.textContent = diffMap[d];
  });

  // Age buttons
  const ageMap = {
    'all': isEn ? '🌟 All' : '🌟 Tất cả',
    '6-7': isEn ? '🌱 Ages 6 - 7' : '🌱 6 - 7 tuổi',
    '7-8': isEn ? '🌿 Ages 7 - 8' : '🌿 7 - 8 tuổi',
    '8-9': isEn ? '🚀 Ages 8 - 9' : '🚀 8 - 9 tuổi'
  };
  document.querySelectorAll('#home-config-details button[data-age]').forEach(btn => {
    const a = btn.getAttribute('data-age');
    if (a && ageMap[a]) btn.textContent = ageMap[a];
  });

  // Google Sheets Sync Card
  const gsheetsTitle = document.getElementById('label-gsheets-title');
  if (gsheetsTitle) gsheetsTitle.textContent = isEn ? 'Auto-Sync Google Sheets' : 'Kết nối Google Sheets Tự Động';
  const gsheetsLink = document.getElementById('label-gsheets-link');
  if (gsheetsLink) gsheetsLink.textContent = isEn ? 'Open Sheet ↗' : 'Mở File ↗';
  const appsScriptInput = document.getElementById('apps-script-url');
  if (appsScriptInput) appsScriptInput.placeholder = isEn ? 'Paste Google Apps Script Web App URL...' : 'Dán Web App URL Google Apps Script...';
  const btnSaveSync = document.getElementById('btn-save-sync');
  if (btnSaveSync) btnSaveSync.textContent = isEn ? 'Save & Sync' : 'Lưu & Đồng Bộ';

  const homeStartBtn = document.getElementById('home-start-btn-text');
  if (homeStartBtn) homeStartBtn.textContent = isEn ? 'START SCIENCE EXPLORATION 🚀' : 'BẮT ĐẦU THÁM HIỂM KHOA HỌC';

  // Render cards and pills in selected language
  renderTopicLabCards(lang);
  renderTopics(lang);
  renderFilterPills(lang);
  updateAllMascotsUI();
  updateHeaderAuthDisplay();
  if (typeof updatePoolCountDisplay === 'function') updatePoolCountDisplay();"""

assert old_lang_block in html, "Could not find old_lang_block in index.html"
html = html.replace(old_lang_block, new_lang_block)

# 3. Add details toggle listener and updatePoolCount alias
old_dom_loaded = """window.addEventListener('DOMContentLoaded', () => {
  refreshLucideIcons();
});"""

new_dom_loaded = """window.addEventListener('DOMContentLoaded', () => {
  refreshLucideIcons();
  
  // Attach toggle listener for Exam Settings details
  const homeDetails = document.getElementById('home-config-details');
  if (homeDetails && !homeDetails.dataset.listenerAdded) {
    homeDetails.dataset.listenerAdded = 'true';
    homeDetails.addEventListener('toggle', () => {
      const isEn = (currentLanguageMode === 'en');
      const badge = document.getElementById('home-config-badge');
      if (badge) {
        badge.textContent = homeDetails.open ? (isEn ? 'Collapse ▴' : 'Thu gọn ▴') : (isEn ? 'Expand ▾' : 'Mở rộng ▾');
      }
    });
  }
});

// Backward-compatible alias
if (typeof window !== 'undefined') {
  window.updatePoolCount = function() {
    if (typeof updatePoolCountDisplay === 'function') updatePoolCountDisplay();
  };
}"""

assert old_dom_loaded in html, "Could not find old_dom_loaded in index.html"
html = html.replace(old_dom_loaded, new_dom_loaded)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully applied exam settings fixes!")
