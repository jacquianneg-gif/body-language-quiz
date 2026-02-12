import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    nav = st.sidebar.radio("Navigation", ["1. Behavioral Visualizer", "2. Master Quiz"])

    if nav == "1. Behavioral Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.info("Reading the 'Parallel Track'—the nonverbal signals that run simultaneously with speech.")
        
        st.markdown("### 🧐 Facial Literacy Trainer")
        st.markdown("**INSTRUCTIONS:** Click each button to reveal the involuntary muscle movements associated with 'muscle reading'.")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth and social success.")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Tight lips and lowered brow. Signals resistance or threat.")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
        
        st.markdown("---")
        st.markdown("### 🧍 Posture Lab")
        st.markdown("**INSTRUCTIONS:** Select a posture to see how positioning communicates interest or status.")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates interest, liking, and openness.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a barrier, signaling defensiveness.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature and vulnerability.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        st.markdown("**INSTRUCTIONS:** Drag the slider to explore 'Proxemics'—how trust and status dictate physical space.")
        v = st.slider("Distance (feet):", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. Reserved for close trust and high-status bonds.")
        elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard for peer-to-peer and professional interactions.")
        else: st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    elif nav == "2. Master Quiz":
        st.header("🏆 Master Quiz: Behavioral Science")
        if "step" not in st.session_state: st.session_state.step = 0
        if "score" not in st.session_state: st.session_state.score = 0
        if "show" not in st.session_state: st.session_state.show = False

        qs = [
            ("What allowed observers to identify sex and emotion in 'point-light' studies?", 
             ["The color of the dots", "The patterns of movement"], 
             "The patterns of movement", 
             "Static dots appear meaningless. Movement is the key that allows the brain to decode identity and emotion."),
            
            ("What does the term 'tie-signs' refer to in nonverbal research?", 
             ["Formal dress codes", "Cues that signal a specific bond"], 
             "Cues that signal a specific bond", 
             "Tie-signs, like standing in an intimate zone, signal a nonverbal relationship to observers."),
            
            ("Social success and popularity in children is most linked to...", 
             ["Reading facial muscle movements", "Memorizing facts"], 
             "Reading facial muscle movements", 
             "Popularity is highly correlated with 'muscle reading'—the ability to accurately interpret subtle facial cues."),
            
            ("When a person leans forward, what is the most likely signal?", 
             ["Boredom", "Receptivity and interest"], 
             "Receptivity and interest", 
             "Leaning into a conversation is a universal sign of interest and openness to the speaker."),
            
            ("Large physical distance typically signals what about social status?", 
             ["Lower social stature", "High authority"], 
             "Lower social stature", 
             "Research shows lower-status individuals often maintain greater distances to avoid appearing as a threat.")
        ]

        if st.session_state.step < len(qs):
            q, opts, cor, ex = qs[st.session_state.step]
            st.markdown(f"### Question {st.session_state.step + 1} of {len(qs)}")
            st.markdown(f"## {q}")
            ans = st.radio("Select the best answer:", opts, key=f"q{st.session_state.step}")
            if st.button("Check Answer"):
                st.session_state.show = True
                if ans == cor: 
                    st.success(f"**CORRECT!** {ex}")
                    st.session_state.score += 1
                else: st.error(f"**NOT QUITE.** {ex}")
            if st.session_state.show and st.button("Move to Next Question ➡️"):
                st.session_state.step += 1; st.session_state.show = False; st.rerun()
        else:
            st.balloons()
            st.header(f"Final Assessment Score: {st.session_state.score}/{len(qs)}")
            if st.button("Restart Quiz"):
                st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
