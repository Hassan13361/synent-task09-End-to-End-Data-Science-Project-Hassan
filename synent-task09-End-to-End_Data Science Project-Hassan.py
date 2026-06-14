import streamlit as st
import pickle
import numpy as np

# Load model + scaler
model = pickle.load(open("loan_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Loan Prediction App")

st.title("🏦 Loan Approval Prediction App")
st.write("Enter customer details below")

# Inputs
dependents = st.number_input("No of Dependents", min_value=0)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income = st.number_input("Income Annum")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
cibil = st.number_input("CIBIL Score")

res_assets = st.number_input("Residential Assets Value")
com_assets = st.number_input("Commercial Assets Value")
lux_assets = st.number_input("Luxury Assets Value")
bank_assets = st.number_input("Bank Assets Value")

# Encoding
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# Predict
if st.button("Predict Loan Status"):

    input_data = np.array([[dependents, education, self_employed,
                            income, loan_amount, loan_term,
                            cibil, res_assets, com_assets,
                            lux_assets, bank_assets]])

    # SCALE INPUT (MOST IMPORTANT FIX)
    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")