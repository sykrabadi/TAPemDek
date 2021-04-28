from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Knn_Predict:
    def __init__(self, n_neighbors):
        self.iris = load_iris()
        self.X = self.iris.data
        self.Y = self.iris.target
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors)

    def train_and_test(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.4, random_state=42)
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test

    def fit(self):
        self.model = self.model.fit(self.X_train, self.Y_train)

    def predict(self, predict_data):
        preds = self.model.predict(predict_data)
        self.pred_species = [self.iris.target_names[p] for p in preds]
        self.accuracy_score = accuracy_score(self.Y_test, self.model.predict(self.X_test))
        return self.pred_species,self.accuracy_score