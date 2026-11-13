# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1527482797697-8795b05a13fe?w=600&auto=format&fit=crop&q=80"
]

# 135 MC items
raw_mc = [
    # 1-35 Hệ Mặt Trời & Hành tinh
    ("Mặt Trời ngôi sao", "Mặt Trời ở trung tâm hệ của chúng ta thực chất là một thiên thể thuộc loại nào?", "Một ngôi sao khổng lồ tự phát sáng và tỏa nhiệt", ["Một hành tinh bằng đá lạnh", "Một vệ tinh quay quanh Trái Đất", "Một đám mây bụi"], "Mặt Trời là một quả cầu khí nóng sáng rực rỡ cung cấp ánh sáng và sự sống cho muôn loài trên Trái Đất.", "6-7", 1),
    ("Trái Đất hành tinh xanh", "Hành tinh thứ ba tính từ Mặt Trời, nơi duy nhất trong Hệ Mặt Trời được biết có sự sống là hành tinh nào?", "Trái Đất", ["Sao Hỏa", "Sao Kim", "Sao Mộc"], "Trái Đất được gọi là 'Hành tinh Xanh' vì hơn 70% bề mặt được bao phủ bởi các đại dương nước mênh mông.", "6-7", 1),
    ("Sao Thủy gần Mặt Trời", "Hành tinh nào nằm ở vị trí gần Mặt Trời nhất trong Hệ Mặt Trời?", "Sao Thủy (Mercury)", ["Sao Kim", "Sao Hỏa", "Trái Đất"], "Sao Thủy là hành tinh nhỏ nhất trong 8 hành tinh và có bề mặt đầy các hố va chạm giống Mặt Trăng.", "7-8", 2),
    ("Sao Kim nóng nhất", "Hành tinh nào sáng nhất trên bầu trời đêm (thường gọi là Sao Hôm hoặc Sao Mai) và nóng nhất Hệ Mặt Trời?", "Sao Kim (Venus)", ["Sao Thủy", "Sao Hỏa", "Sao Thổ"], "Sao Kim có bầu khí quyển CO2 dày đặc tạo hiệu ứng nhà kính cực mạnh khiến nhiệt độ bề mặt lên tới hơn 460 độ C.", "7-8", 2),
    ("Sao Hỏa hành tinh đỏ", "Hành tinh nào có bề mặt phủ đầy bụi oxit sắt màu đỏ cam gạch, được con người phóng nhiều tàu thăm dò nhất?", "Sao Hỏa (Mars)", ["Sao Thổ", "Sao Mộc", "Sao Thiên Vương"], "Sao Hỏa có ngọn núi lửa Olympus Mons cao nhất Hệ Mặt Trời và các thung lũng từng có dòng nước chảy thời cổ đại.", "7-8", 2),
    ("Sao Mộc khổng lồ", "Hành tinh to lớn nhất trong Hệ Mặt Trời có Vết Đỏ Lớn khổng lồ là một cơn bão kéo dài hàng thế kỷ là gì?", "Sao Mộc (Jupiter)", ["Sao Thổ", "Sao Hải Vương", "Trái Đất"], "Sao Mộc là một hành tinh khí khổng lồ, thể tích của nó có thể chứa vừa vặn hơn 1.300 Trái Đất.", "7-8", 2),
    ("Sao Thổ vành đai tráng lệ", "Hành tinh nào nổi tiếng với hệ thống vành đai băng đá và bụi sáng lấp lánh tráng lệ nhất Hệ Mặt Trời?", "Sao Thổ (Saturn)", ["Sao Mộc", "Sao Hỏa", "Sao Kim"], "Vành đai của Sao Thổ cấu tạo từ hàng tỷ tảng băng và hạt bụi quay quanh xích đạo của hành tinh.", "7-8", 2),
    ("Sao Thiên Vương nghiêng hẳn", "Hành tinh màu xanh ngọc lam nào quay nghiêng gần như nằm ngang trên mặt phẳng quỹ đạo quanh Mặt Trời?", "Sao Thiên Vương (Uranus)", ["Sao Hải Vương", "Sao Thổ", "Sao Thủy"], "Sao Thiên Vương có trục nghiêng tới 98 độ, khiến một cực của nó hướng về Mặt Trời suốt 42 năm liên tục.", "8-9", 3),
    ("Sao Hải Vương xa nhất", "Hành tinh thứ 8 xa Mặt Trời nhất, có màu xanh thẳm của khí mêtan và những cơn gió bão mạnh nhất Hệ Mặt Trời?", "Sao Hải Vương (Neptune)", ["Sao Thiên Vương", "Sao Mộc", "Trái Đất"], "Sao Hải Vương có gió bão thổi nhanh gấp nhiều lần vận tốc âm thanh, mất 165 năm Trái Đất để quay một vòng quanh Mặt Trời.", "8-9", 3),
    ("Mặt Trăng vệ tinh", "Mặt Trăng là thiên thể duy nhất quay quanh Trái Đất, được gọi bằng thuật ngữ khoa học nào?", "Vệ tinh tự nhiên của Trái Đất", ["Một ngôi sao nhỏ", "Một tiểu hành tinh", "Một sao chổi"], "Mặt Trăng không tự phát sáng mà phản chiếu ánh sáng Mặt Trời xuống Trái Đất vào ban đêm.", "6-7", 1),
    ("Pha trăng tròn (rằm)", "Vào ngày rằm (15 âm lịch) hàng tháng, ta thấy Mặt Trăng trên bầu trời có hình dạng tròn và sáng nhất vì sao?", "Vì toàn bộ nửa Mặt Trăng được chiếu sáng đang quay trực diện về Trái Đất", ["Vì Mặt Trăng bay gần Trái Đất hơn", "Vì Mặt Trăng tự bốc cháy", "Vì mây bay đi hết"], "Vị trí tương đối giữa Mặt Trời, Trái Đất và Mặt Trăng tạo nên các pha trăng: trăng non, trăng khuyết và trăng tròn.", "7-8", 2),
    ("Hiện tượng thủy triều", "Nước biển dâng lên rồi rút xuống theo chu kỳ mỗi ngày (thủy triều) chủ yếu do lực hút hấp dẫn của thiên thể nào?", "Lực hấp dẫn của Mặt Trăng (kết hợp với Mặt Trời)", ["Do cá voi bơi lội", "Do tàu bè chạy", "Do gió biển thổi mạnh"], "Lực hấp dẫn của Mặt Trăng kéo phồng khối nước đại dương về phía nó tạo nên hiện tượng triều lên và triều xuống.", "8-9", 3),
    ("Nhật thực ban ngày", "Hiện tượng Mặt Trăng đi vào giữa Mặt Trời và Trái Đất, che khuất một phần hoặc toàn bộ Mặt Trời giữa ban ngày gọi là gì?", "Nhật thực", ["Nguyệt thực", "Sao băng", "Cầu vồng"], "Khi nhật thực toàn phần xảy ra, bầu trời giữa ban ngày tối sầm như hoàng hôn và ta thấy vầng hào quang vương miện của Mặt Trời.", "8-9", 3),
    ("Nguyệt thực đêm rằm", "Hiện tượng Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng, bóng của Trái Đất che khuất Mặt Trăng tròn gọi là gì?", "Nguyệt thực (Trăng máu)", ["Nhật thực", "Sao chổi", "Cực quang"], "Ánh sáng đỏ bị khí quyển Trái Đất bẻ cong chiếu vào Mặt Trăng làm Mặt Trăng có màu đỏ đồng huyền ảo trong nguyệt thực toàn phần.", "8-9", 3),
    ("Sao băng trên trời", "Những vệt sáng xẹt qua bầu trời đêm mà dân gian hay gọi là 'sao băng' thực chất là hiện tượng gì?", "Các mẩu thiên thạch nhỏ bốc cháy ma sát khi bay vào khí quyển Trái Đất", ["Một ngôi sao bị rơi xuống đất", "Đèn pha của máy bay", "Pháo hoa của phi hành gia"], "Hầu hết các mẩu đá thiên thạch bốc cháy tan biến hoàn toàn ở tầng trung lưu, bảo vệ mặt đất an toàn.", "7-8", 2),
    ("Sao chổi có đuôi", "Thiên thể bằng băng đá và bụi bay quanh Mặt Trời theo quỹ đạo dài, khi đến gần Mặt Trời bốc hơi tạo thành chiếc đuôi sáng dài gọi là gì?", "Sao chổi", ["Sao băng", "Tiểu hành tinh", "Mặt Trăng"], "Đuôi sao chổi luôn hướng ra xa Mặt Trời do bị áp lực của gió mặt trời thổi bạt về phía sau.", "8-9", 3),
    ("Ngày và đêm", "Hiện tượng ngày và đêm luân phiên nhau trên Trái Đất sinh ra do nguyên nhân cốt lõi nào?", "Do Trái Đất tự quay quanh trục của nó từ Tây sang Đông", ["Do Mặt Trời quay quanh Trái Đất", "Do Mặt Trăng che chở", "Do gió thổi mây bay"], "Nửa Trái Đất hướng về Mặt Trời là ban ngày, nửa quay đi vào bóng tối là ban đêm, quay một vòng tròn mất 24 giờ.", "6-7", 1),
    ("Bốn mùa trong năm", "Hiện tượng bốn mùa Xuân - Hạ - Thu - Đông luân chuyển trên Trái Đất sinh ra do nguyên nhân nào?", "Do trục Trái Đất nghiêng và chuyển động quay quanh Mặt Trời", ["Do Trái Đất lúc gần lúc xa Mặt Trời", "Do Mặt Trời lúc sáng lúc tối", "Do thủy triều"], "Trục nghiêng 23,5 độ không đổi phương khi quay quanh Mặt Trời khiến hai bán cầu lần lượt nhận lượng nhiệt khác nhau trong năm.", "8-9", 3),
    ("Thời gian một năm", "Trái Đất chuyển động một vòng trọn vẹn quanh Mặt Trời mất khoảng thời gian là bao lâu?", "Khoảng 365 ngày và 6 giờ (365,25 ngày)", ["Đúng 100 ngày", "Đúng 24 giờ", "Khoảng 1.000 ngày"], "Chính vì số dư 6 giờ mỗi năm mà cứ sau 4 năm lại có một năm nhuận 366 ngày (tháng 2 có 29 ngày).", "7-8", 2),
    ("Phi hành gia đầu tiên", "Nhà du hành vũ trụ đầu tiên trong lịch sử nhân loại bay vào không gian quanh Trái Đất năm 1961 là ai?", "Yuri Gagarin (Liên Xô)", ["Neil Armstrong", "Phạm Tuân", "Albert Einstein"], "Câu nói bất hủ của Yuri Gagarin khi ngắm nhìn hành tinh chúng ta từ vũ trụ: 'Trái Đất có màu xanh biếc tuyệt đẹp!'.", "7-8", 2),
    ("Người đầu tiên lên Mặt Trăng", "Phi hành gia người Mỹ nào là người đầu tiên đặt bước chân lịch sử lên bề mặt Mặt Trăng vào năm 1969?", "Neil Armstrong", ["Yuri Gagarin", "Phạm Tuân", "Buzz Aldrin"], "Câu nói nổi tiếng: 'Đây là bước đi nhỏ bé của một con người, nhưng là bước tiến khổng lồ của nhân loại'.", "7-8", 2),
    ("Phi hành gia Việt Nam", "Anh hùng phi công nào là người Việt Nam và người châu Á đầu tiên bay vào vũ trụ năm 1980?", "Phạm Tuân", ["Nguyễn Văn Cừ", "Võ Nguyên Giáp", "Trần Đại Nghĩa"], "Trung tướng Phạm Tuân cùng nhà du hành Liên Xô Viktor Gorbatko đã thực hiện chuyến bay lịch sử trên tàu Soyuz 37.", "7-8", 2),
    ("Vũ trụ không có trọng lượng", "Trong khoang trạm vũ trụ không gian, các phi hành gia và đồ vật trôi lơ lửng bồng bềnh là do trạng thái gì?", "Trạng thái không trọng lượng (Vi trọng lực)", ["Do không có không khí", "Do gió thổi mạnh", "Do bị mất nhiệt độ"], "Trạm vũ trụ rơi tự do liên tục quanh Trái Đất tạo ra môi trường vi trọng lực khiến mọi thứ đều lơ lửng.", "8-9", 3),
    ("Kính thiên văn Hubble", "Chiếc kính viễn vọng không gian nổi tiếng bay trên quỹ đạo Trái Đất đã chụp được hàng triệu bức ảnh vũ trụ rực rỡ là kính gì?", "Kính viễn vọng Hubble", ["Kính lúp Galilê", "Kính hiển vi", "Kính thiên văn James Webb"], "Nhờ bay ngoài bầu khí quyển Trái Đất, kính Hubble chụp được những thiên hà xa xôi với độ nét kinh ngạc.", "8-9", 3),
    ("Dải Ngân Hà (Milky Way)", "Hệ Mặt Trời của chúng ta nằm trong một thiên hà xoắn ốc khổng lồ chứa hàng trăm tỷ ngôi sao có tên là gì?", "Dải Ngân Hà (Milky Way)", ["Thiên hà Tiên Nữ", "Đám mây Magellan", "Chòm sao Gấu Lớn"], "Vào những đêm hè trời quang, ta có thể thấy một dải sáng màu bạc vắt ngang bầu trời giống như một dòng sông bạc.", "7-8", 2),
    ("Tốc độ ánh sáng", "Tốc độ nhanh nhất trong vũ trụ là tốc độ ánh sáng, có thể đi được bao nhiêu km trong một giây?", "Khoảng 300.000 km/giây", ["Khoảng 1.000 km/giây", "Khoảng 100 km/giờ", "Khoảng 1 triệu km/giây"], "Với vận tốc ánh sáng, chỉ mất 8 phút 20 giây để một tia sáng đi từ Mặt Trời tới Trái Đất.", "8-9", 3),
    ("Trọng lực Mặt Trăng", "Trọng lực trên bề mặt Mặt Trăng yếu hơn Trái Đất bao nhiêu lần?", "Yếu hơn khoảng 6 lần (bằng 1/6 Trái Đất)", ["Bằng một nửa", "Mạnh gấp đôi", "Không có trọng lực"], "Một bạn nhỏ nặng 30 kg trên Trái Đất khi đứng trên Mặt Trăng cân nặng chỉ còn tương đương 5 kg, có thể nhảy rất cao.", "7-8", 2),
    ("Trái Đất hình gì", "Hình dạng thực tế của hành tinh Trái Đất là gì?", "Hình cầu hơi dẹt ở hai cực và phình ra ở xích đạo (Hình geoid)", ["Hình tròn phẳng như chiếc đĩa", "Hình vuông vức", "Hình tam giác"], "Do lực ly tâm khi tự quay quanh trục, vùng xích đạo phình nhẹ hơn so với hai cực Bắc và Nam.", "7-8", 2),
    ("Bắc Cực và Nam Cực", "Vùng cực nào của Trái Đất là một lục địa đất liền phủ lớp băng dày hàng ngàn mét và có loài chim cánh cụt sinh sống?", "Nam Cực (Châu Nam Cực)", ["Bắc Cực", "Vùng Xích đạo", "Sa mạc Sahara"], "Nam Cực là nơi lạnh nhất, khô nhất và nhiều gió nhất hành tinh, còn Bắc Cực là một đại dương băng trôi.", "8-9", 3),
    ("Đường Xích đạo", "Đường ranh giới tưởng tượng chia Trái Đất thành hai nửa Bán cầu Bắc và Bán cầu Nam có vĩ độ 0 độ gọi là gì?", "Đường Xích đạo", ["Đường Kinh tuyến gốc", "Đường Chí tuyến Bắc", "Vòng Cực Nam"], "Vùng khí hậu quanh đường xích đạo nhận được nhiều ánh nắng quanh năm nhất nên luôn ấm áp nóng ẩm.", "7-8", 2),
    ("Khí quyển Trái Đất", "Lớp vỏ khí bao bọc xung quanh Trái Đất bảo vệ chúng ta khỏi bức xạ độc hại và thiên thạch gọi là gì?", "Bầu khí quyển", ["Lớp Thủy quyển", "Lớp Thạch quyển", "Lõi Trái Đất"], "Khí quyển gồm các tầng: Đối lưu, Bình lưu, Trung lưu, Nhiệt lưu và Ngoại lưu bảo bọc sự sống mỏng manh.", "7-8", 2),
    ("Tầng Ozone bảo vệ", "Tầng khí quý giá trong tầng bình lưu có nhiệm vụ như một chiếc 'kính râm khổng lồ' lọc các tia cực tím (UV) nguy hiểm là tầng gì?", "Tầng Ozone (O3)", ["Tầng khói bụi", "Tầng mây mưa", "Tầng oxy lỏng"], "Bảo vệ tầng ozone bằng cách không sử dụng các chất khí CFC phá hủy tầng khí quyển che chở Trái Đất.", "8-9", 3),
    ("Vệ tinh nhân tạo", "Những cỗ máy do con người chế tạo phóng lên bay quanh Trái Đất giúp phát sóng truyền hình, định vị GPS và dự báo thời tiết gọi là gì?", "Vệ tinh nhân tạo", ["Mặt Trăng giả", "Tên lửa đẩy", "Khinh khí cầu"], "Vệ tinh viễn thông Vinasat-1 là vệ tinh viễn thông đầu tiên của Việt Nam được phóng lên không gian năm 2008.", "7-8", 2),
    ("Kinh tuyến gốc Greenwich", "Đường kinh tuyến 0 độ đi qua đài thiên văn hoàng gia nào ở thủ đô Luân Đôn (nước Anh) được quy ước làm gốc thời gian thế giới (GMT)?", "Đài thiên văn Greenwich", ["Đài thiên văn Paris", "Đài thiên văn Tokyo", "Đài thiên văn New York"], "Việt Nam nằm ở múi giờ GMT+7, nghĩa là sớm hơn giờ chuẩn Greenwich 7 tiếng đồng hồ.", "8-9", 3),
    ("Hành tinh lùn Sao Diêm Vương", "Sao Diêm Vương (Pluto) trước đây từng được coi là hành tinh thứ 9, hiện nay được xếp vào nhóm thiên thể nào?", "Hành tinh lùn (Dwarf planet)", ["Ngôi sao lớn", "Vệ tinh của Trái Đất", "Sao băng"], "Năm 2006, Hiệp hội Thiên văn Quốc tế định nghĩa lại hành tinh và xếp Pluto thành hành tinh lùn do chưa dọn sạch quỹ đạo.", "8-9", 3),

    # 36-70 Thời tiết & Các hiện tượng tự nhiên
    ("Mây hình thành từ đâu", "Những đám mây trắng bồng bềnh trên bầu trời thực chất được cấu tạo từ những hạt gì?", "Vô số giọt nước nhỏ li ti và tinh thể băng ngưng tụ", ["Bông gòn khổng lồ", "Khói bốc lên từ bếp", "Bọt xà phòng"], "Hơi nước bốc lên từ sông hồ biển gặp không khí lạnh trên cao sẽ ngưng tụ thành các giọt nước li ti tạo thành mây.", "6-7", 1),
    ("Hiện tượng mưa rơi", "Khi các giọt nước trong đám mây kết hợp lại với nhau ngày càng to và nặng, không khí không đỡ nổi nữa sẽ xảy ra hiện tượng gì?", "Trời đổ mưa", ["Tuyết rơi mùa hè", "Gió ngừng thổi", "Trời nổi nắng to"], "Nước mưa rơi xuống đất ngấm vào mạch nước ngầm và chảy ra sông ngòi rồi lại bốc hơi, khép kín vòng tuần hoàn của nước.", "6-7", 1),
    ("Gió sinh ra do đâu", "Hiện tượng gió thổi lá cây xào xạc thực chất là sự chuyển động của luồng không khí từ nơi nào đến nơi nào?", "Từ nơi có áp suất cao (nơi lạnh) đến nơi áp suất thấp (nơi nóng)", ["Do Trái Đất vẫy tay", "Do Mặt Trời thổi hơi", "Do sóng biển xô bờ"], "Không khí nóng nhẹ bốc lên cao, không khí lạnh xung quanh tràn vào thay thế tạo thành luồng gió chuyển động.", "7-8", 2),
    ("Sấm và chớp", "Trong cơn giông bão, tại sao chúng ta luôn nhìn thấy tia chớp lóe sáng trước rồi một lúc sau mới nghe thấy tiếng sấm rền vang?", "Vì vận tốc ánh sáng nhanh hơn rất nhiều so với vận tốc âm thanh", ["Vì sấm ở xa hơn chớp", "Vì mắt nhìn nhanh hơn tai nghe", "Vì chớp xảy ra trước sấm 10 phút"], "Ánh sáng truyền đi với tốc độ 300.000 km/s (nhìn thấy ngay lập tức), còn âm thanh chỉ truyền trong không khí khoảng 340 m/s.", "7-8", 2),
    ("Cầu vồng bảy sắc", "Sau cơn mưa rào mùa hè khi trời hửng nắng, hiện tượng cầu vồng rực rỡ xuất hiện là do đâu?", "Do ánh sáng mặt trời bị khúc xạ và tán sắc qua các giọt nước mưa lơ lửng", ["Do có ai vẽ sơn lên trời", "Do cầu vồng bay từ biển vào", "Do khói xe ô tô tạo thành"], "Ánh sáng trắng của Mặt Trời bị tán sắc thành 7 màu cơ bản: Đỏ, Cam, Vàng, Lục, Lam, Chàm, Tím.", "6-7", 1),
    ("Tránh sét đánh an toàn", "Khi đang đi ngoài đồng hoặc trên đường gặp trời giông bão sấm sét, hành động nào sau đây là NGUY HIỂM TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM?", "Chạy vào trú mưa dưới gốc cây to cao đứng đơn độc giữa bãi đất trống", ["Tìm nhà kiên cố vào trú", "Ngồi xổm co cụm người lại nơi thấp", "Không cầm các vật kim loại dài như que sắt ô kim loại"], "Cây to cô đơn là cột thu lôi tự nhiên rất dễ bị sét đánh trúng, truyền điện qua đất gây nguy hiểm đến tính mạng.", "7-8", 2),
    ("Sương mù buổi sáng", "Lớp sương mù bảng lảng che mờ tầm nhìn trên đường vào những buổi sớm mùa đông hình thành do đâu?", "Hơi nước sát mặt đất gặp lạnh ngưng tụ thành hạt nước nhỏ li ti lơ lửng", ["Do khói bụi nhà máy", "Do đất bốc cháy ngầm", "Do mây bị rơi xuống đất"], "Khi Mặt Trời lên cao sưởi ấm không khí, các hạt sương mù bốc hơi tan biến và bầu trời trở lại trong xanh.", "7-8", 2),
    ("Mưa rào mùa hạ", "Cơn mưa rào mùa hè thường có đặc điểm nào sau đây?", "Mưa to xối xả bất chợt, hạt mưa lớn rồi tạnh nhanh", ["Mưa phùn rả rích cả tháng trời", "Mưa rơi kèm tuyết phủ", "Mưa không làm ướt đất"], "Mưa rào đem lại làn gió mát rượi giải tỏa cơn nắng gắt oi ả của buổi trưa hè nhiệt đới.", "6-7", 1),
    ("Mưa phùn mùa xuân", "Tiết trời mưa phùn bay lất phất kèm gió se lạnh ở miền Bắc nước ta là đặc trưng của mùa nào?", "Mùa xuân đầu năm", ["Mùa hè chói chang", "Mùa thu lá vàng", "Mùa đông buốt giá"], "Mưa xuân lất phất tưới ẩm cho chồi non lộc biếc đâm chồi, cây cối vươn mình xanh tốt.", "6-7", 1),
    ("Mưa đá bất thường", "Hiện tượng mưa đá là do những cục băng đá rơi từ đám mây nào xuống đất?", "Đám mây giông vũ tích khổng lồ có luồng không khí nâng cực mạnh", ["Đám mây trắng mỏng", "Mây sương mai", "Không cần có mây"], "Các hạt nước bị luồng gió đẩy lên tầng mây lạnh đóng băng nhiều lần lớn dần đến khi quá nặng rơi xuống.", "8-9", 3),
    ("Bão nhiệt đới", "Cơn bão nhiệt đới hình thành trên các vùng biển ấm có đặc điểm nguy hiểm nào?", "Gió giật cực mạnh, mưa lớn xối xả và sóng biển dâng cao", ["Trời lặng gió ấm áp", "Không có giọt mưa nào", "Nước biển rút cạn khô"], "Việt Nam hàng năm phải hứng chịu nhiều cơn bão từ Biển Đông đổ bộ vào miền Trung và miền Bắc.", "7-8", 2),
    ("Mắt bão lặng gió", "Khu vực tâm của một cơn bão nhiệt đới (gọi là mắt bão) có thời tiết kỳ lạ như thế nào?", "Trời quang mây tạnh, gió lặng ngắt một cách bất ngờ", ["Nơi gió thổi mạnh nhất cơn bão", "Nơi sấm sét đánh dữ dội nhất", "Nơi tuyết rơi dày"], "Xung quanh thành mắt bão là nơi cuồng phong dữ dội nhất, nhưng ngay chính giữa mắt bão lại hoàn toàn yên ả.", "8-9", 3),
    ("Lốc xoáy (Vòi rồng)", "Hiện tượng cột không khí xoáy tròn dữ dội hình chiếc phễu nối từ đám mây giông xuống mặt đất gọi là gì?", "Lốc xoáy (Vòi rồng / Tornado)", ["Gió heo may", "Gió mùa Đông Bắc", "Gió phơn Tây Nam"], "Lốc xoáy có sức hút cực lớn, có thể cuốn phăng cả ô tô, mái nhà và cây cối lên không trung.", "7-8", 2),
    ("Tuyết rơi giá lạnh", "Hiện tượng tuyết rơi trắng xóa xảy ra khi nhiệt độ không khí trên cao và mặt đất giảm xuống mức nào?", "Dưới 0 độ C (nhiệt độ đóng băng của nước)", ["Khoảng 25 độ C mát mẻ", "Khoảng 40 độ C nắng gắt", "Khoảng 100 độ C sôi"], "Tại Việt Nam, vào những đợt rét đậm mùa đông, tuyết thỉnh thoảng xuất hiện trên đỉnh Fansipan (Sa Pa) và Mẫu Sơn.", "7-8", 2),
    ("Băng giá và sương muối", "Vào những đêm đông trời rét buốt ở miền núi cao, hơi nước trên cỏ cây đóng thành lớp vảy băng trắng gọi là gì?", "Sương muối (Băng giá)", ["Mưa axit", "Bụi vàng", "Sương ngọt"], "Sương muối làm cháy lá cây trồng và gây hại cho gia súc nếu không được che chắn ấm áp.", "7-8", 2),
    ("Hạn hán kéo dài", "Hiện tượng thiên tai nhiều tháng liền không có một giọt mưa, đồng ruộng nứt nẻ, sông hồ cạn đáy gọi là gì?", "Hạn hán", ["Lũ lụt", "Động đất", "Triều cường"], "Hạn hán gây thiếu nước sinh hoạt và làm mùa màng mất trắng, cần sử dụng nước tiết kiệm.", "6-7", 1),
    ("Lũ lụt dâng cao", "Hiện tượng mưa lớn nhiều ngày khiến nước sông dâng tràn bờ ngập chìm làng mạc nhà cửa gọi là gì?", "Lũ lụt (Ngập úng)", ["Hạn hán", "Núi lửa phun", "Khô hạn"], "Trồng rừng đầu nguồn là biện pháp quan trọng hàng đầu giúp chặn dòng nước lũ cuồn cuộn.", "6-7", 1),
    ("Lũ quét ở miền núi", "Dòng nước lũ từ trên núi cao ập xuống thung lũng với tốc độ khủng khiếp kèm theo bùn đất đá gọi là gì?", "Lũ quét và sạt lở đất", ["Thủy triều đỏ", "Mưa phùn", "Gió lốc"], "Phá rừng đầu nguồn làm mất lớp thảm phủ thực vật khiến nguy cơ lũ quét tăng vọt vào mùa mưa bão.", "7-8", 2),
    ("Triều cường ở đô thị", "Hiện tượng nước biển và sông dâng cao theo kỳ trăng tràn vào gây ngập lụt đường phố TP Hồ Chí Minh gọi là gì?", "Triều cường", ["Mưa đá", "Sóng thần", "Sạt lở đồi"], "Triều cường thường đạt đỉnh vào các ngày đầu tháng và giữa tháng âm lịch kết hợp gió chướng.", "7-8", 2),
    ("Sóng thần khổng lồ", "Những con sóng biển cao hàng chục mét ập vào bờ với sức tàn phá khủng khiếp chủ yếu sinh ra do nguyên nhân nào?", "Động đất hoặc núi lửa phun trào mạnh dưới đáy đại dương", ["Do gió mùa thổi mạnh", "Do cá voi khổng lồ quẫy đuôi", "Do tàu thủy chạy nhanh"], "Sóng thần (Tsunami) di chuyển trên biển sâu với vận tốc như máy bay phản lực (hơn 800 km/h).", "8-9", 3),
    ("Núi lửa phun trào", "Chất lỏng nóng đỏ rực hàng ngàn độ C trào ra từ miệng núi lửa khi phun trào gọi là gì?", "Dung nham (Lava)", ["Nước sôi", "Dầu thô", "Bùn lầy"], "Mắc-ma nóng chảy từ sâu trong lòng đất khi thoát ra khỏi miệng núi lửa trên mặt đất được gọi là dung nham.", "7-8", 2),
    ("Động đất rung chuyển", "Hiện tượng mặt đất rung chuyển đột ngột do sự giải phóng năng lượng tích tụ ở các mảng kiến tạo vỏ Trái Đất gọi là gì?", "Động đất (Địa chấn)", ["Bão cát", "Lốc xoáy", "Hạn hán"], "Độ mạnh của một trận động đất được đo lường bằng thang độ Richter.", "8-9", 3),
    ("Hiệu ứng nhà kính", "Hiện tượng khí CO2 và các khí thải giữ nhiệt trong bầu khí quyển làm Trái Đất nóng lên gọi là gì?", "Hiệu ứng nhà kính (Greenhouse effect)", ["Hiện tượng cầu vồng", "Hiện tượng quang hợp", "Hiện tượng thủy triều"], "Hiệu ứng nhà kính gia tăng làm tan băng hai cực, mực nước biển dâng cao đe dọa các vùng ven biển.", "8-9", 3),
    ("Biến đổi khí hậu toàn cầu", "Để góp phần bảo vệ hành tinh và chống biến đổi khí hậu, mỗi bạn nhỏ chúng ta nên làm gì?", "Tắt điện khi ra khỏi phòng, trồng cây xanh và không xả rác bừa bãi", ["Chặt phá cây xanh", "Bật quạt và điều hòa cả ngày khi vắng nhà", "Đốt nhiều rác nhựa"], "Tiết kiệm năng lượng và sống xanh mỗi ngày là hành động thiết thực bảo vệ ngôi nhà chung Trái Đất.", "6-7", 1),
    ("Nhiệt kế đo thời tiết", "Dụng cụ dùng để đo nhiệt độ không khí nóng hay lạnh trong ngày gọi là gì?", "Nhiệt kế", ["Áp kế", "Ẩm kế", "Phong kế"], "Nhiệt kế chứa thủy ngân hoặc cồn nhuộm màu đỏ co giãn theo nhiệt độ môi trường xung quanh.", "6-7", 1),
    ("Ẩm kế đo độ ẩm", "Dụng cụ trong trạm khí tượng dùng để đo lượng hơi nước có trong không khí gọi là gì?", "Ẩm kế", ["Nhiệt kế", "Vũ kế", "Địa chấn kế"], "Khi độ ẩm không khí lên cao trên 90%, chúng ta cảm thấy oi bức mồ hôi khó bốc hơi hoặc trời sắp mưa.", "8-9", 3),
    ("Vũ kế đo lượng mưa", "Dụng cụ hình ống trụ dùng để hứng và đo lượng nước mưa rơi xuống một khu vực tính bằng milimét (mm) gọi là gì?", "Vũ kế (Máy đo lượng mưa)", ["Nhiệt kế", "Áp kế", "Tốc độ kế"], "Dự báo thời tiết thông báo lượng mưa 50mm nghĩa là nước mưa dâng cao 50mm trên một bề mặt phẳng bằng phẳng.", "7-8", 2),
    ("La bàn tìm hướng", "Kim nam châm của chiếc la bàn luôn chỉ về hướng địa lý nào trên Trái Đất?", "Hướng Bắc (và hướng Nam)", ["Hướng Đông", "Hướng Tây", "Hướng Mặt Trời mọc"], "Kim la bàn từ tính luôn định hướng theo các đường sức từ trường của Trái Đất.", "6-7", 1),
    ("Gió mùa Đông Bắc", "Loại gió mùa thổi từ phương bắc tràn về nước ta vào mùa đông mang theo không khí lạnh khô và rét buốt là gì?", "Gió mùa Đông Bắc", ["Gió mùa Tây Nam", "Gió Tín phong", "Gió đất"], "Gió mùa Đông Bắc gắn liền với những đợt rét ngọt, áo len ấm và ngày Tết Nguyên Đán ở miền Bắc.", "7-8", 2),
    ("Gió mùa Tây Nam", "Loại gió mùa thổi từ biển Ấn Độ Dương vào nước ta từ tháng 5 đến tháng 10 mang theo nhiều hơi ẩm gây mưa cho vùng nào?", "Gây mưa cho Tây Nguyên và Nam Bộ", ["Gây khô hạn miền Bắc", "Làm đóng băng sông ngòi", "Làm mất hết mây"], "Gió mùa Tây Nam tạo nên mùa mưa đặc trưng ở miền Nam với những cơn mưa rào sảng khoái buổi chiều.", "7-8", 2),
    ("Gió phơn Tây Nam (Gió Lào)", "Gió vượt qua dãy Trường Sơn vào mùa hè tràn xuống đồng bằng ven biển miền Trung trở nên khô khốc và nóng rát gọi là gió gì?", "Gió Lào (Gió phơn)", ["Gió bấc", "Gió nồm", "Gió sương"], "Gió trút hết mưa ở sườn tây (Lào), khi vượt sang sườn đông (Việt Nam) bị nén nhiệt trở nên cực kỳ khô nóng.", "8-9", 3),
    ("Thời tiết nồm ẩm", "Vào cuối mùa xuân ở miền Bắc, hiện tượng hơi nước ngưng tụ đọng ướt sũng sàn nhà và tường gạch gọi là gì?", "Hiện tượng trời nồm (Nồm ẩm)", ["Hiện tượng khô hanh", "Hiện tượng hạn hán", "Hiện tượng bão cát"], "Trời nồm xảy ra khi không khí ẩm thổi từ biển vào gặp sàn nhà còn lạnh chưa kịp ấm lên.", "7-8", 2),
    ("Mùa khô ở phương Nam", "Khí hậu miền Nam nước ta không có 4 mùa rõ rệt như miền Bắc mà chỉ có 2 mùa là mùa nào?", "Mùa Mưa và mùa Khô", ["Mùa Xuân và mùa Thu", "Mùa Đông lạnh và mùa Hè", "Mùa Bão và mùa Tuyết"], "Mùa khô ở miền Nam từ tháng 11 đến tháng 4 năm sau với bầu trời trong xanh đầy nắng ấm chan hòa.", "6-7", 1),
    ("Dự báo thời tiết", "Bản tin dự báo thời tiết trên tivi hàng ngày giúp ích gì cho gia đình và người dân?", "Chủ động chuẩn bị áo mưa, mũ nón và kế hoạch công việc nông nghiệp, tàu thuyền", ["Để xem tivi cho vui mắt", "Không có tác dụng gì", "Để biết ngày sinh nhật"], "Theo dõi dự báo thời tiết giúp bà con ngư dân tránh bão trên biển và học sinh chủ động mặc ấm mùa đông.", "6-7", 1),
    ("Bảo vệ hành tinh xanh", "Thông điệp của sự kiện 'Giờ Trái Đất' được tổ chức vào tối thứ Bảy cuối cùng của tháng Ba hàng năm là gì?", "Tắt các bóng đèn và thiết bị điện không cần thiết trong 60 phút để tiết kiệm năng lượng", ["Bật sáng tất cả các đèn trong nhà", "Tổ chức bắn pháo hoa", "Ngủ cả ngày"], "Giờ Trái Đất nhắc nhở mọi người ý thức tiết kiệm điện năng và giảm phát thải khí nhà kính bảo vệ tương lai.", "7-8", 2)
]

