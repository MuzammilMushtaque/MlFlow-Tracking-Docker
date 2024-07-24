import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psutil

def log_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    mlflow.log_metric("cpu_percent", cpu_percent)
    mlflow.log_metric("memory_percent", memory_info.percent)

def train(n_estimators, max_depth):
    wine = fetch_openml(name='wine', version=1)
    X = wine.data
    y = wine.target.astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run() as run:
        print ('Code is starting under mlflow .......')
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        log_system_metrics()

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        mlflow.sklearn.log_model(model, "model")

        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)

        cm = confusion_matrix(y_test, predictions)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix')
        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")
        plt.close()
        print ('Code finished under mlflow***********')

if __name__ == "__main__":
    print ('Code Started')
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--max_depth", type=int, default=3)
    args = parser.parse_args()
    train(args.n_estimators, args.max_depth)
