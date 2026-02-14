import streamlit as st
import streamlit.components.v1 as components

# FULL CODE BLOCK - Copy everything from here to the bottom
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #f0f2f6; 
            font-family: -apple-system, sans-serif;
            display: flex; 
            justify-content: center; 
            padding: 20px;
        }
        .card { 
            max-width: 650px; width: 100%; background: white; 
            padding: 30px; border-radius: 15px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        }
        .instruction-box { 
            background-color: #eaf2ff; border-left: 5px solid #1a73e8; 
            padding: 15px; border-radius: 8px; margin-bottom: 20px; 
        }
        .scenario-box { 
            background-color: #fff9e6; padding: 20px; 
            border-radius: 10px; border: 1px solid #ffeeba; margin-bottom: 20px; 
        }
        .icon-container { 
            display: flex; justify-content: space-around; margin: 20px 0; 
        }
        .icon-btn { 
            font-size: 35px; cursor: pointer; border: none; background: none; 
            transition: transform 0.2s; 
        }
        .icon-btn:hover { transform: scale(1.2); }
        .slider-section { margin: 25px 0; text-align: center; }
        .quiz-option { 
            background: #f8f9fa; border: 1px solid #dee2e6; padding: 15px; 
            margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; 
        }
        .quiz-option:hover { background: #e9ecef; }
        .result { 
            display: none; margin-top: 15px; padding: 15px; 
            border-radius: 8px; background: #e6f4ea; color: #1e7e34; 
        }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="margin-top:0;">🕵️ Body Language Lab</h2>

        <div class="instruction-box">
            <strong>📋 Instructions:</strong>
            <ul style="margin: 5px 0 0 20px; padding: 0;">
                <li>Click the <strong>Icons</strong> (🔊, 👀, 📏) to discover specific cues.</li>
                <li>Use the <strong>Slider</strong> to test how physical distance impacts the vibe.</li>
                <li>Select the best analysis in the Quiz section.</li>
            </ul>
        </div>

        <div class="scenario-box">
            <strong>Scenario:</strong> You're interviewing a candidate. They seem confident, but you notice a disconnect between their words and their facial expressions.
        </div>

        <div class="icon-container">
            <button class="icon-btn" onclick="alert('Cue 1: Tone is steady, but feels rehearsed.')">🔊</button>
            <button class="icon-btn" onclick="alert('Cue 2: The eyes are static despite the smiling mouth.')">👀</button>
            <button class="icon-btn" onclick="alert('Cue 3: Subtle leaning away suggests a lack of rapport.')">📏</button>
        </div>

        <div class="slider-section">
            <label><strong>Adjust Physical Distance:</strong></label><br>
            <input type="range" min="1" max
