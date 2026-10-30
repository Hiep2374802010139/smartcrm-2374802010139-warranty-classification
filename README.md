# SmartCRM - Phân loại yêu cầu bảo hành tự động (Luồng L10)

**Họ và tên:** Lê Hoàng Hiệp  
**MSSV:** 2374802010139  
**Lớp:** 261_71ITGR40203_05  
**Track:** AI (Trí tuệ nhân tạo)  
**Link Repo GitHub:** `https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification`  
**Tag phiên bản:** `v0.2`

## 1. Mô tả hệ thống
Dự án xây dựng module cốt lõi cho hệ thống SmartCRM của Mekong Mobile, giải quyết bài toán tự động phân loại mô tả lỗi (văn bản tự do) của khách hàng thành 6 nhóm sự cố (MÀN HÌNH, PIN, SẠC, PHẦN MỀM, NƯỚC VÀO, KHÁC). Hệ thống sử dụng phương pháp TF-IDF để vector hóa văn bản, so sánh 4 mô hình (Dummy, Logistic, LinearSVC, ComplementNB) và chọn ra mô hình tốt nhất (`ComplementNB`). Hệ thống cũng đã được đóng gói thành API (FastAPI) để có thể tích hợp vào luồng nghiệp vụ thực tế.

## 2. Yêu cầu môi trường
- **Ngôn ngữ:** Python 3.9 trở lên (đã test trên Python 3.10+).
- **Thư viện:** Các thư viện cần thiết đã được ghim phiên bản chính xác trong file `requirements.txt`.
- **Dữ liệu:** File `issue_descriptions.csv` (đã được đặt sẵn trong thư mục `data/` của repo).
- **Công cụ bổ sung (Tùy chọn):** Docker Desktop (nếu muốn chạy API qua Docker).

## 3. Cấu trúc thư mục
```text
├── configs/               # Chứa file cấu hình train.yaml (siêu tham số, seed)
├── data/                  # Chứa file dữ liệu nguồn issue_descriptions.csv
├── docs/                  # Chứa tài liệu (thay-doi-thiet-ke.md, ai-disclosure.md, bug-log.md, ảnh minh chứng)
├── reports/               # Chứa file kết quả metrics.json sinh ra sau khi train
├── src/                   # Mã nguồn chính
│   ├── data/              # Code xử lý chia dữ liệu
│   ├── features/          # Code làm sạch văn bản, vector hóa TF-IDF
│   ├── models/            # Code chứa baseline, train và predict
│   └── serve/             # Code chứa API FastAPI để dự đoán
├── tests/                 # Chứa các file Unit Test (test_text.py)
├── Dockerfile             # File cấu hình đóng gói API
├── docker-compose.yml     # File cấu hình chạy Docker
├── .env.example           # Khai báo các biến môi trường mẫu
└── README.md              # Tài liệu hướng dẫn 
```

## 4. Hướng dẫn cài đặt và chạy (Từng bước một lệnh)
Bước 1: Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```

Bước 2: Huấn luyện mô hình (Chạy bằng 1 lệnh)
```bash
python -m src.models.train --config configs/train.yaml
```

Bước 3: Chạy bộ kiểm thử (Unit Test)
```bash
python -m pytest -q
```

Bước 4 (Điểm cộng): Đóng gói và chạy API bằng Docker
```bash
# Build và chạy container
docker compose up -d --build

# Kiểm tra API (Gọi thử dự đoán)
curl -X POST http://localhost:8080/du-doan -H "Content-Type: application/json" -d "{\"mo_ta\": \"Màn hình bị sọc xanh, cảm ứng chập chờn\"}"
```

## 5. Cách kiểm tra hệ thống đã chạy đúng
Sau khi chạy lệnh ở Bước 2 thành công, hệ thống sẽ tự động sinh ra 2 tệp minh chứng:

reports/metrics.json: Chứa điểm F1-macro của 4 mô hình trên tập Validation, mô hình được chọn, điểm F1-macro trên tập Test, F1 từng nhãn và Confusion Matrix.

artifacts/model_v1.joblib: File mô hình đã được lưu (đã được chặn bởi .gitignore).

Sau khi chạy Bước 3, màn hình Terminal phải hiển thị dòng chữ xanh: 6 passed (hoặc số lượng test bạn đã viết).
Nếu chạy Bước 4, API sẽ phản hồi bằng một chuỗi JSON chứa nhãn dự đoán và độ tin cậy.

## 6. Trạng thái hiện tại (Cập nhật: Buổi 9)
☑ Dựng cấu trúc thư mục src/ theo kiến trúc BT1.

☑ Code script chia dữ liệu 70/15/15 (stratify) và hàm làm sạch văn bản (giữ dấu).

☑ Huấn luyện và so sánh 4 mô hình trên tập Validation, chọn ComplementNB.

☑ Xuất Confusion Matrix và viết 3 kết luận phân tích lỗi mô hình.

☑ Viết 6 Unit Test (Luồng đúng, Dữ liệu sai, Giá trị biên) cho hàm làm sạch.

☑ Đóng gói mô hình thành API FastAPI và chạy thành công bằng Docker.

☑ Hoàn thiện các tài liệu bắt buộc (ai-disclosure.md, thay-doi-thiet-ke.md, bug-log.md).