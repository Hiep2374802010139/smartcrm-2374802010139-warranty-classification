import argparse, json, random, yaml, numpy as np, pandas as pd, joblib, pathlib
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import ComplementNB
from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score, confusion_matrix
from src.data.split import chia_du_lieu
from src.features.text import lam_sach, tao_vectorizer

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--config', required=True)
    cfg = yaml.safe_load(open(ap.parse_args().config, encoding='utf-8'))
    hg = cfg['hat_giong']; random.seed(hg); np.random.seed(hg)

    df = pd.read_csv(cfg['duong_dan_du_lieu'])
    train, val, test = chia_du_lieu(df, hat_giong=hg)
    
    # Làm sạch
    t_tr, t_va, t_te = (x['issue_desc'].map(lam_sach) for x in (train, val, test))
    
    # Vector hóa (CHỈ FIT TRÊN TRAIN)
    vec = tao_vectorizer()
    X_tr = vec.fit_transform(t_tr)
    X_va, X_te = vec.transform(t_va), vec.transform(t_te)
    y_tr, y_va, y_te = train['issue_category'], val['issue_category'], test['issue_category']

    # 1. SO SÁNH CÁC MÔ HÌNH TRÊN TẬP VALIDATION
    models = {
        'dummy_da_so': DummyClassifier(strategy='most_frequent'),
        'logistic': LogisticRegression(max_iter=1000, class_weight='balanced', random_state=hg),
        'linear_svc': LinearSVC(class_weight='balanced', random_state=hg),
        'complement_nb': ComplementNB()
    }
    
    ket_qua_val = {}
    best_model_name = ""
    best_f1 = -1

    print("--- ĐÁNH GIÁ TRÊN TẬP VALIDATION ---")
    for name, model in models.items():
        model.fit(X_tr, y_tr)
        y_pred_val = model.predict(X_va)
        f1 = f1_score(y_va, y_pred_val, average='macro', zero_division=0)
        ket_qua_val[name] = round(f1, 4)
        print(f"{name:15s} | F1 Macro: {f1:.4f}")
        
        if f1 > best_f1 and name != 'dummy_da_so':
            best_f1 = f1
            best_model_name = name
            best_model = model

    print(f"\n=> Mô hình tốt nhất được chọn: {best_model_name}")

    # 2. ĐO LƯỜNG TRÊN TẬP TEST (CHỈ 1 LẦN DUY NHẤT)
    y_pred_test = best_model.predict(X_te)
    cm = confusion_matrix(y_te, y_pred_test, labels=best_model.classes_)

    ket_qua_cuoi = {
        'hat_giong': hg,
        'so_mau_train': len(train), 'so_mau_val': len(val), 'so_mau_test': len(test),
        'f1_macro_val_cac_mo_hinh': ket_qua_val,
        'mo_hinh_chon': best_model_name,
        'f1_macro_test': round(f1_score(y_te, y_pred_test, average='macro'), 4),
        'f1_theo_nhan_test': {n: round(float(v), 4) for n, v in zip(best_model.classes_, f1_score(y_te, y_pred_test, average=None, labels=best_model.classes_))},
        'confusion_matrix': cm.tolist(),
        'nhan_labels': list(best_model.classes_)
    }
    
    # Ghi metrics.json
    with open('reports/metrics.json', 'w', encoding='utf-8') as f:
        json.dump(ket_qua_cuoi, f, ensure_ascii=False, indent=2, sort_keys=True)
    
    # 3. LƯU MÔ HÌNH (Lưu cả vectorizer và model)
    pathlib.Path('artifacts').mkdir(exist_ok=True)
    joblib.dump({'vectorizer': vec, 'model': best_model, 'nhan_labels': list(best_model.classes_)}, 'artifacts/model_v1.joblib')
    print("\nĐã lưu mô hình vào artifacts/model_v1.joblib và kết quả vào reports/metrics.json")

if __name__ == '__main__':
    main()