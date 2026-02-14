import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("The Professional Body Language Lab")
    st.divider()
    
    # Section I: Simulator
    st.header("I. Behavioral Analysis Simulator")
    st.info("Click buttons to see how signals are interpreted.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("😊 Genuine Smile"): 
            st.success("Signal: Involuntary muscle contraction around eyes.")
        if st.button("🙇‍♂️ Torso Lean"): 
            st.info("Signal: Moving toward a speaker indicates high interest.")
    with col2:
        if st.button("🙅‍♂️ Arm Barrier"): 
            st.error("Signal: Can indicate defensiveness or a need for safety.")
        if st.button("😨 Facial Stress"): 
            st.warning("Signal: Widened eyes indicate feeling overwhelmed.")

    # Section II: Assessment
    st.divider()
    st.header("II. Comprehensive Assessment")
    
    if "step" not in st.session_state: st.session_state.step = 0
    if "score" not in st.session_state: st.session_state.score = 0

    # Data is structured simply to prevent any truncation errors
    questions = [
        ["What identifies sex/emotion in 'point-light' studies?", ["Movement patterns", "Static dots"], "Movement patterns"],
        ["What are 'tie-signs' in social groups?", ["Cues showing a relationship", "Dress codes"], "Cues showing a relationship"],
        ["Which skill is linked to social success in children?", ["Reading facial muscles", "Academic facts"], "Reading facial muscles"],
        ["What does leaning forward usually signal?", ["High interest", "Boredom"], "High interest"],
        ["Large physical distance often signals what?", ["Lower social stature", "High authority"], "Lower social stature"],
        ["Define the 'parallel track' of communication.", ["Nonverbal cues with speech", "Two languages"], "Nonverbal cues with speech"],
        ["Where do men look for reassurance if threatened?", ["Partners/companions", "Strangers"], "Partners/companions"],
        ["Why is nonverbal signaling 'automatic'?", ["Involuntary muscles", "Practice"], "Involuntary muscles"],
        ["What happens in 'point-light' studies when dots stop?", ["Figure disappears", "Figure stays"], "Figure disappears"],
        ["How do nonverbal cues help in social groups?", ["Signal status/receptivity", "Find exits"], "Signal status/receptivity"]
    ]

    if st.session_state.step < len(questions):
        q_text, opts, correct = questions[st.session_state.step]
        st.write(f"### Question {st.session_state.step + 1}")
        st.write(f"**{q_text}**")
        ans = st.radio("Choose one:", opts, key=f"ans_{st.session_state.step}")
        
        if st.button("Submit Answer"):
            if ans == correct:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. The answer is: {correct}")
            st.session_state.step += 1
            st.button("Next Question")
    else:
        st.balloons()
        st.header(f"Final Score: {st.session_state.score} / 10")
        if st.button("Restart"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()

if __name__ == "__main__":
    main()
