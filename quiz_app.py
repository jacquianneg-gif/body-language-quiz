import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    sel = st.sidebar.radio("Navigation", ["1. Visualizer", "2. Master Quiz"])

    if sel == "1. Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.markdown("### 🧐 Facial Literacy Trainer")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Warmth).")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Tight lips (Threat).")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Raised brows (Stress).")
        
        st.markdown("---")
        st.markdown("### 🧍 Interactive Posture Lab")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Interest/Liking.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Defensive.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Low status.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        v = st.slider("Feet:", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE.")
        elif v <= 10: st.info(f"{v}ft: SOCIAL.")
        else: st.error(f"{v}ft: PUBLIC.")

    elif sel == "2. Master Quiz":
        st.header("🏆 Master Quiz")
        if "ix" not in st.session_state: st.session_state.ix = 0
        if "sc" not in st.session_state: st.session_state.sc = 0
        if "dn" not in st.session_state: st.session_state.dn = False

        qs = [
            ("Identity in dot studies?", ["Movement", "Color"], "Movement", "Motion reveals identity."),
            ("What are 'tie-signs'?", ["Bond cues", "Dress"], "Bond cues", "Signals a relationship."),
            ("Success linked to reading...", ["Faces", "Books"], "Faces", "Muscle reading = success."),
            ("Leaning forward signals...", ["Receptive", "Bored"], "Receptive", "Signals interest."),
            ("Large distance = what status?", ["Low", "High"], "Low", "Distance = lower stature."),
            ("Parallel track is...", ["Nonverbal", "Speech"], "Nonverbal", "Simultaneous with speech."),
            ("Threatened men look at...", ["Partners", "Strangers"], "Partners", "Seeking support."),
            ("Nonverbal signaling is...", ["Automatic", "Conscious"], "Automatic", "Occurs without thought."),
            ("Still dots look like...", ["Meaningless", "A person"], "Meaningless", "Motion is required."),
            ("Cues help navigate...", ["Structures", "Forests"], "Structures", "Essential for hierarchy.")
        ]

        if st.session_state.ix < 10:
            q, opts, cor, ex = qs[st.session_state.ix]
            st.markdown(f"### Question {st.session_state.ix + 1}")
            st.markdown(f"## {q}")
            ans = st.radio("Pick one:", opts, key=f"q{st.session_state.ix}")
            if st.button("Check Answer"):
                st.session_state.dn = True
                if ans == cor:
                    st.success(f"CORRECT: {ex}")
                    st.session_state.sc += 1
                else: st.error(f"WRONG: {ex}")
            if st.session_state.dn and st.button("Next Question ➡️"):
                st.session_state.ix += 1; st.session_state.dn = False; st.rerun()
        else:
            st.balloons(); st.header(f"Final Score: {st.session_state.sc}/10")
            if st.button("Restart"): st.session_state.ix = 0; st.session_state.sc = 0; st.rerun()

if __name__ == "__main__":
    main()