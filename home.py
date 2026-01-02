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
    if st.button("Start Screening (5 min)", use_container_width=True):
        st.switch_page("pages/screening.py")
with col2:
    st.markdown("<div style='display: flex; align-items: center; justify-content: flex-end; height: 100%;'><a href='pages/about_Us.py' style='text-decoration: none;'>How it works</a></div>", unsafe_allow_html=True)

st.image("utils/5792283.jpg", 
         caption="Your mental health matters.")
