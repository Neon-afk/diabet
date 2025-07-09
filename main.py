import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Memuat model yang telah disimpan menggunakan pickle
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Judul aplikasi
st.title("Prediksi Risiko Diabetes")

# Input form untuk data pengguna
age = st.slider("Usia", 18, 100, 30)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
glucose_level = st.slider("Tingkat Glukosa", 50, 250, 100)
physical_activity_level = st.selectbox("Tingkat Aktivitas Fisik", ['low', 'moderate', 'high'])
family_history = st.selectbox("Riwayat Keluarga Diabetes", [0, 1])
smoker = st.selectbox("Apakah Anda Seorang Perokok?", [0, 1])

# Encode 'physical_activity_level' menjadi nilai numerik
label_encoder = {'low': 0, 'moderate': 1, 'high': 2}
physical_activity_level_encoded = label_encoder.get(physical_activity_level)  # Gunakan .get() untuk mendapatkan nilai

# Membuat DataFrame dari input yang diberikan
input_data = pd.DataFrame([[age, bmi, glucose_level, physical_activity_level_encoded, family_history, smoker]],
                     columns=['age', 'bmi', 'glucose_level', 'physical_activity_level', 'family_history', 'smoker'])

# Menampilkan data yang dimasukkan oleh pengguna
st.write("Data yang dimasukkan:")
st.write(input_data)

# Prediksi menggunakan model
prediction = model.predict(input_data)

# Menampilkan hasil prediksi
if prediction == 0:
    st.write("**Hasil Prediksi**: Tidak berisiko terkena diabetes.")
else:
    st.write("**Hasil Prediksi**: Berisiko terkena diabetes.")
