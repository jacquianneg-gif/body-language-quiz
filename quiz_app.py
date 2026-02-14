import streamlit as st
import streamlit.components.v1 as components

# Student Instructions and App Code
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background-color: #f0f2f5; padding: 10px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        .instructions { background-color: #e7f3ff; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 5px solid #1877f2; }
        .instructions h3 { margin-top: 0; color: #0c59b3; font-size: 1rem; }
        .scenario { background: #fff9e6; padding: 15px; border-radius: 8px; border: 1px solid #ffeeba; margin-bottom: 20px; }
        .option { display: block; background: #f8f9fa; padding: 12px; margin: 8px 0; border-radius: 6px; cursor: pointer; border: 1px solid #ddd; }
        .option:hover { background: #e9ecef; }
        .feedback { display: none; margin-top: 15px; padding: 12px; border-radius: 6px; }
        .correct { background: #d4edda; color: #155724; display: block; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🕵️ Body Language Lab</h2>
        
        <div class="instructions">
            <h3>📋 Student Instructions:</h3>
            <ol>
                <li><strong>Read the Scenario:</strong> Analyze the social interaction.</li>
                <li><strong>Identify Cues:</strong> Look for "Parallel Track" signals.</li>
                <li><strong>Analyze:</strong> Select the answer backed by research.</li>
            </ol>
        </div>

        <div class="scenario">
            <strong>Scenario:</strong> You notice a candidate's voice sounds confident, but their eyes aren't "crinkling" when they smile, and they have subtly increased their physical distance.
        </div>

        <div class="question">1. What does the lack of "eye crinkling" suggest?</div>
        <div class="option" onclick="document.getElementById('f').style.display='block'">A) It is likely a "social" or forced smile.</div>
        <div class="option">B) It indicates the candidate is extremely focused.</div>
        
        <div id="f" class="feedback correct">
            <strong>Correct!</strong> Research shows genuine smiles involve involuntary eye-area muscle movement.
        </div>
    </div>
</body>
</html>
"""

# This line tells the Python environment to render the HTML above
components.html(html_code, height=600, scrolling=True)
