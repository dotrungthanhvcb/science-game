# -*- coding: utf-8 -*-
import re

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original HTML length:", len(html))

# 1. Thêm <meta name="referrer" content="no-referrer"> và link script questions.js
if '<meta name="referrer"' not in html:
    html = html.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta name="referrer" content="no-referrer">\n<script src="questions.js"></script>')
    print("Added meta referrer and questions.js script link")

# 2. Xóa mảng ALL_QUESTIONS cũ trong index.html (đã nằm trong questions.js)
start_tag = 'const ALL_QUESTIONS = ['
end_tag = '];'
start_idx = html.find(start_tag)
if start_idx != -1:
    end_idx = html.find(end_tag, start_idx) + len(end_tag)
    # Thay thế bằng chú thích
    html = html[:start_idx] + '// Ngân hàng 1.000 câu hỏi đã được nạp tự động từ questions.js' + html[end_idx:]
    print("Replaced embedded ALL_QUESTIONS with external reference")

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML length after replacement:", len(html))
