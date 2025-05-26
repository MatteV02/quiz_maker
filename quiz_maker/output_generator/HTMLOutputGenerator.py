from pathlib import Path
from quiz_maker.question.Question import Question


class HTMLOutputGenerator:
    _HTMLBoilerPlateHeader: str = """<!DOCTYPE html>

<html lang="it">
<head>
<meta charset="utf-8"/>
<title>Quiz</title>
<style>
    body {
    font-family: Arial, sans-serif;
    max-width: 900px;
    margin: 40px auto;
    padding: 0 20px;
    background-color: #f9f9f9;
    color: #222;
    }
    h1 {
    color: #004080;
    text-align: center;
    margin-bottom: 30px;
    }
    .question {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 15px 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    .question p {
    margin: 0 0 10px;
    font-weight: bold;
    }
    input[type="radio"] {
    margin-bottom: 8px;
    }
    button {
    display: block;
    margin: 30px auto;
    padding: 12px 24px;
    font-size: 16px;
    background-color: #004080;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    }
    button:hover {
    background-color: #003060;
    }
    .feedback, .incorrect {
    font-weight: bold;
    display: none;
    }
    .feedback { color: green; }
    .incorrect { color: red; }
    #results {
    background: #e8f0ff;
    padding: 20px;
    margin-top: 30px;
    border-radius: 8px;
    border: 1px solid #bcd;
    }
</style>
</head>
<body>
<h1>Quiz</h1>
<form id="quizForm">
"""
    
    _HTMLBoilerPlateFooter: str = """<button onclick="checkAnswers()" type="button">Check Answers</button>
</form>
<div class="results" id="results"></div>
<script>
    function checkAnswers() {
    const questions = document.querySelectorAll('.question');
    let score = 0;
    let results = '';
    questions.forEach((q, index) => {
        const selected = q.querySelector('input:checked');
        const correct = q.dataset.correct;
        const feedback = q.querySelector('.feedback');
        const incorrect = q.querySelector('.incorrect');
        if (selected) {
        if (selected.value === correct) {
            feedback.style.display = 'inline';
            incorrect.style.display = 'none';
            score++;
            results += `<p><strong>Question ${index + 1}:</strong> Correct</p>`;
        } else {
            feedback.style.display = 'none';
            incorrect.style.display = 'inline';
            results += `<p><strong>Question ${index + 1}:</strong> Wrong</p>`;
        }
        } else {
        results += `<p><strong>Question ${index + 1}:</strong> Not answered</p>`;
        }
    });
    results += `<p><strong>Score:</strong> ${score}/${questions.length}</p>`;
    document.getElementById("results").innerHTML = results;
    }
</script>
</body>
</html>"""

    def __generate(self, questions: list[Question]):
        webpage = self._HTMLBoilerPlateHeader

        for (question_index, question) in enumerate(questions):
            webpage += self.__question_to_HTML(question, question_index + 1)

        webpage += self._HTMLBoilerPlateFooter

        return webpage

    def __question_to_HTML(self, question: Question, index: int) -> str:
        index_to_letter = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
        }
        question_html = ""
        question_html += "<div class=\"question\" data-correct=\""
        if question.solution is not None:
            question_html += str(index_to_letter[question.solution])
        question_html += "\">\n"
        question_html += "<p>"
        question_html += f'{index}. '
        question_html += str(question.question)
        question_html += "</p>\n"
        for (answer_idx, answer) in enumerate(question.answers):
            question_html += f"<input type=\"radio\" name=\"q{index}\" value=\"{index_to_letter[answer_idx]}\"> "
            question_html += answer
            question_html += '<br/>\n'
        question_html += '<span class="feedback">✔️ Correct!</span>\n<span class="incorrect">❌ Wrong</span>\n</div>\n'
        return question_html
    
    def write(self, questions: list[Question], out_file_path_str: str):
        out_file_path = Path(out_file_path_str)

        with out_file_path.open('w', encoding="utf-8") as out_file:
            out_file.write(self.__generate(questions))