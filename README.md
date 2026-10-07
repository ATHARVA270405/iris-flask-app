# 🌸 Iris Species Classifier — Flask + Decision Tree

A machine learning web application that predicts the species of an Iris flower based on its **sepal and petal measurements**.

The application uses a **pre-trained Decision Tree Classifier** and **Flask** to provide a simple web interface where users can enter flower measurements and receive a predicted Iris species.

---

## 📌 Project Overview

The Iris dataset contains measurements of Iris flowers belonging to three different species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

The trained Decision Tree model takes four features as input:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

The trained model is saved as a `.pkl` file and then loaded by the Flask application for making predictions on new user input.

---

## 🎯 Objective

The main objective of this project is to understand how a **machine learning model can be deployed as a web application**.

The project demonstrates the complete workflow:

```text
Iris Dataset
     ↓
Data Preparation
     ↓
Decision Tree Training
     ↓
Model Evaluation
     ↓
Save Trained Model
     ↓
Flask Application
     ↓
User Input
     ↓
Model Prediction
     ↓
Predicted Iris Species
```

---

## 🧠 Machine Learning Model

### Algorithm

**Decision Tree Classifier**

The Decision Tree was trained using the Iris dataset available through Scikit-learn.

The model learns decision rules based on the four flower measurements and classifies each flower into one of the three species.

### Input Features

| Feature      | Description               |
| ------------ | ------------------------- |
| Sepal Length | Length of the sepal in cm |
| Sepal Width  | Width of the sepal in cm  |
| Petal Length | Length of the petal in cm |
| Petal Width  | Width of the petal in cm  |

### Target Classes

| Model Output | Species         |
| -----------: | --------------- |
|          `0` | Iris Setosa     |
|          `1` | Iris Versicolor |
|          `2` | Iris Virginica  |

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Flask
* HTML
* CSS
* Pickle
* Jupyter Notebook

---

## 📁 Project Structure

```text
iris-flask-app/
│
├── app.py
├── iris_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### File Description

#### `app.py`

The main Flask application.

It:

* Creates the Flask server
* Loads the trained Decision Tree model
* Receives user input
* Prepares the input for the model
* Makes predictions
* Sends the prediction back to the webpage

#### `iris_model.pkl`

Contains the **already-trained Decision Tree model**.

The model is serialized using Python's `pickle` module so that it can be loaded later without retraining.

#### `templates/index.html`

The frontend of the application.

It contains:

* Input fields
* Prediction button
* Prediction result

#### `static/style.css`

Contains the CSS used to style the web application.

---

# ⚙️ How the Application Works

## 1. Model Training

The Decision Tree model was trained using the Iris dataset.

The model learns the relationship between:

```text
Flower Measurements → Iris Species
```

After training, the model is saved as:

```text
iris_model.pkl
```

---

## 2. Loading the Model

When the Flask application starts, the saved model is loaded:

```python
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)
```

This means the model does **not need to be trained again** every time the web application starts.

---

## 3. User Input

The user enters four measurements through the web form:

```text
Sepal Length
Sepal Width
Petal Length
Petal Width
```

For example:

```text
5.1
3.5
1.4
0.2
```

---

## 4. Flask Receives the Input

The HTML form sends the data to the Flask `/predict` route using the `POST` method.

Flask retrieves the values:

```python
sepal_length = float(request.form["sepal_length"])
sepal_width = float(request.form["sepal_width"])
petal_length = float(request.form["petal_length"])
petal_width = float(request.form["petal_width"])
```

---

## 5. Preparing Model Input

The four values are converted into the format expected by Scikit-learn:

```python
input_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]
```

For example:

```python
[[5.1, 3.5, 1.4, 0.2]]
```

This represents:

```text
1 sample × 4 features
```

---

## 6. Prediction

The trained Decision Tree makes the prediction:

```python
prediction = model.predict(input_data)[0]
```

For example:

```text
0
```

The numerical prediction is then converted into the actual species name:

```python
species = [
    "Iris Setosa",
    "Iris Versicolor",
    "Iris Virginica"
]

