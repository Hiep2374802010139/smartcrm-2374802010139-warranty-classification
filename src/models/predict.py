import joblib
import argparse
from src.features.text import lam_sach

def du_doan(mo_ta_loi, model_path='artifacts/model_v1.joblib'):
    try:
        # 1. Load mô hình đã lưu
        artifact = joblib.load(model_path)
        vec = artifact['vectorizer']
        model = artifact['model']
        
        # 2. Làm sạch văn bản (Áp dụng đúng hợp đồng dữ liệu)
        text_sach = lam_sach(mo_ta_loi)
        if not text_sach:
            return {"loi": "Mô tả rỗng, không thể dự đoán."}
        
        # 3. Vector hóa (CHỈ DÙNG TRANSFORM, KHÔNG FIT)
        X_new = vec.transform([text_sach])
        
        # 4. Dự đoán
        nhan_du_doan = model.predict(X_new)[0]
        
        # 5. Lấy độ tin cậy (nếu mô hình hỗ trợ predict_proba)
        do_tin_cay = 0.0
        if hasattr(model, "predict_proba"):
            do_tin_cay = max(model.predict_proba(X_new)[0])
            
        return {
            "nhan": nhan_du_doan,
            "do_tin_cay": round(do_tin_cay, 4)
        }
    except FileNotFoundError:
        return {"loi": f"Không tìm thấy file mô hình tại {model_path}. Hãy chạy train.py trước."}

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--mota', type=str, required=True, help="Mô tả lỗi của khách hàng")
    args = ap.parse_args()
    
    ket_qua = du_doan(args.mota)
    print(f"\nMô tả: '{args.mota}'")
    print(f"Kết quả dự đoán: {ket_qua}")