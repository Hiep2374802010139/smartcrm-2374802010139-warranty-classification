# SmartCRM - Phân loại yêu cầu bảo hành tự động (Luồng L10)

**Họ và tên:** Lê Hoàng Hiệp  
**MSSV:** 2374802010139  
**Lớp:** 261_71ITGR40203_05  
**Track:** AI (Trí tuệ nhân tạo)  
**Link Repo GitHub:** `https://github.com/Hiep2374802010139/smartcrm-2374802010139-warranty-classification`  
**Tag phiên bản:** `v0.2`

## 1. Mô tả hệ thống
Dự án xây dựng module cốt lõi cho hệ thống SmartCRM của Mekong Mobile, giải quyết bài toán tự động phân loại mô tả lỗi (văn bản tự do) của khách hàng thành 6 nhóm sự cố (MÀN HÌNH, PIN, SẠC, PHẦN MỀM, NƯỚC VÀO, KHÁC). Hệ thống sử dụng phương pháp TF-IDF để vector hóa văn bản và so sánh 4 mô hình (Dummy, Logistic, LinearSVC, ComplementNB). Mô hình tốt nhất được chọn dựa trên tập Validation và đánh giá một lần duy nhất trên tập Test.

## 2. Yêu cầu môi trường
- **Ngôn ngữ:** Python 3.9 trở lên (đã test trên Python 3.10+).
- **Thư viện:** Các thư viện cần thiết đã được ghim phiên bản chính xác trong file `requirements.txt`.
- **Dữ liệu:** File `issue_descriptions.csv` (đã được đặt sẵn trong thư mục `data/` của repo).

## 3. Cấu trúc thư mục
```text
├── configs/               # Chứa file cấu hình train.yaml (siêu tham số, seed)
├── data/                  # Chứa file dữ liệu nguồn issue_descriptions.csv
├── docs/                  # Chứa tài liệu (thay-doi-thiet-ke.md, ai-disclosure.md, ảnh minh chứng)
├── reports/               # Chứa file kết quả metrics.json sinh ra sau khi train
├── src/                   # Mã nguồn chính
│   ├── data/              # Code xử lý chia dữ liệu
│   ├── features/          # Code làm sạch văn bản, vector hóa TF-IDF
│   └── models/            # Code chứa baseline và script huấn luyện
├── tests/                 # Chứa các file Unit Test (test_text.py)
└── README.md              # Tài liệu hướng dẫn này.
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

## 5. Cách kiểm tra hệ thống đã chạy đúng
Sau khi chạy lệnh ở Bước 2 thành công, hệ thống sẽ tự động sinh ra 2 tệp minh chứng:

reports/metrics.json: Chứa điểm F1-macro của 4 mô hình trên tập Validation, mô hình được chọn, điểm F1-macro trên tập Test, F1 từng nhãn và Confusion Matrix.

artifacts/model_v1.joblib: File mô hình đã được lưu (đã được chặn bởi .gitignore).

Sau khi chạy Bước 3, màn hình Terminal phải hiển thị dòng chữ xanh: 6 passed (hoặc số lượng test bạn đã viết).
## 6. Trạng thái hiện tại (Cập nhật: Buổi 9)
☑ Dựng cấu trúc thư mục src/ theo kiến trúc BT1.

☑ Code script chia dữ liệu 70/15/15 (stratify) và hàm làm sạch văn bản (giữ dấu).

☑ Huấn luyện và so sánh 4 mô hình trên tập Validation.

☑ Chọn mô hình ComplementNB (F1-val: 0.8236) và đánh giá 1 lần trên tập Test (F1-test: 0.8346).

☑ Xuất Confusion Matrix và viết 3 kết luận phân tích lỗi mô hình.

☑ Viết 3 loại Unit Test (Luồng đúng, Dữ liệu sai, Giá trị biên) cho hàm làm sạch.

☑ Đã chụp ảnh minh chứng kết quả chạy lưu tại docs/.