import streamlit as st
import streamlit.components.v1 as components

# SINGLE, COMPLETE, WORKING CODE BLOCK
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #f0f2f6; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex; 
            justify-content: center; 
            padding: 40px 20px;
        }
        .lab-card { 
            max-width: 600px; width: 100%; background: white; 
            padding: 40px; border-radius: 20px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
        }
        h2 { color: #1e293b; margin-top: 0; text-align: center; }
        .subtitle { text-align: center; color: #64748b; font-size: 0.9em; margin-bottom: 30px; }
        .scenario-text { 
            background-color: #f8fafc; padding: 20px; 
            border-radius: 12px; border: 1px solid #e2e8f0; 
            margin-bottom: 30px; line-height: 1.6; color: #334155;
        }
        .interaction-area { display: flex; justify-content: space-around; margin: 40px 0; }
        .icon-btn { 
            font-size: 50px; cursor: pointer; border: none; background: none; 
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
            transition: transform 0.2s ease;
        }
        .icon-btn:hover { transform: translateY(-5px) scale(1.1); }
        .slider-container { margin: 40px 0; text-align: center; }
        input[type=range] { width: 100%; cursor: pointer; }
        .quiz-option { 
            background: white; border: 2px solid #f1f5f9; padding: 18px; 
            margin: 12px 0; border-radius: 12px; cursor: pointer; width: 100%; 
            text-align: left; font-size: 16px; transition: all 0.2s;
        }
        .quiz-option:hover { border-color: #3b82f6; background: #eff6ff; }
        .success-box { 
            display: none; margin-top: 20px; padding: 20px; 
            border-radius: 12px; background: #f0fdf4; color: #166534; 
            border: 1px solid #bbf7d0; font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="lab-card">
        <h2>🕵️ Body Language Lab</h2>
        <p class="subtitle">Click the icons and adjust the slider to investigate the candidate.</p>

        <div class="scenario-text">
            <strong>The Scene:</strong> You
