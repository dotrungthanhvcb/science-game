# -*- coding: utf-8 -*-
"""
Trình khởi tạo ngân hàng 1.000 câu hỏi chuẩn xác cho Khoa Học Tự Nhiên & Xã Hội
Phân bổ:
1. Động Vật: 150 câu (DV001 - DV150)
2. Thực Vật: 140 câu (TV001 - TV140)
3. Vũ Trụ & Thời Tiết: 150 câu (VT001 - VT150)
4. Cơ Thể Người: 140 câu (CT001 - CT140)
5. Địa Lý Việt Nam: 140 câu (DL001 - DL140)
6. Lịch Sử & Văn Hóa: 140 câu (LS001 - LS140)
7. Vật Chất & Hiện Tượng: 140 câu (VC001 - VC140)
Tổng cộng: 1.000 câu
"""
import json
import random

all_questions = []

def add_mc(qid, topic, sub, age, diff, q, correct_ans, distractors, explain, img=""):
    opts = [correct_ans] + distractors[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct_ans))
    all_questions.append({
        "id": qid,
        "topic": topic,
        "sub": sub,
        "age": age,
        "diff": diff,
        "type": "MC",
        "img": img,
        "q": q,
        "a": opts[0],
        "b": opts[1],
        "c": opts[2],
        "d": opts[3],
        "ans": ans_letter,
        "explain": explain
    })

def add_sa(qid, topic, sub, age, diff, q, answer_keywords, explain, img=""):
    all_questions.append({
        "id": qid,
        "topic": topic,
        "sub": sub,
        "age": age,
        "diff": diff,
        "type": "SA",
        "img": img,
        "q": q,
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "ans": answer_keywords,
        "explain": explain
    })

print("Init add_mc & add_sa done")
