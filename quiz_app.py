import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Behavioral Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic nonverbal signals that run simultaneously with spoken words.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth and social success.")
        if st.button("🙇‍♂️ Lean"): st.info("LEANING: Forward movement indicates high interest and receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tightened lips and lowered brow. Signals resistance or threat.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLDING: Crossed arms create a barrier, signaling defensiveness.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
        if st.button("👤 Hunch"): st.warning("HUNCHING: Signals lower social stature and vulnerability.")
    
    st.subheader("The Social Distance Ruler")
    st.caption("How trust and status dictate the physical space between people (known as 'Tie-Signs').")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds and close relationships.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard for peer-to-peer and professional interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st
