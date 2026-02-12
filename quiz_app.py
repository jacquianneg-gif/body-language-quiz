import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    nav = st.sidebar.radio("Navigation", ["1. Behavioral Visualizer", "2. Master Quiz"])

    if nav == "1. Behavioral Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.info("Reading the 'Parallel Track' of automatic muscle movements—the nonverbal signals that run simultaneously with speech.")
        
        st.markdown("### 🧐 Facial Literacy Trainer")
        st.caption("INSTRUCTIONS: Click each emotion below to reveal the specific involuntary muscle movements associated with 'muscle reading' and social success.")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals receptivity and warmth.")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Narrowed lips and lowered brow. Signals resistance or threat.")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
        
        st.markdown("---")
        st.markdown("### 🧍 Interactive Posture Lab")
        st.caption("INSTRUCTIONS: Select a posture to see how physical positioning communicates interest or status to others.")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates interest, liking, and openness.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a barrier, signaling defensiveness.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature and vulnerability.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        st.caption("INSTRUCTIONS: Drag the slider to change your physical distance from another person and observe how the 'Social Zone' shifts.")
        v = st.slider("Distance (feet):", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. Reserved for close relationships and high trust.")
        elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard for peer-to-peer and professional interactions.")
        else: st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    elif nav == "2. Master Quiz":
        st.header("🏆 Master Quiz: Behavioral Science")
        # [Quiz code remains the same as the expanded version provided previously]
        if "step" not in st.session_state: st.session_state.step = 0
        if "score" not in st.session_state: st.session_state.score = 0
        if "show" not in st.session_state: st.session_state.show = False

        qs = [
            ("In the famous 'point-light' dot studies, what was the primary factor that allowed observers to instantly identify a person's sex and emotional state?", 
             ["The color and size of the dots", "The specific patterns of movement and motion"], 
             "The specific patterns of movement and motion", 
             "When the dots were still, they appeared meaningless. Movement is the key to nonverbal identity."),
            ("What does the term 'tie-signs' refer to in nonverbal communication research?", 
             ["Formal dress codes", "Nonverbal cues that signal a specific relationship or bond"], 
             "Nonverbal cues that signal a specific relationship or bond", 
             "Tie-signs like holding hands signal a nonverbal relationship to observers."),
            ("A child's popularity is most closely linked to which specific skill?", 
             ["Reading automatic
