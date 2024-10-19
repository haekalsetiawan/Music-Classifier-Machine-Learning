import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Pisahkan fitur dan label
    X = df.drop('genre', axis=1)  # Sesuaikan nama kolom label jika diperlukan
    y = df['genre']

    # Pisahkan kolom numerik dan kategorikal
    numeric_features = X.select_dtypes(include=['float64', 'int64'])
    categorical_features = X.select_dtypes(include=['object'])

    # Normalisasi data numerik
    scaler = StandardScaler()
    numeric_features = pd.DataFrame(scaler.fit_transform(numeric_features), columns=numeric_features.columns)

    # Tangani fitur kategorikal dengan LabelEncoder
    label_encoder = LabelEncoder()
    for column in categorical_features.columns:
        categorical_features[column] = label_encoder.fit_transform(categorical_features[column])

    # Gabungkan kembali data numerik dan kategorikal
    X_processed = pd.concat([numeric_features, categorical_features], axis=1)

    return X_processed, y

if __name__ == "__main__":
    X, y = load_and_preprocess_data('songs_normalize.csv')
    print(X.head())
