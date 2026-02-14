import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    
    # Header Section
    st.markdown("<h1 style='text-align: center;'>The Professional Body Language Lab</h1>", unsafe_content_code=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Bridging Nonverbal Theory and Social Literacy</h4>", unsafe_content_code=True)
    
    # SECTION 1: THE SIMULATOR
    st.divider()
    st.subheader("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—the automatic nonverbal signals that run simultaneously with spoken words.")
    
    st.markdown("### Facial Literacy Training")
    st.caption("INSTRUCTIONS: Click an emotion to see the involuntary muscle movements associated with 'muscle reading' and social success.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne smile). Signals warmth and high receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Narrowed lips and lowered brow. Signals resistance or perceived threat.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals submissiveness or stress.")
    
    st.markdown("### Postural Positioning")
    st.caption("INSTRUCTIONS: Select a posture to observe how physical alignment communicates interest or social status.")
    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates high interest and openness.")
    with p2:
        if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a barrier, signaling defensiveness or closing off.")
    with p3:
        if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching signals lower social stature and vulnerability.")
    
    st.markdown("### Proxemics: The Social Distance Ruler")
    st.caption("INSTRUCTIONS: Use the slider to explore how trust and status dictate the physical space between people.")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. Reserved for high-trust bonds and close relationships.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. Standard for peer-to-peer and professional interactions.")
    else: st.error(f"{v}ft: PUBLIC ZONE. Maintained for formal speaking or strangers.")

    # SECTION 2: THE QUIZ
    st.divider()
    st.subheader("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    qs = [
        ("What allowed observers to identify sex and emotion in 'point-light' studies?", ["The color of dots", "The patterns of movement"], "The patterns of movement", "Static dots appear meaningless. Movement is the key to decoding identity and emotion."),
        ("What are 'tie-signs'?", ["Formal dress codes", "Cues that signal a specific bond"], "Cues that signal a specific bond", "Tie-signs signal a nonverbal relationship to observers."),
        ("Social success in children is most linked to which skill?", ["Reading facial muscle movements", "Memorizing facts"], "Reading facial muscle movements", "Popularity is highly correlated with 'muscle reading'."),
        ("When a person leans forward, what is the most likely signal?", ["Boredom", "Receptivity and interest"], "Receptivity and interest", "Leaning forward shows interest and openness."),
        ("Large physical distance typically signals what status?", ["Lower social stature", "High authority"], "Lower social stature", "Lower-status individuals maintain distance to avoid appearing as a threat."),
        ("What is the 'parallel track'?", ["Nonverbal cues running with speech", "Speaking two languages"], "Nonverbal cues running with speech", "The nonverbal track runs automatically alongside spoken words."),
        ("Threatened men typically look toward...", ["Strangers", "Partners/Companions"], "Partners/Companions", "Men look to partners for nonverbal reassurance and safety."),
        ("Why is nonverbal signaling considered 'automatic'?", ["Occurs without conscious thought", "It must be learned in a lab"], "Occurs without conscious thought", "Involuntary muscle movements make nonverbal cues more 'honest'."),
        ("What happens when 'point-light' dots stop moving?", ["The figure remains visible", "The human figure disappears"], "The human figure disappears", "Human perception requires motion to activate the parallel track of identity."),
        ("How do nonverbal cues help navigate hierarchies?", ["By signaling status and receptivity", "By helping find exits"], "By signaling status and receptivity", "Posture and distance act as a 'social map' for group structures.")
    ]

    if st.session_state.step < len(qs):
        q, opts, cor, ex = qs[st.session_state.step]
        st.markdown(f"**Question {st.session_state.step + 1} of 10**")
        st.write(f"### {q}")
        ans = st.radio("Select the most accurate answer:", opts, key=f"q{st.session_state.step}")
        if st.button("Check Answer"):
            st.session_state.show = True
            if ans == cor: 
                st.success(f"**CORRECT!** {ex}")
                st.session_state.score += 1
            else: st.error(f"**NOT QUITE.** {ex}")
        if st.session_state.show and st.button("Next Question ➡️"):
            st.session_state.step += 1; st.session_state.show = False; st.rerun()
    else:
        st.balloons()
        st.header(f"Final Score: {st.session_state.score}/10")
        if st.button("Restart Assessment"):
            st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
