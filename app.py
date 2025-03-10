from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('best_house_price_model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_features = np.array([data['features']])
    input_features_scaled = scaler.transform(input_features)
    prediction = model.predict(input_features_scaled)
    return jsonify({'predicted_price': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
