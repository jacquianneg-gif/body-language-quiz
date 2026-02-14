import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    # SECTION I: INTERACTIVE SIMULATOR
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("""**📋 STUDENT INSTRUCTIONS:**
    1. Click the buttons below to explore how specific physical signals are interpreted.
    2. Use the slider to observe how physical distance defines different social zones.
    3. Complete the 10-question evaluation in Section II.""")
    
    st.write("Analyze the 'Parallel Track'—automatic nonverbal signals that run alongside speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 True Joy"): 
            st.success("""TRUE JOY: Characterized by involuntary muscle contraction 
            around the eyes, signaling genuine warmth and rapport.""")
        if st.button("🙇‍♂️ The Lean"): 
            st.info("""THE LEAN: Moving the torso toward a speaker indicates high 
            levels of interest, active listening, and receptivity.""")
    with c2:
        if st.button("😠 Resistance"): 
            st.error("""RESISTANCE: Tightened lips and a lowered brow signal internal 
            disagreement or a lack of openness to new ideas.""")
        if st.button("🙅‍♂️ Barriers"): 
            st.error("""BARRIERS: Crossing arms can signal a defensive posture or 
            a subconscious need for protection in a social environment.""")
    with c3:
        if st.button("😨 Stress"): 
            st.warning("""STRESS: Raised eyebrows and widened eyes signal that a 
            person feels overwhelmed or threatened by their environment.""")
        if st.button("👤 Diminishment"): 
            st.warning("""DIMINISHMENT: Hunching shoulders or lowering the head 
            signals a lack of confidence or lower perceived social stature.""")
    
    st.subheader("The Social Distance Ruler")
    v = st.slider("Physical Distance (feet):", 1, 15, 5)
    if v <= 3:
        st.success(f"{v} ft: INTIMATE SPACE. Reserved for high-trust bonds.")
    elif v <= 10:
        st.info(f"{v} ft: SOCIAL SPACE. Standard for professional interactions.")
    else:
        st.error(f"{v} ft: PUBLIC SPACE. Typical for formal speaking or strangers.")

    st.divider()
    
    # SECTION II: ASSESSMENT
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # DATA FORMAT: [Question, [Options], Correct_Answer, Explanation]
    data = [
        ["In 'point-light' studies, what specific information allowed observers to identify sex and emotion?", 
         ["The specific patterns of movement", "The static arrangement of dots"], 
         "The specific patterns of movement", 
         """The study proved that the human brain decodes identity and emotion through the
