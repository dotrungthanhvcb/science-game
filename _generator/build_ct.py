# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1512069772995-ec65ed45afd6?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=600&auto=format&fit=crop&q=80"
]

# 126 MC items cho CT
raw_mc = [
    # Giác quan & Hệ cơ quan chính (1-35)
    ("Trái tim đập liên tục", "Cơ quan nằm trong lồng ngực hoạt động như một chiếc máy bơm bền bỉ, co bóp ngày đêm để bơm máu đi khắp cơ thể là gì?", "Trái tim", ["Dạ dày", "Lá gan", "Bộ não"], "Trái tim đập khoảng 70-80 lần mỗi phút, đẩy dòng máu giàu oxy và dinh dưỡng nuôi dưỡng từng tế bào sống.", "6-7", 1),
    ("Lá phổi hô hấp", "Cơ quan hình xốp nằm trong lồng ngực có nhiệm vụ hít khí oxy vào máu và thải khí cacbonic ra ngoài là cơ quan nào?", "Hai lá phổi", ["Dạ dày", "Quả thận", "Ruột non"], "Phổi chứa hàng trăm triệu phế nang li ti giúp trao đổi khí giữa không khí hít vào và các mao mạch máu.", "6-7", 1),
    ("Bộ não chỉ huy", "Cơ quan trung ương nằm an toàn trong hộp sọ, điều khiển mọi suy nghĩ, cảm xúc, trí nhớ và hoạt động của cơ thể là gì?", "Bộ não", ["Trái tim", "Lá lách", "Cột sống"], "Bộ não chứa khoảng 86 tỷ tế bào thần kinh (nơ-ron) kết nối chằng chịt như một siêu máy tính sinh học tuyệt đỉnh.", "6-7", 1),
    ("Dạ dày tiêu hóa", "Cơ quan hình chiếc túi co bóp mạnh mẽ và tiết dịch vị axit để nghiền nát, tiêu hóa thức ăn đưa vào cơ thể là gì?", "Dạ dày (Bao tử)", ["Thực quản", "Ruột già", "Bàng quang"], "Dạ dày tiết ra axit clohidric (HCl) và men pepsin giúp phân cắt protein thịt cá thành các mảnh nhỏ dễ hấp thu.", "7-8", 2),
    ("Ruột non hấp thụ dinh dưỡng", "Bộ phận dài khoảng 6 mét trong ổ bụng đảm nhận nhiệm vụ hấp thụ hầu hết các chất dinh dưỡng từ thức ăn vào máu là gì?", "Ruột non", ["Ruột già", "Dạ dày", "Tụy"], "Thành ruột non có hàng triệu vi nhung mao li ti làm tăng diện tích tiếp xúc hấp thu dưỡng chất tối đa.", "8-9", 3),
    ("Ruột già và chất thải", "Phần ruột tiếp theo sau ruột non có nhiệm vụ tái hấp thu nước và tạo khuôn chất bã thải ra ngoài cơ thể là gì?", "Ruột già (Đại tràng)", ["Dạ dày", "Thực quản", "Gan"], "Ruột già chứa hệ vi sinh vật đường ruột có ích giúp tổng hợp một số vitamin nhóm B và vitamin K.", "7-8", 2),
    ("Lá gan thải độc", "Cơ quan nội tạng lớn nhất và nặng nhất trong cơ thể, được ví như 'nhà máy hóa chất' lọc sạch độc tố và tiết mật tiêu hóa là gì?", "Lá gan", ["Trái tim", "Dạ dày", "Phổi"], "Gan thực hiện hơn 500 chức năng quan trọng: thải độc, tích trữ đường glycogen, sản xuất dịch mật tiêu hóa chất béo.", "8-9", 3),
    ("Quả thận lọc máu", "Hai cơ quan hình hạt đậu nằm phía sau lưng có chức năng lọc chất thải trong máu để tạo thành nước tiểu là gì?", "Hai quả thận", ["Hai lá phổi", "Hai lá gan", "Túi mật"], "Mỗi ngày thận lọc khoảng 180 lít máu để giữ lại nước sạch và khoáng chất cần thiết, thải chất cặn bã qua nước tiểu.", "7-8", 2),
    ("Bộ xương nâng đỡ cơ thể", "Hệ cơ quan gồm 206 chiếc xương cứng cáp ghép lại có chức năng gì tối quan trọng đối với cơ thể người?", "Làm khung nâng đỡ cơ thể, bảo vệ nội tạng và giúp vận động", ["Chỉ để làm đẹp", "Chứa nước uống", "Thải khí độc"], "Hộp sọ bảo vệ não, lồng ngực bảo vệ tim phổi, cột sống giúp con người đứng thẳng lưng hiên ngang.", "6-7", 1),
    ("Canxi cho xương chắc khỏe", "Khoáng chất nào có nhiều trong sữa tươi, tôm cua, trứng giúp xương và răng của bé phát triển dài và chắc khỏe?", "Canxi (Calcium)", ["Chất sắt", "Vitamin C", "Đường ngọt"], "Bổ sung đủ canxi cùng vitamin D từ ánh nắng sớm giúp bé tăng trưởng chiều cao vượt trội.", "6-7", 1),
    ("Cơ bắp co giãn", "Bộ phận nào bám vào xương, có khả năng co lại và giãn ra giúp cơ thể chúng ta cử động, chạy nhảy và mang vác?", "Cơ bắp (Hệ cơ)", ["Mỡ dưới da", "Móng tay", "Tóc"], "Cơ thể con người có hơn 600 cơ bắp; cơ tim co bóp tự động suốt đời không hề ngơi nghỉ.", "6-7", 1),
    ("Khớp xương linh hoạt", "Nơi tiếp giáp giữa hai đầu xương cho phép chúng ta gập tay, gập chân và xoay cổ dễ dàng gọi là gì?", "Khớp xương", ["Thịt nạc", "Dây thần kinh", "Mạch máu"], "Tại các khớp xương có lớp sụn trơn láng và bao hoạt dịch tiết chất nhờn giúp xương cử động êm ái không bị cọ xát đau.", "7-8", 2),
    ("Thị giác qua đôi mắt", "Giác quan giúp bé nhìn thấy hình ảnh sắc màu, đọc sách và ngắm nhìn thế giới tươi đẹp xung quanh là gì?", "Thị giác (Đôi mắt)", ["Thính giác", "Khứu giác", "Vị giác"], "Mắt hoạt động giống như một chiếc máy ảnh tự nhiên: giác mạc và thủy tinh thể hội tụ ánh sáng lên võng mạc.", "6-7", 1),
    ("Bảo vệ đôi mắt sáng", "Để giữ cho đôi mắt luôn sáng khỏe và không bị cận thị, thói quen nào sau đây là ĐÚNG ĐẮN?", "Ngồi học đủ ánh sáng, giữ khoảng cách mắt 30cm và hạn chế xem điện thoại liên tục", ["Nằm đọc sách trong bóng tối", "Dí sát mắt vào màn hình tivi", "Dụi tay bẩn vào mắt"], "Sau mỗi 20 phút nhìn màn hình, bé hãy nhìn xa 6 mét trong vòng 20 giây để mắt được thư giãn (quy tắc 20-20-20).", "6-7", 1),
    ("Thính giác qua đôi tai", "Giác quan giúp bé lắng nghe tiếng cô giáo giảng bài, tiếng chim hót và bản nhạc du dương là gì?", "Thính giác (Đôi tai)", ["Thị giác", "Vị giác", "Xúc giác"], "Sóng âm thanh đi qua ống tai làm rung màng nhĩ, truyền qua chuỗi 3 xương con nhỏ nhất cơ thể vào ốc tai.", "6-7", 1),
    ("Bảo vệ màng nhĩ", "Hành động nào sau đây rất NGUY HIỂM có thể làm thủng màng nhĩ gây điếc tai vĩnh viễn?", "Dùng vật nhọn bằng kim loại chọc sâu vào lỗ tai để ngoáy tai", ["Rửa vành tai bằng khăn mềm", "Nghe nhạc vừa đủ nghe", "Đội mũ khi đi xe"], "Tuyệt đối không dùng tăm nhọn, que sắt hay chìa khóa chọc vào tai vì màng nhĩ rất mỏng manh dễ rách.", "6-7", 1),
    ("Khứu giác qua chiếc mũi", "Giác quan giúp bé ngửi thấy mùi hương thơm ngát của bông hoa hay mùi thơm của món ăn ngon là gì?", "Khứu giác (Mũi)", ["Vị giác", "Thính giác", "Thị giác"], "Mũi có các tế bào thụ cảm khứu giác ở vòm mũi trên gửi tín hiệu mùi hương thẳng tới não bộ.", "6-7", 1),
    ("Lông mũi cản bụi", "Lớp lông nhỏ mọc bên trong hai lỗ mũi của chúng ta có tác dụng sinh học quan trọng nào?", "Ngăn cản bụi bẩn và côn trùng nhỏ bay vào đường hô hấp", ["Để làm đẹp cho mũi", "Để tạo tiếng hắt hơi", "Làm ấm thức ăn"], "Lông mũi kết hợp với lớp chất nhầy ẩm ướt hoạt động như chiếc máy lọc không khí tự nhiên đầu tiên của cơ thể.", "7-8", 2),
    ("Vị giác qua chiếc lưỡi", "Cơ quan nằm trong khoang miệng giúp bé cảm nhận được 5 vị cơ bản: ngọt, mặn, chua, đắng và umami là gì?", "Vị giác (Chiếc lưỡi)", ["Khứu giác", "Thị giác", "Xúc giác"], "Bề mặt lưỡi có hàng ngàn chồi vị giác nhỏ li ti chứa các tế bào cảm nhận vị khác nhau.", "6-7", 1),
    ("Xúc giác qua làn da", "Giác quan bao phủ toàn bộ cơ thể giúp bé cảm nhận được nóng, lạnh, trơn, nhám, mềm, cứng và cảm giác đau là gì?", "Xúc giác (Làn da)", ["Vị giác", "Thị giác", "Thính giác"], "Làn da là cơ quan lớn nhất cơ thể, chứa hàng triệu thụ thể cảm giác nhạy cảm tiếp nhận thông tin từ môi trường.", "6-7", 1),
    ("Răng sữa của bé", "Bộ răng sữa mọc đầu đời của một bạn nhỏ khi mọc đủ có tổng cộng bao nhiêu chiếc răng?", "20 chiếc răng sữa", ["32 chiếc", "10 chiếc", "40 chiếc"], "Răng sữa gồm 8 răng cửa, 4 răng nanh và 8 răng hàm nhỏ giúp bé tập nhai thức ăn dặm từ 6 tháng đến 3 tuổi.", "6-7", 1),
    ("Răng vĩnh viễn ở người lớn", "Khi lớn lên thay hết răng sữa, bộ răng vĩnh viễn hoàn chỉnh của một người trưởng thành có bao nhiêu chiếc?", "32 chiếc răng", ["20 chiếc", "24 chiếc", "40 chiếc"], "Răng vĩnh viễn gồm 8 răng cửa, 4 răng nanh, 8 răng tiền hàm và 12 răng hàm (bao gồm cả 4 răng khôn).", "7-8", 2),
    ("Sâu răng do đâu", "Nguyên nhân chính dẫn đến sâu răng, sún răng gây đau nhức ê buốt ở trẻ nhỏ là do đâu?", "Do ăn nhiều kẹo ngọt nhưng lười chải răng, vi khuẩn ăn đường tạo axit phá hủy men răng", ["Do uống nhiều nước lọc", "Do ăn nhiều rau xanh", "Do răng tự rụng"], "Mảng bám thức ăn thừa bị vi khuẩn lên men tạo axit ăn mòn lớp men răng bảo vệ bên ngoài tạo thành lỗ sâu.", "6-7", 1),
    ("Chải răng đúng cách", "Để bảo vệ hàm răng luôn trắng bóng và hơi thở thơm tho, bé nên chải răng như thế nào?", "Chải răng ít nhất 2 lần mỗi ngày (sau khi thức dậy và trước khi đi ngủ buổi tối)", ["Một tuần chải răng 1 lần", "Chỉ súc miệng nước lạnh là đủ", "Chải răng bằng nước ngọt"], "Chải dọc theo chiều răng mọc từ nướu xuống đầu răng ít nhất trong 2 phút bằng kem đánh răng có fluor.", "6-7", 1),
    ("Máu trong cơ thể", "Chất lỏng màu đỏ lưu thông trong hệ tuần hoàn của cơ thể chúng ta có tế bào nào chuyên chở oxy?", "Hồng cầu", ["Bạch cầu", "Tiểu cầu", "Huyết tương"], "Hồng cầu chứa huyết sắc tố hemoglobin có chứa sắt, tạo nên màu đỏ tươi khi kết hợp với khí oxy.", "8-9", 3),
    ("Bạch cầu chiến sĩ bảo vệ", "Tế bào nào trong máu được ví như những người lính dũng cảm tiêu diệt vi khuẩn, virus xâm nhập cơ thể?", "Bạch cầu (Tế bào miễn dịch)", ["Hồng cầu", "Tiểu cầu", "Tế bào mỡ"], "Khi cơ thể bị nhiễm khuẩn vết thương, bạch cầu kéo đến bao vây tiêu diệt vi khuẩn tạo nên vết mủ trắng lành thương.", "7-8", 2),
    ("Tiểu cầu làm đông máu", "Khi chúng ta vô tình bị đứt tay chảy máu, tế bào máu nào nhanh chóng kết dính tạo cục máu đông bịt kín vết thương?", "Tiểu cầu", ["Hồng cầu", "Bạch cầu", "Huyết tương"], "Tiểu cầu giải phóng các yếu tố đông máu tạo thành mạng lưới sợi fibrin ngăn không cho máu chảy ra ngoài.", "8-9", 3),
    ("Nhiệt độ cơ thể người", "Nhiệt độ cơ thể của một người khỏe mạnh bình thường dao động ở mức bao nhiêu độ C?", "Khoảng 36,5 độ C đến 37 độ C", ["Khoảng 40 độ C", "Khoảng 30 độ C", "Khoảng 45 độ C"], "Khi nhiệt độ đo được trên 37,5 độ C là cơ thể đang bị sốt, hệ miễn dịch đang chiến đấu chống lại mầm bệnh.", "6-7", 1),
    ("Tuyến mồ hôi trên da", "Da của chúng ta tiết mồ hôi và chất nhờn có tác dụng chính nào sau đây?", "Điều hòa thân nhiệt mát mẻ và giữ ẩm cho da mềm mại", ["Làm da bị bẩn", "Làm mất năng lượng", "Tạo mùi hôi"], "Chất nhờn tự nhiên trên da còn tạo ra một lớp màng axit yếu nhẹ giúp ức chế vi khuẩn có hại phát triển.", "7-8", 2),
    ("Móng tay móng chân", "Móng tay và móng chân cấu tạo từ chất sừng keratin có chức năng quan trọng nào?", "Bảo vệ đầu ngón tay ngón chân nhạy cảm và tăng lực bấm khi cầm nắm", ["Để cào xước đồ vật", "Để sơn móng cho đẹp", "Không có tác dụng gì"], "Cắt móng tay sạch sẽ gọn gàng giúp loại bỏ nơi trú ngụ ưa thích của giun sán và trứng vi khuẩn lây bệnh.", "6-7", 1),
    ("Tóc trên đầu", "Mái tóc dày trên đầu của chúng ta có vai trò tự nhiên nào sau đây?", "Che nắng, giữ ấm cho hộp sọ và giảm chấn động nhẹ vào đầu", ["Để tạo kiểu tóc", "Làm nặng đầu", "Hút bụi bẩn"], "Mỗi ngày chúng ta rụng tự nhiên từ 50-100 sợi tóc và các sợi tóc mới sẽ mọc lên thay thế liên tục.", "6-7", 1),
    ("Tư thế ngồi học chuẩn", "Tư thế ngồi học ngay ngắn, lưng thẳng, hai bàn chân đặt phẳng trên sàn giúp phòng tránh tật học đường nào?", "Phòng tránh cong vẹo cột sống và gù lưng", ["Phòng tránh gãy răng", "Phòng tránh đau tai", "Phòng tránh rụng tóc"], "Bàn ghế phù hợp chiều cao giúp cột sống phát triển thẳng đẹp và lồng ngực mở rộng hít thở sâu.", "6-7", 1),
    ("Hắt hơi và ho", "Phản xạ hắt hơi hoặc ho đột ngột của cơ thể là hành động tự vệ tự nhiên nhằm mục đích gì?", "Tống khứ dị vật, bụi bẩn và chất nhầy ra khỏi đường thở", ["Để dọa người khác", "Do buồn ngủ", "Để tập thể dục cho phổi"], "Khi ho hoặc hắt hơi, bé nhớ dùng khăn giấy hoặc khuỷu tay áo che miệng để không phát tán mầm bệnh cho bạn bè.", "6-7", 1),
    ("Ngáp khi buồn ngủ", "Tại sao khi chúng ta cảm thấy mệt mỏi, buồn ngủ hoặc thiếu không khí lại hay ngáp to?", "Để hít vào một lượng lớn khí oxy và làm mát bộ não", ["Vì miệng bị đói", "Để nói chuyện to", "Vì mắt bị mỏi"], "Cái ngáp sâu giúp cung cấp thêm oxy cho não bộ đang uể oải và kích thích tuần hoàn máu ở vùng mặt.", "7-8", 2),
    ("Nấc cụt do đâu", "Hiện tượng nấc cụt phiền toái xảy ra là do sự co thắt đột ngột ngoài ý muốn của cơ quan nào?", "Cơ hoành (Cơ ngăn cách ngực và bụng)", ["Cơ bắp tay", "Cơ tim", "Dạ dày"], "Uống một ngụm nước ấm từ từ hoặc hít sâu nín thở vài giây là mẹo dân gian giúp cơ hoành thư giãn hết nấc cụt.", "8-9", 3),

    # 4 nhóm chất dinh dưỡng & Vệ sinh sức khỏe (36-70)
    ("Nhóm chất bột đường", "Nhóm chất dinh dưỡng có nhiều trong gạo, bánh mì, khoai lang, ngô cung cấp năng lượng chủ yếu cho cơ thể hoạt động là gì?", "Chất bột đường (Glucid / Carbohydrate)", ["Chất đạm", "Chất béo", "Vitamin"], "Chất bột đường là nhiên liệu chính giúp não bộ tư duy học tập và cơ bắp chạy nhảy mỗi ngày.", "6-7", 1),
    ("Nhóm chất đạm (Protein)", "Nhóm chất có nhiều trong thịt, cá, trứng, sữa, đậu nành giúp xây dựng cơ bắp và lớn lên từng ngày là chất gì?", "Chất đạm (Protein)", ["Chất đường", "Chất béo", "Chất xơ"], "Protein là những viên gạch kỳ diệu xây dựng tế bào, chữa lành vết thương và tạo kháng thể bảo vệ cơ thể.", "6-7", 1),
    ("Nhóm chất béo (Lipid)", "Chất béo có trong dầu thực vật, mỡ cá hồi, quả bơ, hạt lạc có vai trò quan trọng nào?", "Dự trữ năng lượng và hòa tan các vitamin A, D, E, K", ["Làm cơ thể yếu đi", "Gây sốt cao", "Không có vai trò gì"], "Chất béo tốt omega-3 rất quan trọng cho sự phát triển vượt trội của thị giác và trí thông minh của trẻ nhỏ.", "7-8", 2),
    ("Nhóm vitamin và khoáng chất", "Rau xanh và hoa quả tươi chứa dồi dào nhóm chất nào giúp tăng sức đề kháng và da dẻ hồng hào?", "Vitamin và khoáng chất", ["Chất bột đường", "Chất béo bão hòa", "Chất bảo quản"], "Ăn đủ nhiều loại rau củ quả đa sắc màu mỗi ngày giúp bé khỏe mạnh, không bị ốm vặt.", "6-7", 1),
    ("Chất xơ trong rau củ", "Chất xơ có trong rau củ quả tuy cơ thể không tiêu hóa được nhưng có tác dụng vàng nào?", "Giúp hệ tiêu hóa hoạt động trơn tru, chống táo bón", ["Làm đau dạ dày", "Làm mất nước", "Làm rụng răng"], "Chất xơ hoạt động như chiếc chổi quét sạch lòng ruột và là thức ăn cho các vi khuẩn đường ruột có lợi.", "6-7", 1),
    ("Uống đủ nước mỗi ngày", "Mỗi ngày một bạn nhỏ ở độ tuổi đi học nên uống khoảng bao nhiêu lít nước lọc sạch để cơ thể khỏe mạnh?", "Khoảng 1,5 đến 2 lít nước", ["Chỉ 1 ngụm nhỏ", "Khoảng 10 lít", "Không cần uống nước"], "Nước chiếm hơn 60% trọng lượng cơ thể, giúp vận chuyển dinh dưỡng và đào thải độc tố qua mồ hôi, nước tiểu.", "6-7", 1),
    ("Rửa tay xà phòng 6 bước", "Trước khi ăn cơm và sau khi đi vệ sinh, hành động quan trọng hàng đầu nào giúp phòng ngừa dịch bệnh?", "Rửa tay sạch sẽ bằng xà phòng dưới vòi nước chảy theo 6 bước", ["Chỉ cần lau tay vào quần", "Thổi phù vào bàn tay", "Chỉ rửa ngón tay trỏ"], "Bàn tay sạch giúp ngăn ngừa 80% các bệnh truyền nhiễm nguy hiểm như tiêu chảy, tay chân miệng, cúm mùa.", "6-7", 1),
    ("Giấc ngủ của trẻ nhỏ", "Một bạn nhỏ 7-8 tuổi cần ngủ bao nhiêu tiếng mỗi đêm để cơ thể tiết hormone tăng trưởng chiều cao tối đa?", "Khoảng 9 đến 10 tiếng mỗi đêm", ["Chỉ ngủ 3 tiếng", "Ngủ 24 tiếng cả ngày", "Thức trắng đêm chơi game"], "Tuyến yên tiết hormone tăng trưởng chiều cao mạnh nhất vào khoảng từ 10 giờ đêm đến 2 giờ sáng khi bé ngủ sâu giấc.", "6-7", 1),
    ("Ăn chín uống sôi", "Khẩu hiệu vệ sinh an toàn thực phẩm quan trọng giúp phòng tránh bệnh giun sán và ngộ độc thực phẩm là gì?", "'Ăn chín, uống sôi, đảm bảo vệ sinh'", ["Ăn đồ sống tái", "Uống nước lã ngoài sông", "Ăn thức ăn ôi thiu"], "Nhiệt độ sôi 100 độ C giúp tiêu diệt hầu hết vi khuẩn có hại và trứng giun sán trong thực phẩm.", "6-7", 1),
    ("Bữa ăn sáng quan trọng", "Tại sao bữa ăn sáng lại được coi là bữa ăn quan trọng nhất trong ngày đối với học sinh?", "Nạp năng lượng cho não bộ và cơ thể học tập hăng say sau giấc ngủ dài ban đêm", ["Để đỡ phải ăn bữa trưa", "Để tăng cân thật nhanh", "Không quan trọng"], "Bỏ bữa sáng khiến bé dễ bị hạ đường huyết, hoa mắt chóng mặt, mệt mỏi và giảm khả năng tiếp thu bài học.", "6-7", 1),
    ("Tập thể dục buổi sáng", "Thói quen dậy sớm tập thể dục thể thao mỗi ngày mang lại những lợi ích tuyệt vời nào cho bé?", "Xương khớp dẻo dai, tim phổi khỏe mạnh, tinh thần sảng khoái yêu đời", ["Làm cơ thể mệt mỏi cả ngày", "Làm yếu xương", "Làm lùn đi"], "Vận động ngoài trời còn giúp cơ thể tổng hợp vitamin D tự nhiên từ ánh nắng sớm giúp xương chắc khỏe.", "6-7", 1),
    ("Không ăn quà vặt cổng trường", "Tại sao các bạn nhỏ không nên ăn các loại quà vặt phẩm màu, cay gắt bán không rõ nguồn gốc ở cổng trường?", "Dễ bị ngộ độc thực phẩm, đau bụng và hóa chất độc hại gây bệnh cho dạ dày", ["Vì các món đó quá bổ", "Vì quá đắt tiền", "Vì không có đường"], "Thực phẩm bẩn chứa phẩm màu công nghiệp và chất bảo quản độc hại gây nguy hiểm nghiêm trọng cho sức khỏe.", "6-7", 1),
    ("Đội mũ bảo hiểm", "Khi ngồi trên xe máy, xe đạp điện tham gia giao thông cùng bố mẹ, bé bắt buộc phải làm gì để bảo vệ tính mạng?", "Đội mũ bảo hiểm đạt chuẩn và cài quai đúng quy cách", ["Chỉ cần đội mũ vải che nắng", "Không cần đội gì cả", "Đội mũ ngược"], "Mũ bảo hiểm giúp hấp thu và giảm chấn động bảo vệ hộp sọ và bộ não quý giá khi không may xảy ra va quẹt.", "6-7", 1),
    ("An toàn khi đi bơi", "Quy tắc an toàn sống còn nào khi đi bơi ở hồ bơi hoặc tắm biển để tránh tai nạn đuối nước?", "Luôn mặc áo phao, khởi động kỹ trước khi xuống nước và có người lớn giám sát chặt chẽ", ["Tự ý nhảy xuống hồ bơi sâu một mình", "Bơi ra xa bờ sóng lớn", "Trêu đùa nhấn nước bạn bè"], "Tuyệt đối không được rủ nhau tắm ao hồ, sông suối một mình khi không có người lớn biết bơi đi cùng bảo vệ.", "6-7", 1),
    ("An toàn sử dụng điện", "Hành động nào sau đây là CỰC KỲ NGUY HIỂM có thể dẫn đến điện giật chết người?", "Dùng tay ướt cắm phích điện hoặc chọc que sắt vào ổ cắm điện trong nhà", ["Bật công tắc bằng tay khô ráo", "Nhờ bố mẹ cắm điện giùm", "Tắt quạt khi ra khỏi phòng"], "Nước dẫn điện rất tốt, tay ướt làm dòng điện chạy qua cơ thể gây co giật cơ tim vô cùng nguy hiểm.", "6-7", 1),
    ("Phòng tránh bỏng nước sôi", "Khi mẹ đang nấu nồi canh sôi trên bếp hoặc phích nước sôi, bé nên ứng xử như thế nào?", "Tránh xa khu vực bếp nấu và không với tay kéo nồi canh xuống", ["Chạy nhảy nô đùa quanh bếp", "Thò tay sờ vào nồi canh sôi", "Cầm phích nước nóng chạy"], "Nước sôi 100 độ C gây bỏng sâu và để lại vết sẹo đau đớn trên da, cần hết sức cẩn thận trong gian bếp.", "6-7", 1),
    ("Không đi theo người lạ", "Khi đang ở công viên hoặc tan trường có người lạ mặt đến cho bánh kẹo hoặc bảo dẫn đi tìm bố mẹ, bé phải làm gì?", "Tuyệt đối từ chối, không nhận quà, không đi theo và chạy đến bên thầy cô hoặc bảo vệ cầu cứu", ["Vui vẻ ăn kẹo và đi theo ngay", "Lên xe máy của người lạ chở đi", "Đưa chìa khóa nhà cho người lạ"], "Kỹ năng tự bảo vệ bản thân giúp bé thoát khỏi các nguy cơ bắt cóc hoặc xâm hại từ kẻ xấu.", "6-7", 1),
    ("Khi bị sốt cao cần làm gì", "Khi cặp nhiệt độ thấy sốt cao trên 38,5 độ C, bố mẹ nên làm gì trước khi đưa bé đến bác sĩ?", "Uống thuốc hạ sốt theo hướng dẫn, chườm khăn ấm vào trán nách bẹn và uống nhiều nước", ["Đắp chăn bông thật dày cho toát mồ hôi", "Uống nước đá lạnh", "Tắm nước lạnh ngay lập tức"], "Chườm ấm giúp các mạch máu ngoại vi giãn nở, tỏa nhiệt nhanh chóng giúp hạ sốt an toàn.", "7-8", 2),
    ("Vết thương chảy máu nhẹ", "Khi bị trầy xước chảy một ít máu ở đầu gối do té ngã, bước sơ cứu đúng đầu tiên là gì?", "Rửa sạch vết thương dưới vòi nước sạch hoặc nước muối sinh lý rồi sát trùng băng lại", ["Rắc bột ngọt hoặc lá cây bẩn lên vết thương", "Dùng tay bẩn xoa mạnh", "Để vết thương dính bùn đất"], "Rửa sạch vết thương giúp loại bỏ đất cát và vi khuẩn, ngăn ngừa nguy cơ nhiễm trùng uốn ván.", "6-7", 1),
    ("Tiêm chủng vaccine", "Việc tiêm phòng các loại vaccine đầy đủ từ khi còn bé có tác dụng kỳ diệu nào đối với cơ thể?", "Kích thích hệ miễn dịch tạo kháng thể chủ động phòng chống các bệnh truyền nhiễm nguy hiểm", ["Làm cơ thể yếu đi", "Làm trẻ con bị ốm", "Không có tác dụng gì"], "Vaccine đã giúp nhân loại xóa sổ bệnh đậu mùa và bảo vệ hàng triệu trẻ em khỏi bại liệt, sởi, uốn ván.", "7-8", 2)
]

