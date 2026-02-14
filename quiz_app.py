import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—the automatic nonverbal signals that run simultaneously with spoken words.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): 
            st.success("JOY: Characterized by the Duchenne smile (crinkled eyes). It signals genuine warmth and high social receptivity.")
        if st.button("🙇‍♂️ Lean"): 
            st.info("LEANING: Moving the torso forward indicates a high level of interest, engagement, and openness to the speaker.")
    with c2:
        if st.button("😠 Anger"): 
            st.error("ANGER: Marked by narrowed lips and a lowered brow. It signals resistance, disagreement, or a perceived threat.")
        if st.button("🙅‍♂️ Fold"): 
            st.error("FOLDING: Crossing the arms creates a physical barrier, signaling defensiveness or a lack of receptivity.")
    with c3:
        if st.button("😨 Fear"): 
            st.warning("FEAR: Indicated by raised brows and widened eyes. It signals submissiveness, high stress, or anxiety.")
        if st.button("👤 Hunch"): 
            st.warning("HUNCHING: This posture signals lower social stature, a desire to disappear, or a feeling of vulnerability.")
    
    st.subheader("The Social Distance Ruler")
    st.caption("How trust and status dictate the physical space between people, acting as a 'Tie-Sign' to observers.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: 
        st.success(f"{v}ft: INTIMATE ZONE. Reserved for high-trust bonds and close personal relationships.")
    elif v <= 10: 
        st.info(f"{v}ft: SOCIAL ZONE. The standard distance for peer-to-peer and professional interactions.")
    else: 
        st.error(f"{v}ft: PUBLIC ZONE. Distance maintained for formal speaking or interactions with strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # 10 Detailed Questions with Shuffled Answer Keys
    qs = [
        {
            "q": "What allowed observers to identify sex and emotion in 'point-light' studies?",
            "o": ["Static dot patterns and arrangements", "The specific patterns of movement"],
            "c": "The specific patterns of movement",
            "e": "When dots stop moving, the human figure disappears. Movement is the key to decoding identity."
        },
        {
            "q": "What does the term 'tie-signs' refer to in nonverbal communication research?",
            "o": ["Nonverbal cues that signal a specific bond or relationship", "Formal dress codes required in professional organizations"],
            "c": "Nonverbal cues that signal a specific bond or relationship",
            "e": "Tie-signs act as signals to observers about the nature of the relationship between two people."
        },
        {
            "q": "Social success and popularity in children is most
