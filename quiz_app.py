import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    nav = st.sidebar.radio("Navigation", ["1. Behavioral Visualizer", "2. Master Quiz"])

    if nav == "1. Behavioral Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.info("Reading the 'Parallel Track'—nonverbal signals that run with speech.")
        
        st.markdown("### 🧐 Facial Literacy")
        st.caption("Click buttons to see involuntary emotional cues.")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile).")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Tight lips and lowered brow.")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes.")
        
        st.markdown("---")
        st.markdown("### 🧍 Posture Lab")
        st.caption("Select a posture to see the social signal.")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Indicates interest and openness.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Signals defensiveness.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Signals lower social stature.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        st.caption("Explore 'Proxemics' and social boundaries.")
        v = st.slider("Distance (feet):", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE ZONE.")
        elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE.")
        else: st.error(f"{v}ft: PUBLIC ZONE.")

    elif nav == "2. Master Quiz":
        st.header("🏆 Master Quiz")
        if "step" not in st.session_state: st.session_state.step = 0
        if "score" not in st.session_state: st.session_state.score = 0
        if "show" not in st.session_state: st.session_state.show = False

        qs = [
            ("What revealed identity in dot studies?", ["Movement", "Color"], "Movement", "Motion reveals identity."),
            ("What are 'tie-signs'?", ["Bond cues", "Dress"], "Bond cues", "Signals a relationship."),
            ("Success linked to reading...", ["Faces", "Books"], "Faces", "Muscle reading leads to success."),
            ("Leaning forward signals...", ["Receptive", "Bored"], "Receptive", "Signals interest."),
            ("Distance signals what status?", ["Low", "High"], "Low", "Distance signals lower stature.")
        ]

        if st.session_state.step < len(qs):
            q, opts, cor, ex = qs[st.session_state.step]
            st.markdown(f"### Question {st.session_state.step + 1}")
            st.markdown(f"## {q}")
            ans = st.radio("Pick one:", opts, key=f"q{st.session_state.step}")
            if st.button("Check Answer"):
                st.session_state.show = True
                if ans == cor: 
                    st.success(f"CORRECT: {ex}")
                    st.session_state.score += 1
                else: st.error(f"WRONG: {ex}")
            if st.session_state.show and st.button("Next ➡️"):
                st.session_state.step += 1; st.session_state.show = False; st.rerun()
        else:
            st.balloons(); st.header(f"Final Score: {st.session_state.score}/{len(qs)}")
            if st.button("Restart"): st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