# Thêm 56 câu MC nữa để đủ 126 câu MC
more_mc_ct = [
    ("Tế bào đơn vị sự sống", "Đơn vị cấu tạo nhỏ nhất có đầy đủ chức năng sống của cơ thể con người và muôn loài là gì?", "Tế bào", ["Hạt bụi", "Giọt nước", "Khúc xương"], "Cơ thể một người trưởng thành được tạo nên từ khoảng 37 nghìn tỷ tế bào phối hợp nhịp nhàng.", "7-8", 2),
    ("ADN mang mã di truyền", "Phân tử xoắn kép kỳ diệu nằm trong nhân tế bào chứa đựng toàn bộ mật mã di truyền hình dáng của chúng ta là gì?", "ADN (DNA)", ["Protein", "Chất béo", "Vitamin"], "Nhờ nhận một nửa ADN từ bố và một nửa ADN từ mẹ mà chúng ta có những nét giống cả bố lẫn mẹ.", "8-9", 3),
    ("Vitamin A sáng mắt", "Thiếu hụt vitamin A trong khẩu phần ăn hàng ngày có thể dẫn đến chứng bệnh nào về mắt ở trẻ nhỏ?", "Bệnh quáng gà (Khó nhìn trong bóng tối mờ) và khô mắt", ["Bệnh đau răng", "Bệnh gãy tay", "Bệnh rụng móng"], "Bổ sung cà rốt, bí đỏ, gấc, gan cá giàu vitamin A giúp nuôi dưỡng giác mạc và võng mạc khỏe mạnh.", "7-8", 2),
    ("Vitamin C tăng đề kháng", "Quả cam, chanh, ổi, bưởi, kiwi chứa rất nhiều vitamin nào giúp tăng cường sức đề kháng cho cơ thể?", "Vitamin C (Axit ascorbic)", ["Vitamin D", "Vitamin K", "Vitamin B12"], "Vitamin C kích thích bạch cầu hoạt động tích cực hơn để tiêu diệt các virus cúm xâm nhập cơ thể.", "6-7", 1),
    ("Vitamin D hấp thụ canxi", "Vitamin nào được da tự tổng hợp khi tắm nắng sớm, giúp cơ thể hấp thụ canxi phát triển xương chắc khỏe?", "Vitamin D", ["Vitamin C", "Vitamin B1", "Vitamin A"], "Thiếu vitamin D khiến xương bị mềm, yếu ớt và dễ dẫn đến chứng còi xương chậm lớn ở trẻ em.", "7-8", 2),
    ("Chất sắt bổ máu", "Khoáng chất vi lượng quan trọng có trong thịt bò, gan động vật, rau bina giúp tạo nên huyết sắc tố hồng cầu là gì?", "Chất sắt (Iron)", ["Chất canxi", "Chất kẽm", "Chất i-ốt"], "Thiếu sắt gây thiếu máu khiến cơ thể xanh xao, mệt mỏi, hoa mắt và giảm tập trung học tập.", "7-8", 2),
    ("Muối i-ốt phòng bướu cổ", "Sử dụng muối ăn có bổ sung khoáng chất i-ốt trong bữa cơm gia đình giúp phòng tránh căn bệnh nào?", "Bệnh bướu cổ và thiểu năng trí tuệ", ["Bệnh đau chân", "Bệnh cận thị", "Bệnh sâu răng"], "I-ốt là thành phần thiết yếu của hormone tuyến giáp điều hòa sự phát triển của cơ thể và trí não.", "7-8", 2),
    ("Tuyến giáp ở cổ", "Tuyến nội tiết hình con bướm nằm phía trước cổ tiết ra hormone điều hòa quá trình trao đổi chất của cơ thể là gì?", "Tuyến giáp", ["Tuyến yên", "Tuyến tụy", "Tuyến thượng thận"], "Tuyến giáp hoạt động hài hòa giúp duy trì nhịp tim, nhiệt độ cơ thể và quá trình sinh trưởng khỏe mạnh.", "8-9", 3),
    ("Tuyến tụy và Insulin", "Tuyến nào nằm cạnh dạ dày tiết ra hormone insulin giúp điều hòa lượng đường trong máu ổn định?", "Tuyến tụy", ["Lá lách", "Túi mật", "Tuyến nước bọt"], "Insulin mở cửa tế bào cho đường glucose đi vào sinh năng lượng, thiếu insulin sẽ dẫn đến bệnh tiểu đường.", "8-9", 3),
    ("Men răng cứng nhất", "Bộ phận nào cứng rắn nhất trên cơ thể con người, cứng hơn cả xương ống chân?", "Men răng bao bọc ngoài thân răng", ["Xương sọ", "Xương đùi", "Móng tay"], "Men răng có hàm lượng khoáng hóa lên tới 96% canxi hydroxyapatite nhưng vẫn có thể bị axit sâu răng phá hủy nếu không vệ sinh.", "7-8", 2),
    ("Nước bọt trong miệng", "Dịch lỏng tiết ra từ các tuyến nước bọt trong khoang miệng có chứa men amylase giúp tiêu hóa chất nào ngay khi nhai?", "Tiêu hóa chất tinh bột thành đường ngọt", ["Tiêu hóa chất béo", "Tiêu hóa chất xương", "Làm đông máu"], "Nhai kỹ cơm trong miệng một lúc ta sẽ thấy có vị ngọt thanh tự nhiên là nhờ men amylase biến tinh bột thành đường maltose.", "7-8", 2),
    ("Dây thần kinh truyền tin", "Hệ thống các sợi thần kinh tỏa đi khắp cơ thể hoạt động giống như mạng lưới dây điện để làm gì?", "Truyền tín hiệu cảm giác về não và truyền lệnh vận động đến các cơ", ["Dẫn nước đi nuôi cơ thể", "Dẫn máu chảy", "Tạo ra mồ hôi"], "Tín hiệu thần kinh truyền đi dưới dạng xung điện sinh học với tốc độ lên tới hơn 400 km/h.", "8-9", 3),
    ("Tủy sống trong cột sống", "Dải mô thần kinh hình trụ nằm chạy dài bên trong ống xương sống, nối liền bộ não với các dây thần kinh cơ thể là gì?", "Tủy sống", ["Tủy xương", "Xương sườn", "Đĩa đệm"], "Tủy sống là trung tâm điều khiển của các phản xạ không điều kiện tức thì giúp cơ thể tránh nguy hiểm chớp nhoáng.", "8-9", 3),
    ("Phản xạ giật tay khi chạm vật nóng", "Khi vô tình chạm tay vào chiếc nồi đang nóng bỏng, tay ta tự động rụt phắt lại ngay trước khi não kịp nghĩ là nhờ đâu?", "Phản xạ tủy sống (Cung phản xạ tức thì)", ["Do có người kéo tay lại", "Do vết bỏng tự đẩy", "Do mắt nhìn thấy"], "Cung phản xạ tủy giúp bảo vệ cơ thể khỏi tổn thương nghiêm trọng trong tích tắc bằng cách bỏ qua khâu phân tích dài dòng của vỏ não.", "8-9", 3),
    ("Cột sống 33 đốt xương", "Cột sống của con người gồm khoảng 33 đốt xương xếp chồng lên nhau uốn lượn hình chữ gì giúp giảm xóc khi bước đi?", "Hình chữ S mềm mại", ["Hình thẳng đứng đơ", "Hình tròn vo", "Hình chữ O"], "Độ cong chữ S cùng các đĩa đệm cao su đàn hồi giữa các đốt sống triệt tiêu các chấn động dội lên não khi bé chạy nhảy.", "8-9", 3),
    ("Dấu vân tay độc nhất", "Các đường vân nổi trên đầu ngón tay của mỗi người có đặc điểm kỳ diệu nào trong khoa học hình sự?", "Độc nhất vô nhị, không có hai người nào trên thế giới trùng vân tay kể cả sinh đôi cùng trứng", ["Tất cả mọi người đều giống nhau", "Đổi vân tay mỗi năm", "Biến mất khi lớn lên"], "Dấu vân tay hình thành từ khi còn trong bụng mẹ và giữ nguyên hoa văn đặc trưng suốt cuộc đời.", "7-8", 2),
    ("Mùi hương và ký ức", "Khứu giác là giác quan duy nhất có đường truyền thần kinh kết nối trực tiếp với vùng não hippocampus chi phối điều gì?", "Vùng não chi phối cảm xúc và ký ức lâu dài", ["Vùng điều khiển chạy nhảy", "Vùng điều khiển ngáp", "Vùng đếm số"], "Một mùi hương quen thuộc (mùi bánh mẹ nướng, mùi hoa nhài vườn bà) có thể gợi lại ký ức tuổi thơ sống động tức thì.", "8-9", 3),
    ("Cơ hoành ngăn cách", "Cơ hoành là một tấm cơ mỏng hình vòm có vai trò cơ học quyết định nhất trong hoạt động sinh lý nào?", "Hoạt động hít thở hô hấp của lồng ngực", ["Hoạt động tiêu hóa thức ăn", "Hoạt động co bóp của tim", "Hoạt động đi lại"], "Khi cơ hoành co phẳng hạ xuống, lồng ngực nở rộng hút không khí vào phổi; khi cơ hoành giãn cong lên, không khí bị ép đẩy ra ngoài.", "8-9", 3),
    ("Kháng thể chống bệnh", "Những phân tử protein hình chữ Y do hệ miễn dịch tạo ra để khóa chặt và vô hiệu hóa virus mầm bệnh gọi là gì?", "Kháng thể (Immunoglobulin)", ["Hồng cầu", "Enzym tiêu hóa", "Chất mỡ"], "Sau khi khỏi một bệnh (như thủy đậu), cơ thể lưu giữ tế bào nhớ tạo kháng thể giúp bé không bị mắc lại lần thứ hai.", "8-9", 3),
    ("Nước mắt bôi trơn mắt", "Tuyến lệ tiết ra nước mắt mỗi khi chớp mắt có vai trò sinh học tự nhiên nào đối với đôi mắt?", "Bôi trơn, giữ ẩm giác mạc và chứa chất lysozyme diệt khuẩn bảo vệ mắt", ["Chỉ để khóc khi buồn", "Làm mắt bị mờ", "Không có tác dụng gì"], "Chớp mắt trung bình 15-20 lần mỗi phút giúp trải đều lớp màng nước mắt mỏng bảo vệ bề mặt nhãn cầu.", "7-8", 2),
    ("Hệ bạch huyết phòng vệ", "Mạng lưới các hạch và mạch bạch huyết dẫn dòng dịch trong suốt chảy khắp cơ thể có nhiệm vụ chính là gì?", "Lọc sạch các vi khuẩn, độc tố và tế bào lạ bảo vệ cơ thể", ["Vận chuyển không khí", "Tiêu hóa chất đạm", "Tạo ra mồ hôi"], "Khi cơ thể bị viêm nhiễm (như viêm họng), các hạch bạch huyết ở góc hàm thường sưng to lên để tăng cường sinh bạch cầu chiến đấu.", "8-9", 3),
    ("Sức khỏe tinh thần", "Cười vui vẻ cùng bạn bè và gia đình giúp cơ thể giải phóng hormone endorphin mang lại lợi ích gì?", "Giảm căng thẳng, tăng cường hệ miễn dịch và mang lại cảm giác hạnh phúc", ["Làm cơ thể yếu đi", "Làm mất trí nhớ", "Làm tăng huyết áp"], "Một nụ cười bằng mười thang thuốc bổ, tinh thần lạc quan yêu đời là liều thuốc vàng cho sức khỏe toàn diện.", "6-7", 1),
    ("Đọc sách đúng khoảng cách", "Khoảng cách chuẩn từ mắt bé đến trang sách khi ngồi học bài trên bàn để bảo vệ thị lực là bao nhiêu?", "Khoảng 25cm đến 30cm (bằng một gang tay rưỡi)", ["Khoảng 5cm sát mặt", "Khoảng 1 mét", "Càng gần càng tốt"], "Khoảng cách hợp lý giúp cơ thể mi của mắt không phải điều tiết quá mức, tránh tình trạng mỏi mắt và cận thị sớm.", "6-7", 1),
    ("Bơi lội phát triển toàn diện", "Môn thể thao bơi lội dưới nước được đánh giá cao vì mang lại lợi ích thể chất vượt trội nào?", "Phát triển toàn diện các nhóm cơ bắp, tăng dung tích phổi và hỗ trợ kéo dài cột sống", ["Chỉ làm mát người", "Không có tác dụng gì", "Làm teo cơ"], "Lực nâng của nước làm giảm áp lực trọng lượng lên các khớp xương giúp cơ thể vận động nhẹ nhàng và phát triển chiều cao lý tưởng.", "7-8", 2),
    ("Hạn chế đồ ngọt có gas", "Uống quá nhiều nước ngọt đóng lon có gas và ăn nhiều bánh kẹo ngọt có thể gây ra những nguy cơ sức khỏe nào?", "Gây thừa cân béo phì, sâu răng và làm giảm hấp thu canxi của xương", ["Giúp xương chắc khỏe hơn", "Giúp mắt sáng hơn", "Giúp ngủ ngon hơn"], "Nước ngọt có gas chứa hàm lượng đường tinh luyện rất cao và axit photphoric làm tăng đào thải canxi qua nước tiểu.", "6-7", 1),
    ("Rau xanh đậm màu", "Các loại rau lá xanh đậm như rau bina (chân vịt), cải bó xôi, súp lơ xanh chứa nhiều khoáng chất gì tốt cho máu và xương?", "Chứa nhiều canxi, sắt và axit folic", ["Chứa nhiều mỡ động vật", "Chứa nhiều muối mặn", "Chứa nhiều đường"], "Rau xanh là kho tàng vitamin K giúp kích hoạt protein vận chuyển canxi vào xương giúp khung xương vững chắc.", "7-8", 2),
    ("Ăn chậm nhai kỹ", "Ông bà ta thường khuyên: 'Nhai kỹ no lâu, cày sâu tốt lúa'. Thói quen nhai kỹ thức ăn mang lại ích lợi gì cho dạ dày?", "Nghiền nát thức ăn hòa đều với men nước bọt giúp dạ dày tiêu hóa nhẹ nhàng, hấp thu tốt hơn", ["Làm dạ dày mệt thêm", "Làm tốn thời gian", "Không có tác dụng"], "Nhai kỹ giúp giảm bớt gánh nặng co bóp cho dạ dày, phòng ngừa đau bao tử và đầy hơi trướng bụng.", "6-7", 1),
    ("Đeo khẩu trang nơi đông người", "Đeo khẩu trang đúng cách khi đi xe ngoài đường hoặc đến bệnh viện giúp bảo vệ bé khỏi những nguy cơ nào?", "Ngăn ngừa hít phải khói bụi mịn ô nhiễm và các giọt bắn chứa virus lây bệnh", ["Để che mặt không cho ai nhìn", "Để hít thở khó hơn", "Làm ấm mũi"], "Khẩu trang y tế che kín cả mũi và miệng là lá chắn đơn giản mà cực kỳ hiệu quả bảo vệ đường hô hấp trong lành.", "6-7", 1),
    ("Tẩy giun định kỳ", "Theo khuyến cáo của Bộ Y tế, các bạn nhỏ nên uống thuốc tẩy giun định kỳ bao lâu một lần?", "Khoảng 6 tháng một lần (2 lần mỗi năm)", ["10 năm một lần", "Mỗi ngày một lần", "Không cần tẩy giun"], "Tẩy giun định kỳ giúp loại bỏ các loại giun đũa, giun kim, giun móc ký sinh tranh giành chất dinh dưỡng trong ruột non.", "7-8", 2),
    ("Sức mạnh của giấc ngủ trưa", "Một giấc ngủ trưa ngắn khoảng 15 đến 30 phút sau bữa ăn trưa mang lại lợi ích gì cho bạn nhỏ học bán trú?", "Giúp não bộ và đôi mắt nghỉ ngơi, phục hồi năng lượng học tập hiệu quả vào buổi chiều", ["Làm cơ thể mệt mỏi hơn", "Làm đau đầu", "Không có lợi ích gì"], "Chợp mắt buổi trưa giúp tái tạo sự tập trung của hệ thần kinh, giúp bé tỉnh táo và nhớ bài tốt hơn vào ca học chiều.", "6-7", 1),
    ("Hạn chế đồ chiên rán dầu mỡ", "Ăn quá nhiều đồ chiên rán ngập dầu mỡ (gà rán, khoai tây chiên giòn) thường xuyên có thể gây hại gì?", "Gây béo phì, đầy bụng khó tiêu và tích tụ chất béo xấu có hại cho tim mạch", ["Rất tốt cho sức khỏe", "Làm cơ thể nhẹ nhõm", "Làm sạch mạch máu"], "Chế độ ăn lành mạnh ưu tiên các món hấp, luộc thanh đạm và bổ sung chất béo tốt từ các loại hạt hạt dẻ, óc chó, mè vừng.", "7-8", 2)
]

