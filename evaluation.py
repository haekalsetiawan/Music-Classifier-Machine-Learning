import joblib
from sklearn.metrics import classification_report
from preprocessing import load_and_preprocess_data

def evaluate_model():
    X, y = load_and_preprocess_data('songs_normalize.csv')
    model = joblib.load('trained_model.pkl')

    predictions = model.predict(X)
    report = classification_report(y, predictions, zero_division=0)
    print(report)

if __name__ == "__main__":
    evaluate_model()
