import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Behavioral Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic nonverbal signals.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"):
            st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth.")
        if st.button("🙇‍♂️ Lean"):
            st.info("LEANING: Forward movement indicates high interest.")
    with c2:
        if st.button("😠 Anger"):
            st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"):
            st.error("FOLDING: Crossed arms create a barrier or defensiveness.")
    with c3:
        if st.button("😨 Fear"):
            st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"):
            st.warning("HUNCHING: Signals lower social stature or vulnerability.")
    
    st.subheader("The Social Distance Ruler")
    st.caption("How trust and status dictate physical space ('Tie-Signs').")
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

    # Detailed Questions with Shuffled Answer Keys
    qs = [
        {
            "q": "What allowed observers to identify sex and emotion in 'point-light' studies?",
            "o": ["The specific patterns of movement", "Static dot patterns"],
            "c": "The specific patterns of movement",
            "e": "Motion decodes identity. Without it, the figure disappears."
        },
        {
            "q": "What does the term 'tie-signs' refer to in nonverbal research?",
            "o": ["Formal dress codes", "Cues signaling a bond"],
            "c": "Cues signaling a bond",
            "e": "Tie-signs signal a nonverbal relationship to observers."
        },
        {
            "q": "Social success and popularity in children is most linked to...",
            "o": ["Reading facial muscle movements", "Academic math facts"],
            "c": "Reading facial muscle movements",
            "e": "Success is linked to 'muscle reading' facial cues."
        },
        {
            "q": "When a person leans forward, what is the most likely signal?",
            "o": ["Boredom or fatigue", "Receptivity and interest"],
            "c": "Receptivity and interest",
            "e": "Leaning forward shows engagement and openness."
        },
        {
            "q": "Large social distance typically signals what about social status?",
            "o": ["Lower social stature", "High authority"],
            "c": "Lower social stature",
            "e": "Distance avoids appearing as a threat to others."
        },
        {
            "q": "What exactly is the 'parallel track' of communication?",
            "o": ["Nonverbal cues running with speech", "Speaking two languages"],
            "c": "Nonverbal cues running with speech",
            "e": "The nonverbal track runs automatically alongside words."
        },
        {
            "q": "When feeling threatened, toward whom do men typically look?",
            "o": ["Strangers in the room", "Partners or companions"],
            "c": "Partners or companions",
            "e": "Men look to partners for nonverbal reassurance."
        },
        {
            "q": "Why is nonverbal signaling considered 'automatic'?",
            "o": ["It involves involuntary muscle movements", "It must be learned"],
            "c": "It involves involuntary muscle movements",
            "e": "Involuntary cues are often more 'honest' than speech."
        },
        {
            "q": "What happens when 'point-light' dots stop moving?",
            "o": ["The human figure disappears", "The figure stays visible"],
            "c": "The human figure disappears",
            "e": "The brain needs motion to activate the parallel track."
        },
        {
            "q": "How do nonverbal cues help people navigate social groups?",
            "o": ["By signaling status and receptivity", "Finding physical exits"],
            "c": "By signaling status and receptivity",
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
