
import streamlit as st
import streamlit.components.v1 as components

# FULL UNBROKEN CODE BLOCK
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #f0f2f6; 
            font-family: sans-serif;
            display: flex; 
            justify-content: center; 
            padding: 20px;
        }
        .lab-card { 
            max-width: 650px; width: 100%; background: white; 
            padding: 30px; border-radius: 15px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        }
        .instruction-header { 
            background-color: #eaf2ff; border-left: 5px solid #1a73e8; 
            padding: 15px; border-radius: 8px; margin-bottom: 20px; 
        }
        .scenario-box { 
            background-color: #fff9e6; padding: 20px; 
            border-radius: 10px; border: 1px solid #ffeeba; margin-bottom: 20px; 
        }
        .interactive-zone { 
            display: flex; justify-content: space-around; margin: 30px 0; 
        }
        .icon-btn { 
            font-size: 45px; cursor: pointer; border: none; background: none; 
            transition: transform 0.2s; 
        }
        .icon-btn:hover { transform: scale(1.2); }
        .slider-wrap { margin: 30px 0; text-align: center; }
        .quiz-option { 
            background: #f8f9fa; border: 1px solid #dee2e6; padding: 15px; 
            margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; 
        }
        .quiz-option:hover { background: #e9ecef; }
        .correct-msg { 
            display: none; margin-top: 15px; padding: 15px; 
            border-radius: 8px; background: #e6f4ea; color: #1e7e34; 
        }
    </style>
</head>
<body>
    <div class="lab-card">
        <h2 style="margin-top:0;">🕵️ Body Language Lab</h2>

        <div class="instruction-header">
            <strong>📋 Student Instructions:</strong>
            <p style="margin: 5px 0;">Use the tools below to investigate the candidate:</p>
            <ul style="margin: 0; padding-left: 20px; font-size: 14px;">
                <li>Click the <strong>Icons</strong> (🔊, 👀, 📏) to hear/see specific cues.</li>
                <li>Use the <strong>Slider</strong> to test physical distance.</li>
                <li>Select the correct analysis in the Quiz.</li>
            </ul>
        </div>

        <div class="scenario-box">
            <strong>Scenario:</strong> You are interviewing a candidate. Their verbal answers are perfect, but their non-verbal cues seem contradictory.
        </div>

        <div class="interactive-zone">
            <button class="icon-btn" onclick="alert('Audio Cue: Tone is rehearsed and lacks emotional variance.')">🔊</button>
            <button class="icon-btn" onclick="alert('Visual Cue: The smile is static and does not reach the eyes.')">👀</button>
            <button class="icon-btn" onclick="alert('Spatial Cue: The candidate is subtly leaning away.')">📏</button>
        </div>

        <div class="slider-wrap">
            <label><strong>Testing Proximity (Physical Distance):</strong></label><br>
            <input type="range" min="1" max="100" value="60" style="width:90%;">
            <div style="display:flex; justify-content:space-between; width:90%; margin:auto; font-size:12px; color:#666;">
                <span>Intimate</span><span>Social Zone</span><span>Public</span>
            </div>
        </div>

        <hr style="border: 0; border-top: 1px solid #eee;">

        <p><strong>Quiz: What indicates the candidate’s smile is likely forced?</strong></p>
        <button class="quiz-option" onclick="document.getElementById('success').style.display='block'">
            A) The lack of involuntary "crinkling" around the eyes.
        </button>
        <button class="quiz-option" onclick="alert('Try again. Focus on the eye muscles.')">
            B) The candidate is holding the smile for too long.
        </button>

        <div id="success" class="correct-msg">
            <strong>Correct!</strong> A genuine (
