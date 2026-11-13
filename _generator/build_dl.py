# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1528127269322-539801943592?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1569154941061-e231b4725ef1?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1570535608479-ce0805c6a05c?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=600&auto=format&fit=crop&q=80"
]

# 126 MC items
raw_mc = [
    # 1-35 Vị trí, Lãnh thổ & Thủ đô các vùng miền
    ("Bản đồ hình chữ S", "Đất nước Việt Nam thân yêu của chúng ta trên bản đồ thế giới có hình dáng giống chữ cái nào?", "Hình chữ S mềm mại", ["Hình chữ O tròn vo", "Hình chữ V", "Hình chữ X"], "Bản đồ Việt Nam uốn lượn hình chữ S trải dài từ Lũng Cú (Hà Giang) đến Mũi Cà Mau.", "6-7", 1),
    ("Thủ đô Hà Nội ngàn năm", "Thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là thành phố ngàn năm văn hiến nào?", "Thủ đô Hà Nội", ["Thành phố Hồ Chí Minh", "Thành phố Đà Nẵng", "Thành phố Huế"], "Hà Nội là trái tim của cả nước với Hồ Gươm, Lăng Bác và 36 phố phường cổ kính.", "6-7", 1),
    ("Thành phố mang tên Bác", "Thành phố lớn nhất phương Nam, trung tâm kinh tế năng động và hiện đại hàng đầu nước ta là gì?", "Thành phố Hồ Chí Minh", ["Thành phố Cần Thơ", "Thành phố Hải Phòng", "Thành phố Nha Trang"], "TP Hồ Chí Minh rực rỡ bên dòng sông Sài Gòn với Bến Nhà Rồng lịch sử và chợ Bến Thành sầm uất.", "6-7", 1),
    ("Tiếp giáp phía Bắc", "Ở phía Bắc, nước Việt Nam chúng ta có chung đường biên giới đất liền với quốc gia láng giềng nào?", "Trung Quốc", ["Lào", "Campuchia", "Thái Lan"], "Biên giới phía Bắc có thác Bản Giốc hùng vĩ và cửa khẩu quốc tế Hữu Nghị.", "7-8", 2),
    ("Tiếp giáp phía Tây", "Ở phía Tây, đất nước ta giáp với hai quốc gia anh em láng giềng nào trên bán đảo Đông Dương?", "Lào và Campuchia", ["Thái Lan và Myanmar", "Trung Quốc và Nga", "Ấn Độ và Nhật Bản"], "Việt Nam, Lào và Campuchia cùng tựa lưng vào dãy Trường Sơn hùng vĩ, gắn bó keo sơn.", "7-8", 2),
    ("Tiếp giáp phía Đông", "Toàn bộ bờ biển phía Đông và phía Nam của đất nước Việt Nam tiếp giáp với vùng biển nào?", "Biển Đông", ["Biển Đỏ", "Biển Đen", "Biển Baltic"], "Biển Đông mang lại nguồn hải sản phong phú, dầu khí và điều hòa khí hậu mát mẻ cho đất liền.", "6-7", 1),
    ("Chiều dài bờ biển Việt Nam", "Đường bờ biển của nước ta uốn lượn từ Móng Cái (Quảng Ninh) đến Hà Tiên (Kiên Giang) dài bao nhiêu km?", "Dài hơn 3.260 km", ["Khoảng 500 km", "Khoảng 1.000 km", "Khoảng 10.000 km"], "Bờ biển dài hơn 3.260 km là lợi thế vàng phát triển kinh tế biển, cảng biển và du lịch nghỉ dưỡng.", "7-8", 2),
    ("Quần đảo Hoàng Sa và Trường Sa", "Hai quần đảo thiêng liêng ngoài khơi xa Biển Đông thuộc chủ quyền không thể tách rời của Việt Nam là gì?", "Quần đảo Hoàng Sa và Quần đảo Trường Sa", ["Quần đảo Hawaii", "Quần đảo Côn Lôn", "Quần đảo Nam Du"], "Hoàng Sa thuộc thành phố Đà Nẵng và Trường Sa thuộc tỉnh Khánh Hòa là một phần máu thịt của Tổ quốc.", "6-7", 1),
    ("Điểm cực Bắc Lũng Cú", "Điểm cực Bắc thiêng liêng trên đất liền của Tổ quốc có cột cờ Lũng Cú thuộc tỉnh nào?", "Tỉnh Hà Giang", ["Tỉnh Cao Bằng", "Tỉnh Lào Cai", "Tỉnh Lạng Sơn"], "Lá cờ đỏ sao vàng rộng 54 mét vuông tung bay trên đỉnh Lũng Cú tượng trưng cho 54 dân tộc anh em.", "7-8", 2),
    ("Điểm cực Nam Mũi Cà Mau", "Điểm cực Nam trên đất liền của Tổ quốc nơi có mốc tọa độ quốc gia và bãi bồi phù sa thuộc tỉnh nào?", "Tỉnh Cà Mau", ["Tỉnh Kiên Giang", "Tỉnh Bạc Liêu", "Tỉnh Sóc Trăng"], "Đất mũi Cà Mau là nơi duy nhất trên đất liền có thể ngắm Mặt Trời mọc ở biển Đông và lặn ở biển Tây.", "6-7", 1),
    ("Đỉnh Fansipan nóc nhà Đông Dương", "Đỉnh núi cao nhất Việt Nam và toàn bán đảo Đông Dương (cao 3.143 mét) tại Sa Pa thuộc tỉnh nào?", "Đỉnh Fansipan (Tỉnh Lào Cai)", ["Đỉnh Tây Côn Lĩnh", "Đỉnh Mẫu Sơn", "Đỉnh Bạch Mã"], "Fansipan được mệnh danh là 'Nóc nhà Đông Dương', nơi du khách ngắm biển mây bồng bềnh thần tiên.", "7-8", 2),
    ("Vịnh Hạ Long di sản thế giới", "Kỳ quan thiên nhiên thế giới nổi tiếng với hàng ngàn hòn đảo đá vôi nhô lên trên mặt nước ngọc bích thuộc tỉnh nào?", "Vịnh Hạ Long (Tỉnh Quảng Ninh)", ["Vịnh Nha Trang", "Vịnh Cam Ranh", "Vịnh Lăng Cô"], "Vịnh Hạ Long được UNESCO công nhận là Di sản Thiên nhiên Thế giới với vẻ đẹp non nước hữu tình kỳ vĩ.", "6-7", 1),
    ("Quần thể danh thắng Tràng An", "Di sản hỗn hợp văn hóa và thiên nhiên thế giới của Việt Nam với các hang động ngập nước kỳ ảo thuộc tỉnh nào?", "Tràng An (Tỉnh Ninh Bình)", ["Chùa Hương (Hà Nội)", "Tam Cốc (Bắc Giang)", "Hồ Ba Bể"], "Tràng An gắn liền với cố đô Hoa Lư lịch sử thời Đinh - Tiền Lê được bao bọc bởi núi non trùng điệp.", "7-8", 2),
    ("Động Phong Nha - Kẻ Bàng", "Vườn quốc gia nổi tiếng với hệ thống hang động đá vôi cổ nhất châu Á và hang Sơn Đoòng lớn nhất thế giới thuộc tỉnh nào?", "Tỉnh Quảng Bình", ["Tỉnh Quảng Trị", "Tỉnh Thừa Thiên Huế", "Tỉnh Hà Tĩnh"], "Sơn Đoòng là hang động tự nhiên lớn nhất thế giới, chứa được cả một tòa nhà chọc trời 40 tầng bên trong.", "7-8", 2),
    ("Hồ Hoàn Kiếm (Hồ Gươm)", "Hồ nước ngọt tự nhiên nằm giữa trung tâm thủ đô Hà Nội gắn liền với truyền thuyết Rùa Vàng đòi gươm thần là hồ gì?", "Hồ Hoàn Kiếm (Hồ Gươm)", ["Hồ Tây", "Hồ Trúc Bạch", "Hồ Ba Mẫu"], "Hồ Gươm có Tháp Rùa cổ kính, cầu Thê Húc đỏ son cong cong dẫn vào Đền Ngọc Sơn linh thiêng.", "6-7", 1),
    ("Hồ Tây rộng lớn", "Hồ nước ngọt tự nhiên có diện tích mặt nước rộng nhất thủ đô Hà Nội, nơi ngắm hoàng hôn tuyệt đẹp là gì?", "Hồ Tây (Dâm Đàm)", ["Hồ Gươm", "Hồ Bảy Mẫu", "Hồ Linh Đàm"], "Hồ Tây từng là một đoạn uốn khúc của sông Hồng cổ ngưng đọng lại thành hồ cảnh quan lộng gió.", "7-8", 2),
    ("Hồ Ba Bể trên núi", "Hồ nước ngọt tự nhiên trên vùng núi đá vôi lớn nhất Việt Nam thuộc tỉnh Bắc Kạn có tên là gì?", "Hồ Ba Bể", ["Hồ Núi Cốc", "Hồ Thác Bà", "Hồ Dầu Tiếng"], "Hồ Ba Bể nằm lọt thỏm giữa những dãy núi đá vôi phủ rừng nguyên sinh xanh biếc quanh năm.", "7-8", 2),
    ("Đảo Phú Quốc đảo ngọc", "Hòn đảo có diện tích lớn nhất Việt Nam nằm trong vịnh Thái Lan thuộc tỉnh Kiên Giang được mệnh danh là gì?", "Đảo Ngọc Phú Quốc", ["Đảo Cát Bà", "Đảo Côn Sơn", "Đảo Lý Sơn"], "Phú Quốc nổi tiếng với nước mắm cá cơm truyền thống, vườn tiêu xanh ngát và những bãi biển cát trắng tuyệt đẹp.", "6-7", 1),
    ("Quần đảo Côn Đảo", "Quần đảo thuộc tỉnh Bà Rịa - Vũng Tàu từng có nhà tù lịch sử và nay là thiên đường bảo tồn rùa biển là gì?", "Côn Đảo", ["Phú Quý", "Bạch Long Vĩ", "Cồn Cỏ"], "Côn Đảo có Vườn quốc gia biển phong phú, nơi hàng ngàn rùa biển mẹ lên bãi cát đẻ trứng mỗi năm.", "7-8", 2),
    ("Đảo Cát Bà Hải Phòng", "Hòn đảo lớn ngoài vịnh Bắc Bộ kề cận vịnh Lan Hạ, có khu dự trữ sinh quyển thế giới và loài voọc quý hiếm là gì?", "Đảo Cát Bà (Hải Phòng)", ["Đảo Cô Tô", "Đảo Hòn Tre", "Đảo Hòn Gai"], "Cát Bà là điểm đến du lịch sinh thái nổi tiếng kết hợp rừng nguyên sinh và biển xanh thơ mộng.", "7-8", 2),
    ("Sông Hồng phù sa", "Con sông lớn bồi đắp nên vùng đồng bằng Bắc Bộ trù phú, có màu nước đỏ hồng do chứa nhiều phù sa là sông gì?", "Sông Hồng (Sông Cái)", ["Sông Đà", "Sông Đáy", "Sông Cầu"], "Phù sa sông Hồng màu mỡ tạo nên những cánh đồng lúa xanh tốt và các làng gốm Bát Tràng truyền thống.", "6-7", 1),
    ("Sông Mê Kông chín rồng", "Dòng sông quốc tế chảy qua 6 nước đổ vào miền Nam Việt Nam rồi chia thành 9 cửa sông ra biển gọi là gì?", "Sông Cửu Long (Sông Mê Kông)", ["Sông Đồng Nai", "Sông Sài Gòn", "Sông Vàm Cỏ"], "Sông Cửu Long chia làm hai nhánh chính là sông Tiền và sông Hậu bồi đắp vựa lúa lớn nhất nước ta.", "6-7", 1),
    ("Sông Hương thơ mộng xứ Huế", "Dòng sông êm đềm chảy qua trung tâm thành phố Huế cổ kính, soi bóng chùa Thiên Mụ là sông gì?", "Sông Hương", ["Sông Hàn", "Sông Thu Bồn", "Sông Bến Hải"], "Nước sông Hương thơm ngát hương hoa cỏ cây rừng đầu nguồn, gắn liền với làn điệu ca Huế trên thuyền rồng.", "6-7", 1),
    ("Sông Hàn thành phố Đà Nẵng", "Thành phố biển Đà Nẵng nổi tiếng với chiếc cầu xoay và cầu Rồng phun lửa bắc qua dòng sông nào?", "Sông Hàn", ["Sông Hương", "Sông Trà Khúc", "Sông Côn"], "Đà Nẵng được mệnh danh là 'Thành phố của những cây cầu' lung linh sắc màu phản chiếu mặt nước sông Hàn.", "6-7", 1),
    ("Sông Đà thủy điện lớn", "Con sông chảy qua vùng núi Tây Bắc hiểm trở có nhà máy thủy điện Hòa Bình và Sơn La lớn nhất Đông Nam Á là sông gì?", "Sông Đà", ["Sông Lô", "Sông Gâm", "Sông Thao"], "Sông Đà hung bạo nhưng mang lại nguồn điện năng vô tận thắp sáng cả đất nước và ngăn lũ sông Hồng.", "8-9", 3),
    ("Sông Bạch Đằng lịch sử", "Dòng sông lịch sử ba lần chứng kiến quân dân ta cắm cọc gỗ đại phá quân xâm lược phương Bắc là sông nào?", "Sông Bạch Đằng", ["Sông Như Nguyệt", "Sông Mã", "Sông Gianh"], "Chiến thắng Bạch Đằng của Ngô Quyền năm 938 và Trần Hưng Đạo năm 1288 mãi vang danh non sông.", "7-8", 2),
    ("Đồng bằng sông Cửu Long", "Đồng bằng châu thổ lớn nhất nước ta, được mệnh danh là 'Vựa lúa và vựa trái cây số 1 của cả nước' là đồng bằng nào?", "Đồng bằng sông Cửu Long (Miền Tây Nam Bộ)", ["Đồng bằng sông Hồng", "Đồng bằng duyên hải miền Trung", "Đồng bằng Thanh Nghệ Tĩnh"], "Miền Tây trù phú với mạng lưới kênh rạch chằng chịt, chợ nổi nhộn nhịp và những vườn cây trái xum xuê.", "6-7", 1),
    ("Đồng bằng sông Hồng", "Vùng đồng bằng màu mỡ nằm ở phía Bắc, nơi cái nôi của nền văn minh lúa nước ngàn đời là đồng bằng nào?", "Đồng bằng sông Hồng (Bắc Bộ)", ["Đồng bằng sông Cửu Long", "Đồng bằng sông Mã", "Đồng bằng sông Cả"], "Đồng bằng Bắc Bộ nổi tiếng với hệ thống đê điều kiên cố hàng ngàn cây số bảo vệ mùa màng xóm làng.", "6-7", 1),
    ("Vùng cao nguyên Tây Nguyên", "Vùng đất cao nguyên bazan màu mỡ nổi tiếng với những đồi cà phê, cao su và văn hóa cồng chiêng là vùng nào?", "Tây Nguyên", ["Tây Bắc", "Đông Bắc", "Bắc Trung Bộ"], "Tây Nguyên gồm 5 tỉnh: Kon Tum, Gia Lai, Đắk Lắk, Đắk Nông và Lâm Đồng hùng vĩ thác ngàn.", "7-8", 2),
    ("Thành phố ngàn hoa Đà Lạt", "Thành phố du lịch nổi tiếng trên cao nguyên Lâm Viên có khí hậu mát mẻ quanh năm, ngàn hoa khoe sắc là gì?", "Thành phố Đà Lạt (Lâm Đồng)", ["Thành phố Buôn Ma Thuột", "Thành phố Pleiku", "Thành phố Kon Tum"], "Đà Lạt thơ mộng với rừng thông reo, hồ Xuân Hương, vườn dâu tây chín mọng và thác Cam Ly kỳ vĩ.", "6-7", 1),
    ("Thành phố hoa phượng đỏ Hải Phòng", "Thành phố cảng biển lớn nhất miền Bắc rực rỡ sắc hoa phượng vĩ vào mùa hè có tên gọi là gì?", "Thành phố Hải Phòng", ["Thành phố Hạ Long", "Thành phố Nam Định", "Thành phố Uông Bí"], "Hải Phòng là đầu mối giao thương hàng hải quốc tế sầm uất với các bến cảng container hiện đại.", "6-7", 1),
    ("Phố cổ Hội An", "Đô thị cổ bên bờ sông Hoài (Quảng Nam) được UNESCO vinh danh với những dãy nhà ngói rêu phong và đèn lồng lung linh là gì?", "Phố cổ Hội An", ["Cố đô Huế", "Thành cổ Quảng Trị", "Phố Hiến"], "Hội An từng là thương cảng quốc tế sầm uất từ thế kỷ 16-17, nơi giao thoa văn hóa Việt - Nhật - Hoa.", "7-8", 2),
    ("Cố đô Huế di sản", "Quần thể di tích cung đình triều Nguyễn với Đại Nội, lăng tẩm và Ngọ Môn uy nghiêm nằm ở tỉnh nào?", "Tỉnh Thừa Thiên Huế", ["Tỉnh Quảng Bình", "Tỉnh Quảng Nam", "Tỉnh Thanh Hóa"], "Cố đô Huế mang vẻ đẹp trầm mặc cổ kính với Nhã nhạc cung đình Huế là di sản văn hóa phi vật thể nhân loại.", "7-8", 2),
    ("Địa đạo Củ Chi huyền thoại", "Hệ thống đường hầm ngầm dài hơn 200 km trong lòng đất thời kháng chiến tại TP Hồ Chí Minh được gọi là gì?", "Địa đạo Củ Chi", ["Địa đạo Vịnh Mốc", "Hang Pác Bó", "Chiến khu Đ"], "Địa đạo Củ Chi như một 'thành phố ngầm' có đầy đủ phòng họp, bếp Hoàng Cầm, bệnh viện dã chiến.", "7-8", 2),
    ("Cao nguyên đá Đồng Văn", "Công viên địa chất toàn cầu đầu tiên của Việt Nam với trập trùng núi đá tai mèo xám xịt hùng vĩ thuộc tỉnh nào?", "Tỉnh Hà Giang", ["Tỉnh Yên Bái", "Tỉnh Tuyên Quang", "Tỉnh Sơn La"], "Đồng Văn nổi tiếng với đèo Mã Pí Lèng hiểm trở, dòng sông Nho Quế xanh như ngọc bích và hoa tam giác mạch.", "8-9", 3)
]

