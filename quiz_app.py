import streamlit as st
import streamlit.components.v1 as components

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: #f0f2f6; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
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
        h1 { margin-top: 0; font-size: 28px; display: flex; align-items: center; gap: 12px; }
        
        .instructions { 
            background-color: #eaf2ff; 
            border-left: 4px solid #1a73e8; 
            padding: 20px; 
            border-radius: 8px; 
            margin-bottom: 25px; 
        }
        .instructions h4 { margin: 0 0 10px 0; color: #1a73e8; font-size: 18px; }
        .instructions ol { margin: 0; padding-left: 20px; line-height: 1.6; color: #333; }

        .scenario { 
            background-color: #fff9e6; 
            padding: 20px; 
            border-radius: 10px; 
            border: 1px solid #ffeeba; 
            margin-bottom: 30px; 
            line-height: 1.5;
            color: #1a1a1a;
        }

        .question { font-weight: 600; margin-bottom: 15px; font-size: 18px; }
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
            line-height: 1.5;
        }
    </style>
</head>
