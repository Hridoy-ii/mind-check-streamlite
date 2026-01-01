import streamlit as st

import plotly.graph_objects as go

st.title("📊 Your Screening Results")

if "prediction" not in st.session_state:
    st.warning("Please complete the screening first.")
    st.page_link("pages/screening.py", label="← Go to Screening")
    st.stop()

pred = st.session_state.prediction
adhd, anxiety, dep = pred["adhd"], pred["anxiety"], pred["depression"]

# --- Clinical cutoff flags ---
adhd_pos = pred["asrs_sum"] >= 14
anxiety_pos = pred["gad_sum"] >= 8
dep_pos = pred["phq_sum"] >= 10

# --- Clinical cutoff warnings ---

# --- Visual: Radial gauges ---

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("ADHD Risk", f"{adhd:.4f}", 
              help="Model probability (not diagnostic)")
with col2:
    st.metric("Anxiety Risk", f"{anxiety:.4f}")
with col3:
    st.metric("Depression Risk", f"{dep:.4f}")



# --- Clinical Scores & Labels ---
st.subheader("🧮 Clinical Scores (Standard Cutoffs)")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("ASRS Sum", pred["asrs_sum"], 
              delta="≥14 → Positive" if adhd_pos else "Negative",
              delta_color="inverse")
with col2:
    st.metric("GAD-7 Total", pred["gad_sum"],
              delta="≥8 → Positive" if anxiety_pos else "Negative",
              delta_color="inverse")
with col3:
    st.metric("PHQ-9 Total", pred["phq_sum"],
              delta="≥10 → Positive" if dep_pos else "Negative",
              delta_color="inverse")

st.markdown("### 🏷️ Screening Labels (Clinical Cutoff Based)")
labels = []
labels.append(f"**ADHD**: {'✅ Positive' if adhd_pos else '❌ Negative'}")
labels.append(f"**Anxiety**: {'✅ Positive' if anxiety_pos else '❌ Negative'}")
labels.append(f"**Depression**: {'✅ Positive' if dep_pos else '❌ Negative'}")
st.markdown(" | ".join(labels))

# --- Mismatch warnings ---
mismatches = []
if anxiety_pos == False and anxiety > 0.5:
    mismatches.append("**Anxiety**: Model predicts high risk, but clinical score is below threshold")
if dep_pos == False and dep > 0.5:
    mismatches.append("**Depression**: Model predicts high risk, but clinical score is below threshold")

if mismatches:
    st.warning("⚠️ **Prediction Mismatch Detected**:\n\n" + "\n\n".join(mismatches) + "\n\n✅ **Trust your clinical scores** — they align with evidence-based guidelines.")

# --- Guidance ---
st.subheader("🧠 What This Means")
if not (adhd_pos or anxiety_pos or dep_pos):
    st.success("✨ Your responses suggest **low likelihood** of clinically significant symptoms. Keep nurturing your mental wellness!")
elif adhd_pos or anxiety_pos or dep_pos:
    st.warning("🔶 Your responses suggest **possible symptoms** above screening thresholds. Consider discussing with a counselor or healthcare provider.")

# --- Resources ---
st.markdown("### 🆘 Need Support?")
st.markdown("""
- **Find a Helpline**: [DSS Govt](https://dss.govt.bd)  
- **Crisis Hot Line**: Vent by Mindspace to 09678678778  
- **Kan Pete Roi**: 09612-119911
""")

st.divider()
st.caption("🔒 All processing happens locally. No data is saved or transmitted.")