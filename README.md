# SmartCRM - Phân loại yêu cầu bảo hành tự động (Luồng L10)

**Họ và tên:** Lê Hoàng Hiệp
**MSSV:** 2374802010139
**Track:** AI (Trí tuệ nhân tạo)

## 1. Mô tả hệ thống
Dự án xây dựng module cốt lõi cho hệ thống SmartCRM của Mekong Mobile, giải quyết bài toán tự động phân loại mô tả lỗi (văn bản tự do) của khách hàng thành các nhóm sự cố (MÀN HÌNH, PIN, SẠC, PHẦN MỀM, NƯỚC VÀO, KHÁC). Hệ thống sử dụng phương pháp TF-IDF để vector hóa văn bản và mô hình Logistic Regression để huấn luyện, giúp giảm thời gian phân loại thủ công và hỗ trợ nhân viên tiếp nhận.

## 2. Yêu cầu môi trường
- **Ngôn ngữ:** Python 3.9 trở lên (đã test trên Python 3.10+)
- **Thư viện:** Các thư viện cần thiết đã được ghim phiên bản trong file `requirements.txt` (pandas, scikit-learn, pyyaml, pytest...).

## 3. Hướng dẫn cài đặt và chạy (Từng bước một lệnh)

**Bước 1: Cài đặt các thư viện phụ thuộc**

pip install -r requirements.txt

**Bước 2: Huấn luyện mô hình (Chạy bằng 1 lệnh)**

python -m src.models.train --config configs/train.yaml
