import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    
    # --- ADDED STUDENT INSTRUCTIONS ---
    with st.expander("📋 STUDENT INSTRUCTIONS - READ FIRST", expanded=True):
        st.write("""
        1. **Explore Behavioral Cues:** Click each of the icon buttons (😊, 🙇‍♂️, 😠, etc.) below to reveal what specific body language signals convey about a person's state.
        2. **Test Social Distance:** Use the **Distance Ruler slider** further down to adjust physical space. Observe how different distances (in feet) change the classification of the 'Social Zone.'
        3. **Complete Assessment:** Once you have explored the simulator, move to Section II to test your knowledge.
        """)
    # ----------------------------------

    st.info("Study the 'Parallel Track'—automatic nonverbal signals that run with speech.")
    
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

    # Shuffled 10 detailed questions
    qs = [
        ("What allowed observers to identify sex and emotion in 'point-light' studies?", 
         ["The patterns of movement", "Static dot patterns"], 
         "The patterns of movement", "Motion allows the brain to decode identity."),
        ("What does the term 'tie-signs' refer to in nonverbal research?", 
         ["Formal organizational dress codes", "Cues that signal a specific bond"], 
         "Cues that signal a specific bond", "Tie-signs signal a relationship to observers."),
        ("Social success and popularity in children is most linked to...", 
         ["Reading facial muscle movements", "Memorizing academic facts"], 
         "Reading facial muscle movements", "Popularity is linked to 'muscle reading'."),
        ("When a person leans forward, what is the most likely signal?", 
         ["Boredom or fatigue", "Receptivity and interest"], 
         "Receptivity and interest", "Leaning forward shows interest and openness."),
        ("Large physical distance typically signals what about social status?", 
         ["Lower social stature", "High authority and power"], 
         "Lower social stature", "Distance avoids appearing as a threat."),
        ("What exactly is the 'parallel track' of communication?", 
         ["Nonverbal cues running with speech", "Speaking two languages at once"], 
         "Nonverbal cues running with speech", "It runs automatically alongside
