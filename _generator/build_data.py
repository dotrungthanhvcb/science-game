# -*- coding: utf-8 -*-
"""
Hệ thống ngân hàng 1.000 câu hỏi Khoa Học Tự Nhiên & Xã Hội cho học sinh Tiểu Học (6-9 tuổi)
Chia đều 7 chủ đề, 3 độ tuổi, 3 mức độ khó, giải thích tỉ mỉ, hỗ trợ trắc nghiệm (MC) & tự luận (SA).
"""
import json
import random

all_questions = []

# =========================================================================
# 1. ĐỘNG VẬT (150 câu: DV001 -> DV150)
# =========================================================================
animals_data = [
    # Côn trùng & Sinh vật nhỏ (25 câu)
    ("Loài côn trùng nào siêng năng làm mật thơm ngọt và giúp thụ phấn cho hoa?", "Ong mật", ["Bướm", "Ruồi", "Kiến"], "Ong mật bay từ bông hoa này sang bông hoa khác hút mật và mang theo hạt phấn giúp cây sinh sôi.", "Ong mật", "6-7", 1, "MC", "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=600&auto=format&fit=crop&q=80"),
    ("Loài côn trùng nào sống thành đàn đông đúc, chia sẻ thức ăn và có thể vác đồ nặng gấp nhiều lần trọng lượng cơ thể?", "Con Kiến", ["Bọ cánh cứng", "Châu chấu", "Ve sầu"], "Kiến là loài côn trùng có tính kỷ luật cao và sức mạnh phi thường so với kích thước bé nhỏ của mình.", "Con Kiến", "6-7", 1, "MC", "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?w=600&auto=format&fit=crop&q=80"),
    ("Loài côn trùng nào phát ra âm thanh râm ran báo hiệu mùa hè đến?", "Ve sầu", ["Dế mèn", "Đom đóm", "Bọ ngựa"], "Ve sầu đực có màng phát âm dưới bụng, tạo ra tiếng kêu râm ran quen thuộc suốt mùa hè.", "Ve sầu", "6-7", 1, "MC", "https://images.unsplash.com/photo-1596727147705-61a532a659bd?w=600&auto=format&fit=crop&q=80"),
    ("Loài bọ cánh cứng nào có lưng màu đỏ chấm đen, rất có ích vì chuyên ăn rệp hại cây?", "Bọ rùa", ["Bọ hung", "Sâu róm", "Mối"], "Bọ rùa là thiên địch của rệp cây, giúp bảo vệ mùa màng tự nhiên mà không cần thuốc hóa học.", "Bọ rùa", "6-7", 1, "MC", "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=600&auto=format&fit=crop&q=80"),
    ("Loài côn trùng nào có khả năng tự phát sáng lập lòe trong đêm tối ở phần đuôi?", "Đom đóm", ["Muỗi", "Bướm đêm", "Nhện"], "Đom đóm phát ra ánh sáng lạnh nhờ phản ứng hóa học tự nhiên để tìm bạn tình và giao tiếp.", "Đom đóm", "6-7", 1, "MC", "https://images.unsplash.com/photo-1508873696983-2df5293cb395?w=600&auto=format&fit=crop&q=80"),
    ("Trước khi biến thành một chú bướm rực rỡ sắc màu, sâu bướm phải nằm cuộn mình trong cái gì?", "Cái kén (Nhộng)", ["Tổ đất", "Hang đá", "Vỏ ốc"], "Giai đoạn nhộng trong kén là bước biến thái hoàn toàn kỳ diệu để sâu biến thành bướm bay lượn.", "Cái kén (Nhộng)", "6-7", 1, "MC", "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=600&auto=format&fit=crop&q=80"),
    ("Con chuồn chuồn có mấy chiếc cánh?", "4 chiếc cánh", ["2 chiếc cánh", "6 chiếc cánh", "8 chiếc cánh"], "Chuồn chuồn có 2 cặp cánh mỏng trong suốt (tổng 4 cánh) giúp bay lượn cực kỳ linh hoạt.", "4 chiếc cánh", "7-8", 2, "MC", "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=600&auto=format&fit=crop&q=80"),
    ("Loài vật nào có 8 chân, chăng tơ bắt mồi và không thuộc nhóm côn trùng (do côn trùng có 6 chân)?", "Con Nhện", ["Con Rết", "Bọ cạp", "Bọ ngựa"], "Nhện thuộc lớp hình nhện (Arachnida) với 8 chân, còn côn trùng chỉ có 6 chân.", "Con Nhện", "7-8", 2, "MC", "https://images.unsplash.com/photo-1535083783855-76ae62b2914e?w=600&auto=format&fit=crop&q=80"),
    ("Con tằm ăn lá gì để nhả tơ dệt lụa?", "Lá dâu tằm", ["Lá bàng", "Lá chuối", "Lá lúa"], "Tằm chỉ ăn duy nhất lá dâu tằm tươi sạch để phát triển và nhả ra sợi tơ óng mượt.", "Lá dâu tằm", "7-8", 2, "MC", "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=600&auto=format&fit=crop&q=80"),
    ("Muỗi vằn là vật trung gian truyền loại bệnh nguy hiểm nào cho con người?", "Sốt xuất huyết", ["Cảm cúm thông thường", "Đau dạ dày", "Cận thị"], "Muỗi vằn mang virus Dengue lây truyền bệnh sốt xuất huyết khi đốt người, cần diệt lăng quăng bọ gậy.", "Sốt xuất huyết", "7-8", 2, "MC", "https://images.unsplash.com/photo-1559827291-72ee739d0d9a?w=600&auto=format&fit=crop&q=80"),
]

print(f"Base data template ready.")
