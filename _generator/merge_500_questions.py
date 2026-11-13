# -*- coding: utf-8 -*-
"""
Hợp nhất 5 nguồn câu hỏi thành questions.json chuẩn (500 câu)
Đồng thời tạo questions_500.js để hỗ trợ chạy offline qua file:// không bị CORS.
"""
import json
import os
import sys

# Thêm thư mục hiện tại vào sys.path để import
curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.append(curr_dir)

from source1_sgk import get_sgk_questions
from source2_trangnguyen import get_trangnguyen_questions
from source3_kangaroo import get_kangaroo_questions
from source4_ixl_khan import get_ixl_khan_questions
from source5_natgeo import get_natgeo_questions

def main():
    print("=== BẮT ĐẦU TỔNG HỢP 500 CÂU HỎI KHOA HỌC TIỂU HỌC ===")
    
    q_sgk = get_sgk_questions()
    q_tn = get_trangnguyen_questions()
    q_ik = get_kangaroo_questions()
    q_ixl = get_ixl_khan_questions()
    q_ng = get_natgeo_questions()
    
    print(f"1. SGK Việt Nam (GDPT 2018): {len(q_sgk)} câu")
    print(f"2. Trạng Nguyên & Violympic: {len(q_tn)} câu")
    print(f"3. Kangaroo Khoa học (IKSC): {len(q_ik)} câu")
    print(f"4. IXL & Khan Academy: {len(q_ixl)} câu")
    print(f"5. National Geographic Kids: {len(q_ng)} câu")
    
    all_500 = q_sgk + q_tn + q_ik + q_ixl + q_ng
    total = len(all_500)
    print(f"\n=> Tổng số câu hỏi: {total}")
    assert total == 500, f"Lỗi: Tổng số câu là {total}, yêu cầu đúng 500 câu!"
    
    # Kiểm tra tính toàn vẹn dữ liệu
    ids = set()
    source_counts = {}
    topic_counts = {}
    diff_counts = {}
    
    for idx, q in enumerate(all_500):
        # Kiểm tra ID
        qid = q.get("id")
        assert qid, f"Câu số {idx} thiếu ID!"
        assert qid not in ids, f"Trùng lặp ID: {qid} ở câu số {idx}!"
        ids.add(qid)
        
        # Kiểm tra options và correctIndex
        opts = q.get("options", [])
        assert len(opts) == 4, f"Câu {qid} không đủ 4 lựa chọn!"
        c_idx = q.get("correctIndex")
        assert c_idx in [0, 1, 2, 3], f"Câu {qid} có correctIndex không hợp lệ: {c_idx}!"
        
        expected_ans = ['A', 'B', 'C', 'D'][c_idx]
        assert q.get("ans") == expected_ans, f"Câu {qid} có ans ({q.get('ans')}) không khớp correctIndex ({c_idx})!"
        assert q.get("a") == opts[0]
        assert q.get("b") == opts[1]
        assert q.get("c") == opts[2]
        assert q.get("d") == opts[3]
        
        # Thống kê
        src = q.get("source")
        source_counts[src] = source_counts.get(src, 0) + 1
        top = q.get("topic")
        topic_counts[top] = topic_counts.get(top, 0) + 1
        dif = q.get("difficulty")
        diff_counts[dif] = diff_counts.get(dif, 0) + 1
    
    print("\n--- THỐNG KÊ PHÂN BỔ NGUỒN ---")
    for s, c in source_counts.items():
        print(f"  • {s}: {c} câu")
        assert c == 100, f"Nguồn {s} không đủ 100 câu!"
        
    print("\n--- THỐNG KÊ PHÂN BỔ CHỦ ĐỀ ---")
    for t, c in topic_counts.items():
        print(f"  • {t}: {c} câu")
        
    print("\n--- THỐNG KÊ PHÂN BỔ ĐỘ KHÓ ---")
    for d, c in diff_counts.items():
        print(f"  • {d}: {c} câu")

    # Xuất ra questions.json
    output_dir = os.path.abspath(os.path.join(curr_dir, ".."))
    json_path = os.path.join(output_dir, "questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_500, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã lưu thành công: {json_path} ({os.path.getsize(json_path):,} bytes)")

    # Xuất ra questions_500.js (fallback offline nếu fetch json bị chặn bởi trình duyệt chạy trực tiếp file://)
    js_fallback_path = os.path.join(output_dir, "questions_500.js")
    with open(js_fallback_path, "w", encoding="utf-8") as f:
        f.write("// Ngân hàng 500 câu hỏi Khoa học Tiểu học chuẩn 5 nguồn\n")
        f.write("window.QUESTIONS_500 = ")
        json.dump(all_500, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✅ Đã lưu fallback JS: {js_fallback_path} ({os.path.getsize(js_fallback_path):,} bytes)")

    print("\n=== HOÀN TẤT NHIỆM VỤ 1 ===")

if __name__ == "__main__":
    main()
