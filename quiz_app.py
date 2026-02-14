import streamlit as st
import streamlit.components.v1 as components

# Minimalist Dark Dashboard - Social Distance Edition
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: sans-serif; padding: 20px; }
        .app-container { max-width: 600px; margin: auto; }
        
        /* Interactive Icons */
        .icon-row { display: flex; justify-content: space-around; margin-bottom: 30px; }
        .icon { background: #1a1a1a; border: 1px solid #333; border-radius: 12px; padding: 15px; width: 60px; text-align: center; cursor: pointer; }
        
        /* Content Boxes */
        .info-box { background: #0a111a; border-left: 4px solid #007bff; padding: 15px; border-radius: 4px; margin-bottom: 20px; font-size: 0.9rem; }
        .scenario-box { background: #1a1a00; border: 1px solid #333300; padding: 20px; border-radius: 8px; margin-bottom: 30px; color: #f1e05a; }

        /* Slider Tool */
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 15px 0; }
        .distance-display { text-align: center; font-weight: bold; color: #007bff; font-size: 1.2rem; margin-bottom: 30px; }

        /* Quiz */
        .option-btn { background: #111; border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; color: #fff; }
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 8px; background: #061a0c; color: #4ade80; border: 1px solid #1a3a23; }
    </style>
</head>
<body>
    <div class="app-container">
        <h1>🕵️ Body Language Lab</h1>

        <div class="icon-row">
            <div class="icon">👁️</div>
            <div class="icon">📏</div>
            <div class="icon">🎙️</div>
        </div>

        <div class="info-box">
            <strong>Student Instructions:</strong>
            <ul style="margin: 5px 0; padding-left: 20px;">
                <li>Read the scenario and adjust the <strong>Social Distance</strong> slider.</li>
                <li>Analyze if the physical distance matches the verbal tone.</li>
            </ul>
        </div>

        <div class="scenario-box">
            <strong>Scenario:</strong> The candidate says they are
