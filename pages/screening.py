import streamlit as st

import tensorflow as tf
import numpy as np

# --- Load model (cached) ---
@st.cache_resource
def load_model():
    try:
        return tf.keras.models.load_model("model/adhd_mtl_symptom_only_model.keras", compile=False)
    except Exception as e:
        st.error(f"❌ Model failed to load: {e}")
        st.stop()

model = load_model()
st.title("🩺 Mental Health Screening")
st.caption("Answer all questions using standard clinical scales")

# Custom CSS for larger fonts
st.markdown("""
<style>
    .question-text {
        font-size: 18px !important;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    .stRadio > label {
        font-size: 16px !important;
    }
    h3 {
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Response mappings ---
ASRS_OPTIONS = [
    "Never (0)",
    "Rarely (1)",
    "Sometimes (2)",
    "Often (3)",
    "Very Often (4)"
]
GAD_PHQ_OPTIONS = [
    "Not at all (0)",
    "Several days (1)",
    "More than half the days (2)",
    "Nearly every day (3)"
]

# --- Clinical Questions ---
ASRS_QUESTIONS = [
    "How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?",
    "How often do you have difficulty getting things in order when you have to do a task that requires organization?",
    "How often do you have problems remembering appointments or obligations?",
    "When you have a task that requires a lot of concentration, how often do you avoid or delay getting started?",
    "How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?",
    "How often do you feel overly active and compelled to do things, like you were driven by a motor?"
]

GAD_QUESTIONS = [
    "Feeling nervous, anxious or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it is hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen"
]

PHQ_QUESTIONS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual",
    "Thoughts that you would be better off dead or of hurting yourself in some way"
]

# --- Form ---
with st.form("screening_form"):
    st.subheader("📋 ASRS-v1.1 Screener (ADHD)")
    st.markdown("_How often have you experienced these in the past 6 months?_")
    asrs_responses = []
    for i in range(6):
        resp = st.radio(
            f"Q{i+1}: {ASRS_QUESTIONS[i]}", 
            ASRS_OPTIONS, 
            horizontal=True,
            key=f"asrs_{i}"
        )
        score = int(resp.split("(")[1].replace(")", ""))
        asrs_responses.append(score)

    st.subheader("😰 GAD-7 (Anxiety)")
    st.markdown("_Over the last 2 weeks, how often have you been bothered by...?_")
    gad_responses = []
    for i in range(7):
        resp = st.radio(
            f"Q{i+1}: {GAD_QUESTIONS[i]}",
            GAD_PHQ_OPTIONS,
            horizontal=True,
            key=f"gad_{i}"
        )
        score = int(resp.split("(")[1].replace(")", ""))
        gad_responses.append(score)

    st.subheader("😔 PHQ-9 (Depression)")
    st.markdown("_Over the last 2 weeks, how often have you been bothered by...?_")
    phq_responses = []
    for i in range(9):
        resp = st.radio(
            f"Q{i+1}: {PHQ_QUESTIONS[i]}",
            GAD_PHQ_OPTIONS,
            horizontal=True,
            key=f"phq_{i}"
        )
        score = int(resp.split("(")[1].replace(")", ""))
        phq_responses.append(score)

    submitted = st.form_submit_button("🔍 Analyze My Risk", type="primary")

# --- Prediction ---
if submitted:
    # Combine in exact training order: ASRS (6) + GAD (7) + PHQ (9)
    feature_vector = asrs_responses + gad_responses + phq_responses  # len=22
    X = np.array([feature_vector])

    # Predict (no scaling — raw ints)
    try:
        preds = model.predict(X, verbose=0)
        adhd_prob = float(preds[0][0])
        anxiety_prob = float(preds[1][0])
        dep_prob = float(preds[2][0])
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.stop()

    # Save to session state
    st.session_state.prediction = {
        "adhd": adhd_prob,
        "anxiety": anxiety_prob,
        "depression": dep_prob,
        "asrs_sum": sum(asrs_responses),
        "gad_sum": sum(gad_responses),
        "phq_sum": sum(phq_responses),
        "features": feature_vector
    }

    st.success("✅ Analysis complete!")
    st.page_link("pages/results.py", label="➡️ View Detailed Results", icon="📊")