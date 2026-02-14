import streamlit as st
import streamlit.components.v1 as components

# The core HTML/CSS/JS for your Interactive Dark Dashboard
dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: 'Segoe UI', sans-serif; padding: 20px; }
        .dashboard-container { max-width: 750px; margin: auto; border: 1px solid #333; border-radius: 20px; padding: 30px; background: #0a0a0a; }
        
        /* Interactive Module Icons */
        .module-bar { display: flex; justify-content: space-between; margin-bottom: 30px; gap: 10px; }
        .module-icon { flex: 1; background: #1a1a1a; border: 1px solid #444; border-radius: 12px; padding: 15px; text-align: center; cursor: pointer; transition: 0.3s; }
        .module-icon:hover { border-color: #007bff; background: #222; }
        .module-icon.active { border-color: #007bff; background: #0d1b2a; }

        /* Scenarios & Instructions */
        .instruction-panel { background: #0d1b2a; border-left: 5px solid #007bff; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9rem; color: #d0d0d0; }
        .scenario-active { background: #1a1a00; border: 1px solid #444400; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* Distance Tool (No jargon) */
        .lab-tool { background: #151515; padding: 25px; border-radius: 15px; border: 1px solid #333; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 20px 0; }
        .distance-label { text-align: center; font-weight: bold; font-size: 1.3rem; color: #007bff; text-transform: uppercase; letter-spacing: 1px; }

        /* Quiz Section */
        .quiz-card { background: #111; border: 1px solid #333; padding: 15px; margin: 12px 0; border-radius: 10px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; transition: 0.2s; }
        .quiz-card:hover { background: #222; border-color: #555; }
        .result-box { display: none; margin-top: 20px; padding: 20px; border-radius: 10px; background: #062010; color: #4ade80; border: 1px solid #166534; }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 1.8rem;">🕵️ Body Language Lab</h1>
            <span style="color: #555; font-size: 0.75
