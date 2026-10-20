import pytest
from src.features.text import lam_sach

# ==========================================
# LOẠI 1: LUỒNG ĐÚNG (Happy Path)
# ==========================================
def test_lam_sach_luong_dung():
    cau_goc = "Màn Hình Bị SỌC Xanh!@#"
    ket_qua_mong_doi = "màn hình bị sọc xanh"
    assert lam_sach(cau_goc) == ket_qua_mong_doi

# ==========================================
# LOẠI 3: DỮ LIỆU SAI / BẢO MẬT (Invalid/Masking)
# ==========================================
def test_lam_sach_che_thong_tin_dinh_danh():
    cau_goc = "Gọi cho tôi số 0912345678 hoặc gửi mail tới test@gmail.com"
    ket_qua = lam_sach(cau_goc)
    
    # Cập nhật lại thành chữ thường cho khớp với code mới
    assert "<sdt>" in ket_qua
    assert "<email>" in ket_qua
    
    assert "0912345678" not in ket_qua
    assert "test@gmail.com" not in ket_qua

# ==========================================
# LOẠI 2: GIÁ TRỊ BIÊN (Boundary / Edge Cases)
# ==========================================
@pytest.mark.parametrize("dau_vao", ["", "   ", "\n\t", None])
def test_lam_sach_du_lieu_rong(dau_vao):
    ket_qua = lam_sach(dau_vao)
    assert ket_qua == ""