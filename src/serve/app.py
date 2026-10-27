import os, time, logging, joblib
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.features.text import lam_sach
from src.log_config import cau_hinh_log
from src.serve.errors import dang_ky_xu_ly_loi

cau_hinh_log()
log = logging.getLogger('serve')

MODEL_PATH = os.environ.get('MODEL_PATH', 'artifacts/model_v1.joblib')
NGUONG_TIN_CAY = float(os.environ.get('NGUONG_TIN_CAY', '0.45'))

trang_thai = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Nạp mô hình MỘT LẦN khi khởi động
    goi = joblib.load(MODEL_PATH)
    trang_thai['vectorizer'] = goi['vectorizer']
    trang_thai['model'] = goi['model']
    trang_thai['nhan_labels'] = list(goi['model'].classes_)
    trang_thai['phien_ban'] = "1.0.0"
    log.info('đã nạp mô hình từ %s', MODEL_PATH)
    yield
    trang_thai.clear()

app = FastAPI(title='Phân loại sự cố - Mekong Mobile', version='1.0', lifespan=lifespan)
dang_ky_xu_ly_loi(app) # Đăng ký bắt lỗi

class YeuCau(BaseModel):
    mo_ta: str = Field(min_length=5, max_length=2000)

class NhanDuDoan(BaseModel):
    nhan: str
    do_tin_cay: float

class PhanHoi(BaseModel):
    nhan_goi_y: str | None
    do_tin_cay: float
    top_3: list[NhanDuDoan]
    can_nguoi_xem_lai: bool
    phien_ban_mo_hinh: str

@app.get('/health')
def health():
    if 'model' not in trang_thai:
        raise HTTPException(503, 'Mô hình chưa nạp xong')
    return {'status': 'ok', 'phien_ban_mo_hinh': trang_thai['phien_ban']}

@app.post('/du-doan', response_model=PhanHoi)
def du_doan(req: YeuCau):
    t0 = time.perf_counter()
    x = trang_thai['vectorizer'].transform([lam_sach(req.mo_ta)])
    
    # Mô hình ComplementNB có predict_proba
    xac_suat = trang_thai['model'].predict_proba(x)[0]
    thu_tu = xac_suat.argsort()[::-1]
    
    top3 = [NhanDuDoan(nhan=trang_thai['nhan_labels'][i], do_tin_cay=round(float(xac_suat[i]), 4)) for i in thu_tu[:3]]
    du_tin_cay = top3[0].do_tin_cay >= NGUONG_TIN_CAY
    
    log.info('dự đoán xong: tin cậy=%.2f, %1f ms', top3[0].do_tin_cay, (time.perf_counter() - t0) * 1000)
    
    return PhanHoi(
        nhan_goi_y=top3[0].nhan if du_tin_cay else None,
        do_tin_cay=top3[0].do_tin_cay,
        top_3=top3,
        can_nguoi_xem_lai=not du_tin_cay,
        phien_ban_mo_hinh=trang_thai['phien_ban'],
    )