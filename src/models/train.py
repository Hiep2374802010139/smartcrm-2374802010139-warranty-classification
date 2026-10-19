import argparse, json, random, yaml, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from src.data.split import chia_du_lieu
from src.features.text import lam_sach, tao_vectorizer
from src.models.baseline import baseline_da_so

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--config', required=True)
    cfg = yaml.safe_load(open(ap.parse_args().config, encoding='utf-8'))
    hg = cfg['hat_giong']; random.seed(hg); np.random.seed(hg)

    # 1. Load data
    print("Đang nạp dữ liệu...")
    df = pd.read_csv(cfg['duong_dan_du_lieu'])
    
    # 2. CHIA TRƯỚC (Tránh rò rỉ dữ liệu)
    print("Đang chia dữ liệu...")
    train, val, test = chia_du_lieu(df, hat_giong=hg)
    
    # 3. Làm sạch văn bản
    print("Đang làm sạch văn bản...")
    t_tr, t_va, t_te = (x['issue_desc'].map(lam_sach) for x in (train, val, test))
    
    # 4. Fit Vectorizer CHỈ TRÊN TRAIN
    print("Đang vector hóa...")
    vec = tao_vectorizer()
    X_tr = vec.fit_transform(t_tr)
    X_va, X_te = vec.transform(t_va), vec.transform(t_te)
    
    y_tr, y_va, y_te = train['issue_category'], val['issue_category'], test['issue_category']

    # 5. Huấn luyện & Đánh giá (Dùng C=1 cho nhanh)
    print("Đang huấn luyện mô hình...")
    m = LogisticRegression(C=1, max_iter=1000, class_weight='balanced', random_state=hg)
    m.fit(X_tr, y_tr)
    y_pred = m.predict(X_te)

    # 6. Lưu kết quả
    print("Đang lưu kết quả...")
    ket_qua = {
        'hat_giong': hg,
        'so_mau_train': len(train), 'so_mau_val': len(val), 'so_mau_test': len(test),
        'f1_macro_baseline_da_so': round(baseline_da_so(y_tr, y_te), 3),
        'f1_macro_mo_hinh_chinh': round(f1_score(y_te, y_pred, average='macro'), 3),
        'f1_theo_nhan': {n: round(float(v), 3) for n, v in zip(m.classes_, f1_score(y_te, y_pred, average=None, labels=m.classes_))},
    }
    
    with open('reports/metrics.json', 'w', encoding='utf-8') as f:
        json.dump(ket_qua, f, ensure_ascii=False, indent=2, sort_keys=True)
    print("Hoàn thành! Đã lưu kết quả vào reports/metrics.json")
    print(json.dumps(ket_qua, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()