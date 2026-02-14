import streamlit as st

def main():
    st.set_page_config(page_title="Lab", layout="wide")
    st.title("Body Language Lab")
    
    st.header("I. SIMULATOR")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("😊 Joy"): st.success("JOY: Crinkled eyes.")
        if st.button("🙇‍♂️ Lean"): st.info("LEAN: High interest.")
    with c2:
        if st.button("😠 Anger"): st.error("ANGER: Tight lips.")
        if st.button("🙅‍♂️ Fold"): st.error("FOLD: Defensive.")
    with c3:
        if st.button("😨 Fear"): st.warning("FEAR: Raised brows.")
        if st.button("👤 Hunch"): st.warning("HUNCH: Lower status.")
    
    st.subheader("Social Distance Ruler")
    v = st.slider("Feet:", 1, 15, 5)
    if v <= 3: st.success(f"{v}ft: INTIMATE")
    elif v <= 10: st.info(f"{v}ft: SOCIAL")
    else: st.error(f"{v}ft: PUBLIC")

    st.divider()
    st.header("II. QUIZ")
    if "s" not in st.session_state: st.session_state.s = 0
    if "sc" not in st.session_state: st.session_state.sc = 0

    qs = [
        ("Identify sex in dot studies via?", ["Movement", "Color"], "Movement"),
        ("What are 'tie-signs'?", ["Relationship cues", "Dress codes"], "Relationship cues"),
        ("Success linked to reading?", ["Face muscles", "Math"], "Face muscles"),
        ("Leaning forward signals?", ["Interest", "Boredom"], "Interest"),
        ("Large distance signals?", ["Low status", "High status"], "Low status"),
        ("The 'parallel track' is?", ["Nonverbal", "Speech"], "Nonverbal"),
        ("Threatened men look to?", ["Partners", "Strangers"], "Partners"),
        ("Cues are usually?", ["Automatic", "Manual"], "Automatic"),
        ("No motion, figure?", ["Disappears", "Stays"], "Disappears"),
        ("Cues help navigate?", ["Hierarchies", "Exits"], "Hierarchies")
    ]

    if st.session_state.s < len(qs):
        q, opts, cor = qs[st.session_state.s]
        st.write(f"Q {st.session_state.s + 1}: {q}")
        ans = st.radio("Pick:", opts, key=f"q{st.session_state.s}")
        if st.button("Submit"):
            if ans == cor: 
                st.success("Correct!")
                st.session_state.sc += 1
            else: st.error(f"Wrong. Correct: {cor}")
            st.session_state.s += 1
            st.button("Next")
    else:
        st.balloons()
        st.write(f"Score: {st.session_state.sc}/10")
        if st.button("Reset"):
            st.session_state.s = 0
            st.session_state.sc = 0
            st.rerun()

if __name__ == "__main__":
    main()
