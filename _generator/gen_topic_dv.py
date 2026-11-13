# -*- coding: utf-8 -*-
"""ĐỘNG VẬT: 150 câu (DV001 -> DV150)"""
import json
import random

def get_dv_questions():
    imgs = [
        "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1570042225831-d98fa7577f1e?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1552053831-71594a27632d?w=600&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=600&auto=format&fit=crop&q=80"
    ]

    items = [
        # Thú nuôi & Gia súc (DV001 - DV030)
        ("Chó trông nhà", "Loài vật nuôi nào trung thành, hay sủa 'gâu gâu' và giúp con người trông coi nhà cửa?", "Con Chó", ["Con Mèo", "Con Thỏ", "Con Heo"], "Chó có thính giác và khứu giác cực nhạy, là người bạn thân thiết nhất của con người.", "6-7", 1, "MC"),
        ("Mèo bắt chuột", "Loài vật nuôi nào có mắt tinh trong bóng đêm, bước đi êm và thích bắt chuột?", "Con Mèo", ["Con Vịt", "Con Chó", "Con Ngựa"], "Mèo có đệm thịt dưới chân giúp bước đi không gây tiếng động và mắt nhìn rất rõ trong bóng tối.", "6-7", 1, "MC"),
        ("Gà gáy sáng", "Mỗi buổi sáng sớm, con vật nào thường cất tiếng gáy 'ò ó o' đánh thức mọi người?", "Gà trống", ["Gà mái", "Vịt bầu", "Chim sẻ"], "Gà trống có đồng hồ sinh học chuẩn xác, thường cất tiếng gáy vang báo hiệu trời sáng.", "6-7", 1, "MC"),
        ("Gà mái đẻ trứng", "Loài gia cầm nào thường đẻ trứng tròn và kêu 'cục ta cục tác' sau khi đẻ xong?", "Gà mái", ["Gà trống", "Chim bồ câu", "Đà điểu"], "Gà mái ấp trứng và nuôi gà con, cung cấp nguồn trứng bổ dưỡng cho chúng ta.", "6-7", 1, "MC"),
        ("Vịt bơi lội", "Loài thủy cầm nào có màng ở chân giúp bơi lội dưới nước rất giỏi và kêu 'cạp cạp'?", "Con Vịt", ["Con Gà", "Con Ngựa", "Chim sâu"], "Chân vịt có màng bơi như mái chèo giúp vịt bơi lội và lặn bắt tôm cá dễ dàng.", "6-7", 1, "MC"),
        ("Bò sữa nông trại", "Loài gia súc nào ở nông trại cho con người nguồn sữa tươi thơm ngon giàu canxi?", "Bò sữa", ["Con Cừu", "Con Dê núi", "Con Ngựa"], "Bò sữa ăn cỏ xanh và cho lượng sữa tươi dồi dào, cung cấp canxi giúp bé phát triển chiều cao.", "6-7", 1, "MC"),
        ("Trâu kéo cày", "Loài vật nào được xem là 'đầu cơ nghiệp' của nhà nông Việt Nam, giúp kéo cày trên ruộng đồng?", "Con Trâu", ["Con Voi", "Con Lạc đà", "Con Hươu"], "Trâu khỏe mạnh, chăm chỉ kéo cày và gắn liền với hình ảnh làng quê Việt Nam thanh bình.", "6-7", 1, "MC"),
        ("Lợn nông trại", "Loài vật nuôi nào ăn cám, kêu 'ụt ịt' và có chiếc mũi tròn ngộ nghĩnh?", "Con Heo (Lợn)", ["Con Dê", "Con Thỏ", "Con Chó"], "Heo được nuôi ở nông trại để lấy thịt và cung cấp dinh dưỡng cho bữa ăn gia đình.", "6-7", 1, "MC"),
        ("Ngựa phi nước đại", "Loài động vật 4 chân có móng guốc chắc khỏe, chạy phi nước đại rất nhanh và có bờm đẹp?", "Con Ngựa", ["Con Bò", "Con Cừu", "Con Heo"], "Ngựa chạy rất nhanh, thời xưa được dùng để kéo xe và làm phương tiện di chuyển chính.", "6-7", 1, "MC"),
        ("Cừu lấy lông", "Loài động vật nào có bộ lông xoăn dày xốp, thường được xén để dệt thành áo len ấm áp?", "Con Cừu", ["Con Ngựa", "Con Chó", "Con Hổ"], "Lông cừu mềm mại, giữ nhiệt cực tốt nên được dùng để may áo len mùa đông.", "6-7", 1, "MC"),
        ("Dê leo núi", "Loài động vật nào có chòm râu dưới cằm, kêu 'be be' và leo vách đá rất cừ khôi?", "Con Dê", ["Con Cừu", "Con Trâu", "Con Ngựa"], "Dê có móng guốc đặc biệt bám chắc vào các mỏm đá chênh vênh trên vách núi.", "6-7", 1, "MC"),
        ("Thỏ tai dài", "Loài vật nhỏ có đôi tai dài, đuôi ngắn cũn cỡn, mắt tròn xoe và rất thích ăn cà rốt?", "Con Thỏ", ["Chuột túi", "Sóc", "Chuột lang"], "Thỏ có đôi tai dài giúp đón âm thanh từ xa để phòng tránh kẻ thù nguy hiểm.", "6-7", 1, "MC"),
        ("Hamster tinh nghịch", "Loài gặm nhấm nhỏ bé nào có thói quen tích trữ thức ăn phồng cả hai bên má?", "Chuột Hamster", ["Chuột cống", "Sóc bay", "Mèo con"], "Chuột Hamster có túi má mở rộng để mang vác hạt về tổ cất giữ.", "6-7", 1, "MC"),
        ("Ngỗng canh vườn", "Loài gia cầm lớn nào có cổ dài, tiếng kêu to đanh và tính khí hung dữ hay đuổi người lạ?", "Con Ngỗng", ["Con Vịt bầu", "Con Chim sẻ", "Con Bồ câu"], "Ngỗng rất cảnh giác, thấy người lạ là kêu to và rượt đuổi nên hay được nuôi giữ vườn.", "6-7", 1, "MC"),
        ("Bồ câu hòa bình", "Loài chim nào hiền lành, kêu 'gù gù' và được xem là biểu tượng của Hòa Bình thế giới?", "Chim Bồ câu", ["Chim Ưng", "Kền kền", "Chim Cú"], "Bồ câu ngậm cành ô liu là biểu tượng quen thuộc cho khát vọng hòa bình của nhân loại.", "6-7", 1, "MC"),
        ("Lạc đà sa mạc", "Loài vật nào có bướu trên lưng chứa mỡ dự trữ, sống giỏi trên sa mạc nắng cháy?", "Lạc đà", ["Ngựa vằn", "Hươu cao cổ", "Kỳ đà"], "Bướu lạc đà chứa mỡ cung cấp năng lượng và nước giúp nó nhịn đói khát nhiều ngày giữa sa mạc.", "7-8", 2, "MC"),
        ("Gà tây", "Loài gia cầm lớn có mào thịt lòng thòng trước mỏ, hay xòe đuôi tròn kêu 'cuống cuồng' là gì?", "Gà tây", ["Gà sao", "Đà điểu", "Thiên nga"], "Gà tây là món ăn truyền thống trong lễ Tạ ơn ở nhiều nước phương Tây.", "7-8", 2, "MC"),
        ("Vịt trời", "Loài vịt hoang dã có khả năng bay lượn trên trời và bơi lặn giỏi dưới nước là gì?", "Vịt trời", ["Vịt xiêm", "Ngan ré", "Gà nước"], "Vịt trời di cư bay theo đàn hình chữ V để tiết kiệm sức cản của gió.", "7-8", 2, "MC"),
        ("Con Lừa", "Loài động vật móng guốc giống ngựa nhưng tai dài hơn, chịu khó thồ hàng nặng trên đường đèo dốc là gì?", "Con Lừa", ["Con Ngựa vằn", "Con Lạc đà", "Con Bò"], "Lừa rất dẻo dai, bước chân chắc chắn trên các cung đường núi dốc hiểm trở.", "7-8", 2, "MC"),
        ("Cút đẻ trứng", "Loài chim nhỏ bé nào đẻ ra những quả trứng nhỏ có đốm hoa văn nâu được gọi là trứng cút?", "Chim cút", ["Chim sẻ", "Chim chích", "Chim ri"], "Trứng cút nhỏ bé nhưng rất giàu đạm, vitamin A và khoáng chất bổ dưỡng.", "6-7", 1, "MC"),

        # Côn trùng & Sinh vật nhỏ (DV021 - DV050)
        ("Ong mật chăm chỉ", "Loài côn trùng nào bay lượn hút mật hoa rồi đem về tổ tạo thành mật ong ngọt lịm?", "Con Ong mật", ["Con Bướm", "Con Ruồi", "Con Chuồn chuồn"], "Ong mật thụ phấn cho cây và sản xuất sáp, mật ong rất tốt cho sức khỏe con người.", "6-7", 1, "MC"),
        ("Kiến đoàn kết", "Loài côn trùng sống thành bầy đàn đông đúc, có thể vác đồ nặng gấp hàng chục lần cơ thể mình?", "Con Kiến", ["Bọ rùa", "Châu chấu", "Ve sầu"], "Kiến có sức mạnh cơ bắp phi thường và tính kỷ luật hợp tác tuyệt vời.", "6-7", 1, "MC"),
        ("Bọ rùa có ích", "Loài bọ cánh cứng nào có lưng đỏ chấm đen tròn, là bạn tốt của nông dân vì chuyên ăn rệp hại cây?", "Bọ rùa", ["Bọ xít", "Sâu róm", "Mối"], "Bọ rùa là thiên địch tự nhiên giúp diệt sâu rệp bảo vệ mùa màng tươi tốt.", "6-7", 1, "MC"),
        ("Đom đóm phát sáng", "Loài côn trùng có thể tự phát ra ánh sáng lung linh ở phần bụng trong đêm tối là gì?", "Đom đóm", ["Muỗi", "Bọ rùa", "Bọ xít"], "Phản ứng hóa học giữa luciferin và enzym luciferase giúp đom đóm phát quang mà không tỏa nhiệt.", "7-8", 2, "MC"),
        ("Ve sầu mùa hè", "Loài côn trùng nào phát ra tiếng kêu râm ran quen thuộc báo hiệu mùa hè đến?", "Ve sầu", ["Châu chấu", "Cào cào", "Bọ ngựa"], "Ve sầu đực có màng phát âm dưới bụng rung lên tạo thành bản hòa ca mùa hè rộn rã.", "6-7", 1, "MC"),
        ("Chuồn chuồn bắt muỗi", "Loài côn trùng bay lượn trên mặt nước có 4 cánh mỏng trong suốt, chuyên săn bắt ruồi muỗi có ích là gì?", "Chuồn chuồn", ["Bướm", "Bọ xít", "Ong bầu"], "Chuồn chuồn là tay săn mồi cừ khôi trên không trung, giúp tiêu diệt muỗi gây hại.", "6-7", 1, "MC"),
        ("Bướm xinh đẹp", "Trước khi biến thành một chú bướm rực rỡ sắc màu bay lượn, sâu bướm phải trải qua giai đoạn nào?", "Nằm cuộn mình trong kén (nhộng)", ["Bơi lội dưới nước", "Chôn mình dưới cát sâu", "Rụng hết chân"], "Biến thái hoàn toàn từ trứng -> sâu bướm -> nhộng trong kén -> bướm trưởng thành là một kỳ quan tự nhiên.", "6-7", 1, "MC"),
        ("Con Tằm nhả tơ", "Con tằm ăn lá gì để lớn lên rồi nhả sợi tơ quý giá dệt nên lụa tơ tằm?", "Lá dâu tằm", ["Lá chuối", "Lá bàng", "Lá xoài"], "Tằm ăn lá dâu tằm và cuộn mình trong kén tơ vàng hoặc trắng óng ả.", "7-8", 2, "MC"),
        ("Bọ ngựa kiếm sĩ", "Loài côn trùng có hai chi trước gập lại hình răng cưa như lưỡi kiếm để chộp mồi nhanh như chớp là gì?", "Bọ ngựa", ["Dế mèn", "Bọ hung", "Bọ xít"], "Bọ ngựa ngụy trang như cành cây và phục kích săn mồi với tốc độ cực nhanh.", "7-8", 2, "MC"),
        ("Châu chấu nhảy xa", "Loài côn trùng có đôi chân sau to khỏe gập hình chữ Z giúp bật nhảy vút xa là gì?", "Châu chấu", ["Con Gián", "Con Ve", "Con Kiến"], "Châu chấu dùng sức bật lò xo của hai chân sau để phóng lên không trung.", "6-7", 1, "MC"),
        ("Dế mèn ca hát", "Loài côn trùng sống trong hang đất, cọ hai cánh vào nhau phát ra tiếng gáy 'ri ri' là con gì?", "Dế mèn", ["Giun đất", "Bọ rùa", "Ruồi"], "Dế cọ răng cánh vào gân cánh đối diện để tạo ra âm thanh gọi bạn tình.", "6-7", 1, "MC"),
        ("Bọ hung lực sĩ", "Loài bọ cánh cứng nào chuyên vê các viên phân tròn lăn về tổ và có thể nâng vật nặng gấp hơn 1.000 lần cơ thể?", "Bọ hung", ["Bọ ngựa", "Ve sầu", "Con Mối"], "Bọ hung là loài động vật khỏe nhất hành tinh tính theo tỉ lệ kích thước cơ thể.", "7-8", 2, "MC"),
        ("Con Muỗi truyền bệnh", "Muỗi cái đốt người hút máu để làm gì?", "Lấy protein nuôi dưỡng trứng phát triển", ["Uống cho đỡ khát", "Vì đói bụng không có thức ăn", "Để bay nhanh hơn"], "Chỉ có muỗi cái mới đốt người hút máu lấy chất dinh dưỡng nuôi trứng, muỗi đực chỉ hút mật hoa.", "7-8", 2, "MC"),
        ("Ruồi nhà truyền vi khuẩn", "Tại sao loài ruồi nhà thường hay xoa xoa hai chân trước vào nhau?", "Để làm sạch lông cảm giác ở chân giúp nếm thức ăn", ["Vì ruồi bị lạnh chân", "Để vỗ tay hoan hô", "Để mài vuốt sắc nhọn"], "Chân ruồi có các thụ thể nếm vị giác cực nhạy, nó phải xoa chân liên tục để làm sạch bụi bẩn bám vào.", "8-9", 3, "MC"),
        ("Mối đục gỗ", "Loài côn trùng sống theo bầy hàng triệu con, làm hỏng các đồ đạc gỗ trong nhà là con gì?", "Con Mối", ["Mọt gạo", "Bọ rùa", "Kiến vàng"], "Mối có vi sinh vật đặc biệt trong ruột giúp phân giải chất cellulose có trong gỗ.", "7-8", 2, "MC"),
        ("Con Nhện 8 chân", "Con nhện có phải là côn trùng không? Vì sao?", "Không, vì nhện có 8 chân (côn trùng chỉ có 6 chân)", ["Đúng, vì nhện biết chăng tơ", "Đúng, vì nhện có cánh", "Không, vì nhện sống dưới nước"], "Nhện thuộc lớp hình nhện (Arachnida) với 8 chân và cơ thể chia làm 2 phần, còn côn trùng có 6 chân và 3 phần cơ thể.", "8-9", 3, "MC"),
        ("Bọ cạp sa mạc", "Loài động vật chân đốt có 2 càng to và chiếc đuôi cong vút mang kim châm nọc độc là gì?", "Bọ cạp", ["Tôm tít", "Cua đá", "Ba ba"], "Nọc độc ở chóp đuôi bọ cạp giúp nó tự vệ và làm tê liệt các con mồi săn được.", "7-8", 2, "MC"),
        ("Con Rết", "Loài vật có thân nhiều đốt, mỗi đốt một đôi chân và vết cắn gây sưng tấy nhức nhối là con gì?", "Con Rết", ["Con Giun", "Cuốn chiếu", "Sâu đất"], "Rết là loài săn mồi ăn thịt ban đêm và có nọc độc tự vệ, các bé cần tránh xa.", "7-8", 2, "MC"),
        ("Cuốn chiếu hiền lành", "Loài sinh vật nhiều chân nào khi chạm tay vào sẽ cuộn tròn mình lại như chiếc lò xo đồng xu?", "Con Cuốn chiếu", ["Con Rết", "Sâu róm", "Bọ cạp"], "Cuốn chiếu không cắn và không có nọc độc, nó chỉ cuộn tròn lại tự vệ và ăn lá cây mục nát.", "6-7", 1, "MC"),
        ("Con Giun đất", "Loài động vật không xương sống nào thở bằng da, đào hang giúp đất tơi xốp và màu mỡ?", "Giun đất", ["Sâu đất", "Ấu trùng ve", "Chuột chũi"], "Giun đất là kỹ sư đất đai tuyệt vời, chất thải của giun là loại phân hữu cơ giàu dinh dưỡng nhất.", "6-7", 1, "MC"),

        # Thú hoang dã rừng xanh & Đồng cỏ (DV041 - DV080)
        ("Hổ chúa sơn lâm", "Loài thú săn mồi lớn có bộ lông vàng vằn đen dũng mãnh, được mệnh danh là 'Chúa sơn lâm'?", "Con Hổ (Cọp)", ["Báo đốm", "Sư tử", "Chó sói"], "Hổ là loài mèo lớn nhất thế giới, bơi lội giỏi và có sức mạnh phi thường trong rừng sâu.", "6-7", 1, "MC"),
        ("Sư tử thảo nguyên", "Loài mèo lớn nào sống ở đồng cỏ châu Phi, con đực có chiếc bờm dày uy nghiêm quanh cổ?", "Sư tử", ["Con Báo", "Linh cẩu", "Hổ vằn"], "Sư tử sống thành bầy đàn gắn kết, con đực bảo vệ lãnh thổ còn con cái phối hợp săn mồi.", "6-7", 1, "MC"),
        ("Báo hoa mai", "Loài thú săn mồi nào có đốm hoa mai trên thân, leo trèo cây rất giỏi và hay tha mồi lên cây?", "Báo hoa mai", ["Sư tử", "Chó rừng", "Hổ"], "Báo hoa mai có cơ bắp khỏe giúp nó kéo con mồi nặng gấp đôi trọng lượng lên cành cây cao.", "7-8", 2, "MC"),
        ("Báo săn Cheetah", "Loài động vật trên cạn chạy nhanh nhất hành tinh với tốc độ lên tới hơn 100 km/h là loài nào?", "Báo săn Cheetah", ["Ngựa vằn", "Linh dương", "Thỏ rừng"], "Cheetah có thân hình thon gọn và cột sống linh hoạt như lò xo giúp tăng tốc chớp nhoáng.", "7-8", 2, "MC"),
        ("Voi khổng lồ", "Loài động vật trên cạn lớn nhất thế giới có chiếc vòi dài khéo léo và cặp ngà trắng là gì?", "Con Voi", ["Tê giác", "Hà mã", "Gấu bắc cực"], "Vòi voi thực chất là mũi và môi trên kết hợp, có hơn 40.000 bó cơ giúp cầm nắm cực khéo.", "6-7", 1, "MC"),
        ("Hươu cao cổ", "Loài động vật trên cạn cao nhất thế giới có chiếc cổ dài để ăn lá cây trên ngọn cao?", "Hươu cao cổ", ["Con Đà điểu", "Con Ngựa", "Lạc đà"], "Cổ của hươu cao cổ dài gần 2 mét nhưng cũng chỉ gồm 7 đốt sống cổ giống như con người.", "6-7", 1, "MC"),
        ("Tê giác sừng nhọn", "Loài thú ăn cỏ to lớn có lớp da dày như áo giáp và chiếc sừng nhọn mọc trên sống mũi là gì?", "Tê giác", ["Hà mã", "Heo rừng", "Bò tót"], "Sừng tê giác cấu tạo từ chất sừng (keratin) giống như móng tay của con người.", "7-8", 2, "MC"),
        ("Hà mã ngâm nước", "Loài thú lớn ăn cỏ dành phần lớn thời gian ngâm mình dưới nước và có hàm răng mở rộng khổng lồ?", "Hà mã", ["Cá sấu", "Hải mã", "Voi nước"], "Hà mã ngâm mình dưới nước để giữ mát da và bảo vệ cơ thể khỏi ánh nắng chói chang.", "7-8", 2, "MC"),
        ("Ngựa vằn sọc", "Loài thú nào ở thảo nguyên châu Phi có bộ lông kẻ sọc trắng đen xen kẽ độc đáo giúp đánh lừa ruồi trâu?", "Ngựa vằn", ["Ngựa bạch", "Lừa hoang", "Hươu sao"], "Các sọc đen trắng của ngựa vằn làm rối mắt côn trùng đốt và gây khó khăn cho kẻ săn mồi.", "6-7", 1, "MC"),
        ("Gấu trúc ăn trúc", "Loài gấu có khoang lông đen trắng ở Trung Quốc, thức ăn khoái khẩu là cành lá trúc tươi?", "Gấu trúc", ["Gấu ngựa", "Gấu chó", "Gấu xám"], "Gấu trúc dành tới 12 tiếng mỗi ngày để gặm nhấm thân và lá cây trúc, tre.", "6-7", 1, "MC"),
        ("Gấu Bắc Cực", "Loài gấu lớn sống ở vùng băng tuyết giá lạnh, bơi lội giỏi và săn hải cẩu để sinh sống?", "Gấu Bắc Cực", ["Gấu nâu", "Gấu trúc", "Chim cánh cụt"], "Gấu Bắc Cực có lớp mỡ dày giữ ấm và bàn chân rộng có đệm lông để không bị trượt trên băng.", "7-8", 2, "MC"),
        ("Gấu túi Koala", "Loài thú có túi đáng yêu ở Úc ngủ tới 18-20 tiếng mỗi ngày và chỉ ăn lá cây bạch đàn (khuynh diệp)?", "Koala", ["Gấu lười", "Gấu trúc", "Sóc bay"], "Lá bạch đàn chứa ít năng lượng và có độc tố nhẹ nên Koala ngủ nhiều để tiêu hóa và tiết kiệm sức.", "7-8", 2, "MC"),
        ("Kangaroo nhảy", "Loài thú có túi đặc trưng của nước Úc, di chuyển bằng cách nhảy hai chân sau cực khỏe là gì?", "Kangaroo (Chuột túi)", ["Koala", "Gấu túi Wombat", "Đà điểu"], "Chuột túi mẹ có chiếc túi ấm áp trước bụng để nuôi dưỡng và bảo vệ chuột túi con.", "6-7", 1, "MC"),
        ("Khỉ chuyền cành", "Loài linh trưởng nào thông minh, thích ăn hoa quả, leo trèo thoăn thoắt và có đuôi dài giữ thăng bằng?", "Con Khỉ", ["Chó rừng", "Cầy hương", "Gấu túi"], "Khỉ dùng 4 chi và đuôi linh hoạt để chuyền cành, chúng sống thành bầy rất đoàn kết.", "6-7", 1, "MC"),
        ("Tinh tinh thông minh", "Loài linh trưởng thông minh nhất có ADN giống con người đến 98% và biết dùng cành cây làm công cụ?", "Tinh tinh", ["Khỉ đột", "Vượn cáo", "Khỉ đuôi sóc"], "Tinh tinh có trí tuệ vượt trội, biết dùng que chọc tổ mối và biểu lộ cảm xúc phong phú.", "8-9", 3, "MC"),
        ("Khỉ đột Gorilla", "Loài vượn người to lớn vạm vỡ nhất, thường vỗ tay vào ngực để thể hiện uy phong sức mạnh?", "Khỉ đột Gorilla", ["Đười ươi", "Vượn đen má trắng", "Tinh tinh lùn"], "Gorilla là động vật ăn thực vật hiền lành, chỉ phô trương sức mạnh khi cảm thấy bầy đàn bị đe dọa.", "7-8", 2, "MC"),
        ("Đười ươi tóc đỏ", "Loài linh trưởng lớn có bộ lông dài màu nâu đỏ, dành phần lớn cuộc đời sống trên cây ở rừng nhiệt đới châu Á?", "Đười ươi", ["Khỉ đột", "Vượn tay trắng", "Khỉ đầu chó"], "Đười ươi có sải tay dài hơn cả chiều cao cơ thể giúp chúng đu lượn giữa các tán cây cao dễ dàng.", "8-9", 3, "MC"),
        ("Sói hú đêm trăng", "Loài thú ăn thịt họ chó thường hú vang dưới ánh trăng và săn mồi theo bầy đàn kỷ luật?", "Chó sói", ["Cáo đỏ", "Chó hoang", "Linh cẩu"], "Chó sói có tổ chức bầy đàn chặt chẽ, luôn có sói đầu đàn dẫn dắt đi săn.", "7-8", 2, "MC"),
        ("Cáo tinh ranh", "Loài thú ăn thịt nhỏ có chiếc đuôi xù to đẹp mắt, nổi tiếng tinh ranh trong các câu chuyện ngụ ngôn?", "Con Cáo", ["Chồn hôi", "Chuột túi", "Nhím"], "Cáo có khứu giác thính nhạy, bước chân nhẹ nhàng và chiếc đuôi giúp giữ ấm cơ thể khi ngủ.", "6-7", 1, "MC"),
        ("Nhím lông gai", "Loài thú nhỏ nào có bộ lông biến thành hàng ngàn chiếc gai nhọn hoắt để tự vệ khi gặp nguy hiểm?", "Con Nhím", ["Tê tê", "Chuột chũi", "Lười"], "Khi bị tấn công, nhím cuộn tròn người lại thành một quả cầu gai sắc nhọn khiến kẻ thù khiếp sợ.", "6-7", 1, "MC"),

        # Thú biển & Đại dương (DV061 - DV100)
        ("Cá voi xanh", "Loài động vật to lớn nhất từng tồn tại trên Trái Đất (lớn hơn cả khủng long khổng lồ) là loài nào?", "Cá voi xanh", ["Cá mập trắng", "Mực khổng lồ", "Khủng long bạo chúa"], "Cá voi xanh có thể dài tới 30 mét, nặng gần 200 tấn và tim của nó to bằng một chiếc ô tô nhỏ.", "6-7", 1, "MC"),
        ("Cá voi thở bằng gì", "Cá voi là loài thú biển (động vật có vú) nên nó thở bằng cơ quan nào?", "Bằng Phổi (phải ngoi lên mặt nước thở)", ["Bằng Mang cá", "Bằng Da", "Bằng Đuôi"], "Cá voi không phải là cá, chúng đẻ con, cho con bú sữa mẹ và thở bằng phổi qua lỗ phun nước trên đỉnh đầu.", "7-8", 2, "MC"),
        ("Cá heo cứu người", "Loài động vật biển thông minh, thân thiện, hay cứu người và giao tiếp bằng tiếng lách cách vui nhộn?", "Cá heo", ["Cá mập", "Bạch tuộc", "Hải mã"], "Cá heo có bộ não rất phát triển, có thể nhận biết chính mình trong gương và bơi lướt sóng tuyệt đẹp.", "6-7", 1, "MC"),
        ("Cá mập răng sắc", "Loài săn mồi đại dương có bộ xương hoàn toàn bằng sụn, nhiều hàm răng sắc nhọn thay thế liên tục?", "Cá mập", ["Cá hồi", "Cá ngừ", "Cá heo"], "Cá mập có khứu giác cực nhạy có thể ngửi thấy một giọt máu loãng trong hàng triệu lít nước biển.", "7-8", 2, "MC"),
        ("Cá ngựa mang thai", "Loài sinh vật biển kỳ lạ nào có hình dáng giống quân mã cờ vua và do con đực mang thai sinh con?", "Cá ngựa", ["Sao biển", "Cá đuối", "Lươn biển"], "Cá ngựa đực có túi ấp trước bụng, cá cái đẻ trứng vào túi để cá đực thụ tinh và mang thai sinh con.", "7-8", 2, "MC"),
        ("Bạch tuộc phun mực", "Loài thân mềm có 8 chiếc tua dài mang giác bám, biết phun mực đen để trốn thoát kẻ thù là gì?", "Bạch tuộc", ["Mực ống", "Sứa biển", "Ốc sên"], "Bạch tuộc rất thông minh, có 3 trái tim, máu màu xanh lam và có thể biến đổi màu da ngụy trang tức thì.", "7-8", 2, "MC"),
        ("Mực bơi lùi", "Loài thân mềm biển có 10 xúc tua (8 tay ngắn và 2 tua dài) cùng chiếc mai nang bên trong là gì?", "Mực ống", ["Bạch tuộc", "Cua biển", "Nghêu"], "Mực bơi giật lùi bằng cách phụt luồng nước mạnh qua phễu nước, bơi rất nhanh khi gặp nguy hiểm.", "7-8", 2, "MC"),
        ("Sứa biển dập dềnh", "Loài sinh vật biển thân mềm trong suốt hình chiếc dù bồng bềnh, tua mang tế bào châm gây ngứa bỏng?", "Sứa biển", ["Hải quỳ", "San hô", "Sao biển"], "Cơ thể sứa chứa hơn 95% là nước, một số loài sứa biển có chất độc có thể gây nguy hiểm cho người tắm biển.", "7-8", 2, "MC"),
        ("Sao biển tái sinh", "Loài động vật da gai hình ngôi sao 5 cánh dưới đáy biển có khả năng tái sinh mọc lại cánh bị đứt?", "Sao biển", ["Cầu gai", "Hải sâm", "Cua biển"], "Nếu một cánh sao biển bị cá cắn đứt, nó có thể tự mọc lại cánh mới hoàn chỉnh sau một thời gian.", "7-8", 2, "MC"),
        ("Rùa biển đẻ trứng", "Loài bò sát biển có mai cứng bơi lội bằng 4 chi hình mái chèo và bơi hàng ngàn dặm về bờ cát đẻ trứng?", "Rùa biển (Vích)", ["Cá sấu biển", "Ba ba", "Hải cẩu"], "Rùa biển cái luôn nhớ đường bơi về đúng bãi cát nơi mình sinh ra năm xưa để đào hố đẻ trứng.", "7-8", 2, "MC"),
        ("Hải mã Bắc Cực", "Loài thú biển vùng Bắc Cực băng giá có cặp răng nanh dài chĩa xuống dưới và ria mép dày rậm?", "Hải mã (Moóc)", ["Hải cẩu", "Sư tử biển", "Cá voi"], "Cặp nanh của hải mã dùng để tự vệ, chiến đấu tranh giành lãnh thổ và cắm vào băng giúp kéo cơ thể lên cạn.", "8-9", 3, "MC"),
        ("Hải cẩu bơi lội", "Loài thú biển bơi lội thoăn thoắt dưới nước lạnh nhờ lớp mỡ dày và chi biến thành mái chèo?", "Hải cẩu", ["Gấu trắng", "Cá mập", "Rái cá"], "Hải cẩu có lớp mỡ dưới da dày giúp giữ ấm cơ thể trong làn nước đóng băng giá lạnh.", "7-8", 2, "MC"),
        ("San hô biển", "Những rạn san hô rực rỡ màu sắc dưới đáy biển là thực vật hay động vật?", "Là động vật (thuộc ngành ruột khoang)", ["Là thực vật biển", "Là các hòn đá ngầm vô tri", "Là một loại nấm"], "San hô thực chất là quần thể hàng triệu con polyp san hô bé nhỏ tiết ra canxi cacbonat tạo thành khung cứng.", "8-9", 3, "MC"),
        ("Cá hề sống cùng hải quỳ", "Loài cá nhỏ sặc sỡ màu cam sọc trắng sống an toàn giữa các xúc tua có độc của hải quỳ là gì?", "Cá hề (Clownfish)", ["Cá bảy màu", "Cá betta", "Cá chép"], "Cá hề có lớp chất nhầy đặc biệt trên da giúp nó không bị nọc độc của hải quỳ làm tổn thương.", "6-7", 1, "MC"),
        ("Cá đuối cánh diều", "Loài cá biển có thân hình dẹt phẳng như cánh diều, bơi lượn uốn lượn nhịp nhàng và đuôi có gai nhọn?", "Cá đuối", ["Cá thờn bơn", "Cá chim", "Cá thu"], "Cá đuối có bộ xương bằng sụn, mắt ở mặt trên còn miệng và khe mang nằm ở mặt dưới bụng.", "7-8", 2, "MC"),
        ("Cá voi sát thủ", "Loài cá heo lớn nhất có khoang màu đen trắng, thông minh và săn mồi theo bầy đàn cừ khôi ở biển cả là gì?", "Cá voi sát thủ (Orca)", ["Cá nhà táng", "Cá voi lưng gù", "Cá mập búa"], "Orca thuộc họ cá heo, chúng có ngôn ngữ giao tiếp phức tạp và chiến thuật săn mồi phối hợp đỉnh cao.", "8-9", 3, "MC"),
        ("Cá chuồn bay", "Loài cá biển có vây ngực nở rộng như cánh chim, có thể phóng lên khỏi mặt nước và lướt trên không trung?", "Cá chuồn", ["Cá hồi", "Cá nục", "Cá trích"], "Cá chuồn bay lướt trên mặt nước hàng chục mét để thoát khỏi sự truy đuổi của cá săn mồi bên dưới.", "8-9", 3, "MC"),
        ("Cá hồi vượt thác", "Loài cá nào sinh ra ở sông suối nước ngọt, bơi ra biển lớn sinh sống rồi bơi ngược dòng về nguồn đẻ trứng?", "Cá hồi", ["Cá rô", "Cá tra", "Cá chim"], "Cá hồi vượt thác ghềnh ngoạn mục hàng ngàn km bơi ngược dòng nước chảy xiết để trở về nơi chôn rau cắt rốn đẻ trứng.", "8-9", 3, "MC"),
        ("Cua bò ngang", "Loài giáp xác có mai cứng, 8 cẳng 2 càng và thường bò ngang là con gì?", "Con Cua", ["Con Tôm", "Con Ghẹ", "Ốc mượn hồn"], "Cua bò ngang do cấu tạo các khớp chân của nó chỉ uốn cong được sang hai bên sườn.", "6-7", 1, "MC"),
        ("Tôm búng đuôi", "Loài giáp xác bơi giật lùi bằng cách cong đuôi gập mạnh về phía trước bụng là loài nào?", "Con Tôm", ["Con Cua", "Con Mực", "Con Ốc"], "Đuôi tôm có quạt đuôi khỏe giúp nó búng ngược về phía sau với tốc độ cực nhanh để trốn kẻ thù.", "6-7", 1, "MC"),

        # Thế giới loài chim (DV081 - DV115)
        ("Đại bàng chúa tể", "Loài chim săn mồi dũng mãnh có móng vuốt quắp sắc bén, mắt tinh tường và mệnh danh là 'Chúa tể bầu trời'?", "Đại bàng", ["Bồ câu", "Kền kền", "Chim sẻ"], "Đại bàng có thể nhìn thấy con mồi nhỏ từ khoảng cách xa hàng km khi đang bay lượn trên tầng mây cao.", "6-7", 1, "MC"),
        ("Cú mèo mắt to", "Loài chim săn chuột ban đêm có đôi mắt to tròn nhìn thẳng và có thể quay đầu gần 270 độ?", "Cú mèo", ["Chim gõ kiến", "Vẹt", "Bồ nông"], "Cú mèo có thính giác siêu việt và lông cánh đặc biệt giúp bay hoàn toàn không gây ra tiếng động.", "7-8", 2, "MC"),
        ("Chim cánh cụt Nam Cực", "Loài chim sống ở vùng băng tuyết Nam Cực, không biết bay trên trời nhưng bơi lội dưới nước như tàu ngầm?", "Chim cánh cụt", ["Hải âu", "Đà điểu", "Thiên nga"], "Cánh chim cánh cụt biến đổi thành vây bơi chèo giúp nó lặn sâu hàng trăm mét bắt cá và tôm krill.", "6-7", 1, "MC"),
        ("Đà điểu chạy nhanh", "Loài chim lớn nhất thế giới, không biết bay nhưng chạy trên thảo nguyên nhanh như xe máy?", "Đà điểu", ["Chim ưng", "Thiên nga", "Công"], "Đà điểu có đôi chân dài cơ bắp với 2 ngón chân khỏe, có thể chạy đạt vận tốc tới 70 km/h.", "6-7", 1, "MC"),
        ("Chim ruồi bay lùi", "Loài chim bé nhỏ nhất thế giới có thể đập cánh 80 lần/giây, bay lùi và hút mật hoa khi đang lơ lửng?", "Chim ruồi", ["Chim sâu", "Chim sẻ", "Chim vành khuyên"], "Chim ruồi là loài chim duy nhất có thể bay giật lùi và bay đứng yên một chỗ như trực thăng.", "7-8", 2, "MC"),
        ("Chim gõ kiến bác sĩ", "Loài chim nào dùng mỏ cứng gõ liên tục vào thân cây để bắt sâu đục thân, được gọi là 'Bác sĩ của rừng xanh'?", "Chim gõ kiến", ["Bói cá", "Kền kền", "Tu hú"], "Hộp sọ của chim gõ kiến có đệm xốp đặc biệt bảo vệ não không bị chấn động khi gõ mỏ liên hồi vào gỗ cứng.", "7-8", 2, "MC"),
        ("Bói cá lao nhanh", "Loài chim có bộ lông xanh óng ánh, mỏ dài nhọn, thường đậu rình trên cành cây rồi lao vút xuống nước bắt cá?", "Chim bói cá", ["Chim bồ nông", "Cò trắng", "Diệc"], "Mũi tàu siêu tốc Shinkansen của Nhật Bản được thiết kế phỏng theo hình dáng khí động học của mỏ chim bói cá.", "8-9", 3, "MC"),
        ("Vẹt bắt chước", "Loài chim nhiệt đới có bộ lông sặc sỡ, mỏ quặp khỏe và có khả năng bắt chước tiếng người rất giỏi?", "Con Vẹt", ["Chim yến", "Sáo sậu", "Họa mi"], "Vẹt bắt chước được âm thanh nhờ cơ quan phát âm đặc biệt (syrinx) và chiếc lưỡi dày linh hoạt.", "6-7", 1, "MC"),
        ("Công xòe đuôi", "Loài chim quý có con đực xòe chiếc đuôi dài lộng lẫy như chiếc quạt hoa rực rỡ để thu hút bạn đời?", "Chim Công", ["Gà lôi", "Trĩ đỏ", "Thiên nga"], "Chiếc đuôi công thực chất là lông vũ che trên đuôi, có những đốm mắt sáng rực rỡ tuyệt mỹ.", "6-7", 1, "MC"),
        ("Thiên nga chung thủy", "Loài thủy cầm quý phái có bộ lông trắng muốt, chiếc cổ cong hình chữ S thanh nhã trên mặt hồ?", "Thiên nga", ["Vịt trời", "Ngỗng trời", "Bồ nông"], "Thiên nga sống chung thủy một vợ một chồng trọn đời, là biểu tượng của tình yêu son sắt.", "7-8", 2, "MC"),
        ("Bồ nông xúc cá", "Loài chim nước có chiếc túi da khổng lồ dưới mỏ dưới dùng như chiếc vợt xúc cá?", "Bồ nông", ["Hải âu", "Cò sen", "Vạc"], "Túi mỏ bồ nông có thể chứa tới 13 lít nước và cá, sau khi ép cạn nước nó mới nuốt cá vào bụng.", "7-8", 2, "MC"),
        ("Chim Yến làm tổ", "Loài chim nhỏ làm tổ trên vách đá cheo leo bằng nước bọt dãi quý giá tạo thành món yến sào bổ dưỡng?", "Chim Yến", ["Chim én", "Chim sẻ", "Chim chích"], "Tổ yến đảo tự nhiên được tạo hoàn toàn từ tuyến nước bọt của chim yến đan kết lại dẻo quánh.", "8-9", 3, "MC"),
        ("Kền kền dọn sạch", "Loài chim săn mồi có đầu trọc chuyên dọn sạch xác động vật chết, giúp ngăn ngừa dịch bệnh lây lan?", "Kền kền", ["Diều hâu", "Quạ khoang", "Cú mèo"], "Dạ dày kền kền chứa axit cực mạnh có thể tiêu diệt mọi vi khuẩn nguy hiểm trong xác thối rữa.", "8-9", 3, "MC"),
        ("Hải âu sải cánh", "Loài chim biển có sải cánh dài mênh mông, có thể bay lượn nhiều ngày liên tục trên biển mà không cần đập cánh?", "Hải âu", ["Bồ câu", "Chim ưng", "Nhạn biển"], "Hải âu tận dụng các luồng gió biển để bay lướt tiết kiệm sức lực trong những chuyến bay xuyên đại dương.", "8-9", 3, "MC"),
        ("Hồng hạc đứng một chân", "Loài chim có bộ lông màu hồng rực rỡ nhờ ăn tôm tảo và hay đứng ngủ thăng bằng trên một chân?", "Chim Hồng hạc (Flamingo)", ["Cò trắng", "Sếu đầu đỏ", "Bồ nông"], "Đứng một chân giúp hồng hạc tiết kiệm năng lượng và giảm bớt lượng nhiệt cơ thể thoát ra ngoài làn nước lạnh.", "7-8", 2, "MC"),

        # Bò sát, Lưỡng cư & Tập tính (DV116 - DV135)
        ("Vòng đời của ếch", "Loài lưỡng cư nào sinh ra từ nòng nọc dưới nước, khi lớn thở bằng phổi và da, nhảy bật bắt ruồi muỗi?", "Con Ếch", ["Con Thằn lằn", "Con Rắn", "Con Cá chép"], "Vòng đời của ếch trải qua biến thái: Trứng -> Nòng nọc (thở bằng mang) -> Ếch con (mọc chân, teo đuôi) -> Ếch trưởng thành.", "6-7", 1, "MC"),
        ("Cá sấu đầm lầy", "Loài bò sát khổng lồ sống ở sông đầm lầy, có bộ hàm răng cưa chết chóc và cú táp xoay người xé mồi?", "Cá sấu", ["Kỳ đà", "Khủng long", "Rùa đá"], "Cá sấu xuất hiện từ thời khủng long, có lớp da gai vảy sừng cứng rắn và lực cắn mạnh bậc nhất.", "7-8", 2, "MC"),
        ("Tắc kè hoa đổi màu", "Loài thằn lằn có khả năng thay đổi màu sắc da theo môi trường để ngụy trang và lưỡi bắn dài bắt côn trùng?", "Tắc kè hoa (Chameleon)", ["Thằn lằn bóng", "Kỳ nhông", "Rắn ráo"], "Tắc kè đổi màu nhờ các tế bào sắc tố đặc biệt dưới da, hai mắt nó có thể nhìn độc lập về 2 hướng khác nhau.", "7-8", 2, "MC"),
        ("Rắn lột xác", "Tại sao rắn và một số loài bò sát phải định kỳ lột bỏ lớp da cũ bên ngoài?", "Vì cơ thể lớn lên nhưng lớp da vảy sừng không co giãn được", ["Vì da cũ bị ngứa", "Để thay đổi màu da", "Để thu hút bạn tình"], "Rắn lột da cũ để cơ thể có không gian phát triển lớn hơn và loại bỏ các ký sinh trùng bám trên da.", "8-9", 3, "MC"),
        ("Rắn hổ mang", "Loài rắn độc nguy hiểm có thể phùng mang bạnh to và ngóc cao đầu đe dọa khi bị tấn công là gì?", "Rắn hổ mang", ["Rắn nước", "Trăn gấm", "Rắn ráo"], "Nọc độc của rắn hổ mang tấn công vào hệ thần kinh, cần hết sức cẩn thận và tránh xa.", "7-8", 2, "MC"),
        ("Trăn cuộn siết mồi", "Loài bò sát lớn không có nọc độc nhưng săn mồi bằng cách cuộn xiết chặt làm con mồi ngạt thở rồi nuốt chửng?", "Con Trăn", ["Rắn cạp nong", "Rắn lục", "Kỳ đà"], "Trăn có các khớp xương hàm mở rộng linh hoạt cho phép nuốt chửng con mồi to hơn cả đầu của nó.", "8-9", 3, "MC"),
        ("Thằn lằn đứt đuôi", "Khi bị kẻ thù tóm lấy đuôi, thằn lằn nhà (thạch sùng) tự vệ bằng cách nào?", "Tự đứt đuôi để nghi binh rồi tẩu thoát", ["Phun nọc độc", "Cắn đứt tay kẻ thù", "Giả chết nhắm mắt"], "Cái đuôi đứt vẫn tiếp tục giãy giụa đánh lạc hướng kẻ săn mồi, sau đó thằn lằn sẽ tự mọc lại đuôi mới.", "7-8", 2, "MC"),
        ("Rùa thụt đầu", "Loài bò sát di chuyển chậm chạp, có chiếc mai vòm cứng cáp có thể thụt cả đầu, đuôi và 4 chân vào trong?", "Con Rùa", ["Ốc sên", "Tê tê", "Cua"], "Mai rùa liền với xương sống và xương sườn của nó, là chiếc áo giáp kiên cố bảo vệ cơ thể suốt đời.", "6-7", 1, "MC"),
        ("Động vật hằng nhiệt", "Động vật hằng nhiệt (máu nóng) có đặc điểm sinh học nào sau đây?", "Nhiệt độ cơ thể luôn ổn định không đổi theo môi trường", ["Nhiệt độ thay đổi theo thời tiết bên ngoài", "Máu luôn luôn sôi ở 100 độ C", "Không bao giờ cần ăn uống"], "Chim và thú là động vật hằng nhiệt, có cơ chế điều hòa thân nhiệt giúp thích nghi tốt với mọi khí hậu.", "8-9", 3, "MC"),
        ("Động vật ngủ đông", "Tại sao gấu nâu và một số loài sóc lại ngủ đông suốt nhiều tháng lạnh giá?", "Để giảm tiêu hao năng lượng khi thức ăn ngoài tự nhiên khan hiếm", ["Vì chúng buồn ngủ do thời tiết tối", "Để trốn kẻ thù săn mồi", "Vì lông của chúng bị rụng hết"], "Khi ngủ đông, nhịp tim và thân nhiệt của gấu giảm sâu giúp sống dựa vào lớp mỡ tích lũy từ mùa thu.", "8-9", 3, "MC"),
        ("Thú mỏ vịt", "Loài thú kỳ lạ ở nước Úc có mỏ dẹt như vịt, chân có màng bơi nhưng lại đẻ trứng thay vì đẻ con?", "Thú mỏ vịt (Platypus)", ["Hải ly", "Chuột túi", "Chồn túi"], "Thú mỏ vịt là loài thú đơn huyệt quý hiếm: đẻ trứng nhưng nuôi con bằng sữa mẹ tiết ra trên da.", "8-9", 3, "MC"),
        ("Chim cánh cụt ấp trứng", "Ở loài chim cánh cụt hoàng đế, ai là người nhận nhiệm vụ kẹp quả trứng trên bàn chân để ấp suốt mùa đông buốt giá?", "Chim cánh cụt bố", ["Chim cánh cụt mẹ", "Cả đàn chim thay phiên nhau", "Trứng tự nở trong tuyết"], "Chim bố nhịn ăn suốt hơn 2 tháng, đứng chen chúc cùng nhau giữa bão tuyết để ấp quả trứng ấm áp trên mu bàn chân.", "8-9", 3, "MC"),
        ("Dơi là loài thú", "Con dơi biết bay lượn trên trời nhưng được xếp vào lớp Thú (động vật có vú) vì lý do nào?", "Dơi đẻ con và nuôi con non bằng sữa mẹ", ["Dơi có lông vũ", "Dơi đẻ trứng trong tổ", "Dơi có mỏ cứng"], "Dơi không phải loài chim, chúng đẻ con và cho con bú sữa mẹ giống như chó, mèo, người.", "7-8", 2, "MC"),
        ("Động vật biến nhiệt", "Loài động vật nào sau đây là động vật biến nhiệt (nhiệt độ cơ thể phụ thuộc vào môi trường)?", "Con Thằn lằn (bò sát)", ["Con Chó (thú)", "Con Gà (chim)", "Con Người"], "Bò sát, lưỡng cư và cá là động vật biến nhiệt, chúng hay sưởi nắng để làm ấm cơ thể.", "8-9", 3, "MC"),
        ("Rái cá dùng đá", "Rái cá biển có thói quen đặc biệt nào để mở những vỏ sò, vỏ ốc cứng?", "Đặt đá lên ngực rồi dùng tay đập vỏ sò vào đá", ["Dùng răng nhai nát", "Đem phơi nắng cho tự mở", "Nhờ cá heo cắn giùm"], "Rái cá là một trong số ít động vật thông minh biết sử dụng công cụ đá để lấy thức ăn.", "7-8", 2, "MC"),
        ("Ốc sên bò chậm", "Ốc sên di chuyển bằng bộ phận nào và tiết ra chất gì để dễ trườn bò trên mặt đất gai góc?", "Di chuyển bằng chân bụng và tiết chất nhầy nhớt", ["Bằng 4 chân nhỏ", "Bằng vây bơi", "Bằng các sợi râu"], "Lớp chất nhầy của ốc sên bảo vệ bàn chân bụng mềm mại không bị trầy xước kể cả khi bò qua lưỡi dao lam.", "6-7", 1, "MC"),
        ("Hươu cao cổ ngủ", "Mỗi ngày hươu cao cổ ngủ bao nhiêu tiếng để luôn cảnh giác đề phòng sư tử?", "Chỉ ngủ khoảng 30 phút chia làm nhiều giấc ngắn", ["Ngủ 12 tiếng liên tục", "Ngủ 24 tiếng cả ngày", "Không bao giờ ngủ"], "Để sinh tồn nơi hoang dã, hươu cao cổ thường đứng ngủ và chỉ chợp mắt vài phút mỗi lần.", "8-9", 3, "MC"),
        ("Bạch tuộc đổi màu", "Bạch tuộc ngụy trang hòa vào rạn san hô nhờ các cơ quan nào dưới da?", "Các tế bào sắc tố có thể co giãn linh hoạt", ["Nhờ lông vũ che chắn", "Nhờ phun sơn màu", "Nhờ ánh sáng mặt trời soi vào"], "Bạch tuộc có thể biến đổi màu sắc và cả kết cấu da sần sùi chỉ trong chưa đầy một giây.", "8-9", 3, "MC"),
        ("Chim bồ câu đưa thư", "Thời xưa con người dùng chim bồ câu để đưa thư tín đi xa vì chim bồ câu có khả năng gì?", "Khả năng nhớ đường và định hướng từ trường Trái Đất siêu giỏi", ["Chim biết đọc chữ viết", "Chim bay nhanh hơn máy bay", "Chim thích mang đồ nặng"], "Chim bồ câu có các hạt tinh thể từ tính trong mỏ giúp nó cảm nhận từ trường Trái Đất như một chiếc la bàn sinh học.", "8-9", 3, "MC"),
        ("Kỳ lân biển (Narwhal)", "Loài cá voi ở vùng biển băng Bắc Cực có chiếc ngà dài xoắn ốc chĩa thẳng trước đầu như kỳ lân là gì?", "Kỳ lân biển (Narwhal)", ["Cá voi xanh", "Cá nhà táng", "Cá voi sát thủ"], "Chiếc 'sừng' kỳ lân thực chất là chiếc răng nanh trên bên trái phát triển dài tới 3 mét chứa hàng triệu dây thần kinh cảm giác.", "8-9", 3, "MC")
    ]

    # SA questions (Tự luận ngắn DV136 - DV150)
    sa_items = [
        ("Vua sơn lâm", "Loài thú săn mồi dũng mãnh nào được mệnh danh là chúa sơn lâm?", "hổ|cọp|con hổ|con cọp", "Hổ là chúa sơn lâm dũng mãnh của rừng xanh.", "6-7", 1),
        ("Loài thú lớn nhất", "Loài động vật to lớn nhất thế giới sống dưới đại dương là gì?", "cá voi xanh|cá voi", "Cá voi xanh là sinh vật to lớn nhất hành tinh.", "6-7", 1),
        ("Bác sĩ rừng xanh", "Loài chim nào dùng mỏ gõ vào thân cây bắt sâu đục thân được gọi là bác sĩ rừng xanh?", "chim gõ kiến|gõ kiến", "Chim gõ kiến chữa bệnh cho cây cối bằng cách bắt sâu đục thân.", "7-8", 2),
        ("Loài chim chạy nhanh", "Loài chim lớn nhất thế giới không biết bay nhưng chạy rất nhanh là loài chim nào?", "đà điểu|chim đà điểu", "Đà điểu chạy nhanh tới 70 km/h trên thảo nguyên.", "6-7", 1),
        ("Loài thú có túi ở Úc", "Loài thú nhảy bằng hai chân sau và có túi trước bụng nổi tiếng của nước Úc là gì?", "kangaroo|chuột túi", "Kangaroo là biểu tượng độc đáo của nước Úc.", "6-7", 1),
        ("Loài thú chạy nhanh nhất", "Loài động vật chạy nhanh nhất trên cạn với vận tốc hơn 100 km/h là loài báo nào?", "cheetah|báo săn|báo săn cheetah", "Báo săn Cheetah là tay đua tốc độ số một trên mặt đất.", "7-8", 2),
        ("Loài chim lặn biển Nam Cực", "Loài chim không bay trên trời mà bơi lặn giỏi ở vùng Nam Cực băng giá là chim gì?", "chim cánh cụt|cánh cụt", "Chim cánh cụt có bộ lông chống thấm nước và cánh biến thành vây bơi.", "6-7", 1),
        ("Côn trùng hút mật", "Loài côn trùng siêng năng hút mật hoa về làm mật ong ngọt lịm là con gì?", "ong|con ong|ong mật", "Ong mật giúp thụ phấn cho hoa và làm ra mật ong quý giá.", "6-7", 1),
        ("Côn trùng phát sáng", "Loài côn trùng có thể tự phát ra ánh sáng lung linh ở bụng vào ban đêm là con gì?", "đom đóm|con đom đóm", "Đom đóm phát ra ánh sáng lạnh tự nhiên để tìm bạn tình.", "6-7", 1),
        ("Động vật đổi màu", "Loài thằn lằn nào có khả năng thay đổi màu sắc da để ngụy trang theo môi trường?", "tắc kè hoa|tắc kè", "Tắc kè hoa đổi màu để hòa lẫn vào cành lá tránh kẻ thù.", "7-8", 2),
        ("Bò sát đứt đuôi", "Con vật nào hay bò trên tường nhà, khi bị tóm đuôi sẽ tự đứt đuôi để tẩu thoát?", "thạch sùng|thằn lằn|con thằn lằn|con thạch sùng", "Thằn lằn tự đứt đuôi để cứu lấy mạng sống rồi sau đó mọc lại đuôi mới.", "7-8", 2),
        ("Loài thú biết bay", "Loài động vật có vú (thuộc lớp Thú) duy nhất biết bay lượn thực sự trên bầu trời là con gì?", "dơi|con dơi", "Dơi đẻ con và cho con bú sữa mẹ, cánh dơi là lớp màng da nối ngón tay.", "7-8", 2),
        ("Cá ngựa mang thai", "Ở loài cá ngựa, con bố hay con mẹ là người mang thai và sinh con non?", "con bố|cá đực|con đực|cá ngựa đực|cá bố", "Cá ngựa đực có túi ấp trước bụng nhận trứng từ cá cái để mang thai.", "8-9", 3),
        ("Thú ngủ nhiều ở Úc", "Loài gấu túi đáng yêu ở Úc ngủ tới 18-20 tiếng mỗi ngày và thích ăn lá cây bạch đàn là gì?", "koala|gấu koala|gấu túi koala", "Koala ngủ nhiều để tiêu hóa lá cây bạch đàn ít chất dinh dưỡng.", "7-8", 2),
        ("Khủng long tuyệt chủng", "Nhóm bò sát khổng lồ từng thống trị Trái Đất thời tiền sử rồi bị tuyệt chủng có tên là gì?", "khủng long", "Khủng long thống trị Trái Đất hàng trăm triệu năm trước khi tuyệt chủng.", "6-7", 1)
    ]

    qs = []
    # MC questions (135 câu)
    for i, it in enumerate(items, start=1):
        sub, q_text, correct, dist, expl, age, diff, qtype = it
        qid = f"DV{i:03d}"
        opts = [correct] + dist[:3]
        rng = random.Random(qid)
        rng.shuffle(opts)
        ans_letter = chr(ord('A') + opts.index(correct))
        img_url = imgs[(i - 1) % len(imgs)]
        qs.append({
            "id": qid,
            "topic": "Động Vật",
            "sub": sub,
            "age": age,
            "diff": diff,
            "type": "MC",
            "img": img_url,
            "q": q_text,
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
            "ans": ans_letter,
            "explain": expl
        })

    # SA questions (15 câu: DV136 - DV150)
    for j, sit in enumerate(sa_items, start=len(items) + 1):
        sub, q_text, ans_kw, expl, age, diff = sit
        qid = f"DV{j:03d}"
        img_url = imgs[(j - 1) % len(imgs)]
        qs.append({
            "id": qid,
            "topic": "Động Vật",
            "sub": sub,
            "age": age,
            "diff": diff,
            "type": "SA",
            "img": img_url,
            "q": q_text,
            "a": "",
            "b": "",
            "c": "",
            "d": "",
            "ans": ans_kw,
            "explain": expl
        })

    return qs

if __name__ == '__main__':
    qs = get_dv_questions()
    print(f"Topic 1 (Động Vật): {len(qs)} câu")
