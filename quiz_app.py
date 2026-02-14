import streamlit as st
import streamlit.components.v1 as components

# Restore the dark, interactive Lab dashboard
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #121212; color: #e0e0e0; font-family: 'Inter', sans-serif; padding: 20px; }
        .dashboard { max-width: 700px; margin: auto; border: 1px solid #333; border-radius: 15px; padding: 25px; background: #1e1e1e; }
        
        /* Header & Icons */
        .header { text-align: center; margin-bottom: 30px; }
        .icon-bar { display: flex; justify-content: space-around; margin-bottom: 25px; }
        .icon-btn { background: #2d2d2d; border: 1px solid #444; border-radius: 12px; padding: 15px; cursor: pointer; transition: 0.3s; color: #fff; width: 80px; text-align: center; }
        .icon-btn:hover { background: #3d3d3d; border-color: #1a73e8; transform: translateY(-3px); }

        /* Instructions & Scenario */
        .instructions { background: #1a222f; border-left: 4px solid #1a73e8; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9rem; }
        .scenario { background: #2a261a; border: 1px solid #4d452e; padding: 15px; border-radius: 8px; margin-bottom: 25px; line-height: 1.5; color: #ffeeba; }

        /* Slider Section */
        .control-panel { background: #252525; padding: 20px; border-radius: 10px; margin-bottom: 25px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #1a73e8; }
        .zone-label { text-align: center; font-weight: bold; color: #1a73e8; margin-top: 10px; }

        /* Quiz Section */
        .quiz-option { background: #2d2d2d; border: 1px solid #444; padding: 12px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-
