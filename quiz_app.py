import streamlit as st
import streamlit.components.v1 as components

# Final Dark Lab Version with Student Instructions
dashboard_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: sans-serif; padding: 20px; }
        .lab-container { max-width: 700px; margin: auto; border: 1px solid #333; border-radius: 15px; padding: 30px; background: #0a0a0a; }
        
        /* Module Icons */
        .icon-nav { display: flex; justify-content: space-around; margin-bottom: 30px; }
        .icon-btn { background: #1a1a1a; border: 1px solid #444; border-radius: 10px; padding: 15px; width: 60px; text-align: center; cursor: pointer; }

        /* Student Instructions - Blue Box */
        .instructions-panel { background: #0d1b2a; border-left: 5px solid #007bff; padding: 20px; border-radius: 8px; margin-bottom: 25px; }
        .instructions-panel h3 { margin-top: 0; color: #007bff; font-size: 1.1rem; }
        
        /* Scenario - Yellow Box */
        .scenario-panel { background: #1a1a00; border: 1px solid #444400; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* Social Distance Tool */
        .slider-box { background: #111; padding: 25px; border-radius: 12px; border: 1px solid #222; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 15px 0; }
        .distance-readout { text-align: center; font-weight: bold; color: #007bff; font-size: 1.2rem; text-transform: uppercase; }

        /* Quiz Section */
        .quiz-card { background: #1a1a1a; border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; }
        .quiz-card:hover { background: #222; border-color: #555; }
        .correct-box { display: none; margin-top: 20px; padding: 20px; border-radius: 10px; background: #062010; color: #4ade80; border: 1px solid #166534; }
    </style>
</head>
<body>
    <div class="lab-container">
        <h1 style="margin-top:0;">🕵️ Body Language Lab</h1>

        <div class="icon-nav">
            <div class="icon-btn">👁️</div>
            <div class="icon-btn">📏</div>
            <div class="icon-btn">🎙️</div>
        </div>

        <div class="instructions-panel">
            <h3>📋 Student Instructions:</h3>
            <ol style="margin: 0; padding-left: 20px;">
                <li><strong>Read the Scenario:</strong> Look for contradictions in physical cues.</li>
                <li><strong>Use the Tool:</strong>
