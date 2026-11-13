# -*- coding: utf-8 -*-
import json
import random

imgs = [
    "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1497250681960-ef046c08a56e?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?w=600&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?w=600&auto=format&fit=crop&q=80"
]

# 126 MC items
raw_mc = [
    # 1-30 Bộ phận và chức năng cây
    ("Rễ cây cắm sâu", "Bộ phận nào của cây đâm sâu vào lòng đất để hút nước, chất khoáng và giữ cây đứng vững?", "Rễ cây", ["Thân cây", "Lá cây", "Hoa"], "Rễ hút nước và muối khoáng hòa tan trong đất để nuôi toàn bộ cây phát triển.", "6-7", 1),
    ("Thân cây vận chuyển", "Bộ phận nào của cây nối liền rễ với cành lá, giúp dẫn nước và nâng đỡ toàn bộ tán cây?", "Thân cây", ["Lá cây", "Nụ hoa", "Quả ngọt"], "Thân cây chứa các mạch gỗ và mạch rây giúp vận chuyển nước và chất dinh dưỡng hai chiều.", "6-7", 1),
    ("Lá cây quang hợp", "Bộ phận nào của cây thường có màu xanh lục, thực hiện nhiệm vụ quang hợp chế tạo chất dinh dưỡng?", "Lá cây", ["Rễ cây", "Vỏ cây", "Hạt giống"], "Lá cây chứa chất diệp lục hấp thu ánh sáng mặt trời để quang hợp nuôi cây và tạo khí oxy.", "6-7", 1),
    ("Khí oxy từ cây", "Trong quá trình quang hợp vào ban ngày, lá cây hấp thụ khí cacbonic (CO2) và thải ra khí gì có lợi cho sự sống?", "Khí Oxy (O2)", ["Khí Nitơ", "Khí Độc", "Khí Gas"], "Nhờ nhả khí oxy qua quang hợp, cây xanh được ví như 'nhà máy sản xuất oxy' của Trái Đất.", "6-7", 1),
    ("Quang hợp ban ngày", "Quá trình cây xanh tự chế tạo chất dinh dưỡng từ nước và CO2 nhờ ánh sáng mặt trời gọi là gì?", "Quang hợp", ["Hô hấp", "Thoát hơi nước", "Rụng lá"], "Quang hợp là phản ứng kỳ diệu biến năng lượng ánh sáng thành năng lượng hóa học nuôi cây.", "7-8", 2),
    ("Hoa thụ phấn", "Bộ phận rực rỡ sắc hương của cây có nhiệm vụ thu hút ong bướm thụ phấn và tạo quả là gì?", "Bông hoa", ["Rễ cây", "Thân cây", "Gai nhọn"], "Hoa là cơ quan sinh sản của thực vật hạt kín, gồm đài, tràng (cánh hoa), nhị và nhụy.", "6-7", 1),
    ("Hạt giống nảy mầm", "Hạt giống cây xanh cần những điều kiện tự nhiên thiết yếu nào để nảy mầm thuận lợi?", "Đủ nước, không khí và nhiệt độ ấm áp thích hợp", ["Chỉ cần bóng tối", "Cần nước sôi 100 độ", "Cần gió bão mạnh"], "Hạt hút nước trương lên, hô hấp cần oxy và nhiệt độ ấm áp để phôi thai thức giấc nảy mầm.", "6-7", 1),
    ("Quả bảo vệ hạt", "Bộ phận nào của cây hình thành từ bầu nhụy sau khi hoa thụ phấn, có thịt thơm ngon bảo vệ hạt bên trong?", "Quả ngọt", ["Lá xanh", "Vỏ thân", "Rễ cọc"], "Quả bảo vệ hạt và giúp phát tán hạt giống đi xa nhờ chim muông và con người ăn rồi thải hạt.", "6-7", 1),
    ("Rễ cọc", "Loài rễ có một rễ cái to khỏe đâm thẳng sâu xuống đất cùng nhiều rễ con đâm ngang gọi là rễ gì?", "Rễ cọc", ["Rễ chùm", "Rễ thở", "Rễ củ"], "Cây bàng, cây phượng, cây đậu có rễ cọc bám rất chắc vào lòng đất chống bão gió.", "7-8", 2),
    ("Rễ chùm", "Loài rễ gồm nhiều rễ con dài gần bằng nhau mọc tỏa ra từ gốc thân cây gọi là rễ gì?", "Rễ chùm", ["Rễ cọc", "Rễ củ", "Rễ bám"], "Cây lúa, cây ngô, cây cỏ, cây hành có rễ chùm bám trên tầng đất mặt màu mỡ.", "7-8", 2),
    ("Rễ củ tích lũy", "Củ cà rốt, củ khoai lang, củ sắn mà chúng ta ăn thực chất là do bộ phận nào của cây phình to thành?", "Rễ cây phình to (Rễ củ)", ["Thân cây bò", "Lá cây cuộn", "Hoa nở ra"], "Rễ cây tích lũy nhiều tinh bột và chất dinh dưỡng phình to ra tạo thành củ.", "7-8", 2),
    ("Thân củ khoai tây", "Củ khoai tây có các mắt chồi nảy mầm thực chất là biến dạng của bộ phận nào?", "Thân cây (Thân củ)", ["Rễ cây", "Lá cây", "Hoa cây"], "Khoai tây là thân ngầm phình to dưới đất, trên vỏ có các mắt chồi có thể mọc thành cây mới.", "8-9", 3),
    ("Thân leo bằng tua cuốn", "Cây mướp, cây bầu, cây bí bò lên giàn cao nhờ bộ phận hỗ trợ nào?", "Tua cuốn ở thân", ["Rễ cọc nhọn", "Cánh hoa cứng", "Gai góc"], "Tua cuốn quấn chặt vào que giàn giúp cây leo lên cao đón nhận nhiều ánh nắng mặt trời.", "6-7", 1),
    ("Thân gỗ to lớn", "Thân cây lim, cây bạch đàn, cây đa cứng cáp và sống lâu năm thuộc loại thân gì?", "Thân gỗ", ["Thân thảo (cỏ)", "Thân leo", "Thân bò"], "Thân gỗ có lớp vỏ ngoài bảo vệ và thớ gỗ chắc nịch giúp cây vươn cao hàng chục mét.", "6-7", 1),
    ("Thân thảo mềm yếu", "Cây lúa, cây ngô, cây rau muống có thân mềm, xốp, không có thớ gỗ gọi là thân gì?", "Thân thảo", ["Thân gỗ", "Thân leo", "Thân gai"], "Thân thảo mềm, chứa nhiều nước và thường có vòng đời ngắn trong một hoặc vài mùa vụ.", "6-7", 1),
    ("Chất diệp lục", "Chất màu xanh trong lá cây có vai trò quyết định trong việc hấp thụ năng lượng mặt trời là gì?", "Chất diệp lục (Chlorophyll)", ["Chất canxi", "Chất đạm", "Chất sắt"], "Chất diệp lục giúp lá hấp thu ánh sáng màu đỏ và xanh lam, phản xạ lại ánh sáng xanh lục nên ta thấy lá màu xanh.", "7-8", 2),
    ("Khí khổng ở lá", "Các lỗ li ti trên bề mặt lá cây giúp cây trao đổi khí và thoát hơi nước ra ngoài gọi là gì?", "Khí khổng (Lỗ khí)", ["Rãnh lá", "Màng lá", "Gân lá"], "Khí khổng có thể đóng mở linh hoạt để điều tiết lượng nước thoát ra ngoài tránh cho cây bị héo úa.", "8-9", 3),
    ("Cây xương rồng lá biến gai", "Tại sao lá của cây xương rồng sống ở sa mạc lại biến đổi thành những chiếc gai nhọn hoắt?", "Để giảm thoát hơi nước trong điều kiện khô hạn", ["Để chống chim đậu", "Để đón ánh nắng tốt hơn", "Để tích lũy đường"], "Gai nhọn giúp xương rồng không bị mất nước qua bốc hơi, thân mọng nước của nó đảm nhận việc quang hợp.", "7-8", 2),
    ("Vòng năm thân gỗ", "Khi cưa ngang một thân cây gỗ cổ thụ, người ta thấy những vòng tròn đồng tâm giúp biết điều gì?", "Tuổi thọ của cây và điều kiện khí hậu từng năm", ["Số lượng lá trên cây", "Độ sâu của rễ cây", "Màu sắc của hoa"], "Mỗi năm cây thân gỗ phát triển thêm một vòng gỗ mới; vòng sáng vào mùa mưa, vòng sẫm vào mùa khô.", "8-9", 3),
    ("Cây bắt mồi nắp ấm", "Cây nắp ấm bắt và tiêu hóa côn trùng chủ yếu để bổ sung chất dinh dưỡng nào mà đất nghèo thiếu hụt?", "Chất đạm (Nitơ)", ["Nước uống", "Chất đường", "Ánh sáng"], "Đất đầm lầy cằn cỗi thiếu nitơ, lá nắp ấm biến thành bình chứa dịch tiêu hóa xác côn trùng để lấy đạm.", "8-9", 3),

    # 31-60 Cây lương thực & Nông nghiệp
    ("Cây lúa nước", "Cây lương thực quan trọng nhất của người dân Việt Nam, cho ra hạt thóc xay thành gạo trắng là cây gì?", "Cây lúa nước", ["Cây ngô", "Cây khoai", "Cây sắn"], "Việt Nam là một trong những quốc gia xuất khẩu gạo hàng đầu thế giới với nền văn minh lúa nước ngàn năm.", "6-7", 1),
    ("Cây ngô bắp vàng", "Cây lương thực có bắp hạt vàng óng ả, râu ngô dài như tóc tiên và thân thẳng là cây gì?", "Cây ngô (Cây bắp)", ["Cây mía", "Cây sắn", "Cây đậu"], "Bắp ngô luộc thơm bùi cung cấp nhiều tinh bột, chất xơ và vitamin bổ dưỡng.", "6-7", 1),
    ("Khoai lang bùi ngọt", "Loài dây leo trồng lấy củ dưới đất, củ có ruột vàng hoặc tím, bùi ngọt thơm ngon là gì?", "Khoai lang", ["Củ cải", "Cà rốt", "Hành tây"], "Khoai lang rất giàu chất xơ, vitamin A và tinh bột lành mạnh cho hệ tiêu hóa.", "6-7", 1),
    ("Cây sắn (khoai mì)", "Củ của cây thân gỗ nhỏ nào được dùng để làm bột năng, làm bánh tằm và thức ăn chăn nuôi?", "Cây sắn (Khoai mì)", ["Cây củ từ", "Khoai môn", "Củ đậu"], "Củ sắn chứa hàm lượng tinh bột dồi dào, cần ngâm luộc kỹ để loại bỏ độc tố tự nhiên trước khi ăn.", "7-8", 2),
    ("Cây mía cho đường", "Cây thân thảo cao lớn có gióng đốt, thân chứa đầy nước ngọt lịm ép ra làm đường cát trắng là gì?", "Cây mía", ["Cây tre", "Cây sậy", "Cây chuối"], "Thân mía chứa hàm lượng đường saccarozo rất cao, là nguyên liệu chính của các nhà máy đường.", "6-7", 1),
    ("Cây đậu nành (đậu tương)", "Hạt của loại cây họ đậu nào được dùng để làm sữa đậu nành và những bìa đậu phụ thơm ngon?", "Đậu nành (Đậu tương)", ["Đậu phộng", "Đậu đỏ", "Đậu đen"], "Đậu nành chứa hàm lượng protein thực vật dồi dào, rất tốt cho sức khỏe tim mạch.", "6-7", 1),
    ("Cây lạc (đậu phộng)", "Loài cây họ đậu nào sau khi hoa thụ phấn thì cuống hoa đâm chui xuống lòng đất để kết củ?", "Cây lạc (Đậu phộng)", ["Đậu xanh", "Đậu cove", "Đậu Hà Lan"], "Hiện tượng hoa nở trên cạn nhưng quả vùi lớn lên dưới đất nên đậu phộng còn có tên Hán Việt là 'Lạc hoa sinh'.", "7-8", 2),
    ("Cây cà phê Tây Nguyên", "Cây công nghiệp trồng nhiều ở vùng đất đỏ Tây Nguyên, hạt rang xay tạo ra thức uống thơm nồng nàn là gì?", "Cây cà phê", ["Cây cao su", "Cây chè", "Cây ca cao"], "Việt Nam là nước xuất khẩu cà phê Robusta lớn nhất thế giới, nổi tiếng với vùng đất Buôn Ma Thuột.", "7-8", 2),
    ("Cây chè xanh (trà)", "Búp và lá non của loài cây nào trên vùng cao Thái Nguyên được hái về sao khô pha nước uống thanh mát?", "Cây chè (Cây trà)", ["Cây bạc hà", "Cây bưởi", "Cây xoan"], "Nước chè xanh chứa nhiều chất chống oxy hóa giúp cơ thể thanh nhiệt và tinh thần tỉnh táo.", "6-7", 1),
    ("Cây cao su lấy mủ", "Loài cây thân gỗ lớn nào khi cạo vỏ thân sẽ chảy ra dòng nhựa trắng đục dùng làm lốp xe?", "Cây cao su", ["Cây thông", "Cây bạch đàn", "Cây xà cừ"], "Mủ cao su là nguyên liệu tự nhiên tuyệt vời có tính đàn hồi cao dùng làm gối, nệm và lốp xe máy ô tô.", "7-8", 2),
    ("Cây hồ tiêu", "Loài dây leo bám trên trụ đá cho chùm hạt nhỏ cay nồng làm gia vị thơm ngon cho món canh là gì?", "Cây hồ tiêu (Hạt tiêu)", ["Cây ớt", "Cây gừng", "Cây mù tạt"], "Việt Nam là cường quốc xuất khẩu hạt tiêu số 1 thế giới với chất lượng cay thơm đặc sắc.", "7-8", 2),
    ("Cây điều lấy hạt", "Cây ăn quả có phần hạt hình thận thò ra ngoài một quả giả mọng nước màu đỏ vàng là cây gì?", "Cây điều (Đào lộn hột)", ["Cây óc chó", "Cây mắc ca", "Cây hạnh nhân"], "Hạt điều béo bùi, giàu chất béo tốt và khoáng chất, được xuất khẩu đi khắp các nước trên thế giới.", "7-8", 2),
    ("Cây dừa Bến Tre", "Cây thân cột cao lớn, lá xòe rộng, quả chứa đầy nước ngọt thanh mát là biểu tượng của xứ Bến Tre?", "Cây dừa", ["Cây cau", "Cây cọ", "Cây thốt nốt"], "Cây dừa có ích từ rễ đến ngọn: nước giải khát, cùi làm dầu và mứt, lá lợp nhà, thân làm cầu dừa.", "6-7", 1),
    ("Cây chuối trổ buồng", "Cây thân giả to tròn, hoa chuối nở thành từng nải chuối xếp tầng tạo thành buồng chuối trĩu quả?", "Cây chuối", ["Cây đu đủ", "Cây dứa", "Cây cọ"], "Quả chuối chín mềm ngọt, giàu kali và vitamin B6 giúp bé tràn đầy năng lượng khi vui chơi.", "6-7", 1),
    ("Cây xoài quả thơm", "Quả xoài chín có vỏ màu gì và vị thế nào?", "Vỏ màu vàng ruộm, vị ngọt đậm thơm mát", ["Vỏ màu xanh lục, vị mặn chát", "Vỏ màu tím đen, vị cay nồng", "Vỏ màu trắng phau"], "Xoài Cát Hòa Lộc của đồng bằng sông Cửu Long thơm ngọt nức tiếng gần xa.", "6-7", 1),
    ("Cây sầu riêng vua trái cây", "Quả sầu riêng có lớp vỏ ngoài đầy gai nhọn hoắt, ruột vàng béo ngậy được mệnh danh là gì?", "Vua của các loài trái cây", ["Nữ hoàng trái cây", "Chúa tể thảo mộc", "Thần rừng"], "Sầu riêng có mùi hương nồng nàn đặc trưng và vị ngọt béo ngậy như kem bơ.", "7-8", 2),
    ("Quả măng cụt nữ hoàng", "Loài quả có vỏ tím sẫm dày, múi trắng muốt ngọt thanh mát được mệnh danh là 'Nữ hoàng trái cây'?", "Quả măng cụt", ["Quả thanh long", "Quả bưởi", "Quả cam sành"], "Măng cụt có tính hàn làm mát cơ thể, thường được ăn kết hợp cùng sầu riêng có tính nóng.", "7-8", 2),
    ("Cây thanh long", "Loài cây họ xương rồng có thân bò leo rủ xuống, quả có tai xanh vỏ đỏ ruột trắng hoặc đỏ là cây gì?", "Cây thanh long", ["Cây dưa hấu", "Cây lê ki ma", "Cây hồng xiêm"], "Thanh long Bình Thuận ngọt mát, chứa nhiều hạt vừng đen nhỏ giúp nhuận tràng tiêu hóa tốt.", "6-7", 1),
    ("Cây dưa hấu giải nhiệt", "Quả dưa hấu có vỏ xanh sọc đen, ruột đỏ mọng nước gắn liền với truyền thuyết dân gian nào của Việt Nam?", "Sự tích Mai An Tiêm ở đảo hoang", ["Sự tích quả bầu mẹ", "Sự tích cây khế", "Sự tích bánh chưng"], "Mai An Tiêm nhờ tìm thấy hạt dưa do chim tha đến đảo mà đã gieo trồng nên giống dưa hấu ngọt lành.", "6-7", 1),
    ("Quả mít nhiều múi", "Quả mít có lớp vỏ gai sần sùi, khi chín thơm phức cả góc vườn, bên trong có gì?", "Nhiều múi mít vàng óng bọc lấy hạt mít", ["Một hạt tròn to duy nhất", "Không có hạt nào cả", "Chỉ toàn nước"], "Mít mật, mít dai thơm ngọt, xơ mít cũng có thể dùng làm dưa muối rất ngon.", "6-7", 1),

    # 61-90 Rau củ & Dược liệu & Hoa lá
    ("Củ gừng làm ấm", "Củ gừng mọc dưới đất có vị cay ấm, thường được dùng để nấu trà gừng giải cảm mùa đông là do đâu?", "Gừng có tinh dầu giúp làm ấm cơ thể và kích thích tiêu hóa", ["Gừng có vị ngọt", "Gừng có tính hàn làm lạnh", "Gừng chứa nhiều vitamin C"], "Gừng là vị thuốc dân gian quen thuộc trị đầy bụng, ho và giữ ấm cơ thể rất hiệu quả.", "7-8", 2),
    ("Củ tỏi kháng sinh tự nhiên", "Củ tỏi có nhiều tép nhỏ, vị cay nồng, chứa hợp chất allicin được ví như gì?", "Một loại kháng sinh tự nhiên diệt khuẩn", ["Một loại thuốc nhuộm màu", "Một loại đường hóa học", "Một chất béo bão hòa"], "Ăn tỏi giúp tăng cường sức đề kháng cho hệ miễn dịch phòng chống cảm cúm mùa đông.", "7-8", 2),
    ("Củ nghệ màu vàng", "Củ nghệ có ruột màu vàng cam đậm chứa hoạt chất curcumin thường dùng để làm gì?", "Làm lành vết thương, vết loét dạ dày và nhuộm màu món ăn", ["Làm bột giặt quần áo", "Pha nước ngọt", "Làm đông đá"], "Nghệ giúp mau liền sẹo và tạo màu vàng đẹp mắt cho món cà ri, bánh xèo.", "7-8", 2),
    ("Cây sả thơm ngát", "Cây sả mọc thành bụi có lá sắc và thân gốc thơm lừng tinh dầu, có tác dụng đuổi loài vật nào?", "Đuổi muỗi và côn trùng", ["Đuổi chim bồ câu", "Đuổi cá bơi lội", "Đuổi thỏ con"], "Mùi tinh dầu sả chanh làm rối loạn định hướng của muỗi khiến chúng bay xa.", "6-7", 1),
    ("Cây nha đam mọng nước", "Cây nha đam (lô hội) có lá dày chứa lớp gel trong suốt mát lạnh thường được dùng để làm gì?", "Làm dịu vết bỏng nhẹ, nấu chè và dưỡng ẩm da", ["Làm củi đun lửa", "Làm lốp xe", "Làm giấy viết"], "Lớp thạch nha đam thanh mát, giòn sần sật giúp thanh nhiệt cơ thể ngày hè nắng nóng.", "7-8", 2),
    ("Cây bạc hà cay mát", "Lá bạc hà có mùi thơm cay mát lạnh sảng khoái là do chứa chất gì?", "Chất menthol (tinh dầu bạc hà)", ["Chất canxi", "Chất axit chua", "Chất đường mía"], "Menthol kích thích thụ thể cảm nhận lạnh trên lưỡi giúp ta có cảm giác thơm mát sảng khoái.", "8-9", 3),
    ("Hoa sen quốc hoa", "Loài hoa thanh khiết nở trên đầm bùn 'Gần bùn mà chẳng hôi tanh mùi bùn' là biểu tượng văn hóa Việt Nam?", "Hoa sen", ["Hoa súng", "Hoa bèo tây", "Hoa lục bình"], "Hoa sen có hương thơm dịu mát, hạt sen bổ dưỡng nấu chè, tim sen an thần giúp ngủ ngon.", "6-7", 1),
    ("Hoa mai vàng phương Nam", "Loài hoa cánh vàng tươi rực rỡ tượng trưng cho sự may mắn, nở rộ vào dịp Tết Nguyên Đán ở miền Nam là hoa gì?", "Hoa mai", ["Hoa cúc", "Hoa đào", "Hoa lay ơn"], "Cành mai vàng khoe sắc trong nắng ấm phương Nam báo hiệu một năm mới an khang thịnh vượng.", "6-7", 1),
    ("Hoa đào hồng phương Bắc", "Loài hoa cánh hồng phớt chúm chím nở trong tiết trời se lạnh mùa xuân đón Tết ở miền Bắc là hoa gì?", "Hoa đào", ["Hoa mai", "Hoa hồng", "Hoa đồng tiền"], "Hoa đào Nhật Tân thắm sắc cùng bánh chưng xanh làm nên nét xuân truyền thống miền Bắc.", "6-7", 1),
    ("Hoa phượng vĩ học trò", "Loài hoa có sắc đỏ rực rỡ như lửa nở rộ trên sân trường gắn liền với mùa hè chia tay của học trò?", "Hoa phượng vĩ", ["Hoa bàng", "Hoa bằng lăng", "Hoa dạ yến thảo"], "Cây phượng vĩ nở hoa đỏ rực cùng tiếng ve sầu ngân vang báo hiệu kỳ nghỉ hè vui tươi đã đến.", "6-7", 1),
    ("Hoa bằng lăng tím", "Cùng với hoa phượng, loài hoa có màu tím biếc nở thành từng chùm dịu dàng trên phố mùa hè là hoa gì?", "Hoa bằng lăng", ["Hoa sim tím", "Hoa mua", "Hoa oải hương"], "Hoa bằng lăng tím mang nét đẹp mộng mơ, che bóng mát trên nhiều con đường trường học.", "6-7", 1),
    ("Cây bàng tán tròn", "Cây bóng mát sân trường có lá to bản hình thìa, quả chín vàng ngọt thơm và hạt bùi béo là cây gì?", "Cây bàng", ["Cây phượng", "Cây xà cừ", "Cây sấu"], "Mùa thu lá bàng chuyển sang màu đỏ rực rỡ rồi rụng xuống, mùa xuân lại đâm chồi xanh non mơn mởn.", "6-7", 1),
    ("Hoa hướng dương theo nắng", "Loài hoa lớn màu vàng tươi luôn có tập tính quay đầu hướng về phía Mặt Trời mọc là hoa gì?", "Hoa hướng dương", ["Hoa cúc vạn thọ", "Hoa đồng tiền", "Hoa hồng"], "Đặc tính hướng nhật (heliotropism) giúp hoa hướng dương đón nhận tối đa ánh sáng mặt trời.", "6-7", 1),
    ("Cây trinh nữ (cây xấu hổ)", "Khi ta vô tình chạm tay vào lá cây trinh nữ (xấu hổ), hiện tượng thú vị gì sẽ xảy ra?", "Các cặp lá con lập tức cụp khép lại và cuống lá gục xuống", ["Cây phát ra tiếng còi", "Lá cây biến thành màu đỏ", "Cây bắn gai ra xa"], "Đây là phản ứng tự vệ do sự thay đổi áp suất nước đột ngột ở các khớp cuống lá khi có va chạm.", "7-8", 2),
    ("Hoa mười giờ", "Loài hoa nhỏ xinh trồng viền bồn hoa thường nở bung sắc rực rỡ vào khoảng 10 giờ sáng nắng ấm là hoa gì?", "Hoa mười giờ", ["Hoa cúc", "Hoa lan", "Hoa dâm bụt"], "Hoa mười giờ ưa nắng gắt, cánh hoa mỏng manh đa màu: đỏ, hồng, cam, vàng, trắng.", "6-7", 1),
    ("Hoa quỳnh nở đêm", "Loài hoa trắng muốt quý phái chỉ hé nở cánh và tỏa hương ngào ngạt vào nửa đêm được gọi là gì?", "Hoa quỳnh (Nữ hoàng bóng đêm)", ["Hoa dạ lan hương", "Hoa nhài", "Hoa nguyệt quế"], "Hoa quỳnh nở về đêm để thu hút các loài bướm đêm và dơi đến thụ phấn, đến sáng sớm hoa đã tàn.", "8-9", 3),
    ("Cây bèo tây (lục bình)", "Loài cây thủy sinh trôi nổi trên sông rạch Nam Bộ có cuống lá phồng xốp chứa không khí là cây gì?", "Cây lục bình (Bèo tây)", ["Rau muống nước", "Cây sen", "Cây súng"], "Cuống lá phồng xốp như phao bơi giúp cây bèo tây nổi bồng bềnh và trôi theo dòng nước phù sa.", "6-7", 1),
    ("Rong đuôi chó quang hợp", "Cây rong đuôi chó thả trong bể cá cảnh sủi bọt khí li ti dưới ánh đèn là do quá trình gì?", "Quang hợp nhả bọt khí oxy vào nước cho cá thở", ["Hô hấp nhả khói", "Rong bị nóng sôi", "Nước bị sủi bọt xà phòng"], "Rong nước quang hợp cung cấp nguồn oxy hòa tan tự nhiên dồi dào cho đàn cá bơi lội khỏe mạnh.", "7-8", 2),
    ("Cây đước rừng ngập mặn", "Loài cây nào ở rừng ngập mặn Cà Mau có bộ rễ chống hình nỏ vươn cao khỏi bùn lầy giữ đất biển?", "Cây đước", ["Cây tràm", "Cây bần", "Cây dừa nước"], "Hệ thống rễ cọc và rễ chống của cây đước đan kết như bức tường thành vững chắc chống sóng thần xói lở bờ biển.", "8-9", 3),
    ("Cây tràm U Minh", "Loài cây thân gỗ có vỏ xốp bong thành từng lớp, hoa thơm nuôi ong rừng tạo mật ong hoa tràm nức tiếng?", "Cây tràm", ["Cây bạch đàn", "Cây thông", "Cây keo"], "Rừng tràm U Minh Thượng và U Minh Hạ là khu dự trữ sinh quyển thế giới quý báu của Việt Nam.", "7-8", 2),

    # 91-115 Sinh thái & Bảo vệ rừng
    ("Rừng lá phổi xanh", "Tại sao các cánh rừng bạt ngàn lại được mệnh danh là 'Lá phổi xanh của Trái Đất'?", "Vì cây rừng hấp thụ khí CO2 và thải ra lượng lớn khí oxy trong lành", ["Vì lá rừng có màu xanh", "Vì rừng có nhiều loài thú", "Vì rừng ngăn mưa rơi"], "Không có rừng xanh, lượng khí nhà kính CO2 sẽ tăng vọt khiến Trái Đất nóng lên và thiếu oxy.", "6-7", 1),
    ("Rừng chống xói mòn", "Rễ cây rừng bám chằng chịt trong đất có vai trò vô cùng quan trọng nào sau đây vào mùa mưa bão?", "Giữ chặt đất, ngăn sạt lở núi và giảm lũ quét tàn phá", ["Làm đất bị khô cằn", "Làm nước mưa bốc hơi hết", "Làm cho đất bị lún sụt"], "Rừng đầu nguồn hoạt động như miếng bọt biển khổng lồ giữ nước mưa và nhả từ từ ra suối.", "7-8", 2),
    ("Cây xanh cản bụi tiếng ồn", "Trồng nhiều cây xanh dọc các tuyến phố đô thị mang lại lợi ích thiết thực nào?", "Hút bụi bẩn, giảm tiếng ồn xe cộ và làm bóng mát hạ nhiệt", ["Làm đường phố chật chội", "Thu hút nhiều sâu bọ", "Làm tốn nước tưới"], "Tán lá cây giữ lại các hạt bụi mịn và cản sóng âm thanh giúp không khí đô thị trong lành hơn.", "7-8", 2),
    ("Trồng cây gây rừng", "Bác Hồ từng phát động phong trào ý nghĩa nào vào mỗi dịp đầu xuân năm mới?", "'Tết trồng cây' vì lợi ích mười năm trồng cây, trăm năm trồng người", ["Tết quét dọn nhà", "Tết ăn uống linh đình", "Tết đi du lịch xa"], "Tết trồng cây đầu xuân đã trở thành nét đẹp văn hóa truyền thống của nhân dân ta suốt hơn 60 năm qua.", "6-7", 1),
    ("Cây tầm gửi ký sinh", "Loài cây nào không mọc rễ xuống đất mà cắm giác mút vào thân cành cây khác để hút nhựa sống?", "Cây tầm gửi", ["Cây phong lan", "Cây vạn tuế", "Cây trầu bà"], "Tầm gửi là loài thực vật bán ký sinh, sống nhờ vào nguồn nước và muối khoáng của cây chủ.", "8-9", 3),
    ("Cây phong lan bì sinh", "Cây phong lan bám trên thân cây gỗ lớn trong rừng có hút chất dinh dưỡng của cây gỗ không?", "Không, rễ lan lấy ẩm và bụi trong không khí, chỉ bám nhờ giá thể", ["Có, lan hút cạn nhựa cây gỗ", "Có, lan làm chết cây gỗ", "Lan ăn thịt cây gỗ"], "Phong lan là loài thực vật biểu sinh (bì sinh), rễ lan có lớp màng xốp hút ẩm sương mai từ khí trời.", "8-9", 3),
    ("Rêu mọc nơi ẩm ướt", "Loài thực vật nhỏ bé không có hoa, mọc thành từng mảng xanh mướt trên tường ẩm và vách đá râm mát là gì?", "Rêu", ["Cây dương xỉ", "Nấm rơm", "Cỏ may"], "Rêu chưa có mạch dẫn thực sự, chúng hấp thụ nước trực tiếp qua bề mặt thân và lá nhỏ li ti.", "7-8", 2),
    ("Cây dương xỉ lá non cuộn", "Loài cây cảnh ưa ẩm có lá non cuộn tròn hình chiếc gậy như đầu móc lò xo là cây gì?", "Cây dương xỉ", ["Cây kim tiền", "Cây lưỡi hổ", "Cây thiết mộc lan"], "Dương xỉ sinh sản bằng các ổ bào tử màu nâu nhỏ li ti nằm ở mặt dưới của lá già.", "7-8", 2),
    ("Nấm không phải thực vật", "Nấm rơm, nấm hương, mộc nhĩ có màu sắc đa dạng nhưng không có chất diệp lục, vậy nấm có tự quang hợp được không?", "Không, nấm là sinh vật dị dưỡng thuộc giới Nấm", ["Có, nấm quang hợp như lá cây", "Nấm quang hợp vào ban đêm", "Nấm ăn ánh sáng"], "Nấm sống bằng cách tiết enzym phân hủy các chất hữu cơ mục nát từ gỗ, rơm rạ để hấp thụ dinh dưỡng.", "8-9", 3),
    ("Cây rụng lá mùa đông", "Tại sao nhiều loài cây ở vùng ôn đới như cây phong, cây sồi lại trút sạch lá vào mùa đông?", "Để giảm thoát hơi nước và ngủ đông vượt qua giá rét", ["Vì lá bị sâu ăn hết", "Vì cây bị chết héo", "Để nuôi chim làm tổ"], "Rụng lá giúp cây không bị mất nước khi mặt đất đóng băng rễ không thể hút nước.", "8-9", 3),
    ("Cây thông lá kim", "Lá của cây thông có hình dáng như thế nào để chịu được băng tuyết và gió lạnh vùng cao nguyên?", "Lá nhỏ nhọn như cây kim có lớp sáp dày", ["Lá to bản như quạt ba tiêu", "Lá mỏng manh hình tròn", "Không có lá"], "Lá kim có bề mặt tiếp xúc nhỏ và lớp sáp cutin dày giúp cây thông xanh tốt quanh năm không sợ rét buốt.", "7-8", 2),
    ("Cây tre trăm đốt", "Thân cây tre rỗng ruột có nhiều gióng đốt thẳng tắp, dẻo dai uốn mình trong gió bão tượng trưng cho đức tính gì của người Việt?", "Bất khuất, kiên cường, đoàn kết và ngay thẳng", ["Lười biếng trốn tránh", "Nhút nhát sợ hãi", "Ích kỷ một mình"], "Lũy tre xanh làng quê chở che xóm làng, là biểu tượng ngàn đời của tinh thần kiên trung dân tộc.", "6-7", 1),
    ("Hạt sen trường thọ", "Các nhà khoa học từng gieo hạt sen cổ có niên đại hơn 1.000 năm tìm thấy dưới lớp than bùn mà hạt vẫn nảy mầm nhờ đâu?", "Vỏ hạt sen cực dày và kín bảo vệ phôi thai ngủ sâu an toàn", ["Hạt sen được bọc trong vàng", "Hạt sen hóa thạch thành đá", "Nhờ có phép thuật"], "Hạt sen có lớp vỏ dày không thấm nước giúp phôi hạt giữ được sức sống bền bỉ qua hàng thế kỷ.", "8-9", 3),
    ("Cây bồ công anh phát tán", "Hạt của bông hoa bồ công anh trắng muốt phát tán đi khắp nơi nhờ yếu tố tự nhiên nào?", "Nhờ gió thổi những chiếc 'dù bay' nhỏ xích", ["Nhờ kiến tha về tổ", "Nhờ sóng biển cuốn trôi", "Nhờ chuột gặm mang đi"], "Mỗi hạt bồ công anh mang một túm lông tơ mịn hoạt động như một chiếc dù bay lơ lửng trong gió.", "6-7", 1),
    ("Quả dừa phát tán qua nước", "Quả dừa khô rơi xuống biển có thể trôi dạt hàng ngàn dặm đại dương đến hòn đảo mới nảy mầm nhờ đâu?", "Lớp xơ dừa dày xốp chứa không khí giúp quả dừa nổi bồng bềnh", ["Vì quả dừa có vây bơi", "Vì quả dừa rất nặng", "Vì cá heo đẩy đi"], "Lớp vỏ ngoài không thấm nước và lớp xơ dừa bảo vệ hạt dừa an toàn suốt nhiều tháng trôi dạt trên biển.", "8-9", 3),

    # 116-126
    ("Thụ phấn nhờ gió", "Cây ngô (bắp) và cây lúa nước thường thụ phấn nhờ lực tự nhiên nào thay vì nhờ côn trùng?", "Nhờ gió thổi bay các hạt phấn nhẹ", ["Nhờ giun đất mang phấn", "Nhờ mưa rơi cuốn đi", "Nhờ ếch nhái nhảy qua"], "Hoa của cây lúa và ngô không có hương thơm hay mật ngọt rực rỡ, hạt phấn nhẹ để gió dễ cuốn đi xa.", "7-8", 2),
    ("Cây ăn quả ghép cành", "Phương pháp nhân giống ghép cành hoặc chiết cành mang lại ưu điểm vượt trội nào so với gieo hạt?", "Cây nhanh ra quả và giữ nguyên phẩm chất ngọt ngon của cây mẹ", ["Cây sẽ biến thành thân thảo", "Cây không cần tưới nước", "Cây không có rễ"], "Chiết ghép cành giúp rút ngắn thời gian sinh trưởng, chỉ sau 1-2 năm là cây đã bắt đầu bói quả thơm.", "8-9", 3),
    ("Hạt phấn hoa", "Cơ quan sinh dục đực của bông hoa chứa các hạt phấn màu vàng mịn gọi là gì?", "Nhị hoa (Chứa bao phấn)", ["Nhụy hoa", "Cánh hoa", "Đài hoa"], "Nhị hoa tạo hạt phấn, khi hạt phấn rơi trúng đầu nhụy cái sẽ diễn ra quá trình thụ tinh kết hạt.", "8-9", 3),
    ("Bầu nhụy phát triển thành quả", "Sau khi hoa thụ tinh thành công, noãn bên trong bầu nhụy sẽ phát triển thành bộ phận gì?", "Hạt giống", ["Cành cây", "Lá cây", "Gai nhọn"], "Noãn biến thành hạt giống mang mầm sống mới, còn bầu nhụy dày lên biến thành thịt quả thơm ngon.", "8-9", 3),
    ("Nhựa mủ cây mít", "Khi hái quả mít xanh ta thấy một chất lỏng trắng đục dính nhớt chảy ra, chất đó gọi là gì?", "Nhựa mủ cây", ["Nước khoáng", "Mật hoa", "Dầu ăn"], "Nhựa mủ của cây giúp làm đông kín vết thương trên vỏ thân, ngăn vi khuẩn nấm mốc xâm nhập.", "6-7", 1),
    ("Cây bàng rụng lá mùa đông", "Mùa đông lá bàng chuyển sang màu đỏ rực rỡ trước khi rụng là do chất diệp lục bị phân hủy để lộ sắc tố nào?", "Sắc tố anthocyanin và carotenoid màu đỏ cam", ["Chất diệp lục xanh đậm hơn", "Chất vôi bột trắng", "Chất bùn đất"], "Khi trời lạnh thiếu nắng, cây rút dinh dưỡng từ lá về thân, sắc tố đỏ lộ rõ tạo nên bức tranh mùa đông tuyệt đẹp.", "8-9", 3),
    ("Cây phát triển hướng sáng", "Hiện tượng cây trồng trong phòng kín luôn uốn cong thân ngọn vươn về phía cửa sổ đón nắng gọi là gì?", "Tính hướng sáng (Phototropism)", ["Tính hướng đất", "Tính sợ bóng tối", "Tính thích gió"], "Hoocmôn sinh trưởng auxin dồn về phía khuất sáng kích thích tế bào dài ra, đẩy ngọn cây uốn cong về phía ánh sáng.", "8-9", 3),
    ("Cây rễ thở ở bùn", "Cây bần, cây vẹt ở bãi bồi ven biển có những chiếc rễ nhọn mọc đâm ngược từ bùn lên trời để làm gì?", "Để lấy oxy hô hấp trong lớp bùn ngập nước thiếu khí (Rễ thở)", ["Để đâm thủng thuyền bè", "Để đón nước mưa rơi", "Để bắt cua cá"], "Bùn lầy ngập mặn rất nghèo oxy, các rễ thở mọc chĩa lên không trung chứa nhiều lỗ xốp giúp cây hít thở.", "8-9", 3),
    ("Lá sen không dính nước", "Tại sao những giọt nước mưa rơi lên mặt lá sen lại vo tròn lăn lông lốc mà không làm ướt lá?", "Mặt lá sen có lớp lông nano siêu mịn phủ sáp chống thấm", ["Do lá sen rất nóng làm nước sôi", "Do lá sen có dầu hỏa", "Do nước mưa sợ lá sen"], "Hiệu ứng lá sen (Lotus effect) là cảm hứng cho các nhà khoa học chế tạo sơn và vải thông minh tự làm sạch.", "8-9", 3),
    ("Vỏ cây bảo vệ thân", "Lớp vỏ xù xì bên ngoài cùng của thân cây gỗ có chức năng chính là gì?", "Bảo vệ các mạch sống bên trong khỏi sâu bệnh và mất nước", ["Làm cây nặng hơn để không bị bay", "Làm đẹp cho cây", "Tạo ra bóng râm"], "Nếu một thân cây bị lột một khoanh vỏ quanh thân, mạch rây bị đứt khiến cây sẽ chết héo sau một thời gian.", "7-8", 2),
    ("Cây ngô có cờ bắp", "Cụm hoa đực mọc trên đỉnh ngọn cây ngô được người nông dân gọi dân dã là gì?", "Cờ ngô", ["Bắp ngô", "Râu ngô", "Lá ngô"], "Cờ ngô chứa bao phấn rung rinh trong gió, phấn rơi xuống râu ngô (vòi nhụy cái) bên dưới để thụ phấn tạo hạt.", "7-8", 2)
]

