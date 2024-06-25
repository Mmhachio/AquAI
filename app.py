from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load your model
model = joblib.load('path/to/your/model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    features = [float(data['ph']), float(data['hardness']), float(data['solids']), 
                float(data['chloramines']), float(data['sulfate']), float(data['conductivity']),
                float(data['organic_carbon']), float(data['trihalomethanes']), float(data['turbidity'])]
    
    prediction = model.predict([features])[0]
    return jsonify(prediction=prediction)

@app.route('/result', methods=['POST'])
def result():
    data = request.form.to_dict()
    features = [float(data['ph']), float(data['hardness']), float(data['solids']), 
                float(data['chloramines']), float(data['sulfate']), float(data['conductivity']),
                float(data['organic_carbon']), float(data['trihalomethanes']), float(data['turbidity'])]
    
    prediction = model.predict([features])[0]
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
