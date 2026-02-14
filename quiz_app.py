import streamlit as st
import streamlit.components.v1 as components

# We wrap the entire HTML/CSS/JS in a Python string so the server can render it
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; background-color: #f0f2f5; padding: 10px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        .header { display: flex; align-items: center; margin-bottom: 20px; }
        .instructions { background-color: #e7f3ff; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 5px solid #1877f2; }
        .instructions h3 { margin-top: 0; color: #0c59b3; font-size: 1rem; display: flex; align-items: center; }
        .scenario { background: #fff9e6; padding: 15px; border-radius: 8px; border: 1px solid #ffeeba; margin-bottom: 20px; line-height: 1.5; }
        .question { margin-bottom: 15px; font-weight: 600; }
        .option { display: block; background: #f8f9fa; padding: 12px; margin: 8px 0; border-radius: 6px; cursor: pointer; border: 1px solid #ddd; text-align: left; width: 100%; font-size: 1rem; }
        .option:hover { background: #e9ecef; }
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 6px; font-weight: 500; line-height: 1.4; }
        .correct-box { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2 style="margin:0;">🕵️ Body Language Lab</h2>
        </div>
        
        <div class="instructions">
            <h3>📋 Student Instructions:</h3>
            <ol style="margin: 5px 0; padding-left: 20px;">
                <li><strong>Read the Scenario:</strong> Analyze the social interaction.</li>
                <li><strong>Identify Cues:</strong> Look for "Parallel Track" signals.</li>
                <li><strong>Analyze:</strong> Select the answer backed by research.</li>
            </ol>
        </div>

        <div class="scenario">
            <strong>Scenario:</strong> You notice a candidate's voice sounds confident, but their eyes aren't "crinkling" when they smile, and they have subtly increased their physical distance.
        </div>

        <div class="question">1. What does the lack of "eye crinkling" suggest?</div>
        <button class="option" onclick="showFeedback()">A) It is likely a "social" or forced smile.</button>
        <button class="option" onclick="alert('Try again! Think about involuntary muscle movements.')">B) It indicates the candidate is extremely focused.</button>
        
        <div id="feedback-area" class="feedback correct-box">
            <strong>Correct!</strong> Research shows genuine smiles involve involuntary eye-area muscle movement, whereas "social" smiles often only involve the mouth.
        </div>
    </div>

    <script>
        function showFeedback() {
            document.getElementById('feedback-area').style.display = 'block';
        }
    </script>
</body>
</html>
"""

# This renders the code in your Streamlit/Python environment
components.html(app_code, height=650, scrolling=True)
