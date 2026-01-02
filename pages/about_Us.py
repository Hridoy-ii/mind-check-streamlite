import streamlit as st

st.title("👥 About This Tool")

st.markdown("""
### 📋 What This Is
A research-informed screening aid built using:
- **ASRS-v1.1** (6-item WHO screener for ADHD)
- **GAD-7** (7-item anxiety severity scale)
- **PHQ-9** (9-item depression severity scale)

### 🧠 How It Works
1. You answer **22 standard clinical questions**
2. Your responses are scored per clinical guidelines:
   - ASRS: 0–4 per item (sum 0–24; ≥14 = screen positive)
   - GAD-7: 0–3 per item (sum 0–21; ≥8 = screen positive)
   - PHQ-9: 0–3 per item (sum 0–27; ≥10 = screen positive)
3. A **multitask neural network** (Keras/TensorFlow) estimates probabilistic risk for each condition.

### ⚙️ Technical Details
- **Input**: 22 raw symptom scores (no demographic/lifestyle features)
- **Model**: Shared hidden layers + task-specific heads
- **Training**: 5-fold stratified cross-validation on survey data
- **Output**: Probabilities (0–1) for ADHD, Anxiety, Depression

### 🛡️ Privacy & Ethics
- ✅ No data collection
- ✅ No tracking or cookies
- ✅ Runs locally in your browser (if using stlite) or on your server

### 📚 References
- Kessler, R. C., et al. (2005). *ASRS-v1.1*. World Health Organization.  
- Spitzer, R. L., et al. (2006). *GAD-7*. Archives of Internal Medicine.  
- Kroenke, K., et al. (2001). *PHQ-9*. JAMA.

> 🙏 Developed to promote early awareness — not replace professional care.
""")

st.markdown("""
### 👨‍💻 Project Team

**Nur Mohammad Hridoy**: [hridoy15-5952@diu.edu.bd](mailto:hridoy15-5952@diu.edu.bd) \n
**Kanij Fatema**: [fatema15-4884@diu.edu.bd](mailto:fatema15-4884@diu.edu.bd)
""")