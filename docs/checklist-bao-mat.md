# Security Checklist (Track AI)

| STT | Hạng mục | Trạng thái | Minh chứng / Lý do |
| :--- | :--- | :--- | :--- |
| 1 | Không có secret trong repo | ĐÃ LÀM | Chạy lệnh `git log --all --oneline -- .env` không ra kết quả. |
| 2 | Dữ liệu vào được kiểm tra | ĐÃ LÀM | Pydantic schema giới hạn `mo_ta` từ 5-2000 ký tự. Test case trả về 422 khi sai. |
| 3 | Kiểm soát truy cập | KHÔNG ÁP DỤNG | Module AI không có chức năng đăng nhập người dùng. |
| 4 | Mật khẩu băm/mã hóa | KHÔNG ÁP DỤNG | Không có chức năng lưu mật khẩu. |
| 5 | Thông báo lỗi không lộ nội bộ | ĐÃ LÀM | API trả về mã 422/500 với message chung, không trả stack trace. |
| 6 | Nhật ký an toàn | ĐÃ LÀM | Log chỉ ghi `do_dai_mo_ta`, `nhan_du_doan`, `do_tin_cay`, KHÔNG ghi nội dung mô tả. |
| 7 | Phụ thuộc ghim phiên bản | ĐÃ LÀM | File `requirements.txt` đã dùng `==`. |