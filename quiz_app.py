import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    # --- SECTION I: SIMULATOR ---
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Instructions: Click buttons to reveal interpretations and use the slider to check social zones.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 True Joy"): st.success("TRUE JOY: Characterized by involuntary muscle contraction around the eyes, signaling genuine rapport.")
        if st.button("🙇‍♂️ The Lean"): st.info("THE LEAN: Moving the torso toward a speaker indicates high levels of interest and receptivity.")
    with c2:
        if st.button("😠 Resistance"): st.error("RESISTANCE: Tightened lips and a lowered brow signal internal disagreement or a lack of openness.")
        if st.button("🙅‍♂️ Barriers"): st.error("BARRIERS: Crossing arms can signal a defensive posture or a subconscious need for protection.")
    with c3:
        if st.button("😨 Stress"): st.warning("STRESS: Raised eyebrows and widened eyes signal that a person feels overwhelmed by their environment.")
        if st.button("👤 Diminishment"): st.warning("DIMINISHMENT: Hunching shoulders signals a lack of confidence or lower perceived social stature.")
    
    st.subheader("The Social Distance Ruler")
    v = st.slider("Physical Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v} ft: INTIMATE ZONE. Reserved for high-trust bonds and close personal relationships.")
    elif v <= 10: st.info(f"{v} ft: SOCIAL ZONE. The standard distance for professional interactions and peer discussions.")
    else: st.error(f"{v} ft: PUBLIC ZONE. Typical for formal public speaking or interactions with strangers.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT ---
    st.header("II. COMPREHENSIVE ASSESSMENT")
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Assessment data - Structured to prevent truncation errors
    qs = [
        ["In 'point-light' studies, what information allowed observers to identify sex and emotion?", ["Patterns of movement", "Static arrangement of dots"], "Patterns of movement", "The brain decodes identity and emotion through the rhythm of motion, even without a visible body."],
        ["What does the term 'tie-signs' refer to when analyzing human behavior in a group?", ["Cues signaling a relationship exists", "Formal group dress codes"], "Cues signaling a relationship exists", "Tie-signs are signals like a hand on a shoulder that inform observers of a specific bond between people."],
        ["What skill is most closely linked to social success and popularity in children?", ["Reading facial muscle movements", "Memorizing academic facts"], "Reading facial muscle movements", "Accurately decoding nonverbal cues leads to better social navigation and significantly higher peer acceptance."],
        ["When a person leans their torso forward, what is the most likely social signal?", ["High receptivity and interest",
