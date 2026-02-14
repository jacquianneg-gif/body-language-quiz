import streamlit as st
import streamlit.components.v1 as components

# Dark Dashboard with "Social Distance" and verified NotebookLM facts
app_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #e0e0e0; font-family: sans-serif; padding: 15px; }
        .dashboard { max-width: 700px; margin: auto; border: 1px solid #333; border-radius: 12px; padding: 25px; background: #111111; }
        
        /* Interactive Elements */
        .icon-row { display: flex; justify-content: space-around; margin-bottom: 25px; }
        .icon-box { background: #222; border: 1px solid #444; border-radius: 10px; padding: 12px; width: 70px; text-align: center; cursor: pointer; }
        .icon-box:hover { border-color: #1a73e8; }

        /* Scenarios */
        .instruction-tag { background: #0d1b2a; border-left: 4px solid #1a73e8; padding: 12px; border-radius: 6px; margin-bottom: 20px; font-size: 0.9rem; }
        .scenario-tag { background: #1a1a00; border: 1px solid #4d452e; padding: 15px; border-radius: 8px; margin-bottom: 25px; color: #ffeeba; }

        /* The Tool */
        .slider-tool { background: #1a1a1a; padding: 20px; border-radius: 10px; margin-bottom: 25px; border: 1px solid #333; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #1a73e8; }
        .distance-label { text-align: center; font-weight: bold; color: #1a73e8; margin-top: 10px; font-
