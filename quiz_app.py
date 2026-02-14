import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic nonverbal signals that run with speech.")
    
    st.subheader("Facial Literacy Training")
    st.caption("Click to see involuntary muscle movements associated with 'muscle reading'.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tight lips/lowered brow. Signals resistance.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows/widened eyes. Signals stress.")
    
    st.subheader("Postural Positioning")
    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Indicates high interest and openness.")
    with p2:
        if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms signal defensiveness.")
    with p3:
        if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Signals lower social stature.")
    
    st.subheader("Proxemics: The Social Distance Ruler")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. Close trust/High status.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Professional interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Strangers/Formal speaking.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    st.write("#### Research Focus: The Point-Light Experiment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    qs = [
        ("What allowed observers to identify sex in 'point-light' studies?", ["Color", "Movement"], "Movement", "Movement allows the brain to decode identity."),
        ("What are 'tie-signs'?", ["Dress codes", "Bond cues"], "Bond cues", "Tie-signs signal a specific relationship to observers."),
        ("Social success in children is linked to...", ["Muscle reading", "Math"], "Muscle reading", "Popularity is linked to reading facial cues."),
        ("Leaning forward signals...", ["Boredom", "Interest"], "Interest", "Leaning in shows openness and receptivity."),
        ("Large distance signals what status
