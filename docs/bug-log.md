# Nhật ký sửa lỗi (Bug Log)

## BUG-001 · Major — Lỗi làm sạch văn bản ăn nhầm chữ thành Email
1. **Mã và mức độ:** BUG-001 · Major (Ảnh hưởng đến dữ liệu đầu vào của mô hình).
2. **Phát hiện bởi:** Test case `test_lam_sach_luong_dung` trong file `tests/test_text.py`.
3. **Triệu chứng:** Chạy pytest báo FAILED, hàm `lam_sach("Màn Hình Bị SỌC Xanh!@#")` trả về `"màn hình bị sọc email"` thay vì `"màn hình bị sọc xanh"`.
4. **Cách tái lập:** Chạy lệnh `python -m pytest -q`. Test case số 1 thất bại.
5. **Nguyên nhân:** Regex nhận diện email `\S+@\S+` quá lỏng lẻo, khớp nhầm với cụm `"Xanh!@#"`.
6. **Cách sửa:** Thắt chặt Regex email thành `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'`, giữ nguyên dấu `< >` khi xóa ký tự đặc biệt.
7. **Commit và xác nhận:** Commit `test: them 3 unit test va sua loi ham lam sach`. Chạy lại `pytest` PASS 6/6 test.