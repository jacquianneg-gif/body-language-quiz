import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.markdown("### Nonverbal Theory & Social Literacy")
    
    st.divider()
    st.header("I. BEHAVIORAL SIMULATOR")
    st.info("The 'Parallel Track': Automatic signals running with speech.")
    
    st.subheader("Facial & Postural Literacy")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes. Signals warmth.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: Signals high interest.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tight lips. Signals threat.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Signals defensiveness.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows. Signals stress.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Signals lower status.")
    
    st.subheader("Proxemics: Social Distance")
    v = st.slider("Distance (feet):", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE (High Trust)")
    elif v <= 10: st.info(f"{v}ft: SOCIAL (Peer/Professional)")
    else: st.error(f"{v}ft: PUBLIC (Formal/Strangers)")

    st.divider()
    st.header("II. ASSESSMENT")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0
    if "show" not in st.session_state: st.session_state.show = False

    qs = [
        ("What identifies sex in dot studies?", ["Movement", "Color"], "Movement", "Motion decodes identity."),
        ("What are 'tie-signs'?", ["Bond cues", "Dress codes"], "Bond cues", "They signal a relationship."),
        ("Success is linked to reading...", ["Facial muscles", "Math"], "Facial muscles", "Reading cues leads to popularity."),
        ("Leaning forward signals...", ["Interest", "Boredom"], "Interest", "Shows receptivity."),
        ("Large distance signals...", ["Low status", "High status"], "Low status", "Distance avoids appearing as a threat."),
        ("The 'parallel track' is...", ["Nonverbal cues", "Dual speech"], "Nonverbal cues", "Runs with spoken words."),
        ("Threatened men look to...", ["Partners", "Strangers"], "Partners", "Seeking reassurance."),
        ("Nonverbal cues are...", ["Automatic", "Manual"], "Automatic", "Involuntary muscle movements."),
        ("Dots stop moving, figure...", ["Disappears", "Stays"], "Disappears", "Brain needs motion to see."),
        ("Cues help navigate...", ["Hierarchies", "Exits"], "Hierarchies", "Signals social maps.")
    ]

    if st.session_state.step < len(qs):
        q, opts, cor, ex = qs[st.session_state.step]
        st.write(f"**Question {st.session_state.step + 1}/10: {q}**
