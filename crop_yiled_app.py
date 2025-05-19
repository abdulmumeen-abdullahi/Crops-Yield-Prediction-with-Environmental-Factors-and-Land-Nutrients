import streamlit as st
import pickle
import numpy as np
import os
import gdown

st.set_page_config(page_title="Smart Farming AI System", layout="centered")
st.title("Crop Yield Prediction")

# Google Drive file ID
file_id = "1lDIpOAM4jLx7wbnBlB9360z98twaprvG"
model_url = f"https://drive.google.com/uc?id={file_id}"
model_path = "yield_best_random_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(model_path):
        with st.spinner("Downloading model..."):
            gdown.download(model_url, model_path, quiet=False)
    with open(model_path, "rb") as model_file:
        return pickle.load(model_file)

try:
    model = load_model()
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# Crop type and soil type options
crop_type = st.selectbox("Crop Type", ["Corn", "Potato", "Rice", "Sugarcane", "Wheat"])
soil_type = st.selectbox("Soil Type", ["Clay", "Loamy", "Peaty", "Saline", "Sandy"])

# Numeric inputs
soil_ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
temperature = st.slider("Temperature (°C)", 10, 40, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 100, 15)
n = st.number_input("Nitrogen (N)", min_value=0, value=60)
p = st.number_input("Phosphorus (P)", min_value=0, value=45)
k = st.number_input("Potassium (K)", min_value=0, value=31)
soil_quality = st.number_input("Soil Quality", min_value=0, max_value=100, value=50)

# Encode categorical variables
crop_type_encoded = {"Corn": 0, "Potato": 1, "Rice": 2, "Sugarcane": 3, "Wheat": 4}[crop_type]
soil_type_encoded = {"Clay": 0, "Loamy": 1, "Peaty": 2, "Saline": 3, "Sandy": 4}[soil_type]

input_data = np.array([[crop_type_encoded, soil_type_encoded, soil_ph, temperature, humidity,
                        wind_speed, n, p, k, soil_quality]])

if st.button("Predict Yield"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Crop Yield: {prediction[0]:.2f} tons/ha")
