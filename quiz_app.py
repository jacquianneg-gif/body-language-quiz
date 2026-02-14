import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Behavioral Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic signals that run with speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"):
            st.success("JOY: Marked by the crinkling of the eyes. This signal is a predictor of social success.")
        if st.button("🙇‍♂️ Lean"):
            st.info("LEANING: Moving the torso forward indicates interest and receptivity.")
    with c2:
        if st.button("😠 Anger"):
            st.error("ANGER: Narrowed lips and a lowered brow. Signals resistance or a perceived threat.")
        if st.button("🙅‍♂️ Fold"):
            st.error("FOLDING: Crossed arms create a barrier, signaling defensiveness.")
    with c3:
        if st.button("😨 Fear"):
            st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
        if st.button("👤 Hunch"):
            st.warning("HUNCHING: Signals lower social stature and vulnerability.")
    
    st.subheader("The Social Distance Ruler")
    st.caption("How status dictates physical space, acting as a 'Tie-Sign' to observers.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3:
        st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds and close relationships.")
    elif v <= 10:
        st.info(f"{v}ft: SOCIAL ZONE. Standard peer-to-peer and professional space.")
    else:
        st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "show" not in st.session_state:
        st.session_state.show = False

    qs = [
        {
            "q": "What allowed observers to identify sex and emotion in 'point-light' studies?",
            "o": ["The specific patterns of movement", "Static dot patterns"],
            "c": "The specific patterns of movement",
            "e": "Motion decodes identity. Without it, the figure disappears."
        },
        {
            "q": "What does the term 'tie-signs' refer to in nonverbal research?",
            "o": ["Cues signaling a specific bond", "Formal dress codes"],
            "c": "Cues signaling a bond",
            "e": "Tie-signs signal a relationship to observers."
        },
        {
            "q": "Social success and popularity in children is most linked to which skill?",
            "o": ["Reading facial muscle movements", "Academic math facts"],
            "c": "Reading facial muscle movements",
            "e": "Success is linked to 'muscle reading' facial cues like eye crinkling."
        },
        {
            "q": "When a person leans forward, what is the most likely signal?",
            "o": ["Receptivity and interest", "Boredom or fatigue"],
            "c": "Receptivity and interest",
            "e": "Leaning forward shows engagement and openness."
        },
        {
            "q": "Large social distance typically signals what about social status?",
            "o": ["Lower social stature", "High authority"],
            "c": "Lower social stature",
            "e": "Distance avoids appearing as a threat to others."
        }
    ]

    if st.session_state.step < len(qs):
        item = qs[st.session_state.step]
        st.write(f"### Question {st.session_state.step + 1} of 5")
        st.write(f"**{item['q']}**")
        ans = st.radio("Select answer:", item['o'], key=f"q{st.session_state.step}")
        if st.button("Check Answer"):
            st.session_state.show = True
            if ans == item['c']: 
                st.success(f"CORRECT: {item['e']}")
                st.session_state.score += 1
            else:
                st.error(f"WRONG: {item['e']}")
        if st.session_state.show and st.button("Next Question ➡️"):
            st.session_state.step += 1
            st.session_state.show = False
            st.rerun()
    else:
        st.balloons()
        st.header(f"Final Score: {st.session_state.score}/5")
        if st.button("Restart Assessment"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()

if __name__ == "__main__":
    main()
