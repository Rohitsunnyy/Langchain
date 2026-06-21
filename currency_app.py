import streamlit as st
import requests
import base64

st.set_page_config(page_title="💰 Currency Converter", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Cormorant+Garamond:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cormorant Garamond', serif;
    }

    .stApp {
        background-image: url("https://images.unsplash.com/photo-1559526324-593bc073d938?w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.65);
        z-index: 0;
    }

    .block-container {
        position: relative;
        z-index: 1;
    }

    h1 {
        text-align: center;
        font-family: 'Playfair Display', serif !important;
        font-size: 3.2rem !important;
        color: #d4af37 !important;
        letter-spacing: 3px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #c9b99a;
        font-size: 1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }

    .card {
        background: rgba(20, 15, 5, 0.75);
        border: 1px solid #d4af37;
        border-radius: 16px;
        padding: 30px;
        backdrop-filter: blur(10px);
    }

    .result-box {
        background: linear-gradient(135deg, rgba(212,175,55,0.2), rgba(180,140,30,0.3));
        border: 1px solid #d4af37;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        backdrop-filter: blur(10px);
    }

    .result-box h2 {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        color: #d4af37;
        margin: 0;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    .result-box p {
        color: #c9b99a;
        margin: 8px 0 0 0;
        font-size: 1rem;
        letter-spacing: 1px;
    }

    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {
        color: #d4af37 !important;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 0.85rem !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d4af37, #a07d1c);
        color: #1a1200;
        border: none;
        padding: 15px;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: 700;
        cursor: pointer;
        margin-top: 10px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-family: 'Playfair Display', serif;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #f0cc55, #c09830);
    }

    div[data-baseweb="select"] {
        background-color: rgba(212,175,55,0.08) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(212,175,55,0.3) !important;
    }

    input {
        color: #d4af37 !important;
        background-color: rgba(212,175,55,0.08) !important;
    }

    .divider {
        border: none;
        border-top: 1px solid rgba(212,175,55,0.3);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>💰 Old Money Exchange</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">✦ Real-Time Currency Conversion ✦</p>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- Currencies ---
currencies = ["USD", "INR", "EUR", "GBP", "JPY", "AED", "CAD", "AUD", "CHF", "CNY", "MXN", "SGD", "HKD", "KRW"]

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", currencies, index=0)
with col2:
    to_currency = st.selectbox("To Currency", currencies, index=1)

amount = st.number_input("Enter Amount", min_value=0.0, value=100.0, step=10.0)

# --- Convert Button ---
if st.button("✦ Convert ✦"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url).json()

    if "rates" in response:
        rate = response["rates"][to_currency]
        converted = amount * rate

        st.markdown(f"""
            <div class="result-box">
                <h2>{converted:,.2f} {to_currency}</h2>
                <p>✦ {amount:,.2f} {from_currency} · Rate: {rate:.4f} ✦</p>
            </div>
        """, unsafe_allow_html=True)

        st.snow()
    else:
        st.error("Could not fetch rates. Please try again.")