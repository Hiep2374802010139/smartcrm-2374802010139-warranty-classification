# Model Card: Warranty Issue Classification

## 1. Basic Information
- **Model name:** `warranty-classification` v1.0
- **Author:** Lê Hoàng Hiệp (MSSV: 2374802010139)

## 2. Intended Use
Suggests an issue category to intake staff based on free-text descriptions. Staff makes the final decision.

## 3. Out-of-Scope Uses (SHOULD NOT be used for)
- NOT for automatically assigning technicians.
- NOT for deciding warranty eligibility without human confirmation.
- NOT for languages other than Vietnamese.

## 4. Training Data
- **Source:** `issue_descriptions.csv` (2400 samples).
- **Split:** 70/15/15 (stratified), `random_state=42`.
- **Label Distribution:** MAN_HINH (32.8%), PIN (24.5%), etc.

## 5. Architecture and Processing
- **Vectorizer:** TF-IDF (ngram 1-2, max_features=20000).
- **Model:** ComplementNB (chosen via validation set comparison).
- **Preprocessing:** Lowercase, keep Vietnamese diacritics, mask Phone/Email.

## 6. Evaluation Metrics
- **Test F1-macro:** `0.8346` (Data v1.0, seed 42).
- **Per-label F1:** KHAC (0.81), MAN_HINH (0.90), NUOC_VAO (0.83), PHAN_MEM (0.77), PIN (0.86), SAC (0.85).

## 7. Baseline
- **Dummy Classifier (Majority class):** F1-macro = `0.059`.

## 8. Measured Bias
- Measured by label. The minority label `KHAC` (5.5% of data) achieved an F1 of 0.81, showing no significant bias against the minority class. The confusion matrix shows confusion between `PIN` and `SAC` due to similar wording.

## 9. Risks and Limitations
- **(a) Similar wording:** Descriptions for `PIN` and `SAC` are often confused. *Mitigation:* Staff reviews the top 3 predictions.
- **(b) Low confidence:** If confidence is < 0.45, the system flags `can_nguoi_xem_lai = true`. *Mitigation:* Staff must choose manually.

## 10. Maintenance
- Retrain when the staff correction rate exceeds 35%, or when a new issue category is added.