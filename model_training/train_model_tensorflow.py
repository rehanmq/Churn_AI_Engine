import pandas as pd
import tensorflow as tf
from sklearn.metrics import roc_auc_score

def train_model():
    # Load preprocessed data
    df = pd.read_parquet("data/processed/cleaned_data.parquet")

    # Select numeric features and label
    X = df[["tenure", "monthly_charges"]]
    y = df["label"]

    # Define the model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X, y, epochs=10, batch_size=32)

    # ===== Evaluate ROC-AUC Score =====
    y_pred = model.predict(X)
    roc_auc = roc_auc_score(y, y_pred)
    print("\n✅ ROC-AUC Score:", round(roc_auc, 4))  # Optional: round for readability

    # Save the trained model
    model.save("model_training/model_tf.h5")

if __name__ == '__main__':
    train_model()
