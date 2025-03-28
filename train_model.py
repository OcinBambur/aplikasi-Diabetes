import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pickle

# Memuat dataset
data = pd.read_csv('diabetes.csv')

# Pisahkan fitur dan target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Bagi data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Simpan model ke file menggunakan pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model Naive Bayes telah dilatih dan disimpan sebagai model.pkl")