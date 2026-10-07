from flask import Flask, render_template, request
import pickle


# Create Flask application
app = Flask(__name__)


# Load the trained Decision Tree model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)


# Iris class names
species = [
    "Iris Setosa",
    "Iris Versicolor",
    "Iris Virginica"
]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get input values from HTML form
    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])

    # Prepare input for the model
    input_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Convert numerical prediction into species name
    predicted_species = species[prediction]

    # Send prediction back to HTML
    return render_template(
        "index.html",
        prediction=predicted_species
    )


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)