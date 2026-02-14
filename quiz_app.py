import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic signals that run with speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Forward torso movement indicates high interest.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Crossed arms signal defensiveness or a barrier.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower social stature and vulnerability.")
    
    st.subheader("The Social Distance Ruler")
    st.caption("How trust and status dictate physical space ('Tie-Signs').")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard peer/professional space.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Used for strangers or formal speaking.")

    st.divider()
    st.header("II. ASSESSMENT")
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # 10 Detailed Questions with Shuffled Answer Keys (A and B)
    qs = [
        ("Identify sex/emotion in 'point-light' studies via?", ["Movement patterns", "Static dot patterns"], "Movement patterns",
