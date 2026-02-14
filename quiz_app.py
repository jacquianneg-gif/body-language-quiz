import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()

    # --- I. PROXIMITY SLIDER ---
    st.header("I. Proximity & Space")
    st.write("Adjust the slider to see the social zones of distance.")
    dist = st.slider("Distance in Feet:", 0.0, 15.0, 4.0)
    
    if dist < 1.5:
        st.error(f"{dist}ft: INTIMATE ZONE (Extreme trust or threat)")
    elif dist < 4.0:
        st.success(f"{dist}ft: PERSONAL ZONE (Friends and family)")
    elif dist < 12.0:
        st.info(f"{dist}ft: SOCIAL ZONE (Professional/Casual)")
    else:
        st.warning(f"{dist}ft: PUBLIC ZONE (Strangers/Formal)")

    st.divider()
    
    # --- II. BEHAVIORAL SIMULATOR ---
    st.header("II. Behavioral Analysis Simulator")
    st.write("Click a button to analyze the nonverbal signal.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("😊 JOY")
        if st.button("Analyze Joy"):
            st.success("ANALYSIS: True joy involves involuntary "
                       "muscle contraction around the eyes.")
        
        st.subheader("😠 RESISTANCE")
        if st.button("Analyze Resistance"):
            st.error("ANALYSIS: Compressed lips signal internal "
                     "disagreement or cognitive effort.")

        st.subheader("🙅‍♂️ BARRIERS")
        if st.button("Analyze Barriers"):
            st.error("ANALYSIS: Crossed arms act as a barrier, "
                     "signaling defensiveness.")
            
    with c2:
        st.subheader("😨 STRESS")
        if st.button("Analyze Stress"):
            st.warning("ANALYSIS: Widened eyes increase visual "
                       "intake, signaling a threat response.")

        st.subheader("🙇‍♂️ HUNCHED SHOULDERS")
        if st.button("Analyze Posture"):
            st.warning("ANALYSIS: Hunching is an attempt to "
                       "appear smaller and less threatening.")

    st.divider()
    
    # --- III. ASSESSMENT ---
    st.header("III. Comprehensive Assessment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "fb" not in st.session_state: st.session_state.fb = None

    # Shuffled Question Data
    qs = [
        {
            "q": "In 'point-light' studies, what identifies sex and emotion?",
            "o": ["Patterns of movement", "Static dots"],
            "c": "Patterns of movement",
            "e": "The brain decodes identity through the rhythm of motion."
        },
        {
            "q": "What do 'tie-signs' refer to in social groups?",
            "o": ["Dress codes", "Cues signaling a relationship"],
            "c": "Cues signaling a relationship",
            "e": "Tie-signs are signals like a hand on a shoulder."
        },
        {
            "q": "What skill is linked to social success in children?",
            "o": ["Academic facts", "Reading facial muscles"],
            "c": "Reading facial muscles",
            "e": "Decoding nonverbal cues allows for peer acceptance."
        },
        {
            "q": "When a person leans forward, what is the signal?",
            "o": ["High receptivity", "Boredom"],
            "c": "High receptivity",
            "e": "A forward lean signals engagement and openness."
        },
        {
            "q": "Large physical distance often signals what?",
            "o": ["High authority", "Lower social stature"],
            "c": "Lower social stature",
            "e": "Distance is often used to avoid appearing as a threat."
        },
        {
            "q": "Define the 'parallel track' of communication.",
            "o": ["Two languages", "Nonverbal cues with speech"],
            "c": "Nonverbal cues with speech",
            "e": "The nonverbal track handles the emotional truth."
        },
        {
            "q": "Where do men look for reassurance when threatened?",
            "o": ["Partners/companions", "Strangers"],
            "c": "Partners/companions",
            "e": "Individuals look to 'safe' targets for support."
        },
        {
            "q": "Why is nonverbal signaling 'automatic'?",
            "o": ["Practice", "Involuntary muscles"],
            "c": "Involuntary muscles",
            "e": "The limbic system controls signals like pupil dilation."
        },
        {
            "q": "In 'point-light' studies, what happens when dots stop?",
            "o": ["Figure stays", "Figure disappears"],
            "c": "Figure disappears",
            "e": "The brain requires motion to perceive the human form."
        },
        {
            "q": "How do nonverbal cues help navigate hierarchies?",
            "o": ["By signaling status", "By finding exits"],
            "c": "By signaling status",
            "e": "Body language acts as a map of social power."
        }
    ]

    if st.session_state.step < len(qs):
        curr = qs[st.session_state.step]
        st.subheader(f"Question {st.session_state.step + 1}")
        st.write(f"**{curr['q']}**")
        ans = st.radio("Pick one:", curr['o'], key=f"ans_{st.session_state.step}")
        
        if st.button("Check Answer"):
            if ans == curr['c']:
                st.session_state.score += 1
                st.session_state.fb = ("ok", f"CORRECT: {curr['e']}")
            else:
                st.session_state.fb = ("no", f"WRONG: {curr['e']}")

        if st.session_state.fb:
            res, msg = st.session_state.fb
            if res == "ok": st.success(msg)
            else: st.error(msg)
            if st.button("Next ➡️"):
                st.session_state.step += 1
                st.session_state.fb = None
                st.rerun()
    else:
        st.balloons()
        st.header(f"Final Score: {st.session_state.score} / {len(qs)}")
        if st.button("Restart"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()

if __name__ == "__main__":
    main()
