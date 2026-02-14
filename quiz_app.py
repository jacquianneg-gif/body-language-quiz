import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    # --- SECTION I: SIMULATOR ---
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Explore how specific physical signals are interpreted in professional settings.")
    
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
    if v <= 3: st.success(f"{v} ft: INTIMATE SPACE. Reserved for high-trust bonds.")
    elif v <= 10: st.info(f"{v} ft: SOCIAL SPACE. Standard for professional and peer interactions.")
    else: st.error(f"{v} ft: PUBLIC SPACE. Typical for formal speaking or strangers.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT ---
    st.header("II. COMPREHENSIVE ASSESSMENT")
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Question Bank
    data = [
        {"q": "In 'point-light' studies, what allowed observers to identify sex and emotion?", "o": ["Patterns of movement", "Static arrangement of dots"], "c": "Patterns of movement", "e": "The brain decodes identity through the rhythm of motion, even without a visible body."},
        {"q": "What do 'tie-signs' refer to in social groups?", "o": ["Cues signaling a relationship exists", "Formal group dress codes"], "c": "Cues signaling a relationship exists", "e": "Tie-signs are signals like a hand on a shoulder that inform observers of a specific bond."},
        {"q": "What skill is most linked to social success in children?", "o": ["Reading facial muscle movements", "Memorizing academic facts"], "c": "Reading facial muscle movements", "e": "Accurately decoding nonverbal cues leads to better social navigation and peer acceptance."},
        {"q": "When a person leans forward, what is the likely signal?", "o": ["Receptivity and interest", "Boredom or fatigue"], "c": "Receptivity and interest", "e": "Leaning in reduces distance and signals that the listener is fully engaged."},
        {"q": "What does large physical distance typically signal about stature?", "o": ["Lower perceived social stature", "High levels of authority"], "c": "Lower perceived social stature", "e": "Individuals with lower stature often maintain distance to avoid appearing as a threat."},
        {"q": "How is the 'parallel track' of communication defined?", "o": ["Nonverbal cues running with speech", "Speaking two languages at once"], "c": "Nonverbal cues running with speech", "e": "The verbal track handles words, while the parallel track handles emotional truth."},
        {"q": "Where do men look for reassurance when threatened socially?", "o": ["Toward partners or companions", "Toward strangers in the room"], "c": "Toward partners or companions", "e": "In high-stress settings, individuals glance toward 'safe' people for emotional support."},
        {"q": "Why is non
