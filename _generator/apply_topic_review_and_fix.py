import json
import re

# 1. Update questions.json and questions_500.js
plant_ids = {
    # SGK
    "SGK016", "SGK017", "SGK018", "SGK019", "SGK020", "SGK027", "SGK030", 
    "SGK066", "SGK067", "SGK068", "SGK069", "SGK070", "SGK071", "SGK077",
    "SGK094", "SGK095", "SGK096",
    # TN
    "TN043", "TN044", "TN045", "TN046", "TN047", "TN048", "TN049", "TN050",
    # IK
    "IK019", "IK020", "IK021", "IK022", "IK023", "IK024", "IK025", "IK026", "IK027", "IK028", "IK029", "IK030",
    "IK056", "IK057", "IK058", "IK059", "IK060",
    # IXL
    "IXL016", "IXL017", "IXL018", "IXL019", "IXL020", "IXL021", "IXL022", "IXL023", "IXL024", "IXL025",
    "IXL026", "IXL027", "IXL028", "IXL029", "IXL030", "IXL046", "IXL047", "IXL048", "IXL049", "IXL050",
    # NG
    "NG034", "NG035", "NG067", "NG068", "NG078", "NG082"
}

space_ids = {
    "SGK032", "SGK038",
    "TN051", "TN052", "TN053", "TN054", "TN055", "TN056", "TN058", "TN066", "TN067", "TN068",
    "IK031", "IK066", "IK067", "IK068", "IK069", "IK070", "IK071", "IK072", "IK073", "IK074", "IK078", "IK080",
    "IXL051", "IXL052", "IXL053", "IXL054", "IXL055", "IXL056", "IXL059", "IXL060", "IXL063", "IXL065",
    "NG051", "NG052", "NG053", "NG054", "NG055", "NG056", "NG057", "NG058", "NG059", "NG060",
    "NG061", "NG062", "NG063", "NG064", "NG065"
}

with open("/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for q in questions:
    orig = q.get("curriculum_topic") or q.get("topic")
    qid = q.get("id")
    q["curriculum_topic"] = orig
    
    if orig == "Con người & Sức khỏe":
        q["topic"] = "Cơ Thể Người"
    elif orig == "Vật chất & Năng lượng":
        q["topic"] = "Vật Chất & Năng Lượng"
    elif orig == "Thực vật & Động vật":
        q["topic"] = "Thực Vật" if qid in plant_ids else "Động Vật"
    elif orig == "Trái Đất & Bầu trời":
        if qid in plant_ids:
            q["topic"] = "Thực Vật"
        elif qid in space_ids:
            q["topic"] = "Vũ Trụ & Bầu Trời"
        else:
            q["topic"] = "Địa Lý"

with open("/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open("/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/questions_500.js", "w", encoding="utf-8") as f:
    f.write("// Ngân hàng 500 câu hỏi Khoa học Tiểu học chuẩn 5 nguồn (Kèm Song ngữ Anh - Việt)\nwindow.QUESTIONS_500 = ")
    json.dump(questions, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Updated questions.json and questions_500.js successfully.")
