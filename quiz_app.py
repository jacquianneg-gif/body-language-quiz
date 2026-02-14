import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    st.divider()
    
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("""**📋 STUDENT INSTRUCTIONS:**
    1. Click buttons to see how signals are interpreted in professional settings.
    2. Use the slider to see how physical space changes social zones.
    3. Complete the 10-question assessment in Section II.""")
    
    st.write("Study the 'Parallel Track'—automatic nonverbal signals running alongside speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 True Joy"): 
            st.success("""TRUE JOY: This is signaled by involuntary muscle contraction 
            around the eyes, which indicates genuine warmth and rapport.""")
        if st.button("🙇‍♂️ The Lean"): 
            st.info("""THE LEAN: Moving the torso toward a speaker indicates high levels 
            of interest, active listening, and receptivity.""")
    with c2:
        if st.button("😠 Resistance"): 
            st.error("""RESISTANCE: Tightened lips and a lowered brow often signal internal 
            disagreement or a lack of openness to new ideas.""")
        if st.button("🙅‍♂️ Barriers"): 
            st.error("""BARRIERS: Crossing arms can signal a defensive posture or a 
            subconscious need for protection in a social environment.""")
    with c3:
        if st.button("😨 Stress"): 
            st.warning("""STRESS: Raised eyebrows and widened eyes signal that a person 
            feels overwhelmed or threatened by their current environment.""")
        if st.button("👤 Diminishment"): 
            st.warning("""DIMINISHMENT: Hunching the shoulders or lowering the head 
            signals a lack of confidence or a lower perceived social stature.""")
    
    st.subheader("The Social Distance Ruler")
    v = st.slider("Physical Distance (feet):", 1, 15, 5)
    if v <= 3:
        st.success(f"{v} ft: INTIMATE SPACE. Reserved for high-trust bonds.")
    elif v <= 10:
        st.info(f"{v} ft: SOCIAL SPACE. Standard for professional/peer interactions.")
    else:
        st.error(f"{v} ft: PUBLIC SPACE. Typical for formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    # DATA FORMAT: [Question, [Options], Correct_Answer, Detailed_Explanation]
    qs = [
        ["In the famous 'point-light' studies, what specific information allowed observers to identify the sex and emotional state of a subject?", 
         ["The specific patterns of movement", "The static arrangement of dots"], 
         "The specific patterns of movement", 
         "The study proved that the human brain decodes identity and emotion through the rhythm and flow of motion, even when no physical body is visible."],
        
        ["What does the research term 'tie-signs' refer to when analyzing human nonverbal behavior in a social group?", 
         ["Specific cues that signal a relationship exists", "The formal dress codes of an organization"], 
         "Specific cues that signal a relationship exists", 
         "Tie-signs are signals like a hand on a shoulder or shared proximity that inform observers of the specific bond or 'tie' between two people."],
        
        ["According to social literacy research, what skill is most closely linked to social success and popularity in children?", 
         ["The ability to read facial muscle movements", "The ability to memorize complex academic facts"], 
         "The ability to read facial muscle movements", 
         "Children who can accurately decode nonverbal 'muscle movements' are better at navigating social nuances, which leads to higher peer acceptance."],
        
        ["When a person leans their torso forward during a conversation, what is the most likely social signal being sent?", 
         ["High levels of receptivity and interest", "General boredom or physical fatigue"], 
         "High levels of receptivity and interest", 
         "A forward lean reduces the distance between speakers and signals that the listener is fully engaged and open to the information being shared."],
        
        ["If a person consistently maintains a large physical distance from others, what does this typically signal about their social stature?", 
         ["A lower perceived social stature", "High levels of authority and social power"], 
         "A lower perceived social stature", 
         "Lower-stature individuals often maintain more distance to avoid appearing as a threat to those with more power or to signal their own vulnerability."],
        
        ["How is the 'parallel track' of communication defined in the context of professional body language?", 
         ["Nonverbal cues that run automatically with speech", "The act of speaking two different languages"], 
         "Nonverbal cues that run automatically with speech", 
         "Communication is two-fold: the 'verbal track' handles the words, while the 'parallel nonverbal track' handles the emotional truth and context."],
        
        ["Based on behavioral studies, where do men typically look for reassurance when they feel socially threatened in a room?", 
         ["Toward their partners or close companions", "Toward the strangers standing
