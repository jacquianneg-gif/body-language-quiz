import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    
    # Professional Header
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    # SECTION 1: THE SIMULATOR
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—the automatic nonverbal signals that run simultaneously with spoken words.")
    
    st.subheader("Facial Literacy Training")
    st.caption("INSTRUCTIONS: Click an emotion to see the involuntary muscle movements associated with 'muscle reading'.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth and high receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Narrowed lips and lowered brow. Signals resistance or perceived threat.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
    
    st.subheader("Postural Positioning")
    st.caption("INSTRUCTIONS: Select a posture to observe how positioning communicates interest or status.")
    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates high interest and openness.")
    with p2:
        if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a barrier, signaling defensiveness.")
    with p3:
        if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature and vulnerability.")
    
    st.subheader("Proxemics: The Social Distance Ruler")
    st.caption("INSTRUCTIONS: Use the slider to explore how trust and status dictate physical space.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds and close relationships.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard for peer-to-peer and professional interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    # SECTION 2: THE ASSESSMENT
    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    st.markdown("#### Visualizing the Research: The Point-Light Experiment")
    st.caption("Observers can instantly identify sex and mood from moving dots alone—proof of our 'Parallel Track' perception.")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    qs = [
        ("What allowed observers to identify sex and emotion in 'point-light' studies?", ["The color of dots", "The patterns of movement"], "The patterns of movement", "Static dots appear meaningless. Movement allows the brain to decode identity."),
        ("What are 'tie-signs'?", ["Formal dress codes", "Cues that signal a specific bond"], "Cues that signal a specific bond", "Tie-signs signal a nonverbal relationship to observers."),
        ("Social success in children is most linked to which skill?", ["Reading facial muscle movements",
