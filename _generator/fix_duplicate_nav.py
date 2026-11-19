with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_block = """function navigateToTab(tabName) {
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
} else if (tabName === 'leaderboard') {
    openLeaderboardModal();
  } else if (tabName === 'history') {
    openHistoryScreen();
  } else if (tabName === 'user-mgmt') {
    openUserManagementModal();
  }
}"""

clean_block = """function navigateToTab(tabName) {
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

if bad_block in text:
    text = text.replace(bad_block, clean_block)
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned up navigateToTab.")
else:
    print("Bad block not found directly, checking regex.")
