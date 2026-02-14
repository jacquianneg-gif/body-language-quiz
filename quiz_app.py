import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    # --- SECTION I: SIMULATOR ---
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("""**📋 STUDENT INSTRUCTIONS:**
1. **Explore Icons:** Click buttons below to reveal how specific signals are interpreted in professional settings.
2. **Distance Ruler:** Use the slider to adjust physical space and observe how interaction zones are classified.
3. **Assessment:** Scroll to Section II to complete the formal 10-question evaluation.""")
    
    st.write("Study the 'Parallel Track'—the automatic nonverbal signals that run alongside spoken words.")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 True Joy"): st.success("TRUE JOY: Characterized by involuntary muscle contraction around the eyes, signaling genuine warmth.")
        if st.button("🙇‍♂️ The Lean"): st.info("THE LEAN: Moving the torso toward a speaker indicates high interest, active listening, and receptivity.")
    with c2:
        if st.button("😠 Resistance"): st.error("RESISTANCE: Tightened lips and a lowered brow signal internal disagreement or a lack of openness.")
        if st.button("🙅‍♂️ Barriers"): st.error("BARRIERS: Crossing arms can signal a defensive posture or a subconscious need for protection.")
    with c3:
        if st.button("😨 Stress"): st.warning("STRESS: Raised eyebrows and widened eyes signal that a person feels overwhelmed by the environment.")
        if st.button("👤 Diminishment"): st.warning("DIMINISHMENT: Hunching shoulders signals a lack of confidence or lower perceived social stature.")
    
    st.subheader("The Social Distance Ruler")
    v = st.slider("Physical Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v} ft: INTIMATE SPACE. Reserved for high-trust bonds and close personal relationships.")
    elif v <= 10: st.info(f"{v} ft: SOCIAL SPACE. The standard distance for professional interactions and peer discussions.")
    else: st.error(f"{v} ft: PUBLIC SPACE. Typical for public speaking or interactions with strangers in formal settings.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT ---
    st.header("II. COMPREHENSIVE ASSESSMENT")
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # Each question and explanation is kept on a single line to prevent truncation errors.
    data = [
        ["In the famous 'point-light' studies, what specific information allowed observers to identify the sex and emotional state of a subject?", ["The specific patterns of movement", "The static arrangement of dots"], "The specific patterns of movement", "The study proved that the human brain decodes identity and emotion through the rhythm and flow of motion, even when no physical body is visible."],
        ["What does the research term 'tie-signs' refer to when analyzing human nonverbal behavior in a social group?", ["Specific cues that signal a relationship exists", "The formal dress codes of an organization"], "Specific cues that signal a relationship exists", "Tie-signs are signals like a hand on a shoulder or shared proximity that inform observers of the specific bond or 'tie' between two people."],
        ["According to social literacy
