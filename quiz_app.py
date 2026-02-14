import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—the automatic nonverbal signals that run with speech.")
    
    # Simulator Buttons
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Forward movement indicates high interest and openness.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Crossed arms signal defensiveness or barriers.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower social stature and vulnerability.")
    
    st.subheader("Proxemics: Social Distance Ruler")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Professional/Peer interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Formal speaking/Strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # 10 Detailed Questions with Mixed Answers (A and B)
    qs = [
        ("What allowed observers to identify sex and emotion in 'point-light' studies?", ["Static dot patterns", "The patterns of movement"], "The patterns of movement", "Motion allows the brain to decode identity and emotion."),
        ("What does the term 'tie-signs' refer
