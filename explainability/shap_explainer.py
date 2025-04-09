import shap
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

def run_shap():
    df = pd.read_parquet("data/processed/cleaned_data.parquet")

    # ✅ Select only numeric input features
    X = df[["tenure", "monthly_charges"]]
    model = tf.keras.models.load_model("model_training/model_tf.h5")

    explainer = shap.Explainer(model.predict, X)
    shap_values = explainer(X)

    shap.summary_plot(shap_values, X, show=False)
    plt.savefig("explainability/shap_summary.png")

if __name__ == '__main__':
    run_shap()
