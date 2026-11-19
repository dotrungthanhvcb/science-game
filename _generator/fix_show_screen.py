with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_show = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) {
    target.classList.add('active');
  }
  if (id === 'home-screen' || id === 'welcome-screen') {
    setActiveNavTab('home');
  } else if (id === 'quiz-screen') {
    setActiveNavTab('quiz');
  } else if (id === 'history-screen') {
    setActiveNavTab('history');
  } else if (id === 'result-screen') {
    setActiveNavTab('quiz');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}
  if (id === 'home-screen' || id === 'welcome-screen') {
    setActiveNavTab('home');
  } else if (id === 'history-screen') {
    setActiveNavTab('history');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}"""

good_show = """function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) {
    target.classList.add('active');
  }
  if (id === 'home-screen' || id === 'welcome-screen') {
    setActiveNavTab('home');
  } else if (id === 'quiz-screen') {
    setActiveNavTab('quiz');
  } else if (id === 'history-screen') {
    setActiveNavTab('history');
  } else if (id === 'result-screen') {
    setActiveNavTab('quiz');
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
  refreshLucideIcons();
}"""

if bad_show in text:
    text = text.replace(bad_show, good_show)
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned up showScreen successfully.")
else:
    print("bad_show not matched!")
