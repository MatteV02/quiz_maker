import subprocess


def check_return_code(command: str, expected: int):
    result = subprocess.run(command.split(' '))
    assert result.returncode == expected, command

if __name__ == '__main__':     
    check_return_code('python -m quiz_maker.main -i tests/resources/non-existing.json -o tests/resources/non-existing.html', 1)

    check_return_code('python -m quiz_maker.main -i tests/resources/twenty_questions.json -o wrong/path/file.json', 1)

    check_return_code('python -m quiz_maker.main -i tests/resources/wrong_format.json -o tests/resources/wrong_format.html', 1)
            
    check_return_code('python -m quiz_maker.main -i tests/resources/not_conforming/wrong_answers_type.json -o tests/resources/not_conforming/wrong_answers_type.html', 1)
        
    check_return_code('python -m quiz_maker.main -i tests/resources/one_question.json -o tests/resources/one_question.html', 0)

    check_return_code('python -m quiz_maker.main -i tests/resources/no_questions.json -o tests/resources/no_question.html', 0)
        
    check_return_code('python -m quiz_maker.main -i tests/resources/twenty_questions.json -o tests/resources/twenty_questions.html', 0)

