# Nhật ký thay đổi thiết kế 

## TD-01: Bổ sung mô tả bảng prediction_log và model_metric_log
- **Phân hồi của GV**: Bảng prediction_log (có cột human_corrected_category) và model_metric_log được dùng ở UC nhưng chưa được mô tả cột.
- **Quyết định**: SỬA
- **Lý do**: Cần đặc tả rõ cấu trúc CSDL để hiện thực hóa ở BT2.
- **Ảnh hưởng**: Thêm mục 4.2 vào tài liệu thiết kế (ERD/Dictionary).

## TD-02: Đánh số lại luồng chính UC03
- **Phân hồi của GV**: Luồng chính UC03 chưa đánh số bước, ngoại lệ ghi 3a, 4a gây khó đối chiếu.
- **Quyết định**: SỬA
- **Lý do**: Đảm bảo tính truy vết (traceability) giữa đặc tả và code.
- **Ảnh hưởng**: Cập nhật lại tài liệu SRS mục 2.2.