# 14 SA items (TV127 - TV140)
raw_sa = [
    ("Quang hợp của lá", "Quá trình cây xanh dùng ánh sáng mặt trời chế tạo chất dinh dưỡng và nhả oxy gọi là gì?", "quang hợp", "Quang hợp là phản ứng kỳ diệu nuôi sống cây và tạo oxy cho Trái Đất.", "7-8", 2),
    ("Lá phổi xanh", "Các cánh rừng xanh bạt ngàn được ví như bộ phận nào của Trái Đất?", "lá phổi xanh|lá phổi", "Rừng xanh là lá phổi khổng lồ thanh lọc không khí cho muôn loài.", "6-7", 1),
    ("Bộ phận hút nước", "Bộ phận nào của cây cắm sâu vào lòng đất để hút nước và muối khoáng?", "rễ|rễ cây", "Rễ cây hút nước và giữ cho cây đứng vững chắc.", "6-7", 1),
    ("Khí cây nhả ban ngày", "Vào ban ngày khi quang hợp, cây xanh nhả ra loại khí nào cần cho sự thở của con người?", "khí oxy|oxy|o2", "Cây xanh tạo ra khí oxy nuôi dưỡng sự sống muôn loài.", "6-7", 1),
    ("Khí cây hấp thụ", "Để quang hợp tạo chất dinh dưỡng, lá cây hấp thụ loại khí nào có nhiều trong không khí?", "khí cacbonic|cacbonic|co2|carbon dioxide", "Cây hấp thụ khí CO2 giúp giảm thiểu hiệu ứng nhà kính.", "7-8", 2),
    ("Chất làm lá màu xanh", "Chất màu xanh trong lá cây giúp hấp thu ánh sáng mặt trời để quang hợp có tên là gì?", "diệp lục|chất diệp lục|chlorophyll", "Chất diệp lục là cỗ máy biến năng lượng ánh sáng thành chất dinh dưỡng cho cây.", "7-8", 2),
    ("Cây lương thực chính", "Cây lương thực trồng trên ruộng nước cho ra hạt thóc xay thành gạo trắng ở nước ta là cây gì?", "lúa|cây lúa|lúa nước", "Cây lúa nước là cây lương thực cốt lõi nuôi sống hàng triệu người dân Việt Nam.", "6-7", 1),
    ("Quốc hoa Việt Nam", "Loài hoa thanh khiết mọc trên đầm bùn được xem là biểu tượng quốc hoa của Việt Nam là hoa gì?", "hoa sen|sen", "Hoa sen là biểu tượng của tâm hồn thanh cao, thuần khiết của người Việt.", "6-7", 1),
    ("Hoa Tết miền Nam", "Loài hoa cánh vàng tươi rực rỡ đặc trưng cho ngày Tết Nguyên Đán ở miền Nam là hoa gì?", "hoa mai|mai vàng|mai", "Sắc mai vàng phương Nam rực rỡ mang đến may mắn đầu năm mới.", "6-7", 1),
    ("Hoa Tết miền Bắc", "Loài hoa cánh hồng phớt chúm chím nở trong tiết xuân đón Tết miền Bắc là hoa gì?", "hoa đào|đào", "Hoa đào thắm tươi là sắc màu mùa xuân thân thương của miền Bắc.", "6-7", 1),
    ("Hoa hè học trò", "Loài hoa cánh đỏ rực rỡ nở vào mùa hè trên sân trường báo hiệu mùa chia tay là hoa gì?", "hoa phượng|hoa phượng vĩ|phượng vĩ|phượng", "Hoa phượng vĩ đỏ rực rỡ gắn bó thân thương với tuổi học trò cắp sách.", "6-7", 1),
    ("Cây sa mạc lá biến gai", "Loài cây mọng nước sống ở sa mạc khô hạn có lá biến thành gai nhọn hoắt là cây gì?", "xương rồng|cây xương rồng", "Cây xương rồng trữ nước trong thân và có gai chống thoát hơi nước.", "6-7", 1),
    ("Hoa hướng về mặt trời", "Loài hoa màu vàng lớn luôn quay mặt về phía ánh sáng Mặt Trời có tên là gì?", "hoa hướng dương|hướng dương", "Hoa hướng dương luôn hướng về ánh sáng mặt trời rạng rỡ.", "6-7", 1),
    ("Thân cây lấy củ", "Củ khoai tây mà chúng ta ăn thực chất là biến dạng của bộ phận nào của cây?", "thân|thân củ|thân cây", "Khoai tây là thân ngầm phình to chứa nhiều tinh bột dưới lòng đất.", "8-9", 3)
]

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"TV{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Thực Vật",
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
    qid = f"TV{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Thực Vật",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/tv_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"TV: {len(questions)} câu đã được ghi vào tv_140.json")

