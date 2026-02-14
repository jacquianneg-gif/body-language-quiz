import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()
    
    # --- SECTION I: SIMULATOR (CLICK-TO-REVEAL) ---
    st.header("I. Behavioral Analysis Simulator")
    st.write("Click 'Analyze' to reveal the professional interpretation of each signal.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("😊 JOY")
        if st.button("Analyze Joy"):
            st.success("ANALYSIS: True joy (Duchenne smile) involves involuntary muscle contraction around the eyes.")
            
        st.subheader("🙇‍♂️ THE LEAN")
        if st.button("Analyze The Lean"):
            st.info("ANALYSIS: Leaning the torso forward reduces distance and signals high interest and receptivity.")

    with col2:
        st.subheader("😠 RESISTANCE")
        if st.button("Analyze Resistance"):
            st.error("ANALYSIS: Compressed lips and a lowered brow often signal internal disagreement or cognitive effort.")
            
        st.subheader("🙅‍♂️ BARRIERS")
        if st.button("Analyze Barriers"):
            st.error("ANALYSIS: Arms crossed across the chest acts as a barrier, signaling defensiveness.")

    with col3:
        st.subheader("😨 STRESS")
        if st.button("Analyze Stress"):
            st.warning("ANALYSIS: Widened eyes and raised brows increase visual intake, signaling a threat response.")
            
        st.subheader("👤 DIMINISHMENT")
        if st.button("Analyze Diminishment"):
            st.warning("ANALYSIS: Hunching shoulders (the 'turtle effect') is an attempt to appear smaller and less threatening.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT (WITH FULL EXPLANATIONS) ---
    st.header("II. Comprehensive Assessment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "feedback" not in st.session_state: st.session_state.feedback = None

    # Question Database - Built with short lines to prevent truncation crashes
    qs = []
    qs.append(["In 'point-light' studies, what identifies sex and emotion?", ["Patterns of movement", "Static dots"], "Patterns of movement", "The brain decodes identity through the 'rhythm' of motion, even without a visible body."])
    qs.append(["What do 'tie-signs' refer to in social groups?", ["Cues signaling a relationship", "Dress codes"], "Cues signaling a relationship", "Tie-signs are signals like a hand on a shoulder that inform observers of a specific bond."])
    qs.append(["What skill is linked to social success in children?", ["Reading facial muscles", "Academic facts"], "Reading facial muscles", "Decoding nonverbal cues allows children to navigate social nuances and gain peer acceptance."])
    qs.append(["When a person leans forward, what is the signal?", ["High receptivity", "Boredom"], "High receptivity", "A forward lean reduces distance and signals that the listener is fully engaged and open."])
    qs.append(["Large physical distance often signals what?", ["Lower social stature", "High authority"], "Lower social stature", "Lower-status individuals often maintain distance to avoid appearing as a threat."])
    qs.append(["Define the 'parallel track' of communication.", ["Nonverbal cues with speech", "Two languages"], "Nonverbal cues with speech", "The verbal track handles words, while the parallel nonverbal track handles the emotional truth."])
    qs.append(["Where do men look for reassurance when threatened?", ["Partners/companions", "Strangers"], "Partners/companions", "In stress, individuals glance toward a 'safe' person to gather nonverbal data and support."])
    qs.append(["Why is nonverbal signaling 'automatic'?", ["Involuntary muscles", "Practice"], "Involuntary muscles", "Signals like pupil dilation are driven by the nervous system and are hard to fake."])
    qs.append(["In 'point-light' studies, what happens when dots stop?", ["Figure disappears", "Figure stays"], "Figure disappears",
