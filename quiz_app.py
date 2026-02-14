import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    
    # Professional Header
    st.markdown("<h1 style='text-align: center;'>The Professional Body Language Lab</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Bridging Nonverbal Theory and Social Literacy</h4>", unsafe_allow_html=True)
    
    # SECTION 1: THE SIMULATOR
    st.divider()
    st.subheader("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—the automatic nonverbal signals that run simultaneously with spoken words.")
    
    st.markdown("### Facial Literacy Training")
    st.caption("INSTRUCTIONS: Click an emotion to see the involuntary muscle movements associated with 'muscle reading'.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth and high receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Narrowed lips and lowered brow. Signals resistance or perceived threat.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
    
    st.markdown("### Postural Positioning")
    st.caption("INSTRUCTIONS: Select a posture to observe how positioning communicates interest or status.")
    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates high interest and openness.")
    with p2:
        if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a barrier, signaling defensiveness.")
    with p3:
        if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature and vulnerability.")
    
    st.markdown("### Proxemics: The Social Distance Ruler")
    st.caption("INSTRUCTIONS: Use the slider to explore how trust and status dictate physical space.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Professional/Peer interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Formal speaking/Strangers.")

    # SECTION 2: THE ASSESSMENT
    st.divider()
    st.subheader("II. COMPREHENSIVE ASSESSMENT")
