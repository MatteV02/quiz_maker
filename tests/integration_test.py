import subprocess


def check_return_code(command: str, expected: int):
    result = subprocess.run(
        command.split(' '),
        stdout=subprocess.DEVNULL
    )
    assert result.returncode == expected, command

if __name__ == '__main__':     
    # wrong arguments
    # 1. wrong input tag
    check_return_code('python -m quiz_maker.main -j tests/resources/one_question.json -o tests/resources/one_question.html', 1)
    # 2. wrong output tag
    check_return_code('python -m quiz_maker.main -i tests/resources/one_question.json -w tests/resources/one_question.html', 1)
    # 3. only input tag
    check_return_code('python -m quiz_maker.main -i tests/resources/one_question.json', 1)
    # 4. only output tag
    check_return_code('python -m quiz_maker.main -o tests/resources/one_question.html', 1)
    # 5. non existing input file
    check_return_code('python -m quiz_maker.main -i tests/resources/non-existing.json -o tests/resources/non-existing.html', 1)
    # 6. non existing output path
    check_return_code('python -m quiz_maker.main -i tests/resources/twenty_questions.json -o wrong/path/file.json', 1)
    # 7. unsupported format input file
    check_return_code('python -m quiz_maker.main -i tests/resources/wrong_format.json -o tests/resources/wrong_format.html', 2)
    # 8. not conforming input file   
    check_return_code('python -m quiz_maker.main -i tests/resources/not_conforming/wrong_answers_type.json -o tests/resources/not_conforming/wrong_answers_type.html', 3)
    
    # correct arguments
    # 1. one question json file
    check_return_code('python -m quiz_maker.main -i tests/resources/one_question.json --out-file tests/resources/one_question.html', 0)
    # 2. no questions json file
    check_return_code('python -m quiz_maker.main --in-file tests/resources/no_questions.json -o tests/resources/no_question.html', 0)
    # 3. twenty questions json file 
    check_return_code('python -m quiz_maker.main -i tests/resources/twenty_questions.json -o tests/resources/twenty_questions.html', 0)
