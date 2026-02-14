<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Body Language Lab</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f0f2f5; padding: 20px; color: #1c1e21; }
        .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .header { text-align: center; border-bottom: 2px solid #eee; padding-bottom: 15px; margin-bottom: 20px; }
        .instructions { background-color: #e7f3ff; padding: 15px; border-radius: 8px; margin-bottom: 25px; border-left: 5px solid #1877f2; }
        .instructions h3 { margin-top: 0; color: #0c59b3; font-size: 1rem; }
        .scenario { background: #fff9e6; padding: 20px; border-radius: 8px; border: 1px solid #ffeeba; margin-bottom: 25px; line-height: 1.5; }
        .question { margin-bottom: 20px; font-weight: 600; }
        .option { display: block; background: #f8f9fa; padding: 12px; margin: 10px 0; border-radius: 6px; cursor: pointer; border: 1px solid #ddd; transition: 0.2s; }
        .option:hover { background: #e9ecef; }
        .feedback { display: none; margin-top: 15px; padding: 15px; border-radius: 6px; font-weight: 500; }
        .correct { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .incorrect { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        button { background: #1877f2; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-weight: bold; width: 100%; cursor: pointer; }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🕵️ Body Language Lab</h1>
        <p><em>Factual insights via NotebookLM | Designed by Gemini</em></p>
    </div>

    <div class="instructions">
        <h3>📋 Student Instructions:</h3>
        <ol>
            <li><strong>Read the Scenario:</strong> Carefully analyze the social interaction described below.</li>
            <li><strong>Identify the Cues:</strong> Look for "Parallel Track" signals (gestures, distance, micro-expressions).</li>
            <li><strong>Choose the Best Answer:</strong> Use the research data to determine the most likely outcome.</li>
        </ol>
    </div>

    <div class="scenario">
        <strong>The Scenario:</strong> You are watching a job interview. The candidate is answering a difficult question. While their voice sounds confident, you notice their eyes aren't quite "crinkling" when they smile, and they have subtly increased the distance between themselves and the interviewer.
    </div>

    <div id="quiz">
        <div class="question">1. Based on the research, what does the lack of "eye crinkling" during the smile suggest?</div>
        <div class="option" onclick="checkAnswer(this, true, 'Correct! This is often referred to as a \'social smile\' rather than a genuine felt emotion.')">A) It is likely a "social" or forced smile.</div>
        <div class="option" onclick="checkAnswer(this, false, 'Actually, the research suggests that genuine smiles require the involuntary movement of muscles around the eyes.')">B) It indicates the candidate is extremely focused.</div>
        <div class="option" onclick="checkAnswer(this, false, 'Not quite. High confidence is usually paired with more relaxed, genuine facial movements.')">C) It confirms their high level of confidence.</div>

        <div id="feedback" class="feedback"></div>
    </div>
</div>

<script>
    function checkAnswer(element, isCorrect, message) {
        const feedback = document.getElementById('feedback');
        feedback.style.display = 'block';
        feedback.innerHTML = message;
        feedback.className = 'feedback ' + (isCorrect ? 'correct' : 'incorrect');
        
        // Disable other options
        const options = document.querySelectorAll('.option');
        options.forEach(opt => opt.style.pointerEvents = 'none');
    }
</script>

</body>
</html>
