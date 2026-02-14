import streamlit as st
import streamlit.components.v1 as components

# The complete, unbreakable code for your Black Dashboard Lab
final_app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; padding: 20px; }
        .lab-wrapper { max-width: 700px; margin: auto; border: 1px solid #333; border-radius: 20px; padding: 30px; background: #080808; }
        
        /* Interactive Nav Icons */
        .icon-nav { display: flex; justify-content: space-around; margin-bottom: 30px; }
        .nav-item { background: #1a1a1a; border: 1px solid #444; border-radius: 12px; padding: 15px; width: 60px; text-align: center; cursor: pointer; }
        .nav-item:hover { border-color: #007bff; }

        /* Student Instructions - Restored */
        .instructions-box { background: #0d1b2a; border-left: 5px solid #007bff; padding: 20px; border-radius: 8px; margin-bottom: 25px; }
        .instructions-box h3 { margin: 0 0 10px 0; color: #007bff; font-size: 1.1rem; }
        
        /* Scenario - The Lab Task */
        .scenario-panel { background: #1a1a00; border: 1px solid #333300; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* Social Distance Slider */
        .tool-well { background: #111; padding: 25px; border-radius: 15px; border: 1px solid #222; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 15px 0; }
        .readout { text-align: center; font-weight: bold; color: #007bff; font-size: 1.3rem; text-transform: uppercase; }

        /* Quiz Section */
        .quiz-option { background: #1a1a1a; border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; }
        .quiz-option:hover { background: #252525; }
        .success-msg { display: none; margin-top: 20px; padding: 20px; border-radius: 10px; background: #062010; color: #4ade80; border: 1px solid #166534; }
    </style>
</head>
<body>
    <div class="lab-wrapper">
        <h1 style="margin: 0 0 20px 0;">🕵️ Body Language Lab</h1>

        <div class="icon-nav">
            <div class="nav-item">👁️</div>
            <div class="nav-item">📏</div>
            <div class="nav-item">🎙️</div>
        </div>

        <div class="instructions-box">
            <h3>📋 Student Instructions:</h3>
            <ol style="margin: 0; padding-left: 20px; line-height: 1.5;">
                <li><strong>Analyze:</strong> Read the scenario for behavioral contradictions.</li>
                <li><strong>Interact:</strong> Use the <strong>Social Distance</strong> tool to match the cues.</li>
                <li><strong>Verify:</strong> Complete the quiz based on your lab findings.</li>
            </ol>
        </div>

        <div class="scenario-panel">
            <strong>Active Scenario:</strong> "The subject claims to be 'totally relaxed,' but their vocal pitch has spiked, they have no eye-crinkling during smiles, and they have retreated to about 8 feet away."
        </div>

        <div class="tool-well">
            <label style="color: #666; font-size: 0.8rem;">LAB TOOL: SOCIAL DIST
