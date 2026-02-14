import streamlit as st
import streamlit.components.v1 as components

# Triple quotes MUST start and end the block to keep the HTML safe from Python
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; background-color: #f8f9fa; padding: 15px; }
        .lab-card { max-width: 650px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
        .instructions { background-color: #eef6ff; padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 6px solid #1a73e8; }
        .instructions h3 { margin-top: 0; color: #1a73e8; font-size: 1.1rem; }
        .scenario-box { background: #fffdf2; padding: 20px; border-radius: 10px; border: 1px solid #ffeeba; margin-bottom: 25px; line-height: 1.6; }
        .question-text { font-weight: 600; margin-bottom: 15px; font-size: 1.05rem; }
        .btn { display: block; width: 100%; text-align: left; padding: 15px; margin: 10px 0; border: 1px solid #e0e0e0; border-radius: 8px; background: white; cursor: pointer; transition: 0.2s; font-size: 1rem; }
        .btn:hover { background: #f1f3f4; border-color: #bdc1c6; }
        .feedback { display: none; margin-top: 20px; padding: 20px; border-radius: 8px; font-weight: 500; line-height: 1.5; }
        .correct { background: #e6f4ea; color: #137333; border: 1px solid #ceead6; }
    </style>
</head>
<body>
    <div class="lab-card">
        <h2 style="margin-top:0;">🕵️ Body Language Lab</h2>
        
        <div class="instructions">
            <h3>📋 Student Instructions:</h3>
            <ol style="margin: 0; padding-left: 20px;">
                <li><strong>Read the Scenario:</strong> Analyze the social interaction.</li>
                <li><strong>Identify Cues:</strong> Look for "Parallel Track" signals.</li>
                <li><strong>Analyze:</strong> Select the answer backed by research.</li>
            </ol>
        </div>

        <div class="scenario-box">
            <strong>Scenario:</strong> You notice a candidate's voice sounds confident, but their eyes aren't "crinkling" when they smile, and they have subtly increased their physical distance.
        </div>

        <div class="question-text">1. What does the lack of "eye crinkling" suggest?</div>
        
        <button class="btn" onclick="document.getElementById('correct-feedback').style.display='block'">A) It is likely a "social" or forced smile.</button>
        <button class="btn" onclick="alert('Think about involuntary muscle movements! Try again.')">B) It indicates the candidate is extremely focused.</button>
        
        <div id="correct-feedback" class="feedback correct">
            <strong>Correct!</strong> Research shows genuine smiles involve involuntary eye-area muscle movement.
        </div>
    </div>
</body>
</html>
"""

# This displays the HTML block we just created
components.html(html_content, height=750, scrolling=True)
