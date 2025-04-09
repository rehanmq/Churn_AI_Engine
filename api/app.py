from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model("../model_training/model_tf.h5")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = np.array(request.json["data"]).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({"churn_probability": float(prediction[0][0])})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