# Thêm 65 MC items nữa để tròn 135 MC
more_mc_vt = [
    ("Ánh sáng Mặt Trời đến Trái Đất", "Tia nắng từ Mặt Trời mất khoảng thời gian bao lâu để vượt qua 150 triệu km tới Trái Đất?", "Khoảng 8 phút 20 giây", ["Khoảng 1 giây", "Khoảng 24 giờ", "Khoảng 1 năm"], "Dù ánh sáng bay cực nhanh (300.000 km/s), khoảng cách bao la giữa Trái Đất và Mặt Trời vẫn cần hơn 8 phút.", "8-9", 3),
    ("Sao Bắc Cực dẫn đường", "Ngôi sao sáng luôn nằm cố định gần trục quay ở phương Bắc giúp các thủy thủ định hướng ban đêm là sao gì?", "Sao Bắc Cực (Polaris)", ["Sao Kim", "Sao Hỏa", "Sao Chổi Halley"], "Ở Bán cầu Bắc, nhìn thấy Sao Bắc Cực là ta biết chính xác đó là hướng Bắc địa lý.", "7-8", 2),
    ("Chòm sao Đại Hùng (Gấu Lớn)", "Chòm sao có 7 ngôi sao sáng xếp thành hình chiếc muỗng (cái gàu múc nước) khổng lồ trên bầu trời là gì?", "Chòm sao Bắc Đẩu (Gấu Lớn)", ["Chòm sao Bọ Cạp", "Chòm sao Thợ Săn", "Chòm sao Sư Tử"], "Hai ngôi sao ở đáy chiếc gàu chỉ thẳng tới vị trí của Sao Bắc Cực.", "7-8", 2),
    ("Chòm sao Lạp Hộ (Thợ Săn)", "Chòm sao nổi bật trên bầu trời mùa đông có 3 ngôi sao sáng thẳng hàng tạo thành thắt lưng là gì?", "Chòm sao Lạp Hộ (Orion)", ["Chòm sao Song Nam", "Chòm sao Kim Ngưu", "Chòm sao Thiên Nga"], "Chòm sao Orion mang hình dáng một dũng sĩ thợ săn giương cung giữa các vì sao lấp lánh.", "8-9", 3),
    ("Năm nhuận có bao nhiêu ngày", "Năm nhuận dương lịch (cứ 4 năm có một lần, tháng Hai có 29 ngày) có tổng cộng bao nhiêu ngày?", "366 ngày", ["365 ngày", "360 ngày", "370 ngày"], "Thêm 1 ngày vào năm nhuận để bù cho số dư 0,25 ngày mỗi vòng quay quanh Mặt Trời của Trái Đất.", "6-7", 1),
    ("Vành đai tiểu hành tinh", "Vành đai chứa hàng triệu tảng đá tiểu hành tinh trong Hệ Mặt Trời nằm ở giữa hai hành tinh nào?", "Giữa Sao Hỏa và Sao Mộc", ["Giữa Trái Đất và Sao Kim", "Giữa Sao Thổ và Sao Thiên Vương", "Giữa Mặt Trời và Sao Thủy"], "Vành đai tiểu hành tinh là ranh giới phân chia các hành tinh đất đá bên trong và các hành tinh khí bên ngoài.", "8-9", 3),
    ("Núi lửa cao nhất Hệ Mặt Trời", "Ngọn núi lửa khổng lồ Olympus Mons cao gấp 3 lần đỉnh Everest nằm trên hành tinh nào?", "Sao Hỏa", ["Mặt Trăng", "Sao Kim", "Sao Thủy"], "Olympus Mons cao tới 22 km so với bề mặt xung quanh, là ngọn núi lửa lớn nhất từng được ghi nhận trong Hệ Mặt Trời.", "8-9", 3),
    ("Mặt Trăng Titan của Sao Thổ", "Mặt trăng Titan của Sao Thổ là vệ tinh duy nhất trong Hệ Mặt Trời có đặc điểm kỳ thú nào?", "Có bầu khí quyển dày đặc và các biển hồ chứa đầy metan lỏng", ["Có người ngoài hành tinh sinh sống", "Tự phát sáng như mặt trời", "Làm hoàn toàn bằng vàng"], "Titan có mây, mưa và các con sông chảy bằng chất lỏng hydrocarbon thay vì nước như Trái Đất.", "8-9", 3),
    ("Mặt Trăng Europa của Sao Mộc", "Vệ tinh Europa của Sao Mộc được các nhà khoa học săn đón tìm kiếm sự sống vì dưới lớp vỏ băng của nó có gì?", "Một đại dương nước lỏng khổng lồ", ["Một mỏ dầu thô", "Một khu rừng rậm", "Toàn là kim cương"], "Lực hấp dẫn kéo đẩy của Sao Mộc sinh nhiệt làm ấm và duy trì đại dương nước lỏng dưới lớp băng dày.", "8-9", 3),
    ("Cực quang huyền ảo", "Những dải sáng màu xanh lục, hồng tím uốn lượn kỳ ảo trên bầu trời đêm vùng cực gọi là hiện tượng gì?", "Cực quang (Bắc cực quang và Nam cực quang)", ["Cầu vồng đêm", "Sao băng rơi", "Bão Mặt Trời"], "Cực quang sinh ra khi các hạt mang điện từ gió mặt trời va chạm với các phân tử khí quyển ở hai cực Trái Đất.", "8-9", 3),
    ("Gió Mặt Trời", "Dòng các hạt mang điện năng lượng cao liên tục phóng ra từ khí quyển ngoài của Mặt Trời gọi là gì?", "Gió Mặt Trời (Solar wind)", ["Gió bão Trái Đất", "Gió mùa", "Gió lốc"], "Từ trường Trái Đất hoạt động như một tấm khiên vô hình làm lệch hướng gió mặt trời bảo vệ sự sống.", "8-9", 3),
    ("Hố đen vũ trụ (Lỗ đen)", "Thiên thể kỳ bí trong vũ trụ có lực hấp dẫn khủng khiếp đến mức ngay cả ánh sáng cũng không thể thoát ra ngoài là gì?", "Hố đen (Lỗ đen / Black hole)", ["Hố sâu đại dương", "Ngôi sao chết", "Hành tinh khí"], "Hố đen uốn cong không gian và thời gian xung quanh nó, hình thành khi một ngôi sao khổng lồ suy sụp vào cuối đời.", "8-9", 3),
    ("Năm ánh sáng là gì", "Năm ánh sáng (Light-year) trong thiên văn học là đơn vị dùng để đo đại lượng nào?", "Đo khoảng cách (quãng đường ánh sáng đi trong 1 năm)", ["Đo thời gian một năm", "Đo độ sáng của đèn", "Đo nhiệt độ của sao"], "Một năm ánh sáng tương đương khoảng 9.460 tỷ kilômét, dùng để đo khoảng cách giữa các vì sao bao la.", "8-9", 3),
    ("Sao chổi Halley", "Ngôi sao chổi nổi tiếng nhất lịch sử cứ khoảng 75 - 76 năm lại bay qua Trái Đất một lần có tên là gì?", "Sao chổi Halley", ["Sao chổi Encke", "Sao chổi Hale-Bopp", "Sao chổi Swift-Tuttle"], "Lần gần nhất sao chổi Halley xuất hiện là năm 1986, và dự kiến sẽ quay lại bầu trời Trái Đất vào năm 2061.", "8-9", 3),
    ("Hố va chạm trên Mặt Trăng", "Bề mặt Mặt Trăng có vô số hố lõm hình tròn (Crater) kích thước lớn nhỏ là do nguyên nhân gì?", "Do các thiên thạch va chạm vào bề mặt suốt hàng tỷ năm", ["Do núi lửa phun trào", "Do con người đào hố", "Do nước xói mòn"], "Vì Mặt Trăng không có bầu khí quyển để thiêu cháy thiên thạch và không có gió mưa xói mòn nên các hố tồn tại nguyên vẹn.", "7-8", 2),
    ("Bầu trời ban ngày màu xanh", "Tại sao bầu trời vào những ngày nắng đẹp lại có màu xanh lam trong vắt?", "Do ánh sáng xanh có bước sóng ngắn bị các phân tử khí quyển tán xạ mạnh nhất (Tán xạ Rayleigh)", ["Do phản chiếu màu nước biển", "Do không khí màu xanh", "Do mây màu xanh"], "Khi Mặt Trời lặn xuống thấp ở chân trời, ánh sáng đỏ cam ít bị tán xạ xuyên qua khí quyển tạo nên màu hoàng hôn đỏ rực.", "8-9", 3),
    ("Áp suất khí quyển", "Không khí vô hình xung quanh chúng ta ép lên mọi vật một áp lực được gọi là gì?", "Áp suất khí quyển", ["Trọng lực", "Lực ma sát", "Lực đàn hồi"], "Càng lên cao trên đỉnh núi, không khí càng loãng và áp suất khí quyển càng giảm khiến nước sôi ở nhiệt độ thấp hơn.", "8-9", 3),
    ("Nước sôi ở nhiệt độ nào", "Ở điều kiện áp suất tiêu chuẩn trên mặt nước biển, nước tinh khiết sôi và bốc hơi mãnh liệt ở bao nhiêu độ C?", "100 độ C", ["0 độ C", "50 độ C", "200 độ C"], "Nhiệt kế thủy ngân đo nhiệt độ sôi của nước làm mốc 100 độ C trong thang nhiệt độ Celsius.", "6-7", 1),
    ("Nước đóng băng ở nhiệt độ nào", "Nước lỏng chuyển thành thể rắn (đá viên) ở nhiệt độ bao nhiêu độ C?", "0 độ C", ["100 độ C", "10 độ C", "-50 độ C"], "Mốc 0 độ C là nhiệt độ đông đặc của nước tinh khiết thành băng đá.", "6-7", 1),
    ("Chu trình của nước", "Ba quá trình chính tạo nên vòng tuần hoàn bất tận của nước trong tự nhiên là gì?", "Bốc hơi -> Ngưng tụ -> Mưa rơi", ["Đông đá -> Nấu sôi -> Đổ ra biển", "Uống nước -> Rửa tay -> Quét nhà", "Tưới cây -> Ra hoa -> Kết quả"], "Nước trên Trái Đất không bao giờ tự mất đi mà liên tục luân chuyển qua các thể khí, lỏng, rắn.", "6-7", 1),
    ("Gió bấc mùa đông", "Ở miền Bắc, người dân thường gọi gió mùa Đông Bắc lạnh buốt bằng tên dân dã thân thương là gì?", "Gió bấc", ["Gió nồm", "Gió nam", "Gió tây"], "Mỗi đợt gió bấc tràn về là các bạn nhỏ lại được mẹ mặc áo khoác bông và quàng khăn ấm áp đến trường.", "6-7", 1),
    ("Gió nồm mùa xuân hè", "Loại gió mang hơi ẩm từ biển Đông thổi vào miền Bắc vào cuối xuân đầu hè mang theo gió mát mẻ gọi là gì?", "Gió nồm (Gió đông nam)", ["Gió bấc", "Gió Lào", "Gió chướng"], "Gió nồm mát rượi thổi qua các lũy tre xua tan oi ả trong những buổi trưa hè thanh bình thôn quê.", "7-8", 2),
    ("Gió chướng miền Tây", "Gió mùa Đông Bắc khi thổi xuống vùng đồng bằng sông Cửu Long vào cuối năm được bà con gọi là gió gì?", "Gió chướng", ["Gió bấc", "Gió phơn", "Gió lốc"], "Mùa gió chướng về cũng là mùa nước lũ rút trên các cánh đồng miền Tây và mùa hoa màu Tết bắt đầu.", "7-8", 2),
    ("Cây ATM không khí sạch", "Cây xanh đô thị và rừng tự nhiên có thể làm giảm bao nhiêu nhiệt độ không khí xung quanh nhờ bóng râm và thoát hơi nước?", "Giảm từ 2 đến 8 độ C", ["Giảm 50 độ C đóng băng", "Không giảm độ nào", "Làm trời nóng thêm"], "Đi dưới hàng cây rợp bóng mát ta luôn cảm thấy dễ chịu hơn rất nhiều so với đi trên đường nhựa nắng chang chang.", "7-8", 2),
    ("Đo độ gió Beaufort", "Thang đo cấp gió dùng trong dự báo bão và thời tiết có tên gọi quốc tế là thang đo gì?", "Thang sức gió Beaufort", ["Thang đo Richter", "Thang đo Celsius", "Thang đo Newton"], "Thang Beaufort chia cấp gió từ cấp 0 (trời lặng gió) đến cấp 12 (gió bão cuồng phong cực mạnh trên 118 km/h).", "8-9", 3),
    ("Mưa axit nguy hại", "Mưa axit sinh ra do khí thải ô nhiễm từ các nhà máy nhiệt điện và xe cộ chủ yếu chứa các khí nào?", "Khí lưu huỳnh đioxit (SO2) và nitơ oxit (NOx)", ["Khí oxy nguyên chất", "Khí heli nhẹ", "Hơi nước tinh khiết"], "Mưa axit làm chua đất nông nghiệp, rụng lá rừng cây và ăn mòn các tượng đài đá lịch sử.", "8-9", 3),
    ("Rừng chắn gió bão ven biển", "Hàng cây phi lao (dương) trồng bạt ngàn dọc bờ cát biển miền Trung có tác dụng tuyệt vời nào?", "Chắn gió bão biển và ngăn nạn cát bay vùi lấp ruộng đồng", ["Lấy bóng mát câu cá", "Thu hút cá mập", "Làm củi khô"], "Rừng phòng hộ phi lao kiên cường cản gió mặn của bão biển, bảo vệ xóm làng bình yên bên bờ cát.", "7-8", 2),
    ("Bão cát sa mạc", "Hiện tượng những cơn gió lốc dữ dội cuốn tung hàng triệu tấn bụi cát mù mịt trên sa mạc gọi là gì?", "Bão cát (Haboob)", ["Bão tuyết", "Lũ quét", "Sương mù"], "Khi gặp bão cát sa mạc, lạc đà có thể tự khép kín lỗ mũi và có hai hàng mi dày ngăn cát bay vào mắt.", "7-8", 2),
    ("Thời tiết cực đoan El Nino", "Hiện tượng lớp nước biển bề mặt ở vùng xích đạo Thái Bình Dương nóng lên bất thường gây khô hạn nắng nóng kỷ lục gọi là gì?", "Hiện tượng El Niño", ["Hiện tượng La Niña", "Hiện tượng nhật thực", "Hiện tượng trăng tròn"], "El Niño thường gây ra hạn hán khốc liệt và mùa hè nắng nóng gay gắt kéo dài tại Việt Nam.", "8-9", 3),
    ("Thời tiết cực đoan La Nina", "Hiện tượng nước biển vùng xích đạo lạnh đi bất thường, gây mưa bão dồn dập và lũ lụt nhiều hơn bình thường gọi là gì?", "Hiện tượng La Niña", ["Hiện tượng El Niño", "Hiệu ứng nhà kính", "Sóng thần"], "La Niña thường đi kèm với những mùa đông rét đậm rét hại và số lượng cơn bão nhiệt đới tăng cao.", "8-9", 3),
    ("Đường chân trời", "Đường ranh giới tưởng tượng xa tít tắp nơi mặt đất (hoặc mặt biển) dường như tiếp giáp với bầu trời gọi là gì?", "Đường chân trời (Đường chân mây)", ["Đường kinh tuyến", "Đường ranh giới", "Đường xích đạo"], "Khi nhìn một con tàu từ xa tiến vào bờ biển, ta thấy cánh buồm nhô lên trước rồi mới thấy thân tàu do mặt biển cong.", "7-8", 2),
    ("Sao Mai và Sao Hôm", "Ngôi sao sáng lấp lánh xuất hiện lúc rạng đông (Sao Mai) và chập tối (Sao Hôm) thực chất là hành tinh nào?", "Sao Kim (Venus)", ["Sao Thủy", "Sao Hỏa", "Sao Mộc"], "Vì sao Kim nằm gần Mặt Trời hơn Trái Đất nên ta chỉ nhìn thấy nó vào lúc bình minh hoặc hoàng hôn.", "7-8", 2),
    ("Định vị bằng bóng nắng", "Vào đúng 12 giờ trưa ở Bắc bán cầu, bóng của một chiếc cọc cắm thẳng đứng trên đất sẽ đổ về hướng nào?", "Hướng Bắc", ["Hướng Nam", "Hướng Đông", "Hướng Tây"], "Mặt Trời buổi trưa ở hướng Nam nên bóng của mọi vật trên mặt đất sẽ đổ ngược về hướng Bắc.", "7-8", 2),
    ("Đồng hồ Mặt Trời cổ xưa", "Thời cổ đại khi chưa có đồng hồ điện tử, con người đo thời gian trong ngày bằng dụng cụ nào?", "Đồng hồ Mặt Trời (Dựa vào bóng cọc di chuyển)", ["Đồng hồ đeo tay", "Điện thoại thông minh", "Nhiệt kế thủy ngân"], "Khi Mặt Trời di chuyển từ Đông sang Tây, bóng của cây cọc trên mặt đĩa tròn di chuyển chỉ giờ chính xác.", "7-8", 2),
    ("Mùa lá rụng mùa thu", "Mùa thu mát mẻ với bầu trời trong xanh, gió heo may se lạnh và cây cối bắt đầu làm gì?", "Lá cây chuyển màu vàng đỏ rồi rụng xuống", ["Cây cối đóng băng trắng", "Cây cối nở hoa rực rỡ như mùa xuân", "Cây cối bị chết úng"], "Khung cảnh mùa thu Hà Nội với lá vàng xào xạc và hương hoa sữa nồng nàn là nét đẹp thơ mộng xao xuyến lòng người.", "6-7", 1)
]

