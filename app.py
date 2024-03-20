from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('train-model.joblib')

@app.route('/')
def home():
    return "Welcome to the model prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    data = request.json

    # Convert input to correct format for prediction
    features = [data[f'feature{i+1}'] for i in range(5)]  # Assuming 5 features for the model

    # Make prediction
    prediction = model.predict([features])[0]

    # Return prediction as JSON response
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
