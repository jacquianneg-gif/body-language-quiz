import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()
    
    # --- SECTION I: SIMULATOR (IMAGE & WORD DISCOVERY) ---
    st.header("I. Behavioral Analysis Simulator")
    st.write("Click on the behavioral signal to reveal the professional analysis.")
    
    # Discovery Grid
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("😊 **JOY**")
        if st.button("Analyze Joy"):
            st.success("ANALYSIS: True joy is signaled by involuntary muscle contraction around the eyes. This indicates genuine warmth and social rapport.")
        
        st.write("🙇‍♂️ **THE LEAN**")
        if st.button("Analyze The Lean"):
            st.info("ANALYSIS: Moving the torso toward a speaker indicates high levels of interest, active listening, and receptivity.")

    with c2:
        st.write("😠 **RESISTANCE**")
        if st.button("Analyze Resistance"):
            st.error("ANALYSIS: Tightened lips and a lowered brow often signal internal disagreement or a lack of openness to new ideas.")
            
        st.write("🙅‍♂️ **BARRIERS**")
        if st.button("Analyze Barriers"):
            st.error("ANALYSIS: Crossing arms can signal a defensive posture or a subconscious need for protection in a social environment.")

    with c3:
        st.write("😨 **STRESS**")
        if st.button("Analyze Stress"):
            st.warning("ANALYSIS: Raised eyebrows and widened eyes signal that a person feels overwhelmed or threatened by their current environment.")
            
        st.write("👤 **DIMINISHMENT**")
        if st.button("Analyze Diminishment"):
            st.warning("ANALYSIS: Hunching the shoulders or lowering the head signals a lack of confidence or a lower perceived social stature.")

    # --- SECTION II: ASSESSMENT (WITH FULL EXPLANATIONS) ---
    st.divider()
    st.header("II. Comprehensive Assessment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "feedback" not in st.session_state: st.session_state.feedback = None

    # Assessment data - Structured to prevent truncation errors
    qs = [
        ["In 'point-light' studies, what identifies sex and emotion?", ["Patterns of movement", "Static dots"], "Patterns of movement", "The brain decodes identity and emotion through the rhythm of motion, even without a visible body."],
        ["What do 'tie-signs' refer to in social groups?", ["Cues signaling a relationship", "Dress codes"], "Cues signaling a relationship", "Tie-signs are signals like a hand on a shoulder that inform observers of a specific bond between people."],
        ["What skill is linked to social success in children?", ["Reading facial muscles", "Academic facts"], "Reading facial muscles", "Accurately decoding nonverbal 'muscle movements' leads to better social navigation and peer acceptance."],
        ["When a person leans forward, what is the signal?", ["High receptivity", "Boredom"], "High receptivity", "A forward lean reduces distance and signals that the listener is fully engaged and open to the information."],
        ["Large physical distance often signals what?", ["Lower social stature", "High authority"],
