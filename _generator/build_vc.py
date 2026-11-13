# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"
]

# 126 MC items
raw_mc = [
    # 1-35 Các thể của vật chất, Nước & Không khí
    ("Ba thể của vật chất", "Trong tự nhiên, hầu hết các chất xung quanh chúng ta thường tồn tại ở ba thể cơ bản nào?", "Thể rắn, thể lỏng và thể khí", ["Thể nóng, thể lạnh, thể ấm", "Thể cứng, thể mềm, thể giòn", "Thể to, thể nhỏ, thể vừa"], "Ví dụ nước: thể rắn là đá viên, thể lỏng là nước uống, thể khí là hơi nước bốc lên.", "6-7", 1),
    ("Đặc điểm thể rắn", "Vật chất ở thể rắn (như hòn đá, thanh sắt, quyển sách) có đặc điểm vật lý nào?", "Có hình dạng và thể tích xác định", ["Có thể tích nhưng không có hình dạng", "Hình dạng biến đổi theo bình chứa", "Không có khối lượng"], "Các phân tử ở thể rắn liên kết chặt chẽ với nhau, giữ cho vật giữ nguyên hình dáng của nó.", "6-7", 1),
    ("Đặc điểm thể lỏng", "Chất lỏng (như nước lọc, dầu ăn, sữa tươi) có đặc điểm nào sau đây?", "Có thể tích xác định nhưng hình dạng phụ thuộc vào bình chứa nó", ["Có hình dạng cố định như khối đá", "Không có thể tích", "Tự bay biến mất ngay"], "Đổ nước vào cốc thì nước hình cái cốc, đổ vào chai thì nước có hình cái chai, mặt thoáng nằm ngang.", "6-7", 1),
    ("Đặc điểm thể khí", "Chất khí (như không khí trong quả bóng bay, khí gas) có đặc tính vật lý nào?", "Không có hình dạng và không có thể tích xác định, lan tỏa chiếm toàn bộ không gian chứa", ["Hình dạng tròn cố định", "Luôn chìm xuống đáy", "Cứng rắn"], "Các phân tử khí chuyển động hỗn loạn không ngừng về mọi phía và có thể bị nén ép lại rất dễ dàng.", "7-8", 2),
    ("Hiện tượng nóng chảy", "Quá trình một chất chuyển từ thể rắn sang thể lỏng khi được đun nóng gọi là gì?", "Hiện tượng nóng chảy", ["Hiện tượng đông đặc", "Hiện tượng bay hơi", "Hiện tượng ngưng tụ"], "Đá viên để ngoài trời nắng tan thành nước lỏng, que kem tan chảy dưới nắng hè là hiện tượng nóng chảy.", "6-7", 1),
    ("Hiện tượng đông đặc", "Quá trình một chất chuyển từ thể lỏng sang thể rắn khi bị làm lạnh gọi là gì?", "Hiện tượng đông đặc", ["Hiện tượng nóng chảy", "Hiện tượng thăng hoa", "Hiện tượng hòa tan"], "Cho khay nước lỏng vào ngăn đá tủ lạnh sau vài giờ nước đông đặc thành những viên đá rắn chắc.", "6-7", 1),
    ("Hiện tượng bay hơi", "Quá trình chất lỏng biến thành thể khí hơi ở bề mặt thoáng của chất lỏng gọi là gì?", "Hiện tượng bay hơi", ["Hiện tượng ngưng tụ", "Hiện tượng đông đặc", "Hiện tượng lắng đọng"], "Quần áo ướt phơi dưới nắng gió khô ráo là do nước trong vải đã bay hơi vào không khí.", "6-7", 1),
    ("Hiện tượng ngưng tụ", "Quá trình chất khí (hơi) gặp lạnh chuyển ngược lại thành chất lỏng gọi là gì?", "Hiện tượng ngưng tụ", ["Hiện tượng bay hơi", "Hiện tượng nóng chảy", "Hiện tượng hòa tan"], "Khi đun nước sôi, mở nắp vung ra ta thấy những giọt nước đọng trên nắp vung là do hơi nước ngưng tụ.", "6-7", 1),
    ("Tính chất của nước sạch", "Nước tinh khiết trong suốt có những tính chất vật lý cơ bản nào sau đây?", "Không màu, không mùi, không vị, chảy từ cao xuống thấp và thấm qua một số vật", ["Có màu xanh, vị ngọt", "Có mùi thơm hoa hồng", "Có vị mặn chát"], "Nước hòa tan được nhiều chất như đường, muối, xà phòng nhưng không hòa tan được dầu ăn, cát sỏi.", "6-7", 1),
    ("Nước không tan trong dầu", "Khi ta đổ dầu ăn vào một cốc nước lọc, hiện tượng gì sẽ xảy ra?", "Dầu ăn không tan và nổi lên trên mặt nước vì dầu nhẹ hơn nước", ["Dầu ăn tan biến mất", "Dầu ăn chìm xuống đáy cốc", "Nước biến thành màu đỏ"], "Dầu ăn có khối lượng riêng nhẹ hơn nước và không phân cực nên luôn nổi thành váng trên mặt nước.", "6-7", 1),
    ("Sự nổi và chìm", "Một hòn sỏi thả vào chậu nước thì chìm nghỉm, nhưng một thanh gỗ hay quả bóng lại nổi bồng bềnh là do đâu?", "Do vật có khối lượng riêng nhỏ hơn nước thì nổi, lớn hơn nước thì chìm", ["Do hòn sỏi biết bơi", "Do thanh gỗ có cánh", "Do nước thích thanh gỗ"], "Lực đẩy Ác-si-mét nâng đỡ các vật nhúng trong chất lỏng, nếu lực đẩy lớn hơn trọng lượng thì vật sẽ nổi.", "7-8", 2),
    ("Tàu thủy bằng thép vẫn nổi", "Tại sao một chiếc đinh sắt thả vào nước thì chìm, nhưng con tàu thủy khổng lồ bằng thép nặng hàng vạn tấn lại nổi trên mặt biển?", "Vì tàu thủy được thiết kế rỗng ruột chứa nhiều không khí làm khối lượng riêng trung bình nhẹ hơn nước", ["Vì nước biển mặn hơn nước ngọt", "Vì tàu có động cơ đẩy", "Vì thép trên tàu là thép nhẹ"], "Phần thể tích rỗng chứa không khí tạo ra lực đẩy Ác-si-mét khổng lồ đủ để nâng toàn bộ con tàu nổi vững vàng.", "8-9", 3),
    ("Thành phần của không khí", "Bầu không khí xung quanh chúng ta là một hỗn hợp khí gồm những thành phần chính nào?", "Khoảng 78% khí Nitơ, 21% khí Oxy và 1% các khí khác (CO2, hơi nước, khí hiếm)", ["100% là khí Oxy", "Toàn là khí độc", "Chỉ có hơi nước"], "Khí oxy duy trì sự sống hô hấp và sự cháy, khí nitơ dồi dào kìm hãm sự cháy nổ mãnh liệt.", "7-8", 2),
    ("Không khí có trọng lượng", "Một quả bóng bay khi được bơm căng không khí sẽ nặng hơn quả bóng xẹp ban đầu, điều này chứng minh gì?", "Không khí có trọng lượng và chiếm không gian", ["Không khí không có khối lượng", "Quả bóng tự lớn lên", "Không khí nhẹ hơn hư không"], "Dù vô hình không nhìn thấy được, không khí thực sự là vật chất có khối lượng và tác dụng áp suất lên vạn vật.", "7-8", 2),
    ("Khí oxy duy trì sự cháy", "Khi úp một chiếc cốc thủy tinh lên một ngọn nến đang cháy, ngọn nến sẽ tắt ngấm sau vài giây vì sao?", "Vì lượng khí oxy trong cốc đã bị đốt cháy hết", ["Vì cốc quá tối", "Vì nến sợ bóng tối", "Vì gió thổi tắt"], "Sự cháy cần khí oxy để duy trì phản ứng hóa học tỏa nhiệt, cách ly nguồn oxy là nguyên tắc dập tắt đám cháy.", "6-7", 1),
    ("Bình chữa cháy CO2", "Tại sao người ta dùng bình chữa cháy chứa khí cacbonic (CO2) để dập tắt các đám cháy nhỏ?", "Khí CO2 nặng hơn không khí, phủ kín ngọn lửa ngăn cách nguồn oxy làm đám cháy tắt", ["Khí CO2 làm cháy to hơn", "Khí CO2 biến thành nước đá", "Khí CO2 có mùi thơm"], "Khí CO2 xịt ra rất lạnh làm hạ nhiệt vùng cháy và phủ kín cách ly oxy giúp dập tắt lửa an toàn.", "8-9", 3),
    ("Sự truyền thẳng của ánh sáng", "Trong một môi trường trong suốt và đồng tính (như không khí trong lành), ánh sáng truyền đi theo đường nào?", "Truyền thẳng theo đường thẳng", ["Truyền uốn lượn lượn sóng", "Truyền hình chữ Z", "Truyền vòng tròn"], "Nhờ ánh sáng truyền thẳng mà người thợ xây dùng dây dọi hoặc thước ngắm thẳng hàng rất chuẩn xác.", "6-7", 1),
    ("Hiện tượng bóng râm", "Khi ta đi dưới nắng trời, phía sau lưng ta xuất hiện một cái bóng râm màu đen trên mặt đất là do đâu?", "Do cơ thể con người là vật cản sáng, ngăn không cho ánh sáng truyền qua", ["Do bóng tối đuổi theo ta", "Do đất bị ướt", "Do quần áo tối màu"], "Vùng phía sau vật cản sáng không nhận được ánh sáng từ nguồn sáng chiếu tới tạo nên bóng tối và bóng nửa tối.", "6-7", 1),
    ("Gương phẳng phản chiếu", "Khi bé đứng soi gương, hình ảnh khuôn mặt nhìn thấy trong gương phẳng có tính chất quang học nào?", "Ảnh ảo bằng đúng kích thước thật, đối xứng với vật qua gương", ["Ảnh to gấp đôi", "Ảnh lộn ngược đầu xuống đất", "Ảnh bị mất màu"], "Gương phẳng phản xạ toàn bộ ánh sáng chiếu vào nó giúp ta nhìn thấy hình ảnh rõ ràng sắc nét.", "6-7", 1),
    ("Kính lúp hội tụ ánh sáng", "Chiếc kính lúp cầm tay có phần mặt kính lồi ở giữa có tác dụng quang học gì?", "Phóng to hình ảnh các vật nhỏ và hội tụ ánh sáng mặt trời vào một điểm", ["Làm nhỏ đồ vật", "Làm tối hình ảnh", "Đổi màu đồ vật"], "Kính lúp là thấu kính hội tụ, các bạn nhỏ dùng để quan sát chi tiết gân lá, kiến bò rất thú vị.", "6-7", 1),
    ("Âm thanh sinh ra do đâu", "Tiếng đàn guitar gảy, tiếng trống gõ, tiếng giọng nói phát ra khi các vật thể có chuyển động gì?", "Dao động rung rinh qua lại liên tục (Sự rung động)", ["Đứng im bất động", "Bốc hơi nóng lên", "Biến đổi màu sắc"], "Dùng tay chạm nhẹ vào mặt trống đang kêu 'tùng tùng', ta cảm nhận rõ ràng mặt trống đang rung bần bật.", "6-7", 1),
    ("Âm thanh truyền qua các môi trường", "Âm thanh có thể truyền đi qua các môi trường nào sau đây?", "Truyền qua chất rắn, chất lỏng và chất khí", ["Chỉ truyền qua không khí", "Chỉ truyền dưới nước", "Không truyền qua chất rắn"], "Người xưa áp tai xuống đất có thể nghe thấy tiếng vó ngựa từ xa hàng km vì âm thanh truyền trong đất rắn nhanh hơn không khí.", "7-8", 2),
    ("Chân không không truyền âm", "Trong môi trường chân không ngoài không gian vũ trụ (nơi không có vật chất, không khí), âm thanh có truyền được không?", "Hoàn toàn không truyền được âm thanh", ["Truyền rất nhanh", "Truyền như bình thường", "Truyền to hơn"], "Các phi hành gia ngoài không gian phải nói chuyện với nhau thông qua sóng vô tuyến của bộ đàm mũ bảo hiểm.", "8-9", 3),
    ("Vận tốc truyền âm", "Âm thanh truyền đi nhanh nhất trong môi trường vật chất nào sau đây?", "Trong chất rắn (như thép, đá)", ["Trong chất lỏng (nước)", "Trong chất khí (không khí)", "Như nhau trong mọi chất"], "Vận tốc âm thanh trong thép khoảng 5.000 m/s, trong nước khoảng 1.500 m/s, trong không khí chỉ khoảng 340 m/s.", "8-9", 3),
    ("Tiếng vang phản xạ âm", "Khi chúng ta hét to trong một hang đá sâu hoặc hẻm núi, một lát sau ta lại nghe thấy chính tiếng hét của mình dội lại là do đâu?", "Do sóng âm thanh va vào vách đá bị phản xạ dội ngược lại tai (Tiếng vang)", ["Do có người trốn trong hang nhại lại", "Do tiếng hét bay vòng tròn", "Do gió thổi lại"], "Nếu âm phản xạ đến tai cách âm trực tiếp ít nhất 1/15 giây thì tai ta sẽ phân biệt được tiếng vang rõ ràng.", "8-9", 3),
    ("Nam châm có hai cực", "Một thanh nam châm vĩnh cửu luôn có hai cực từ tính đối lập nhau gọi là gì?", "Cực Bắc (N - North) và Cực Nam (S - South)", ["Cực Đông và Cực Tây", "Cực Lớn và Cực Nhỏ", "Cực Nóng và Cực Lạnh"], "Cực Bắc thường được sơn màu đỏ ký hiệu chữ N, cực Nam sơn màu xanh ký hiệu chữ S.", "6-7", 1),
    ("Tương tác giữa hai nam châm", "Khi đưa hai đầu cùng cực của hai thanh nam châm lại gần nhau (ví dụ Bắc - Bắc hoặc Nam - Nam), hiện tượng gì xảy ra?", "Hai cực đẩy nhau dạt ra xa", ["Hai cực hút chặt lấy nhau", "Không có hiện tượng gì", "Nam châm bị vỡ vụn"], "Quy tắc từ học cơ bản: 'Cùng cực thì đẩy nhau, khác cực thì hút nhau'.", "6-7", 1),
    ("Nam châm hút kim loại nào", "Thanh nam châm có lực từ hút mạnh mẽ các đồ vật được làm từ chất liệu kim loại nào sau đây?", "Sắt, thép, niken và coban", ["Vàng, bạc, đồng, nhôm", "Gỗ, nhựa, thủy tinh", "Vải, cao su, giấy"], "Nam châm không hút đồng, nhôm, vàng, bạc; nam châm dùng để phân loại rác thải sắt thép tái chế rất hiệu quả.", "6-7", 1),
    ("La bàn từ tính Trái Đất", "Tại sao chiếc kim la bàn luôn luôn tự quay đầu chỉ về hướng Bắc địa lý của Trái Đất?", "Vì Trái Đất hoạt động như một khối nam châm khổng lồ có từ trường hút kim la bàn", ["Vì có gió thổi kim", "Vì kim la bàn thích Mặt Trời", "Do trọng lực kéo"], "Cực từ nam của Trái Đất nằm gần cực Bắc địa lý nên nó hút cực Bắc của kim nam châm la bàn.", "7-8", 2),
    ("Vật dẫn điện tốt", "Chất liệu nào sau đây cho dòng điện chạy qua dễ dàng, được dùng làm lõi dây điện gia đình?", "Kim loại đồng và nhôm", ["Chất nhựa dẻo", "Cao su", "Gỗ khô"], "Đồng có điện trở rất nhỏ, dẫn điện tốt và dẻo dai dễ uốn nên được dùng làm lõi dây dẫn điện phổ biến.", "6-7", 1),
    ("Vật cách điện an toàn", "Chất liệu nào sau đây KHÔNG cho dòng điện chạy qua, được dùng làm vỏ bọc ngoài dây điện bảo vệ con người?", "Nhựa, cao su và thủy tinh", ["Sắt thép", "Nước muối", "Thanh nhôm"], "Lớp vỏ bọc cao su cách điện ngăn không cho dòng điện rò rỉ ra ngoài gây điện giật nguy hiểm.", "6-7", 1),
    ("Mạch điện kín sáng đèn", "Bóng đèn pin sẽ phát sáng rực rỡ khi nào?", "Khi mạch điện được nối kín hoàn chỉnh từ cực dương qua bóng đèn về cực âm của pin", ["Khi mạch điện bị đứt hở", "Khi tháo pin ra ngoài", "Khi tắt công tắc"], "Dòng điện chỉ có thể chạy qua một mạch điện khép kín liên tục tạo thành dòng electron chuyển động.", "6-7", 1),
    ("Pin nguồn năng lượng", "Viên pin tiểu (AA) quen thuộc trong đồng hồ treo tường và điều khiển tivi chuyển hóa dạng năng lượng nào thành điện năng?", "Chuyển hóa hóa năng thành điện năng", ["Chuyển nhiệt năng", "Chuyển cơ năng", "Chuyển quang năng"], "Các phản ứng hóa học bên trong viên pin tạo ra hiệu điện thế 1,5V cung cấp dòng điện một chiều êm ái.", "7-8", 2),
    ("Vật dẫn nhiệt tốt", "Chất liệu nào sau đây dẫn nhiệt nhanh nhất, được dùng làm xoong nồi nấu nướng thức ăn mau sôi?", "Kim loại nhôm, inox, gang và đồng", ["Gỗ khô", "Nhựa xốp", "Thủy tinh cách nhiệt"], "Kim loại truyền nhiệt nhanh từ ngọn lửa bếp ga qua đáy nồi làm chín thức ăn tiết kiệm nhiên liệu.", "6-7", 1),
    ("Vật cách nhiệt bảo vệ", "Chuôi của chiếc chảo xào nấu và tay cầm ấm đun nước thường được bọc bằng chất liệu gỗ hoặc nhựa nhằm mục đích gì?", "Cách nhiệt để tay người cầm không bị bỏng nóng", ["Làm chiếc chảo nặng hơn", "Làm đẹp cho chảo", "Để chảo nấu nhanh sôi"], "Gỗ và nhựa xốp dẫn nhiệt rất kém, giúp giữ nhiệt độ mát mẻ ở phần tay cầm an toàn cho người nấu bếp.", "6-7", 1)
]

