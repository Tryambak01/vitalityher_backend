from flask import Flask, request, jsonify
import numpy as np
from fuzzy_logic import predictRes  # Import your ML function
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/predict', methods=['POST'])
@cross_origin(supports_credentials=True)
def predict():
    try:
        data = request.json  # Assuming data is sent as JSON into the backend
        answers = np.array(data['answers'])
        print(answers)
    
        prediction = predictRes(answers)  # Calling fuzzy logic function
        return prediction
    except Exception as e:
        return jsonify({"message": "Error", "error": str(e)})


@app.route('/get-questions', methods=['GET'])
def getQuestions():
    with open('questions.json') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
