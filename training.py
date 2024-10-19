import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocessing import load_and_preprocess_data

def train_model():
    X, y = load_and_preprocess_data('songs_normalize.csv')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'trained_model.pkl')

    print("Model training complete.")

if __name__ == "__main__":
    train_model()
