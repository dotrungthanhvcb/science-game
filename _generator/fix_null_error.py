with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add id="res-icon" to result-screen banner
target_banner = """      <div class="result-stars" id="res-stars">⭐⭐⭐</div>"""
repl_banner = """      <div class="result-stars" id="res-stars">⭐⭐⭐</div>
      <span id="res-icon" style="display:none;">🏆</span>"""

if target_banner in html:
    html = html.replace(target_banner, repl_banner, 1)
    print("1. Added res-icon element to result-screen.")
else:
    print("Warning: target_banner not found.")

# 2. Guard res-score, res-correct, res-time in submitAndFinishQuiz
target_stats = """  // 4. Hiển thị lên màn hình kết quả (result-screen)
  document.getElementById('res-score').textContent = `${score10}/10 (${pct}%)`;
  document.getElementById('res-correct').textContent = `${correctCount}/${total}`;
  const resWrongElem = document.getElementById('res-wrong');
  if (resWrongElem) resWrongElem.textContent = `${wrongCount}/${total}`;
  document.getElementById('res-time').textContent = timeStr;"""

repl_stats = """  // 4. Hiển thị lên màn hình kết quả (result-screen)
  const resScoreElem = document.getElementById('res-score');
  if (resScoreElem) resScoreElem.textContent = `${score10}/10 (${pct}%)`;
  const resCorrectElem = document.getElementById('res-correct');
  if (resCorrectElem) resCorrectElem.textContent = `${correctCount}/${total}`;
  const resWrongElem = document.getElementById('res-wrong');
  if (resWrongElem) resWrongElem.textContent = `${wrongCount}/${total}`;
  const resTimeElem = document.getElementById('res-time');
  if (resTimeElem) resTimeElem.textContent = timeStr;"""

if target_stats in html:
    html = html.replace(target_stats, repl_stats, 1)
    print("2. Guarded result stat elements.")
else:
    print("Warning: target_stats not found.")

# 3. Guard res-stars, res-icon, res-title, res-desc in submitAndFinishQuiz
target_title = """  document.getElementById('res-stars').textContent = stars;
  document.getElementById('res-icon').textContent = icon;
  document.getElementById('res-title').textContent = title;
  const resDescElem = document.getElementById('res-desc');
  if (resDescElem) resDescElem.textContent = desc;"""

repl_title = """  const resStarsElem = document.getElementById('res-stars');
  if (resStarsElem) resStarsElem.textContent = stars;
  const resIconElem = document.getElementById('res-icon');
  if (resIconElem) resIconElem.textContent = icon;
  const resTitleElem = document.getElementById('res-title');
  if (resTitleElem) resTitleElem.textContent = title;
  const resDescElem = document.getElementById('res-desc');
  if (resDescElem) resDescElem.textContent = desc;"""

if target_title in html:
    html = html.replace(target_title, repl_title, 1)
    print("3. Guarded res-icon, res-stars, res-title, res-desc.")
else:
    print("Warning: target_title not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished applying fix_null_error.py!")