raw_mc.extend(more_mc_ct)

# 14 SA items (CT127 - CT140)
raw_sa = [
    ("Máy bơm máu", "Cơ quan nằm trong lồng ngực hoạt động như chiếc máy bơm máu đi nuôi cơ thể là gì?", "tim|trái tim", "Trái tim co bóp bền bỉ ngày đêm bơm máu khắp cơ thể.", "6-7", 1),
    ("Cơ quan hô hấp", "Cơ quan trong lồng ngực nhận khí oxy và thải khí cacbonic khi ta hít thở là gì?", "phổi|hai lá phổi|lá phổi", "Phổi thực hiện nhiệm vụ trao đổi khí quan trọng cho sự sống.", "6-7", 1),
    ("Cơ quan chỉ huy", "Cơ quan trung ương nằm trong hộp sọ điều khiển mọi hoạt động và suy nghĩ của con người là gì?", "não|bộ não|não bộ", "Bộ não là trung tâm chỉ huy thần kinh tối cao của cơ thể.", "6-7", 1),
    ("Túi tiêu hóa thức ăn", "Cơ quan hình chữ J co bóp nghiền nát và tiết dịch axit tiêu hóa thức ăn là gì?", "dạ dày|bao tử", "Dạ dày tiết dịch vị nghiền nhuyễn thức ăn.", "6-7", 1),
    ("Cơ quan lọc máu tạo nước tiểu", "Hai cơ quan hình hạt đậu nằm phía sau lưng có chức năng lọc máu tạo nước tiểu là gì?", "thận|hai quả thận|quả thận", "Thận lọc sạch máu và đào thải chất độc qua nước tiểu.", "7-8", 2),
    ("Cơ quan thải độc lớn nhất", "Cơ quan nội tạng lớn nhất cơ thể được ví như nhà máy lọc độc tố và tiết dịch mật là gì?", "gan|lá gan", "Lá gan thực hiện hàng trăm phản ứng hóa học bảo vệ cơ thể.", "7-8", 2),
    ("Giác quan nhìn", "Đôi mắt là cơ quan của giác quan nào giúp chúng ta nhìn thấy vạn vật?", "thị giác", "Thị giác giúp bé ngắm nhìn thế giới lung linh sắc màu.", "6-7", 1),
    ("Giác quan nghe", "Đôi tai là cơ quan của giác quan nào giúp chúng ta lắng nghe âm thanh?", "thính giác", "Thính giác tiếp nhận sóng âm thanh truyền tới não bộ.", "6-7", 1),
    ("Giác quan ngửi", "Chiếc mũi là cơ quan của giác quan nào giúp chúng ta ngửi thấy mùi hương?", "khứu giác", "Khứu giác giúp nhận biết hàng ngàn mùi hương khác nhau.", "6-7", 1),
    ("Giác quan nếm", "Chiếc lưỡi là cơ quan của giác quan nào giúp chúng ta nếm vị ngọt, mặn, chua, cay?", "vị giác", "Vị giác cảm nhận hương vị thơm ngon của các món ăn.", "6-7", 1),
    ("Giác quan cảm nhận qua da", "Làn da bao bọc cơ thể là cơ quan của giác quan nào giúp cảm nhận nóng lạnh, đau nhức?", "xúc giác", "Xúc giác giúp bé cảm nhận được sự tiếp xúc của môi trường.", "6-7", 1),
    ("Số răng sữa của bé", "Khi mọc đủ, bộ răng sữa đầu đời của trẻ nhỏ có tổng cộng bao nhiêu chiếc răng?", "20|20 chiếc|20 răng", "Bộ răng sữa có 20 chiếc răng xinh xắn.", "6-7", 1),
    ("Khoáng chất chắc xương", "Khoáng chất có nhiều trong sữa tươi giúp xương và răng của bé chắc khỏe là chất gì?", "canxi|calcium", "Canxi là vật liệu xây dựng xương chắc khỏe và tăng chiều cao.", "6-7", 1),
    ("Tế bào máu chở oxy", "Tế bào màu đỏ trong máu chuyên chở khí oxy đi nuôi các cơ quan trong cơ thể gọi là gì?", "hồng cầu", "Hồng cầu mang oxy từ phổi đi khắp mọi ngóc ngách cơ thể.", "8-9", 3)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"CT{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Cơ Thể Người",
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

for j, item in enumerate(raw_sa, start=len(raw_mc) + 1):
    sub, q_text, ans_kw, expl, age, diff = item
    qid = f"CT{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Cơ Thể Người",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/ct_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"CT: {len(questions)} câu đã được ghi vào ct_140.json")

