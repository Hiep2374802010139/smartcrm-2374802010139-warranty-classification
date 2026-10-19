import re
from sklearn.feature_extraction.text import TfidfVectorizer

def lam_sach(s):
    """Làm sạch văn bản, GIỮ DẤU tiếng Việt, thay thế thông tin định danh"""
    if not isinstance(s, str):
        return ""
    s = s.lower()
    # Thay thế số điện thoại và email bằng thẻ
    s = re.sub(r'\b0\d{9}\b', ' <SDT> ', s)
    s = re.sub(r'\S+@\S+', ' <EMAIL> ', s)
    # Xóa ký tự đặc biệt, giữ lại chữ cái (bao gồm cả có dấu) và số
    s = re.sub(r'[^\w\sàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def tao_vectorizer():
    return TfidfVectorizer(ngram_range=(1, 2), max_features=20000)