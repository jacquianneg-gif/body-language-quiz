import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("""**📋 STUDENT INSTRUCTIONS:**
1. **Explore Behavioral Cues:** Click the buttons below to reveal how specific physical signals are interpreted.
2. **Observe Social Distance:** Use the slider below to adjust physical space and see how interaction zones are classified.
3. **Test Knowledge:** Scroll to Section II to complete the formal assessment.""")
    
    st.write("Study the 'Parallel Track'—the automatic nonverbal signals that run constantly alongside spoken words.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 True Joy"): st.success("TRUE JOY: This is characterized by involuntary muscle contraction around the eyes, which signals genuine warmth and rapport.")
        if st.button("🙇‍♂️ The Lean"): st.info("THE LEAN: Moving the torso toward a speaker indicates high levels of interest, active listening, and receptivity.")
    with c2:
        if st.button("😠 Resistance"): st.error("RESISTANCE: Tightened lips and a lowered brow often signal internal disagreement or a lack of openness to new ideas.")
        if st.button("🙅‍♂️ Barriers"): st.error("BARRIERS: Crossing arms or placing objects between people can signal a defensive posture or a need for protection.")
    with c3:
        if st.button("😨 Stress"): st.warning("STRESS: Raised eyebrows and widened eyes often signal that a person feels overwhelmed or threatened by the environment.")
        if st.button("👤 Diminishment"): st.warning("DIMINISHMENT: Hunching the shoulders or lowering the head signals a lack of confidence or a lower perceived social stature.")
    
    st.subheader("The Social Distance Ruler")
    v = st.slider("Physical Distance (measured in feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v} feet: INTIMATE SPACE. This distance is reserved for high-trust bonds and close personal relationships.")
    elif v <= 10: st.info(f"{v} feet: PEER/SOCIAL SPACE. This is the standard distance for professional interactions and peer-to-peer discussions.")
    else: st.error(f"{v} feet: PUBLIC/FORMAL SPACE. This distance is typical for public speaking or interactions with strangers in a formal setting.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session
