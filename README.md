# Churn_AI_Engine
The Smart Engine for Customer Retention and Churn Insight

# Churn_AI_Engine - Intelligent Churn Prediction and Explainability Engine

This repository contains the codebase for **Churn_AI_Engine**, an end-to-end machine learning pipeline designed to predict customer churn and provide business-explainable insights using SHAP.

## 🧠 Project Summary
Churn_AI_Engine is built to help B2C companies identify at-risk customers and explain churn drivers using interpretable machine learning. The system is modular, scalable, and production-ready, built using industry-grade tools for big data and explainable AI.

## 📊 Results & Achievements
- Achieved **87.3% ROC-AUC** score on test set using TensorFlow
- Preprocessing completed in **7.09s (PySpark)** vs **0.03s (Pandas)** on small data; PySpark enables large-scale scalability
- Real-time churn prediction served via Flask API with sub-100ms latency
- Customer-specific SHAP explanations enable actionable decision-making via dashboards

## 🛠 Tools & Technologies
**Python, PySpark, TensorFlow, Flask, SHAP, Apache Airflow, Pandas, Scikit-learn, Power BI, GitHub Codespaces**

## 📁 Project Structure
```
churn_ai_engine/
├── data/
│   ├── raw/                        # Raw input data
│   └── processed/                  # Cleaned and transformed data
├── spark_jobs/
│   ├── preprocess_data.py         # PySpark script for preprocessing
│   ├── preprocess_pandas.py       # Pandas-based benchmark version
├── model_training/
│   ├── train_model_tensorflow.py  # Model training using TensorFlow
│   └── utils.py                   # Utility functions
├── explainability/
│   └── shap_explainer.py          # SHAP-based explanation script
├── api/
│   └── app.py                     # Flask API to serve predictions
├── airflow_dags/
│   └── churn_pipeline.py          # Airflow DAG for automation
├── dashboards/
│   └── powerbi_dashboard.pbix     # Power BI Dashboard (or Tableau)
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker setup
├── README.md                      # Project documentation
```

## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Churn_AI_Engine.git
cd Churn_AI_Engine
```

### 2. Launch in GitHub Codespaces
Use GitHub Codespaces to open and run the full stack directly in the cloud.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Preprocessing (PySpark)
```bash
python spark_jobs/preprocess_data.py
```

### 5. Train Model (TensorFlow + ROC-AUC Evaluation)
```bash
python model_training/train_model_tensorflow.py
```

### 6. Run SHAP Explainability
```bash
python explainability/shap_explainer.py
```

### 7. Serve Real-Time Predictions
```bash
cd api
python app.py
```
Test with:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [12, 79.9]}'
```

### 8. Airflow DAG (Optional Automation)
Place `churn_pipeline.py` into Airflow's DAG folder and start the scheduler.

### 9. Visualize in Power BI
Use `data/processed/predictions.csv` + `shap_summary.png` to build interactive dashboards.

## 🤝 Contributing
Pull requests and feature suggestions are welcome. Please open an issue first to discuss changes.

---
Built with ❤️ in GitHub Codespaces
