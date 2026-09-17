import os

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("house_model.pkl")

@app.route("/")
def home():
    return "House Price Prediction API"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    size = data["size"]

    prediction = model.predict([[size]])

    return jsonify({
        "house_size": size,
        "predicted_price": float(prediction[0])
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=port, debug=debug)