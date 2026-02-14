import streamlit as st
import streamlit.components.v1 as components

# FULL COMPLETE CODE BLOCK
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #f0f2f6; font-family: sans-serif; display: flex; justify-content: center; padding: 20px; }
        .card { max-width: 600px; width: 100%; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .instruction-box { background-color: #eaf2ff; border-left: 5px solid #1a73e8; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        .scenario { background-color: #fff9e6; padding: 15px; border-radius: 10px; border: 1px solid #ffeeba; margin-bottom: 20px; font-style: italic; }
        .icon-row { display: flex; justify-content: space-around; margin: 25px 0; }
        .icon-btn { font-size: 40px; cursor: pointer; border: none; background: none; transition: transform 0.2s; }
        .icon-btn:hover { transform: scale(1.2); }
        .slider-section { margin: 30px 0; text-align: center; }
        .quiz-option { background: #f8f9fa; border: 1px solid #dee2e6; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; }
        .quiz-option:hover { background: #e9ecef; }
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 8px; background: #e6f4ea; color: #1e7e34; border: 1px solid #c3e6cb; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="margin-top:0;">🕵️ Body Language Lab</h2>

        <div class="instruction-box">
            <strong>📋 Student Instructions:</strong>
            <ul style="margin: 5px 0 0 20px; padding: 0;">
                <li>Click the <b>Icons</b> (🔊, 👀, 📏) to find specific behavioral cues.</li>
                <li>Use the <b>Slider</b> to test how physical distance changes the dynamic.</li>
                <li>Select the correct
