import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("How We Communicate Through Body Language")
    
    st.header("I. BEHAVIORAL SIMULATOR")
    st.info("The 'Parallel Track': Automatic signals running with speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes (Duchenne). Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Signals high interest/receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tight lips. Signals resistance/threat.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Signals defensiveness/barrier.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower social stature.")
    
    st.subheader("Social Distance Ruler (Tie-Signs)")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE (High Trust).")
    elif v <= 10: st.info(f"{v}ft: SOCIAL (Peer/Professional).")
    else: st.error(f"{v}ft: PUBLIC (Strangers/Formal).")

    st.divider()
    st.header("II. ASSESSMENT")
    if "s" not in st.session_state: st.session_state.s = 0
    if "sc" not in st.session_state: st.session_state.sc = 0

    qs = [
        ("Identify sex in dot studies via?", ["Movement", "Static dots"], "Movement"),
        ("What are 'tie-signs'?", ["Bond cues", "Dress codes"], "Bond cues"),
        ("Social success linked to?", ["Muscle reading", "Math"], "Muscle reading"),
        ("Leaning forward signals?", ["Interest", "Boredom"], "Interest"),
        ("Large distance signals?", ["Low status", "High status"], "Low status"),
        ("The 'parallel track' is?", ["Nonverbal", "Speech"], "Nonverbal"),
        ("Threatened men look to