raw_mc.extend(more_mc_vt)

# 15 SA items (VT136 - VT150)
raw_sa = [
    ("Hành tinh xanh", "Hành tinh thứ ba trong Hệ Mặt Trời nơi chúng ta đang sinh sống có tên là gì?", "trái đất", "Trái Đất là mái nhà chung tuyệt đẹp của muôn loài.", "6-7", 1),
    ("Ngôi sao trung tâm", "Ngôi sao khổng lồ tự phát sáng ở trung tâm của Hệ Mặt Trời là gì?", "mặt trời", "Mặt Trời cung cấp năng lượng ánh sáng và hơi ấm cho sự sống.", "6-7", 1),
    ("Vệ tinh của Trái Đất", "Thiên thể tự nhiên duy nhất bay quanh Trái Đất và tỏa sáng dịu mát vào ban đêm là gì?", "mặt trăng", "Mặt Trăng quay quanh Trái Đất và gây ra hiện tượng thủy triều.", "6-7", 1),
    ("Hành tinh đỏ", "Hành tinh nào trong Hệ Mặt Trời có bề mặt màu đỏ gạch do chứa nhiều oxit sắt?", "sao hỏa|hỏa tinh", "Sao Hỏa là hành tinh đỏ đang được con người tích cực thám hiểm.", "7-8", 2),
    ("Hành tinh lớn nhất", "Hành tinh to lớn nhất trong Hệ Mặt Trời có Vết Đỏ Lớn khổng lồ là hành tinh nào?", "sao mộc|mộc tinh", "Sao Mộc là hành tinh khí khổng lồ lớn nhất Hệ Mặt Trời.", "7-8", 2),
    ("Hiện tượng che Mặt Trời", "Hiện tượng Mặt Trăng đi vào giữa Mặt Trời và Trái Đất che khuất Mặt Trời ban ngày gọi là gì?", "nhật thực", "Nhật thực là hiện tượng thiên văn kỳ thú khi Mặt Trăng che khuất Mặt Trời.", "8-9", 3),
    ("Hiện tượng bóng Trái Đất che trăng", "Hiện tượng Trái Đất nằm giữa Mặt Trời và Mặt Trăng che khuất Mặt Trăng đêm rằm gọi là gì?", "nguyệt thực", "Nguyệt thực tạo ra hiện tượng trăng máu màu đỏ đồng kỳ ảo.", "8-9", 3),
    ("Cầu vồng sau mưa", "Hiện tượng dải sáng 7 màu uốn cong xuất hiện sau cơn mưa rào hửng nắng gọi là gì?", "cầu vồng|cầu vồng 7 sắc", "Cầu vồng gồm 7 màu: Đỏ, Cam, Vàng, Lục, Lam, Chàm, Tím.", "6-7", 1),
    ("Tia sáng nhanh hơn âm thanh", "Trong cơn giông bão, giữa tiếng sấm và tia chớp, cái nào xuất hiện truyền đến mắt chúng ta trước?", "tia chớp|chớp|ánh sáng chớp", "Vận tốc ánh sáng nhanh hơn vận tốc âm thanh nên ta thấy chớp trước sấm.", "7-8", 2),
    ("Vòng tuần hoàn nước", "Nước bốc hơi lên trời gặp lạnh ngưng tụ thành gì bồng bềnh trước khi tạo thành mưa?", "mây|đám mây", "Mây là tập hợp của hàng triệu giọt nước li ti trên bầu trời.", "6-7", 1),
    ("Dụng cụ đo nhiệt độ", "Dụng cụ dùng để đo nhiệt độ thời tiết xem trời nóng hay lạnh gọi là gì?", "nhiệt kế", "Nhiệt kế đo nhiệt độ không khí theo độ C (Celsius).", "6-7", 1),
    ("Dụng cụ chỉ hướng", "Dụng cụ có kim nam châm luôn chỉ về hướng Bắc giúp người đi rừng không bị lạc là gì?", "la bàn", "La bàn là công cụ định hướng quan trọng dựa vào từ trường Trái Đất.", "6-7", 1),
    ("Nhiệt độ nước sôi", "Ở áp suất bình thường, nước tinh khiết sôi ở bao nhiêu độ C?", "100|100 độ|100 độ c", "Nước sôi sủi bọt mạnh mẽ ở nhiệt độ 100 độ C.", "6-7", 1),
    ("Nhiệt độ đóng băng", "Nước tinh khiết bắt đầu đóng thành băng đá ở bao nhiêu độ C?", "0|0 độ|0 độ c", "Nước đóng băng thể rắn ở nhiệt độ 0 độ C.", "6-7", 1),
    ("Hiệu ứng giữ nhiệt khí quyển", "Hiện tượng khí cacbonic giữ nhiệt làm Trái Đất ngày càng nóng lên gọi là hiệu ứng gì?", "hiệu ứng nhà kính", "Hiệu ứng nhà kính làm biến đổi khí hậu và tan băng ở hai cực.", "8-9", 3)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"VT{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vũ Trụ & Thời Tiết",
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
    qid = f"VT{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vũ Trụ & Thời Tiết",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/vt_150.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"VT: {len(questions)} câu đã được ghi vào vt_150.json")

