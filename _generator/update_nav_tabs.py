import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Update navigateToTab
new_nav = """function navigateToTab(tabName) {
  setActiveNavTab(tabName);
  if (tabName === 'home') {
    showScreen('home-screen');
  } else if (tabName === 'quiz') {
    if (typeof currentDeck !== 'undefined' && currentDeck && currentDeck.length > 0 && !isQuizSubmitted) {
      showScreen('quiz-screen');
    } else {
      startQuiz();
    }
  } else if (tabName === 'leaderboard') {
    openLeaderboardModal();
  } else if (tabName === 'history') {
    openHistoryScreen();
  } else if (tabName === 'user-mgmt') {
    openUserManagementModal();
  }
}"""

text = re.sub(r'function navigateToTab\(tabName\)\s*\{[^}]*\}', new_nav, text, count=1)

# Update showScreen
new_show_screen = """function showScreen(id) {
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

text = re.sub(r'function showScreen\(id\)\s*\{[^}]*\}', new_show_screen, text, count=1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated navigateToTab and showScreen successfully.")
