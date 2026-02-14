import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    
    # --- I. BEHAVIORAL ANALYSIS SIMULATOR ---
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    
    # ADDED STUDENT INSTRUCTIONS
    st.info("""
    **📋 STUDENT INSTRUCTIONS:**
    1. **Reveal Cues:** Click the buttons in the columns below (😊, 🙇‍♂️, 😠, etc.) to learn what each specific body signal communicates.
    2. **Observe Proximity:** Use the **'Distance (feet)' slider** to test how physical space affects social interaction zones.
    3. **Test Knowledge:** Once you've explored, scroll down to Section II to begin your assessment.
    """)
    
    st.write("Study the 'Parallel Track'—automatic nonverbal signals that run with speech.")
    
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
    
    # ADDED SLIDER INSTRUCTIONS IN THE LABEL
    v = st.slider("Distance Ruler (Slide to change feet and observe the zone):", 1, 15, 5)
    
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Professional/Peer interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Formal speaking/Strangers.")

    st.divider()
    
    # --- II. COMPREHENSIVE ASSESSMENT ---
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Shuffled 10 detailed questions