# Thêm 91 câu MC nữa để đủ 126 câu MC
more_mc_vc = [
    ("Bình giữ nhiệt chân không", "Chiếc bình giữ nhiệt có thể giữ nước nóng hoặc nước đá lạnh suốt nhiều giờ nhờ cấu tạo đặc biệt nào?", "Lớp chân không ở giữa hai lớp vỏ kim loại ngăn cản sự truyền nhiệt dẫn nhiệt và đối lưu", ["Nhờ cắm điện ngầm", "Nhờ lớp bông dày", "Nhờ có phép màu"], "Môi trường chân không không có phân tử vật chất nên nhiệt độ nóng hoặc lạnh bên trong không thể thoát ra ngoài.", "8-9", 3),
    ("Nhiệt kế thủy ngân hoạt động", "Nhiệt kế đo nhiệt độ dựa trên nguyên lý giãn nở vì nhiệt của chất lỏng như thế nào?", "Chất lỏng nở ra dâng cao khi nóng lên và co lại tụt xuống khi lạnh đi", ["Chất lỏng tự đổi màu", "Chất lỏng bốc cháy", "Chất lỏng đứng yên"], "Cột thủy ngân hoặc cồn đỏ giãn nở đều đặn theo nhiệt độ chỉ đúng vạch nhiệt độ trên thang đo.", "7-8", 2),
    ("Khe hở đường ray xe lửa", "Tại sao ở chỗ nối giữa các thanh ray xe lửa bằng thép luôn phải để lại một khe hở nhỏ vài milimét?", "Để khi trời nắng nóng thanh thép nở dài ra không bị kích cong vênh làm trật bánh tàu", ["Để tiết kiệm thép", "Để xe lửa chạy kêu xình xịch", "Để nước mưa thoát"], "Chất rắn nở ra khi nóng lên, nếu không có khe co giãn thì lực nở vì nhiệt cực lớn sẽ bẻ cong cả thanh thép ray đường tàu.", "7-8", 2),
    ("Trọng lực hút mọi vật", "Tại sao khi chúng ta nhảy lên cao khỏi mặt đất, chúng ta luôn luôn rơi trở lại mặt đất chứ không bay bổng lên trời?", "Do trọng lực (lực hút của Trái Đất) kéo mọi vật về phía tâm Trái Đất", ["Do gió thổi xuống", "Do chân nặng", "Do không khí đè"], "Trọng lực tác dụng lên mọi vật có khối lượng, tạo nên trọng lượng của vật thể.", "6-7", 1),
    ("Lực ma sát có ích", "Rãnh hoa văn xẻ trên lốp xe đạp và đế giày thể thao có tác dụng gì vô cùng quan trọng?", "Tăng lực ma sát bám đường giúp không bị trượt ngã khi chạy xe và đi lại", ["Làm lốp xe mòn nhanh", "Chỉ để làm đẹp", "Làm xe chạy chậm"], "Nếu không có lực ma sát giữa đế giày và mặt đường, chúng ta sẽ bị trượt ngã liên tục như đi trên sàn băng trơn láng.", "6-7", 1),
    ("Lực ma sát có hại", "Khi xích líp xe đạp bị khô dầu kêu ken két và đạp nặng nề, người ta tra dầu nhớt vào nhằm mục đích gì?", "Giảm lực ma sát giúp xích líp quay trơn tru êm ái và chống mòn kim loại", ["Để xích xe dính bụi", "Làm xích xe nặng hơn", "Làm thơm xe"], "Chất bôi trơn dầu nhớt tạo màng ngăn cách giữa hai bề mặt kim loại cọ xát, giảm hao mòn máy móc.", "7-8", 2),
    ("Khối lượng và trọng lượng", "Một phi hành gia có khối lượng 60 kg khi bay lên Mặt Trăng thì khối lượng và trọng lượng thay đổi như thế nào?", "Khối lượng vẫn giữ nguyên 60 kg, nhưng trọng lượng giảm đi 6 lần do lực hút Mặt Trăng yếu hơn", ["Khối lượng bị giảm còn 10 kg", "Cả khối lượng và trọng lượng đều tăng", "Mất hoàn toàn khối lượng"], "Khối lượng là lượng chất chứa trong vật (không đổi), còn trọng lượng là độ lớn lực hút trọng lực tác dụng lên vật.", "8-9", 3),
    ("Hiện tượng phản xạ ánh sáng", "Ánh sáng từ ngọn đèn chiếu vào trang sách rồi phản xạ dội vào mắt chúng ta giúp ta đọc được chữ, hiện tượng đó gọi là gì?", "Phản xạ ánh sáng", ["Hút ánh sáng", "Tắt ánh sáng", "Nóng sáng"], "Chúng ta chỉ nhìn thấy một vật khi có ánh sáng từ vật đó truyền vào mắt ta.", "6-7", 1),
    ("Vật tự phát sáng", "Thiên thể hoặc đồ vật nào sau đây là nguồn sáng tự phát sáng ra ánh sáng?", "Ngọn nến đang cháy, Mặt Trời, con đom đóm", ["Mặt Trăng đêm rằm", "Chiếc gương soi", "Mặt nước hồ"], "Mặt Trăng và chiếc gương không tự phát sáng mà chỉ phản chiếu ánh sáng từ nguồn sáng Mặt Trời chiếu tới.", "6-7", 1),
    ("Kính râm chống chói", "Kính râm đeo mắt màu đen hoặc nâu có tác dụng quang học gì khi đi ngoài trời nắng gắt?", "Hấp thụ bớt cường độ ánh sáng chói chang và lọc tia cực tím bảo vệ mắt", ["Làm trời tối đen không thấy đường", "Phóng to đồ vật", "Làm mát trán"], "Mắt kính râm chất lượng phủ lớp chống tia UV giúp mắt không bị chói lóa và phòng ngừa đục thủy tinh thể.", "6-7", 1),
    ("Lăng kính tán sắc ánh sáng", "Khi chiếu chùm ánh sáng trắng mặt trời qua một lăng kính thủy tinh tam giác, ta thu được dải màu gì?", "Dải 7 sắc cầu vồng: Đỏ, Cam, Vàng, Lục, Lam, Chàm, Tím", ["Chỉ có một màu trắng", "Chỉ có màu đen", "Chỉ có màu xanh lục"], "Nhà bác học Isaac Newton là người đầu tiên làm thí nghiệm tán sắc ánh sáng chứng minh ánh sáng trắng gồm nhiều ánh sáng đơn sắc.", "8-9", 3),
    ("Âm thanh to và nhỏ", "Độ to của âm thanh phát ra (âm lượng) phụ thuộc vào yếu tố dao động nào của nguồn âm?", "Biên độ dao động của nguồn âm (dao động mạnh thì âm to, nhẹ thì âm nhỏ)", ["Tần số dao động", "Màu sắc của vật", "Nhiệt độ của vật"], "Khi ta đánh trống thật mạnh, mặt trống rung với biên độ lớn phát ra âm thanh 'TÙNG' vang rền.", "7-8", 2),
    ("Âm thanh trầm và bổng", "Độ cao của âm thanh (tiếng trầm như tiếng sấm hay tiếng bổng véo von như chim hót) phụ thuộc vào gì?", "Tần số dao động (Số dao động trong 1 giây, tính bằng Hertz - Hz)", ["Độ dày của vật", "Khoảng cách truyền âm", "Độ sáng của phòng"], "Vật dao động càng nhanh (tần số càng cao) thì phát ra âm càng bổng (cao); dao động chậm thì phát ra âm trầm (thấp).", "8-9", 3),
    ("Ô nhiễm tiếng ồn", "Tiếng ồn xe cộ còi xe inh ỏi, tiếng máy khoan kéo dài vượt quá mức cho phép gây hại gì cho con người?", "Gây căng thẳng thần kinh, giảm thính lực của tai và mất ngủ", ["Giúp tai thính hơn", "Làm tim đập chậm", "Không có ảnh hưởng gì"], "Trồng cây xanh quanh nhà và lắp cửa kính cách âm là những biện pháp hữu hiệu giảm ô nhiễm tiếng ồn đô thị.", "7-8", 2),
    ("Chất dẻo (Nhựa polymer)", "Đồ dùng bằng nhựa (chậu nhựa, thước kẻ, vỏ bút) có ưu điểm nhẹ, bền, không rỉ sét nhưng có nhược điểm lớn nào?", "Khó phân hủy trong tự nhiên, gây ô nhiễm môi trường rác thải nhựa hàng trăm năm", ["Dễ bị rỉ sét", "Dẫn điện mạnh", "Quá nặng"], "Hãy hạn chế sử dụng túi nilon và đồ nhựa dùng một lần, tích cực tái chế rác thải nhựa bảo vệ thiên nhiên xanh.", "6-7", 1),
    ("Kim loại dẫn điện tốt nhất", "Trong số các kim loại sau đây, kim loại nào có khả năng dẫn điện tốt nhất trong tự nhiên?", "Kim loại Bạc (Ag)", ["Kim loại Đồng (Cu)", "Kim loại Vàng (Au)", "Kim loại Sắt (Fe)"], "Bạc dẫn điện tốt nhất nhưng đắt tiền nên người ta dùng đồng và nhôm để làm dây dẫn điện phổ biến.", "8-9", 3),
    ("Sự gỉ sét của sắt", "Một chiếc đinh sắt để ngoài không khí ẩm lâu ngày bị phủ một lớp gỉ màu nâu đỏ giòn xốp là do phản ứng gì?", "Sắt bị oxy hóa tác dụng với khí oxy và hơi nước trong không khí", ["Sắt bị dính bụi đất", "Sắt bị mọc rêu", "Sắt bị nóng chảy"], "Sơn phủ lớp sơn chống rỉ hoặc bôi dầu mỡ lên bề mặt đồ dùng bằng sắt thép giúp ngăn tiếp xúc với oxy và hơi ẩm.", "7-8", 2),
    ("Hòa tan và dung dịch", "Khi cho một thìa đường cát trắng vào cốc nước ấm rồi khuấy đều, đường biến mất tạo thành một chất lỏng đồng nhất gọi là gì?", "Dung dịch nước đường", ["Chất rắn hỗn hợp", "Chất khí bốc hơi", "Chất đục lơ lửng"], "Đường là chất tan, nước là dung môi, nước đường ngọt lịm thu được là một dung dịch.", "6-7", 1),
    ("Nước biển mặn vì sao", "Nước biển đại dương có vị mặn chát là do chứa một lượng lớn muối hòa tan nào?", "Muối ăn (Natri clorua - NaCl)", ["Đường saccarozo", "Bột ngọt mì chính", "Vôi sống"], "Nước mưa bào mòn các lớp đất đá trên lục địa cuốn theo muối khoáng đổ ra sông rồi dồn tích tụ lại đại dương suốt hàng tỷ năm.", "7-8", 2),
    ("Nước tinh khiết và nước khoáng", "Nước khoáng đóng chai thiên nhiên khác với nước cất tinh khiết ở điểm nào?", "Nước khoáng chứa các ion khoáng chất có lợi như Canxi, Magie, Kali hòa tan", ["Nước khoáng có màu đục", "Nước khoáng có vị ngọt đường", "Nước khoáng sôi ở 200 độ C"], "Uống nước khoáng tự nhiên giúp bổ sung các vi chất điện giải thiết yếu cho cơ thể sau khi vận động thể thao.", "7-8", 2),
    ("Sự truyền nhiệt bằng đối lưu", "Hiện tượng dòng nước nóng ở đáy ấm bốc lên trên và dòng nước lạnh trên mặt chìm xuống tạo thành vòng tuần hoàn đun sôi nước gọi là gì?", "Sự đối lưu nhiệt", ["Sự dẫn nhiệt", "Sự bức xạ nhiệt", "Sự khúc xạ"], "Đối lưu là hình thức truyền nhiệt chủ yếu trong các chất lỏng và chất khí.", "8-9", 3),
    ("Bức xạ nhiệt từ Mặt Trời", "Năng lượng nhiệt ấm áp từ Mặt Trời vượt qua khoảng chân không bao la của vũ trụ truyền tới Trái Đất bằng hình thức nào?", "Bức xạ nhiệt (Bằng các tia nhiệt hồng ngoại)", ["Dẫn nhiệt qua kim loại", "Đối lưu không khí", "Truyền qua dây dẫn"], "Bức xạ nhiệt là hình thức truyền nhiệt duy nhất có thể truyền được qua môi trường chân không tuyệt đối.", "8-9", 3),
    ("Màu sắc hấp thụ nhiệt", "Vào những ngày hè nắng gắt, mặc áo màu đen sẽ cảm thấy nóng hơn mặc áo màu trắng vì sao?", "Vì màu đen hấp thụ nhiệt bức xạ mạnh nhất, màu trắng phản xạ hầu hết nhiệt", ["Vì áo đen nặng hơn áo trắng", "Vì áo đen dày hơn", "Vì áo đen không có gió"], "Mùa hè nên mặc quần áo sáng màu (trắng, xanh nhạt) để phản xạ ánh nắng, mùa đông mặc áo màu sẫm để giữ ấm.", "7-8", 2),
    ("Gió tạo ra điện", "Những cánh quạt khổng lồ quay đều trên các cánh đồng điện gió ở Bạc Liêu, Ninh Thuận chuyển hóa dạng năng lượng nào thành điện năng?", "Chuyển hóa động năng của gió thành điện năng (Năng lượng gió)", ["Năng lượng hóa học", "Năng lượng hạt nhân", "Năng lượng địa nhiệt"], "Điện gió là nguồn năng lượng tái tạo sạch, vô tận và không phát thải khí nhà kính bảo vệ môi trường.", "7-8", 2),
    ("Pin năng lượng Mặt Trời", "Các tấm pin màu xanh sẫm lắp trên mái nhà hấp thụ ánh sáng mặt trời biến đổi trực tiếp thành điện năng gọi là gì?", "Pin quang điện (Pin năng lượng Mặt Trời)", ["Pin con thỏ", "Máy phát điện chạy xăng", "Ắc quy chì"], "Năng lượng Mặt Trời là nguồn năng lượng xanh sạch phong phú nhất hành tinh đang được ứng dụng rộng rãi.", "7-8", 2),
    ("Thủy điện tạo ra dòng điện", "Các nhà máy thủy điện Hòa Bình, Sơn La sử dụng sức mạnh nào của dòng nước để quay tua-bin phát điện?", "Thế năng và động năng của dòng nước chảy xiết từ trên đập cao đổ xuống", ["Nhiệt độ nóng của nước", "Độ mặn của nước", "Màu sắc của nước"], "Nước từ trên hồ chứa chảy qua đường ống áp lực làm quay cánh quạt tua-bin nối với máy phát điện tạo ra dòng điện mạnh mẽ.", "7-8", 2),
    ("Năng lượng không tự nhiên sinh ra", "Định luật bảo toàn năng lượng vĩ đại trong vật lý học phát biểu điều gì?", "Năng lượng không tự nhiên sinh ra cũng không tự mất đi, chỉ chuyển từ dạng này sang dạng khác", ["Năng lượng tự nhiên biến mất", "Năng lượng luôn tăng lên gấp đôi", "Năng lượng chỉ có một dạng"], "Ví dụ khi bật bóng đèn điện, điện năng được chuyển hóa thành quang năng chiếu sáng và một phần nhiệt năng làm nóng bóng đèn.", "8-9", 3),
    ("Hiện tượng cầu vồng nhân tạo", "Khi bé dùng vòi phun nước tưới cây thành các tia nước mịn li ti dưới ánh nắng mặt trời, ta thấy chiếc cầu vồng nhỏ xuất hiện là do đâu?", "Các giọt nước nhỏ tán sắc ánh sáng mặt trời giống hệt như sau cơn mưa rào", ["Do nước có màu sơn", "Do ánh nắng bị rách", "Do vòi phun đổi màu"], "Hiện tượng quang học kỳ thú này chứng minh ánh sáng mặt trời là sự tổng hợp của dải quang phổ nhiều màu sắc.", "6-7", 1),
    ("Băng nổi trên mặt nước", "Tại sao những tảng băng đá lại nổi bồng bềnh trên mặt nước lỏng thay vì chìm xuống đáy?", "Vì nước khi đóng băng giãn nở thể tích làm khối lượng riêng của băng nhẹ hơn nước lỏng", ["Vì băng đá rỗng ruột", "Vì băng đá có không khí", "Vì băng đá biết bơi"], "Đây là tính chất dị thường tuyệt vời của nước giúp các sinh vật biển vẫn bơi lội an toàn dưới lớp băng bề mặt vào mùa đông lạnh giá.", "8-9", 3),
    ("Không khí nở ra khi nóng", "Khi hơ nóng đáy một bình thủy tinh đậy kín có nút gắn ống hút cắm vào cốc nước, ta thấy bọt khí sủi ra là do đâu?", "Không khí bên trong bình nóng lên nở ra tràn qua ống hút ra ngoài", ["Nước bị sôi", "Không khí bị biến mất", "Bình thủy tinh co lại"], "Chất khí nở vì nhiệt nhiều hơn chất lỏng, và chất lỏng nở vì nhiệt nhiều hơn chất rắn.", "7-8", 2),
    ("Không khí lạnh co lại", "Quả bóng bàn bị móp méo một vết lõm, khi nhúng quả bóng vào bát nước sôi thì quả bóng tròn căng trở lại nhờ đâu?", "Không khí bên trong quả bóng gặp nhiệt độ nóng nở ra đẩy vết móp phồng lên", ["Nước sôi làm mềm vỏ bóng", "Do vỏ bóng tự vá", "Do hơi nước chui vào"], "Áp suất của khối khí nóng giãn nở bên trong đã tạo ra lực đẩy căng tròn vỏ bóng bàn trong tích tắc.", "6-7", 1),
    ("Thước nhựa cọ xát nhiễm điện", "Sau khi cọ xát chiếc thước kẻ bằng nhựa vào mảnh vải len khô, chiếc thước có thể hút các mẩu giấy vụn nhỏ nhờ hiện tượng gì?", "Hiện tượng nhiễm điện do cọ xát (Tĩnh điện)", ["Thước kẻ bị dính keo", "Thước kẻ bị từ tính như nam châm", "Mẩu giấy tự bay lên"], "Cọ xát làm dịch chuyển các hạt electron tạo nên điện tích tĩnh trên bề mặt thước kẻ hút các vật nhẹ.", "7-8", 2),
    ("Sấm sét là dòng điện khổng lồ", "Tia sét xẹt qua bầu trời trong cơn giông bão thực chất là hiện tượng tĩnh điện nào trong tự nhiên?", "Sự phóng tia lửa điện khổng lồ giữa các đám mây tích điện trái dấu hoặc giữa mây và mặt đất", ["Mặt Trời phát nổ", "Ngôi sao rơi", "Núi lửa phun khói"], "Dòng điện của tia sét có thể lên tới hàng trăm ngàn ampe và nhiệt độ nóng tới 30.000 độ C (nóng gấp 5 lần bề mặt Mặt Trời).", "8-9", 3),
    ("Cột thu lôi chống sét", "Chiếc cột kim loại nhọn gắn trên nóc các tòa nhà cao tầng có dây đồng nối sâu xuống đất gọi là gì?", "Cột thu lôi (Cột chống sét)", ["Cột cờ", "Ăng-ten xem tivi", "Cột đèn chiếu sáng"], "Cột thu lôi chủ động hút tia sét và dẫn dòng điện cực lớn chạy thẳng an toàn xuống lòng đất bảo vệ tòa nhà.", "7-8", 2),
    ("Bóng đèn sợi đốt Edison", "Nhà bác học thiên tài Thomas Edison đã phát minh ra sợi dây tóc bóng đèn sợi đốt làm bằng kim loại chịu nhiệt cao nào?", "Kim loại Vonfram (Tungsten)", ["Kim loại Đồng", "Kim loại Chì", "Kim loại Nhôm"], "Vonfram có nhiệt độ nóng chảy cao nhất trong các kim loại (hơn 3.400 độ C), phát sáng chói lọi khi dòng điện chạy qua.", "8-9", 3),
    ("Bóng đèn LED tiết kiệm điện", "Đèn LED (Đi-ốt phát quang) ngày nay được sử dụng rộng rãi thay thế bóng đèn sợi đốt truyền thống vì ưu điểm vượt trội nào?", "Tiết kiệm hơn 80% điện năng, tỏa rất ít nhiệt và tuổi thọ bền bỉ hàng chục ngàn giờ", ["Giá đắt gấp trăm lần", "Tỏa nhiệt rất nóng", "Dễ cháy nổ"], "Đèn LED chuyển đổi trực tiếp điện năng thành quang năng hiệu suất cao, là giải pháp chiếu sáng xanh cho tương lai.", "6-7", 1),
    ("Chất dẻo cách điện", "Tại sao cán kìm điện, tay cầm tuốc-nơ-vít của bác thợ điện luôn luôn được bọc lớp nhựa dày?", "Để cách điện bảo vệ thợ điện không bị dòng điện giật khi sửa chữa điện", ["Để cầm êm tay hơn", "Làm cho kìm đẹp hơn", "Để kìm không bị rơi"], "An toàn điện là nguyên tắc số 1, luôn ngắt cầu dao điện trước khi sửa chữa bất kỳ thiết bị điện gia đình nào.", "6-7", 1),
    ("Trọng lực và rơi tự do", "Hai hòn bi sắt to và nhỏ cùng thả rơi từ một độ cao trên mặt đất trong điều kiện không có sức cản không khí sẽ rơi như thế nào?", "Cả hai hòn bi sắt rơi chạm đất cùng một lúc", ["Hòn bi to rơi trước rất nhiều", "Hòn bi nhỏ rơi trước", "Hai hòn bi bay lơ lửng"], "Nhà bác học Galileo Galilei đã làm thí nghiệm thả vật rơi tự do nổi tiếng trên tháp nghiêng Pisa để chứng minh chân lý này.", "8-9", 3),
    ("Chất tan trong nước nóng", "Khi pha sữa bột hoặc đường vào nước, ta thấy đường tan nhanh hơn rất nhiều trong nước nóng so với nước lạnh là do đâu?", "Ở nhiệt độ cao các phân tử nước chuyển động nhanh hơn va đập mạnh làm tan chất nhanh hơn", ["Do nước nóng làm đường bốc hơi", "Do nước nóng ngọt hơn", "Do đường sợ nước nóng"], "Nhiệt độ làm tăng vận tốc chuyển động nhiệt hỗn loạn của các phân tử dung môi và chất tan.", "7-8", 2),
    ("Nam châm điện mạnh mẽ", "Một cuộn dây đồng quấn quanh lõi sắt non khi có dòng điện chạy qua sẽ trở thành nam châm gì có thể bật tắt lực hút linh hoạt?", "Nam châm điện", ["Nam châm vĩnh cửu", "Nam châm đất hiếm", "Thanh sắt vô tri"], "Nam châm điện được ứng dụng trong cần cẩu phế liệu bốc dỡ hàng tấn sắt thép ở các bến cảng nhà máy.", "8-9", 3),
    ("Ứng dụng nam châm trong đời sống", "Đồ vật quen thuộc nào trong gia đình bé có gắn nam châm ở mép cánh cửa để hút đóng kín giữ nhiệt?", "Cánh cửa tủ lạnh", ["Cửa sổ gỗ", "Cửa phòng tắm", "Cửa tủ quần áo"], "Lớp gioăng cao su bọc dải nam châm mềm quanh viền cửa tủ lạnh giúp hút chặt cánh cửa ngăn khí lạnh thất thoát.", "6-7", 1)
]

