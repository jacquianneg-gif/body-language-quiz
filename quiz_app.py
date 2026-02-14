import streamlit as st
import streamlit.components.v1 as components

# Professional Dark Dashboard - Minimalist Lab Edition
lab_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; padding: 20px; }
        .lab-frame { max-width: 650px; margin: auto; border: 1px solid #333; border-radius: 20px; padding: 30px; background: #080808; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
        
        /* Dashboard Icons */
        .icon-nav { display: flex; justify-content: space-between; margin-bottom: 30px; }
        .icon-item { background: #1a1a1a; border: 1px solid #333; border-radius: 12px; padding: 15px; width: 60px; text-align: center; cursor: pointer; transition: 0.2s; }
        .icon-item:hover { border-color: #007bff; background: #222; }

        /* Content Areas */
        .student-guide { background: #0d1b2a; border-left: 5px solid #007bff; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9rem; color: #d0d0d0; }
        .active-scenario { background: #1a1a00; border: 1px solid #333300; padding: 20px; border-radius: 10px; margin-bottom: 30px; color: #f1e05a; line-height: 1.6; }

        /* Slider Tool - No Jargon */
        .interactive-tool { background: #111; padding: 20px; border-radius: 12px; border: 1px solid #222; margin-bottom: 30px; }
        input[type=range] { width: 100%; cursor: pointer; accent-color: #007bff; margin: 15px 0; }
        .distance-readout { text-align: center; font-weight: bold; color: #007bff; font-size: 1.3rem; text-transform: uppercase; }

        /* Quiz Logic */
        .choice-btn { background: #1a1a1a; border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; width: 100%; text-align: left; color: #fff; font-size: 1rem; }
        .choice-
