import streamlit as st
import streamlit.components.v1 as components

# Restore the dark, interactive dashboard layout
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; padding: 20px; }
        .dashboard { max-width: 800px; margin: auto; border: 1px solid #333; border-radius: 20px; padding: 30px; background: #111111; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        
        /* Interactive Icon Bar */
        .icon-bar { display: flex; justify-content: space-between; margin-bottom: 30px; gap: 15px; }
        .icon-btn { flex: 1; background: #222; border: 1px solid #444; border-radius: 12px; padding: 15px; cursor: pointer; transition: 0.3s; text-align: center; }
        .icon-btn:hover { background: #333; border-color: #00aaff; transform: translateY(-2px); }
        .icon-btn.active { border-color: #00aaff; background: #1a2635; }

        /* Scenarios & Instructions */
        .instruction-box { background: #0d1b2a; border-left: 5px solid #00aaff; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9rem; }
        .scenario-box { background: #1a1a00; border: 1px solid #444400; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* The Slider Section */
        .lab-tool { background: #1a1a1a; padding: 25px; border-radius: 15px; border: 1px solid #333; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #00aaff; margin: 20px 0; }
        .zone-display { text-align: center; font-weight: bold; font-size: 1.2rem; color: #00aaff; text-transform: uppercase; letter-spacing: 1px; }

        /* Quiz Section */
        .quiz-option { background: #222; border: 1px solid #444; padding: 15px; margin: 12px 0; border-radius: 10px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; transition: 0.2s; }
        .quiz-option:hover { background: #2a2a2a; border-color: #666; }
        .feedback { display: none; margin-top: 20px; padding: 20px; border-radius: 10px; background: #062010; color: #4ade80; border: 1px solid #166534; }
    </style>
</head>
<body>
    <div class="dashboard">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 1.8rem; color: #fff;">🕵️ Body Language Lab</h1>
            <span style="color: #666; font-size: 0.8rem; letter-spacing: 1px;">GEMINI + NOTEBOOKLM COLLAB</span>
        </div>

        <div class="icon-bar">
            <div class="icon-btn active">👁️<br><small>FACIAL CUES</small></div>
            <div class="icon-btn">📏<br><small>PROXEMICS</small></div>
            <div class="icon-btn">🎙️<br><small>PARALINGUISTICS</small></div>
        </div>

        <div class="instruction-box">
            <strong style="color: #00aaff;">STUDENT INSTRUCTIONS:</strong>
            <ul style="margin: 8px 0 0 0; padding-left: 20px;">
                <li>Analyze the active scenario for "Parallel Track" contradictions.</li>
                <li>Use the tool below to verify if physical distance matches the verbal tone.</li>
            </ul>
        </div>

        <div class="scenario-box">
            <strong>ACTIVE SCENARIO:</strong> "The candidate says they are 'excited to start,' but their voice is monotone, eyes are scanning the exit, and they have retreated to the far end of the table (approx. 8 feet)."
        </div>

        <div class="lab-tool">
            <label style="color: #888; font-size: 0.9rem;">INTERACTIVE TOOL: DISTANCE ANALYSIS (PROXEMICS)</label>
            <input type="range" min="1" max="4" value="3" oninput="updateZone(this.value)">
            <div id="zone-label" class="zone-display">Social Zone (4 - 12 ft)</div>
        </div>

        <div class="quiz-container">
            <p style="margin-bottom: 15px;"><strong>ANALYSIS CHECK:</strong> Why is the 8-foot distance significant here?</p>
            <button class="quiz-option" onclick="document.getElementById('fb').style.display='block'">
                A) It contradicts the "excited" claim by creating a Social/Public barrier.
            </button>
            <button class="quiz-option" onclick="alert('Incorrect. This distance usually suggests a lack of personal rapport.')">
                B) It shows the candidate is respecting the interviewer's personal space.
            </button>
            
            <div id="fb" class="feedback">
                <strong>VERIFIED RESULT:</strong> Correct. Moving into the "Social Zone" during an interview can signal a desire for psychological distance or defensive posturing.
            </div>
        </div>
    </div>

    <script>
        function updateZone(val) {
            const zones = ["", "Intimate (< 1.5 ft)", "Personal (1.5 - 4 ft)", "Social (4 - 12 ft)", "Public (> 12 ft)"];
            document.getElementById('zone-label').innerText = zones[val];
        }
    </script>
</body>
</html>
"""

# Render the dashboard in Streamlit
components.html(app_code, height=900, scrolling=True)
