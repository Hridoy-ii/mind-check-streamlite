import streamlit as st

st.set_page_config(
    page_title="Mental Health Screening",
    layout="centered"
)

st.title("Mental Health Self-Screening Tool")
st.markdown("""
A confidential, evidence-based screener for:

- **ADHD** (ASRS-v1.1)
- **Anxiety** (GAD-7)
- **Depression** (PHQ-9)

Powered by a machine learning model trained on clinical responses.

> **Disclaimer**:  
> This tool does **not** provide medical advice or diagnosis.  
> Results are for self-reflection and awareness only.  
> Always consult a qualified mental health professional.
""")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/screening.py", label="Start Screening (5 min)")
with col2:
    st.page_link("pages/about_Us.py", label="How It Works")

st.image("utils/5792283.jpg", 
         caption="Your mental health matters.", use_column_width=True)
