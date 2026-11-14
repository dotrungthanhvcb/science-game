#!/usr/bin/env python3
import json
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
import urllib.parse

SRC_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions.json"
JS_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions_500.js"

with open(SRC_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions.")

def translate_single(text):
    if not text:
        return ""
    try:
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=en&dt=t&q=" + urllib.parse.quote(text)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return "".join([part[0] for part in res[0] if part[0]]).strip()
    except Exception as e:
        return ""

def translate_question(q_obj):
    # Check if already translated
    if q_obj.get("q_en") and q_obj.get("options_en") and len(q_obj.get("options_en")) == 4:
        return q_obj

    q = q_obj.get("q", "")
    a = q_obj.get("a", "")
    b = q_obj.get("b", "")
    c = q_obj.get("c", "")
    d = q_obj.get("d", "")
    exp = q_obj.get("explain", "")

    combined = "\n@@@\n".join([q, a, b, c, d, exp])
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=en&dt=t&q=" + urllib.parse.quote(combined)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    success = False
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                trans = "".join([part[0] for part in res[0] if part[0]])
                parts = [p.strip() for p in trans.split("@@@")]
                if len(parts) >= 6:
                    q_obj["q_en"] = parts[0]
                    q_obj["question_en"] = parts[0]
                    q_obj["a_en"] = parts[1]
                    q_obj["b_en"] = parts[2]
                    q_obj["c_en"] = parts[3]
                    q_obj["d_en"] = parts[4]
                    q_obj["options_en"] = [parts[1], parts[2], parts[3], parts[4]]
                    q_obj["explain_en"] = parts[5]
                    success = True
                    break
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))

    if not success:
        # Fallback to single translate
        q_en = translate_single(q)
        a_en = translate_single(a)
        b_en = translate_single(b)
        c_en = translate_single(c)
        d_en = translate_single(d)
        exp_en = translate_single(exp)
        q_obj["q_en"] = q_en or q
        q_obj["question_en"] = q_en or q
        q_obj["a_en"] = a_en or a
        q_obj["b_en"] = b_en or b
        q_obj["c_en"] = c_en or c
        q_obj["d_en"] = d_en or d
        q_obj["options_en"] = [q_obj["a_en"], q_obj["b_en"], q_obj["c_en"], q_obj["d_en"]]
        q_obj["explain_en"] = exp_en or exp

    return q_obj

start_time = time.time()
translated_list = [None] * len(questions)

print("Starting parallel translation of 500 questions...")
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(translate_question, q): idx for idx, q in enumerate(questions)}
    done_count = 0
    for future in as_completed(futures):
        idx = futures[future]
        try:
            translated_list[idx] = future.result()
        except Exception as e:
            translated_list[idx] = questions[idx]
        done_count += 1
        if done_count % 50 == 0 or done_count == len(questions):
            elapsed = time.time() - start_time
            print(f"[{done_count}/{len(questions)}] Translated... ({elapsed:.1f}s)")

# Save updated questions.json
with open(SRC_PATH, "w", encoding="utf-8") as f:
    json.dump(translated_list, f, ensure_ascii=False, indent=2)

# Save updated questions_500.js
with open(JS_PATH, "w", encoding="utf-8") as f:
    f.write("// Ngân hàng 500 câu hỏi Khoa học Tiểu học chuẩn 5 nguồn (Kèm Song ngữ Anh - Việt)\n")
    f.write("window.QUESTIONS_500 = " + json.dumps(translated_list, ensure_ascii=False, indent=2) + ";\n")

print(f"DONE! All 500 questions saved with bilingual fields in {time.time() - start_time:.2f}s!")
