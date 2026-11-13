# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1555400038-63f5ba517a47?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1582650625119-3a31f841839d?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=600&auto=format&fit=crop&q=80"
]

# 126 MC items
raw_mc = [
    # 1-35 Cội nguồn, Truyền thuyết & Thời dựng nước
    ("Nguồn gốc con Rồng cháu Tiên", "Theo truyền thuyết dân gian, tổ tiên của người Việt Nam gắn liền với cuộc hôn nhân thiêng liêng của ai?", "Lạc Long Quân và mẹ Âu Cơ (Bọc trăm trứng)", ["Sơn Tinh và Thủy Tinh", "An Dương Vương và Mị Châu", "Thánh Gióng và mẹ"], "Mẹ Âu Cơ sinh ra bọc trăm trứng nở thành trăm người con, 50 con theo cha xuống biển, 50 con theo mẹ lên núi chia nhau cai quản đất nước.", "6-7", 1),
    ("Nhà nước đầu tiên Văn Lang", "Vị vua đầu tiên lập nên nhà nước Văn Lang - nhà nước đầu tiên trong lịch sử dân tộc Việt Nam là ai?", "Vua Hùng (Hùng Vương thứ nhất)", ["An Dương Vương", "Vua Lý Thái Tổ", "Vua Đinh Tiên Hoàng"], "Các Vua Hùng đóng đô tại Phong Châu (Phú Thọ), dạy dân cấy lúa nước, săn bắn và đặt tên nước là Văn Lang.", "6-7", 1),
    ("Ngày Giỗ Tổ Hùng Vương", "Ngày lễ quốc gia thiêng liêng tưởng nhớ công ơn dựng nước của các Vua Hùng được tổ chức vào ngày nào hàng năm?", "Ngày mùng 10 tháng 3 âm lịch", ["Ngày 2 tháng 9", "Ngày 1 tháng 1 âm lịch", "Ngày 30 tháng 4"], "'Dù ai đi ngược về xuôi / Nhớ ngày Giỗ Tổ mùng mười tháng ba' là lời nhắc nhở đạo lý uống nước nhớ nguồn sâu sắc.", "6-7", 1),
    ("Sự tích Bánh chưng bánh giầy", "Người con trai thứ 18 của Vua Hùng nhờ tấm lòng hiếu thảo và sáng tạo ra bánh chưng, bánh giầy được truyền ngôi báu là ai?", "Hoàng tử Lang Liêu", ["Mai An Tiêm", "Thạch Sanh", "Chử Đồng Tử"], "Bánh chưng hình vuông tượng trưng cho Đất, bánh giầy hình tròn tượng trưng cho Trời làm từ hạt gạo nếp thơm nuôi sống con người.", "6-7", 1),
    ("Truyền thuyết Thánh Gióng", "Người anh hùng làng Phù Đổng lên ba tuổi không biết nói cười, bỗng vươn vai thành tráng sĩ cưỡi ngựa sắt dẹp giặc Ân là ai?", "Thánh Gióng (Phù Đổng Thiên Vương)", ["Trần Quốc Toản", "Kim Đồng", "Lê Văn Tám"], "Thánh Gióng nhổ từng bụi tre đằng ngà quất tan tác quân thù, sau khi dẹp xong giặc thì cưỡi ngựa bay thẳng lên đỉnh núi Sóc về trời.", "6-7", 1),
    ("Sự tích quả dưa hấu", "Chàng hoàng tử nuôi chí kiên cường bị đày ra đảo hoang đã gieo trồng nên giống dưa hấu ngọt lành là ai?", "Mai An Tiêm", ["Lang Liêu", "Thạch Sanh", "Trương Ba"], "Mai An Tiêm với câu nói nổi tiếng 'Của biếu là của lo, của cho là của nợ' khẳng định sức lao động tự lực cánh sinh của con người.", "6-7", 1),
    ("Sơn Tinh Thủy Tinh dâng nước", "Vị thần núi Tản Viên có phép dời non lấp biển, đánh thắng thần nước Thủy Tinh giành được nàng công chúa Mị Nương là ai?", "Sơn Tinh (Thần Núi Tản Viên)", ["Thủy Tinh", "Thần Kim Quy", "Thần Gió"], "Cuộc chiến Sơn Tinh - Thủy Tinh phản ánh khát vọng và ý chí kiên cường đắp đê ngăn lũ lụt trị thủy của tổ tiên người Việt ngàn đời.", "6-7", 1),
    ("Thành Cổ Loa hình xoáy ốc", "Vị vua nối tiếp thời Hùng Vương đổi tên nước thành Âu Lạc và cho xây tòa thành Cổ Loa hình xoáy trôn ốc kiên cố là ai?", "An Dương Vương (Thục Phán)", ["Vua Hùng Vương", "Triệu Đà", "Lý Nam Đế"], "Thành Cổ Loa có 9 vòng xoáy ốc thành cao hào sâu, được thần Kim Quy trao tặng chiếc móng rùa làm lẫy nỏ thần bắn một phát trăm phát trúng.", "7-8", 2),
    ("Trống đồng Đông Sơn đỉnh cao", "Hiện vật khảo cổ học bằng đồng tiêu biểu nhất cho thời kỳ văn hóa Đông Sơn rực rỡ thời Hùng Vương - An Dương Vương là gì?", "Trống đồng Đông Sơn (như Trống đồng Ngọc Lũ)", ["Chuông đồng", "Tượng Phật bằng đồng", "Thạp gốm"], "Mặt trống đồng khắc họa hình ảnh Mặt Trời ở tâm, xung quanh là cảnh người giã gạo, múa cờ, chèo thuyền phản ánh đời sống nông nghiệp phồn vinh.", "7-8", 2),
    ("Hai Bà Trưng phất cờ khởi nghĩa", "Hai nữ anh hùng dân tộc đầu tiên cưỡi voi ra trận đánh đuổi thái thú Tô Định nhà Đông Hán năm 40 sau Công nguyên là ai?", "Trưng Trắc và Trưng Nhị (Hai Bà Trưng)", ["Bà Triệu", "Bùi Thị Xuân", "Nguyễn Thị Định"], "Hai Bà Trưng phất cờ khởi nghĩa tại cửa sông Hát Môn với lời thề: 'Một xin rửa sạch nước thù / Hai xin dựng lại nghiệp xưa họ Hùng'.", "6-7", 1),
    ("Bà Triệu cưỡi voi đánh cống", "Nữ tướng anh hùng ở Thanh Hóa từng tuyên bố 'Tôi muốn cưỡi cơn gió mạnh, đạp luồng sóng dữ, chém cá kình ở biển Đông' là ai?", "Bà Triệu (Triệu Thị Trinh)", ["Trưng Trắc", "Dương Vân Nga", "Lê Chân"], "Bà Triệu cưỡi voi trắng một ngà xung trận khiến quân giặc Ngô khiếp sợ thốt lên: 'Vung tay đánh cọp dễ, giáp mặt vua Bà khó'.", "7-8", 2),
    ("Ngô Quyền chiến thắng Bạch Đằng", "Năm 938, vị anh hùng dân tộc nào đã dùng kế cắm cọc gỗ bịt sắt trên sông Bạch Đằng đánh tan quân Nam Hán, mở ra kỷ nguyên độc lập?", "Ngô Quyền", ["Đinh Bộ Lĩnh", "Lê Hoàn", "Lý Thường Kiệt"], "Chiến thắng Bạch Đằng năm 938 đã chấm dứt hơn 1.000 năm Bắc thuộc đen tối, khẳng định chủ quyền độc lập muôn đời của non sông đất Việt.", "6-7", 1),
    ("Đinh Bộ Lĩnh cờ lau tập trận", "Cậu bé chăn trâu thông minh ở Hoa Lư lấy bông lau làm cờ tập trận, sau này dẹp loạn 12 sứ quân thống nhất đất nước lên ngôi hoàng đế là ai?", "Đinh Bộ Lĩnh (Đinh Tiên Hoàng)", ["Lê Đại Hành", "Lý Công Uẩn", "Trần Thủ Độ"], "Năm 968, Đinh Bộ Lĩnh lên ngôi Hoàng đế đặt tên nước là Đại Cồ Việt, dời đô về Hoa Lư xây cung điện đúc tiền đồng đầu tiên.", "6-7", 1),
    ("Lê Hoàn phá quân Tống", "Vị tướng tài ba được Thái hậu Dương Vân Nga trao áo long bào lãnh đạo quân dân đánh thắng quân Tống trên sông Bạch Đằng năm 981 là ai?", "Lê Hoàn (Vua Lê Đại Hành)", ["Đinh Phế Đế", "Lý Thái Tổ", "Trần Hưng Đạo"], "Vua Lê Đại Hành còn là vị vua đầu tiên đích thân xuống ruộng cày cấy trong lễ hội Tịch điền đầu xuân khuyến khích nông nghiệp.", "7-8", 2),
    ("Lý Thái Tổ dời đô về Thăng Long", "Năm 1010, vị vua anh minh nào nhìn thấy hình ảnh rồng vàng bay lên nên đã quyết định dời đô từ Hoa Lư về thành Đại La đổi tên là Thăng Long?", "Vua Lý Thái Tổ (Lý Công Uẩn)", ["Vua Lý Nhân Tông", "Vua Lý Thánh Tông", "Vua Trần Thái Tông"], "Chiếu dời đô của Lý Thái Tổ khẳng định Thăng Long là 'chốn hội tụ trọng yếu của bốn phương đất nước, muôn đời là kinh đô bậc nhất'.", "7-8", 2),
    ("Lý Thường Kiệt và bài thơ thần", "Bài thơ 'Nam quốc sơn hà' được xem là bản Tuyên ngôn Độc lập đầu tiên của nước ta vang lên trên phòng tuyến sông Như Nguyệt của ai?", "Lý Thường Kiệt", ["Nguyễn Trãi", "Trần Hưng Đạo", "Quang Trung"], "'Nam quốc sơn hà Nam đế cư / Tiệt nhiên định phận tại thiên thư / Như hà nghịch lỗ lai xâm phạm / Nhữ đẳng hành khan thủ bại hư'.", "7-8", 2),
    ("Văn Miếu - Quốc Tử Giám", "Trường đại học đầu tiên của Việt Nam được xây dựng dưới thời nhà Lý vào năm 1076 tại kinh thành Thăng Long là gì?", "Quốc Tử Giám (Văn Miếu)", ["Trường Bưởi", "Trường Quốc Học Huế", "Trường Đông Kinh Nghĩa Thục"], "Văn Miếu thờ Khổng Tử và Quốc Tử Giám đào tạo hàng ngàn bậc hiền tài đỗ đạt tiến sĩ phụng sự giang sơn xã tắc.", "6-7", 1),
    ("Bia Tiến sĩ Văn Miếu", "82 tấm bia đá đặt trên lưng rùa đá trong Văn Miếu - Quốc Tử Giám khắc tên các bậc tiến sĩ mang ý nghĩa gì?", "Tôn vinh truyền thống hiếu học và trọng dụng người hiền tài của dân tộc", ["Để trang trí sân đình", "Làm ghế ngồi", "Đếm số rùa đá"], "Thân nhân Trung từng khắc trên bia: 'Hiền tài là nguyên khí của quốc gia, nguyên khí thịnh thì thế nước mạnh, nguyên khí suy thì thế nước yếu'.", "8-9", 3),
    ("Nhà Trần 3 lần đại phá Nguyên Mông", "Dưới sự lãnh đạo của vua tôi nhà Trần và Hưng Đạo Đại Vương, quân dân Đại Việt đã lập nên kỳ tích hiển hách nào?", "Ba lần đánh thắng đội quân xâm lược Nguyên Mông hùng mạnh nhất thế giới", ["Mở rộng lãnh thổ sang phương Tây", "Xây dựng Vạn Lý Trường Thành", "Chế tạo tàu hỏa"], "Chiến thắng Đông Bộ Đầu, Hàm Tử, Chương Dương, Vạn Kiếp và Bạch Đằng 1288 làm rạng rỡ hào khí Đông A bất khuất.", "7-8", 2),
    ("Trần Hưng Đạo Hịch tướng sĩ", "Vị Đại Vương kiệt xuất với câu nói đanh thép trước vua Trần: 'Nếu bệ hạ muốn hàng, xin hãy chém đầu thần trước đã' là ai?", "Trần Hưng Đạo (Trần Quốc Tuấn)", ["Trần Thủ Độ", "Trần Quang Khải", "Trần Khánh Dư"], "Trần Quốc Tuấn soạn 'Hịch tướng sĩ' khơi dậy lòng yêu nước nồng nàn và tinh thần quyết chiến quyết thắng của toàn quân.", "7-8", 2),
    ("Hội nghị Diên Hồng ý Đảng lòng dân", "Hội nghị đoàn kết toàn dân do Thượng hoàng Trần Thánh Tông triệu tập các bô lão cả nước tại kinh thành Thăng Long năm 1284 hỏi về kế sách đánh giặc?", "Hội nghị Diên Hồng (Muôn người đồng thanh hô vang: ĐÁNH!)", ["Hội nghị Bình Than", "Hội thi Đình", "Hội thề Lũng Nhai"], "Hội nghị Diên Hồng là biểu tượng sáng ngời cho tinh thần dân chủ và sức mạnh đại đoàn kết toàn dân tộc khi Tổ quốc lâm nguy.", "8-9", 3),
    ("Trần Quốc Toản bóp nát quả cam", "Người thiếu niên anh hùng vì chưa đủ tuổi dự hội nghị Bình Than đã uất ức bóp nát quả cam trong tay, thêu cờ 6 chữ vàng là ai?", "Trần Quốc Toản", ["Kim Đồng", "Lê Văn Tám", "Võ Thị Sáu"], "Lá cờ 'Phá cường địch, báo hoàng ân' của Trần Quốc Toản tung bay chỉ huy đội quân dũng cảm lập nhiều chiến công hiển hách.", "6-7", 1),
    ("Thầy giáo Chu Văn An", "Vị danh sư mẫu mực của muôn đời học trò Việt Nam, từng dâng 'Thất trảm sớ' xin chém 7 tên nịnh thần là ai?", "Thầy giáo Chu Văn An", ["Nguyễn Bỉnh Khiêm", "Lê Quý Đôn", "Lương Thế Vinh"], "Thầy Chu Văn An được thờ trang trọng trong Văn Miếu - Quốc Tử Giám, là tấm gương sáng ngời về đạo đức liêm khiết và lòng cương trực.", "8-9", 3),
    ("Lê Lợi khởi nghĩa Lam Sơn", "Vị chủ tướng nông dân áo vải dấy binh khởi nghĩa tại vùng núi Lam Sơn (Thanh Hóa) ròng rã 10 năm đánh đuổi quân Minh là ai?", "Lê Lợi (Vua Lê Thái Tổ)", ["Nguyễn Trãi", "Lê Lai", "Trần Nguyên Hãn"], "Hội thề Lũng Nhai năm 1416 gắn kết 19 tướng lĩnh cùng đồng lòng chung sức cứu nước, lập nên triều đại Hậu Lê.", "7-8", 2),
    ("Lê Lai liều mình cứu chúa", "Vị tướng dũng cảm mặc áo ngự bào của Lê Lợi chỉ huy toán quân cảm tử xông ra ngoài nghi binh để cứu chủ tướng thoát khỏi vòng vây giặc là ai?", "Lê Lai", ["Lê Khôi", "Lê Sát", "Đinh Liệt"], "Hành động hy sinh quả cảm của Lê Lai giúp bảo toàn lực lượng nghĩa quân, dân gian có câu 'Hai mốt Lê Lai, hai hai Lê Lợi' tưởng nhớ ngày giỗ.", "8-9", 3),
    ("Nguyễn Trãi Bình Ngô đại cáo", "Danh nhân văn hóa thế giới, quân sư tài ba viết nên bản 'Bình Ngô đại cáo' - bản Tuyên ngôn Độc lập thứ hai của nước ta là ai?", "Nguyễn Trãi (Hiệu Ức Trai)", ["Lê Lợi", "Nguyễn Du", "Cao Bá Quát"], "'Đem đại nghĩa để thắng hung tàn / Lấy chí nhân để thay cường bạo' là tư tưởng nhân nghĩa cao cả ngời sáng muôn đời của Nguyễn Trãi.", "8-9", 3),
    ("Sự tích Hồ Hoàn Kiếm", "Sau khi đánh tan quân Minh giặc nước thanh bình, vua Lê Lợi ngự thuyền trên hồ Tả Vọng đã trả lại thanh gươm báu cho ai?", "Rùa Vàng (Thần Kim Quy) nên hồ đổi tên thành Hồ Hoàn Kiếm", ["Cá chép vàng", "Rồng vàng", "Giao long"], "Thanh gươm 'Thuận Thiên' hoàn trả cho thần Kim Quy thể hiện khát vọng hòa bình muôn thuở của dân tộc Việt Nam.", "6-7", 1),
    ("Vua Quang Trung hành quân thần tốc", "Vị hoàng đế áo vải Tây Sơn hành quân thần tốc ra Bắc đánh tan 29 vạn quân Mãn Thanh xâm lược dịp Tết Kỷ Dậu 1789 là ai?", "Quang Trung (Nguyễn Huệ)", ["Nguyễn Nhạc", "Nguyễn Lữ", "Ngô Thì Nhậm"], "Chiến thắng Ngọc Hồi - Đống Đa mùng 5 Tết Kỷ Dậu 1789 vang dội non sông, bảo vệ vững chắc nền độc lập bờ cõi.", "7-8", 2),
    ("Cành đào báo tin thắng trận", "Sau chiến thắng Ngọc Hồi - Đống Đa vang dội, vua Quang Trung sai người phi ngựa hỏa tốc mang cành đào thắm vào Phú Xuân tặng cho ai?", "Công chúa Ngọc Hân (Hoàng hậu)", ["Mẹ của vua", "Tướng Ngô Văn Sở", "Nhân dân thành Huế"], "Cành đào Nhật Tân rực rỡ tươi thắm gửi tặng người vợ hiền là cử chỉ tình cảm lãng mạn tuyệt đẹp của vị anh hùng dân tộc.", "7-8", 2),
    ("Bác Hồ tìm đường cứu nước", "Người thanh niên yêu nước Nguyễn Tất Thành (Bác Hồ) rời bến cảng Nhà Rồng ra đi tìm đường cứu nước vào ngày tháng năm nào?", "Ngày 5 tháng 6 năm 1911", ["Ngày 2 tháng 9 năm 1945", "Ngày 19 tháng 5 năm 1890", "Ngày 30 tháng 4 năm 1975"], "Trên con tàu Amiral Latouche-Tréville với tên gọi Văn Ba làm phụ bếp, Người đã bôn ba khắp năm châu bốn biển tìm ra con đường cứu nước cho dân tộc.", "7-8", 2),
    ("Tuyên ngôn Độc lập ngày 2/9/1945", "Tại Quảng trường Ba Đình lịch sử, Chủ tịch Hồ Chí Minh đã đọc bản Tuyên ngôn Độc lập khai sinh ra nước Việt Nam vào ngày nào?", "Ngày 2 tháng 9 năm 1945 (Ngày Quốc khánh)", ["Ngày 19 tháng 8", "Ngày 30 tháng 4", "Ngày 1 tháng 1"], "'Nước Việt Nam có quyền hưởng tự do và độc lập, và sự thật đã thành một nước tự do, độc lập!' vang vọng non sông.", "6-7", 1),
    ("Chiến thắng Điện Biên Phủ 1954", "Chiến thắng lịch sử 'Lừng lẫy năm châu, chấn động địa cầu' kết thúc cuộc kháng chiến chống thực dân Pháp diễn ra vào ngày nào?", "Ngày 7 tháng 5 năm 1954", ["Ngày 30 tháng 4 năm 1975", "Ngày 2 tháng 9 năm 1945", "Ngày 19 tháng 12 năm 1946"], "Lá cờ 'Quyết chiến Quyết thắng' tung bay trên nóc hầm tướng De Castries đánh dấu mốc son chói lọi trong lịch sử dân tộc.", "7-8", 2),
    ("Đại tướng Võ Nguyên Giáp", "Vị Tổng tư lệnh Quân đội Nhân dân Việt Nam, người anh cả của quân đội, chỉ huy chiến dịch Điện Biên Phủ toàn thắng là ai?", "Đại tướng Võ Nguyên Giáp", ["Đại tướng Văn Tiến Dũng", "Đại tướng Nguyễn Chí Thanh", "Thượng tướng Chu Huy Mân"], "Đại tướng Võ Nguyên Giáp là một trong những danh tướng vĩ đại kiệt xuất nhất của lịch sử quân sự thế giới thế kỷ 20.", "7-8", 2),
    ("Ngày Giải phóng miền Nam 30/4/1975", "Ngày lịch sử non sông nối liền một dải, đất nước Việt Nam hoàn toàn thống nhất hòa bình độc lập là ngày nào?", "Ngày 30 tháng 4 năm 1975", ["Ngày 2 tháng 9", "Ngày 1 tháng 5", "Ngày 19 tháng 8"], "Chiếc xe tăng 390 húc đổ cánh cổng Dinh Độc Lập lúc 11 giờ 30 phút trưa ngày 30/4/1975 khép lại cuộc kháng chiến chống Mỹ cứu nước.", "6-7", 1),
    ("Quốc kỳ Việt Nam", "Lá cờ đỏ sao vàng thiêng liêng của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam có ý nghĩa biểu tượng nào?", "Nền đỏ tượng trưng cho máu cách mạng và nhiệt huyết, ngôi sao vàng 5 cánh tượng trưng cho 5 tầng lớp nhân dân đoàn kết", ["Chỉ để trang trí đẹp", "Tượng trưng cho Mặt Trời", "Màu cờ của các nước"], "Năm cánh sao vàng đại diện cho sĩ, nông, công, thương, binh cùng đoàn kết xây dựng và bảo vệ đất nước phồn vinh.", "6-7", 1)
]

