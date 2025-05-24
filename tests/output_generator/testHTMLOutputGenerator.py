import unittest

import quiz_maker.output_generator.HTMLOutputGenerator as base

class TestHTMLOutputGenerator(unittest.TestCase):
    __HTMLOutputGenerator: base.HTMLOutputGenerator

    def setUp(self) -> None:
        self.__HTMLOutputGenerator = base.HTMLOutputGenerator()
        
        return super().setUp()
    
    def test_class(self):
        self.__check_class_member()
        pass

    def test_write(self):
        self.__check_wrong_type_arguments()
        # check output with right args

        questions = [
            base.Question(
                'Question 1',
                [
                    'Answer 1',
                    'Answer 2',
                    'Answer 3',
                    'Answer 4'
                ],
                0
            ),
            base.Question(
                'Question 2',
                [
                    'Answer 1',
                    'Answer 2',
                    'Answer 3',
                    'Answer 4'
                ],
                1
            ),
            base.Question(
                'Question 3',
                [
                    'Answer 1',
                    'Answer 2',
                    'Answer 3',
                    'Answer 4'
                ],
                None
            ),
        ]
        path = 'tests/resources/out_test_write.html'

        self.__HTMLOutputGenerator.write(questions, path)

        expected = """<!DOCTYPE html>

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
<div class="question" data-correct="a">
<p>1. Question 1</p>
<input type="radio" name="q1" value="a"> Answer 1<br/>
<input type="radio" name="q1" value="b"> Answer 2<br/>
<input type="radio" name="q1" value="c"> Answer 3<br/>
<input type="radio" name="q1" value="d"> Answer 4<br/>
<span class="feedback">✔️ Correct!</span>
<span class="incorrect">❌ Wrong</span>
</div>
<div class="question" data-correct="b">
<p>2. Question 2</p>
<input type="radio" name="q2" value="a"> Answer 1<br/>
<input type="radio" name="q2" value="b"> Answer 2<br/>
<input type="radio" name="q2" value="c"> Answer 3<br/>
<input type="radio" name="q2" value="d"> Answer 4<br/>
<span class="feedback">✔️ Correct!</span>
<span class="incorrect">❌ Wrong</span>
</div>
<div class="question" data-correct="">
<p>3. Question 3</p>
<input type="radio" name="q3" value="a"> Answer 1<br/>
<input type="radio" name="q3" value="b"> Answer 2<br/>
<input type="radio" name="q3" value="c"> Answer 3<br/>
<input type="radio" name="q3" value="d"> Answer 4<br/>
<span class="feedback">✔️ Correct!</span>
<span class="incorrect">❌ Wrong</span>
</div>
<button onclick="checkAnswers()" type="button">Check Answers</button>
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
        with open(path) as out_file:
            content = out_file.read()
            self.assertEqual(content, expected)


    def __check_class_member(self):
        self.assertTrue(callable(self.__HTMLOutputGenerator.write))

    def __check_wrong_type_arguments(self):
        with self.assertRaises(TypeError):
            self.__HTMLOutputGenerator.write(base.Question('str', ['str'], 0), 'path') # type: ignore
        with self.assertRaises(TypeError):
            self.__HTMLOutputGenerator.write([base.Question('str', ['str'], 0)], 1.0) # type: ignore
        with self.assertRaises(OSError):
            self.__HTMLOutputGenerator.write([base.Question('str', ['str'], 0)], 'non/existing/path')
