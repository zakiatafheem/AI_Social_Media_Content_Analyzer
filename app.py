import streamlit as st
from model_utils import analyze_text

# Config
st.set_page_config(page_title="AI Social Analyzer", layout="wide")
st.title("📱 AI Social Media Content Analyzer")

# Input
text = st.text_area("Enter Social Media Content")

# Analyze
if st.button("Analyze 🚀"):

    if not text.strip():
        st.warning("Enter some text")

    else:
        with st.spinner("Analyzing..."):
            result = analyze_text(text)

        st.subheader("📊 Results")
        st.write(result)