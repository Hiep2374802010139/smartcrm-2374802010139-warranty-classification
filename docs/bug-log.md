# Nhật ký sửa lỗi (Bug Log) - Bài tập 3

## BUG-001 · Critical — Ứng dụng Docker bị crash ngay khi khởi động
- **1. Mã và mức độ:** BUG-001 · Critical (Hệ thống không dùng được).
- **2. Phát hiện bởi:** Kiểm thử thủ công quá trình chạy Docker, kiểm tra log bằng lệnh `docker compose logs model`.
- **3. Triệu chứng:** Container API khởi động được vài giây rồi tự động tắt (Exited). Màn hình log báo lỗi `ValueError: Unknown level: 'info'`.
- **4. Cách tái lập:** Chạy lệnh `docker compose up -d`, sau đó chạy `docker compose ps` thấy trạng thái không phải là `healthy`. Chạy `docker compose logs` để xem chi tiết.
- **5. Nguyên nhân:** Biến môi trường `LOG_LEVEL` được truyền vào từ file `docker-compose.yml` là chữ thường (`info`). Trong khi đó, thư viện `logging` của Python yêu cầu các mức log phải viết IN HOA (ví dụ: `INFO`, `ERROR`).
- **6. Cách sửa:** Sửa hàm `cau_hinh_log()` trong file `src/log_config.py`, thêm hàm `.upper()` vào sau `os.getenv(...)` để tự động chuyển đổi giá trị truyền vào thành chữ in hoa trước khi cấu hình.
- **7. Link commit và xác nhận:** [9d3a2b3](https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification/commit/9d3a2b3) - Chạy lại `docker compose up -d` -> Container báo `healthy`, test API thành công.

## BUG-002 · Major — Lỗi làm sạch văn bản ăn nhầm chữ thành Email
- **1. Mã và mức độ:** BUG-002 · Major (Chức năng quan trọng sai, ảnh hưởng trực tiếp đến độ chính xác của mô hình).
- **2. Phát hiện bởi:** Test case `test_lam_sach_luong_dung` (Tự động phát hiện qua Unit Test).
- **3. Triệu chứng:** Hàm `lam_sach("Màn Hình Bị SỌC Xanh!@#")` trả về kết quả `"màn hình bị sọc email"` thay vì `"màn hình bị sọc xanh"`.
- **4. Cách tái lập:** Chạy lệnh `python -m pytest -q`. Test case số 1 báo FAILED với thông báo AssertionError.
- **5. Nguyên nhân:** Regex nhận diện email `\S+@\S+` quá lỏng lẻo, khớp nhầm với cụm ký tự đặc biệt `"Xanh!@#"` trong câu. Ngoài ra, Regex xóa ký tự đặc biệt cũ bị mất dấu tiếng Việt.
- **6. Cách sửa:** Thắt chặt Regex email thành `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'`. Bổ sung dải ký tự tiếng Việt (`àáảã...`) vào Regex xóa ký tự đặc biệt để giữ nguyên dấu.
- **7. Link commit và xác nhận:** [f76300d](https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification/commit/f76300d) - Chạy lại `pytest -q` -> PASS 100%. *(Ghi chú: Commit này chứa module predict/report, lỗi regex đã được sửa từ trước đó)*

## BUG-003 · Major — Lỗi build Docker do thư viện đặc thù của Windows
- **1. Mã và mức độ:** BUG-003 · Major (Không thể đóng gói sản phẩm để chạy trên môi trường khác).
- **2. Phát hiện bởi:** Chạy lệnh `docker compose up -d --build` trong quá trình kiểm thử máy trắng.
- **3. Triệu chứng:** Quá trình build Docker thất bại ở bước `[4/7] RUN pip install ...`. Log báo lỗi `linker 'cc' not found` khi đang cố gắng biên dịch thư viện `pywinpty`.
- **4. Cách tái lập:** Xóa cache Docker (`docker system prune -af`), sau đó chạy lại `docker compose up -d --build`.
- **5. Nguyên nhân:** File `requirements.txt` chứa thư viện `pywinpty` (một thư viện chỉ dành riêng cho môi trường Windows). Khi Docker chạy trên nền tảng Linux, nó cố gắng biên dịch thư viện này từ mã nguồn nhưng môi trường `python:3.11-slim` không có sẵn trình biên dịch C/Rust (`cc`).
- **6. Cách sửa:** Xóa dòng `pywinpty` ra khỏi file `requirements.txt` (vì khi chạy trên Docker Linux, thư viện này không cần thiết).
- **7. Link commit và xác nhận:** [95c1019](https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification/commit/95c1019) - Chạy lại `docker compose up -d --build` -> Build thành công, container chạy `healthy`.