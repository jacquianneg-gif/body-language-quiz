import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic nonverbal signals that run with speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Forward movement indicates high interest and openness.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Crossed arms signal defensiveness or barriers.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower social stature and vulnerability.")
    
    st.subheader("Proxemics: Social Distance Ruler")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Professional/Peer interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Formal speaking/Strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Shuffled 10 detailed questions
    qs = [
        ("What allowed observers to identify sex and emotion in 'point-light' studies?", 
         ["The patterns of movement", "Static dot patterns"], 
         "The patterns of movement", "Motion allows the brain to decode identity."),
        ("What does the term 'tie-signs' refer to in nonverbal research?", 
         ["Formal organizational dress codes", "Cues that signal a specific bond"], 
         "Cues that signal a specific bond", "Tie-signs signal a relationship to observers."),
        ("Social success and popularity in children is most linked to...", 
         ["Reading facial muscle movements", "Memorizing academic facts"], 
         "Reading facial muscle movements", "Popularity is linked to 'muscle reading'."),
        ("When a person leans forward, what is the most likely signal?", 
         ["Boredom or fatigue", "Receptivity and interest"], 
         "Receptivity and interest", "Leaning forward shows interest and openness."),
        ("Large physical distance typically signals what about social status?", 
         ["Lower social stature", "High authority and power"], 
         "Lower social stature", "Distance avoids appearing as a threat."),
        ("What exactly is the 'parallel track' of communication?", 
         ["Nonverbal cues running with speech", "Speaking two languages at once"], 
         "Nonverbal cues running with speech", "It runs automatically alongside words."),
        ("When feeling threatened, men typically look toward...", 
         ["Partners or companions", "Strangers in the room"], 
         "Partners or companions", "Men look to partners for nonverbal reassurance."),
        ("Why is nonverbal signaling considered 'automatic'?", 
         ["It involves involuntary muscle movements", "It must be practiced in a mirror"], 
         "It involves involuntary muscle movements", "Involuntary cues are more 'honest'."),
        ("What happens when 'point-light' dots stop moving?", 
         ["The figure remains visible", "The human figure disappears"], 
         "The human figure disappears", "Perception requires motion to activate the track."),
        ("How do nonverbal cues help people navigate social groups?", 
         ["By signaling status and receptivity", "By helping find the nearest exit"], 
         "By signaling status and receptivity", "Cues act as a 'social map' for groups.")
    ]

    if st.session_state.step < len(qs):
        q, opts, cor, ex = qs[st.session_state.step]
        st.write(f"### Question {st.session_state.step + 1} of 10")
        st.write(f"**{q}**")
        ans = st.radio("Select the best answer:", opts, key=f"q{st.session_state.step}")
        if st.button("Check Answer"):
            st.session_state.show = True
            if ans == cor: 
                st.success(f"CORRECT! {ex}")
                st.session_state.score += 1
            else: st.error(f"NOT QUITE. {ex}")
        if st.session_state.show and st.button("Next Question ➡️"):
            st.session_state.step += 1; st.session_state.show = False; st.rerun()
    else:
        st.balloons()
        st.header(f"Final Score: {st.session_state.score}/10")
        if st.button("Restart Assessment"):
            st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
