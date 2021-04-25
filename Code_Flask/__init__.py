from flask import Flask, request, render_template, url_for
from Code_Flask.ml_model.Ml_Model import Knn_Predict
import pickle
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = '026c4ba5ad18bcc7b243b4d9'
model = joblib.load('Code_Flask/iris_classifier_knn.joblib')
@app.route('/', methods=["GET","POST"])
def home():
    preds = ""
    global model
    if request.method == "POST":
        sepal_length = float(request.form.get("sepal_length"))
        sepal_width = float(request.form.get("sepal_width"))
        petal_length = float(request.form.get("petal_length"))
        petal_width = float(request.form.get("petal_width"))
        n_neighbors = int(request.form.get("n_neighbors"))
        predict_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        
        model = Knn_Predict(n_neighbors = n_neighbors)
        model.train_and_test()
        model.fit()
        preds = model.predict(predict_data)

    return render_template('home.html', preds = preds)