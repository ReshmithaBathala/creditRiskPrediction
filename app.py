import streamlit as st
# import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")  # Save your logistic regression model first using joblib

st.title("Credit Risk Prediction App")

# Collect input data
age = st.slider("Age", 18, 75, 35)
job = st.selectbox("Job (0=Unemployed, 1=Unskilled, 2=Skilled, 3=Highly Skilled)", [0, 1, 2, 3])
credit_amount = st.number_input("Credit Amount", min_value=0, value=3000)
duration = st.number_input("Duration (months)", min_value=1, value=24)

sex_male = st.selectbox("Sex", ["Male", "Female"]) == "Male"
housing = st.selectbox("Housing", ["own", "free", "rent"])
saving_acc = st.selectbox("Saving Accounts", ["little", "moderate", "quite rich", "rich"])
checking_acc = st.selectbox("Checking Accounts", ["little", "moderate", "rich"])
purpose = st.selectbox("Purpose", [
    "car", "domestic appliances", "education", "furniture/equipment",
    "radio/TV", "repairs", "vacation/others"
])

# Prepare input dict based on UI
input_data = {
    'Age': age,
    'Job': job,
    'Credit amount': credit_amount,
    'Duration': duration,
    'Sex_male': int(sex_male),
    'Housing_own': int(housing == "own"),
    'Housing_rent': int(housing == "rent"),
    'Saving accounts_moderate': int(saving_acc == "moderate"),
    'Saving accounts_quite rich': int(saving_acc == "quite rich"),
    'Saving accounts_rich': int(saving_acc == "rich"),
    'Checking account_moderate': int(checking_acc == "moderate"),
    'Checking account_rich': int(checking_acc == "rich"),
    'Purpose_car': int(purpose == "car"),
    'Purpose_domestic appliances': int(purpose == "domestic appliances"),
    'Purpose_education': int(purpose == "education"),
    'Purpose_furniture/equipment': int(purpose == "furniture/equipment"),
    'Purpose_radio/TV': int(purpose == "radio/TV"),
    'Purpose_repairs': int(purpose == "repairs"),
    'Purpose_vacation/others': int(purpose == "vacation/others"),
}

# Convert to DataFrame
sample_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict Credit Risk"):
    prediction = model.predict(sample_df)
    result = "High" if prediction[0] == 1 else "Low"
    st.success(f"Predicted Credit Risk: {result}")