# Bổ sung 40 câu MC còn thiếu cho TV
more_mc = [
    ("Quả cà chua bổ dưỡng", "Quả cà chua mọng nước khi chín có màu đỏ tươi chứa nhiều vitamin nào tốt cho mắt?", "Vitamin A và vitamin C", ["Vitamin B12", "Chất đạm thịt", "Chất béo mỡ"], "Cà chua giàu lycopene và vitamin A giúp đôi mắt bé sáng khỏe và tăng sức đề kháng.", "6-7", 1),
    ("Củ cà rốt giòn ngọt", "Củ cà rốt có màu cam rực rỡ mọc dưới đất là nguồn cung cấp dồi dào chất gì tiền vitamin A?", "Beta-carotene", ["Chất sắt", "Canxi", "I-ốt"], "Cơ thể chuyển hóa beta-carotene trong cà rốt thành vitamin A giúp nhìn tinh trong bóng tối.", "7-8", 2),
    ("Quả bưởi Năm Roi", "Quả bưởi có lớp cùi xốp trắng, bên trong có nhiều múi chứa các tép bưởi mọng nước vị gì?", "Vị chua ngọt thanh mát", ["Vị mặn chát", "Vị đắng nghét", "Vị cay xè"], "Tép bưởi chứa rất nhiều nước và vitamin C giải khát tuyệt vời trong ngày hè.", "6-7", 1),
    ("Cây cam sành", "Quả cam sành vỏ sần sùi màu xanh đậm, khi vắt lấy nước uống có tác dụng chính là gì?", "Bổ sung vitamin C tăng cường miễn dịch", ["Làm cơ thể buồn ngủ", "Làm yếu xương", "Làm rụng tóc"], "Một ly nước cam ấm mật ong mỗi sáng giúp bé phòng ngừa cảm cúm rất tốt.", "6-7", 1),
    ("Cây chanh chua thanh", "Nước cốt quả chanh có vị chua gắt là do chứa loại axit tự nhiên nào?", "Axit citric", ["Axit sunfuric", "Axit clohidric", "Axit axetic"], "Axit citric tự nhiên trong chanh giúp thanh lọc cơ thể và hỗ trợ tiêu hóa thức ăn.", "7-8", 2),
    ("Cây ớt cay nồng", "Chất tạo nên vị cay xé lưỡi đặc trưng của quả ớt có tên khoa học là gì?", "Chất Capsaicin", ["Chất Diệp lục", "Chất Cafein", "Chất Đường"], "Capsaicin kích thích đầu dây thần kinh cảm nhận nhiệt trên lưỡi tạo cảm giác cay nóng bùng nổ.", "8-9", 3),
    ("Cây hành hoa rễ chùm", "Cây hành lá, hành hoa quen thuộc trong gian bếp có loại rễ gì?", "Rễ chùm trắng mọc quanh gốc", ["Rễ cọc đâm sâu 2 mét", "Rễ củ to tròn", "Không có rễ"], "Hành lá có rễ chùm phát triển ở tầng đất mặt, cần đất xốp và tưới ẩm đều đặn.", "6-7", 1),
    ("Củ hành tây cay mắt", "Tại sao khi mẹ thái củ hành tây trong bếp thường hay bị cay mắt chảy nước mắt?", "Hành tây giải phóng hợp chất lưu huỳnh bay hơi kích thích tuyến lệ", ["Vì hành tây quá lạnh", "Vì hành tây có bụi bẩn", "Vì mùi hành tây thơm"], "Chất khí lưu huỳnh phản ứng với màng nước mắt tạo axit nhẹ kích thích mắt tiết nước mắt rửa trôi.", "8-9", 3),
    ("Quả dứa (thơm/khóm)", "Quả dứa mắt nhiều thực chất là dạng quả gì trong sinh học thực vật?", "Quả phức (do cả một cụm hoa kết hợp lại thành)", ["Quả đơn một hoa", "Quả khô tự nẻ", "Củ mọc dưới đất"], "Mỗi 'mắt dứa' thực chất là tàn tích của một bông hoa riêng lẻ trên trục cụm hoa dứa.", "8-9", 3),
    ("Cây đu đủ trĩu quả", "Quả đu đủ khi chín có ruột màu cam mềm ngọt, bên trong khoang rỗng chứa đầy thứ gì?", "Nhiều hạt tròn nhỏ màu đen bóng", ["Một hạt to như quả trứng", "Không có hạt nào", "Chỉ toàn nước ngọt"], "Hạt đu đủ bọc trong lớp màng nhầy, cây đu đủ cái thụ phấn cho chùm quả trĩu quanh thân.", "6-7", 1),
    ("Quả bơ béo ngậy", "Quả bơ sáp có thịt màu vàng xanh dẻo quánh, chứa hàm lượng cao loại chất dinh dưỡng nào?", "Chất béo không bão hòa tốt cho tim mạch", ["Chất đường ngọt gắt", "Chất đắng độc hại", "Chất cồn"], "Quả bơ chứa nhiều axit béo omega-3 và omega-6 rất bổ dưỡng cho trí não của trẻ nhỏ.", "7-8", 2),
    ("Cây mít ra quả ở thân", "Tại sao quả mít lại thường mọc trực tiếp từ thân cây gỗ to lớn thay vì mọc ở đầu cành nhỏ?", "Vì quả mít rất to nặng, thân cây to mới nâng đỡ được", ["Vì mít không có cành lá", "Vì cành mít không có hoa", "Do rễ cây kéo quả lên"], "Hiện tượng ra hoa đậu quả trên thân gỗ già (Cauliflory) giúp cây nâng đỡ những chùm quả nặng hàng chục kg.", "8-9", 3),
    ("Cây nho leo giàn", "Cây nho là loài thân leo cho những chùm quả mọng tròn màu xanh, đỏ, tím dùng để làm gì?", "Ăn tươi, sấy làm nho khô và ủ rượu nho", ["Làm đồ gỗ nội thất", "Làm giấy viết", "Làm thuốc nhuộm vải"], "Ninh Thuận là vùng đất đầy nắng gió của Việt Nam nổi tiếng với những vườn nho trĩu quả.", "6-7", 1),
    ("Cây ổi giòn ngọt", "Lá ổi non có vị chát thường được dân gian hái búp nhai ăn để chữa chứng bệnh gì?", "Đau bụng tiêu chảy", ["Đau mắt đỏ", "Gãy xương chân", "Chảy máu cam"], "Chất tannin trong búp ổi non làm săn niêm mạc ruột và ức chế vi khuẩn đường ruột rất tốt.", "7-8", 2),
    ("Cây me chua", "Quả me có vỏ giòn nâu, thịt me dẻo dính vị chua thanh thường dùng để nấu món canh gì ngon miệng?", "Canh chua cá lóc", ["Canh rau ngót nấu thịt", "Canh khổ qua", "Canh bí đỏ"], "Nước cốt me chua dịu kết hợp cùng dứa, cà chua tạo nên hương vị canh chua Nam Bộ trứ danh.", "6-7", 1),
    ("Cây vải thiều Lục Ngạn", "Quả vải thiều chín đỏ mọng có cùi trắng trong ngọt lịm nổi tiếng nhất ở vùng đất nào của Việt Nam?", "Lục Ngạn (Bắc Giang) và Thanh Hà (Hải Dương)", ["Cà Mau", "Đà Lạt", "Sa Pa"], "Vải thiều Việt Nam ngọt thơm nức tiếng, được xuất khẩu sang cả Nhật Bản, Mỹ và châu Âu.", "7-8", 2),
    ("Quả nhãn lồng Hưng Yên", "Quả nhãn có vỏ màu nâu nhạt, cùi giòn ngọt thơm mọng nước và hạt đen nhánh gọi là gì?", "Nhãn lồng Hưng Yên", ["Nhãn xuồng Vũng Tàu", "Nhãn tiêu da bò", "Nhãn rừng"], "Thời phong kiến, nhãn lồng Hưng Yên ngon ngọt nức tiếng từng được chọn làm sản vật tiến vua.", "7-8", 2),
    ("Cây chôm chôm râu dài", "Quả chôm chôm có lớp vỏ ngoài màu đỏ phủ đầy những sợi lông râu dài mềm mại, ruột quả ra sao?", "Cùi trắng giòn ngọt tróc hạt", ["Chua loét nhiều hạt nhỏ", "Rỗng ruột", "Có vị mặn"], "Vườn chôm chôm chín đỏ rực rỡ là điểm đến du lịch miệt vườn hấp dẫn ở miền Tây Nam Bộ.", "6-7", 1),
    ("Cây khế năm múi", "Khi cắt ngang một quả khế chín, ta sẽ thấy lát khế có hình thù kỳ diệu nào?", "Hình ngôi sao 5 cánh", ["Hình trái tim", "Hình tròn vo", "Hình tam giác"], "Quả khế có 5 múi cạnh nổi rõ, cắt ngang tạo thành những ngôi sao vàng lấp lánh trang trí đĩa ăn.", "6-7", 1),
    ("Cây vú sữa ngọt lành", "Quả vú sữa khi chín bóp nhẹ quanh quả sẽ ứa ra dòng nước trắng đục thơm ngọt như gì?", "Thơm ngọt như dòng sữa mẹ", ["Nước dừa tươi", "Nước chanh chua", "Nước khoáng mặn"], "Vú sữa Lò Rèn Tiền Giang gắn liền với câu chuyện cổ tích cảm động về tình mẫu tử thiêng liêng.", "6-7", 1),
    ("Cây sầu đâu (cây xoan)", "Cây xoan ở miền Bắc trổ hoa tím li ti mùi thơm thoang thoảng vào mùa nào?", "Mùa xuân sau Tết", ["Mùa đông lạnh giá", "Mùa hè gay gắt", "Mùa thu lá rụng"], "Mưa bụi mùa xuân bay lất phất cùng hoa xoan rụng tím sân nhà là hình ảnh quen thuộc của làng quê Bắc Bộ.", "7-8", 2),
    ("Cây bồ đề linh thiêng", "Lá cây bồ đề có đặc điểm nhận dạng độc đáo nào ở phần chóp lá?", "Đuôi lá kéo dài nhọn hoắt như giọt nước", ["Lá hình tròn xoe", "Lá có gai góc xung quanh", "Lá xẻ răng cưa sâu"], "Phần đuôi lá bồ đề kéo dài (drip tip) giúp nước mưa trôi nhanh khỏi mặt lá tránh ẩm mốc.", "8-9", 3),
    ("Cây đa cổ thụ đầu làng", "Cây đa nghìn năm đầu làng thường có những chiếc rễ dài buông thõng từ cành cây xuống đất gọi là rễ gì?", "Rễ phụ (Rễ chống khí sinh)", ["Rễ củ", "Rễ thở ngập mặn", "Tua cuốn"], "Rễ phụ buông rủ cắm sâu xuống đất lâu ngày phát triển to lớn thành những chiếc cột phụ vững chãi.", "7-8", 2),
    ("Cây hoa cúc mùa thu", "Hoa cúc vàng rực rỡ tượng trưng cho sự trường thọ và lòng hiếu thảo thường nở rộ vào mùa nào?", "Mùa thu se lạnh", ["Mùa hè chói chang", "Mùa đông buốt tuyết", "Giữa trưa hè"], "Hoa cúc là một trong tứ quý 'Tùng - Cúc - Trúc - Mai' mang ý nghĩa thanh cao và bền bỉ.", "6-7", 1),
    ("Hoa sen nở mùa nào", "Những đầm sen ngát hương thơm ở Hồ Tây (Hà Nội) và Đồng Tháp Mười nở rực rỡ nhất vào mùa nào?", "Mùa hè (từ tháng 5 đến tháng 8)", ["Mùa đông giá rét", "Mùa xuân mưa phùn", "Mùa giáp Tết"], "Mùa hè là mùa sen nở rộ, người ta hái hoa sen sớm ướp trà sen thượng hạng thơm ngát đất trời.", "6-7", 1),
    ("Cây rau muống đồng", "Cây rau muống là món rau quốc dân của người Việt, có thân rỗng xốp sống được ở cả môi trường nào?", "Sống được cả trên cạn lẫn dưới nước ao bè", ["Chỉ sống trên sa mạc", "Chỉ sống trong tủ lạnh", "Chỉ sống dưới đáy biển"], "Rau muống bè thả ao hồ phát triển thần tốc, ngọn rau xanh giòn luộc chấm tương hoặc xào tỏi thơm lừng.", "6-7", 1),
    ("Cây rau ngót nấu canh thịt", "Lá rau ngót có tính mát lành, thường được tuốt lá nấu canh thịt băm bổ dưỡng cho ai vừa ốm dậy?", "Bổ dưỡng cho trẻ nhỏ và người mẹ sau sinh", ["Cho thú cưng ăn", "Làm thức ăn cho cá mập", "Không ai ăn được"], "Rau ngót chứa nhiều vitamin C, đạm thực vật và chất sắt giúp thanh nhiệt, bổ máu hồi phục sức khỏe.", "6-7", 1),
    ("Cây bắp cải cuộn lá", "Bắp cải có các lớp lá xếp cuộn tròn chặt chẽ vào nhau tạo thành khối cầu lớn là loại rau ưa khí hậu gì?", "Ưa khí hậu mát mẻ và lạnh mùa đông", ["Ưa khí hậu nắng nóng sa mạc", "Ưa ngập lụt quanh năm", "Ưa bóng tối hoàn toàn"], "Bắp cải trồng nhiều ở Đà Lạt và vụ đông miền Bắc, lá giòn ngọt xào hoặc luộc đều rất ngon.", "6-7", 1),
    ("Cây súp lơ (bông cải)", "Phần hoa súp lơ trắng hoặc xanh giòn ngọt mà chúng ta ăn thực chất là bộ phận gì của cây?", "Cụm hoa non chưa nở gồm hàng ngàn nụ hoa li ti", ["Lá cây cuộn lại", "Thân cây phình to", "Rễ cây"], "Súp lơ chứa nhiều hợp chất chống ung thư, vitamin C và chất xơ tuyệt vời cho sức khỏe.", "7-8", 2),
    ("Quả bí đỏ bổ não", "Quả bí đỏ có ruột màu vàng cam đậm, hạt bùi béo, chứa nhiều vitamin A và glutamic acid tốt cho cơ quan nào?", "Rất tốt cho não bộ và thị lực", ["Làm mỏi mắt", "Làm yếu răng", "Làm đau dạ dày"], "Canh bí đỏ hầm xương hoặc chè bí đỏ là món ăn bổ não tăng cường trí nhớ hàng đầu cho bé học tập.", "6-7", 1),
    ("Quả dưa leo (dưa chuột)", "Quả dưa chuột chứa đến 95% là nước mát, có tác dụng giải nhiệt và cung cấp khoáng chất gì?", "Bù nước và thanh nhiệt cơ thể", ["Gây nóng trong người", "Làm mất nước", "Làm khát thêm"], "Ăn dưa leo giòn mát trong ngày hè oi ả giúp bù đắp lượng nước và muối khoáng đã mất qua mồ hôi.", "6-7", 1),
    ("Cây mướp hương leo giàn", "Quả mướp hương khi già khô quắt lại thì phần ruột biến thành thứ gì dùng để cọ rửa rất sạch?", "Xơ mướp tự nhiên dẻo dai", ["Khối bùn đất", "Bột phấn trắng", "Thanh sắt cứng"], "Xơ mướp là miếng cọ rửa chén bát và bông tắm tự nhiên thân thiện tuyệt đối với môi trường.", "7-8", 2),
    ("Cây đậu xanh làm giá đỗ", "Khi ta ngâm hạt đậu xanh trong nước ấm và ủ bóng tối 2-3 ngày, hạt sẽ nảy mầm thành món rau gì?", "Giá đỗ giòn mát", ["Nấm rơm", "Rau bina", "Cải mầm cay"], "Giá đỗ giàu vitamin E và C, là món rau sống thanh mát quen thuộc ăn kèm bún bò, phở cuốn.", "6-7", 1),
    ("Cây hoa súng trên mặt nước", "Hoa súng nở trên mặt ao hồ có cuống dài cắm vào bùn, lá tròn xẻ thùy xòe trên mặt nước khác hoa sen ở điểm nào?", "Lá hoa súng nằm nổi sát mặt nước, hoa sen vươn cao khỏi mặt nước", ["Hoa súng không có cánh", "Hoa súng nở dưới bùn sâu", "Hoa súng có lá gai"], "Hoa sen có lá và hoa vươn cao kiêu hãnh trên mặt nước, trong khi hoa súng hoa và lá nổi dập dềnh mặt nước.", "7-8", 2),
    ("Cây cọ xòe ô", "Bài thơ thiếu nhi có câu: 'Cây cọ xòe ô che nắng râm, đường em đi học dưới hàng cọ xanh'. Lá cọ có hình dạng gì?", "Lá xòe tròn như chiếc ô, có khía răng cưa", ["Lá dài nhọn như mũi giáo", "Lá tròn xoe như đồng xu", "Lá mỏng manh như sợi tơ"], "Đồi cọ Phú Thọ bạt ngàn xanh mướt, lá cọ được người dân dùng để lợp mái nhà và đan nón cọ xinh xắn.", "6-7", 1),
    ("Cây hoa lan hồ điệp", "Loài hoa phong lan quý phái có cánh hoa xòe tròn nở lâu tàn giống như những chú bướm rập rờn là gì?", "Lan Hồ Điệp", ["Lan Vũ Nữ", "Lan Phi Điệp", "Lan Hạc Đỉnh"], "Lan hồ điệp có nhiều màu sắc sang trọng, có thể tươi lâu suốt 2-3 tháng trong dịp Tết.", "7-8", 2),
    ("Cây thủy trúc lọc nước", "Cây thủy trúc trồng quanh mép hồ nước có rễ chùm dày đặc có khả năng làm sạch môi trường nước nhờ đâu?", "Rễ cây hấp thụ các chất ô nhiễm và cung cấp oxy cho vi sinh vật có lợi", ["Cây tiết ra xà phòng", "Cây hút cạn nước bẩn", "Cây lọc bằng lá gai"], "Hệ thống bãi lọc ngập nước bằng cây thủy trúc là giải pháp công nghệ xanh xử lý nước thải sinh hoạt an toàn.", "8-9", 3),
    ("Cây thông có quả thông", "Quả thông khô có những lớp vảy gỗ xếp chồng lên nhau, mở ra khi trời khô ráo và khép lại khi trời ẩm ướt là do đâu?", "Do các thớ gỗ của vảy quả thông co giãn nhạy cảm với độ ẩm không khí", ["Do sóc rừng mở ra", "Do quả thông thích tắm mưa", "Do quả thông bị hỏng"], "Vảy quả thông tự đóng lại khi ẩm ướt để bảo vệ hạt phấn không bị ướt và mở bung ra thả hạt bay trong gió khô.", "8-9", 3),
    ("Cây nấm ăn được", "Nấm rơm, nấm kim châm, nấm đùi gà cung cấp nguồn dinh dưỡng quý giá nào cho người ăn chay?", "Đạm thực vật, chất xơ và nhiều khoáng chất vi lượng", ["Nhiều mỡ động vật", "Nhiều đường hóa học", "Nhiều chất cồn"], "Nấm thơm ngon ngọt tự nhiên như thịt, là thực phẩm vàng cho sức khỏe tim mạch và hệ tiêu hóa.", "6-7", 1),
    ("Cây ngũ gia bì đuổi muỗi", "Cây ngũ gia bì có chùm 5 lá xanh bóng thường được trồng trong nhà chậu cảnh có tác dụng gì?", "Xua đuổi muỗi và thanh lọc các khí độc hại trong nhà", ["Tạo ra nhiều bụi bẩn", "Thu hút nhiều rắn rết", "Làm nhà bị ẩm ướt"], "Mùi hương thoang thoảng của tinh dầu ngũ gia bì khiến loài muỗi khó chịu và tự động tránh xa không gian sống.", "7-8", 2)
]

# Thêm more_mc vào raw_mc và tái tạo file
raw_mc.extend(more_mc)

questions = []
for i, item in enumerate(raw_mc, start=1):
    sub, q_text, correct, dist, expl, age, diff = item
    qid = f"TV{i:03d}"
    opts = [correct] + dist[:3]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans_letter = chr(ord('A') + opts.index(correct))
    img_url = imgs[(i - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Thực Vật",
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
    qid = f"TV{j:03d}"
    img_url = imgs[(j - 1) % len(imgs)]
    questions.append({
        "id": qid,
        "topic": "Thực Vật",
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

with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/tv_140.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Cập nhật TV hoàn tất: {len(questions)} câu đã được ghi vào tv_140.json")
