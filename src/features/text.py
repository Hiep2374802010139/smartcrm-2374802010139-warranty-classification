import re
from sklearn.feature_extraction.text import TfidfVectorizer

def lam_sach(s):
    """
    HỢP ĐỒNG DỮ LIỆU:
    - Hình dạng: Nhận vào 1 chuỗi (string) hoặc None. 
    - Ý nghĩa: Trả về chuỗi đã chuẩn hóa (lowercase, giữ dấu, che SĐT/Email).
    - Hành vi khi sai: Nếu đầu vào là None hoặc không phải string -> trả về chuỗi rỗng "", KHÔNG ném ngoại lệ.
    """
    if not isinstance(s, str):
        return ""
    s = s.lower()
    
    # 1. Regex email chặt chẽ hơn (phải có tên miền .com, .vn...)
    s = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', ' <email> ', s)
    
    # 2. Regex số điện thoại
    s = re.sub(r'\b0\d{9}\b', ' <sdt> ', s)
    
    # 3. Xóa ký tự đặc biệt, NHƯNG GIỮ LẠI dấu < > để không làm hỏng thẻ
    s = re.sub(r'[^\w\sàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ<>]', ' ', s)
    
    return re.sub(r'\s+', ' ', s).strip()

def tao_vectorizer():
    return TfidfVectorizer(ngram_range=(1, 2), max_features=20000)