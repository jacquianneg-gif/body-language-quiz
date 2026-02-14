import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()
    
    # --- SECTION I: SIMULATOR (CLICK-TO-REVEAL) ---
    st.header("I. Behavioral Analysis Simulator")
    st.write("Click 'Analyze' to reveal the professional interpretation of each signal.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("😊 JOY")
        if st.button("Analyze Joy"):
            st.success("ANALYSIS: True joy (Duchenne smile) involves involuntary "
                       "muscle contraction around the eyes.")
            
        st.subheader("🙇‍♂️ THE LEAN")
        if st.button("Analyze The Lean"):
            st.info("ANALYSIS: Leaning the torso forward reduces distance and "
                    "signals high interest and receptivity.")

    with col2:
        st.subheader("😠 RESISTANCE")
        if st.button("Analyze Resistance"):
            st.error("ANALYSIS: Compressed lips and a lowered brow often signal "
                     "internal disagreement or cognitive effort.")
            
        st.subheader("🙅‍♂️ BARRIERS")
        if st.button("Analyze Barriers"):
            st.error("ANALYSIS: Arms crossed across the chest acts as a barrier, "
                     "signaling defensiveness or self-protection.")

    with col3:
        st.subheader("😨 STRESS")
        if st.button("Analyze Stress"):
            st.warning("ANALYSIS: Widened eyes and raised brows increase visual "
                       "intake, signaling a person feels threatened.")
            
        st.subheader("👤 DIMINISHMENT")
        if st.button("Analyze Diminishment"):
            st.warning("ANALYSIS: Hunching shoulders (the 'turtle effect') is an "
                       "attempt to appear smaller and less threatening.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT (WITH FULL EXPLANATIONS) ---
    st.header("II. Comprehensive Assessment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "feedback" not in st.session_state: st.session_state.feedback = None

    # Quiz Database - formatted with multi-line strings to prevent truncation
    qs = [
        {
            "q": "In 'point-light' studies, what identifies sex and emotion?",
            "o": ["Patterns of movement", "Static dots"],
            "c": "Patterns of movement",
            "e": "The brain decodes identity and emotion through the rhythm "
                 "of motion, even without a visible body."
        },
        {
            "q": "What do 'tie-signs' refer to in social groups?",
            "o": ["Cues signaling a relationship", "Dress codes"],
            "c": "Cues signaling a relationship",
            "e": "Tie-signs are signals like a hand on a shoulder that inform "
                 "observers of a specific bond between people."
        },
        {
            "q": "What skill is linked to social success in children?",
            "o": ["Reading facial muscles", "Academic facts"],
            "c": "Reading facial muscles",
            "e": "Accurately decoding nonverbal cues leads to better social "
                 "navigation and peer acceptance."
        },
        {
            "q": "When a person leans forward, what is the signal?",
            "o": ["High receptivity", "Boredom"],
            "c": "High receptivity",
            "e": "A forward lean reduces distance and signals that the "
                 "listener is fully engaged and open."
        },
        {
            "q": "Large physical distance often signals what?",
            "o": ["Lower social stature", "High authority"],
            "c": "Lower social stature",
            "e": "Individuals with lower stature often maintain more distance "
                 "to avoid appearing as a threat to those in power."
        },
        {
            "q": "Define the 'parallel track' of communication.",
            "o": ["Nonverbal cues with speech", "Two languages"],
            "c": "Nonverbal cues with speech",
            "e": "The verbal track handles words, while the parallel nonverbal "
                 "track handles the emotional truth and context."
        },
        {
            "q": "Where do