# Bổ sung 40 câu MC cho CT
extra_ct_40 = [
    ("Đường huyết trong máu", "Nguồn năng lượng đường đơn giản nhất hòa tan trong máu để cung cấp cho các tế bào hoạt động gọi là gì?", "Đường Glucose", ["Đường Mía", "Đường Hóa học", "Đường Phèn"], "Nồng độ glucose trong máu ổn định nhờ sự điều tiết nhịp nhàng của hormone insulin từ tuyến tụy.", "8-9", 3),
    ("Nhóm máu của người", "Hệ nhóm máu ABO cơ bản và phổ biến nhất của con người được chia thành mấy nhóm máu chính?", "4 nhóm máu (A, B, AB và O)", ["2 nhóm máu", "10 nhóm máu", "Chỉ có 1 nhóm máu duy nhất"], "Người mang nhóm máu O là người cho phổ thông, có thể truyền hồng cầu cho tất cả các nhóm máu khác khi cấp cứu.", "8-9", 3),
    ("Kháng thể mẹ truyền cho con", "Sữa non màu vàng đặc sánh của mẹ trong những ngày đầu sau sinh chứa lượng lớn chất gì quý giá?", "Kháng thể tự nhiên bảo vệ em bé sơ sinh khỏi bệnh tật", ["Chất đường ngọt", "Chất đạm thịt", "Nhiều muối"], "Sữa mẹ là nguồn dinh dưỡng hoàn hảo nhất cho sự phát triển toàn diện của trẻ sơ sinh và trẻ nhỏ.", "6-7", 1),
    ("Vị trí của trái tim", "Trái tim của con người nằm ở vị trí nào trong khoang ngực?", "Nằm ở giữa ngực, hơi chếch lệch sang phía bên trái", ["Nằm hoàn toàn bên tay phải", "Nằm dưới bụng", "Nằm sau lưng"], "Trái tim to xấp xỉ bằng một nắm tay khép chặt của chính người đó.", "6-7", 1),
    ("Nhịp tim đập khi chạy", "Khi bé chạy nhảy vận động mạnh, nhịp tim đập nhanh hơn rất nhiều nhằm mục đích gì?", "Bơm máu mang nhiều oxy và đường tới cơ bắp đang hoạt động", ["Làm tim bị mệt", "Để làm mát phổi", "Để tạo tiếng đập to"], "Nhu cầu oxy của các bó cơ tăng vọt đòi hỏi tim phải tăng tốc độ co bóp để đáp ứng kịp thời.", "7-8", 2),
    ("Mạch đập ở cổ tay", "Khi đặt nhẹ ngón tay lên cổ tay phía ngón cái, ta cảm nhận được từng nhịp nảy nảy nhẹ, đó là gì?", "Mạch đập của động mạch theo từng nhịp co bóp của tim", ["Xương cựa", "Gân tay rung", "Dây thần kinh co"], "Bác sĩ thường bắt mạch ở cổ tay để kiểm tra tần số và nhịp điệu hoạt động của trái tim bệnh nhân.", "7-8", 2),
    ("Mao mạch máu li ti", "Những mạch máu nhỏ li ti mỏng manh nhất nối liền giữa động mạch và tĩnh mạch nơi diễn ra trao đổi chất gọi là gì?", "Mao mạch", ["Động mạch chủ", "Tĩnh mạch lớn", "Ống bạch huyết"], "Mao mạch nhỏ đến mức các tế bào hồng cầu phải xếp hàng một để lách qua từng chiếc một.", "8-9", 3),
    ("Huyết áp là gì", "Áp lực của dòng máu tác động lên thành các động mạch khi tim co bóp bơm máu gọi là gì?", "Huyết áp", ["Nhiệt độ máu", "Độ nhớt của máu", "Trọng lượng máu"], "Chế độ ăn nhạt, ít muối giúp giữ cho huyết áp luôn ổn định và bảo vệ tim mạch suốt đời.", "8-9", 3),
    ("Khí quản dẫn khí", "Ống dẫn khí hình trụ có các vòng sụn cứng giúp đường thở luôn mở rộng nối từ họng xuống phổi là gì?", "Khí quản", ["Thực quản", "Cuống họng", "Dây thanh quản"], "Các vòng sụn chữ C giữ cho khí quản không bị xẹp lép khi chúng ta hít thở không khí vào phổi.", "8-9", 3),
    ("Dây thanh âm phát ra tiếng", "Hai dải cơ nằm trong thanh quản rung lên khi luồng không khí từ phổi thở ra giúp chúng ta phát ra tiếng nói gọi là gì?", "Dây thanh âm (Dây thanh đới)", ["Lưỡi gà", "Vòm họng", "Răng cửa"], "Dây thanh âm rung với tần số khác nhau kết hợp môi, lưỡi, răng giúp tạo nên muôn vàn âm thanh ngôn ngữ phong phú.", "7-8", 2),
    ("Tế bào nón nhìn màu sắc", "Các tế bào cảm quang nằm trên võng mạc mắt giúp bé phân biệt được các màu sắc rực rỡ xanh, đỏ, vàng gọi là gì?", "Tế bào nón (Cone cells)", ["Tế bào que", "Tế bào biểu mô", "Tế bào mỡ"], "Tế bào que giúp nhìn trong ánh sáng mờ ban đêm, còn tế bào nón giúp nhìn chi tiết sắc màu dưới ánh sáng ban ngày.", "8-9", 3),
    ("Mù màu (Rối loạn sắc giác)", "Người bị tật mù màu bẩm sinh thường gặp khó khăn nhất khi phân biệt hai màu sắc nào?", "Màu đỏ và màu xanh lục", ["Màu đen và màu trắng", "Màu tím và màu hồng", "Màu vàng và màu cam"], "Người mù màu đỏ - xanh lục cần cẩn thận khi quan sát tín hiệu đèn giao thông trên đường phố.", "8-9", 3),
    ("Vành tai hứng âm", "Phần sụn bên ngoài của đôi tai có hình dáng xòe rộng như chiếc phễu có chức năng chính là gì?", "Hứng và định hướng sóng âm thanh vào trong ống tai", ["Làm đẹp cho khuôn mặt", "Để đeo kính", "Để giữ ấm đầu"], "Nhiều loài động vật như chó, mèo có thể cử động xoay vành tai về nhiều hướng để đón âm thanh rất thính.", "6-7", 1),
    ("Ráy tai bảo vệ", "Chất sáp màu vàng dính bên trong ống tai ngoài thực chất có tác dụng bảo vệ tự nhiên nào?", "Bẫy bụi bẩn, côn trùng nhỏ và kháng khuẩn ngăn nhiễm trùng tai", ["Làm tai bị bẩn cần lấy hết mỗi ngày", "Làm điếc tai", "Gây ngứa tai"], "Ráy tai tự động khô bong và di chuyển ra ngoài theo chuyển động nhai của hàm, không nên dùng tăm bông chọc sâu.", "7-8", 2),
    ("Màng nhĩ mỏng manh", "Lớp màng mỏng ngăn cách giữa tai ngoài và tai giữa rung lên khi đón nhận sóng âm thanh là gì?", "Màng nhĩ", ["Màng mắt", "Màng mũi", "Màng miệng"], "Âm thanh quá lớn như tiếng nổ bom mìn có thể tạo áp lực làm rách màng nhĩ, cần bịt tai lại khi có tiếng nổ lớn.", "7-8", 2),
    ("Xương bàn chân hình vòm", "Cấu trúc các xương ở lòng bàn chân con người uốn cong hình vòm mang lại ưu điểm cơ học nào?", "Giảm xóc đàn hồi khi bước đi chạy nhảy và nâng đỡ trọng lượng cơ thể êm ái", ["Làm bàn chân yếu đi", "Làm chân khó đứng", "Không có tác dụng gì"], "Bàn chân bẹt không có độ vòm khiến trẻ dễ bị mỏi chân và đau khớp gối khi đi bộ đường dài.", "8-9", 3),
    ("Xương sườn bảo vệ ngực", "Lồng ngực của con người gồm 12 đôi xương sườn cong vòm có nhiệm vụ bảo vệ những cơ quan nội tạng nào?", "Bảo vệ trái tim và hai lá phổi an toàn", ["Bảo vệ dạ dày và bàng quang", "Bảo vệ hai quả thận", "Bảo vệ não bộ"], "Xương sườn vừa chắc khỏe để che chở vừa có tính linh hoạt cử động nở ra xẹp xuống theo từng nhịp thở.", "7-8", 2),
    ("Gân nối cơ với xương", "Các bó sợi collagen màu trắng dẻo dai cực khỏe nối liền đầu cơ bắp vào xương gọi là gì?", "Gân (Gân cơ)", ["Dây chằng", "Mạch máu", "Dây thần kinh"], "Gân gót chân (Gân Achilles) là sợi gân to khỏe nhất cơ thể, giúp chúng ta kiễng chân và bật nhảy.", "8-9", 3),
    ("Dây chằng giữ khớp", "Các dải mô liên kết sợi chắc chắn nối xương với xương tại các khớp giúp giữ khớp không bị trật ra ngoài là gì?", "Dây chằng", ["Cơ bắp", "Gân", "Tủy xương"], "Khởi động kỹ các khớp cổ chân, đầu gối trước khi đá bóng giúp phòng tránh chấn thương giãn đứt dây chằng.", "8-9", 3),
    ("Xương bánh chè ở đầu gối", "Chiếc xương nhỏ hình tam giác tròn nằm phía trước khớp gối giúp bảo vệ khớp gối khi quỳ gối là gì?", "Xương bánh chè", ["Xương gót", "Xương chày", "Xương mác"], "Xương bánh chè tăng lực đòn bẩy cho cơ tứ đầu đùi duỗi thẳng cẳng chân khi đá bóng chạy nhảy.", "7-8", 2),
    ("Tủy đỏ tạo máu", "Chất mềm xốp nằm bên trong các khoang xương xốp (như xương chậu, xương ức) có chức năng sinh học vĩ đại nào?", "Nhà máy sản xuất ra các tế bào hồng cầu, bạch cầu và tiểu cầu cho máu", ["Tích trữ mỡ", "Làm xương nặng", "Tiêu hóa thức ăn"], "Mỗi giây tủy xương sản sinh ra hơn 2 triệu tế bào hồng cầu mới thay thế cho các hồng cầu già yếu bị tiêu hủy.", "8-9", 3),
    ("Vết thâm tím trên da", "Khi bị va đập bầm tím một vùng da, mảng màu tím xanh dưới da xuất hiện là do hiện tượng gì?", "Các mao mạch nhỏ dưới da bị vỡ làm máu rỉ ra đọng dưới lớp mô da", ["Da bị đổi màu", "Do đất bám vào da", "Do xương bị gãy"], "Cơ thể sẽ từ từ dọn dẹp khối máu tụ bầm tím này, màu sắc sẽ chuyển dần sang vàng xanh rồi biến mất hoàn toàn.", "7-8", 2),
    ("Nốt ruồi trên da", "Những nốt chấm nhỏ màu nâu đen trên da của chúng ta thực chất là do sự tích tụ của tế bào gì?", "Tế bào sắc tố melanin sản xuất màu da", ["Mảnh bụi bẩn dưới da", "Mẩu xương nhỏ", "Mụn nhọt"], "Sắc tố melanin giúp bảo vệ các tế bào da bên dưới khỏi tác hại nguy hiểm của tia tử ngoại từ ánh nắng mặt trời.", "7-8", 2),
    ("Tập thói quen đi vệ sinh đúng giờ", "Tập thói quen đi đại tiện vào một khung giờ cố định mỗi sáng mang lại lợi ích gì cho ruột già?", "Hình thành phản xạ tự nhiên giúp phòng chống táo bón và bảo vệ đại tràng khỏe mạnh", ["Làm tốn thời gian", "Làm cơ thể yếu đi", "Không có tác dụng gì"], "Không nên nhịn đi vệ sinh vì phân lưu lại lâu trong ruột già sẽ bị hút cạn nước trở nên khô cứng gây đau rát.", "6-7", 1),
    ("Thức ăn nhanh (Fast food)", "Ăn quá nhiều gà rán, khoai tây chiên, xúc xích rán mà không ăn rau xanh sẽ dẫn đến tình trạng gì?", "Táo bón, nóng trong người, thừa cân và thiếu hụt các vitamin thiết yếu", ["Giúp thông minh vượt trội", "Làm xương dài nhanh", "Làm mắt sáng"], "Bữa ăn lý tưởng luôn cần sự cân bằng: 1/2 đĩa là rau củ quả, 1/4 đĩa là chất đạm và 1/4 đĩa là ngũ cốc tinh bột.", "6-7", 1),
    ("Ăn nhạt bảo vệ thận", "Thói quen ăn quá nhiều muối mặn (chấm nhiều nước mắm, ăn mì tôm thường xuyên) sẽ gây áp lực lớn cho cơ quan nào?", "Gây quá tải cho hai quả thận và làm tăng huyết áp tim mạch", ["Làm đau ngón chân", "Làm rụng tóc", "Làm hỏng mắt"], "Ăn thanh đạm, giảm bớt muối mặn giúp thận lọc máu nhẹ nhàng và bảo vệ mạch máu luôn đàn hồi dẻo dai.", "7-8", 2),
    ("Tránh xa khói thuốc lá", "Khói thuốc lá độc hại chứa chất nicotine và hàng ngàn hóa chất gây ung thư tàn phá nặng nề nhất cơ quan nào?", "Hai lá phổi và hệ hô hấp", ["Đầu ngón tay", "Móng chân", "Xương đầu gối"], "Hút thuốc lá thụ động (hít phải khói thuốc của người khác) cũng gây nguy hiểm tương đương cho phổi non nớt của trẻ nhỏ.", "6-7", 1),
    ("Uống sữa mỗi ngày", "Một ly sữa ấm mỗi ngày cung cấp nguồn dinh dưỡng quý báu nào cho sự phát triển của học sinh tiểu học?", "Canxi, vitamin D, đạm sinh học và phốt pho giúp cao lớn khỏe mạnh", ["Chỉ có nước lọc", "Chứa nhiều chất độc", "Gây sâu răng"], "Sữa tươi tiệt trùng không đường hoặc ít đường là thức uống bổ dưỡng tuyệt vời cho bữa phụ giữa giờ học.", "6-7", 1),
    ("Rửa hoa quả trước khi ăn", "Trước khi gọt vỏ hoặc ăn các loại hoa quả tươi, bé bắt buộc phải làm sạch hoa quả bằng cách nào?", "Rửa kỹ dưới vòi nước chảy sạch nhiều lần để trôi hết bụi bẩn và thuốc bảo vệ thực vật", ["Chỉ cần lau vào vạt áo", "Thổi bụi rồi ăn ngay", "Không cần rửa"], "Vỏ trái cây có thể còn đọng lại vi khuẩn từ đất và dư lượng thuốc trừ sâu, cần rửa sạch để đảm bảo an toàn.", "6-7", 1),
    ("Bảo vệ vùng kín cơ thể (Quy tắc đồ lót)", "Quy tắc đồ lót (Pants Rules) dạy bé điều quan trọng nào để tự bảo vệ cơ thể khỏi xâm hại?", "Vùng kín được che bởi đồ bơi/đồ lót là khu vực riêng tư tuyệt đối, không ai được phép nhìn hay chạm vào ngoại trừ bố mẹ khi tắm hoặc bác sĩ khám bệnh", ["Cho bất kỳ ai chạm vào tùy thích", "Không được mặc quần áo", "Không cần quan tâm"], "Nếu có ai cố tình chạm vào hoặc yêu cầu giữ bí mật xấu, bé phải hét to 'KHÔNG ĐƯỢC' và chạy ngay đi kể cho bố mẹ.", "6-7", 1),
    ("Tự giác rửa tay sau khi chơi", "Sau khi chơi đùa ngoài sân bóng đất cát hoặc nghịch đồ chơi chung với bạn, bé cần làm gì ngay?", "Rửa tay sạch sẽ bằng xà phòng để trôi sạch mầm bệnh", ["Dùng tay bốc thức ăn ăn luôn", "Dụi tay lên mắt mũi miệng", "Lau tay vào ghế"], "Bàn tay là cầu nối đưa vi khuẩn vào miệng và mắt nếu không được rửa sạch bằng xà phòng thường xuyên.", "6-7", 1),
    ("Đường tiêu hóa dài bao nhiêu", "Toàn bộ ống tiêu hóa từ miệng qua thực quản, dạ dày, ruột non đến ruột già của một người dài khoảng bao nhiêu mét?", "Khoảng 8 đến 9 mét", ["Chỉ dài 1 mét", "Dài 50 mét", "Dài 100 mét"], "Ống tiêu hóa cuộn gọn gàng kỳ diệu trong khoang bụng, thực hiện hành trình tiêu hóa thức ăn kéo dài từ 24 đến 48 giờ.", "8-9", 3),
    ("Nụ cười giải tỏa căng thẳng", "Khi mỉm cười, cơ thể chúng ta sử dụng ít cơ bắp hơn nhiều so với khi cau có mặt mày, điều này cho thấy gì?", "Cười vui vẻ giúp cơ mặt thư giãn và tinh thần nhẹ nhõm hơn nhiều so với tức giận", ["Cau có giúp khỏe hơn", "Tức giận làm đẹp da", "Cười làm mỏi cơ"], "Luôn giữ thái độ hòa nhã, chan hòa yêu thương bạn bè giúp bé có một trái tim khỏe mạnh và nhiều bạn tốt bè vui.", "6-7", 1),
    ("Mắt chớp tự nhiên", "Mỗi phút mắt chúng ta tự động chớp khoảng 15-20 lần mà không cần suy nghĩ nhằm mục đích gì?", "Trải đều nước mắt giữ ẩm giác mạc và quét sạch bụi nhỏ", ["Để tập thể dục cho mí mắt", "Do mắt bị buồn ngủ", "Để nháy mắt với bạn"], "Khi chăm chú nhìn vào màn hình điện thoại hoặc máy tính, tần số chớp mắt giảm một nửa khiến mắt bị khô rát khó chịu.", "7-8", 2),
    ("Uống nước ấm buổi sáng", "Uống một ly nước ấm ngay sau khi thức dậy vào buổi sáng mang lại tác dụng thần kỳ nào?", "Đánh thức hệ tiêu hóa, thanh lọc đường ruột và bù đắp lượng nước mất sau đêm dài", ["Làm đau bụng", "Làm mất năng lượng", "Làm buồn ngủ thêm"], "Ly nước ấm buổi sáng giúp kích thích nhu động ruột và tăng cường tuần hoàn máu chuẩn bị cho ngày mới năng động.", "6-7", 1),
    ("Hơi thở sâu hít căng lồng ngực", "Thói quen hít thở sâu bằng bụng (hít vào phình bụng, thở ra xẹp bụng) giúp ích gì cho cơ thể?", "Cung cấp lượng oxy dồi dào cho máu và xoa dịu thần kinh giảm căng thẳng lo âu", ["Làm phổi bị căng rách", "Làm đau dạ dày", "Không có tác dụng gì"], "Tập thở sâu mỗi ngày giúp tăng dung tích sống của phổi và giữ cho tinh thần luôn bình an, tập trung học tập.", "7-8", 2),
    ("Kháng thể chống vi khuẩn", "Hệ miễn dịch của cơ thể chúng ta giống như một đội quân tinh nhuệ gồm những chiến sĩ bảo vệ nào?", "Các tế bào bạch cầu, kháng thể và hệ thống hạch bạch huyết", ["Tế bào da chết", "Móng tay và tóc", "Men răng"], "Một lối sống lành mạnh ăn uống đủ chất, ngủ đủ giấc và tập thể dục đều đặn là cách tốt nhất nâng cao sức mạnh quân đội miễn dịch.", "7-8", 2),
    ("Bảo vệ cột sống khi vác nặng", "Khi cúi xuống bê một chồng sách nặng từ sàn nhà lên, tư thế an toàn chuẩn xác nhất là gì?", "Khuỵu hai đầu gối xuống, giữ lưng thẳng rồi dùng lực cơ đùi đứng lên", ["Cúi gập cong lưng xuống rồi kéo mạnh", "Vừa vặn người vừa nhấc đồ", "Dùng cổ kéo đồ"], "Cúi gập lưng bê vật nặng tạo áp lực đè ép cực lớn lên các đĩa đệm cột sống thắt lưng dễ gây thoát vị đau đớn.", "8-9", 3),
    ("Ý nghĩa của việc kiểm tra sức khỏe", "Khám sức khỏe định kỳ hàng năm tại trường học giúp ích gì cho học sinh và gia đình?", "Phát hiện sớm các tật khúc xạ mắt, cong vẹo cột sống hay bệnh lý để điều trị kịp thời", ["Để tiêm đau", "Để mất thời gian học", "Không có ích lợi gì"], "Phòng bệnh hơn chữa bệnh, kiểm tra sức khỏe định kỳ giúp bé luôn phát triển toàn diện thể chất và tinh thần.", "6-7", 1),
    ("Thói quen rửa chân trước khi ngủ", "Rửa chân sạch sẽ bằng nước ấm trước khi đi ngủ buổi tối mang lại cảm giác dễ chịu nào?", "Lưu thông khí huyết các huyệt đạo ở bàn chân, giúp cơ thể thư giãn và ngủ ngon giấc", ["Làm chân bị lạnh", "Làm khó ngủ", "Làm bẩn chăn"], "Bàn chân chứa nhiều đầu mút thần kinh, giữ cho đôi chân sạch sẽ ấm áp là bí quyết vàng cho giấc ngủ sâu lành.", "6-7", 1)
]

raw_mc.extend(extra_ct_40)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"CT{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Cơ Thể Người",
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

for j, item in enumerate(raw_sa, start=len(raw_mc) + 1):
    sub, q_text, ans_kw, expl, age, diff = item
    qid = f"CT{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Cơ Thể Người",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/ct_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Cập nhật CT hoàn tất: {len(questions)} câu đã được ghi vào ct_140.json")