# Bổ sung 30 câu MC còn thiếu cho VT
extra_mc_vt = [
    ("Thiên hà Tiên Nữ (Andromeda)", "Thiên hà xoắn ốc lớn gần Dải Ngân Hà của chúng ta nhất có thể nhìn thấy bằng mắt thường vào ban đêm là thiên hà gì?", "Thiên hà Tiên Nữ (Andromeda)", ["Thiên hà Tam Giác", "Thiên hà Xì Gà", "Thiên hà Bánh Xe"], "Thiên hà Tiên Nữ cách Trái Đất khoảng 2,5 triệu năm ánh sáng và đang từ từ tiến về phía Dải Ngân Hà.", "8-9", 3),
    ("Mặt Trời mọc hướng nào", "Do Trái Đất tự quay quanh trục từ Tây sang Đông, hàng ngày chúng ta nhìn thấy Mặt Trời mọc ở hướng nào?", "Hướng Đông", ["Hướng Tây", "Hướng Nam", "Hướng Bắc"], "Mặt Trời mọc ở đằng Đông và lặn ở đằng Tây là quy luật thiên nhiên bất biến.", "6-7", 1),
    ("Mặt Trời lặn hướng nào", "Buổi chiều tà khi hoàng hôn buông xuống, Mặt Trời sẽ lặn ở phương nào?", "Hướng Tây", ["Hướng Đông", "Hướng Bắc", "Hướng Nam"], "Nhìn Mặt Trời lặn giúp xác định phương hướng khi đi lạc trong rừng vào buổi chiều.", "6-7", 1),
    ("Sao Thủy không có khí quyển", "Tại sao ban ngày trên Sao Thủy nóng tới 430 độ C nhưng ban đêm lại hạ xuống âm 180 độ C?", "Vì Sao Thủy gần như không có bầu khí quyển giữ nhiệt", ["Vì Sao Thủy bị Mặt Trời tắt đèn", "Vì Sao Thủy có tuyết rơi đêm", "Vì Sao Thủy xoay quá nhanh"], "Không có khí quyển che chắn hay giữ nhiệt, nhiệt độ bề mặt Sao Thủy dao động chênh lệch khủng khiếp giữa ngày và đêm.", "8-9", 3),
    ("Khí Heli trên Mặt Trời", "Mặt Trời phát sáng và tỏa nhiệt khổng lồ nhờ phản ứng nhiệt hạch biến đổi khí Hydro thành khí gì?", "Khí Heli (Helium)", ["Khí Oxy", "Khí Cacbonic", "Khí Clo"], "Phản ứng nhiệt hạch hợp hạch hạt nhân trên Mặt Trời là nguồn cội của mọi dạng năng lượng trên Trái Đất.", "8-9", 3),
    ("Vết đen Mặt Trời", "Những đốm đen thỉnh thoảng xuất hiện trên bề mặt chói lòa của Mặt Trời thực chất là gì?", "Những vùng có từ trường cực mạnh và nhiệt độ thấp hơn xung quanh (Vết đen Mặt Trời)", ["Những cái hố than cháy", "Những mẩu thiên thạch rơi vào", "Mặt Trời bị thủng lỗ"], "Vết đen Mặt Trời là nơi thường phát sinh các vụ bùng nổ tia bức xạ (lóe sáng mặt trời) tác động đến vệ tinh Trái Đất.", "8-9", 3),
    ("Bão từ tác động Trái Đất", "Khi Mặt Trời bùng phát các vụ nổ cực mạnh, hiện tượng nào có thể xảy ra trên Trái Đất?", "Bão từ gây nhiễu sóng vô tuyến viễn thông và lưới điện", ["Động đất làm nứt đất", "Nước biển sôi sục", "Không có ảnh hưởng gì"], "Bão từ có thể làm tê liệt hệ thống định vị GPS và mất tín hiệu liên lạc của máy bay, tàu thủy.", "8-9", 3),
    ("Tàu vũ trụ Voyager 1", "Con tàu thám hiểm không người lái của con người hiện đã bay xa nhất ra khỏi Hệ Mặt Trời vào không gian liên sao là tàu nào?", "Voyager 1", ["Apollo 11", "Curiosity", "Sputnik 1"], "Phóng từ năm 1977, Voyager 1 mang theo chiếc Đĩa Vàng chứa âm thanh và hình ảnh của Trái Đất gửi tới vũ trụ bao la.", "8-9", 3),
    ("Xe tự hành Sao Hỏa", "Robot tự hành bánh xe của NASA đang lăn bánh đào xới đất đá tìm dấu vết sự sống cổ đại trên Sao Hỏa có tên là gì?", "Perseverance (Kiên trì) và Curiosity (Tò mò)", ["Challenger", "Discovery", "Columbia"], "Các robot tự hành này gửi về Trái Đất hàng vạn bức ảnh độ nét cao về cảnh quan sa mạc đá đỏ ngoạn mục của Sao Hỏa.", "8-9", 3),
    ("Trạm Vũ trụ Quốc tế ISS", "Căn cứ khoa học khổng lồ bay trên quỹ đạo Trái Đất nơi các nhà du hành vũ trụ từ nhiều quốc gia cùng làm việc là gì?", "Trạm Vũ trụ Quốc tế (ISS)", ["Trạm Hòa Bình Mir", "Trạm Thiên Cung", "Trạm Skylab"], "Trạm ISS bay quanh Trái Đất với tốc độ 28.000 km/h, mỗi ngày các phi hành gia đón 16 lần bình minh và hoàng hôn.", "8-9", 3),
    ("Vận tốc thoát ly Trái Đất", "Để một tên lửa có thể thắng lực hút Trái Đất và bay vào không gian vũ trụ, nó cần đạt vận tốc tối thiểu bao nhiêu?", "Khoảng 11,2 km/giây (Vận tốc vũ trụ cấp 2)", ["Khoảng 100 km/giờ", "Khoảng 1.000 km/giờ", "Khoảng 300.000 km/giây"], "Động cơ tên lửa đốt nhiên liệu cực mạnh phụt luồng khí phản lực xuống dưới để đẩy tên lửa phóng vút lên cao.", "8-9", 3),
    ("Trọng lực là gì", "Lực bí mật kéo quả táo rơi từ trên cành cây xuống đất và giữ cho con người không bị bay vào không gian là gì?", "Trọng lực (Lực hấp dẫn của Trái Đất)", ["Lực từ trường nam châm", "Lực cản của gió", "Lực đàn hồi của đất"], "Nhà bác học thiên tài Isaac Newton đã phát hiện ra định luật vạn vật hấp dẫn khi quan sát quả táo rơi trong vườn.", "6-7", 1),
    ("Sức cản không khí khi rơi", "Tại sao một chiếc lá khô rơi từ trên cây xuống lại chao liệng chậm hơn nhiều so với một hòn sỏi?", "Vì chiếc lá có diện tích mặt phẳng lớn nên chịu lực cản không khí nhiều hơn", ["Vì chiếc lá nhẹ hơn Trái Đất", "Vì chiếc lá sợ rơi đau", "Do hòn sỏi có cánh"], "Trong ống chân không không có không khí, một chiếc lông chim và một quả cầu sắt nặng sẽ rơi chạm đáy cùng một lúc.", "8-9", 3),
    ("Dù nhảy hoạt động thế nào", "Chiếc dù của vận động viên nhảy dù mở to bung ra trên không trung nhằm mục đích gì?", "Tạo diện tích cản không khí tối đa để hãm tốc độ rơi an toàn xuống đất", ["Để đón gió bay lên vũ trụ", "Làm đẹp cho bầu trời", "Để che mưa rơi"], "Lực cản của tấm vải dù khổng lồ giữ cho vận động viên rơi với tốc độ êm ái khoảng 5 mét/giây tiếp đất nhẹ nhàng.", "7-8", 2),
    ("Áp suất tăng khi lặn sâu", "Khi các thợ lặn lặn sâu xuống đáy biển, tai họ cảm thấy đau nhức là do đại lượng nào tăng lên?", "Áp suất của cột nước đè lên màng nhĩ tăng dần theo độ sâu", ["Nước biển bị ngọt đi", "Cá biển cắn vào tai", "Do thiếu ánh sáng"], "Cứ lặn sâu thêm 10 mét, áp suất nước lại tăng thêm tương đương 1 bầu khí quyển (1 atm).", "8-9", 3),
    ("Khinh khí cầu bay lên", "Chiếc khinh khí cầu khổng lồ có thể bay bổng lên bầu trời nhờ nguyên lý vật lý nào?", "Đốt lửa làm nóng không khí trong quả cầu khiến nó nhẹ hơn không khí lạnh xung quanh", ["Bơm nước đá vào quả cầu", "Gắn cánh quạt máy bay", "Nhờ bồ câu kéo lên"], "Không khí nóng giãn nở, có khối lượng riêng nhẹ hơn không khí mát bên ngoài nên lực đẩy Ác-si-mét đẩy khinh khí cầu bay lên.", "7-8", 2),
    ("Bong bóng xà phòng hình cầu", "Tại sao những quả bong bóng xà phòng bay trong gió luôn luôn có hình cầu tròn vo hoàn hảo?", "Do sức căng bề mặt của màng xà phòng kéo co lại diện tích nhỏ nhất có thể", ["Do hơi thở thổi vào hình tròn", "Do gió uốn thành hình cầu", "Do trọng lực kéo tròn"], "Hình cầu là hình học có diện tích bề mặt nhỏ nhất tương ứng với một thể tích khí nhất định.", "8-9", 3),
    ("Tia cực tím (UV) có ở đâu", "Nguồn phát ra tia cực tím (tia tử ngoại UV) mạnh nhất trong tự nhiên tác động đến da chúng ta là gì?", "Ánh nắng Mặt Trời", ["Ngọn nến cháy", "Ánh trăng đêm rằm", "Đèn pin đồ chơi"], "Tiếp xúc quá nhiều với tia UV gay gắt giữa trưa có thể gây bỏng rát da và hại mắt, cần đội mũ và bôi kem chống nắng.", "7-8", 2),
    ("Mùa mưa ở miền Trung", "Khác với miền Bắc và miền Nam, mùa mưa lũ lớn nhất ở dải ven biển miền Trung nước ta thường rơi vào các tháng nào?", "Các tháng cuối năm (tháng 9, 10, 11 và 12)", ["Các tháng hè tháng 5 và 6", "Các tháng giêng sau Tết", "Quanh năm không mưa"], "Do địa hình Trường Sơn chắn gió đông bắc ẩm từ biển vào kết hợp với bão dồn dập vào mùa thu đông.", "8-9", 3),
    ("Biển Đông của Việt Nam", "Vùng biển rộng lớn nằm ở phía Đông và Nam của đất nước Việt Nam thân yêu có tên gọi là gì?", "Biển Đông", ["Biển Đỏ", "Biển Đen", "Biển Chết"], "Biển Đông là vùng biển nhiệt đới giàu tài nguyên hải sản, dầu khí và có vị trí giao thương hàng hải huyết mạch quốc tế.", "6-7", 1),
    ("Gió biển ban ngày", "Vào ban ngày ở vùng bờ biển, gió thường thổi từ hướng nào vào hướng nào?", "Từ biển thổi vào đất liền (Gió biển mát rượi)", ["Từ đất liền thổi ra biển", "Từ trên mây thổi xuống", "Không có gió"], "Ban ngày đất liền nóng nhanh hơn mặt biển làm không khí trên đất bốc lên, luồng gió mát từ biển tràn vào thay thế.", "8-9", 3),
    ("Gió đất ban đêm", "Ngược lại vào ban đêm ở bờ biển, gió thường thổi theo hướng nào ra biển?", "Từ đất liền thổi ra biển (Gió đất)", ["Từ biển thổi vào đất", "Thổi thẳng lên trời", "Gió lốc xoáy"], "Ban đêm đất liền tỏa nhiệt nguội nhanh hơn nước biển, không khí ấm trên biển bốc lên hút gió từ đất liền thổi ra.", "8-9", 3),
    ("Nhiệt kế đo thân nhiệt", "Nhiệt kế thủy ngân y tế dùng đo nhiệt độ cơ thể bé thường có vạch giới hạn từ bao nhiêu đến bao nhiêu độ C?", "Từ 35 độ C đến 42 độ C", ["Từ 0 độ C đến 100 độ C", "Từ -10 độ C đến 50 độ C", "Từ 30 độ C đến 80 độ C"], "Nhiệt độ cơ thể người bình thường dao động quanh mốc 36,5 - 37 độ C, không bao giờ thấp hơn 35 hay cao hơn 42 độ C.", "7-8", 2),
    ("Trời lạnh hà hơi ra khói", "Vào những ngày đông buốt giá ở miền Bắc, khi chúng ta thở phào ra miệng thấy làn khói mờ ảo là do đâu?", "Hơi nước ấm trong hơi thở gặp không khí lạnh bên ngoài ngưng tụ thành hạt nước li ti", ["Do trong miệng bốc cháy khói", "Do hít phải bụi", "Do thức ăn bốc hơi"], "Hiện tượng ngưng tụ hơi nước này hoàn toàn giống như cách những đám mây nhỏ hình thành trên bầu trời.", "6-7", 1),
    ("Mồ hôi làm mát cơ thể", "Khi chạy nhảy vui chơi ngoài nắng nóng, cơ thể bé toát nhiều mồ hôi ra da nhằm mục đích sinh học nào?", "Mồ hôi bốc hơi mang theo nhiệt lượng giúp làm mát hạ nhiệt cơ thể", ["Để làm ướt quần áo", "Để cơ thể nhẹ bớt", "Do cơ thể bị thừa nước"], "Toát mồ hôi là cơ chế tự điều hòa thân nhiệt tuyệt vời của con người giúp tránh bị sốc nhiệt ngày hè oi ả.", "7-8", 2),
    ("Uống nước khi trời nóng", "Vào những ngày hè oi bức hoặc sau khi tập thể dục toát mồ hôi, bé nên làm gì để bảo vệ sức khỏe?", "Uống từng ngụm nước lọc ấm hoặc nước khoáng bổ sung", ["Uống ngay một cốc nước đá lạnh buốt thật nhanh", "Nhịn uống nước", "Uống nhiều nước ngọt có gas"], "Uống nước mát từng ngụm nhỏ giúp bù đắp nước và chất điện giải đã mất mà không làm co mạch máu đột ngột.", "6-7", 1),
    ("Cây cối sau cơn mưa", "Sau cơn mưa rào, cây cối trong vườn trông tươi xanh mơn mởn hơn hẳn không chỉ nhờ nước mà còn nhờ gì?", "Tia sét giúp chuyển hóa khí nitơ trong không khí thành phân đạm tự nhiên theo nước mưa ngấm vào rễ", ["Do mưa có xà phòng", "Do gió thổi sạch lá", "Do chim hót làm cây vui"], "Dân gian có câu: 'Lúa chiêm lấp ló đầu bờ, Hễ nghe tiếng sấm phất cờ mà lên' giải thích hiện tượng bón đạm tự nhiên kỳ diệu này.", "8-9", 3),
    ("Hiện tượng bóng trăng đáy nước", "Khi nhìn xuống mặt hồ phẳng lặng đêm rằm, ta thấy hình ảnh vầng trăng tròn vành vạnh là do hiện tượng quang học nào?", "Hiện tượng phản xạ ánh sáng trên mặt nước phẳng như gương", ["Mặt Trăng rơi xuống đáy hồ", "Dưới đáy hồ có bóng đèn", "Do cá bơi xếp thành hình trăng"], "Mặt nước phẳng lặng đóng vai trò như một chiếc gương phẳng phản chiếu hình ảnh ánh trăng trên bầu trời.", "7-8", 2),
    ("Nhìn thấy các vì sao lấp lánh", "Tại sao khi ngắm các ngôi sao xa xôi trên bầu trời đêm ta lại thấy chúng lấp lánh nhấp nháy?", "Do ánh sáng sao bị các luồng khí quyển xáo động bẻ cong liên tục khi truyền tới mắt ta", ["Do các vì sao bật tắt công tắc liên tục", "Do sao sắp tắt", "Do mắt chớp"], "Kính thiên văn không gian Hubble bay ngoài bầu khí quyển nhìn thấy các vì sao sáng ổn định không hề bị nhấp nháy.", "8-9", 3),
    ("Bảo tồn nguồn nước sạch", "Nước ngọt sạch trên Trái Đất chỉ chiếm chưa đầy 3% tổng lượng nước, vì vậy bé cần có ý thức gì?", "Khóa chặt vòi nước sau khi dùng, không lãng phí và không xả rác xuống nguồn nước", ["Mở vòi nước chảy tự do", "Đổ rác thải nhựa xuống sông ngòi", "Xả nước tắm hàng giờ"], "Tiết kiệm từng giọt nước sạch là bảo vệ nguồn sống quý báu cho chính tương lai của chúng ta.", "6-7", 1)
]

raw_mc.extend(extra_mc_vt)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"VT{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vũ Trụ & Thời Tiết",
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
    qid = f"VT{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Vũ Trụ & Thời Tiết",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/vt_150.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Cập nhật VT hoàn tất: {len(questions)} câu đã được ghi vào vt_150.json")
