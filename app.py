import streamlit as st
import pickle
import string


from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS



# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Spam Detection",
    page_icon="📩",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS (Professional + Tight Layout)
# --------------------------------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        max-width: 650px;
        margin: auto;
    }
    h1 {
        font-size: 26px !important;
        color: #1f2937;
        font-weight: 600;
    }
    textarea {
        font-size: 14px !important;
    }
    .stButton button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        height: 42px;
    }
    .stButton button:hover {
        background-color: #1e40af;
    }
    .card {
        background-color: #f9fafb;
        padding: 1.2rem;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load Model & Vectorizer
# --------------------------------------------------
@st.cache_resource
def load_resources():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, tfidf = load_resources()

ps = PorterStemmer()

# --------------------------------------------------
# Text Processing
# --------------------------------------------------
def transform_text(text):
    text = text.lower()
    tokens = text.split()

    cleaned = [
        ps.stem(word)
        for word in tokens
        if word.isalnum() and word not in ENGLISH_STOP_WORDS
    ]

    return " ".join(cleaned)

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>Email / SMS Spam Detection</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#6b7280; font-size:14px;'>"
    "Machine Learning based message classification"
    "</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Input Card
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

text_input = st.text_area(
    "Message Content",
    height=120,
    placeholder="Paste email or SMS content here..."
)

predict = st.button("Analyze Message", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Prediction Output
# --------------------------------------------------
if predict:
    if not text_input.strip():
        st.warning("Please enter a message to analyze.")
    else:
        with st.spinner("Processing..."):
            processed_text = transform_text(text_input)
            vector_input = tfidf.transform([processed_text])
            result = model.predict(vector_input)[0]

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if result == 1:
            st.error("🚫 Spam Message Detected")
            st.write(
                "This message has characteristics commonly associated with **spam or phishing content**."
            )
        else:
            st.success("✅ Message is Not Spam")
            st.write(
                "This message appears to be **legitimate and safe**."
            )

        st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:12px; margin-top:20px;'>"
    "© 2026 Spam Detection System | Streamlit Deployment Ready"
    "</p>",
    unsafe_allow_html=True
)

