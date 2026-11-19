with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_snippet = """// BIẾN QUẢN LÝ NGÔN NGỮ & ĐỘ TUỔI / LỚP HỌC
let currentLanguageMode = 'vi'; // 'vi' | 'bilingual' | 'en'


}

function onClassGradeChange() {"""

good_snippet = """// BIẾN QUẢN LÝ NGÔN NGỮ & ĐỘ TUỔI / LỚP HỌC
let currentLanguageMode = 'vi'; // 'vi' | 'bilingual' | 'en'

function onClassGradeChange() {"""

if bad_snippet in text:
    text = text.replace(bad_snippet, good_snippet)
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed extra brace successfully.")
else:
    print("bad_snippet not matched!")
