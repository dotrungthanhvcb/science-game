# -*- coding: utf-8 -*-
"""
NGUỒN 1: SGK Việt Nam (GDPT 2018) - 100 câu hỏi (SGK001 -> SGK100)
Bám sát kiến thức môn Tự nhiên & Xã hội (lớp 1-3) và Khoa học (lớp 4-5) từ bộ Kết nối tri thức & Chân trời sáng tạo.
Chia làm 2 đợt:
- Đợt 1: 50 câu (Lớp 1, 2, 3)
- Đợt 2: 50 câu (Lớp 4, 5)
"""
import random

SOURCE_NAME = "SGK Việt Nam (GDPT 2018)"

def get_sgk_questions():
    questions = []

    # ĐỢT 1: 50 câu Lớp 1, 2, 3
    batch1 = [
        # Con người & Sức khỏe (15 câu)
        ("Để giữ vệ sinh thân thể sạch sẽ và phòng bệnh ngoài da, bé nên làm gì mỗi ngày?", ["Tắm rửa sạch sẽ hàng ngày và thay quần áo sạch", "Chỉ tắm vào dịp cuối tuần", "Mặc quần áo ẩm ướt", "Không cần rửa mặt"], 0, "Con người & Sức khỏe", "easy", 1, "Tắm rửa hàng ngày bằng xà phòng giúp làm sạch mồ hôi và vi khuẩn gây bệnh."),
        ("Khi ngồi học bài, khoảng cách thích hợp từ mắt đến mặt bàn học là bao nhiêu?", ["Khoảng 25 đến 30 cm", "Khoảng 5 cm sát mặt bàn", "Khoảng 1 mét", "Càng gần càng tốt"], 0, "Con người & Sức khỏe", "easy", 1, "Khoảng cách 25-30 cm giúp mắt không bị mỏi và phòng tránh tật cận thị học đường."),
        ("Bộ phận nào trong khoang miệng giúp bé nghiền nát thức ăn trước khi nuốt?", ["Răng", "Lưỡi", "Môi", "Nướu"], 0, "Con người & Sức khỏe", "easy", 1, "Răng có nhiệm vụ cắn, xé và nghiền nát thức ăn giúp dạ dày tiêu hóa dễ dàng."),
        ("Để bảo vệ hàm răng chắc khỏe, không bị sâu răng, em nên đánh răng vào lúc nào?", ["Sau khi ăn và trước khi đi ngủ buổi tối", "Chỉ đánh răng vào buổi sáng", "Một tuần đánh răng một lần", "Chỉ súc miệng nước ngọt"], 0, "Con người & Sức khỏe", "easy", 1, "Đánh răng ít nhất 2 lần/ngày giúp loại bỏ mảng bám thức ăn thừa gây sâu răng."),
        ("Cơ quan nào trong cơ thể giúp chúng ta hít thở không khí?", ["Cơ quan hô hấp (mũi, khí quản, phổi)", "Cơ quan tiêu hóa", "Cơ quan bài tiết", "Cơ quan thần kinh"], 0, "Con người & Sức khỏe", "easy", 2, "Cơ quan hô hấp lấy khí oxy từ không khí vào cơ thể và thải khí cacbonic ra ngoài."),
        ("Khi chạy nhanh, nhịp tim và nhịp thở của em thay đổi như thế nào?", ["Nhịp tim đập nhanh hơn và thở gấp hơn", "Nhịp tim đập chậm lại", "Ngừng thở hoàn toàn", "Không có thay đổi gì"], 0, "Con người & Sức khỏe", "easy", 2, "Khi vận động mạnh, các cơ bắp cần nhiều oxy và năng lượng nên tim đập nhanh hơn."),
        ("Cơ quan vận động của cơ thể người gồm có những bộ phận nào kết hợp lại?", ["Bộ xương và hệ cơ bắp", "Dạ dày và ruột non", "Não và tủy sống", "Tim và mạch máu"], 0, "Con người & Sức khỏe", "medium", 2, "Bộ xương làm khung nâng đỡ, các cơ bắp co giãn giúp cơ thể cử động và di chuyển."),
        ("Để xương và cơ phát triển khỏe mạnh, học sinh tiểu học cần làm gì?", ["Ăn uống đủ chất, tập thể dục thường xuyên và ngồi học đúng tư thế", "Thức khuya chơi điện tử", "Nhịn ăn sáng", "Chỉ ăn thịt không ăn rau"], 0, "Con người & Sức khỏe", "easy", 2, "Dinh dưỡng cân đối kết hợp vận động ngoài trời giúp xương chắc khỏe và tăng chiều cao."),
        ("Cơ quan bài tiết nước tiểu trong cơ thể gồm những bộ phận nào?", ["Hai quả thận, hai ống dẫn tiểu, bóng đái và ống đái", "Dạ dày và ruột già", "Phổi và khí quản", "Gan và mật"], 0, "Con người & Sức khỏe", "medium", 3, "Thận lọc chất thải trong máu tạo thành nước tiểu, dẫn xuống bóng đái trước khi thải ra ngoài."),
        ("Bộ não của con người được bảo vệ an toàn bên trong bộ phận xương nào?", ["Hộp sọ", "Lồng ngực", "Xương cột sống", "Xương chậu"], 0, "Con người & Sức khỏe", "easy", 3, "Hộp sọ bằng xương cứng bảo vệ bộ não - trung tâm điều khiển mọi hoạt động của cơ thể."),
        ("Để giữ cho hệ thần kinh luôn khỏe mạnh, trẻ em lứa tuổi tiểu học cần ngủ mấy tiếng mỗi ngày?", ["Khoảng 9 đến 10 tiếng mỗi đêm", "Khoảng 4 đến 5 tiếng", "Chỉ cần ngủ 2 tiếng", "Ngủ 15 tiếng cả ngày"], 0, "Con người & Sức khỏe", "medium", 3, "Giấc ngủ đủ giúp não bộ nghỉ ngơi, phục hồi năng lượng và phát triển trí tuệ."),
        ("Khi ho hoặc hắt hơi, em cần làm gì để không lây mầm bệnh cho người xung quanh?", ["Dùng khăn giấy hoặc khuỷu tay áo che miệng và mũi", "Hắt hơi thẳng vào mặt bạn", "Mở to miệng cười", "Lấy tay quẹt mũi rồi quẹt vào bàn"], 0, "Con người & Sức khỏe", "easy", 1, "Che miệng bằng khăn giấy hoặc khuỷu tay giúp ngăn chặn giọt bắn chứa vi khuẩn lây lan."),
        ("Hành động nào sau đây giúp phòng tránh tai nạn đuối nước cho học sinh?", ["Không tự ý rủ nhau tắm sông, hồ, ao khi không có người lớn giám sát", "Tự nhảy xuống hồ bơi sâu", "Bơi ra xa bờ biển khi có sóng to", "Chơi đùa gần bờ vực nước sâu"], 0, "Con người & Sức khỏe", "easy", 2, "Chỉ bơi lội ở nơi an toàn có phao cứu sinh và có sự giám sát của người lớn biết bơi."),
        ("Khi ngồi trên xe máy tham gia giao thông, học sinh bắt buộc phải làm gì?", ["Đội mũ bảo hiểm đạt chuẩn và cài quai đúng cách", "Chỉ đội mũ lưỡi trai", "Đứng lên yên xe", "Không cần đội gì cả"], 0, "Con người & Sức khỏe", "easy", 1, "Đội mũ bảo hiểm giúp giảm chấn thương vùng đầu khi không may xảy ra va chạm giao thông."),
        ("Để phòng chống bệnh sốt xuất huyết trong gia đình, chúng ta cần làm gì?", ["Diệt lăng quăng (bọ gậy), đậy kín lu chứa nước và ngủ màn", "Tưới nhiều nước đọng quanh nhà", "Mở cửa sổ cho muỗi bay vào", "Tích trữ rác thải ẩm ướt"], 0, "Con người & Sức khỏe", "medium", 3, "Loại bỏ nơi muỗi đẻ trứng bằng cách úp chum vại và thả cá diệt bọ gậy."),

        # Thực vật & Động vật (15 câu)
        ("Cây xanh có những bộ phận chính nào?", ["Rễ, thân, lá, hoa và quả", "Chỉ có rễ và lá", "Chỉ có thân gỗ", "Chỉ có hoa và quả"], 0, "Thực vật & Động vật", "easy", 1, "Mỗi bộ phận của cây xanh đảm nhiệm một chức năng riêng biệt giúp cây sinh trưởng."),
        ("Rễ cây có chức năng quan trọng nào đối với đời sống của cây?", ["Hút nước, chất khoáng từ đất và giúp cây bám chắc", "Hấp thụ ánh sáng mặt trời", "Tạo ra hạt giống mới", "Nở hoa kết quả"], 0, "Thực vật & Động vật", "easy", 2, "Rễ đâm sâu vào đất vừa hút nước nuôi cây vừa giữ cho thân cây không bị đổ ngã."),
        ("Lá cây thường có màu xanh lục là nhờ có chất gì?", ["Chất diệp lục", "Chất canxi", "Chất sắt", "Chất đường"], 0, "Thực vật & Động vật", "medium", 3, "Chất diệp lục trong lá cây giúp hấp thu năng lượng ánh sáng mặt trời để quang hợp."),
        ("Loài cây nào sau đây có rễ cọc đâm sâu vào lòng đất?", ["Cây bàng", "Cây lúa nước", "Cây ngô", "Cây hành lá"], 0, "Thực vật & Động vật", "medium", 3, "Cây bàng, cây phượng vĩ có rễ cọc to khỏe bám chắc vào đất sâu chống bão."),
        ("Cây lúa nước và cây ngô có loại rễ nào sau đây?", ["Rễ chùm", "Rễ cọc", "Rễ thở", "Rễ củ"], 0, "Thực vật & Động vật", "easy", 3, "Cây lúa và ngô có chùm rễ mọc tỏa đều từ gốc thân giúp hút dinh dưỡng ở tầng đất mặt."),
        ("Loài động vật nào sau đây đẻ con và nuôi con bằng sữa mẹ?", ["Con Chó", "Con Gà", "Con Vịt", "Con Cá chép"], 0, "Thực vật & Động vật", "easy", 2, "Chó, mèo, bò, lợn là động vật thuộc lớp Thú, đẻ con và cho con non bú sữa mẹ."),
        ("Loài động vật nào sau đây đẻ trứng?", ["Con Chim bồ câu", "Con Mèo", "Con Lợn", "Con Thỏ"], 0, "Thực vật & Động vật", "easy", 2, "Các loài chim và gia cầm như bồ câu, gà, vịt đều đẻ trứng rồi ấp nở thành con."),
        ("Cơ thể của loài côn trùng gồm có mấy phần chính?", ["3 phần: Đầu, ngực và bụng", "2 phần: Đầu và đuôi", "4 phần: Đầu, cổ, ngực, bụng", "Chỉ có 1 khối tròn"], 0, "Thực vật & Động vật", "medium", 3, "Côn trùng có cơ thể chia làm 3 phần (đầu, ngực, bụng) và thường có 6 chân ở phần ngực."),
        ("Loài côn trùng nào sau đây có ích cho nhà nông vì giúp thụ phấn cho hoa?", ["Con Ong mật", "Con Muỗi", "Con Ruồi", "Con Mối"], 0, "Thực vật & Động vật", "easy", 2, "Ong mật bay đi hút mật hoa, mang hạt phấn từ hoa này sang hoa khác giúp cây kết quả."),
        ("Con cá bơi lội dưới nước thở bằng cơ quan nào?", ["Mang cá", "Phổi", "Da", "Miệng"], 0, "Thực vật & Động vật", "easy", 2, "Nước chảy qua khe mang giúp các lá mang hấp thụ oxy hòa tan trong nước cho cá thở."),
        ("Loài chim nào bơi lặn giỏi dưới nước và có màng da nối giữa các ngón chân?", ["Con Vịt", "Con Gà trống", "Chim bồ câu", "Chim sẻ"], 0, "Thực vật & Động vật", "easy", 1, "Chân vịt có màng bơi như mái chèo giúp vịt đẩy nước bơi lội rất nhanh nhẹn."),
        ("Cây trinh nữ (cây xấu hổ) có phản ứng thú vị nào khi bị chạm tay vào?", ["Các lá con lập tức cụp khép lại", "Cây phát ra tiếng còi", "Lá cây rụng hết ngay", "Hoa nở bung tức thì"], 0, "Thực vật & Động vật", "easy", 3, "Đây là phản ứng tự vệ do áp suất nước thay đổi nhanh ở các khớp cuống lá."),
        ("Tại sao chúng ta cần bảo vệ các loài động vật hoang dã quý hiếm?", ["Để giữ gìn sự cân bằng sinh thái của tự nhiên", "Để lấy lông thú may áo", "Để nuôi nhốt trong nhà", "Vì động vật không có ích gì"], 0, "Thực vật & Động vật", "medium", 3, "Mỗi loài sinh vật đều có mắt xích quan trọng duy trì sự bền vững của thiên nhiên."),
        ("Con giun đất sống trong lòng đất có ích lợi gì cho cây trồng?", ["Làm tơi xốp đất và tăng độ màu mỡ cho đất", "Ăn phá hoại rễ cây", "Làm đất bị khô cằn", "Hút hết nước của cây"], 0, "Thực vật & Động vật", "easy", 2, "Giun đất đào hang làm đất thoáng khí và phân giun là loại phân hữu cơ giàu dưỡng chất."),
        ("Thực vật cần những yếu tố tự nhiên nào để sống và phát triển xanh tốt?", ["Nước, chất khoáng, không khí và ánh sáng mặt trời", "Chỉ cần bóng tối", "Chỉ cần nước ngọt có gas", "Không cần ánh sáng"], 0, "Thực vật & Động vật", "easy", 2, "Thiếu nước hoặc ánh sáng mặt trời, cây xanh sẽ bị héo úa và không thể quang hợp."),

        # Trái Đất & Bầu trời (10 câu)
        ("Mặt Trời mọc vào buổi sáng ở hướng nào và lặn vào buổi chiều ở hướng nào?", ["Mọc ở hướng Đông, lặn ở hướng Tây", "Mọc ở hướng Tây, lặn ở hướng Đông", "Mọc ở hướng Nam, lặn ở hướng Bắc", "Mọc ở hướng Bắc, lặn ở hướng Nam"], 0, "Trái Đất & Bầu trời", "easy", 1, "Trái Đất tự quay từ Tây sang Đông nên ta nhìn thấy Mặt Trời mọc ở đằng Đông, lặn ở đằng Tây."),
        ("Hiện tượng ngày và đêm luân phiên nhau trên Trái Đất là do đâu?", ["Do Trái Đất tự quay quanh trục của nó", "Do Mặt Trời tự tắt đèn", "Do Mặt Trăng che khuất", "Do mây bay che lấp"], 0, "Trái Đất & Bầu trời", "medium", 3, "Nửa Trái Đất được Mặt Trời chiếu sáng là ban ngày, nửa quay vào bóng tối là ban đêm."),
        ("Nước trong tự nhiên tồn tại ở mấy thể cơ bản?", ["3 thể: Thể rắn, thể lỏng và thể khí", "Chỉ có thể lỏng", "Chỉ có thể rắn", "2 thể: Nóng và lạnh"], 0, "Trái Đất & Bầu trời", "easy", 2, "Nước đá là thể rắn, nước sinh hoạt là thể lỏng, hơi nước bốc lên là thể khí."),
        ("Vòng tuần hoàn của nước trong tự nhiên gồm các quá trình chính nào?", ["Bay hơi -> Ngưng tụ thành mây -> Mưa rơi xuống đất", "Đông đá -> Nấu sôi -> Đổ ra biển", "Uống nước -> Rửa tay -> Quét nhà", "Nắng -> Gió -> Tuyết"], 0, "Trái Đất & Bầu trời", "medium", 3, "Hơi nước bốc lên cao gặp lạnh ngưng tụ thành mây, các giọt nước nặng rơi xuống thành mưa."),
        ("Gió được sinh ra do nguyên nhân tự nhiên nào?", ["Sự chuyển động của không khí từ nơi áp cao đến nơi áp thấp", "Do Trái Đất vẫy cánh", "Do Mặt Trời thổi hơi", "Do cây cối quạt gió"], 0, "Trái Đất & Bầu trời", "medium", 3, "Không khí ở các vùng nóng lạnh khác nhau tạo ra sự chênh lệch áp suất sinh ra luồng gió thổi."),
        ("Dấu hiệu nào sau đây cho thấy một cơn giông bão sắp kéo đến?", ["Mây đen kéo đến ùn ùn, gió thổi giật mạnh và sấm chớp lóe sáng", "Bầu trời trong xanh không một gợn mây", "Nắng ấm chan hòa", "Gió hiu hiu thổi nhẹ"], 0, "Trái Đất & Bầu trời", "easy", 2, "Khi thấy mây đen vần vũ và gió giật, các em cần nhanh chóng tìm nơi trú ẩn an toàn."),
        ("Cầu vồng bảy sắc thường xuất hiện trên bầu trời vào thời điểm nào?", ["Sau cơn mưa rào mùa hè khi trời hửng nắng", "Vào ban đêm không trăng", "Giữa trưa nắng hạn hán", "Khi trời có sương mù dày đặc"], 0, "Trái Đất & Bầu trời", "easy", 3, "Ánh sáng mặt trời bị khúc xạ và tán sắc qua các giọt nước mưa lơ lửng tạo thành 7 sắc cầu vồng."),
        ("Vào ngày rằm (15 âm lịch) hàng tháng, Mặt Trăng trên bầu trời có hình dạng thế nào?", ["Tròn vành vạnh và sáng rõ", "Hình lưỡi liềm khuyết", "Mặt Trăng biến mất hoàn toàn", "Hình ngôi sao"], 0, "Trái Đất & Bầu trời", "easy", 3, "Vào đêm rằm, toàn bộ phần nửa Mặt Trăng được chiếu sáng quay trực diện về phía Trái Đất."),
        ("Bản đồ địa lý nước Việt Nam có hình dáng giống chữ cái nào?", ["Hình chữ S", "Hình chữ O", "Hình chữ V", "Hình chữ T"], 0, "Trái Đất & Bầu trời", "easy", 1, "Dải đất non sông Việt Nam uốn lượn hình chữ S mềm mại trải dài ven bờ Biển Đông."),
        ("Thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là thành phố nào?", ["Thủ đô Hà Nội", "Thành phố Hồ Chí Minh", "Thành phố Đà Nẵng", "Thành phố Hải Phòng"], 0, "Trái Đất & Bầu trời", "easy", 1, "Hà Nội là trái tim của cả nước với nghìn năm lịch sử văn hiến hào hùng."),

        # Vật chất & Năng lượng (10 câu)
        ("Nước tinh khiết có những tính chất vật lý nào sau đây?", ["Không màu, không mùi, không vị và trong suốt", "Có màu xanh, vị ngọt mát", "Có mùi thơm hoa hồng", "Có vị mặn chát"], 0, "Vật chất & Năng lượng", "easy", 2, "Nước nguyên chất không màu, không mùi, không vị, chảy từ cao xuống thấp và hòa tan được muối, đường."),
        ("Chất nào sau đây có thể tan hoàn toàn trong nước?", ["Đường ăn và muối ăn", "Cát xây dựng", "Dầu ăn", "Sỏi đá"], 0, "Vật chất & Năng lượng", "easy", 2, "Đường và muối tan tạo thành dung dịch trong suốt, còn cát sỏi không tan lắng xuống đáy."),
        ("Chất nào sau đây không tan trong nước và nổi lên trên mặt nước?", ["Dầu ăn", "Muối ăn", "Đường kính", "Sữa bột"], 0, "Vật chất & Năng lượng", "easy", 2, "Dầu ăn nhẹ hơn nước và không phân cực nên không tan, luôn nổi thành lớp váng trên mặt nước."),
        ("Không khí xung quanh chúng ta có những tính chất nào?", ["Không màu, không mùi, không vị và chiếm không gian", "Có màu trắng đục như khói", "Có vị ngọt ngào", "Có hình dạng vuông vức"], 0, "Vật chất & Năng lượng", "medium", 2, "Không khí trong suốt vô hình, có thể bị nén lại hoặc giãn ra và có ở khắp mọi nơi."),
        ("Vật nào sau đây là nguồn sáng tự nhiên tự phát ra ánh sáng?", ["Mặt Trời", "Mặt Trăng", "Chiếc gương soi", "Mặt nước hồ phẳng lặng"], 0, "Vật chất & Năng lượng", "easy", 3, "Mặt Trời là ngôi sao tự phát sáng, còn Mặt Trăng và gương chỉ phản chiếu ánh sáng chiếu tới."),
        ("Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường nào?", ["Đường thẳng", "Đường cong lượn sóng", "Đường gấp khúc", "Đường tròn"], 0, "Vật chất & Năng lượng", "medium", 3, "Ánh sáng luôn truyền theo đường thẳng, nhờ đó ta ngắm hàng cây thẳng tắp dễ dàng."),
        ("Bóng tối của một vật xuất hiện ở phía nào của vật cản sáng?", ["Ở phía sau vật cản sáng (phía ngược với nguồn sáng)", "Ở phía trước nguồn sáng", "Ở ngay trên đỉnh đầu vật", "Bóng tối ở khắp mọi nơi"], 0, "Vật chất & Năng lượng", "easy", 3, "Vật cản ngăn không cho ánh sáng truyền qua, vùng phía sau không nhận được ánh sáng tạo thành bóng tối."),
        ("Âm thanh phát ra từ một vật thể khi vật thể đó có hiện tượng gì?", ["Vật thể dao động rung rinh", "Vật thể đứng yên bất động", "Vật thể nóng chảy", "Vật thể đổi màu"], 0, "Vật chất & Năng lượng", "medium", 3, "Khi ta gảy dây đàn guitar hoặc gõ mặt trống, chúng rung lên phát ra sóng âm thanh."),
        ("Âm thanh có thể truyền qua những môi trường nào sau đây?", ["Chất rắn, chất lỏng và chất khí", "Chỉ truyền qua không khí", "Chỉ truyền dưới nước", "Không truyền qua chất rắn"], 0, "Vật chất & Năng lượng", "medium", 3, "Âm thanh truyền nhanh nhất qua chất rắn (như thép, đất), chậm nhất qua chất khí."),
        ("Vật liệu nào sau đây là vật liệu dẫn nhiệt tốt?", ["Kim loại nhôm, đồng, sắt", "Gỗ khô", "Nhựa xốp", "Vải len"], 0, "Vật chất & Năng lượng", "easy", 3, "Kim loại dẫn nhiệt nhanh nên được dùng làm xoong nồi nấu nướng thức ăn mau sôi.")
    ]

    # ĐỢT 2: 50 câu Lớp 4, 5
    batch2 = [
        # Vật chất & Năng lượng (15 câu)
        ("Nước sôi ở nhiệt độ bao nhiêu độ C trong điều kiện áp suất khí quyển tiêu chuẩn?", ["100 độ C", "0 độ C", "50 độ C", "200 độ C"], 0, "Vật chất & Năng lượng", "easy", 4, "Ở áp suất 1 atm, nước tinh khiết sôi sùng sục và bốc hơi mãnh liệt ở mốc 100 độ C."),
        ("Nước tinh khiết bắt đầu đóng băng thành thể rắn ở nhiệt độ bao nhiêu độ C?", ["0 độ C", "100 độ C", "10 độ C", "-50 độ C"], 0, "Vật chất & Năng lượng", "easy", 4, "Mốc 0 độ C là nhiệt độ đông đặc của nước lỏng thành các tinh thể đá rắn."),
        ("Khí nào trong không khí là cần thiết nhất cho sự hô hấp của sinh vật và duy trì sự cháy?", ["Khí Oxy", "Khí Nitơ", "Khí Cacbonic", "Khí Heli"], 0, "Vật chất & Năng lượng", "easy", 4, "Khí oxy chiếm khoảng 21% thể tích không khí, duy trì sự sống hô hấp và sự cháy."),
        ("Để dập tắt một đám cháy nhỏ do chập điện, hành động đúng đắn đầu tiên là gì?", ["Ngắt cầu dao điện tổng ngay lập tức", "Dội nước lã vào đám cháy", "Thổi phù vào ngọn lửa", "Dùng quạt quạt mạnh"], 0, "Vật chất & Năng lượng", "medium", 5, "Nước dẫn điện gây nguy hiểm chết người, cần ngắt điện trước rồi dùng bình chữa cháy chuyên dụng."),
        ("Vật liệu nào sau đây là vật liệu cách điện tốt và an toàn?", ["Nhựa, cao su và thủy tinh", "Thanh đồng", "Dây nhôm", "Nước muối"], 0, "Vật chất & Năng lượng", "easy", 4, "Nhựa và cao su không cho dòng điện chạy qua nên được dùng làm vỏ bọc ngoài dây điện."),
        ("Mạch điện gồm có pin, bóng đèn và dây nối sẽ phát sáng khi nào?", ["Khi mạch điện được nối kín hoàn chỉnh", "Khi mạch điện bị đứt hở", "Khi tháo pin ra ngoài", "Khi tắt công tắc"], 0, "Vật chất & Năng lượng", "easy", 4, "Dòng điện chỉ có thể chạy qua một mạch điện kín liên tục từ cực dương qua bóng đèn về cực âm."),
        ("Nguồn năng lượng nào sau đây là nguồn năng lượng tái tạo sạch và vô tận?", ["Năng lượng mặt trời và năng lượng gió", "Than đá", "Dầu mỏ", "Khí đốt tự nhiên"], 0, "Vật chất & Năng lượng", "medium", 5, "Năng lượng mặt trời, gió và thủy triều liên tục được tái tạo tự nhiên và không gây ô nhiễm."),
        ("Nhiên liệu hóa thạch nào sau đây nếu khai thác cạn kiệt sẽ không thể tự phục hồi lại?", ["Than đá và dầu mỏ", "Ánh sáng mặt trời", "Sức gió", "Dòng nước chảy"], 0, "Vật chất & Năng lượng", "medium", 5, "Nhiên liệu hóa thạch hình thành từ xác sinh vật chôn vùi hàng triệu năm, cần sử dụng tiết kiệm."),
        ("Khi trộn xi măng, cát và nước theo tỉ lệ thích hợp ta thu được vật liệu gì trong xây dựng?", ["Vữa xi măng", "Đá hoa cương", "Đất sét", "Thạch cao"], 0, "Vật chất & Năng lượng", "easy", 4, "Vữa xi măng kết dính các viên gạch lại với nhau tạo nên những bức tường nhà kiên cố."),
        ("Kim loại nhôm có những đặc tính nổi bật nào sau đây?", ["Màu trắng bạc, nhẹ, dẫn điện dẫn nhiệt tốt và không bị rỉ sét", "Màu đen kịt, rất nặng", "Rất giòn dễ vỡ vụn", "Không dẫn nhiệt"], 0, "Vật chất & Năng lượng", "medium", 4, "Nhôm nhẹ và bền nên được ứng dụng làm vỏ máy bay, xoong nồi nhôm và khung cửa sổ."),
        ("Đồng là kim loại có màu đỏ cam dẻo dai, được ứng dụng phổ biến nhất để làm gì?", ["Làm lõi dây dẫn điện", "Làm lốp xe ô tô", "Làm phấn viết bảng", "Làm bóng đèn chiếu sáng"], 0, "Vật chất & Năng lượng", "easy", 4, "Đồng dẫn điện rất tốt và dễ uốn kéo thành sợi dài làm lõi dây điện gia đình."),
        ("Hiện tượng biến đổi hóa học xảy ra trong trường hợp nào sau đây?", ["Đinh sắt để ngoài không khí ẩm bị rỉ sét thành chất mới màu nâu", "Xé một tờ giấy thành nhiều mảnh nhỏ", "Đá viên tan thành nước lỏng", "Hòa tan đường vào cốc nước"], 0, "Vật chất & Năng lượng", "hard", 5, "Biến đổi hóa học là sự biến đổi từ chất này thành chất khác có tính chất hoàn toàn mới."),
        ("Hiện tượng biến đổi vật lý xảy ra trong trường hợp nào sau đây?", ["Đá viên tan chảy thành nước lỏng", "Đốt cháy que diêm thành than đen", "Quả trứng chiên chín", "Đinh sắt bị rỉ sét"], 0, "Vật chất & Năng lượng", "medium", 5, "Biến đổi vật lý chỉ làm thay đổi trạng thái, hình dạng hoặc kích thước mà không sinh ra chất mới."),
        ("Tại sao đáy của những chiếc xoong nồi nấu bếp thường làm bằng kim loại inox hoặc nhôm?", ["Để dẫn nhiệt nhanh giúp thức ăn mau chín và tiết kiệm ga", "Để làm nồi nặng hơn", "Để chống nóng", "Để nồi cách điện"], 0, "Vật chất & Năng lượng", "easy", 4, "Kim loại dẫn nhiệt tốt giúp truyền nhiệt lượng nhanh chóng từ ngọn lửa vào thức ăn."),
        ("Hành động nào sau đây giúp tiết kiệm điện năng trong gia đình?", ["Tắt đèn và các thiết bị điện khi ra khỏi phòng", "Bật tivi cả ngày khi không xem", "Mở cửa tủ lạnh thật lâu", "Bật điều hòa ở nhiệt độ 16 độ C liên tục"], 0, "Vật chất & Năng lượng", "easy", 4, "Tắt điện khi không sử dụng vừa tiết kiệm tiền điện vừa giảm bớt khí thải nhà kính cho môi trường."),

        # Thực vật & Động vật (15 câu)
        ("Quá trình quang hợp của cây xanh diễn ra chủ yếu ở bộ phận nào?", ["Lá cây (nhờ có chất diệp lục)", "Rễ cây đâm sâu", "Vỏ thân cây", "Cánh hoa rực rỡ"], 0, "Thực vật & Động vật", "easy", 4, "Lá cây hấp thu ánh sáng mặt trời để tổng hợp chất hữu cơ nuôi cây và thải khí oxy."),
        ("Trong quá trình quang hợp vào ban ngày, cây xanh hấp thụ khí gì và nhả ra khí gì?", ["Hấp thụ khí cacbonic (CO2) và nhả ra khí oxy (O2)", "Hấp thụ khí oxy và nhả khí cacbonic", "Hấp thụ khí nitơ và nhả khí gas", "Hấp thụ khói bụi và nhả nước"], 0, "Thực vật & Động vật", "medium", 4, "Nhờ quang hợp nhả khí oxy, cây xanh được mệnh danh là 'lá phổi xanh của Trái Đất'."),
        ("Vào ban đêm khi không có ánh sáng mặt trời, cây xanh thực hiện quá trình nào?", ["Cây hô hấp (hít khí oxy và thải khí cacbonic)", "Cây tiếp tục quang hợp", "Cây ngừng hoạt động hoàn toàn", "Cây tự phát sáng"], 0, "Thực vật & Động vật", "medium", 4, "Vì ban đêm cây xanh hô hấp lấy oxy nên không nên để quá nhiều chậu cây xanh trong phòng ngủ đóng kín."),
        ("Hoa là cơ quan sinh sản của thực vật có hoa, gồm những bộ phận chính nào?", ["Đài hoa, cánh hoa (tràng hoa), nhị hoa và nhụy hoa", "Chỉ có cánh hoa và lá", "Rễ và thân cành", "Quả và hạt"], 0, "Thực vật & Động vật", "medium", 5, "Nhị hoa là cơ quan sinh dục đực sinh hạt phấn, nhụy hoa là cơ quan sinh dục cái chứa noãn."),
        ("Sau khi hoa được thụ phấn và thụ tinh, bầu nhụy sẽ phát triển thành bộ phận gì?", ["Quả chứa hạt", "Cành cây mới", "Chiếc lá xanh", "Gai nhọn"], 0, "Thực vật & Động vật", "medium", 5, "Noãn biến đổi thành hạt mang mầm sống mới, bầu nhụy dày lên tạo thành thịt quả thơm ngon."),
        ("Hạt giống cây xanh cần những điều kiện tự nhiên nào để nảy mầm thuận lợi?", ["Đủ nước, không khí và nhiệt độ thích hợp", "Chỉ cần bóng tối", "Cần nhiệt độ đóng băng", "Cần gió bão mạnh"], 0, "Thực vật & Động vật", "easy", 4, "Hạt hút nước trương nở, lấy oxy hô hấp và cần nhiệt độ ấm áp của đất để phôi nảy mầm."),
        ("Hình thức sinh sản của các loài thú (động vật có vú) có đặc điểm nào?", ["Đẻ con và nuôi con non bằng sữa mẹ", "Đẻ trứng trong tổ", "Tự phân đôi cơ thể", "Đẻ trứng dưới đáy nước"], 0, "Thực vật & Động vật", "easy", 4, "Các loài thú như trâu, bò, hổ, voi, cá heo đều mang thai, đẻ con và cho con bú sữa mẹ."),
        ("Vòng đời sinh trưởng và biến thái của loài bướm trải qua 4 giai đoạn nào?", ["Trứng -> Sâu bướm (ấu trùng) -> Nhộng trong kén -> Bướm trưởng thành", "Trứng -> Bướm con -> Bướm lớn", "Nhộng -> Trứng -> Sâu", "Sâu -> Trứng -> Bướm"], 0, "Thực vật & Động vật", "medium", 5, "Đây là hiện tượng biến thái hoàn toàn kỳ diệu của côn trùng trong thế giới tự nhiên."),
        ("Vòng đời của con ếch đồng trải qua các giai đoạn biến thái nào?", ["Trứng -> Nòng nọc (thở bằng mang) -> Ếch con -> Ếch trưởng thành", "Trứng -> Ếch con mọc cánh", "Đẻ con trực tiếp", "Nòng nọc đẻ trứng"], 0, "Thực vật & Động vật", "medium", 4, "Nòng nọc sống dưới nước thở bằng mang, khi lớn lên rụng đuôi, mọc 4 chân và thở bằng phổi, da."),
        ("Chuỗi thức ăn trong tự nhiên thường được bắt đầu bằng mắt xích sinh vật nào?", ["Sinh vật sản xuất (cây xanh quang hợp)", "Động vật ăn thịt", "Vi khuẩn phân hủy", "Con người"], 0, "Thực vật & Động vật", "medium", 4, "Cây xanh tự chế tạo chất hữu cơ từ năng lượng mặt trời là nguồn thức ăn ban đầu cho động vật ăn cỏ."),
        ("Trong chuỗi thức ăn: 'Cỏ -> Châu chấu -> Ếch đồng -> Rắn', con ếch đóng vai trò gì?", ["Động vật ăn thịt tiêu thụ châu chấu", "Sinh vật sản xuất thức ăn", "Sinh vật phân hủy cỏ", "Vật không có vai trò gì"], 0, "Thực vật & Động vật", "medium", 4, "Ếch đồng là động vật ăn động vật (ăn côn trùng), là mắt xích kiểm soát số lượng châu chấu phá hoại mùa màng."),
        ("Tại sao việc chặt phá rừng đầu nguồn bừa bãi lại làm gia tăng lũ lụt và sạt lở đất?", ["Rễ cây rừng giữ đất và thảm thực vật cản dòng chảy của nước mưa", "Cây rừng làm trời mưa to hơn", "Chặt cây làm đất màu mỡ hơn", "Rừng không có tác dụng giữ nước"], 0, "Thực vật & Động vật", "hard", 5, "Mất rừng đầu nguồn khiến nước mưa xối thẳng xuống sườn núi dốc tạo thành lũ quét và lở đất kinh hoàng."),
        ("Loài chim di cư bay tránh rét vào mùa đông theo đội hình hình chữ gì để tiết kiệm sức?", ["Đội hình hình chữ V", "Đội hình hình tròn", "Bay lộn xộn", "Bay một hàng ngang"], 0, "Thực vật & Động vật", "easy", 4, "Đội hình chữ V giúp các con chim bay sau tận dụng luồng khí nâng từ cánh của con chim đầu đàn."),
        ("Loài thú biển nào to lớn nhất hành tinh, đẻ con và thở bằng phổi qua lỗ phun nước?", ["Cá voi xanh", "Cá mập trắng", "Bạch tuộc khổng lồ", "Mực ống đại dương"], 0, "Thực vật & Động vật", "easy", 4, "Cá voi xanh là loài thú biển thuộc lớp động vật có vú, không phải loài cá thở bằng mang."),
        ("Hiện tượng ngủ đông của một số loài động vật (như gấu nâu) nhằm mục đích gì?", ["Giảm tiêu hao năng lượng khi thời tiết giá rét khan hiếm thức ăn", "Vì chúng thích ngủ nướng", "Để trốn kẻ săn mồi", "Vì mắt bị mỏi"], 0, "Thực vật & Động vật", "medium", 5, "Khi ngủ đông, thân nhiệt và nhịp tim của gấu giảm sâu giúp sống sót nhờ lớp mỡ tích lũy.")
    ]

    # Thêm 10 câu Trái Đất & Bầu trời + Con người lớp 4,5
    batch3 = [
        ("Nước ta nằm trong đới khí hậu nào trên Trái Đất?", ["Đới khí hậu nhiệt đới gió mùa", "Đới hàn đới quanh năm băng giá", "Đới ôn đới bốn mùa tuyết rơi", "Đới hoang mạc khô cằn"], 0, "Trái Đất & Bầu trời", "easy", 5, "Khí hậu nhiệt đới gió mùa ẩm mang lại lượng mưa dồi dào và cây cối xanh tươi bốn mùa."),
        ("Đồng bằng châu thổ màu mỡ lớn nhất nước ta ở phương Nam là đồng bằng nào?", ["Đồng bằng sông Cửu Long", "Đồng bằng sông Hồng", "Đồng bằng Thanh Nghệ Tĩnh", "Đồng bằng ven biển miền Trung"], 0, "Trái Đất & Bầu trời", "easy", 4, "Đồng bằng sông Cửu Long do phù sa sông Tiền và sông Hậu bồi đắp là vựa lúa lớn nhất nước ta."),
        ("Con sông lớn nhất miền Bắc chở nặng phù sa đỏ bồi đắp đồng bằng Bắc Bộ là gì?", ["Sông Hồng", "Sông Đà", "Sông Cầu", "Sông Đáy"], 0, "Trái Đất & Bầu trời", "easy", 4, "Sông Hồng gắn liền với nền văn minh sông Hồng và hệ thống đê điều kiên cố ngàn năm."),
        ("Đỉnh núi cao nhất Việt Nam và toàn bán đảo Đông Dương (cao 3.143m) là đỉnh nào?", ["Đỉnh Fansipan (Lào Cai)", "Đỉnh Tây Côn Lĩnh", "Đỉnh Bạch Mã", "Đỉnh Mẫu Sơn"], 0, "Trái Đất & Bầu trời", "easy", 4, "Fansipan thuộc dãy Hoàng Liên Sơn hùng vĩ được mệnh danh là 'Nóc nhà Đông Dương'."),
        ("Quần đảo Hoàng Sa và Trường Sa thuộc chủ quyền thiêng liêng của quốc gia nào?", ["Việt Nam", "Trung Quốc", "Philippines", "Malaysia"], 0, "Trái Đất & Bầu trời", "easy", 4, "Hoàng Sa và Trường Sa là một phần lãnh thổ máu thịt thiêng liêng không thể tách rời của Tổ quốc Việt Nam."),
        ("Bệnh bướu cổ và thiểu năng trí tuệ ở trẻ em có thể phòng tránh bằng cách nào?", ["Sử dụng muối ăn có bổ sung khoáng chất I-ốt trong bữa ăn", "Uống nhiều nước ngọt", "Ăn nhiều bánh kẹo", "Kiêng ăn muối hoàn toàn"], 0, "Con người & Sức khỏe", "medium", 5, "I-ốt là vi chất dinh dưỡng thiết yếu cho tuyến giáp và sự phát triển trí não của trẻ nhỏ."),
        ("Bệnh cận thị ở học sinh có thể phòng tránh bằng thói quen tốt nào sau đây?", ["Ngồi học đủ ánh sáng, ngồi thẳng lưng và hạn chế nhìn màn hình điện thoại quá gần", "Nằm đọc sách trên giường", "Dí sát mắt vào sách", "Xem tivi trong bóng tối"], 0, "Con người & Sức khỏe", "easy", 4, "Thực hiện quy tắc nghỉ ngơi mắt 20-20-20 giúp bảo vệ đôi mắt luôn sáng khỏe tinh tường."),
        ("Thói quen ăn quá nhiều đồ ăn mặn (chứa nhiều muối) có thể gây tác hại gì cho cơ thể?", ["Gây tăng huyết áp và quá tải cho hai quả thận", "Làm sâu răng", "Làm cơ thể yếu cơ", "Làm rụng tóc"], 0, "Con người & Sức khỏe", "medium", 5, "Ăn nhạt thanh đạm giúp bảo vệ quả thận và giữ cho hệ tim mạch luôn khỏe mạnh bền bỉ."),
        ("Tuổi dậy thì ở lứa tuổi học sinh thường bắt đầu diễn ra ở khoảng độ tuổi nào?", ["Từ 10 đến 15 tuổi (ở nữ) và từ 11 đến 16 tuổi (ở nam)", "Từ 1 đến 3 tuổi", "Từ 30 đến 40 tuổi", "Từ 60 tuổi trở lên"], 0, "Con người & Sức khỏe", "medium", 5, "Tuổi dậy thì đánh dấu bước phát triển nhảy vọt về thể chất, chiều cao và sự thay đổi tâm sinh lý."),
        ("Để giữ gìn vệ sinh và sức khỏe trong giai đoạn tuổi dậy thì, các em cần làm gì?", ["Tắm rửa sạch sẽ, ăn uống đủ chất, chia sẻ tâm sự với cha mẹ thầy cô", "Tự ti giấu giếm lo sợ", "Nhịn ăn giảm cân quá mức", "Thức khuya xem phim"], 0, "Con người & Sức khỏe", "easy", 5, "Hiểu biết đúng đắn về sự thay đổi cơ thể giúp các em tự tin và trưởng thành khỏe mạnh.")
    ]

    all_raw = batch1 + batch2 + batch3
    print(f"Total SGK questions prepared: {len(all_raw)}")

    # Gán ID từ SGK001 đến SGK100
    for idx, item in enumerate(all_raw, start=1):
        q_text, opts, c_idx, topic, level, grade, expl = item
        qid = f"SGK{idx:03d}"
        
        # Shuffle options nhưng cập nhật c_idx chính xác
        correct_text = opts[c_idx]
        shuffled_opts = list(opts)
        rng = random.Random(qid)
        rng.shuffle(shuffled_opts)
        new_c_idx = shuffled_opts.index(correct_text)
        ans_letter = chr(ord('A') + new_c_idx)

        diff_num = 1 if level == "easy" else (2 if level == "medium" else 3)

        questions.append({
            "id": qid,
            "q": q_text,
            "question": q_text,
            "options": shuffled_opts,
            "correctIndex": new_c_idx,
            "a": shuffled_opts[0],
            "b": shuffled_opts[1],
            "c": shuffled_opts[2],
            "d": shuffled_opts[3],
            "ans": ans_letter,
            "source": SOURCE_NAME,
            "topic": topic,
            "difficulty": level,
            "diff": diff_num,
            "grade": grade,
            "explain": expl,
            "img": ""
        })

    # Thêm 10 câu để tròn 100 câu
    for idx, item in enumerate(extra_sgk_10, start=len(questions) + 1):
        q_text, opts, c_idx, topic, level, grade, expl = item
        qid = f"SGK{idx:03d}"
        correct_text = opts[c_idx]
        shuffled_opts = list(opts)
        rng = random.Random(qid)
        rng.shuffle(shuffled_opts)
        new_c_idx = shuffled_opts.index(correct_text)
        ans_letter = chr(ord('A') + new_c_idx)
        diff_num = 1 if level == "easy" else (2 if level == "medium" else 3)
        questions.append({
            "id": qid,
            "q": q_text,
            "question": q_text,
            "options": shuffled_opts,
            "correctIndex": new_c_idx,
            "a": shuffled_opts[0],
            "b": shuffled_opts[1],
            "c": shuffled_opts[2],
            "d": shuffled_opts[3],
            "ans": ans_letter,
            "source": SOURCE_NAME,
            "topic": topic,
            "difficulty": level,
            "diff": diff_num,
            "grade": grade,
            "explain": expl,
            "img": ""
        })

    return questions

