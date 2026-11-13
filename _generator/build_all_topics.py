# -*- coding: utf-8 -*-
"""
Bộ sinh 1.000 câu hỏi chuẩn xác cho Khoa Học Tự Nhiên & Xã Hội
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

print("Helper ready")
