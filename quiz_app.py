import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()
    
    # --- SECTION I: SIMULATOR ---
    st.header("I. Behavioral Analysis Simulator")
    st.write("Examine the signal, then click 'Analyze' to reveal the professional interpretation.")
    
    # We use columns to create the grid layout
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.subheader("😊 JOY")
        if st.button("Analyze Joy"):
            st.success("ANALYSIS: True joy (Duchenne smile) involves involuntary muscle contraction around the eyes.")
            
        st.subheader("🙇‍♂️ THE LEAN")
        if st.button("Analyze The Lean"):
            st.info("ANALYSIS: Leaning the torso forward reduces distance and signals high interest and receptivity.")

    with c2:
        st.subheader("😠 RESISTANCE")
        if st.button("Analyze Resistance"):
            st.error("ANALYSIS: Compressed lips and a lowered brow often signal internal disagreement or cognitive effort.")
            
        st.subheader("🙅‍♂️ BARRIERS")
        if st.button("Analyze Barriers"):
            st.error("ANALYSIS: Arms crossed across the chest acts as a 'barrier' to protect vital organs, signaling defensiveness.")

    with c3:
        st.subheader("😨 STRESS")
        if st.button("Analyze Stress"):
            st.warning("ANALYSIS: Widened eyes and raised brows increase visual intake, signaling a person feels threatened.")
            
        st.subheader("👤 DIMINISHMENT")
        if st.button("Analyze Diminishment"):
            st.warning("ANALYSIS: Hunching shoulders (the 'turtle effect') is an attempt to appear smaller and less threatening.")

    st.divider()
    
    # --- SECTION II: ASSESSMENT ---
    st.header("II. Comprehensive Assessment")
    
    # Initialize session state for the quiz
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "feedback" not in st.session_state: st.session_state.feedback = None

    # We build the question list one by one to prevent code crashes
    qs = []
    
    # Q1
    qs.append([
        "In 'point-light' studies, what allowed observers to identify sex and emotion?",
        ["Patterns of movement", "Static arrangement of dots"],
        "Patterns of movement",
        "The brain decodes identity through the 'rhythm' of motion, even without a visible body."
    ])
    
    # Q2
    qs.append([
        "What do 'tie-signs' refer to in social analysis?",
        ["Cues signaling a relationship exists", "Formal dress codes"],
        "Cues signaling a relationship exists",
        "Tie-signs (like touching or proximity) publicly signal the bond between two people."
    ])
    
    # Q3
    qs.append([
        "What skill is most linked
