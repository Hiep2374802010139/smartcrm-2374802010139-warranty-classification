# TEST REPORT - BÀI TẬP 3

## 1. Thông tin chung
- **Người thực hiện:** Lê Hoàng Hiệp (MSSV: 2374802010139)
- **Môi trường test:** Local (`.venv`), Python 3.11+, chạy trên Docker Container.
- **Lệnh chạy test:** `python -m pytest -q`
- **Kết quả tổng quan:** 10/10 test PASS.

## 2. Bảng Test Case chi tiết (8 cột)

| Mã | Tiền điều kiện | Các bước | Dữ liệu thử | Kết quả mong đợi | Ưu tiên | Kết quả thực tế | P/F |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Hàm `lam_sach` sẵn sàng | Gọi hàm làm sạch với văn bản thường | `"Màn Hình Bị SỌC Xanh!@#"` | Trả về `"màn hình bị sọc xanh"` | Cao | `"màn hình bị sọc xanh"` | **PASS** |
| **TC-02** | Hàm `lam_sach` sẵn sàng | Gọi hàm làm sạch với văn bản chứa SĐT/Email | `"Gọi 0912345678, mail a@b.com"` | Che thông tin thành `<sdt>`, `<email>` | Cao | `"gọi <sdt> , mail <email>"` | **PASS** |
| **TC-03** | Hàm `lam_sach` sẵn sàng | Gọi hàm làm sạch với chuỗi rỗng | `""` (chuỗi rỗng) | Trả về `""`, không sập | Trung bình | `""` | **PASS** |
| **TC-04** | Hàm `lam_sach` sẵn sàng | Gọi hàm làm sạch với giá trị None | `None` | Trả về `""`, không ném ngoại lệ | Trung bình | `""` | **PASS** |
| **TC-05** | Dữ liệu văn bản thô | Kiểm tra hàm làm sạch giữ dấu và thay thế serial | `"SN10293A màn hình vỡ"` | Chứa `<serial>`, giữ nguyên dấu `"màn hình vỡ"` | Cao | `"<serial> màn hình vỡ"` | **PASS** |
| **TC-06** | Đã có tập Train/Test | Kiểm tra rò rỉ dữ liệu (Data Leakage) | `train_texts`, `test_texts` | Từ vựng của Vectorizer không chứa từ chỉ có ở Test | Cao | Không có từ nào bị rò rỉ | **PASS** |
| **TC-07** | Môi trường sẵn sàng | Chạy script `train.py` 2 lần liên tiếp | `configs/train.yaml` | 2 file `metrics.json` giống hệt nhau | Cao | Kết quả 2 lần giống nhau | **PASS** |
| **TC-08** | API đang chạy (Docker) | Gọi API với dữ liệu hợp lệ | `{"mo_ta": "Máy sạc không vào điện"}` | Mã 200, trả về top 3 nhãn và độ tin cậy | Cao | 200 OK, JSON hợp lệ | **PASS** |
| **TC-09** | API đang chạy (Docker) | Gọi API với mô tả rỗng | `{"mo_ta": ""}` | Mã 422 (Lỗi validation) | Cao | 422 Unprocessable Entity | **PASS** |
| **TC-10** | API đang chạy (Docker) | Gọi API với mô tả quá ngắn | `{"mo_ta": "abc"}` | Mã 422 (Lỗi validation) | Cao | 422 Unprocessable Entity | **PASS** |

## 3. Đối chiếu 5 loại test bắt buộc của BT3
- [x] **Test luồng đúng:** TC-01, TC-08.
- [x] **Test giá trị biên:** TC-03, TC-04.
- [x] **Test dữ liệu sai:** TC-09, TC-10.
- [x] **Test bảo mật / chất lượng dữ liệu:** TC-02, TC-06.
- [x] **Test tính tái lập:** TC-07.

## 4. Minh chứng kết quả chạy
- **Ảnh chụp màn hình Terminal chạy 10 test PASS:** [Xem ảnh tại đây](./screenshots/ket-qua-10-test.png)