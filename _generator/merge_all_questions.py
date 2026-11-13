# -*- coding: utf-8 -*-
import json
import os

files = [
    ("dv_150.json", 150, "Động Vật"),
    ("tv_140.json", 140, "Thực Vật"),
    ("vt_150.json", 150, "Vũ Trụ & Thời Tiết"),
    ("ct_140.json", 140, "Cơ Thể Người"),
    ("dl_140.json", 140, "Địa Lý Việt Nam"),
    ("ls_140.json", 140, "Lịch Sử & Văn Hóa"),
    ("vc_140.json", 140, "Vật Chất & Hiện Tượng")
]

all_questions = []
id_set = set()

for filename, expected_count, topic_name in files:
    filepath = os.path.join('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Loaded {filename}: {len(data)} questions (Expected: {expected_count})")
    assert len(data) == expected_count, f"Count mismatch in {filename}: {len(data)} != {expected_count}"
    for q in data:
        qid = q['id']
        assert qid not in id_set, f"Duplicate ID: {qid}"
        id_set.add(qid)
        assert q['topic'] == topic_name, f"Topic mismatch: {q['topic']} != {topic_name}"
        if q['type'] == 'MC':
            assert q['ans'] in ['A', 'B', 'C', 'D'], f"Invalid MC answer: {q['ans']} for {qid}"
            assert q['a'] and q['b'] and q['c'] and q['d'], f"Empty option in {qid}"
        elif q['type'] == 'SA':
            assert q['ans'], f"Empty SA answer in {qid}"
        all_questions.append(q)

print(f"Total verified questions: {len(all_questions)}")

# Xuất ra questions.js
output_js = '/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions.js'
with open(output_js, 'w', encoding='utf-8') as f:
    f.write("// NGÂN HÀNG 1.000 CÂU HỎI KHOA HỌC TỰ NHIÊN & XÃ HỘI CHUẨN MỰC\n")
    f.write("// Phân bổ: Động vật (150), Thực vật (140), Vũ trụ & Thời tiết (150), Cơ thể người (140), Địa lý VN (140), Lịch sử & Văn hóa (140), Vật chất & Hiện tượng (140)\n")
    f.write("const ALL_QUESTIONS = ")
    json.dump(all_questions, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated {output_js} with {len(all_questions)} questions!")
