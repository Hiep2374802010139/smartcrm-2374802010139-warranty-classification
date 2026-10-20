PHÂN TÍCH CONFUSION MATRIX 
1. Cặp nhãn bị nhầm lẫn nhiều nhất là gì?

Số liệu: Nhìn vào ma trận, dòng số 4 (nhãn thật PIN) và cột số 5 (nhãn dự đoán SAC), có 13 trường hợp bị đoán nhầm. Ngoài ra, dòng số 4 (nhãn thật PHAN_MEM) bị đoán nhầm thành MAN_HINH tới 15 trường hợp (dòng 4, cột 2).

Câu kết luận 1: "Mô hình nhầm lẫn nhiều nhất giữa nhãn PHẦN MỀM thành MÀN HÌNH (15 ca) và PIN thành SẠC (13 ca). Về mặt nghiệp vụ, các lỗi phần mềm đôi khi biểu hiện ra ngoài giống lỗi màn hình (ví dụ: treo máy, đơ màn hình), và pin/sạc thường dùng chung từ ngữ miêu tả của người dùng."

2. Nhãn nào có Recall (độ phủ) thấp nhất và hậu quả là gì?

Số liệu: Tính Recall = Số dự đoán đúng / Tổng số mẫu thực tế của nhãn đó.

Nhãn PHAN_MEM (Dòng 4): Dự đoán đúng 38 / Tổng (3+15+0+38+0+1) = 38/57 = 66.7% (Thấp nhất).

Nhãn KHAC (Dòng 1): Dự đoán đúng 48 / Tổng (48+0+11+4+1+0) = 48/64 = 75%.

Câu kết luận 2: "Nhãn PHẦN MỀM có độ phủ (Recall) thấp nhất (chỉ 66.7%, tức là bỏ sót 1/3 số ca thực tế). Hậu quả nghiệp vụ: Nếu nhân viên tiếp nhận tin vào gợi ý của mô hình, họ có thể chuyển máy cho bộ phận thay màn hình trong khi lỗi thực chất chỉ là phần mềm, gây lãng phí chi phí và thời gian."

3. Có nhãn nào đang hoạt động như một "thùng rác" hút các dự đoán sai không?

Số liệu: Nhìn vào Cột 1 (cột dự đoán KHAC), nó nhận 4 ca từ NUOC_VAO, 3 ca từ PHAN_MEM. Không quá tệ. Tuy nhiên, cột MAN_HINH (Cột 2) đang hút tới 15 ca của PHAN_MEM và 11 ca của KHAC.

Câu kết luận 3: "Nhãn MÀN HÌNH đang có xu hướng trở thành 'thùng rác' khi hút rất nhiều dự đoán sai từ nhãn PHẦN MỀM và KHÁC. Hướng xử lý: Cần bổ sung thêm các từ khóa đặc trưng (feature) phân biệt rõ lỗi phần mềm (như 'treo', 'đơ', 'khởi động lại') so với lỗi phần cứng màn hình để mô hình tách biệt tốt hơn."