predicted_species = species[prediction]
```

Therefore:

```text
0 → Iris Setosa
```

---

## 7. Displaying the Result

The prediction is sent back to the HTML page:

```python
return render_template(
    "index.html",
    prediction=predicted_species
)
```

The user then sees the predicted species on the webpage.

---

# 🔄 Application Architecture

```text
                 USER
                  │
                  ▼
        ┌───────────────────┐
        │    HTML FORM      │
        │                   │
        │ Sepal Length      │
        │ Sepal Width       │
        │ Petal Length      │
        │ Petal Width       │
        └─────────┬─────────┘
                  │
                  │ POST /predict
                  ▼
        ┌───────────────────┐
        │      FLASK        │
        │      app.py       │
        └─────────┬─────────┘
                  │
                  ▼
        ┌───────────────────┐
        │  iris_model.pkl   │
        │                   │
        │ Decision Tree     │
        └─────────┬─────────┘
                  │
                  │ Prediction
                  ▼
        ┌───────────────────┐
        │  Species Mapping  │
        │                   │
        │ 0 → Setosa        │
        │ 1 → Versicolor    │
        │ 2 → Virginica     │
        └─────────┬─────────┘
                  │
                  ▼
        ┌───────────────────┐
        │   HTML Result     │
        │                   │
        │ Iris Setosa       │
        └───────────────────┘
```

---

# 💻 Installation

Install the required Python libraries:

```bash
pip install flask scikit-learn pandas numpy
```

---

# ▶️ Running the Application

Open **Anaconda Prompt** or a terminal.

Navigate to the project directory:

```bash
cd path/to/iris-flask-app
```

Run the Flask application:

```bash
python app.py
```

The Flask server will start at:

```text
http://127.0.0.1:5000
```

Open this address in your browser.

---

# 🧪 Testing the Application

## Test Case 1 — Iris Setosa

Input:

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

Expected output:

```text
Iris Setosa
```

---

## Test Case 2 — Iris Versicolor

Input:

```text
Sepal Length: 6.0
Sepal Width: 2.9
Petal Length: 4.5
Petal Width: 1.5
```

Expected output:

```text
Iris Versicolor
```

---

## Test Case 3 — Iris Virginica

Input:

```text
Sepal Length: 6.7
Sepal Width: 3.0
Petal Length: 5.2
Petal Width: 2.3
```

Expected output:

```text
Iris Virginica
```

---

# 📊 Example Prediction

For the input:

```text
[5.1, 3.5, 1.4, 0.2]
```

the Decision Tree predicts:

```text
Model Output: 0
```

which is mapped to:

```text
Iris Setosa
```

---

# 🔑 Important Concepts Learned

This project demonstrates several important machine learning and deployment concepts:

### Machine Learning

* Supervised Learning
* Classification
* Decision Trees
* Training and testing
* Model prediction
* Model serialization

### Flask

* Flask application
* Routes
* GET and POST requests
* HTML templates
* Form handling
* Sending data from frontend to backend

### Model Deployment

* Saving a trained ML model
* Loading a saved model
* Using a trained model for real-time predictions
* Connecting an ML model with a web interface

---

# 🧩 Why Save the Model?

Training a machine learning model can take time and computational resources.

Instead of training the Decision Tree every time the Flask application starts, the trained model is saved:

```text
Decision Tree
     ↓
iris_model.pkl
```

The Flask application then loads it:

```text
iris_model.pkl
     ↓
Flask
     ↓
Prediction
```

This separates **model training** from **model deployment**.

---

# 🚀 Future Improvements

Possible improvements to this project include:

* Display prediction probabilities
* Add Decision Tree visualization
* Add input validation
* Improve UI/UX
* Add responsive design
* Add prediction history
* Deploy the application online
* Add Docker support
* Create an API endpoint
* Add model performance metrics
* Add automated testing

---

# 📚 Learning Outcome

Through this project, I learned how to take a trained machine learning model and integrate it into a web application.

The project helped me understand the complete pipeline:

```text
Machine Learning
      ↓
Model Training
      ↓
Model Saving
      ↓
Flask Backend
      ↓
Frontend
      ↓
User Input
      ↓
Prediction
```

This demonstrates a basic **machine learning deployment workflow** using Python and Flask.

---

## 👨‍💻 Author

**Atharva Pundkar**

Built as a machine learning deployment project using Python, Scikit-learn, Decision Tree, and Flask.
