Phạm vi: Kiểm thử hàm làm sạch văn bản, API dự đoán FastAPI. Không kiểm thử giao diện web (vì không làm), không kiểm thử hiệu năng phần cứng.

Loại test và số lượng: 10 test case (6 Unit test cho hàm làm sạch, 4 test cho API/ML pipeline như rò rỉ dữ liệu, tính tái lập).

Tiêu chí thành công: 100% test case PASS khi chạy lệnh pytest -q. Không còn bug Critical nào đang mở.

Môi trường: Chạy trên môi trường ảo .venv cục bộ, dữ liệu test được sinh tự động trong code.

