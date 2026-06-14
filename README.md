**Problem Statement**

Build a Loan Approval Prediction System that predicts whether a loan application will be approved or rejected based on an applicant's financial and personal information.

**Dataset Details**

The Loan Approval Dataset contains applicant details, financial information, asset values, and credit scores used to determine loan eligibility.

**Features**

Number of Dependents
Education Status
Self-Employment Status
Annual Income
Loan Amount
Loan Term
CIBIL Score
Residential Assets Value
Commercial Assets Value
Luxury Assets Value
Bank Assets Value

**Target**

Loan Status (Approved / Rejected)

**Approach**

Load the trained machine learning model and scaler using Pickle.
Collect user inputs through a Streamlit web interface.
Encode categorical variables (Education and Self-Employment).
Scale input features using the saved scaler.
Use the trained model to predict loan approval status.
Display the prediction result in the web application.

**Results**
The application successfully predicts loan approval decisions.
Input data is preprocessed using the same scaler used during model training.
Users receive instant feedback on whether their loan is likely to be approved or rejected.
The Streamlit interface provides an interactive and user-friendly experience.

**Conclusion**

This project demonstrates how a trained machine learning model can be deployed as a web application using Streamlit. By analyzing applicant information and financial factors, the system provides quick and automated loan approval predictions, supporting decision-making in the lending process.
