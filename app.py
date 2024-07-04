import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'gradient_boosting_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define the prediction function
def predict(input_data):
    input_data = np.array(input_data).reshape(1, -1)  # Ensure the input data is in the correct shape
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app layout
st.title("Drinker Prediction")

# Collect inputs for the selected features
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 18, 100, 25)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
waistline = st.number_input("Waistline (cm)", min_value=50, max_value=150, value=80)
HDL_chole = st.number_input("HDL Cholesterol (mg/dL)", min_value=0, max_value=100, value=50)
LDL_chole = st.number_input("LDL Cholesterol (mg/dL)", min_value=0, max_value=200, value=100)
hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0, max_value=20, value=14)
SGOT_ALT = st.number_input("SGOT/ALT (U/L)", min_value=0, max_value=200, value=30)
gamma_GTP = st.number_input("Gamma-GTP (U/L)", min_value=0, max_value=200, value=30)
SMK_stat_type_cd = st.selectbox("Smoking Status", ["Non-Smoker", "Ex-Smoker", "Current Smoker"])

# Convert categorical inputs to the required format
sex = 0 if sex == "Male" else 1
SMK_stat_type_cd = ["Non-Smoker", "Ex-Smoker", "Current Smoker"].index(SMK_stat_type_cd)

if st.button("Predict"):
    input_data = [sex, age, height, waistline, HDL_chole, LDL_chole, hemoglobin, SGOT_ALT, gamma_GTP, SMK_stat_type_cd]
    prediction = predict(input_data)
    st.write("Prediction:", "Drinker" if prediction == 1 else "Non-Drinker")
