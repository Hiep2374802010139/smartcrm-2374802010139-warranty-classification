from sklearn.model_selection import train_test_split

def chia_du_lieu(df, nhan='issue_category', hat_giong=42):
    """Chia 70/15/15, stratify để giữ tỉ lệ nhãn"""
    train, temp = train_test_split(
        df, test_size=0.30, random_state=hat_giong, stratify=df[nhan]
    )
    val, test = train_test_split(
        temp, test_size=0.50, random_state=hat_giong, stratify=temp[nhan]
    )
    return train, val, test