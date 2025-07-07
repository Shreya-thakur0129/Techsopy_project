import streamlit as st
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("models/risk_model.pkl")

st.set_page_config(page_title="Insurance Underwriting System", layout="centered", page_icon="📋")

# 🌟 Updated UI Style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #eaf0f6;
        color: #1c1c1c;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-container {
        background-color: #ffffff;
        padding: 2rem 2rem;
        border-radius: 16px;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
    }

    h1 {
        text-align: center;
        font-weight: 600;
        color: #2d3e50;
        margin-bottom: 1.5rem;
    }

    .stButton > button {
        background-color: #0078D7;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.4rem;
        border: none;
        border-radius: 8px;
        transition: background 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #005a9e;
        transform: scale(1.02);
    }

    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox div {
        background-color: #f4f7fa !important;
        border: 1px solid #cfd8e3;
        color: #1a1a1a !important;
        border-radius: 10px;
        padding: 0.4rem;
    }

    .stAlert {
        border-radius: 10px !important;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("📋 Insurance Underwriting System")

employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])
annual_income = st.number_input("Annual Income (₹)", min_value=0)
num_defaults = st.number_input("Number of Previous Defaults", min_value=0)
age = st.number_input("Age", min_value=0)

if st.button("📊 Evaluate Application"):
    emp_status_encoded = 1 if employment_status == "Employed" else 0
    input_data = [[emp_status_encoded, annual_income, num_defaults, age]]

    prediction = model.predict(input_data)[0]
    st.write("🔍 Raw model prediction:", prediction)

    if prediction == 1:
        decision = "❌ Rejected"
        reason = "⚠️ The system flagged high risk due to income, defaults, age, or employment status."
        st.error(f"📌 Underwriting Decision: {decision}")
        st.info(reason)

    elif prediction == 0 and num_defaults == 0 and annual_income > 60000:
        decision = "✅ Accepted"
        reason = "🎉 Clean record and sufficient income. Eligible for approval."
        st.success(f"📌 Underwriting Decision: {decision}")
        st.info(reason)

    else:
        decision = "❓ Needs More Information"
        reason = "ℹ️ Profile needs manual review due to borderline eligibility."
        st.warning(f"📌 Underwriting Decision: {decision}")
        st.info(reason)

st.markdown('</div>', unsafe_allow_html=True)
