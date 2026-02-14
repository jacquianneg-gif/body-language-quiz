import streamlit as st
import streamlit.components.v1 as components

# FULL SCRIPT: Includes original grey background, icons, and slider.
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
            font-size: 40px; cursor: pointer; border: none; background: none; 
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
            <ul style="margin: 8px 0 0 20px; padding: 0; line-height: 1.5;">
                <li><strong>Icons:</strong> Click 🔊, 👀, and 📏 below to reveal hidden cues.</li>
                <li><strong>Slider:</strong> Adjust physical distance to see how it impacts the scene.</li>
                <li><strong>Quiz:</strong> Select the correct answer based on your findings.</li>
            </ul>