raw_mc.extend(more_mc_vc)

# 14 SA items (VC127 - VC140)
raw_sa = [
    ("Ba thể vật chất", "Nước đá là thể rắn, nước lọc là thể lỏng, vậy hơi nước bốc lên là vật chất ở thể gì?", "thể khí|khí|thể hơi|hơi", "Hơi nước bốc lên bay lơ lửng trong không khí ở thể khí.", "6-7", 1),
    ("Đá tan thành nước", "Hiện tượng nước đá viên chuyển từ thể rắn sang thể lỏng khi gặp nhiệt độ ấm gọi là hiện tượng gì?", "nóng chảy|sự nóng chảy", "Nóng chảy là sự biến đổi trạng thái từ rắn sang lỏng khi nhiệt độ tăng.", "6-7", 1),
    ("Nước hóa thành đá", "Hiện tượng nước lỏng để trong ngăn đông tủ lạnh đông cứng thành đá viên gọi là hiện tượng gì?", "đông đặc|sự đông đặc", "Đông đặc là sự biến đổi trạng thái từ lỏng sang rắn khi gặp lạnh.", "6-7", 1),
    ("Khí cần cho sự cháy", "Khí nào trong không khí chiếm 21% cần thiết cho sự thở của con người và duy trì sự cháy?", "khí oxy|oxy|o2", "Khí oxy là nguồn cội của sự hô hấp và duy trì sự cháy trên Trái Đất.", "6-7", 1),
    ("Đường truyền ánh sáng", "Trong không khí trong lành, ánh sáng truyền đi theo đường gì?", "đường thẳng|thẳng", "Ánh sáng luôn truyền theo đường thẳng trong môi trường đồng tính.", "6-7", 1),
    ("Nguồn gốc âm thanh", "Mọi âm thanh phát ra xung quanh chúng ta đều có nguồn gốc từ sự chuyển động gì của vật?", "rung động|dao động|sự rung động", "Âm thanh sinh ra do sự dao động rung rinh của vật thể.", "7-8", 2),
    ("Hai cực của nam châm", "Thanh nam châm có hai cực từ đối lập nhau là cực Bắc và cực gì?", "cực nam|nam", "Nam châm có cực Bắc (N) và cực Nam (S).", "6-7", 1),
    ("Lực hút của Trái Đất", "Lực bí mật kéo mọi vật rơi xuống đất và giữ bầu khí quyển không bay mất gọi là lực gì?", "trọng lực|lực hấp dẫn|lực hút trái đất", "Trọng lực kéo mọi vật thể rơi về phía tâm Trái Đất.", "6-7", 1),
    ("Kim loại làm lõi dây điện", "Kim loại màu đỏ cam dẻo dai dẫn điện rất tốt được dùng làm lõi dây điện gia đình là kim loại gì?", "đồng", "Đồng dẫn điện tốt và dẻo dai được dùng làm dây điện.", "6-7", 1),
    ("Chất liệu bọc dây điện", "Chất liệu không dẫn điện (cách điện) an toàn được dùng làm vỏ bọc ngoài dây điện là chất gì?", "nhựa|cao su|chất nhựa", "Nhựa và cao su cách điện an toàn bảo vệ con người.", "6-7", 1),
    ("Sóng âm dội lại", "Âm thanh va vào vách đá dội ngược lại tai chúng ta nghe thấy gọi là hiện tượng gì?", "tiếng vang|tiếng vọng", "Tiếng vang là âm thanh phản xạ nghe thấy sau âm trực tiếp.", "7-8", 2),
    ("Dụng cụ hứng ánh sáng hội tụ", "Thấu kính lồi cầm tay giúp phóng to chữ nhỏ và hội tụ ánh sáng mặt trời gọi là kính gì?", "kính lúp", "Kính lúp phóng to hình ảnh các vật thể li ti.", "6-7", 1),
    ("Nước sôi ở nhiệt độ", "Ở điều kiện áp suất bình thường, nước tinh khiết sôi sục ở bao nhiêu độ C?", "100|100 độ|100 độ c", "Nước sôi ở mốc 100 độ C trên thang nhiệt độ.", "6-7", 1),
    ("Chất tan trong nước", "Gia vị màu trắng có vị mặn tan hoàn toàn trong nước tạo thành nước muối gọi là gì?", "muối|muối ăn", "Muối ăn tan hoàn toàn trong nước tạo thành dung dịch nước muối.", "6-7", 1)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"VC{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vật Chất & Hiện Tượng",
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
    qid = f"VC{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vật Chất & Hiện Tượng",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/vc_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành toàn bộ VC: {len(questions)} câu đã được ghi vào vc_140.json")

# Bổ sung 50 câu MC còn thiếu cho VC
extra_vc_50 = [
    ("Nến cháy tỏa nhiệt và sáng", "Khi ngọn nến đang cháy, sáp nến bị nóng chảy thành chất lỏng rồi biến đổi hóa học tạo ra sản phẩm gì?", "Khí cacbonic (CO2) và hơi nước tỏa nhiệt phát sáng", ["Khí oxy", "Khí hydro", "Bột sắt"], "Ngọn lửa nến là phản ứng cháy oxy hóa của sáp nến với oxy không khí.", "7-8", 2),
    ("Băng khô là gì", "Băng khô (đá khói) thường dùng để làm khói sân khấu và bảo quản kem lạnh thực chất là chất gì ở thể rắn?", "Khí cacbonic (CO2) đóng băng ở -78,5 độ C", ["Nước đá bình thường", "Khí oxy đông cứng", "Bột thạch cao"], "Băng khô thăng hoa trực tiếp từ thể rắn sang thể khí mà không tan chảy qua thể lỏng.", "8-9", 3),
    ("Hiện tượng thăng hoa", "Quá trình một chất chuyển thẳng từ thể rắn sang thể khí mà không qua thể lỏng gọi là gì?", "Hiện tượng thăng hoa", ["Hiện tượng nóng chảy", "Hiện tượng ngưng tụ", "Hiện tượng bay hơi"], "Viên băng phiến (long não) để trong tủ quần áo lâu ngày tự teo nhỏ rồi biến mất là hiện tượng thăng hoa.", "8-9", 3),
    ("Hiện tượng ngưng kết", "Quá trình chất khí chuyển thẳng thành thể rắn khi bị làm lạnh đột ngột gọi là gì?", "Hiện tượng ngưng kết (Lắng đọng)", ["Hiện tượng thăng hoa", "Hiện tượng đông đặc", "Hiện tượng nóng chảy"], "Hiện tượng sương muối hình thành vào những đêm đông giá buốt là hơi nước trong không khí ngưng kết trực tiếp thành tinh thể băng.", "8-9", 3),
    ("Trộn giấm với baking soda", "Khi ta đổ giấm ăn vào một thìa bột nở (baking soda), hiện tượng sủi bọt khí mạnh mẽ xảy ra là do sinh ra khí gì?", "Khí cacbonic (CO2)", ["Khí oxy", "Khí nitơ", "Khí gas"], "Phản ứng giữa axit axetic trong giấm và natri hidrocacbonat tạo ra bọt khí CO2 sủi ào ạt như núi lửa mini.", "7-8", 2),
    ("Gọt táo bị thâm nâu", "Tại sao miếng táo sau khi gọt vỏ để ngoài không khí một lúc lại bị đổi màu sang thâm nâu?", "Do enzym trong táo phản ứng với khí oxy không khí làm oxy hóa các hợp chất hữu cơ", ["Do táo bị nhiễm bụi", "Do táo bị lạnh", "Do dao cắt bị bẩn"], "Vắt một chút nước cốt chanh lên mặt lát táo vừa gọt sẽ giúp axit citric ngăn chặn phản ứng thâm nâu giữ táo tươi ngon.", "7-8", 2),
    ("Chảo chống dính phủ Teflon", "Lớp chống dính màu đen phủ trên bề mặt chảo chiên rán giúp thức ăn không bị bám dính làm từ vật liệu gì?", "Hợp chất polymer Teflon (PTFE)", ["Chất bơ thực vật", "Mỡ động vật", "Lớp gốm nung"], "Teflon có hệ số ma sát cực thấp và khả năng trơ hóa học chịu nhiệt tốt, giúp rán trứng không cần nhiều dầu mỡ.", "8-9", 3),
    ("Kính cường lực an toàn", "Kính cường lực lắp cửa sổ và lan can nhà ở khi bị va đập vỡ sẽ vỡ thành những mảnh như thế nào?", "Vỡ vụn thành các hạt nhỏ tròn như hạt lựu không có cạnh sắc nhọn gây nguy hiểm", ["Vỡ thành các mảnh dao sắc nhọn", "Biến thành bột cát", "Không bao giờ vỡ"], "Kính được tôi nhiệt rồi làm nguội nhanh tạo ứng suất nén bề mặt giúp chịu lực gấp 5 lần kính thường.", "8-9", 3),
    ("Lốp xe bơm căng mùa hè", "Tại sao vào mùa hè nắng gắt ta không nên bơm lốp xe đạp hay xe máy quá căng?", "Vì không khí bên trong lốp nở vì nhiệt có thể làm nổ lốp xe nguy hiểm", ["Vì xe sẽ chạy chậm", "Vì tốn công bơm", "Vì lốp sẽ bị xẹp"], "Mặt đường nhựa hấp thụ nhiệt lên tới 60 độ C truyền nhiệt làm không khí trong lốp giãn nở tăng áp suất mạnh mẽ.", "7-8", 2),
    ("Làm lạnh nhanh lon nước ngọt", "Để làm lạnh nhanh một lon nước ngọt trong thùng đá, ta nên cho thêm chất gì vào nước đá?", "Cho thêm một nắm muối ăn vào nước đá", ["Cho thêm đường", "Cho thêm nước sôi", "Cho thêm dầu ăn"], "Muối làm hạ điểm đóng băng của nước đá xuống dưới 0 độ C tạo ra hỗn hợp sinh hàn cực lạnh làm mát lon nước trong tích tắc.", "8-9", 3),
    ("Nam châm dẻo đính tủ lạnh", "Miếng dán trang trí ngộ nghĩnh dính trên cánh cửa tủ lạnh làm từ loại nam châm nào?", "Nam châm dẻo (Bột từ tính trộn cao su hoặc polymer)", ["Nam châm kim loại cứng", "Nam châm điện", "Đá bazan"], "Nam châm dẻo có thể uốn cong, cắt xén dễ dàng và có lực hút vừa đủ để giữ giấy ghi chú trên bề mặt thép tủ lạnh.", "7-8", 2),
    ("Cực quang và từ trường", "Từ trường Trái Đất bảo vệ chúng ta khỏi hiểm họa nào từ vũ trụ bao la?", "Chắn gió Mặt Trời và các tia vũ trụ năng lượng cao bắn phá vào mặt đất", ["Chắn ánh sáng mặt trời", "Chắn mưa rơi", "Chắn thiên thạch to"], "Từ trường Trái Đất bẻ cong quỹ đạo của các hạt mang điện, dẫn chúng về hai cực tạo nên hiện tượng cực quang tuyệt mỹ.", "8-9", 3),
    ("Sự nổi của quả trứng", "Một quả trứng tươi thả vào cốc nước lọc thì chìm, nhưng khi hòa thêm thật nhiều muối vào cốc nước thì quả trứng lại nổi lên là vì sao?", "Vì nước muối đặc có khối lượng riêng lớn hơn quả trứng", ["Vì muối làm trứng nhẹ đi", "Vì trứng bị biến chất", "Vì muối có lực đẩy nam châm"], "Thêm muối làm tăng khối lượng riêng của dung dịch nước, khi khối lượng riêng của nước muối lớn hơn trứng thì lực đẩy Ác-si-mét đẩy trứng nổi lên.", "7-8", 2),
    ("Nước biển Chết không chìm", "Biển Chết ở Trung Đông có độ mặn cực kỳ cao (gấp 10 lần biển thường), người xuống tắm có hiện tượng kỳ thú nào?", "Con người tự động nổi bồng bềnh trên mặt nước mà không sợ bị chìm kể cả không biết bơi", ["Bị chìm nghỉm xuống đáy", "Nước sôi sục", "Biến thành tảng muối"], "Khối lượng riêng của nước biển Chết quá đậm đặc tạo lực đẩy khổng lồ nâng đỡ cơ thể con người nổi tự nhiên như phao.", "8-9", 3),
    ("Bóng bay khí Heli", "Quả bóng bay có thể tự bay vút lên cao trên bầu trời vì bên trong được bơm loại khí nhẹ nào?", "Khí Heli (Helium)", ["Khí Oxy", "Khí Cacbonic", "Khí Gas"], "Khí heli nhẹ hơn không khí xung quanh rất nhiều nên quả bóng chịu lực đẩy Ác-si-mét nâng bay lên cao.", "6-7", 1),
    ("Khí Hydro dễ nổ", "Tại sao người ta không nên bơm khí hydro vào bóng bay đồ chơi cho trẻ em?", "Vì khí hydro rất dễ bắt lửa gây cháy nổ nguy hiểm bỏng mặt", ["Vì khí hydro quá nặng", "Vì khí hydro có mùi hôi", "Vì khí hydro đắt tiền"], "Khí hydro phản ứng cháy nổ dữ dội với oxy khi gặp tàn thuốc lá hoặc tia lửa nhỏ, heli là khí trơ an toàn hơn.", "7-8", 2),
    ("Băng dính dán dính đồ", "Lớp keo dính trên băng dính dán chặt hai tờ giấy lại với nhau nhờ lực liên kết nào giữa các phân tử?", "Lực bám dính phân tử (Adhesion force)", ["Lực từ trường nam châm", "Trọng lực Trái Đất", "Lực ma sát"], "Các phân tử keo len lỏi vào các khe vi mô của bề mặt giấy tạo thành các cầu nối liên kết bền vững.", "7-8", 2),
    ("Gọt vỏ bút chì bằng gọt chì", "Lưỡi dao gọt bút chì gọt gỗ bút chì dễ dàng vì sao?", "Lưỡi thép của đồ gọt chì có độ cứng lớn hơn nhiều so với gỗ và ruột chì", ["Gỗ bút chì làm bằng nhựa", "Đồ gọt chì có động cơ", "Ruột chì tự gãy"], "Quy tắc gia công vật liệu: vật liệu có độ cứng lớn hơn có thể cắt gọt được vật liệu có độ cứng nhỏ hơn.", "6-7", 1),
    ("Ruột bút chì làm bằng gì", "Ruột màu đen xám của chiếc bút chì viết bài hàng ngày thực chất được làm từ chất gì?", "Khoáng chất Than chì (Graphite) trộn với đất sét", ["Làm bằng kim loại chì độc hại", "Làm bằng than củi đen", "Làm bằng sắt vụn"], "Than chì mềm, gồm các lớp nguyên tử cacbon trượt lên nhau để lại vệt xám đen rõ ràng trên trang giấy trắng.", "7-8", 2),
    ("Kim cương và than chì", "Viên kim cương lấp lánh cứng nhất hành tinh và ruột bút chì đen xốp mềm thực chất đều cấu tạo từ một nguyên tố hóa học duy nhất nào?", "Nguyên tố Cacbon (C)", ["Nguyên tố Sắt", "Nguyên tố Vàng", "Nguyên tố Nhôm"], "Cùng là cacbon nhưng kim cương có cấu trúc tinh thể mạng lưới tứ diện cực kỳ vững chắc dưới áp suất và nhiệt độ khổng lồ trong lòng đất.", "8-9", 3),
    ("Thủy tinh trong suốt làm từ đâu", "Cốc thủy tinh trong suốt, cửa kính nhà ở được sản xuất chủ yếu bằng cách nung chảy nguyên liệu tự nhiên nào?", "Cát thạch anh (Silica / Cát trắng)", ["Đất sét đỏ", "Gỗ cây", "Đá vôi vụn"], "Cát thạch anh được nung chảy ở nhiệt độ trên 1.700 độ C rồi làm nguội định hình thành các sản phẩm thủy tinh trong suốt.", "7-8", 2),
    ("Gốm sứ từ đất sét", "Bát đĩa, chén chén ấm trà bằng gốm sứ được tạo hình từ đất sét dẻo rồi nung qua nhiệt độ nào?", "Nung trong lò gốm ở nhiệt độ cao từ 1.000 đến 1.300 độ C", ["Để phơi ngoài trời nắng", "Nung trong nước sôi 100 độ", "Cho vào tủ lạnh"], "Nhiệt độ cao biến đổi cấu trúc khoáng vật của đất sét thành khối gốm sứ cứng chắc, không thấm nước và bền đẹp.", "7-8", 2),
    ("Giấy viết từ cây gỗ", "Những trang vở trắng tinh khôi của học sinh được sản xuất chủ yếu từ thành phần tự nhiên nào?", "Sợi cellulose chiết xuất từ thân cây gỗ (như keo, bạch đàn, tre nứa)", ["Từ đá vôi nghiền mịn", "Từ lông thú", "Từ nhựa dầu mỏ"], "Sợi gỗ được nấu thành bột giấy, tẩy trắng rồi cán mỏng sấy khô thành những cuộn giấy viết mịn màng.", "6-7", 1),
    ("Cao su tự nhiên đàn hồi", "Chất liệu làm săm lốp xe đạp, cục tẩy bút chì và đệm ngủ êm ái có tính đàn hồi vượt trội là gì?", "Cao su (Mủ cây cao su thiên nhiên)", ["Chất nhựa cứng", "Kim loại dẻo", "Gỗ xốp"], "Cao su có cấu trúc các chuỗi phân tử polymer uốn lượn như lò xo, khi kéo giãn ra rồi buông tay sẽ tự co về hình dạng cũ.", "6-7", 1),
    ("Cục tẩy xóa vết bút chì", "Khi ta dùng cục tẩy chà xát lên vết bút chì trên giấy, vết chì biến mất nhờ cơ chế nào?", "Chất cao su của cục tẩy dính chặt lấy các hạt than chì trên giấy và cuộn bóc chúng ra ngoài", ["Cục tẩy xóa bằng mực trắng", "Cục tẩy làm giấy tan biến", "Cục tẩy đốt cháy than chì"], "Cục tẩy mòn dần thành các vụn tẩy cuốn theo hạt than chì trả lại bề mặt trang giấy sạch sẽ.", "6-7", 1),
    ("Mực bút bi chảy đều", "Viên bi siêu nhỏ bằng tungsten carbide ở đầu ngòi chiếc bút bi có tác dụng cơ học gì?", "Lăn tròn đều đặn cuốn mực đặc từ ống mực ra tiếp xúc với mặt giấy", ["Để làm ngòi bút nhọn", "Để giữ cho mực không chảy", "Để bút không bị rơi"], "Khi viết, ma sát với mặt giấy làm viên bi xoay tròn kéo lớp mực mỏng trải đều tạo nên nét chữ liền mạch sắc nét.", "7-8", 2),
    ("Đòn bẩy bập bênh", "Trò chơi bập bênh ngoài sân trường và chiếc kéo cắt giấy hoạt động dựa trên nguyên lý máy cơ đơn giản nào?", "Nguyên lý đòn bẩy (Có điểm tựa, điểm đặt lực và điểm tải)", ["Mặt phẳng nghiêng", "Ròng rọc", "Bánh xe trục quay"], "Đòn bẩy giúp con người nâng bổng vật nặng hoặc cắt gọt vật liệu một cách nhẹ nhàng tốn ít sức lực hơn.", "6-7", 1),
    ("Mặt phẳng nghiêng dắt xe", "Tấm ván dốc bắc từ mặt đường lên bậc thềm nhà để dắt xe máy vào nhà là ứng dụng của máy cơ nào?", "Mặt phẳng nghiêng", ["Ròng rọc cố định", "Đòn bẩy", "Bánh xe răng cưa"], "Mặt phẳng nghiêng làm giảm lực kéo cần thiết để đưa vật lên cao, độ dốc càng thoai thoải thì dắt xe càng nhẹ nhàng.", "7-8", 2),
    ("Ròng rọc kéo cờ", "Chiếc bánh xe có rãnh gắn trên đỉnh cột cờ luồn sợi dây kéo lá cờ đỏ sao vàng lên cao là máy cơ đơn giản nào?", "Ròng rọc cố định", ["Mặt phẳng nghiêng", "Đòn bẩy", "Bánh răng"], "Ròng rọc cố định không làm giảm lực kéo nhưng giúp đổi hướng của lực kéo: kéo dây xuống dưới thì lá cờ bay vút lên trên.", "7-8", 2),
    ("Bánh xe và trục quay", "Phát minh vĩ đại thời cổ đại giúp con người vận chuyển hàng hóa nặng nề đi xa mà tốn ít sức lực nhất là gì?", "Bánh xe tròn gắn vào trục quay", ["Đôi ủng da", "Cái gùi đeo lưng", "Tấm ván trượt"], "Bánh xe biến ma sát trượt thành ma sát lăn cực nhỏ, mở ra cuộc cách mạng giao thông vận tải của nhân loại.", "6-7", 1),
    ("Sự gỉ sét của đinh sắt trong nước", "Một chiếc đinh sắt thả trong cốc nước có hòa muối sẽ bị rỉ sét nhanh hơn trong cốc nước sạch vì sao?", "Nước muối dẫn điện tốt hơn làm tăng tốc độ ăn mòn điện hóa của kim loại", ["Muối ăn mòn bằng răng", "Muối làm nước nóng lên", "Đinh sắt thích muối"], "Môi trường nước biển mặn khiến tàu thuyền kim loại và công trình cầu cảng bị ăn mòn rỉ sét rất nhanh chóng.", "8-9", 3),
    ("Gương cầu lồi ngã ba đường", "Chiếc gương hình cầu cong lồi lắp ở các khúc cua đèo dốc hoặc bãi đỗ xe có ưu điểm quang học nào?", "Cho vùng quan sát rộng hơn nhiều so với gương phẳng giúp tài xế quan sát góc khuất", ["Phóng to hình ảnh", "Đổi màu xe cộ", "Làm xe chạy chậm lại"], "Gương cầu lồi tạo ảnh ảo nhỏ hơn vật nhưng mở rộng trường nhìn góc nhìn giúp đảm bảo an toàn giao thông.", "7-8", 2),
    ("Gương cầu lõm nha sĩ", "Chiếc gương nhỏ có mặt kính cong lõm vào trong mà bác sĩ nha khoa dùng soi răng có tác dụng gì?", "Cho hình ảnh ảo phóng to rõ nét của chiếc răng sâu trong khoang miệng", ["Làm nhỏ chiếc răng", "Làm sáng bóng răng", "Không có tác dụng gì"], "Gương cầu lõm hội tụ ánh sáng và phóng đại hình ảnh khi vật đặt gần tiêu cự, giúp bác sĩ nhìn rõ từng lỗ sâu nhỏ.", "8-9", 3),
    ("Tia laser hội tụ", "Chùm ánh sáng laser đỏ phát ra từ chiếc bút chỉ laser có đặc điểm nổi bật nào khác với bóng đèn thường?", "Tia sáng truyền thẳng định hướng cao, cùng một bước sóng đơn sắc và tập trung năng lượng cao", ["Tia sáng tỏa rộng ra mọi phía", "Tia sáng có nhiều màu sắc", "Tia sáng uốn cong vòng"], "Tia laser được ứng dụng trong phẫu thuật y tế mắt, đọc đĩa CD, quét mã vạch siêu thị và gia công cắt kim loại.", "8-9", 3),
    ("Sợi quang học dẫn ánh sáng", "Dây cáp quang truyền internet tốc độ cao xuyên đại dương truyền tín hiệu bằng gì bên trong sợi thủy tinh trong suốt?", "Truyền bằng các xung ánh sáng dựa trên hiện tượng phản xạ toàn phần", ["Truyền bằng dòng nước chảy", "Truyền bằng âm thanh rung", "Truyền bằng áp lực gió"], "Ánh sáng phản xạ zig-zag liên tục bên trong lõi sợi thủy tinh truyền đi hàng ngàn km với tốc độ ánh sáng cực nhanh.", "8-9", 3),
    ("Sóng điện từ xung quanh", "Tín hiệu sóng wifi, sóng điện thoại di động và sóng radio truyền thông tin qua không gian bằng loại sóng gì?", "Sóng điện từ (Sóng vô tuyến)", ["Sóng âm thanh", "Sóng nước", "Sóng gió"], "Sóng điện từ truyền đi với tốc độ ánh sáng trong không gian và có thể truyền được qua cả môi trường chân không.", "8-9", 3),
    ("Vi sóng hâm nóng thức ăn", "Chiếc lò vi sóng (Microwave) trong bếp làm nóng thức ăn nhanh chóng bằng cách nào?", "Sóng vi ba làm các phân tử nước trong thức ăn dao động ma sát sinh nhiệt từ bên trong", ["Dùng ngọn lửa ga", "Dùng dây mayso đỏ rực", "Thổi hơi nóng từ ngoài vào"], "Sóng vi ba xuyên sâu vào thức ăn kích thích các phân tử nước quay hàng tỷ lần mỗi giây tạo nhiệt lượng làm nóng đều đặn.", "8-9", 3),
    ("Tủ lạnh làm lạnh bằng gì", "Tủ lạnh làm mát đồ ăn bằng cách dùng máy nén tuần hoàn chất làm lạnh (gas lạnh) để làm gì?", "Hút nhiệt lượng bên trong tủ rồi tỏa nhiệt ra dàn nóng phía sau lưng tủ", ["Thổi đá lạnh vào tủ", "Sản xuất ra tuyết", "Hút hết không khí"], "Chất làm lạnh bay hơi ở dàn lạnh bên trong hút nhiệt, sau đó bị máy nén ép hóa lỏng ở dàn nóng bên ngoài tỏa nhiệt ra phòng.", "8-9", 3),
    ("Máy điều hòa nhiệt độ", "Vào mùa hè nóng bức, chiếc máy điều hòa phả ra luồng gió mát rượi trong phòng thực chất là do nguyên lý gì?", "Hút không khí nóng trong phòng qua dàn lạnh để hạ nhiệt rồi thổi ngược lại phòng mát mẻ", ["Tạo ra băng tuyết", "Phun nước mát vào phòng", "Đổi màu không khí"], "Hơi nước trong không khí gặp dàn lạnh bị ngưng tụ thành nước chảy theo ống dẫn thoát ra ngoài giúp phòng khô ráo mát mẻ.", "7-8", 2),
    ("Bình chữa cháy bọt tuyết", "Khi dập tắt đám cháy xăng dầu, tại sao người ta tuyệt đối KHÔNG ĐƯỢC dùng nước dội vào ngọn lửa?", "Vì xăng dầu nhẹ hơn nước, nổi lên trên mặt nước và loang rộng làm đám cháy bùng to hơn", ["Vì nước làm xăng bay hơi", "Vì nước dẫn điện", "Vì nước đắt tiền"], "Phải dùng cát khô hoặc bình bọt chữa cháy phủ kín bề mặt để cách ly hoàn toàn nguồn oxy tiếp xúc với xăng dầu.", "8-9", 3),
    ("Nước cứng và nước mềm", "Nước giếng khoan chứa nhiều muối canxi và magie hòa tan làm xà phòng khó sủi bọt gọi là loại nước gì?", "Nước cứng", ["Nước mềm", "Nước cất", "Nước ngọt"], "Đun sôi nước cứng lâu ngày tạo thành lớp cặn vôi màu trắng bám chặt dưới đáy ấm đun nước.", "8-9", 3),
    ("Ấm đun nước có cặn vôi", "Để tẩy sạch lớp cặn vôi trắng bám dưới đáy ấm đun nước, mẹo vặt gia đình đơn giản và hiệu quả nhất là gì?", "Đổ giấm ăn hoặc nước cốt chanh vào đun sôi ngâm một lúc rồi rửa sạch", ["Dùng dao cạo mạnh", "Rắc muối ăn vào", "Đổ dầu ăn vào"], "Axit axetic trong giấm phản ứng với canxi cacbonat trong cặn vôi tạo thành muối tan dễ dàng rửa trôi sạch bóng.", "7-8", 2),
    ("Sơn phủ chống gỉ", "Các cây cầu thép, cột điện và tàu thủy bằng sắt thép luôn được sơn các lớp sơn phủ dày nhằm mục đích gì?", "Cách ly bề mặt sắt thép khỏi tiếp xúc trực tiếp với nước và oxy không khí chống rỉ sét", ["Để cây cầu nặng hơn", "Làm cầu thơm hơn", "Chỉ để làm đẹp cho cầu"], "Sơn chống rỉ là lớp áo giáp bảo vệ kéo dài tuổi thọ của các công trình xây dựng bằng kim loại qua nhiều thập kỷ.", "7-8", 2),
    ("Chất giặt rửa xà phòng", "Phân tử xà phòng giặt rửa vết dầu mỡ trên áo quần nhờ có cấu tạo hai đầu đặc biệt nào?", "Một đầu ưa nước gắn vào nước và một đầu ưa dầu gắn bẫy lấy hạt dầu mỡ kéo trôi đi", ["Cả hai đầu đều sợ nước", "Xà phòng đốt cháy dầu mỡ", "Xà phòng nhuộm trắng vải"], "Nước cuốn theo các hạt phân tử xà phòng bọc lấy vết bẩn rửa trôi sạch sẽ trả lại tấm vải tinh tươm.", "8-9", 3),
    ("Muối ăn là hợp chất", "Hạt muối ăn quen thuộc hàng ngày có công thức hóa học gồm hai nguyên tố nào kết hợp với nhau?", "Natri (Na) và Clo (Cl) tạo thành Natri clorua (NaCl)", ["Sắt và Oxy", "Hydro và Oxy", "Cacbon và Oxy"], "Khí clo độc hại và kim loại natri nổ khi gặp nước kết hợp lại thành hạt muối ăn vô cùng thiết yếu cho sự sống muôn loài.", "8-9", 3),
    ("Nước tinh khiết là H2O", "Phân tử nước tinh khiết (H2O) gồm có 2 nguyên tử của nguyên tố nào gắn với 1 nguyên tử oxy?", "2 nguyên tử Hydro (H)", ["2 nguyên tử Cacbon", "2 nguyên tử Sắt", "2 nguyên tử Nitơ"], "Nước là dung môi phổ biến nhất của sự sống, chiếm phần lớn cơ thể mọi sinh vật trên Trái Đất.", "7-8", 2),
    ("Trọng lượng riêng của nước", "Một lít nước tinh khiết ở nhiệt độ 4 độ C có khối lượng đúng bằng bao nhiêu kilôgam?", "Đúng bằng 1 kilôgam (1 kg)", ["Nặng 10 kg", "Nặng 0,5 kg", "Nặng 100 kg"], "Đây là quy ước chuẩn của hệ đo lường quốc tế: 1 lít nước nguyên chất tương đương đúng 1 kg khối lượng.", "7-8", 2),
    ("Hiện tượng mao dẫn rễ cây", "Nước từ rễ cây có thể tự động leo ngược lên các cành lá cao hàng chục mét nhờ hiện tượng vật lý nào?", "Hiện tượng mao dẫn trong các ống mạch gỗ siêu nhỏ kết hợp thoát hơi nước ở lá", ["Do rễ cây có máy bơm", "Do gió hút lên", "Do trọng lực đẩy"], "Lực căng bề mặt của nước và lực bám dính của phân tử nước vào thành ống vi mạch kéo cột nước dâng cao.", "8-9", 3),
    ("Hiện tượng khúc xạ ánh sáng", "Khi ta cắm một chiếc đũa hoặc ống hút vào cốc nước trong suốt, ta nhìn thấy chiếc đũa như bị gãy khúc ở mặt nước là do đâu?", "Do hiện tượng khúc xạ ánh sáng (Tia sáng bị bẻ gãy đổi hướng khi truyền qua hai môi trường khác nhau)", ["Chiếc đũa bị gãy thật", "Do nước có dao cắt", "Do mắt nhìn nhầm"], "Vận tốc truyền ánh sáng trong nước chậm hơn trong không khí khiến tia sáng bị bẻ cong tạo nên ảo ảnh gãy khúc kỳ thú.", "7-8", 2),
    ("Kính hiển vi phóng đại", "Dụng cụ quang học trong phòng thí nghiệm dùng hệ thống thấu kính để quan sát các vi khuẩn và tế bào siêu nhỏ là gì?", "Kính hiển vi", ["Kính thiên văn", "Kính râm", "Kính lúp cầm tay"], "Kính hiển vi quang học có thể phóng đại hình ảnh các vật thể li ti lên tới hàng ngàn lần.", "7-8", 2)
]

raw_mc.extend(extra_vc_50)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"VC{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vật Chất & Hiện Tượng",
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
    qid = f"VC{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vật Chất & Hiện Tượng",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/vc_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành toàn bộ VC: {len(questions)} câu đã được ghi vào vc_140.json")
