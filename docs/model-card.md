Model Details: Logistic Regression/ComplementNB.

Intended Use: Phân loại sự cố thiết bị.

Factors: Không dùng để phân loại ảnh.

Metrics: Macro F1 (0.8346), F1 từng nhãn.

Evaluation Data: Tập test 15% (2400 dòng).

Training Data: File issue_descriptions.csv.

Quantitative Analyses: Bảng F1 từng nhãn.

Ethical Considerations: Dữ liệu được che PII (SĐT, Email).

Caveats and Recommendations: (Rất quan trọng) Nêu rõ hạn chế: Mô hình nhầm lẫn nhiều giữa PIN và SẠC do dùng chung từ ngữ. Nhãn PHẦN MỀM có Recall thấp nhất (66.7%).

Model Version: v0.2 (hoặc 1.0.0).