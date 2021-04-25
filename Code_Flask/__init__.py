from flask import Flask, request, render_template, url_for
import pickle
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = '026c4ba5ad18bcc7b243b4d9'
model = joblib.load('Code_Flask/iris_classifier_knn.joblib')
@app.route('/', methods=["GET","POST"])
def home():
    preds = []
    global model
    if request.method == "POST":
        sepal_length = request.form.get("sepal_length")
        sepal_width = request.form.get("sepal_width")
        petal_length = request.form.get("petal_length")
        petal_width = request.form.get("petal_width")
        n_neighbors = request.form.get("n_neighbors")
        predict_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        preds = model.predict(predict_data)
        if preds == [0]:
            preds = "Setosa"
        elif preds == [1]:
            preds = "Versicolor"
        else:
            preds = "Virginica"

    return render_template('home.html', preds = preds)