# Thêm 91 câu MC nữa để đủ 126 câu MC
more_mc_dl = [
    ("Đèo Hải Vân thiên hạ đệ nhất hùng quan", "Con đèo hiểm trở uốn lượn vượt qua dãy núi Bạch Mã nối liền tỉnh Thừa Thiên Huế và TP Đà Nẵng là đèo gì?", "Đèo Hải Vân", ["Đèo Ngang", "Đèo Cả", "Đèo Ngoạn Mục"], "Vua Lê Thánh Tông khi vi hành từng khắc tặng đèo Hải Vân danh hiệu 'Thiên hạ đệ nhất hùng quan'.", "7-8", 2),
    ("Đèo Ngang ranh giới lịch sử", "Con đèo ranh giới giữa hai tỉnh Hà Tĩnh và Quảng Bình từng đi vào bài thơ bất hủ của Bà Huyện Thanh Quan là đèo gì?", "Đèo Ngang", ["Đèo Hải Vân", "Đèo Cù Mông", "Đèo Pha Đin"], "'Bước tới Đèo Ngang bóng xế tà, Cỏ cây chen đá lá chen hoa' là những câu thơ ghi sâu trong lòng người Việt.", "7-8", 2),
    ("Đèo Mã Pí Lèng vua của các con đèo", "Một trong 'Tứ đại đỉnh đèo' hùng vĩ bậc nhất miền Bắc nằm trên con đường Hạnh Phúc ở Hà Giang là đèo gì?", "Đèo Mã Pí Lèng", ["Đèo Ô Quy Hồ", "Đèo Khau Phạ", "Đèo Pha Đin"], "Đứng trên đỉnh Mã Pí Lèng nhìn xuống hẻm Tu Sản sâu hun hút và dòng sông Nho Quế uốn lượn như dải lụa xanh.", "8-9", 3),
    ("Thác Bản Giốc thác nước biên giới", "Thác nước tự nhiên tuyệt đẹp nằm trên đường biên giới Việt Nam - Trung Quốc thuộc tỉnh Cao Bằng là thác gì?", "Thác Bản Giốc", ["Thác Cam Ly", "Thác Dambri", "Thác Pongour"], "Thác Bản Giốc tuôn dòng bọt trắng xóa như dải lụa khổng lồ buông xuống giữa non xanh nước biếc Trùng Khánh.", "7-8", 2),
    ("Chợ nổi Cái Răng miền Tây", "Nét sinh hoạt văn hóa độc đáo trên sông nước Cần Thơ nơi hàng trăm ghe thuyền họp chợ mua bán trái cây gọi là gì?", "Chợ nổi Cái Răng", ["Chợ Bến Thành", "Chợ Đồng Xuân", "Chợ Đông Ba"], "Mỗi chiếc thuyền cắm một cây sào tre gọi là 'cây bẹo' treo lủng lẳng loại trái cây muốn bán để khách nhìn từ xa.", "6-7", 1),
    ("Cánh đồng lúa Mù Cang Chải", "Những thửa ruộng bậc thang kỳ vĩ xếp tầng tầng lớp lớp vàng óng ả mùa lúa chín thuộc tỉnh nào?", "Mù Cang Chải (Yên Bái)", ["Hòa Bình", "Điện Biên", "Lai Châu"], "Ruộng bậc thang là kiệt tác nghệ thuật canh tác độc đáo của đồng bào dân tộc H'Mông trên sườn núi cao.", "7-8", 2),
    ("Thung lũng Mường Thanh vựa lúa Tây Bắc", "Cánh đồng lúa trù phú lớn nhất vùng Tây Bắc gắn liền với chiến thắng Điện Biên Phủ lẫy lừng là cánh đồng nào?", "Cánh đồng Mường Thanh (Điện Biên)", ["Cánh đồng Mường Lò", "Cánh đồng Mường Than", "Cánh đồng Mường Tấc"], "Dân gian có câu: 'Nhất Thanh, nhì Lò, tam Than, tứ Tấc' ngợi ca 4 cánh đồng phì nhiêu trù phú nhất Tây Bắc.", "8-9", 3),
    ("Vùng biển Cà Ná Ninh Thuận", "Vùng biển có độ mặn cao và nắng nhiều nhất Việt Nam, là vựa sản xuất muối lớn nhất cả nước là gì?", "Cà Ná (Ninh Thuận)", ["Sa Huỳnh (Quảng Ngãi)", "Hòn Khói (Khánh Hòa)", "Bạc Liêu"], "Muối Cà Ná trắng tinh khiết, đậm đà hạt ngọc của biển cả cung cấp cho cả nước và công nghiệp hóa chất.", "8-9", 3),
    ("Mũi Né đồi cát bay", "Bãi biển nghỉ dưỡng nổi tiếng với những đồi cát đỏ, cát trắng di động hình thù thay đổi theo gió thuộc tỉnh nào?", "Mũi Né (Bình Thuận)", ["Vũng Tàu", "Phan Rang", "Tuy Hòa"], "Đồi cát Mũi Né như một tiểu sa mạc rực rỡ, nơi du khách thích thú chơi trò trượt cát từ đỉnh đồi.", "6-7", 1),
    ("Vịnh Nha Trang biển xanh cát trắng", "Thành phố biển xinh đẹp thuộc tỉnh Khánh Hòa nổi tiếng với vịnh biển êm đềm, cáp treo vượt biển Vinpearl là gì?", "Thành phố Nha Trang", ["Thành phố Quy Nhơn", "Thành phố Phan Thiết", "Thành phố Tuy Hòa"], "Nha Trang có Viện Hải dương học lưu giữ hàng vạn mẫu sinh vật biển kỳ thú và rạn san hô Hòn Mun lộng lẫy.", "6-7", 1),
    ("Vườn quốc gia Cúc Phương", "Vườn quốc gia đầu tiên của Việt Nam nằm trên địa bàn 3 tỉnh Ninh Bình, Hòa Bình, Thanh Hóa là gì?", "Vườn quốc gia Cúc Phương", ["Vườn quốc gia Ba Vì", "Vườn quốc gia Cát Tiên", "Vườn quốc gia Bạch Mã"], "Cúc Phương nổi tiếng với cây chò ngàn năm tuổi, trung tâm cứu hộ linh trưởng và mùa bướm trắng bay rợp trời tháng Năm.", "7-8", 2),
    ("Vườn quốc gia Cát Tiên", "Khu dự trữ sinh quyển thế giới ở miền Đông Nam Bộ là mái nhà của loài tê giác một sừng (trước đây) và đàn voi rừng là gì?", "Vườn quốc gia Nam Cát Tiên", ["Vườn Tràm Chim", "Vườn U Minh", "Vườn Bến En"], "Cát Tiên có Bàu Sấu là vùng đất ngập nước Ramsar quốc tế bảo tồn loài cá sấu xiêm nước ngọt quý hiếm.", "8-9", 3),
    ("Vườn quốc gia Tràm Chim Tam Nông", "Vùng đất ngập nước ở Đồng Tháp nổi tiếng là nơi dừng chân kiếm ăn của loài chim sếu đầu đỏ quý hiếm là gì?", "Vườn quốc gia Tràm Chim", ["Vườn U Minh Hạ", "Khu bảo tồn Láng Sen", "Rừng ngập mặn Cần Giờ"], "Tràm Chim là vương quốc của các loài thủy cầm hoang dã giữa cánh đồng cỏ bàng và hoa sen nở rộ.", "8-9", 3),
    ("Rừng Sác Cần Giờ lá phổi xanh TP.HCM", "Khu dự trữ sinh quyển rừng ngập mặn ven biển rộng lớn được mệnh danh là lá phổi xanh của TP Hồ Chí Minh là gì?", "Rừng ngập mặn Cần Giờ (Rừng Sác)", ["Rừng ngập mặn Cà Mau", "Rừng tràm Trà Sư", "Rừng Bảy Mẫu"], "Cần Giờ chắn sóng biển bảo vệ thành phố và là điểm du lịch sinh thái với Đảo Khỉ ngộ nghĩnh.", "7-8", 2),
    ("Rừng tràm Trà Sư An Giang", "Khu rừng tràm ngập nước xanh mướt với những thảm bèo cám phủ kín mặt nước ngồi xuồng chèo len lỏi là gì?", "Rừng tràm Trà Sư", ["Rừng U Minh Thượng", "Rừng tràm Gáo Giồng", "Rừng đước Năm Căn"], "Đi tắc ráng lướt trên thảm bèo xanh như nhung giữa tiếng chim chóc ríu rít là trải nghiệm khó quên của miền Tây.", "7-8", 2),
    ("Thác Dray Nur và Dray Sap", "Cặp thác nước sinh đôi hùng vĩ tuôn trào trắng xóa trên dòng sông Sêrêpôk huyền thoại thuộc vùng đất nào?", "Đắk Lắk và Đắk Nông (Tây Nguyên)", ["Gia Lai", "Kon Tum", "Lâm Đồng"], "Dòng sông Sêrêpôk đặc biệt chảy ngược dòng sang phía tây đổ sang Campuchia trước khi hòa vào Mê Kông.", "8-9", 3),
    ("Hồ Lắk Đắk Lắk", "Hồ nước ngọt tự nhiên lớn nhất Tây Nguyên gắn liền với hình ảnh đàn voi lội nước và buôn làng người M'Nông là hồ gì?", "Hồ Lắk", ["Biển Hồ T'Nưng", "Hồ Ayun Hạ", "Hồ Ea Kao"], "Bên bờ Hồ Lắk có biệt điện cổ kính của vua Bảo Đại nhìn ra toàn cảnh mặt hồ mênh mông thơ mộng.", "8-9", 3),
    ("Biển Hồ Pleiku (Hồ T'Nưng)", "Hồ nước trong xanh biếc phẳng lặng trên cao nguyên Pleiku từng là miệng một ngọn núi lửa cổ xưa tắt hàng triệu năm là gì?", "Biển Hồ (Hồ T'Nưng)", ["Hồ Lắk", "Hồ Than Thở", "Hồ Tuyền Lâm"], "Nhạc sĩ Nguyễn Cường từng viết bài hát nổi tiếng: 'Không dám nhìn vào đôi mắt ấy... đôi mắt Pleiku Biển Hồ đầy'.", "7-8", 2),
    ("Dãy núi Trường Sơn hùng vĩ", "Xương sống địa hình của bán đảo Đông Dương chia cắt khí hậu hai miền Đông và Tây là dãy núi nào?", "Dãy núi Trường Sơn (Trường Sơn Bắc và Trường Sơn Nam)", ["Dãy Hoàng Liên Sơn", "Dãy Tam Đảo", "Dãy Đông Triều"], "Đường mòn Hồ Chí Minh lịch sử xẻ dọc Trường Sơn đi cứu nước là bản anh hùng ca bất diệt của dân tộc.", "7-8", 2),
    ("Dãy Hoàng Liên Sơn nóc nhà", "Dãy núi cao và đồ sộ nhất Việt Nam nằm ở vùng Tây Bắc nơi có đỉnh Fansipan chót vót là dãy núi nào?", "Dãy Hoàng Liên Sơn", ["Dãy Sông Gâm", "Dãy Ngân Sơn", "Dãy Bắc Sơn"], "Hoàng Liên Sơn như bức tường thành khổng lồ ngăn gió mùa đông bắc tạo nên sự khác biệt khí hậu giữa Tây Bắc và Đông Bắc.", "8-9", 3),
    ("Thành phố Quy Nhơn biển xanh", "Thành phố biển miền Trung có bãi tắm Kỳ Co, Eo Gió tuyệt đẹp và gắn liền với nhà thơ Hàn Mặc Tử là thành phố nào?", "Thành phố Quy Nhơn (Bình Định)", ["Thành phố Tuy Hòa", "Thành phố Quảng Ngãi", "Thành phố Cam Ranh"], "Quy Nhơn là vùng đất võ Bình Định anh hùng, nơi phát tích của phong trào Tây Sơn hiển hách.", "7-8", 2),
    ("Thành phố Buôn Ma Thuột thủ phủ cà phê", "Thành phố lớn nhất Tây Nguyên được công nhận là 'Thủ phủ cà phê của Việt Nam' là thành phố nào?", "Thành phố Buôn Ma Thuột (Đắk Lắk)", ["Thành phố Pleiku", "Thành phố Kon Tum", "Thành phố Gia Nghĩa"], "Nơi đây có Bảo tàng Thế giới Cà phê hiện đại và lễ hội cà phê quốc tế rộn ràng hàng năm.", "7-8", 2),
    ("Thành phố Cần Thơ gạo trắng nước trong", "Thành phố trực thuộc trung ương lớn nhất miền Tây Nam Bộ có câu ca dao 'Gạo trắng nước trong, ai đi đến đó lòng không muốn về' là gì?", "Thành phố Cần Thơ", ["Thành phố Mỹ Tho", "Thành phố Long Xuyên", "Thành phố Rạch Giá"], "Cần Thơ là trung tâm kinh tế, giáo dục y tế của cả vùng đồng bằng sông Cửu Long với bến Ninh Kiều lộng gió.", "6-7", 1),
    ("Cầu Cần Thơ dây văng", "Cây cầu dây văng có nhịp chính dài nhất Đông Nam Á bắc qua sông Hậu nối liền Vĩnh Long và Cần Thơ là cầu gì?", "Cầu Cần Thơ", ["Cầu Mỹ Thuận", "Cầu Rạch Miễu", "Cầu Cổ Chiên"], "Cầu Cần Thơ khánh thành năm 2010 đã chấm dứt nhiều thập kỷ cảnh phà tắc nghẽn qua sông Hậu.", "7-8", 2),
    ("Cầu Mỹ Thuận cây cầu dây văng đầu tiên", "Cây cầu dây văng đầu tiên của Việt Nam bắc qua sông Tiền khánh thành năm 2000 nối Tiền Giang và Vĩnh Long là cầu gì?", "Cầu Mỹ Thuận", ["Cầu Cần Thơ", "Cầu Hàm Rông", "Cầu Long Biên"], "Cầu Mỹ Thuận mang hình dáng cánh chim hải âu vươn cao mở ra kỷ nguyên mới xây dựng cầu hiện đại ở nước ta.", "7-8", 2),
    ("Cầu Long Biên chứng nhân lịch sử", "Cây cầu thép cổ kính hơn 100 năm tuổi bắc qua sông Hồng ở Hà Nội từng là một trong những cây cầu dài nhất thế giới thời bấy giờ?", "Cầu Long Biên", ["Cầu Thăng Long", "Cầu Nhật Tân", "Cầu Chương Dương"], "Cầu Long Biên do người Pháp xây dựng, như một chứng nhân lịch sử kiên cường đi qua hai cuộc kháng chiến vĩ đại.", "7-8", 2),
    ("Cầu Nhật Tân cầu dây văng 5 nhịp", "Cây cầu dây văng hiện đại bắc qua sông Hồng ở Hà Nội có 5 trụ tháp tượng trưng cho 5 cửa ô Hà Nội là cầu gì?", "Cầu Nhật Tân", ["Cầu Vĩnh Tuy", "Cầu Thanh Trì", "Cầu Đuống"], "Vào ban đêm, cầu Nhật Tân bừng sáng lung linh với hệ thống đèn LED đổi màu hiện đại chào đón du khách quốc tế.", "7-8", 2),
    ("Thành phố cảng Vân Đồn", "Thương cảng biển đầu tiên trong lịch sử Đại Việt được thành lập từ thời vua Lý Anh Tông năm 1149 là thương cảng nào?", "Thương cảng Vân Đồn (Quảng Ninh)", ["Thương cảng Phố Hiến", "Thương cảng Hội An", "Thương cảng Ba Ngòi"], "Vân Đồn từng là cửa ngõ giao thương hàng hải sầm uất đón hàng ngàn tàu buôn từ Trung Quốc, Xiêm La, Ấn Độ.", "8-9", 3),
    ("Phố Hiến thứ nhất Kinh Kỳ", "Thương cảng trên bến dưới thuyền bên sông Hồng thời thế kỷ 17 có câu ca dao 'Thứ nhất Kinh Kỳ, thứ nhì...' là vùng đất nào?", "Phố Hiến (Hưng Yên)", ["Phố Cổ Hội An", "Kinh Bắc", "Sơn Nam"], "Phố Hiến xưa kia là đô thị buôn bán tấp nập của các thương gia Hà Lan, Anh, Pháp, Nhật Bản và Trung Hoa.", "8-9", 3),
    ("Chùa Một Cột đóa sen ngàn năm", "Ngôi chùa cổ kính độc đáo ở Hà Nội được xây dựng trên một cột đá đứng giữa hồ sen giống như đóa sen nở là gì?", "Chùa Một Cột (Chùa Diên Hựu)", ["Chùa Trấn Quốc", "Chùa Quán Sứ", "Chùa Thầy"], "Vua Lý Thái Tông cho dựng chùa năm 1049 sau giấc mơ thấy Phật Bà Quan Âm dắt lên tòa sen vàng.", "6-7", 1),
    ("Chùa Hương lễ hội mùa xuân", "Quần thể chùa chiền hang động thắng cảnh ở Mỹ Đức (Hà Nội) có lễ hội kéo dài suốt 3 tháng mùa xuân là gì?", "Chùa Hương (Hương Sơn)", ["Chùa Bái Đính", "Chùa Tam Chúc", "Chùa Yên Tử"], "Du khách ngồi thuyền suối Yến thơ mộng ngắm hoa gạo đỏ rực vào vãn cảnh Động Hương Tích 'Nam thiên đệ nhất động'.", "7-8", 2),
    ("Chùa Bái Đính kỷ lục", "Ngôi chùa khổng lồ ở Ninh Bình sở hữu nhiều kỷ lục châu Á như tượng Phật bằng đồng dát vàng lớn nhất, hành lang La Hán dài nhất là gì?", "Chùa Bái Đính", ["Chùa Tam Chúc", "Chùa Ba Vàng", "Chùa Vĩnh Nghiêm"], "Chùa Bái Đính nằm trong quần thể di sản Tràng An, là trung tâm sinh hoạt Phật giáo tâm linh lớn của cả nước.", "7-8", 2),
    ("Núi Yên Tử đất tổ Phật giáo", "Ngọn núi cao ở Quảng Ninh nơi vua Trần Nhân Tông xuất gia tu hành và sáng lập ra Thiền phái Trúc Lâm Yên Tử là núi gì?", "Núi Yên Tử (Bạch Vân Sơn)", ["Núi Bà Đen", "Núi Cấm", "Núi Chúa"], "Yên Tử quanh năm mây trắng bay mờ ảo, đỉnh núi có chùa Đồng linh thiêng đúc hoàn toàn bằng đồng nguyên khối.", "8-9", 3),
    ("Núi Bà Đen nóc nhà Đông Nam Bộ", "Ngọn núi lửa đã tắt cao nhất miền Đông Nam Bộ (cao 986 mét) sừng sững giữa đồng bằng thuộc tỉnh Tây Ninh là núi gì?", "Núi Bà Đen", ["Núi Chứa Chan", "Núi Dinh", "Núi Bà Rá"], "Núi Bà Đen có hệ thống cáp treo hiện đại và đại tượng Phật Bà Tây Bổ Đà Sơn bằng đồng kỷ lục châu Á.", "7-8", 2),
    ("Núi Cấm An Giang", "Ngọn núi cao và linh thiêng nhất trong dãy Thất Sơn (Bảy Núi) huyền bí vùng biên giới Tây Nam An Giang là núi gì?", "Núi Cấm (Thiên Cấm Sơn)", ["Núi Cô Tô", "Núi Két", "Núi Dài"], "Núi Cấm có hồ Thủy Liêm trên đỉnh và tượng Phật Di Lặc khổng lồ ngồi mỉm cười thanh thản giữa non ngàn.", "8-9", 3),
    ("Đảo Lý Sơn vương quốc tỏi", "Hòn đảo núi lửa ngoài khơi tỉnh Quảng Ngãi nổi tiếng với những cánh đồng hành tỏi thơm ngon bậc nhất là đảo gì?", "Đảo Lý Sơn (Cù Lao Ré)", ["Đảo Cù Lao Chàm", "Đảo Cồn Cỏ", "Đảo Hòn Ngư"], "Đất đỏ bazan trộn cát san hô trắng tạo nên hương vị cay nồng thanh tao nức tiếng cho củ tỏi Lý Sơn.", "7-8", 2),
    ("Đảo Cù Lao Chàm Hội An", "Cụm đảo ngoài khơi Hội An (Quảng Nam) là khu dự trữ sinh quyển thế giới nghiêm cấm sử dụng túi nilon là đảo gì?", "Cù Lao Chàm", ["Cù Lao Xanh", "Cù Lao Câu", "Cát Bà"], "Cù Lao Chàm nổi tiếng với rạn san hô nguyên sơ, món ốc vú nàng và chiến dịch bảo vệ môi trường biển kiểu mẫu.", "7-8", 2),
    ("Vịnh Cam Ranh cảng nước sâu", "Vịnh biển kín gió nước sâu bậc nhất thế giới nằm ở tỉnh Khánh Hòa có vị trí chiến lược quân sự hàng đầu là vịnh gì?", "Vịnh Cam Ranh", ["Vịnh Vân Phong", "Vịnh Xuân Đài", "Vịnh Vĩnh Hy"], "Cam Ranh có thể neo đậu được những tàu sân bay và tàu ngầm quân sự khổng lồ an toàn tránh bão.", "8-9", 3),
    ("Vịnh Vĩnh Hy Ninh Thuận", "Một trong những vịnh biển đẹp và hoang sơ nhất Việt Nam nằm lọt thỏm giữa núi rừng Vườn quốc gia Núi Chúa là gì?", "Vịnh Vĩnh Hy", ["Vịnh Lăng Cô", "Vịnh Hạ Long", "Vịnh Lan Hạ"], "Vĩnh Hy nước trong vắt nhìn thấy đáy, du khách đi tàu đáy kính ngắm nhìn những rạn san hô nhiều màu sắc kỳ thú.", "7-8", 2),
    ("Ghềnh Đá Đĩa Phú Yên", "Kỳ quan địa chất độc nhất vô nhị ở Phú Yên với hàng ngàn cột đá bazan hình lục giác xếp khít nhau như chồng đĩa là gì?", "Ghềnh Đá Đĩa", ["Ghềnh Ráng", "Mũi Điện", "Hòn Yến"], "Nham thạch núi lửa phun trào gặp nước biển lạnh co rút đột ngột nứt thành những cột đá hình trụ lục giác thẳng tắp.", "8-9", 3),
    ("Mũi Điện Đại Lãnh", "Mũi đất nhô ra biển ở Phú Yên có ngọn hải đăng cổ kính, nơi đón ánh bình minh đầu tiên trên đất liền Việt Nam là gì?", "Mũi Điện (Mũi Đại Lãnh)", ["Mũi Né", "Mũi Kê Gà", "Mũi Ba Làng An"], "Đón những tia nắng đầu tiên của ngày mới trên ngọn hải đăng Mũi Điện là trải nghiệm tự hào thiêng liêng.", "7-8", 2),
    ("Mũi Đôi Khánh Hòa cực Đông", "Điểm cực Đông thực tế trên đất liền của Tổ quốc Việt Nam nằm tại bán đảo Hòn Gốm thuộc tỉnh nào?", "Tỉnh Khánh Hòa (Mũi Đôi)", ["Tỉnh Bình Định", "Tỉnh Phú Yên", "Tỉnh Ninh Thuận"], "Hành trình chinh phục mốc cực Đông Mũi Đôi vượt qua các cồn cát trắng và bãi đá nhảy hoang sơ đầy thách thức.", "8-9", 3),
    ("Mốc cực Tây A Pa Chải", "Ngã ba biên giới Việt Nam - Lào - Trung Quốc nơi có câu nói 'một con gà gáy cả ba nước cùng nghe' nằm ở tỉnh nào?", "A Pa Chải (Tỉnh Điện Biên)", ["Tỉnh Lai Châu", "Tỉnh Sơn La", "Tỉnh Lào Cai"], "Mốc số 0 A Pa Chải nằm trên đỉnh núi Khoan La San cao gần 1.900m là điểm đến tự hào của tuổi trẻ yêu nước.", "8-9", 3),
    ("Biển Sầm Sơn Thanh Hóa", "Bãi biển du lịch nổi tiếng với sóng to cát mịn và hòn Trống Mái huyền thoại thuộc tỉnh nào?", "Tỉnh Thanh Hóa (Sầm Sơn)", ["Tỉnh Nghệ An", "Tỉnh Hà Tĩnh", "Tỉnh Ninh Bình"], "Sầm Sơn là bãi tắm nghỉ mát quen thuộc hàng trăm năm nay của người dân miền Bắc mỗi dịp hè về.", "6-7", 1),
    ("Biển Cửa Lò Nghệ An", "Bãi biển trải dài nước trong xanh nằm gần quê hương Bác Hồ ở Nghệ An có tên là gì?", "Bãi biển Cửa Lò", ["Bãi biển Thiên Cầm", "Bãi biển Nhật Lệ", "Bãi biển Hải Hòa"], "Cửa Lò có đảo Lan Châu và đảo Song Ngư chắn sóng, hải sản mực nhảy nang luộc thơm ngọt tươi rói.", "6-7", 1),
    ("Thành cổ Quảng Trị", "Di tích lịch sử hào hùng bên dòng sông Thạch Hãn chứng kiến cuộc chiến đấu kiên cường 81 ngày đêm năm 1972 là gì?", "Thành cổ Quảng Trị", ["Cố đô Huế", "Thành Nhà Hồ", "Thành Cổ Loa"], "'Đò lên Thạch Hãn ơi... chèo nhẹ / Đáy sông còn đó bạn tôi nằm' nhắc nhở sự hy sinh vô giá của thế hệ cha anh.", "7-8", 2),
    ("Cầu Hiền Lương vĩ tuyến 17", "Cây cầu bắc qua sông Bến Hải (Quảng Trị) từng là giới tuyến quân sự tạm thời chia cắt hai miền Nam - Bắc suốt 20 năm là cầu gì?", "Cầu Hiền Lương", ["Cầu Đắkrông", "Cầu Thạch Hãn", "Cầu Bến Thủy"], "Cầu Hiền Lương hôm nay sơn hai màu xanh - vàng kỷ niệm ngày đất nước nối liền một dải non sông thống nhất.", "7-8", 2),
    ("Thành Nhà Hồ Thanh Hóa", "Công trình thành quách bằng đá độc nhất vô nhị ở Đông Nam Á do Hồ Quý Ly xây dựng năm 1397 là di sản thế giới nào?", "Thành Nhà Hồ (Tây Đô)", ["Thành Cổ Loa", "Thành Thăng Long", "Thành Lam Kinh"], "Các khối đá xanh khổng lồ nặng hàng chục tấn được đẽo gọt vuông vức ghép khít khao không cần vôi vữa.", "8-9", 3),
    ("Khu di tích Lam Kinh", "Vùng đất cội nguồn phát tích cuộc khởi nghĩa Lam Sơn của anh hùng dân tộc Lê Lợi thuộc tỉnh nào?", "Tỉnh Thanh Hóa", ["Tỉnh Nghệ An", "Tỉnh Hà Tĩnh", "Tỉnh Ninh Bình"], "Lam Kinh là nơi an nghỉ của các vị vua triều Hậu Lê với cây ổi cười kỳ lạ và bia Vĩnh Lăng bất hủ.", "8-9", 3),
    ("Làng Sen quê Bác", "Ngôi làng quê nội thanh bình với mái nhà tranh đơn sơ hàng rào râm bụt nơi Bác Hồ kính yêu cất tiếng khóc chào đời là làng nào?", "Làng Sen (Kim Liên, Nam Đàn, Nghệ An)", ["Làng Hoàng Trù", "Làng Chùa", "Làng Vạn Phúc"], "Thăm quê Bác ở Nam Đàn giúp các bạn nhỏ thấu hiểu nếp sống giản dị, thanh bạch của vị lãnh tụ vĩ đại.", "6-7", 1),
    ("Khu di tích Tân Trào", "Thủ đô kháng chiến nơi Bác Hồ và Trung ương Đảng lãnh đạo thành công cuộc Tổng khởi nghĩa Cách mạng Tháng Tám 1945 thuộc tỉnh nào?", "Tân Trào (Tỉnh Tuyên Quang)", ["Pác Bó (Cao Bằng)", "Định Hóa (Thái Nguyên)", "Ba Bể (Bắc Kạn)"], "Cây đa Tân Trào lịch sử là nơi Đại tướng Võ Nguyên Giáp đọc Quân lệnh số 1 xuất quân tiến về giải phóng Hà Nội.", "7-8", 2),
    ("Khu di tích Pác Bó", "Hang đá bên dòng suối Lê-nin trong vắt nơi Bác Hồ trở về Tổ quốc sau 30 năm bôn ba cứu nước năm 1941 thuộc tỉnh nào?", "Pác Bó (Tỉnh Cao Bằng)", ["Tuyên Quang", "Lạng Sơn", "Hà Giang"], "'Sáng ra bờ suối tối vào hang / Cháo bẹ rau măng vẫn sẵn sàng' thể hiện tinh thần lạc quan cách mạng của Bác.", "7-8", 2),
    ("Mỏ than Quảng Ninh", "Vùng đất mỏ giàu tài nguyên khoáng sản than đá lớn nhất cả nước được mệnh danh là 'Vàng đen của Tổ quốc' là tỉnh nào?", "Tỉnh Quảng Ninh", ["Tỉnh Thái Nguyên", "Tỉnh Lạng Sơn", "Tỉnh Bắc Giang"], "Các tầng than đá lộ thiên Cẩm Phả, Hòn Gai cung cấp nhiên liệu cho các nhà máy nhiệt điện và xuất khẩu.", "7-8", 2),
    ("Mỏ bô-xít Tây Nguyên", "Tài nguyên khoáng sản kim loại có trữ lượng khổng lồ ở Đắk Nông và Lâm Đồng dùng để luyện nhôm là quặng gì?", "Quặng Bô-xít (Bauxite)", ["Quặng Sắt", "Quặng Đồng", "Quặng Vàng"], "Công nghiệp alumin và luyện nhôm là ngành kinh tế mũi nhọn đang được đầu tư phát triển tại Tây Nguyên.", "8-9", 3),
    ("Mỏ dầu khí Bạch Hổ", "Mỏ dầu thô lớn ngoài khơi thềm lục địa Vũng Tàu nơi ngọn lửa giàn khoan rực sáng giữa biển khơi là mỏ nào?", "Mỏ Bạch Hổ", ["Mỏ Đại Hùng", "Mỏ Rạng Đông", "Mỏ Sư Tử Đen"], "Ngành dầu khí đóng góp nguồn thu ngân sách quan trọng và khẳng định chủ quyền biển đảo thiêng liêng.", "8-9", 3),
    ("Vùng biển Kiên Giang cá trích", "Tỉnh có ngư trường đánh bắt thủy hải sản lớn nhất nước ta với bờ biển dài và vùng vịnh Thái Lan êm đềm là tỉnh nào?", "Tỉnh Kiên Giang", ["Tỉnh Cà Mau", "Tỉnh Bạc Liêu", "Tỉnh Trà Vinh"], "Đội tàu đánh bắt xa bờ của Kiên Giang cung cấp hàng trăm ngàn tấn tôm cá cho chế biến xuất khẩu.", "7-8", 2),
    ("Vương quốc hoa Sa Đéc", "Làng hoa kiểng truyền thống trăm năm tuổi bên bờ sông Tiền rực rỡ sắc màu phục vụ Tết thuộc tỉnh nào?", "Làng hoa Sa Đéc (Đồng Tháp)", ["Làng hoa Cái Mơn (Bến Tre)", "Làng hoa Mỹ Tho", "Làng hoa Đà Lạt"], "Nông dân Sa Đéc trồng hoa trên các giàn cao ngập nước, người chăm hoa bơi xuồng len lỏi tưới hoa độc đáo.", "7-8", 2),
    ("Vương quốc cây giống Cái Mơn", "Vùng đất nổi tiếng là thủ phủ cung cấp cây giống ăn quả và hoa kiểng lớn nhất miền Tây thuộc tỉnh nào?", "Cái Mơn (Chợ Lách, Bến Tre)", ["Mỹ Tho", "Cần Thơ", "Sóc Trăng"], "Các nghệ nhân Chợ Lách khéo tay uốn ghép nên những cây kiểng hình rồng, phượng tuyệt mỹ xuất khẩu.", "8-9", 3),
    ("Xứ sở dừa sáp Cầu Kè", "Loài dừa đặc sản có cơm dừa dày xốp dẻo quánh như kem bơ, nước dừa sền sệt thơm ngọt thuộc tỉnh nào?", "Dừa sáp Cầu Kè (Trà Vinh)", ["Bến Tre", "Tiền Giang", "Vĩnh Long"], "Dừa sáp Cầu Kè là sản vật quý hiếm đắt đỏ, dầm đường đá sữa là món sinh tố ngon trứ danh.", "8-9", 3),
    ("Măng tây xanh đất cát Ninh Thuận", "Loài rau cao cấp giàu dinh dưỡng phát triển tốt trên vùng đất cát khô hạn đầy nắng gió Phan Rang là gì?", "Măng tây xanh", ["Rau muống", "Cải bắp", "Bí đỏ"], "Măng tây xanh giòn ngọt được mệnh danh là 'hoàng đế của các loài rau' mang lại thu nhập cao cho nông dân.", "7-8", 2),
    ("Nho xanh Ninh Thuận", "Cây ăn quả đặc sản chịu hạn giỏi được trồng giàn bạt ngàn tại Ninh Thuận cho những chùm quả mọng ngọt là cây gì?", "Cây nho", ["Cây táo", "Cây dừa", "Cây xoài"], "Ninh Thuận là thủ phủ nho của Việt Nam với các sản phẩm nho tươi, rượu vang nho và mật nho thanh mát.", "6-7", 1),
    ("Thanh long ruột đỏ Bình Thuận", "Tỉnh dẫn đầu cả nước về diện tích và sản lượng xuất khẩu trái thanh long ngọt mát là tỉnh nào?", "Tỉnh Bình Thuận", ["Tỉnh Ninh Thuận", "Tỉnh Khánh Hòa", "Tỉnh Đồng Nai"], "Vào ban đêm, những cánh đồng thanh long chong hàng triệu bóng đèn vàng rực rỡ như một biển sao lung linh.", "7-8", 2),
    ("Hồ Thác Bà Yên Bái", "Hồ nước nhân tạo khổng lồ hình thành khi ngăn đập xây nhà máy thủy điện Thác Bà đầu tiên ở miền Bắc là hồ gì?", "Hồ Thác Bà", ["Hồ Trị An", "Hồ Đa Nhim", "Hồ Hòa Bình"], "Hồ Thác Bà có hơn 1.300 hòn đảo lớn nhỏ xanh ngắt được ví như 'Vịnh Hạ Long trên núi' của Yên Bái.", "8-9", 3),
    ("Hồ Trị An Đồng Nai", "Hồ thủy điện lớn nhất miền Nam cung cấp nước tưới và nguồn điện dồi dào cho vùng kinh tế trọng điểm phía Nam là hồ gì?", "Hồ Trị An", ["Hồ Dầu Tiếng", "Hồ Thác Mơ", "Hồ Cần Đơn"], "Hồ Trị An được xây dựng trên sông Đồng Nai với sự giúp đỡ chí tình của các chuyên gia Liên Xô.", "8-9", 3),
    ("Hồ Dầu Tiếng Tây Ninh", "Hồ chứa nước thủy lợi ngọt nhân tạo lớn nhất Việt Nam và Đông Nam Á phục vụ nông nghiệp Nam Bộ là hồ nào?", "Hồ Dầu Tiếng", ["Hồ Kẻ Gỗ", "Hồ Núi Cốc", "Hồ Định Bình"], "Hồ Dầu Tiếng tiếp giáp 3 tỉnh Tây Ninh, Bình Dương, Bình Phước tưới tiêu cho hàng trăm ngàn hecta lúa và hoa màu.", "8-9", 3),
    ("Hồ Núi Cốc Thái Nguyên", "Hồ nước thơ mộng gắn liền với truyền thuyết cảm động về tình yêu chung thủy giữa chàng Cốc và nàng Công thuộc tỉnh nào?", "Tỉnh Thái Nguyên", ["Tỉnh Bắc Giang", "Tỉnh Vĩnh Phúc", "Tỉnh Tuyên Quang"], "'Hồ Núi Cốc mang bóng hình chàng Cốc / Nước sông Công chảy lệ của nàng Công' là câu chuyện truyền thuyết đẹp.", "7-8", 2),
    ("Làng gốm Bát Tràng Hà Nội", "Làng nghề gốm sứ truyền thống nổi tiếng hơn 700 năm tuổi nằm ven đê sông Hồng ở ngoại thành Hà Nội là làng gì?", "Làng gốm Bát Tràng", ["Làng lụa Vạn Phúc", "Làng tranh Đông Hồ", "Làng đồng Đại Bái"], "Sản phẩm gốm Bát Tràng tinh xảo với men lam, men rạn độc đáo được ưa chuộng khắp trong và ngoài nước.", "6-7", 1),
    ("Làng lụa Vạn Phúc Hà Đông", "Làng dệt lụa tơ tằm truyền thống lâu đời nức tiếng với những tấm lụa mềm mại mát mịn ở Hà Nội là làng gì?", "Làng lụa Vạn Phúc (Hà Đông)", ["Làng lụa Mã Châu", "Làng lụa Tân Châu", "Làng lụa Nha Xá"], "Lụa Vạn Phúc xưa từng được chọn may y phục cho vua chúa và được đem đi triển lãm quốc tế tại Pháp.", "7-8", 2),
    ("Làng hoa cây cảnh Vị Khê", "Làng nghề trồng hoa và tạo hình cây thế (bonsai) cổ xưa nhất miền Bắc hơn 800 năm tuổi thuộc tỉnh nào?", "Tỉnh Nam Định (Vị Khê)", ["Tỉnh Thái Bình", "Tỉnh Hải Dương", "Tỉnh Hưng Yên"], "Nghệ nhân Vị Khê nổi tiếng với đôi tay tài hoa uốn lượn cây cảnh thành hình rồng bay, phượng múa uy nghi.", "8-9", 3),
    ("Làng làm nón Chuông Hà Nội", "Làng nghề làm nón lá truyền thống phẳng phiu tinh tế nằm bên bờ sông Đáy ở huyện Thanh Oai (Hà Nội) là làng gì?", "Làng Chuông", ["Làng Triều Khúc", "Làng Định Công", "Làng Bát Tràng"], "Chiếc nón lá làng Chuông soi nghiêng vành nón tôn thêm vẻ duyên dáng dịu dàng cho người phụ nữ Việt Nam.", "7-8", 2),
    ("Làng tranh khắc gỗ Đông Hồ", "Làng tranh dân gian nổi tiếng với tranh 'Đám cưới chuột', 'Đánh ghen' in trên giấy điệp thuộc tỉnh nào?", "Làng tranh Đông Hồ (Bắc Ninh)", ["Làng tranh Hàng Trống", "Làng tranh Kim Hoàng", "Làng tranh Sình"], "Tranh Đông Hồ dùng màu tự nhiên từ lá chàm, hoa hòe, than rơm nếp in trên giấy điệp óng ánh vỏ sò.", "7-8", 2)
]

