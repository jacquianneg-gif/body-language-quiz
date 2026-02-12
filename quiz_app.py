import streamlit as st

def main():
    st.set_page_config(page_title="Body Language Lab", layout="wide")
    st.title("🧠 The Interactive Body Language Lab")
    
    nav = st.sidebar.radio("Navigation", ["1. Behavioral Visualizer", "2. Master Quiz"])

    if nav == "1. Behavioral Visualizer":
        st.header("🎭 Behavioral Simulator")
        st.info("Reading the 'Parallel Track' of automatic muscle movements—the nonverbal signals that run simultaneously with speech.")
        
        st.markdown("### 🧐 Facial Literacy Trainer")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("😊 Joy"): st.success("JOY: Characterized by crinkled eyes (Duchenne smile). This signals receptivity, warmth, and high social success.")
        with c2:
            if st.button("😠 Anger"): st.error("ANGER: Characterized by tight, narrowed lips and a lowered brow. This signals resistance, threat, or a lack of cooperation.")
        with c3:
            if st.button("😨 Fear"): st.warning("FEAR: Characterized by raised brows and widened eyes. This signals submissiveness, vulnerability, or high stress.")
        
        st.markdown("---")
        st.markdown("### 🧍 Interactive Posture Lab")
        p1, p2, p3 = st.columns(3)
        with p1:
            if st.button("🙇‍♂️ Lean"): st.info("RECEPTIVE: Leaning forward indicates high interest, liking, and an openness to the speaker's ideas.")
        with p2:
            if st.button("🙅‍♂️ Fold"): st.error("RESISTANT: Folded arms create a physical barrier, signaling defensiveness or a desire to close off the interaction.")
        with p3:
            if st.button("👤 Hunch"): st.warning("SUBMISSIVE: Hunching the shoulders and lowering the head signals a desire to look smaller, indicating lower social stature.")
        
        st.markdown("---")
        st.markdown("### 📏 Social Distance Ruler")
        v = st.slider("Distance (feet):", 1, 15, 5)
        if v <= 3: st.success(f"{v}ft: INTIMATE ZONE. Reserved for close relationships and high-trust bonds.")
        elif v <= 10: st.info(f"{v}ft: SOCIAL ZONE. The standard distance for peer-to-peer and professional interactions.")
        else: st.error(f"{v}ft: PUBLIC ZONE. The distance maintained for formal speaking or interactions with strangers.")

    elif nav == "2. Master Quiz":
        st.header("🏆 Master Quiz: Behavioral Science")
        if "step" not in st.session_state: st.session_state.step = 0
        if "score" not in st.session_state: st.session_state.score = 0
        if "show" not in st.session_state: st.session_state.show = False

        qs = [
            ("In the famous 'point-light' dot studies, what was the primary factor that allowed observers to instantly identify a person's sex and emotional state?", 
             ["The color and size of the dots", "The specific patterns of movement and motion"], 
             "The specific patterns of movement and motion", 
             "When the dots were still, they appeared meaningless. However, as soon as they moved, the human brain could identify gender and emotion through motion alone, proving that movement is the key to nonverbal identity."),
            
            ("What does the term 'tie-signs' refer to in the context of nonverbal communication research?", 
             ["The specific way a person dresses for formal events", "Nonverbal cues that signal a specific relationship or bond between two people"], 
             "Nonverbal cues that signal a specific relationship or bond between two people", 
             "Tie-signs are behaviors (like holding hands or standing in an intimate zone) that signal to the world that a nonverbal relationship or 'tie' exists between individuals."),
            
            ("According to social research, a child's popularity among their peers is most closely linked to which specific skill?", 
             ["Their ability to read automatic muscle movements in faces", "Their ability to memorize and recite facts from books"], 
             "Their ability to read automatic muscle movements in faces", 
             "Social success and popularity are highly correlated with 'muscle reading.' Children who can accurately interpret subtle facial cues are better at navigating complex social structures."),
            
            ("When a person leans their torso forward during a conversation, what is the most likely nonverbal signal being sent?", 
             ["They are feeling bored and tired", "They are expressing receptivity, interest, and liking"], 
             "They are expressing receptivity, interest, and liking", 
             "Forward leaning is a universal sign of receptivity. It shows the person is 'leaning into' the conversation and is open to the speaker's influence."),
            
            ("In the study of proxemics, what does maintaining a large physical distance from others typically signal about a person's social status?", 
             ["It signals a lower social stature or lack of power", "It signals a position of high authority and dominance"], 
             "It signals a lower social stature or lack of power", 
             "Research shows that individuals with lower social stature often maintain greater distances or show submissive postures (like hunching) to avoid appearing as a threat to higher-status individuals."),
            
            ("What is meant by the concept of the 'parallel track' in human communication?", 
             ["The nonverbal cues that run automatically and simultaneously with spoken words", "The ability to speak two different languages at the same time"], 
             "The nonverbal cues that run automatically and simultaneously with spoken words", 
             "Communication happens on two tracks: the verbal track (words) and the parallel nonverbal track (muscle movements). High social intelligence requires monitoring both at once."),
            
            ("When men feel socially threatened in a public setting, where do they typically look for nonverbal support?", 
             ["They stare at strangers to establish dominance", "They look toward their partners or close companions"], 
             "They look toward their partners or close companions", 
             "Under stress or threat, men often look to their partners for nonverbal 'tie-signs' and reassurance, seeking a sense of safety within their established bond."),
            
            ("Why is nonverbal signaling described as 'automatic' rather than 'conscious'?", 
             ["Because it occurs without conscious intent or thought", "Because it is a skill that must be learned in a classroom"], 
             "Because it occurs without conscious intent or thought", 
             "Most nonverbal cues are produced by involuntary muscle movements. Because they are automatic, they are often considered more 'honest' than spoken words, which are consciously chosen."),
            
            ("What happens to an observer's perception when 'point-light' dots stop moving?", 
             ["The observer can still see a human figure", "The dots become meaningless and the human figure disappears"], 
             "The dots become meaningless and the human figure disappears", 
             "This illustrates that human perception is finely tuned to movement. Without motion, we lose the 'parallel track' of information that identifies the person."),
            
            ("How do nonverbal cues help individuals navigate social structures and hierarchies?", 
             ["By providing a constant stream of information about status and receptivity", "By helping them find their way through physical structures like buildings"], 
             "By providing a constant stream of information about status and receptivity", 
             "Cues like posture and distance act as a 'social map,' helping individuals understand who is in charge and who is open to interaction within a group hierarchy.")
        ]

        if st.session_state.step < 10:
            q, opts, cor, ex = qs[st.session_state.step]
            st.markdown(f"### Question {st.session_state.step + 1} of 10")
            st.markdown(f"## {q}")
            ans = st.radio("Select the most accurate answer:", opts, key=f"q{st.session_state.step}")
            if st.button("Check My Answer"):
                st.session_state.show = True
                if ans == cor:
                    st.success(f"**CORRECT!** \n\n {ex}")
                    st.session_state.score += 1
                else: 
                    st.error(f"**NOT QUITE.** \n\n {ex}")
            if st.session_state.show and st.button("Move to Next Question ➡️"):
                st.session_state.step += 1
                st.session_state.show = False
                st.rerun()
        else:
            st.balloons()
            st.header(f"Final Assessment Score: {st.session_state.score}/10")
            st.write("Great job! You have completed the Nonverbal Literacy Trainer.")
            if st.button("Restart Quiz"):
                st.session_state.step = 0
                st.session_state.score = 0
                st.rerun()

if __name__ == "__main__":
    main()
