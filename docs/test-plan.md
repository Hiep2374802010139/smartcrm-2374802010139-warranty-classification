1.Phạm vi:

Kiểm: Hàm làm sạch văn bản, quá trình chia dữ liệu (chống rò rỉ), quá trình huấn luyện (tính tái lập), API dự đoán (dữ liệu đúng/sai).

Không kiểm: Giao diện web (vì bạn không làm), hiệu năng phần cứng (thuộc môn khác).

2.Loại test và số lượng: (Dựa theo Kim tự tháp kiểm thử)

Unit test: 6 test case (tập trung vào hàm lam_sach).

API/End-to-End test: 4 test case (gọi thử API /du-doan).

Tổng cộng: 10 test case (đúng chuẩn 10-12 test).

3.Tiêu chí thành công (Đo được):

100% test case PASS khi chạy lệnh pytest -q.

Mô hình đạt F1-macro > 0.7 trên tập Test.

API không bị sập (trả về mã 500) khi gặp dữ liệu sai.

4.Môi trường và dữ liệu thử:

Chạy trên Docker container.

Dữ liệu test được tự dựng trong code (không phụ thuộc file có sẵn trên máy).