# Thêm 91 câu MC nữa để đủ 126 câu MC
more_mc_ls = [
    ("Quốc ca Việt Nam", "Bài hát Quốc ca hùng tráng của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là bài hát nào do nhạc sĩ Văn Cao sáng tác?", "Bài hát 'Tiến quân ca'", ["Bài hát 'Như có Bác trong ngày đại thắng'", "Bài hát 'Đoàn vệ quốc quân'", "Bài hát 'Mùa xuân trên thành phố Hồ Chí Minh'"], "'Đoàn quân Việt Nam đi / Chung lòng cứu quốc / Bước chân dồn vang trên đường gập ghềnh xa...' vang lên trang nghiêm trong lễ chào cờ.", "6-7", 1),
    ("Quốc huy Việt Nam", "Biểu tượng Quốc huy nước Cộng hòa Xã hội Chủ nghĩa Việt Nam có hình ngôi sao vàng ở giữa được bao bọc bởi những hình ảnh nào?", "Bông lúa vàng hai bên và bánh xe răng công nghiệp ở dưới", ["Hai khẩu súng trường", "Hai con rồng bay", "Hai bông hoa sen"], "Bông lúa vàng và bánh xe răng tượng trưng cho khối liên minh công nông vững chắc lãnh đạo cách mạng.", "7-8", 2),
    ("Kim Đồng người anh hùng nhỏ tuổi", "Người đội trưởng đầu tiên của Đội Thiếu niên Tiền phong Hồ Chí Minh hy sinh anh dũng khi làm nhiệm vụ giao liên là ai?", "Anh Kim Đồng (Nông Văn Dền)", ["Lê Văn Tám", "Vừ A Dính", "Kpa Klơng"], "Anh Kim Đồng nhanh trí đánh lạc hướng quân giặc để bảo vệ cán bộ cách mạng thoát hiểm an toàn bên bờ suối Lê-nin.", "6-7", 1),
    ("Nữ anh hùng Võ Thị Sáu", "Người con gái Đất Đỏ kiên cường trước mũi súng quân thù vẫn hiên ngang cài hoa lê-ki-ma lên tóc và hát vang bài Quốc tế ca là ai?", "Chị Võ Thị Sáu", ["Chị Mười Hai", "Chị Út Tịch", "Chị Nguyễn Thị Minh Khai"], "Chị Võ Thị Sáu ngã xuống trên mảnh đất Côn Đảo khi mới 19 tuổi, trở thành tấm gương bất tử của tuổi trẻ Việt Nam anh hùng.", "6-7", 1),
    ("Anh hùng Vừ A Dính", "Người thiếu niên dân tộc H'Mông dũng cảm làm liên lạc cho bộ đội, kiên quyết không khai dù bị giặc tra tấn dã man là ai?", "Vừ A Dính", ["Kim Đồng", "Lý Tự Trọng", "Bế Văn Đàn"], "Quỹ học bổng Vừ A Dính ngày nay nâng cánh ước mơ cho hàng vạn học sinh, sinh viên dân tộc thiểu số nghèo vượt khó học giỏi.", "7-8", 2),
    ("Anh hùng Bế Văn Đàn lấy thân làm giá súng", "Trong chiến dịch Điện Biên Phủ, người chiến sĩ dũng cảm đã lấy hai vai làm giá súng cho đồng đội bắn tỉa quân thù là ai?", "Anh Bế Văn Đàn", ["Phan Đình Giót", "Tô Vĩnh Diện", "Trần Can"], "Hành động anh hùng của Bế Văn Đàn đã khích lệ toàn trung đoàn xốc tới quét sạch cứ điểm địch.", "7-8", 2),
    ("Anh hùng Phan Đình Giót lấy thân chèn lỗ châu mai", "Trong trận đánh mở màn đồi Him Lam lịch sử, người chiến sĩ anh dũng đã lấy thân mình lấp kín lỗ châu mai của địch là ai?", "Anh Phan Đình Giót", ["Bế Văn Đàn", "Tô Vĩnh Diện", "Cù Chính Lan"], "Tiếng súng địch câm bặt tạo thời cơ cho toàn đại đội xông lên cắm cờ chiến thắng trên cứ điểm Him Lam.", "7-8", 2),
    ("Anh hùng Tô Vĩnh Diện lấy thân chèn pháo", "Người chiến sĩ pháo binh quả cảm đã dùng cả thân mình chèn vào bánh pháo đang trôi xuống dốc đèo để cứu khẩu pháo cao xạ là ai?", "Anh Tô Vĩnh Diện", ["Phan Đình Giót", "Bế Văn Đàn", "Lê Văn Tám"], "Khẩu pháo cao xạ 37mm được cứu an toàn đã bắn rơi nhiều máy bay giặc trên bầu trời Điện Biên Phủ.", "7-8", 2),
    ("Tết Nguyên Đán đoàn viên", "Ngày Tết cổ truyền lớn nhất và thiêng liêng nhất trong năm của người dân Việt Nam là tết gì?", "Tết Nguyên Đán (Tết Ta / Tết Âm lịch)", ["Tết Trung Thu", "Tết Hàn Thực", "Tết Đoan Ngọ"], "Tết Nguyên Đán là dịp con cháu từ khắp phương trời tụ họp về bên gia đình, chúc thọ ông bà cha mẹ và nhận phong bao lì xì đỏ may mắn.", "6-7", 1),
    ("Mâm ngũ quả ngày Tết", "Mâm ngũ quả trên bàn thờ tổ tiên ngày Tết ở miền Nam thường có 5 loại trái cây: Cầu, Sung, Dừa, Đủ, Xoài gửi gắm ước nguyện gì?", "'Cầu mong vừa đủ xài và sung túc trong năm mới'", ["Cầu mong ăn nhiều", "Cầu mong trúng số", "Cầu mong đi chơi xa"], "Ước mong mộc mạc mà chân thành về một cuộc sống gia đình ấm no, bình an và hạnh phúc của người dân phương Nam.", "6-7", 1),
    ("Gói bánh chưng ngày Tết", "Vào những ngày giáp Tết, cả gia đình ngồi quây quần bên bếp lửa hồng nấu nồi bánh chưng thơm nức từ những nguyên liệu gì?", "Lá dong xanh, gạo nếp cái hoa vàng, đỗ xanh và thịt lợn ướp tiêu", ["Bột mì và đường", "Rau bina và cá hồi", "Bánh mì kẹp"], "Tiếng củi tí tách reo cùng nồi bánh chưng sôi ùng ục là ký ức tuổi thơ ấm áp ngọt ngào nhất trong lòng người Việt xa xứ.", "6-7", 1),
    ("Tết Trung Thu trông trăng", "Ngày rằm tháng Tám âm lịch (Tết Trung Thu) là ngày tết vui tươi dành riêng cho ai?", "Ngày Tết của thiếu nhi (Tết trông trăng, phá cỗ rước đèn)", ["Tết của người già", "Tết của thầy cô", "Tết của thợ săn"], "Bé rước đèn ông sao lấp lánh, xem múa lân rộn rã tùng dinh dinh và phá cỗ bánh nướng bánh dẻo dưới ánh trăng rằm tròn vành vạnh.", "6-7", 1),
    ("Bánh Trung Thu cổ truyền", "Hai loại bánh truyền thống không thể thiếu trong mâm cỗ Trung Thu phá cỗ trông trăng là bánh gì?", "Bánh nướng và bánh dẻo", ["Bánh chưng và bánh giầy", "Bánh bao và bánh mì", "Bánh rán và bánh cuốn"], "Bánh dẻo trắng muốt hình tròn như vầng trăng, bánh nướng thơm lừng nhân thập cẩm tượng trưng cho sự đoàn viên tròn đầy.", "6-7", 1),
    ("Trang phục Áo dài truyền thống", "Trang phục truyền thống thướt tha tôn vinh nét đẹp dịu dàng của người phụ nữ Việt Nam là trang phục nào?", "Bộ Áo dài truyền thống", ["Áo bà ba", "Áo tứ thân", "Áo dạ hội"], "Tà áo dài trắng tinh khôi của nữ sinh cắp sách đến trường là hình ảnh biểu tượng văn hóa thanh lịch của đất nước Việt Nam.", "6-7", 1),
    ("Chiếc nón lá Việt Nam", "Vật dụng che mưa che nắng bình dị mà duyên dáng làm từ lá nón, cật tre gắn liền với tà áo dài là gì?", "Chiếc nón lá", ["Chiếc ô dù", "Chiếc mũ tai bèo", "Chiếc khăn rằn"], "Nón bài thơ xứ Huế soi nghiêng dưới ánh nắng soi tỏ những vần thơ và hình ảnh chùa Thiên Mụ ẩn hiện bên trong vành nón.", "6-7", 1),
    ("Chiếc khăn rằn Nam Bộ", "Chiếc khăn kẻ caro đen trắng hoặc đỏ trắng choàng cổ gắn liền với người dân lao động và du kích miền Tây Nam Bộ là gì?", "Chiếc khăn rằn", ["Khăn mỏ quạ", "Khăn len", "Khăn voan"], "Khăn rằn vừa dùng lau mồ hôi trên đồng ruộng, vừa che nắng che gió và là biểu tượng của tinh thần quật khởi phương Nam.", "6-7", 1),
    ("Dân ca Quan họ Bắc Ninh", "Loại hình dân ca truyền thống với những làn điệu mượt mà, lời ca ý nhị của các liền anh, liền chị trên thuyền rồng là gì?", "Dân ca Quan họ Bắc Ninh", ["Hát Xoan Phú Thọ", "Ca trù", "Đờn ca tài tử"], "Quan họ Bắc Ninh được UNESCO công nhận là Di sản Văn hóa Phi vật thể đại diện của nhân loại với văn hóa ứng xử trọng nghĩa trọng tình.", "7-8", 2),
    ("Không gian văn hóa Cồng chiêng Tây Nguyên", "Di sản văn hóa phi vật thể của đồng bào các dân tộc thiểu số Tây Nguyên gắn liền với các lễ hội đâm trâu, mừng lúa mới là gì?", "Không gian văn hóa Cồng chiêng Tây Nguyên", ["Hát chèo", "Nhã nhạc cung đình", "Hát bội"], "Tiếng cồng chiêng ngân vang như tiếng sấm rền, tiếng suối reo kết nối con người với thần linh và núi rừng đại ngàn.", "7-8", 2),
    ("Nghệ thuật Đờn ca tài tử Nam Bộ", "Loại hình âm nhạc dân gian đặc trưng của vùng sông nước Nam Bộ gắn liền với cây đàn kìm, đàn tranh và bài Dạ cổ hoài lang là gì?", "Đờn ca tài tử Nam Bộ", ["Hát chèo", "Hát tuồng", "Hát then"], "Đờn ca tài tử thể hiện tâm hồn phóng khoáng, hào sảng và tình cảm chân chất của người dân miệt vườn sông nước Cửu Long.", "7-8", 2),
    ("Nhã nhạc Cung đình Huế", "Loại hình âm nhạc bác học biểu diễn trong các dịp đại lễ triều đình phong kiến nhà Nguyễn được UNESCO vinh danh là gì?", "Nhã nhạc Cung đình Huế", ["Dân ca ví dặm", "Hát cải lương", "Hát sẩm"], "Dàn nhạc cung đình với biên chế hoàn chỉnh gồm kèn, trống, đàn tam, đàn tỳ bà tạo nên không khí trang nghiêm lộng lẫy chốn hoàng cung.", "8-9", 3),
    ("Nghệ thuật Múa rối nước", "Loại hình nghệ thuật sân khấu dân gian độc đáo của cư dân lúa nước Bắc Bộ biểu diễn trên mặt hồ nước với chú Tễu vui nhộn là gì?", "Múa rối nước truyền thống", ["Múa lân sư rồng", "Xiếc thú", "Kịch câm"], "Các nghệ nhân đứng ngâm mình sau tấm mành tre khéo léo dùng sào và dây điều khiển các con rối gỗ biểu diễn sinh động trên mặt nước.", "6-7", 1),
    ("Chú Tễu trong múa rối nước", "Nhân vật rối nước có thân hình tròn mập mạp, cởi trần đóng khố, luôn nở nụ cười tươi rói mở màn câu chuyện là ai?", "Chú Tễu", ["Thạch Sanh", "Cuội", "Bờm"], "Chú Tễu là hiện thân của sự lạc quan, hóm hỉnh và tiếng cười châm biếm sâu sắc của người nông dân lao động.", "6-7", 1),
    ("Hát Xoan Phú Thọ cửa đình", "Di sản hát dân ca nghi lễ gắn liền với tín ngưỡng thờ cúng Hùng Vương biểu diễn vào mùa xuân ở Phú Thọ là gì?", "Hát Xoan Phú Thọ", ["Hát Then", "Hát Dặm", "Hát Ca trù"], "Hát Xoan gồm có hát nghi lễ thờ cúng, hát quả cách và hát giao duyên rộn rã sân đình cổ kính.", "8-9", 3),
    ("Dân ca Ví Giặm Nghệ Tĩnh", "Di sản dân ca truyền thống sâu lắng, mộc mạc bên dòng sông Lam núi Hồng của hai tỉnh Nghệ An và Hà Tĩnh là gì?", "Dân ca Ví, Giặm Nghệ Tĩnh", ["Quan họ Bắc Ninh", "Hò sông Hương", "Hát Bả trạo"], "Ví Giặm cất lên mộc mạc khi dệt vải, cấy lúa thể hiện tình yêu quê hương đất nước và lòng son sắt thủy chung.", "7-8", 2),
    ("Lễ hội Đua thuyền rồng", "Lễ hội sông nước truyền thống đầu xuân cầu mưa thuận gió hòa, mùa màng bội thu của cư dân ven sông ven biển là gì?", "Lễ hội Đua thuyền rồng (Đua ghe ngo)", ["Lễ hội thả diều", "Lễ hội chọi trâu", "Lễ hội kéo co"], "Các đội chèo thuyền nhịp nhàng theo tiếng trống giục giã thể hiện tinh thần thượng võ và sức mạnh đoàn kết tập thể.", "6-7", 1),
    ("Lễ hội Chọi trâu Đồ Sơn", "Lễ hội truyền thống độc đáo của cư dân vùng biển Hải Phòng gắn liền với câu ca dao 'Dù ai buôn đâu bán đâu / Mùng chín tháng tám chọi trâu thì về' là gì?", "Lễ hội Chọi trâu Đồ Sơn", ["Lễ hội Tịch điền", "Lễ hội Đền Trần", "Lễ hội Yên Thế"], "Chọi trâu Đồ Sơn mang ý nghĩa cầu mong trời yên biển lặng, tôm cá đầy khoang và thể hiện tinh thần dũng mãnh của người miền biển.", "7-8", 2),
    ("Lễ hội Tịch điền Đọi Sơn", "Lễ hội đầu xuân tái hiện cảnh vua xuống đồng cày ruộng cầu cho quốc thái dân an, mùa màng tươi tốt thuộc tỉnh Hà Nam là gì?", "Lễ hội Tịch điền Đọi Sơn", ["Lễ hội Đền Hùng", "Lễ hội Côn Sơn", "Lễ hội Cổ Loa"], "Hình ảnh các đồng chí lãnh đạo mặc áo nâu xuống cày luống đất đầu năm tôn vinh hạt ngọc trời và người nông dân cần cù.", "7-8", 2),
    ("Lễ Khai ấn Đền Trần Nam Định", "Lễ hội đêm rằm tháng Giêng thu hút hàng vạn người dân xin lộc ấn may mắn công danh tại vùng đất phát tích nhà Trần là gì?", "Lễ hội Khai ấn Đền Trần", ["Lễ hội Phủ Dầy", "Lễ hội Chùa Keo", "Lễ hội Đền Quát"], "Bốn chữ 'Tích phúc vô cương' khắc trên ấn Đền Trần khuyên dạy hậu thế phải luôn tích đức làm việc thiện cho muôn dân.", "8-9", 3),
    ("Lễ hội Cầu ngư của ngư dân miền Trung", "Lễ hội tôn kính thờ cá Ông (cá voi cứu người) cầu mong biển êm sóng lặng, tôm cá đầy thuyền của ngư dân miền Trung là gì?", "Lễ hội Cầu ngư (Thờ cá Ông)", ["Lễ hội Nghinh Ông", "Lễ hội Miếu Bà", "Lễ hội Cột Cờ"], "Ngư dân coi cá voi là vị thần hộ mệnh linh thiêng trên biển cả, khi cá voi mất đều được an táng trang trọng tại lăng Ông.", "7-8", 2),
    ("Lễ hội Đua ghe Ngo Sóc Trăng", "Lễ hội đua thuyền rực rỡ sắc màu lớn nhất trong năm của đồng bào dân tộc Khmer Nam Bộ vào dịp lễ Ooc Om Boc là gì?", "Lễ hội Đua ghe Ngo", ["Lễ hội Katê", "Lễ hội Chôl Chnăm Thmây", "Lễ hội Sen Dolta"], "Những chiếc ghe Ngo dài hàng chục mét chạm trổ hình rồng phụng bay lượn vút nhanh trên mặt sông giữa tiếng hò reo vang dội.", "7-8", 2),
    ("Tết Chôl Chnăm Thmây của người Khmer", "Tết mừng năm mới cổ truyền theo lịch Phật giáo của đồng bào dân tộc Khmer Nam Bộ diễn ra vào tháng mấy dương lịch?", "Tháng Tư hàng năm (khoảng 14-16/4)", ["Tháng Giêng âm lịch", "Tháng Tám", "Tháng Mười hai"], "Vào dịp này bà con Khmer đến chùa đắp núi cát tích đức, thực hiện nghi thức tắm Phật và té nước chúc phúc may mắn.", "8-9", 3),
    ("Lễ hội Katê của người Chăm", "Lễ hội dân gian lớn nhất trong năm tưởng nhớ các vị thần linh và vua chúa hiển hách của đồng bào dân tộc Chăm là lễ hội gì?", "Lễ hội Katê (Ninh Thuận và Bình Thuận)", ["Lễ hội Ramưwan", "Lễ hội Cầu mùa", "Lễ hội Ka-tơ"], "Tiếng kèn Saranai réo rắt cùng nhịp trống Paranưng rộn ràng hòa theo điệu múa quạt duyên dáng của các thiếu nữ Chăm bên tháp Chàm cổ kính.", "8-9", 3),
    ("Cây đàn Bầu độc đáo của Việt Nam", "Nhạc cụ dân tộc độc nhất vô nhị chỉ có một dây đàn mà phát ra những âm thanh nỉ non sâu lắng rung động lòng người là gì?", "Đàn Bầu (Độc huyền cầm)", ["Đàn Tranh", "Đàn Nhị", "Đàn Nguyệt"], "'Đàn bầu ai gảy nấy nghe / Làm thân con gái chớ nghe đàn bầu' là câu ca dao ngợi ca sức truyền cảm kỳ diệu của tiếng đàn bầu Việt Nam.", "6-7", 1),
    ("Đàn T'rưng Tây Nguyên", "Nhạc cụ gõ truyền thống làm từ các ống tre nứa khô dài ngắn khác nhau phát ra âm thanh như tiếng suối reo của Tây Nguyên là gì?", "Đàn T'rưng", ["Đàn Đáy", "Đàn Tam thập lục", "Đàn Goong"], "Nghệ nhân dùng dùi gõ vào các ống nứa rung lên những giai điệu rộn rã của núi rừng đại ngàn hoang sơ.", "7-8", 2),
    ("Đàn K'lông Pút", "Nhạc cụ tre nứa độc đáo của phụ nữ Tây Nguyên không dùng dùi gõ mà người chơi vỗ hai bàn tay vào nhau tạo luồng khí rung là gì?", "Đàn K'lông Pút", ["Đàn T'rưng", "Đàn Chapi", "Đàn Tính"], "Luồng gió từ đôi bàn tay vỗ ép không khí vào miệng ống nứa tạo nên những âm thanh trầm bổng kỳ diệu như tiếng gió rừng.", "8-9", 3),
    ("Cây đàn Tính của người Tày Nùng", "Cây đàn dây có bầu đàn làm bằng nửa quả bầu khô, cần đàn dài bằng gỗ dẻo gắn liền với điệu hát Then là gì?", "Đàn Tính (Tính tẩu)", ["Đàn Bầu", "Đàn Nhị", "Đàn Nguyệt"], "Điệu hát Then cùng tiếng đàn Tính mượt mà của đồng bào Tày, Nùng đã được UNESCO vinh danh là Di sản Văn hóa phi vật thể nhân loại.", "7-8", 2),
    ("Trò chơi dân gian Kéo co", "Trò chơi tập thể truyền thống rèn luyện sức mạnh cơ bắp và tinh thần đoàn kết kéo một sợi dây thừng về phía mình là trò gì?", "Trò chơi Kéo co", ["Nhảy dây", "Trốn tìm", "Bịt mắt bắt dê"], "Nghi lễ và trò chơi Kéo co của Việt Nam, Hàn Quốc, Campuchia và Philippines đã được UNESCO ghi danh là di sản văn hóa thế giới.", "6-7", 1),
    ("Trò chơi Ô ăn quan", "Trò chơi dân gian rèn luyện tư duy tính toán thông minh với những viên sỏi nhỏ rải trên bảng vẽ 10 ô vuông 2 ô hình bán nguyệt là gì?", "Trò chơi Ô ăn quan", ["Cờ tướng", "Cờ vua", "Rồng rắn lên mây"], "Ô ăn quan giúp các bạn nhỏ rèn luyện khả năng tính toán cộng trừ nhẩm nhanh và tư duy chiến thuật nhạy bén.", "6-7", 1),
    ("Trò chơi Bịt mắt bắt dê", "Trò chơi dân gian vui nhộn một bạn nhỏ bị bịt mắt bằng khăn phải lắng nghe tiếng kêu 'be be' để tìm bắt các bạn xung quanh là gì?", "Bịt mắt bắt dê", ["Cướp cờ", "Thả đỉa ba ba", "Trốn tìm"], "Tiếng cười đùa rộn rã trên bãi cỏ làng quê trong trò chơi bịt mắt bắt dê là ký ức tuổi thơ trong trẻo tuyệt đẹp.", "6-7", 1),
    ("Thả diều đồng quê", "Vào những buổi chiều hè lộng gió, các bạn nhỏ rủ nhau ra đê làng thả những cánh diều sáo bay vút lên bầu trời gọi là gì?", "Trò chơi Thả diều (Diều sáo)", ["Bắn bi", "Đánh đáo", "Nhảy bao bố"], "Tiếng sáo diều vi vu ngân nga giữa tầng không đem lại cảm giác thanh bình, khoáng đạt cho tâm hồn trẻ thơ.", "6-7", 1),
    ("Đạo lý Uống nước nhớ nguồn", "Truyền thống đạo lý tốt đẹp nhắc nhở con cháu luôn biết ơn thế hệ cha ông đi trước đã dày công gây dựng là gì?", "'Uống nước nhớ nguồn' / 'Ăn quả nhớ kẻ trồng cây'", ["Ăn xổi ở thì", "Vắt chanh bỏ vỏ", "Qua cầu rút ván"], "Biết ơn ông bà, cha mẹ, thầy cô và các anh hùng liệt sĩ là phẩm chất đạo đức cao quý hàng đầu của mỗi người Việt Nam.", "6-7", 1),
    ("Truyền thống Tôn sư trọng đạo", "Ngày lễ tri ân các thầy cô giáo - những người lái đò thầm lặng đưa bao thế hệ học trò cập bến bờ tri thức là ngày nào?", "Ngày 20 tháng 11 (Ngày Nhà giáo Việt Nam)", ["Ngày 1 tháng 6", "Ngày 26 tháng 3", "Ngày 15 tháng 8"], "Bông hoa điểm mười tươi thắm và lời chào kính cẩn là món quà ý nghĩa nhất dâng lên thầy cô giáo kính yêu.", "6-7", 1),
    ("Ngày Quốc tế Thiếu nhi", "Ngày hội tết vui tươi dành cho tất cả trẻ em trên toàn thế giới được tổ chức vào ngày đầu tiên của tháng Sáu là ngày nào?", "Ngày 1 tháng 6", ["Ngày 20 tháng 10", "Ngày 8 tháng 3", "Ngày 22 tháng 12"], "Trẻ em như búp trên cành, được toàn xã hội yêu thương chăm sóc, bảo vệ và tạo điều kiện học tập vui chơi tốt nhất.", "6-7", 1),
    ("Năm điều Bác Hồ dạy", "Năm điều Bác Hồ dạy thiếu niên nhi đồng bắt đầu bằng lời dạy thiêng liêng nào?", "'1. Yêu Tổ quốc, yêu đồng bào'", ["Học thật giỏi", "Ăn thật nhiều", "Chơi thể thao"], "Năm điều Bác dạy là kim chỉ nam rèn luyện đạo đức và học tập của mọi thế hệ măng non Đội Thiếu niên Tiền phong.", "6-7", 1),
    ("Khăn quàng đỏ thắm", "Chiếc khăn hình tam giác màu đỏ rực thắt trên vai áo của các bạn đội viên thiếu niên tiền phong tượng trưng cho điều gì?", "Một phần của lá cờ Tổ quốc thiêng liêng và niềm tự hào cách mạng", ["Để giữ ấm cổ", "Để lau mồ hôi", "Chỉ làm đẹp"], "Được vinh dự đeo khăn quàng đỏ nhắc nhở các bạn nhỏ luôn phấn đấu học tập, tu dưỡng trở thành cháu ngoan Bác Hồ.", "6-7", 1),
    ("Bác Hồ yêu hoa sen", "Loài hoa thanh cao gắn liền với tên tuổi và phẩm chất giản dị, thanh bạch của Bác Hồ kính yêu là hoa gì?", "Hoa sen", ["Hoa hồng", "Hoa cúc", "Hoa lan"], "'Tháp Mười đẹp nhất bông sen / Việt Nam đẹp nhất có tên Bác Hồ' - vần thơ bất hủ ca ngợi vị cha già kính yêu của dân tộc.", "6-7", 1),
    ("Lăng Chủ tịch Hồ Chí Minh", "Nơi an nghỉ vĩnh hằng của Bác Hồ kính yêu nằm trang nghiêm bên Quảng trường Ba Đình lịch sử ở Hà Nội là gì?", "Lăng Bác (Lăng Chủ tịch Hồ Chí Minh)", ["Nhà sàn Bác Hồ", "Phủ Chủ tịch", "Viện Bảo tàng"], "Hàng triệu đồng bào và bạn bè quốc tế mỗi ngày xếp hàng trang nghiêm vào lăng viếng Bác với lòng thành kính sâu sắc.", "6-7", 1),
    ("Bác Hồ và các cháu thiếu nhi", "Hình ảnh Bác Hồ luôn dành tình cảm yêu thương trìu mến nhất cho thiếu nhi thể hiện qua câu thơ nổi tiếng nào?", "'Bác mong các cháu chăm ngoan / Mai sau gìn giữ giang sơn Lạc Hồng'", ["Bác thích đi chơi xa", "Bác dạy tập bắn súng", "Bác khen đi ngủ sớm"], "Sinh thời dù bận trăm công nghìn việc nước, Bác Hồ vẫn luôn gửi thư, gửi quà khen ngợi các cháu thiếu nhi mỗi dịp Trung Thu, khai giảng.", "6-7", 1),
    ("Thư Bác Hồ gửi ngày khai trường", "Trong bức thư gửi học sinh nhân ngày khai trường đầu tiên năm 1945, Bác Hồ đã gửi gắm niềm tin son sắt nào?", "'Non sông Việt Nam có trở nên tươi đẹp hay không... chính là nhờ một phần lớn ở công học tập của các em'", ["Bác khuyên nghỉ học", "Bác bảo đi buôn bán", "Bác bảo không cần đọc sách"], "Lời dạy thiêng liêng của Bác thôi thúc bao thế hệ học sinh nỗ lực vươn lên chiếm lĩnh đỉnh cao tri thức nhân loại.", "7-8", 2),
    ("Đoàn kết là sức mạnh", "Bác Hồ từng tổng kết chân lý sức mạnh bất diệt của cách mạng Việt Nam bằng câu nói nổi tiếng nào?", "'Đoàn kết, đoàn kết, đại đoàn kết / Thành công, thành công, đại thành công'", ["Chia rẽ là sức mạnh", "Một mình làm tất cả", "Không cần hợp tác"], "Sức mạnh đại đoàn kết toàn dân tộc là cội nguồn của mọi thắng lợi vĩ đại trong lịch sử dựng nước và giữ nước.", "7-8", 2)
]

