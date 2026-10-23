import json
import time
import os

def xuat_bao_cao(file_path='reports/metrics.json'):
    # TRẠNG THÁI 1: ĐANG TẢI (Loading)
    print("Đang tải dữ liệu báo cáo...", end="", flush=True)
    time.sleep(1) 
    print(" Xong.")
    
    # TRẠNG THÁI 3: LỖI (Error)
    if not os.path.exists(file_path):
        print(f"[LỖI] Không tìm thấy file {file_path}. Vui lòng chạy train.py trước.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TRẠNG THÁI 2: RỖNG (Empty)
    if not data or 'f1_theo_nhan_test' not in data:
        print("[RỖNG] File metrics.json không có dữ liệu hoặc thiếu thông tin F1.")
        return

    print("\n=== BÁO CÁO CHẤT LƯỢNG MÔ HÌNH ===")
    print(f"Mô hình được chọn: {data['mo_hinh_chon']}")
    print(f"F1-Macro (Test): {data['f1_macro_test']}")
    print("\nF1 theo từng nhãn:")
    for nhan, f1 in data['f1_theo_nhan_test'].items():
        # Xử lý nhãn thiếu dữ liệu/bị bỏ rơi
        canh_bao = " (CẢNH BÁO: F1 < 0.7)" if f1 < 0.7 else ""
        print(f" - {nhan}: {f1}{canh_bao}")

if __name__ == '__main__':
    xuat_bao_cao()