import subprocess
import os
import json

def test_hai_lan_huan_luyen_cho_ket_qua_giong_nhau():
    lenh = ['python', '-m', 'src.models.train', '--config', 'configs/train.yaml']
    
    # Tạo bản sao môi trường và ép buộc dùng UTF-8 cho tiến trình con
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    
    # Chạy lần 1
    subprocess.run(lenh, check=True, env=env)
    with open('reports/metrics.json', 'r', encoding='utf-8') as f:
        lan1 = json.load(f)
        
    # Chạy lần 2
    subprocess.run(lenh, check=True, env=env)
    with open('reports/metrics.json', 'r', encoding='utf-8') as f:
        lan2 = json.load(f)
        
    # So sánh
    assert lan1 == lan2, "Hai lần chạy cho kết quả khác nhau -> chưa tái lập được"

import json, subprocess

def test_hai_lan_huan_luyen_cho_ket_qua_giong_nhau():
    lenh = ['python', '-m', 'src.models.train', '--config', 'configs/train.yaml']
    subprocess.run(lenh, check=True)
    with open('reports/metrics.json', 'r', encoding='utf-8') as f:
        lan1 = json.load(f)
        
    subprocess.run(lenh, check=True)
    with open('reports/metrics.json', 'r', encoding='utf-8') as f:
        lan2 = json.load(f)
        
    assert lan1['f1_macro_test'] == lan2['f1_macro_test']

from fastapi.testclient import TestClient
from src.serve.app import app
import pytest

client = TestClient(app)

# Test dữ liệu sai (Mô tả quá ngắn)
@pytest.mark.parametrize("mo_ta, ma_loi_mong_doi", [
    ("", 422), ("abc", 422), (None, 422)
])
def test_api_du_doan_du_lieu_sai(mo_ta, ma_loi_mong_doi):
    response = client.post("/du-doan", json={"mo_ta": mo_ta})
    assert response.status_code == ma_loi_mong_doi