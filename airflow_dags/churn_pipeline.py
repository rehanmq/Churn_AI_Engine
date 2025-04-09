from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("churn_ai_engine_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    preprocess = BashOperator(task_id="preprocess", bash_command="python spark_jobs/preprocess_data.py")
    train = BashOperator(task_id="train_model", bash_command="python model_training/train_model_tensorflow.py")
    explain = BashOperator(task_id="explain_model", bash_command="python explainability/shap_explainer.py")

    preprocess >> train >> explain
