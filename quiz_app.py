import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    st.markdown("### Interactive Behavioral Research Lab")
    
    st.divider()
    st.header("I. BEHAVIORAL ANALYSIS SIMULATOR")
    st.info("Study the 'Parallel Track'—automatic signals.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"):
            st.success("JOY: Crinkled eyes (Duchenne). Signals warmth.")
        if st.button("🙇‍♂️ Lean"):
            st.info("LEAN: Forward movement indicates high interest.")
    with c2:
        if st.button("😠 Anger"):
            st.error("ANGER: Tight lips and lowered brow. Signals resistance.")
        if st.button("🙅‍♂️ Fold"):
            st.error("FOLD: Crossed arms create a barrier or defensiveness.")
    with c3:
        if st.button("😨 Fear"):
            st.warning("FEAR: Raised brows and widened eyes. Signals stress.")
        if st.button("👤 Hunch"):
            st.warning("HUNCH: Signals lower social stature or vulnerability.")
    
    st.subheader("Social Distance Ruler")
    st.caption("How status dictates physical space ('Tie-Signs').")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3:
        st.success(f"{v}ft: INTIMATE ZONE. High-trust bonds.")
    elif v <= 10:
        st.info(f"{v}ft: SOCIAL ZONE. Standard peer/professional space.")
    else:
        st.error(f"{v}ft: PUBLIC ZONE. Formal speaking or strangers.")

    st.divider()
    st.header("II. COMPREHENSIVE ASSESSMENT")
    
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "show" not in st.session_state:
        st.session_state.show = False

    # Vertical data structure to prevent editor cutoff
    qs = [
        {
            "q": "What allowed observers to identify sex and emotion in 'point-light' studies?",
            "o": ["Static dot patterns", "The specific patterns of movement"],
            "c": "The specific patterns of movement",
            "e": "Motion decodes identity. Without it, the figure disappears."