raw_mc.extend(more_mc_ls)

# 14 SA items (LS127 - LS140)
raw_sa = [
    ("Tổ tiên Rồng Tiên", "Theo truyền thuyết, tổ tiên người Việt gắn với cha Lạc Long Quân và mẹ có tên là gì?", "âu cơ|mẹ âu cơ", "Mẹ Âu Cơ sinh bọc trăm trứng là cội nguồn con Rồng cháu Tiên.", "6-7", 1),
    ("Các vị vua đầu tiên", "Các vị vua có công dựng nên nhà nước Văn Lang đầu tiên của nước ta gọi chung là gì?", "vua hùng|các vua hùng|hùng vương", "Các Vua Hùng có công dựng nước Văn Lang.", "6-7", 1),
    ("Chiến thắng sông Bạch Đằng 938", "Vị anh hùng cắm cọc gỗ trên sông Bạch Đằng năm 938 chấm dứt 1000 năm Bắc thuộc là ai?", "ngô quyền", "Ngô Quyền là vị vua mở đầu nền độc lập tự chủ lâu dài.", "6-7", 1),
    ("Bài thơ thần trên sông Như Nguyệt", "Vị danh tướng lãnh đạo kháng chiến chống Tống viết bài thơ thần Nam quốc sơn hà là ai?", "lý thường kiệt", "Lý Thường Kiệt lãnh đạo quân dân phá tan quân Tống xâm lược.", "7-8", 2),
    ("Bóp nát quả cam", "Người thiếu niên anh hùng thêu cờ 6 chữ vàng phá cường địch báo hoàng ân là ai?", "trần quốc toản", "Trần Quốc Toản tuổi trẻ chí lớn là tấm gương yêu nước ngời sáng.", "6-7", 1),
    ("Vị tướng 3 lần thắng Nguyên Mông", "Vị Tiết chế Quốc công chỉ huy quân dân nhà Trần 3 lần đại thắng quân Nguyên Mông là ai?", "trần hưng đạo|trần quốc tuấn", "Trần Hưng Đạo là vị thánh tướng kiệt xuất của non sông đất Việt.", "7-8", 2),
    ("Trả gươm báu Hồ Gươm", "Vị vua lãnh đạo khởi nghĩa Lam Sơn toàn thắng rồi trả gươm báu cho Rùa Vàng là ai?", "lê lợi|lê thái tổ", "Lê Lợi lập nên triều Hậu Lê sau 10 năm gian khổ kháng chiến.", "7-8", 2),
    ("Tác giả Bình Ngô đại cáo", "Nhà quân sự, danh nhân văn hóa thế giới viết áng thiên cổ hùng văn Bình Ngô đại cáo là ai?", "nguyễn trãi", "Nguyễn Trãi là nhà văn hóa lỗi lạc vì dân vì nước.", "8-9", 3),
    ("Vua Quang Trung áo vải", "Vị hoàng đế áo vải Tây Sơn đại phá 29 vạn quân Mãn Thanh mùa xuân Kỷ Dậu 1789 có tên thật là gì?", "nguyễn huệ|quang trung nguyễn huệ", "Quang Trung Nguyễn Huệ là thiên tài quân sự bách chiến bách thắng.", "7-8", 2),
    ("Đọc Tuyên ngôn Độc lập", "Vị lãnh tụ vĩ đại đọc bản Tuyên ngôn Độc lập ngày 2 tháng 9 năm 1945 tại Quảng trường Ba Đình là ai?", "bác hồ|hồ chí minh|chủ tịch hồ chí minh", "Bác Hồ kính yêu là người cha già vĩ đại của dân tộc Việt Nam.", "6-7", 1),
    ("Người đội trưởng đầu tiên", "Người đội trưởng đầu tiên của Đội Thiếu niên Tiền phong Hồ Chí Minh có tên bí danh là gì?", "kim đồng|anh kim đồng", "Anh Kim Đồng dũng cảm hy sinh khi làm nhiệm vụ giao liên.", "6-7", 1),
    ("Tác giả Quốc ca", "Nhạc sĩ tài hoa nào đã sáng tác bài hát Tiến quân ca - Quốc ca của nước ta?", "văn cao|nhạc sĩ văn cao", "Nhạc sĩ Văn Cao sáng tác bài Tiến quân ca hào hùng.", "7-8", 2),
    ("Bánh truyền thống ngày Tết", "Loại bánh hình vuông gói bằng lá dong tượng trưng cho Đất vào dịp Tết Nguyên Đán là bánh gì?", "bánh chưng", "Bánh chưng xanh là linh hồn ẩm thực ngày Tết cổ truyền.", "6-7", 1),
    ("Trường đại học đầu tiên", "Khu di tích lịch sử tại Hà Nội được coi là trường đại học đầu tiên của Việt Nam có tên là gì?", "quốc tử giám|văn miếu quốc tử giám", "Quốc Tử Giám là cái nôi đào tạo nhân tài đầu tiên của nước ta.", "7-8", 2)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"LS{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Lịch Sử & Văn Hóa",
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
    qid = f"LS{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Lịch Sử & Văn Hóa",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/ls_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành LS: {len(questions)} câu đã được ghi vào ls_140.json")

# Bổ sung 41 câu MC cho LS
extra_ls_41 = [
    ("Truyền thống tôn sư", "Câu thành ngữ nào sau đây thể hiện sâu sắc truyền thống biết ơn thầy cô giáo của người Việt Nam?", "'Không thầy đố mày làm nên' / 'Nhất tự vi sư, bán tự vi sư'", ["Học thầy không tày học bạn", "Đi một ngày đàng học một sàng khôn", "Học ăn học nói"], "Kính trọng và biết ơn người thầy dạy dỗ tri thức đạo đức là nét đẹp văn hóa ngàn đời của dân tộc.", "6-7", 1),
    ("Nhà giáo Chu Văn An quê ở đâu", "Thầy giáo Chu Văn An sinh ra tại vùng đất Thanh Đàm nay thuộc huyện nào của thủ đô Hà Nội?", "Huyện Thanh Trì (Hà Nội)", ["Huyện Đông Anh", "Huyện Gia Lâm", "Huyện Thường Tín"], "Thầy mở trường dạy học tại làng Huỳnh Cung, học trò của thầy nhiều người đỗ đại khoa làm quan lớn.", "8-9", 3),
    ("Trạng Lợn Trạng Quỳnh", "Các nhân vật thông minh, hóm hỉnh trong truyện cười dân gian Việt Nam thường dùng trí tuệ đối đáp sứ thần phương Bắc là ai?", "Trạng Quỳnh và Trạng Lợn", ["Thạch Sanh", "Lý Thông", "Chử Đồng Tử"], "Tiếng cười Trạng Quỳnh mang tính nhân văn sâu sắc, ngợi ca trí thông minh dân gian và tinh thần tự hào dân tộc.", "7-8", 2),
    ("Trạng Trình Nguyễn Bỉnh Khiêm", "Nhà tiên tri, nhà tư tưởng lỗi lạc thời Mạc nổi tiếng với những lời sấm truyền dự báo thế sự trăm năm là ai?", "Trạng Trình Nguyễn Bỉnh Khiêm", ["Trạng Quỳnh", "Lương Thế Vinh", "Phùng Khắc Khoan"], "Lời khuyên 'Biển Đông vạn dặm giang tay giữ' của Nguyễn Bỉnh Khiêm khẳng định tầm nhìn chiến lược về biển đảo từ thế kỷ 16.", "8-9", 3),
    ("Trạng Lường Lương Thế Vinh", "Vị trạng nguyên thời Lê sơ thông minh kiệt xuất, tác giả cuốn sách toán 'Đại thành toán pháp' và đo cân nặng voi bằng thuyền là ai?", "Trạng Lường Lương Thế Vinh", ["Trần Tất Văn", "Vũ Kiệt", "Giáp Hải"], "Lương Thế Vinh dùng nguyên lý mực nước dâng trên mạn thuyền để cân con voi khổng lồ khiến sứ giặc phục lăn.", "7-8", 2),
    ("Trạng nguyên trẻ nhất Nguyễn Hiền", "Cậu bé thông minh đỗ Trạng nguyên khi mới 13 tuổi - Trạng nguyên trẻ tuổi nhất trong lịch sử khoa bảng Việt Nam là ai?", "Nguyễn Hiền", ["Lê Văn Hưu", "Mạc Đĩnh Chi", "Đào Duy Từ"], "Nguyễn Hiền đỗ Trạng nguyên năm 1247 thời vua Trần Thái Tông, nổi tiếng với giai thoại giải câu đố xâu chỉ qua vỏ ốc xoắn.", "7-8", 2),
    ("Lưỡng quốc Trạng nguyên Mạc Đĩnh Chi", "Vị quan thanh liêm, tài đức vẹn toàn thời Trần được cả vua Đại Việt và hoàng đế nhà Nguyên phong danh hiệu 'Lưỡng quốc Trạng nguyên' là ai?", "Mạc Đĩnh Chi", ["Nguyễn Trực", "Lương Thế Vinh", "Phạm Đôn Lễ"], "Mạc Đĩnh Chi ví mình như bông sen trong giếng ngọc 'Ngọc tỉnh liên', toát lên khí phách thanh cao của kẻ sĩ Đại Việt.", "8-9", 3),
    ("Đại thi hào Nguyễn Du", "Tác giả kiệt tác 'Truyện Kiều' bất hủ - Danh nhân văn hóa thế giới vĩ đại của nền văn học Việt Nam là ai?", "Đại thi hào Nguyễn Du", ["Nguyễn Trãi", "Hồ Xuân Hương", "Đoàn Thị Điểm"], "'Truyện Kiều' bằng thể thơ lục bát truyền thống đã được dịch ra hơn 30 thứ tiếng trên khắp thế giới.", "8-9", 3),
    ("Bà Chúa thơ Nôm Hồ Xuân Hương", "Nữ thi sĩ tài ba độc đáo thời phong kiến nổi tiếng với những bài thơ Nôm sắc sảo như 'Bánh trôi nước', 'Quả mít' là ai?", "Hồ Xuân Hương", ["Bà Huyện Thanh Quan", "Đoàn Thị Điểm", "Sương Nguyệt Anh"], "Năm 2021, UNESCO đã vinh danh nữ sĩ Hồ Xuân Hương là Danh nhân văn hóa thế giới.", "8-9", 3),
    ("Bà Huyện Thanh Quan", "Nữ sĩ tài danh thời Nguyễn có những vần thơ hoài cổ trang nhã, man mác buồn trong bài 'Qua Đèo Ngang' là ai?", "Bà Huyện Thanh Quan (Nguyễn Thị Hinh)", ["Hồ Xuân Hương", "Anh Thơ", "Xuân Quỳnh"], "Thơ Bà Huyện Thanh Quan chuẩn mực về niêm luật Đường luật và giàu tình yêu non sông đất nước.", "8-9", 3),
    ("Hủ tiếu Nam Bộ", "Món ăn sợi gạo dai ngon, nước dùng ngọt thanh từ xương ống và tôm khô đặc trưng của người dân Nam Bộ là gì?", "Hủ tiếu (như Hủ tiếu Mỹ Tho, Hủ tiếu Sa Đéc)", ["Phở bò", "Bún chả", "Bánh canh"], "Hủ tiếu là sự giao thoa văn hóa ẩm thực tuyệt vời giữa người Việt, người Hoa và người Khmer phương Nam.", "6-7", 1),
    ("Phở Hà Nội di sản ẩm thực", "Món ăn truyền thống nổi tiếng thế giới của thủ đô Hà Nội với bánh phở mềm, nước dùng thơm nồng hồi quế là món gì?", "Phở Hà Nội (Phở bò, Phở gà)", ["Bún đậu", "Bánh tôm", "Chả cá"], "Phở là đại sứ ẩm thực số 1 của Việt Nam, được du khách quốc tế ngợi ca và tôn vinh trong từ điển Oxford.", "6-7", 1),
    ("Bánh mì Việt Nam giòn rụm", "Món ăn đường phố kẹp pa-tê, thịt nướng, dưa góp, rau thơm nổi tiếng khắp năm châu bốn biển của nước ta là gì?", "Bánh mì kẹp Việt Nam", ["Bánh bao", "Bánh pizza", "Bánh hamburger"], "Bánh mì Việt Nam luôn nằm trong top những món ăn sandwich đường phố ngon nhất thế giới.", "6-7", 1),
    ("Bún chả Hà Nội", "Món ăn truyền thống của người Hà Nội gồm chả nướng than hoa thơm lừng chấm nước mắm chua ngọt ăn kèm bún là gì?", "Bún chả Hà Nội", ["Bún bò Huế", "Bún riêu cua", "Bún ốc"], "Tổng thống Mỹ Barack Obama khi đến thăm Việt Nam năm 2016 đã thưởng thức món bún chả thơm ngon tại phố cổ Hà Nội.", "6-7", 1),
    ("Cơm tấm sườn bì chả Sài Gòn", "Món ăn bình dị mà hấp dẫn làm từ hạt gạo tấm vỡ ăn kèm sườn nướng than hoa thơm phức đặc trưng của TP.HCM là gì?", "Cơm tấm Sài Gòn", ["Cơm lam Tây Bắc", "Cơm hến Huế", "Cơm cháy Ninh Bình"], "Mùi sườn nướng thơm ngào ngạt lan tỏa khắp các góc phố Sài Gòn là nét ẩm thực thân thương khó quên.", "6-7", 1),
    ("Bánh xèo giòn rụm", "Món bánh tráng mỏng màu vàng ươm nghệ, nhân tôm thịt giá đỗ, khi đổ vào chảo phát ra tiếng 'xèo xèo' vui tai là gì?", "Bánh xèo miền Tây", ["Bánh khọt", "Bánh cuốn", "Bánh bèo"], "Bánh xèo cuốn bánh tráng rau rừng chấm nước mắm tỏi ớt chua ngọt giòn tan thơm béo đậm đà.", "6-7", 1),
    ("Cơm lam nướng ống tre", "Món cơm thơm dẻo của đồng bào các dân tộc vùng núi được nấu bằng gạo nếp nương trong ống tre tươi nướng trên than hồng là gì?", "Cơm lam", ["Xôi ngũ sắc", "Cơm tấm", "Bánh chưng"], "Mùi thơm của gạo nếp hòa quyện với hương thơm của ống nứa rừng tạo nên vị ngọt bùi khó cưỡng.", "6-7", 1),
    ("Xôi ngũ sắc Tây Bắc", "Món xôi dẻo thơm có 5 màu rực rỡ (đỏ, vàng, xanh, tím, trắng) nhuộm từ lá cây rừng tự nhiên của người Thái là gì?", "Xôi ngũ sắc", ["Xôi gấc", "Xôi đỗ xanh", "Xôi lạc"], "Năm màu xôi tượng trưng cho ngũ hành Kim, Mộc, Thủy, Hỏa, Thổ mang ý nghĩa cầu mong may mắn tốt lành.", "7-8", 2),
    ("Cốm làng Vòng Hà Nội", "Hạt nếp non xanh non bấm ra sữa được rang giã tỉ mỉ bọc trong lá sen thơm ngát vào mùa thu Hà Nội là gì?", "Cốm làng Vòng", ["Bánh cốm", "Chè cốm", "Xôi cốm"], "Cốm Vòng thơm thảo là thức quà tinh tế mùa thu, gắn liền với ngòi bút tài hoa của nhà văn Thạch Lam.", "6-7", 1),
    ("Kẹo cu đơ Hà Tĩnh", "Món kẹo đặc sản giòn ngọt bùi nấu từ mật mía, gừng tươi và hạt lạc kẹp giữa hai miếng bánh tráng nướng là gì?", "Kẹo Cu Đơ (Hà Tĩnh)", ["Kẹo dừa Bến Tre", "Kẹo mè xửng Huế", "Kẹo Sìu Châu"], "Uống bát nước chè xanh chát ấm cắn miếng kẹo cu đơ cay ngọt là nét ẩm thực dân dã ấm lòng miền Trung.", "7-8", 2),
    ("Mè xửng cố đô Huế", "Thứ kẹo dẻo ngọt làm từ mạch nha, vừng mè và lạc thơm bùi thường được du khách mua làm quà khi đến Huế là gì?", "Kẹo Mè xửng Huế", ["Kẹo kéo", "Kẹo chuối", "Kẹo dừa"], "Mè xửng nhâm nhi cùng chén trà sen cung đình Huế thanh nhã là thú tao nhã của người dân cố đô.", "7-8", 2),
    ("Kẹo dừa Bến Tre béo ngậy", "Đặc sản kẹo ngọt thơm béo ngậy nấu từ nước cốt dừa tươi nguyên chất gói trong lớp bánh tráng mỏng ăn được là gì?", "Kẹo dừa Bến Tre", ["Kẹo đậu phộng", "Kẹo sầu riêng", "Kẹo thốt nốt"], "Bà Nguyễn Thị Vinh là người đầu tiên sáng chế ra nghề làm kẹo dừa tại thị trấn Mỏ Cày năm 1970.", "6-7", 1),
    ("Nước mắm cá cơm Phú Quốc", "Gia vị truyền thống cốt lõi trong bữa cơm Việt được ủ chượp từ cá cơm tươi và muối hạt trong thùng gỗ bời lời là gì?", "Nước mắm truyền thống Phú Quốc (và Phan Thiết)", ["Nước tương", "Dầu hào", "Giấm gạo"], "Nước mắm màu nâu cánh gián, đậm đà vị ngọt đạm tự nhiên là linh hồn ẩm thực Việt Nam được bảo hộ chỉ dẫn địa lý tại châu Âu.", "7-8", 2),
    ("Chè Thái Nguyên đệ nhất danh trà", "Búp chè một tôm hai lá vùng Tân Cương sao khô xoăn như móc câu, nước xanh vàng óng vị tiền chát hậu ngọt là gì?", "Chè Tân Cương Thái Nguyên", ["Chè Suối Giàng", "Chè San Tuyết", "Chè Ô Long"], "Uống trà là nét văn hóa ứng xử thanh cao, 'khách đến nhà không trà thì bánh' thể hiện lòng hiếu khách của người Việt.", "7-8", 2),
    ("Trang phục Áo tứ thân", "Trang phục cổ truyền của người phụ nữ nông thôn Bắc Bộ xưa gồm 4 vạt áo thắt dải yếm đào thắt lưng xanh là gì?", "Áo tứ thân", ["Áo dài", "Áo bà ba", "Áo chàm"], "Áo tứ thân gắn liền với chiếc nón quai thao và chiếc khăn mỏ quạ duyên dáng của các liền chị quan họ.", "7-8", 2),
    ("Trang phục Áo bà ba", "Chiếc áo giản dị xẻ tà hai bên hông có hai túi trước ngực gắn liền với người dân lao động Nam Bộ là gì?", "Áo bà ba", ["Áo tứ thân", "Áo chàm", "Áo dài"], "Áo bà ba bằng vải lụa hoặc gấm tôn lên vẻ đẹp mộc mạc, khỏe khoắn của người phụ nữ trên bến dưới thuyền.", "6-7", 1),
    ("Trang phục dệt thổ cẩm", "Vải thổ cẩm thủ công dệt hoa văn hình học rực rỡ sắc màu bằng sợi bông nhuộm củ rừng là nét văn hóa của đồng bào nào?", "Đồng bào các dân tộc vùng núi cao (H'Mông, Dao, Thái, Mường...)", ["Người Kinh ở đồng bằng", "Người nước ngoài", "Không có ai dệt"], "Những bộ váy xòe thổ cẩm xúng xính hoa văn cầu kỳ thể hiện sự khéo léo, kiên nhẫn và thẩm mỹ của các thiếu nữ vùng cao.", "7-8", 2),
    ("Nhà sàn của người miền núi", "Kiểu nhà truyền thống bằng gỗ nứa dựng trên các cột trụ cao cách mặt đất của đồng bào vùng cao gọi là gì?", "Nhà sàn", ["Nhà rông", "Nhà ngói", "Nhà đất"], "Nhà sàn giúp người dân tránh được thú dữ, ẩm ướt của đất rừng và đón gió mát mẻ trong lành.", "6-7", 1),
    ("Nhà rông mái cao Tây Nguyên", "Ngôi nhà cộng đồng to lớn nhất buôn làng Tây Nguyên có mái nhọn vút cao như lưỡi búa vươn lên trời xanh là gì?", "Nhà rông Tây Nguyên", ["Nhà dài", "Nhà sàn", "Chòi canh"], "Nhà rông là trái tim của buôn làng, nơi già làng họp bàn việc lớn, tổ chức lễ hội cồng chiêng và tiếp đón khách quý.", "7-8", 2),
    ("Nhà dài của người Ê-đê", "Ngôi nhà truyền thống của người Ê-đê dài hàng chục mét như một tiếng chuông ngân, cứ mỗi khi con gái lấy chồng lại nối dài thêm là gì?", "Nhà dài Ê-đê", ["Nhà rông", "Nhà lá", "Nhà ống"], "Cầu thang nhà dài chạm khắc hình đôi bầu sữa mẹ và vầng trăng khuyết thể hiện chế độ mẫu hệ tôn kính người phụ nữ.", "8-9", 3),
    ("Tục ăn trầu têm cánh phượng", "Miếng trầu têm cánh phượng khéo léo gồm lá trầu xanh, miếng cau vàng và chút vôi trắng gắn liền với truyền thuyết nào?", "Sự tích Trầu Cau", ["Sự tích quả dưa hấu", "Sự tích Bánh chưng", "Sự tích cây khế"], "'Miếng trầu là đầu câu chuyện', miếng trầu cau thắm đỏ tượng trưng cho tình nghĩa anh em hòa thuận và tình cảm vợ chồng son sắt thủy chung.", "6-7", 1),
    ("Cây nêu ngày Tết", "Cây tre cao dựng trước sân nhà vào ngày 23 tháng Chạp tiễn ông Táo có treo chuông gió và khánh đất để làm gì?", "Xua đuổi ma quỷ và báo hiệu mùa xuân may mắn về", ["Để chim bồ câu đậu", "Làm cột cờ", "Để phơi quần áo"], "Dân gian có câu: 'Thịt mỡ, dưa hành, câu đối đỏ / Cây nêu, tràng pháo, bánh chưng xanh' tóm trọn không khí Tết xưa.", "7-8", 2),
    ("Lễ cúng ông Công ông Táo", "Vào ngày 23 tháng Chạp âm lịch hàng năm, người dân thả cá chép đỏ xuống sông hồ nhằm mục đích gì?", "Làm phương tiện cho ông Táo cưỡi bay về trời báo cáo Ngọc Hoàng việc trần gian", ["Để nuôi cá lớn", "Cho cá tắm mát", "Để bắt cá ăn"], "Cá chép vượt vũ môn hóa rồng mang ước nguyện về sự thăng tiến, may mắn và tài lộc cho gia đình trong năm mới.", "6-7", 1),
    ("Mâm cơm tất niên chiều 30 Tết", "Bữa cơm đầm ấm chiều cuối năm quy tụ đầy đủ các thành viên gia đình cảm tạ tổ tiên và tiễn năm cũ gọi là gì?", "Mâm cơm Tất niên", ["Cơm tân niên", "Cơm hội nghị", "Cơm trưa"], "Khói hương trầm thơm ngát cùng mâm cơm tất niên ấm áp là khoảnh khắc thiêng liêng nhất kết nối các thế hệ trong gia đình.", "6-7", 1),
    ("Phong tục xông đất đầu năm", "Người khách đầu tiên bước vào chúc Tết gia đình vào sáng mùng Một Tết được gọi là gì?", "Người xông đất (Xông nhà)", ["Người bán hàng", "Người đưa thư", "Người gác cổng"], "Gia chủ thường nhờ người vui vẻ, tốt tính, hợp tuổi đến xông nhà để mang lại may mắn hanh thông suốt cả năm.", "7-8", 2),
    ("Phong tục mừng tuổi (lì xì)", "Những phong bao giấy đỏ tươi chứa tiền mới may mắn người lớn tặng trẻ em dịp đầu năm mới gọi là gì?", "Tiền mừng tuổi (Lì xì)", ["Tiền mua kẹo", "Tiền học phí", "Tiền tiết kiệm"], "Màu đỏ của phong bao tượng trưng cho sự may mắn, chúc các bạn nhỏ thêm một tuổi mới chăm ngoan học giỏi.", "6-7", 1),
    ("Lễ hội hoa tam giác mạch", "Lễ hội mùa đông rực rỡ với những cánh đồng hoa tím hồng trên cao nguyên đá thuộc tỉnh nào?", "Tỉnh Hà Giang (Đồng Văn)", ["Tỉnh Lào Cai", "Tỉnh Yên Bái", "Tỉnh Sơn La"], "Hoa tam giác mạch nhỏ nhắn mọc trên đá tai mèo cằn cỗi là biểu tượng cho sức sống kiên cường của đồng bào vùng biên cương.", "7-8", 2),
    ("Hát then của người Tày", "Nghi lễ tâm linh độc đáo kết hợp âm nhạc, ca từ và điệu múa của đồng bào Tày, Nùng để tạ ơn thần linh là gì?", "Hát Then", ["Hát Chèo", "Hát Tuồng", "Hát Xẩm"], "Cây đàn Tính cùng chùm xóc nhạc rung vang đưa lời thỉnh cầu của con người lên các đấng siêu nhiên mong mùa màng tốt tươi.", "8-9", 3),
    ("Chợ tình Sa Pa", "Nét sinh hoạt văn hóa giao duyên truyền thống độc đáo của các chàng trai cô gái H'Mông, Dao đỏ vào tối thứ Bảy ở Sa Pa là gì?", "Chợ tình Sa Pa", ["Chợ nổi", "Chợ hoa quả", "Chợ bò"], "Tiếng khèn Mông réo rắt gọi bạn tình cùng tiếng chuông ngựa lách cách tạo nên không gian văn hóa lãng mạn nơi phố núi sương mờ.", "7-8", 2),
    ("Lễ hội đâm trâu Tây Nguyên", "Lễ hội truyền thống cổ xưa của đồng bào Bana, Êđê tạ ơn thần linh đã ban cho buôn làng vụ mùa ấm no là lễ hội gì?", "Lễ hội Đâm trâu (Lễ ăn trâu)", ["Lễ hội Cầu ngư", "Lễ hội Đua voi", "Lễ hội Chọi gà"], "Ngày nay lễ hội được tổ chức với các nghi thức văn hóa biểu diễn cồng chiêng và múa xoang truyền thống hòa bình.", "8-9", 3),
    ("Lễ hội Đua voi Buôn Đôn", "Lễ hội mùa xuân rộn rã trên thảo nguyên Đắk Lắk nơi những chú voi rừng thuần dưỡng thi chạy và bơi vượt sông Sêrêpôk là gì?", "Lễ hội Đua voi Buôn Đôn", ["Đua ngựa", "Đua trâu", "Đua lạc đà"], "Buôn Đôn nổi tiếng với truyền thống săn bắt và thuần dưỡng voi rừng của vua voi Khun Ju Nốp huyền thoại.", "7-8", 2)
]

raw_mc.extend(extra_ls_41)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"LS{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Lịch Sử & Văn Hóa",
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
    qid = f"LS{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Lịch Sử & Văn Hóa",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/ls_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Hoàn thành toàn bộ LS: {len(questions)} câu đã được ghi vào ls_140.json")
