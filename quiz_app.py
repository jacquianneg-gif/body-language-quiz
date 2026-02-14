import streamlit as st
import streamlit.components.v1 as components

# Restore original white-container dashboard with Student Instructions
app_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #f4f7f9; font-family: sans-serif; display: flex; justify-content: center; padding: 20px; }
        .container { max-width: 600px; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        
        h2 { display: flex; align-items: center; gap: 10px; margin-top: 0; }
        
        .instructions { background-color: #e8f0fe; border-left: 4px solid #1a73e8; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .instructions h4 { margin: 0 0 10px 0; color: #1a73e8; }
        
        .scenario { background-color: #fff9c4; padding: 15px; border-radius: 8px; border: 1px solid #fbc02d; margin-bottom: 20px; }
        
        .option { background: #f8f9fa; border: 1px solid #dee2e6; padding: 12px; margin: 10px 0; border-radius: 6px; cursor: pointer; width: 100%; text-align: left; }
        .option:hover { background: #e9ecef; }
        
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 6px; background: #e6f4ea; color: #1e7e34; border: 1px solid #c3e6
