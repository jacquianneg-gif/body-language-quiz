import streamlit as st
import streamlit.components.v1 as components

# FULL COMPLETE CODE
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #f0f2f6; font-family: sans-serif; display: flex; justify-content: center; padding: 20px; }
        .card { max-width: 600px; width: 100%; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .instructions { background-color: #eaf2ff; border-left: 5px solid #1a73e8; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        .scenario { background-color: #fff9e6; padding: 15px; border-radius: 10px; border: 1px solid #ffeeba; margin-bottom: 20px; }
        .icon-row { display: flex; justify-content: space-around; margin: 25px 0; }
        .icon-btn { font-size: 45px; cursor: pointer; border: none; background: none; transition: transform 0.2s; }
        .icon-btn:hover { transform: scale(1.2); }
        .slider-box { margin: 30px 0; text-align: center; }
        .quiz-option { background: #f8f9fa; border: 1px solid #dee2e6; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; font-size: 16px; }
        .quiz-option:hover { background: #e9ecef; }
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 8px; background: #e6f4ea; color: #1e7e34; border: 1px solid #c3e6cb; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="margin-top:0;">🕵️ Body Language Lab</h2>

        <div class="instructions">
            <strong>📋 Student Instructions:</strong>
            <ul style="margin: 5px 0 0 20px; padding: 0;">
                <li>Click the <b>Icons</b> (🔊, 👀, 📏) to reveal specific behavioral cues.</li>
                <li>Adjust the <b>Slider</b> to test how physical distance affects the scene.</li>
                <li>Choose the correct answer in the quiz to complete the lab.</li>
            </ul>
        </div>

        <div class="scenario">
            <b>Scenario:</b> You are interviewing a candidate. Their verbal answers are flawless, but you sense a disconnect in their physical presence.
        </div>

        <div class="icon-row">
            <button class="icon-btn" onclick="alert('Audio Cue: Tone is steady but feels rehearsed and lacks natural warmth.')">🔊</button>
            <button class="icon-btn" onclick="alert('Visual Cue: The smile is static; the muscles around the eyes are not moving.')">👀</button>
            <button class="icon-btn" onclick="alert('Barrier Cue: The candidate has placed their briefcase between you.')">📏</button>
        </div>

        <div class="slider-box">
            <label><b>Physical Distance (Proximity):</b></label><br><br>
            <input type="range" min="1" max="100" value="70" style="width:90%;">
            <div style="display:flex; justify-content:space-between; width:90%; margin:auto; font-size:12px; color:#666;">
                <span>Intimate</span><span>Social Zone</span><span>Public</span>
            </div>
        </div>

        <hr style="border:0; border-top:1px solid #eee;">
        <p><b>Analysis: What does the lack of eye movement during the smile suggest?</b></p>
        
        <button class="quiz-option" onclick="document.getElementById('fb').style.display='block'">
            A) It is likely a forced or "social" smile.
        </button>
        <button class="quiz-option" onclick="alert('Try again! Think about involuntary vs. voluntary muscle movements.')">
            B) It indicates the candidate is extremely focused.
        </button>

        <div id="fb" class="feedback">
            <b>Correct!</b> Genuine (Duchenne) smiles require involuntary contraction of the muscles around the eyes.
        </div>
    </div>
</body>
</html>
"""

components.html(app_code, height=900, scrolling=True)
