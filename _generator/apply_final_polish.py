#!/usr/bin/env python3

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. ADD username IN submitAndFinishQuiz()
old_save_block = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  const currentRecordId = currentSessionQuizId || ('QUIZ-' + Date.now());
  saveQuizToLocalHistory({
    id: currentRecordId,
    quizId: currentSessionQuizId,
    quizDate: currentSessionDate,
    quizTime: currentSessionTime,
    syncedToSheets: false,"""

new_save_block = """  // LƯU LỊCH SỬ BÀI THI VÀO BỘ NHỚ MÁY (KÈM CHI TIẾT CÂU HỎI VÀ ĐÁP ÁN)
  const storedAcc = typeof getStoredAccount === 'function' ? getStoredAccount() : null;
  const currentRecordId = currentSessionQuizId || ('QUIZ-' + Date.now());
  saveQuizToLocalHistory({
    id: currentRecordId,
    quizId: currentSessionQuizId,
    quizDate: currentSessionDate,
    quizTime: currentSessionTime,
    username: storedAcc ? storedAcc.username : '',
    syncedToSheets: false,"""

if old_save_block in content:
    content = content.replace(old_save_block, new_save_block, 1)
    print("1. Added username to saveQuizToLocalHistory.")

# 2. LINK playSound TO playKidSound
old_play_sound = """function playSound(type) {
  try {
    if (audioCtx.state === 'suspended') audioCtx.resume();"""

new_play_sound = """function playSound(type) {
  try {
    if (typeof playKidSound === 'function') {
      playKidSound(type);
      return;
    }
    if (audioCtx.state === 'suspended') audioCtx.resume();"""

if old_play_sound in content:
    content = content.replace(old_play_sound, new_play_sound, 1)
    print("2. Linked playSound to playKidSound.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Final polish complete!")
