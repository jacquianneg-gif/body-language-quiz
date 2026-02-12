import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    nav = st.sidebar.radio("Navigation", ["1. Behavioral Visualizer", "2. Master Quiz"])

    if nav == "1. Behavioral Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.info("Reading the 'Parallel Track' of automatic muscle movements—the signals that run simultaneously with speech.")
        
        st.markdown("### 🧐 Facial Literacy Trainer")
        st.markdown("**STUDENT INSTRUCTIONS:** Click each button to see how 'muscle reading' helps identify involuntary emotional cues.")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth and social success.")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Tight lips and lowered brow. Signals resistance or threat.")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
        
        st.markdown("---")
        st.markdown("### 🧍 Interactive Posture Lab")
        st.markdown("**STUDENT INSTRUCTIONS:** Select a posture to observe how body positioning communicates interest or status.")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates interest and openness.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms signal defensiveness or closing off.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        st.markdown("**STUDENT INSTRUCTIONS:** Use the slider to explore 'Proxemics'—how physical distance changes based on trust and status.")
        v = st.slider("Distance (feet):", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE ZONE (Close bonds/Trust).")
        elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE (Peers/Professional).")
        else: st.error(f"{v}ft: PUBLIC ZONE (Strangers/Formal).")

    elif nav == "2. Master Quiz":
        st.header("🏆 Master Quiz")
        if "step" not in st.session_state: st.session_state.step = 0
        if "score" not in st.session_state: st.session_state.score = 0
        if "show" not in st.session_state: st.session_state.show = False

        # Condensed quiz logic to prevent any further GitHub truncation
        qs = [
            ("What revealed identity in dot studies?", ["Movement", "Color"], "Movement", "Motion reveals identity and emotion."),
            ("What are 'tie-signs'?", ["Bond cues", "Dress"], "Bond cues", "Signals a nonverbal relationship."),
            ("Success linked to reading...", ["Faces", "Books"], "Faces", "Muscle reading leads to social success."),
            ("Leaning forward signals...", ["Receptive", "Bored"], "Receptive", "Signals interest and liking."),
            ("Distance signals what status?", ["Low", "High"], "Low", "Distance signals lower stature."),
            ("The 'parallel track' is...", ["Nonverbal", "Speech"], "Nonverbal", "Runs with speech."),
            ("Threatened men look at...", ["Partners", "Strangers"], "Partners", "Seeking nonverbal support."),
            ("Nonverbal signaling is...", ["Automatic", "Conscious"], "Automatic", "Occurs without thought."),
            ("Still dots look like...", ["Meaningless", "A person"], "Meaningless", "Motion is required for perception."),
            ("Cues help navigate...", ["Structures", "Forests"], "Structures", "Essential for social hierarchy.")
        ]

        if st.session_state.step < 10:
            q, opts, cor, ex = qs[st.session_state.step]
            st.markdown(f"### Question {st.session_state.step + 1}")
            st.markdown(f"## {q}")
            ans = st.radio("Pick one:", opts, key=f"q{st.session_state.step}")
            if st.button("Check Answer"):
                st.session_state.show = True
                if ans == cor: st.success(f"CORRECT: {ex}")
                else: st.error(f"WRONG: {ex}")
                if ans == cor: st.session_state.score += 1
            if st.session_state.show and st.button("Next ➡️"):
                st.session_state.step += 1; st.session_state.show = False; st.rerun()
        else:
            st.balloons(); st.header(f"Final Score: {st.session_state.score}/10")
            if st.button("Restart"): st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
