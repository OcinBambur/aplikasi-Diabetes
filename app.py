import streamlit as st
import pickle

# Memuat model yang sudah dilatih
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Antarmuka Streamlit
st.title("Aplikasi Prediksi Diabetes dengan Naive Bayes")
st.write("Masukkan nilai untuk memprediksi diabetes:")

# Input pengguna
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=100)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=846, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=25.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.078, max_value=2.42, value=0.3725)
age = st.number_input("Age", min_value=21, max_value=81, value=25)

# Tombol prediksi
if st.button("Prediksi"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("Hasil Prediksi: ANDA POSITIF DIABETES")
    else:
        st.success("Hasil Prediksi: ANDA NEGATIF DIABETES")