# Bổ sung 10 câu để tròn đúng 100 câu SGK
extra_sgk_10 = [
    ("Muỗi vằn là sinh vật trung gian truyền loại bệnh nguy hiểm nào?", ["Bệnh sốt xuất huyết", "Bệnh cúm thông thường", "Bệnh sâu răng", "Bệnh cận thị"], 0, "Con người & Sức khỏe", "easy", 3, "Muỗi vằn truyền virus Dengue gây bệnh sốt xuất huyết, cần tích cực diệt bọ gậy."),
    ("Ruồi nhà đậu vào thức ăn có thể làm lây lan những bệnh nào cho con người?", ["Bệnh về đường tiêu hóa như tả, lỵ, tiêu chảy", "Bệnh cận thị", "Bệnh đau mắt hột", "Bệnh gãy xương"], 0, "Con người & Sức khỏe", "easy", 2, "Ruồi mang hàng triệu vi khuẩn trên lông chân làm ô nhiễm thức ăn, cần đậy lồng bàn kín."),
    ("Để tránh bị ngộ độc thực phẩm trong gia đình, chúng ta cần thực hiện nguyên tắc nào?", ["Ăn chín, uống sôi, không ăn thức ăn ôi thiu", "Ăn thức ăn để lâu ngày bốc mùi", "Uống nước lã chưa đun", "Ăn rau sống chưa rửa"], 0, "Con người & Sức khỏe", "easy", 3, "Nhiệt độ đun sôi 100 độ C giúp tiêu diệt hầu hết vi khuẩn gây hại trong thực phẩm."),
    ("Cây khoai lang và cây sắn (khoai mì) tích trữ chất dinh dưỡng ở bộ phận nào?", ["Ở rễ cây phình to thành củ", "Ở hoa", "Ở quả chín", "Ở ngọn cây"], 0, "Thực vật & Động vật", "easy", 3, "Rễ cây tích lũy nhiều tinh bột phình to thành củ cung cấp lương thực cho con người."),
    ("Củ khoai tây có các mắt mầm thực chất là biến dạng của bộ phận nào của cây?", ["Thân cây phình to dưới đất (thân củ)", "Rễ cọc", "Lá cây", "Hoa"], 0, "Thực vật & Động vật", "medium", 4, "Khoai tây là thân ngầm phình to dưới đất, các mắt trên củ có thể nảy mầm thành cây mới."),
    ("Loài hoa nào được xem là Quốc hoa thanh cao của đất nước Việt Nam?", ["Hoa sen", "Hoa hồng", "Hoa cúc", "Hoa mai"], 0, "Thực vật & Động vật", "easy", 2, "Hoa sen vươn lên từ bùn lầy tỏa hương thơm ngát là biểu tượng thanh khiết của dân tộc."),
    ("Khí hậu miền Nam nước ta có hai mùa rõ rệt là những mùa nào?", ["Mùa Mưa và mùa Khô", "Mùa Xuân và mùa Thu", "Mùa Đông lạnh và mùa Hè", "Mùa Tuyết rơi và mùa Nắng"], 0, "Trái Đất & Bầu trời", "easy", 3, "Miền Nam nắng ấm quanh năm, chỉ có 2 mùa mưa và khô rõ rệt."),
    ("Khí hậu miền Bắc nước ta có 4 mùa luân chuyển rõ rệt là những mùa nào?", ["Xuân, Hạ, Thu, Đông", "Mùa Mưa và mùa Khô", "Mùa Nắng và mùa Bão", "Mùa Lũ và mùa Hạn"], 0, "Trái Đất & Bầu trời", "easy", 3, "Miền Bắc có 4 mùa với mùa đông lạnh có gió mùa Đông Bắc và mùa xuân mưa phùn ẩm ướt."),
    ("Gió mùa Đông Bắc thổi vào nước ta vào mùa đông mang lại đặc trưng thời tiết nào?", ["Trời trở lạnh buốt, hanh khô vào đầu đông và mưa phùn se lạnh cuối đông", "Trời nóng như thiêu như đốt", "Mưa rào mùa hè", "Gió bão cát sa mạc"], 0, "Trái Đất & Bầu trời", "medium", 4, "Gió mùa Đông Bắc mang theo khối không khí lạnh từ lục địa phương bắc tràn về."),
    ("Hành động nào sau đây giúp giữ gìn bầu không khí trong lành ở trường học?", ["Trồng và chăm sóc bồn hoa cây xanh, không vứt rác bừa bãi", "Bẻ cành hái hoa", "Đốt rác nilông trong sân trường", "Khạc nhổ bừa bãi"], 0, "Vật chất & Năng lượng", "easy", 2, "Cây xanh quang hợp hút bụi bẩn và tạo bóng mát cho sân trường rợp bóng.")
]

if __name__ == '__main__':
    qs = get_sgk_questions()
    print(f"Generated {len(qs)} questions for {SOURCE_NAME}")

