import streamlit as st
import streamlit.components.v1 as components

# Complete code for the Dark Dashboard with Student Instructions
app_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: sans-serif; padding: 20px; }
        .dashboard-frame { max-width: 700px; margin: auto; border: 1px solid #333; border-radius: 15px; padding: 30px; background: #0a0a0a; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        
        /* Interactive Module Icons */
        .icon-nav { display: flex; justify-content: space-around; margin-bottom: 30px; }
        .icon-btn { background: #1a1a1a; border: 1px solid #444; border-radius: 10px; padding: 15px; width: 60px; text-align: center; cursor: pointer; transition: 0.3s; }
        .icon-btn:hover { border-color: #007bff; background: #222; }

        /* Student Instructions - Blue Box */
        .instruction-box { background: #0d1b2a; border-left: 5px solid #007bff; padding: 20px; border-radius: 8px; margin-bottom: 25px; }
        .instruction-box h3 { margin-top: 0; color: #007bff; font-size: 1.1rem; }
        
        /* Scenario - Yellow Box */
        .scenario-box { background: #1a1a00; border: 1px solid #444400; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* Social Distance Slider */
        .tool-section { background: #111; padding: 25px; border-radius: 12px; border: 1px solid #222; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 15px 0; }
        .distance-display { text-align: center; font-weight: bold; color: #007bff; font-size: 1.2rem; text-transform: uppercase; }

        /* Quiz area */
        .quiz-option { background: #1a1a1a; border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; }
        .quiz-option:hover { background:
