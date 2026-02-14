import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    
    st.info("""
    **STUDENT INSTRUCTIONS:**
    1. **Explore Icons:** Click buttons below (😊, 🙇‍♂️, 😠, etc.) to see behavioral meanings.
    2. **Use Slider:** Move the 'Distance Ruler' to see how physical space changes social zones.
    """)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Duchenne smile (crinkled eyes). Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Forward movement indicates high interest.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tightened lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Crossed arms signal defensiveness.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower social stature.")
    
    st.subheader("Proxemics: Social Distance Ruler")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE ZONE.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE.")
    else: st.error(f"{v}ft: PUBLIC ZONE.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Condensed question list to prevent cut-off errors
    qs = [
        ("What identifies sex/emotion in 'point-light' studies?", ["Movement patterns", "Static dots"], "Movement patterns", "Motion decodes identity."),
        ("What are 'tie-signs'?", ["Dress codes", "Cues signaling a bond"], "Cues signaling a bond", "They signal relationships."),
        ("Social success in children is linked to...", ["Muscle reading", "Facts"], "Muscle reading", "Linked to reading facial cues."),
        ("Leaning forward signals...", ["Boredom", "Interest"], "Interest", "Shows receptivity."),
        ("Large distance signals...", ["High status", "Lower status"], "Lower status", "Avoids appearing as a threat."),
        ("The 'parallel track' is...", ["Nonverbal cues with speech", "Two languages"], "Nonverbal cues with speech", "Runs with words."),
        ("Threatened men look toward...", ["Partners", "Strangers"], "Partners", "For reassurance."),
        ("Nonverbal signaling is 'automatic' because...", ["Involuntary muscles", "Practice"], "Involuntary muscles", "Harder to fake."),
        ("If 'point-light' dots stop moving...", ["Figure stays", "Figure disappears"], "Figure disappears", "Brain needs motion."),
        ("Cues help navigate groups by...", ["Signaling status", "Finding exits"], "Signaling status", "Acts as a social map.")
    ]

    if st.session_state.step < len(qs):
        q, opts, cor, ex = qs[st.session_state.step]
        st.write(f"### Question {st.session_state.step + 1}")
        ans = st.radio(q, opts, key=f"q{st.session_state.step}")
        if st.button("Check Answer"):
            st.session_state.show = True
            if ans == cor:
                st.success(f"CORRECT! {ex}")
                st.session_state.score += 1
            else: st.error(f"NOT QUITE. {ex}")
        if st.session_state.show and st.button("Next ➡️"):
            st.session_state.step += 1; st.session_state.show = False; st.rerun()
    else:
        st.balloons(); st.header(f"Final Score: {st.session_state.score}/10")
        if st.button("Restart"): st.session_state.step = 0; st.session_state.score = 0; st.rerun()

if __name__ == "__main__":
    main()
