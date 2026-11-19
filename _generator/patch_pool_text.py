#!/usr/bin/env python3
# -*- coding: utf-8 -*-
path = '/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old_pool_text = """  if (pool.length >= requested) {
    textElem.textContent = `Bộ lọc hiện có ${pool.length} câu phù hợp. Đảm bảo chọn đủ ${requested} câu cho lượt thi này!`;
  } else if (pool.length > 0) {
    textElem.textContent = `Bộ lọc có ${pool.length} câu. Chế độ thông minh (Smart Fallback) sẽ bổ sung thêm ${requested - pool.length} câu liên quan cùng nguồn để bé làm đủ ${requested} câu!`;
  } else {
    textElem.textContent = `Không có câu nào khớp với tất cả bộ lọc tuổi/chủ đề hiện tại. Hãy mở rộng chủ đề hoặc độ tuổi!`;
  }"""

new_pool_text = """  const isEn = (currentLanguageMode === 'en');
  if (pool.length >= requested) {
    textElem.textContent = isEn 
      ? `Filters matched ${pool.length} questions. Ready with ${requested} questions for this mission!`
      : `Bộ lọc hiện có ${pool.length} câu phù hợp. Đảm bảo chọn đủ ${requested} câu cho lượt thi này!`;
  } else if (pool.length > 0) {
    textElem.textContent = isEn
      ? `Filters matched ${pool.length} questions. Smart Fallback will add ${requested - pool.length} questions to reach ${requested}!`
      : `Bộ lọc có ${pool.length} câu. Chế độ thông minh (Smart Fallback) sẽ bổ sung thêm ${requested - pool.length} câu liên quan cùng nguồn để bé làm đủ ${requested} câu!`;
  } else {
    textElem.textContent = isEn
      ? `No questions match all current filters. Please broaden your topic or grade selection!`
      : `Không có câu nào khớp với tất cả bộ lọc tuổi/chủ đề hiện tại. Hãy mở rộng chủ đề hoặc độ tuổi!`;
  }"""

if old_pool_text in c:
    c = c.replace(old_pool_text, new_pool_text)
    print("Successfully replaced pool count text!")
else:
    print("WARNING: old_pool_text not found.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
