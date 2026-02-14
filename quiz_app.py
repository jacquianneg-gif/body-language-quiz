import streamlit as st

def main():
    st.set_page_config(page_title="Body Language", layout="wide")
    st.title("How We Communicate Through Body Language")
    
    st.header("I. BEHAVIOR SIMULATOR")
    st.info("The 'Parallel Track': Nonverbal cues running with speech.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("Joy: Crinkled eyes (Duchenne).")
        if st.button("🙇‍♂️ Lean"): st.info("Lean: High interest/receptivity.")
    with c2:
        if st.button("😠 Anger"): st.error("Anger: Tight lips/lowered brow.")
        if st.button("🙅‍♂️ Fold"): st.error("Fold: Defensive barrier cue.")
    with c3:
        if st.button("😨 Fear"): st.warning("Fear: Raised brows/stress.")
        if st.button("👤 Hunch"): st.warning("Hunch: Signals lower status.")
    
    st.subheader("Social Distance (Tie-Signs)")
    v = st.slider("Feet:", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE.")
    elif v <= 10: st.info(f"{v}ft: SOCIAL.")
    else: st.error(f"{v}ft: PUBLIC.")

    st.divider()
    st.header("II. MASTER QUIZ")
    if "s" not in st.session_state: st.session_state.s = 0
    if "sc" not in st.session_state: st.session_state.sc = 0

    # Shuffled answers (Mixed A and B)
    qs = [
        ("Identify sex in dot studies via?", ["Dots", "Motion"], "Motion"),
        ("What are 'tie-signs'?", ["Bond cues", "Dress"], "Bond cues"),
        ("Success linked to reading?", ["Face muscles", "Math"], "Face muscles"),
        ("Leaning forward signals?", ["Boredom", "Interest"], "Interest"),
        ("Large distance signals?", ["Low status", "High status"], "Low status"),
        ("The 'parallel track' is?", ["Nonverbal", "Speech"], "Nonverbal"),
        ("Threatened men look to?", ["Partners", "Strangers"], "Partners"),
        ("Cues are usually?", ["Automatic", "Manual"], "Automatic"),
        ("No motion, figure?", ["Disappears", "Stays"], "Disappears"),
        ("Cues help navigate?", ["Hierarchies", "Exits"], "Hierarchies")
    ]

    if st.session_state.s < len(qs):
        q, opts, cor = qs[st.session_state.s]
        st.write(f"**Question {st.session_state.s+1}/10: {q}**")
        ans = st.radio("Pick:", opts, key=f"q{st.session_state.s}")
        if st.button("Submit Answer"):
            if ans == cor: 
                st.success("Correct!")
                st.session_state.sc += 1
            else: st.error(f"Wrong. Correct: {cor}")
            st.session_state.s += 1
            st.button("Next")
    else:
        st.balloons(); st.header(f"Score: {st.session_state.sc}/10")
        if st.button("Restart"):
            st.session_state.s = 0; st.session_state.sc = 0; st.rerun()

if __name__ == "__main__":
    main()
