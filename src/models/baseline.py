from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score

def baseline_da_so(y_train, y_test):
    """Mức sàn: luôn đoán nhãn xuất hiện nhiều nhất"""
    m = DummyClassifier(strategy='most_frequent').fit([[0]] * len(y_train), y_train)
    y_pred = m.predict([[0]] * len(y_test))
    return f1_score(y_test, y_pred, average='macro', zero_division=0)