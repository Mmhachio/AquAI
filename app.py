from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__, template_folder="C:/minor project/templates")

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input values from the form
    ph = float(request.form["ph"])
    hardness = float(request.form["hardness"])
    solids = float(request.form["solids"])
    chloramines = float(request.form["chloramines"])
    sulfate = float(request.form["sulfate"])
    conductivity = float(request.form["conductivity"])
    organic_carbon = float(request.form["organic_carbon"])
    trihalomethanes = float(request.form["trihalomethanes"])
    turbidity = float(request.form["turbidity"])

    # Make a prediction using the model
    prediction = model.predict([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])[0]

    # Map prediction to human-readable output
    prediction_text = "Water is Safe" if prediction == 1 else "Water is Unsafe"

    # Render the result template with the prediction
    return render_template("result.html", prediction=prediction_text)


if __name__ == "__main__":
    app.run(debug=True)
