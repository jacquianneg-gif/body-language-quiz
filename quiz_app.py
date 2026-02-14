import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Bridging Nonverbal Theory and Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("""Study the 'Parallel Track'—the automatic nonverbal signals 
    that run simultaneously with spoken words.""")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): 
            st.success("""JOY: Duchenne smile (crinkled eyes). 
            Signals warmth and social success.""")
        if st.button("🙇‍♂️ Lean"): 
            st.info("""LEANING: Torso movement forward indicates 
            high interest and openness to the speaker.""")
    with c2:
        if st.button("😠 Anger"): 
            st.error("""ANGER: Narrowed lips and lowered brow. 
            Signals resistance or a perceived threat.""")
        if st.button("🙅‍♂️ Fold"): 
            st.error("""FOLDING: Crossed arms create a barrier, 
            signaling defensiveness or lack of receptivity.""")
    with c3:
        if st.button("😨 Fear"): 
            st.warning("""FEAR: Raised brows and widened eyes. 
            Signals submissiveness or high stress.""")
        if st.button("👤 Hunch"): 
            st.warning("""HUNCHING: Signals lower social stature 
            and a desire to appear less threatening.""")
    
    st.subheader("The Social Distance Ruler")
    st.caption("""How trust and status dictate physical space, 
    acting as a 'Tie-Sign' to observers.""")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: 
        st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10: 
        st.info(f"{v}ft: SOCIAL ZONE. Standard professional interactions.")
    else: 
        st.error(f"{v}ft: PUBLIC ZONE. Formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step =
