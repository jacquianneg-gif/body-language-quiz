import streamlit as st
import streamlit.components.v1 as components

# FULL, SELF-CONTAINED SCRIPT
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #f0f2f6; 
            font-family: sans-serif;
            display: flex; 
            justify-content: center; 
            padding: 40px 20px;
        }
        .card { 
            max-width: 650px; 
            width: 100%;
            background: white; 
            padding: 40px; 
            border-radius: 16px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
        }
        .instructions { 
            background-color: #eaf2ff; 
            border-left: 4px solid #1a73e8; 
            padding: 20px; 
            border-radius: 8px; 
            margin-bottom: 25px; 
        }
        .instructions h4 { margin: 0 0 10px 0; color: #1a73e8; }
        .scenario { 
            background-color: #fff9e6; 
            padding: 20px; 
            border-radius: 10px; 
            border: 1px solid #ffeeba; 
            margin-bottom: 30px; 
        }
        .option { 
            background: #f8f9fa; 
            border: 1px solid #e9ecef; 
            padding: 18px; 
            margin: 12px 0; 
            border-radius: 10px; 
            cursor: pointer; 
            width: 100%; 
            text-align: left; 
            font-size: 16px;
        }
        .option:hover { background: #f1f3f5; }
        .feedback { 
            display: none; 
            margin-top: 20px; 
            padding: 20px; 
            border-radius: 10px; 
            background: #e6f4ea; 
            color: #1e7e34; 
            border: 1px solid #c3e6cb;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1 style="margin-top:0;">🕵️