raw_mc.extend(more_mc_dl)

# 14 SA items (DL127 - DL140)
raw_sa = [
    ("Thủ đô nước ta", "Thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là thành phố nào?", "hà nội|thủ đô hà nội", "Hà Nội là thủ đô ngàn năm văn hiến linh thiêng.", "6-7", 1),
    ("Đỉnh núi cao nhất", "Đỉnh núi cao nhất Việt Nam và Đông Nam Dương được mệnh danh là nóc nhà Đông Dương có tên là gì?", "fansipan|phan xi păng", "Fansipan cao 3.143 mét quanh năm mây mù che phủ.", "7-8", 2),
    ("Kỳ quan thiên nhiên thế giới", "Vịnh biển nổi tiếng ở tỉnh Quảng Ninh có hàng ngàn đảo đá vôi được UNESCO công nhận là gì?", "vịnh hạ long|hạ long", "Vịnh Hạ Long là di sản thiên nhiên thế giới tráng lệ.", "6-7", 1),
    ("Sông mẹ miền Bắc", "Con sông lớn chở nặng phù sa đỏ bồi đắp nên đồng bằng Bắc Bộ có tên là gì?", "sông hồng|sông cái", "Sông Hồng bồi đắp phù sa cho vựa lúa miền Bắc.", "6-7", 1),
    ("Sông chín rồng phương Nam", "Dòng sông lớn chia thành 9 cửa sông đổ ra biển bồi đắp nên miền Tây Nam Bộ có tên là gì?", "sông cửu long|cửu long|sông mê kông", "Sông Cửu Long tưới mát cho đồng bằng sông Cửu Long trù phú.", "6-7", 1),
    ("Điểm cực Bắc", "Cột cờ quốc gia trên đỉnh núi Rồng đánh dấu điểm cực Bắc thiêng liêng của Tổ quốc có tên là gì?", "lũng cú|cột cờ lũng cú", "Cột cờ Lũng Cú kiêu hãnh trên đỉnh cao Hà Giang.", "7-8", 2),
    ("Điểm cực Nam", "Điểm cực Nam trên đất liền của Tổ quốc nơi có bãi bồi phù sa thuộc tỉnh nào?", "cà mau|mũi cà mau", "Mũi Cà Mau là điểm cuối đất liền cực Nam Tổ quốc.", "6-7", 1),
    ("Hòn đảo lớn nhất", "Hòn đảo lớn nhất của Việt Nam nằm ở tỉnh Kiên Giang được mệnh danh là Đảo Ngọc là đảo gì?", "phú quốc|đảo phú quốc", "Phú Quốc là hòn đảo ngọc du lịch thiên đường.", "6-7", 1),
    ("Thành phố ngàn hoa", "Thành phố trên cao nguyên Lâm Viên có khí hậu mát mẻ quanh năm và ngàn hoa khoe sắc là thành phố nào?", "đà lạt", "Đà Lạt mộng mơ với sương mù và ngàn hoa tươi tốt.", "6-7", 1),
    ("Hồ nước giữa Hà Nội", "Hồ nước ngọt giữa lòng thủ đô gắn với truyền thuyết trả gươm báu cho Rùa Vàng là hồ gì?", "hồ gươm|hồ hoàn kiếm", "Hồ Gươm là trái tim thân thương của thủ đô Hà Nội.", "6-7", 1),
    ("Động tự nhiên lớn nhất", "Hang động tự nhiên lớn nhất thế giới nằm trong Vườn quốc gia Phong Nha - Kẻ Bàng là hang gì?", "sơn đoòng|hang sơn đoòng", "Hang Sơn Đoòng là kỳ quan hang động vĩ đại của nhân loại.", "8-9", 3),
    ("Thành phố hoa phượng đỏ", "Thành phố cảng biển lớn ở miền Bắc có biểu tượng hoa phượng đỏ rực rỡ là thành phố nào?", "hải phòng", "Hải Phòng là thành phố cảng hoa phượng đỏ anh hùng.", "6-7", 1),
    ("Hình dáng bản đồ Việt Nam", "Đất nước Việt Nam trên bản đồ địa lý thế giới có hình dáng giống chữ cái nào?", "chữ s|s", "Bản đồ Việt Nam uốn lượn hình chữ S thân thương.", "6-7", 1),
    ("Vùng đất cồng chiêng", "Vùng cao nguyên đất đỏ bazan bạt ngàn cà phê và văn hóa cồng chiêng có tên gọi là gì?", "tây nguyên", "Tây Nguyên đại ngàn hùng vĩ với âm vang cồng chiêng.", "7-8", 2)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"DL{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Địa Lý Việt Nam",
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
    qid = f"DL{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Địa Lý Việt Nam",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/dl_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Cập nhật DL hoàn tất: {len(questions)} câu đã được ghi vào dl_140.json")

# Bổ sung 20 câu MC còn thiếu cho DL
extra_dl_20 = [
    ("Thành phố hoa Đà Lạt", "Đà Lạt thuộc tỉnh nào của vùng đất Tây Nguyên?", "Tỉnh Lâm Đồng", ["Tỉnh Đắk Lắk", "Tỉnh Gia Lai", "Tỉnh Kon Tum"], "Đà Lạt nằm trên cao nguyên Lâm Viên có độ cao 1.500m so với mực nước biển.", "6-7", 1),
    ("Thành phố biển Vũng Tàu", "Thành phố biển nghỉ mát gần TP Hồ Chí Minh nhất có tượng Chúa Kito giang tay trên đỉnh núi Nhỏ là gì?", "Thành phố Vũng Tàu", ["Thành phố Phan Thiết", "Thành phố Rạch Giá", "Thành phố Hà Tiên"], "Vũng Tàu có Bãi Trước và Bãi Sau đón hàng triệu du khách đến tắm biển mỗi dịp cuối tuần.", "6-7", 1),
    ("Bán đảo Sơn Trà lá phổi xanh Đà Nẵng", "Bán đảo nhô ra biển ở Đà Nẵng có chùa Linh Ứng tượng Phật Bà cao 67m và loài voọc chà vá chân nâu quý hiếm là gì?", "Bán đảo Sơn Trà", ["Bán đảo Cam Ranh", "Bán đảo Đầm Môn", "Bán đảo Phương Mai"], "Sơn Trà như bức bình phong khổng lồ che chở gió bão từ biển Đông cho thành phố Đà Nẵng.", "7-8", 2),
    ("Cố đô Hoa Lư ngàn năm", "Kinh đô đầu tiên của nhà nước phong kiến tập quyền Đại Cồ Việt thời vua Đinh Tiên Hoàng đóng tại đâu?", "Hoa Lư (Ninh Bình)", ["Cổ Loa (Đông Anh)", "Thăng Long (Hà Nội)", "Lam Kinh (Thanh Hóa)"], "Hoa Lư có thế núi non hiểm trở như bức tường thành tự nhiên bảo vệ nền độc lập dân tộc non trẻ.", "7-8", 2),
    ("Đền Hùng đất tổ Phú Thọ", "Khu di tích lịch sử Đền Hùng nơi thờ phụng các vị Vua Hùng dựng nước Văn Lang nằm trên ngọn núi nào?", "Núi Nghĩa Lĩnh (Phú Thọ)", ["Núi Ba Vì", "Núi Yên Tử", "Núi Sóc"], "Hàng năm vào dịp Giỗ Tổ mùng 10 tháng 3 âm lịch, hàng triệu đồng bào từ khắp nơi về trẩy hội Đền Hùng.", "6-7", 1),
    ("Thành phố ngã ba sông Việt Trì", "Thành phố trung tâm của tỉnh Phú Thọ nằm tại ngã ba nơi sông Hồng, sông Đà và sông Lô hợp lưu là gì?", "Thành phố Việt Trì", ["Thành phố Vĩnh Yên", "Thành phố Tuyên Quang", "Thành phố Yên Bái"], "Bến Bạch Hạc ở ngã ba sông Việt Trì gắn liền với nhiều huyền tích lịch sử thời dựng nước của dân tộc.", "7-8", 2),
    ("Thành phố chè Thái Nguyên", "Thành phố công nghiệp luyện kim và thủ phủ chè búp nổi tiếng ở vùng trung du miền núi Bắc Bộ là gì?", "Thành phố Thái Nguyên", ["Thành phố Bắc Kạn", "Thành phố Cao Bằng", "Thành phố Lạng Sơn"], "Thái Nguyên có Đại học Thái Nguyên là trung tâm đào tạo nhân lực lớn cho các tỉnh miền núi phía Bắc.", "7-8", 2),
    ("Núi Côn Sơn Chí Linh", "Khu di tích danh thắng Côn Sơn - Kiếp Bạc gắn liền với danh nhân văn hóa thế giới Nguyễn Trãi thuộc tỉnh nào?", "Tỉnh Hải Dương", ["Tỉnh Hưng Yên", "Tỉnh Bắc Ninh", "Tỉnh Quảng Ninh"], "'Côn Sơn suối chảy rì rầm / Ta nghe như tiếng đàn cầm bên tai' là những vần thơ thanh nhã của Nguyễn Trãi.", "7-8", 2),
    ("Đền Kiếp Bạc thờ Trần Hưng Đạo", "Khu đền Kiếp Bạc nằm bên bờ sông Lục Đầu linh thiêng là nơi thờ vị anh hùng dân tộc vĩ đại nào?", "Hưng Đạo Đại Vương Trần Quốc Tuấn", ["Vua Quang Trung", "Vua Lê Lợi", "Lý Thường Kiệt"], "Lễ hội quân trên sông Lục Đầu hàng năm tái hiện hào khí Đông A oanh liệt của quân dân nhà Trần đánh giặc.", "8-9", 3),
    ("Chùa Tam Chúc lớn nhất thế giới", "Ngôi chùa khổng lồ tựa lưng vào núi Thất Tinh hướng ra hồ Lục Nhạc thơ mộng thuộc tỉnh nào?", "Tỉnh Hà Nam (Tam Chúc)", ["Tỉnh Nam Định", "Tỉnh Ninh Bình", "Tỉnh Thái Bình"], "Quần thể chùa Tam Chúc là địa điểm tổ chức Đại lễ Phật đản Liên Hợp Quốc Vesak 2019 thành công rực rỡ.", "7-8", 2),
    ("Làng nón Phú Gia Bình Định", "Làng nghề làm nón ngựa truyền thống tinh xảo bằng lá kè và ống giang bền đẹp nổi tiếng thuộc tỉnh nào?", "Tỉnh Bình Định (Phú Gia)", ["Tỉnh Quảng Nam", "Tỉnh Quảng Ngãi", "Tỉnh Thừa Thiên Huế"], "Nón ngựa Phú Gia xưa kia chuyên dùng cho các bậc quan lại và tướng lĩnh cưỡi ngựa thao diễn võ nghệ.", "8-9", 3),
    ("Làng rèn Đa Sỹ Hà Nội", "Làng nghề rèn dao kéo truyền thống hàng trăm năm nổi tiếng sắc bén bằng thép nhíp xe thuộc quận nào ở Hà Nội?", "Quận Hà Đông (Đa Sỹ)", ["Huyện Đông Anh", "Huyện Gia Lâm", "Quận Hoàng Mai"], "Tiếng búa đe quai nhịp nhàng đỏ lửa ngày đêm của làng rèn Đa Sỹ tạo nên những dụng cụ làm bếp tuyệt hảo.", "7-8", 2),
    ("Làng quạt Chàng Sơn Thạch Thất", "Làng nghề làm quạt nan tre, quạt giấy và quạt tranh nghệ thuật tinh tế nổi tiếng ở Hà Nội là gì?", "Làng quạt Chàng Sơn", ["Làng tranh Đông Hồ", "Làng gốm Bát Tràng", "Làng nón Chuông"], "Chiếc quạt giấy Chàng Sơn từng bay sang Pháp dự triển lãm thế giới từ thế kỷ 19 làm rạng danh nghề thủ công Việt.", "8-9", 3),
    ("Làng chuông đồng Đại Bái", "Làng nghề đúc đồng truyền thống đúc tượng Phật, chuông đồng, đỉnh đồng nổi tiếng thuộc tỉnh nào?", "Tỉnh Bắc Ninh (Đại Bái)", ["Tỉnh Hưng Yên", "Tỉnh Hải Dương", "Tỉnh Vĩnh Phúc"], "Đồng Đại Bái đúc tinh xảo, tiếng chuông đồng ngân vang trong trẻo khắp các đình chùa linh thiêng.", "8-9", 3),
    ("Làng đá mỹ nghệ Non Nước", "Làng nghề điêu khắc tượng đá nghệ thuật dưới chân danh thắng Ngũ Hành Sơn thuộc thành phố nào?", "Thành phố Đà Nẵng", ["Thành phố Huế", "Thành phố Tam Kỳ", "Thành phố Hội An"], "Các nghệ nhân tài hoa biến những khối đá cẩm thạch thô ráp thành những pho tượng Phật và linh vật sống động.", "7-8", 2),
    ("Cây cầu Rồng phun lửa nước", "Cây cầu hình con rồng thép vươn ra biển Đông biết phun lửa và phun nước vào tối cuối tuần ở Đà Nẵng là cầu gì?", "Cầu Rồng", ["Cầu Thuận Phước", "Cầu Trần Thị Lý", "Cầu Tiên Sơn"], "Cầu Rồng là biểu tượng khát vọng vươn mình mạnh mẽ của thành phố đáng sống nhất Việt Nam.", "6-7", 1),
    ("Vịnh Lăng Cô vịnh đẹp thế giới", "Vịnh biển êm đềm với bờ cát trắng mịn thoai thoải nằm dưới chân đèo Hải Vân thuộc tỉnh nào?", "Tỉnh Thừa Thiên Huế (Lăng Cô)", ["Tỉnh Quảng Nam", "Thành phố Đà Nẵng", "Tỉnh Quảng Bình"], "Vịnh Lăng Cô được bình chọn là một trong những vịnh biển đẹp nhất thế giới với đầm Lập An thơ mộng kề bên.", "7-8", 2),
    ("Suối khoáng nóng Bang Quảng Bình", "Dòng suối khoáng nóng tự nhiên có độ sôi lộ thiên lên tới 105 độ C kỷ lục Việt Nam là suối gì?", "Suối khoáng nóng Bang", ["Suối khoáng Kim Bôi", "Suối khoáng Bình Châu", "Suối khoáng Kênh Gà"], "Du khách có thể luộc chín trứng gà thơm ngon ngay tại các mạch nước nóng phun trào lộ thiên giữa rừng nguyên sinh.", "8-9", 3),
    ("Cố đô Lam Kinh Thanh Hóa", "Vùng đất phát tích cuộc khởi nghĩa Lam Sơn chống giặc Minh xâm lược thế kỷ 15 do ai lãnh đạo?", "Bình Định Vương Lê Lợi", ["Hưng Đạo Vương Trần Quốc Tuấn", "Quang Trung Nguyễn Huệ", "Ngô Quyền"], "Khởi nghĩa Lam Sơn toàn thắng, Lê Lợi lên ngôi vua lập ra triều đại Hậu Lê rực rỡ trong lịch sử nước nhà.", "7-8", 2),
    ("Thành phố hoa sen Đồng Tháp", "Thành phố Cao Lãnh thủ phủ của tỉnh Đồng Tháp nổi tiếng với di tích lăng mộ của ai là thân sinh Chủ tịch Hồ Chí Minh?", "Cụ Phó bảng Nguyễn Sinh Sắc", ["Cụ Phan Bội Châu", "Cụ Huỳnh Thúc Kháng", "Cụ Nguyễn Đình Chiểu"], "Khu di tích cụ Phó bảng Nguyễn Sinh Sắc tại Cao Lãnh là địa chỉ đỏ giáo dục truyền thống hiếu học và lòng yêu nước.", "7-8", 2)
]

raw_mc.extend(extra_dl_20)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"DL{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Địa Lý Việt Nam",
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
    qid = f"DL{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Địa Lý Việt Nam",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/dl_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành DL: {len(questions)} câu đã được ghi vào dl_140.json")
