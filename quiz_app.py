import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Behavioral Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic signals.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"):
            st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth.")
        if st.button("🙇‍♂️ Lean"):
            st.info("LEAN: Forward movement indicates high interest.")
    with c2:
        if st.button("😠 Anger"):
            st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"):
            st.error("FOLD: Crossed arms create a barrier or defensiveness.")
    with c3:
        if st.button("😨 Fear"):
            st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"):
            st.warning("HUNCH: Signals lower social stature or vulnerability.")
    
    st.subheader("Social Distance Ruler (Tie-Signs)")
    st.caption("How trust and status dictate physical space.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3:
        st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10:
        st.info(f"{v}ft: SOCIAL ZONE. Standard peer/professional space.")
    else:
        st.error(f"{v}ft: PUBLIC ZONE. Formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "show" not in st.session_state:
        st.session_state.show = False

    # Vertical list structure to prevent line cutoff
    qs = [
        {
            "q": "What allowed identification of sex in 'point-light' studies?",
            "o": ["Static dot patterns", "Patterns of movement"],
            "c": "Patterns of movement",
            "e": "Motion decodes identity. Without it, the figure disappears."
        },
        {
            "q": "What does the term 'tie-signs' refer to in research?",
            "o": ["Cues signaling a bond", "Formal dress codes"],
            "c": "Cues signaling a bond",
            "e": "Tie-signs signal a nonverbal relationship to observers."
        },
        {
            "q": "Social success in children is most linked to which skill?",
            "o": ["Reading facial muscles", "Academic math facts"],
            "c": "Reading facial muscles",
            "e": "Success is linked to 'muscle reading' facial cues."
        },
        {
            "q": "When a person leans forward, what is the likely signal?",
            "o": ["Receptivity and interest", "Boredom or fatigue"],
            "c": "Receptivity and interest",
            "e": "Leaning forward shows engagement and openness."
        },
        {
            "q": "Large social distance typically signals what about status?",
            "o": ["High authority", "Lower social stature"],
            "c": "Lower social stature",
            "e": "Distance avoids appearing as a threat to others."
        },
        {
            "q": "What exactly is the 'parallel track' of communication?",
            "o": ["Nonverbal cues with speech", "Speaking two languages"],
            "c": "Nonverbal cues with speech",
            "e": "The nonverbal track runs automatically with words."
        },
        {
            "q": "When feeling threatened, toward whom do men look?",
            "o": ["Partners or companions", "Strangers in the room"],
            "c": "Partners or companions",
            "e": "Men look to partners for nonverbal reassurance."
        },
        {
            "q": "Why is nonverbal signaling considered 'automatic'?",
            "o": ["Involuntary muscle movements", "Intentional practice"],
            "c": "Involuntary muscle movements",
            "e": "Involuntary cues are often more 'honest' than speech."
        },
        {
            "q": "What happens when 'point-light' dots stop moving?",
            "o": ["The figure stays visible", "The human figure disappears"],
            "c": "The human figure disappears",
            "e": "The brain needs motion to activate the parallel track."
        },
        {
            "q": "How do nonverbal cues help navigate social groups?",
            "o": ["Signaling status/receptivity", "Finding physical exits"],
            "c": "Signaling status/receptivity",
            "e": "Posture and distance act as a 'social map' for groups."
        }
    ]

    if st.session_state.step < len(qs):
        item = qs[st.session_state.step]
        st.write(f"### Question {st.session_state.step + 1} of 10")
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
        st.header(f"Final Score: {st.session_state.score}/10")
        if st.button("Restart Assessment"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()

if __name__ == "__main__":
    main()
