import streamlit as st
import pandas as pd
import pickle

# Load pipeline model
with open("023_Capstone Modul 3_Ikhsan.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📋 Prediksi Klaim Asuransi Perjalanan")
st.markdown("Masukkan data berikut untuk memprediksi apakah klaim akan diterima atau ditolak.")

# Form input
with st.form("input_form"):
    age = st.slider("Usia Pemegang Polis", 18, 100, 30)
    annual_income = st.number_input("Pendapatan Tahunan (USD)", min_value=0, value=50000)
    
    travel_frequency = st.selectbox("Frekuensi Perjalanan", ["Low", "Medium", "High"])
    destination_risk = st.selectbox("Risiko Destinasi", ["Low", "Medium", "High"])
    travel_type = st.selectbox("Tipe Perjalanan", ["Business", "Personal"])
    chronic_disease = st.radio("Memiliki Penyakit Kronis?", ["Tidak", "Ya"])

    agency = st.selectbox("Agency", ["Agency A", "Agency B", "Agency C"])
    product_name = st.selectbox("Product Name", ["Product 1", "Product 2", "Product 3"])
    destination = st.selectbox("Destination", ["USA", "Europe", "Asia"])
    agency_type = st.selectbox("Agency Type", ["Airlines", "Travel Agency"])
    claim = st.selectbox("Pernah Klaim Sebelumnya?", ["Yes", "No"])

    submitted = st.form_submit_button("🔍 Prediksi")

# Manual encoding ONLY untuk fitur yang tidak di-handle oleh pipeline
def preprocess_input():
    travel_freq_map = {"Low": 0, "Medium": 1, "High": 2}
    risk_map = {"Low": 0, "Medium": 1, "High": 2}
    travel_type_map = {"Business": 0, "Personal": 1}
    disease_map = {"Tidak": 0, "Ya": 1}
    agency_map = {"Agency A": 0, "Agency B": 1, "Agency C": 2}
    product_map = {"Product 1": 0, "Product 2": 1, "Product 3": 2}
    destination_map = {"USA": 0, "Europe": 1, "Asia": 2}
    agency_type_map = {"Airlines": 0, "Travel Agency": 1}
    claim_map = {"Yes": 1, "No": 0}

    data = {
        "Age": age,
        "AnnualIncome": annual_income,
        "TravelFrequency": travel_freq_map[travel_frequency],
        "DestinationRisk": risk_map[destination_risk],
        "TravelType": travel_type_map[travel_type],
        "ChronicDisease": disease_map[chronic_disease],
        "Agency": agency_map[agency],
        "Product Name": product_map[product_name],
        "Destination": destination_map[destination],
        "Agency Type": agency_type_map[agency_type],
        "Claim": claim_map[claim]
    }
    return pd.DataFrame([data])

# Prediksi
if submitted:
    input_df = preprocess_input()
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("✅ Klaim DITERIMA!")
    else:
        st.error("❌ Klaim DITOLAK.")
