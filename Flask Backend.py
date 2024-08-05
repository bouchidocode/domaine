from flask import Flask, request, jsonify
import joblib

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('domain_value_model.pkl')

@app.route('/estimate', methods=['POST'])
def estimate_value():
    data = request.json
    # Assume data is a dictionary with necessary features
    input_features = np.array([data['feature1'], data['feature2'], ...]).reshape(1, -1)
    estimated_value = model.predict(input_features)[0]
    return jsonify({'estimated_value': estimated_value})

if __name__ == '__main__':
    app.run(debug=True)
