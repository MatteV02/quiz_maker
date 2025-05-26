# Quiz Maker

Quiz Maker converts questions in human readable format to an interactive form.  

> [!WARNING]  
> Tested on Python 3.13  
> It may not work on previous versions of Python

---

## CLI

```bash
quiz_maker [-i|--in-file] FILE_INPUT [-o|--out-file] FILE_OUTPUT
```

---

## Input Files

Supported input files:

- JSON files

### JSON

Example of JSON input file.  

> [!NOTE]  
> For now only single solution are supported.  

```json
[
    {
        "question": "Question content",
        "solution": 0,
        "answers": [
            "correct answer",
            "wrong answer 1",
            "wrong answer 2",
            "wrong answer 3"
        ]
    },
    "_comment": "More questions",
]
```

---

## Output files

Supported output files:

- HTML with scripts

### HTML

The interactive form is produced as an HTML page with a JavaScript script to check the correct answers

## Contribute

### Documentation

Application API is available under `API documentation folder`. Each unit of code has its own UML class diagram and Markdown description. Please maintain the documentation up to date while you code.

### Testing environment

The code is produced in a test-driven development fashion. Each code unit has its own unit test under the directory `tests`. `tests` directory mirrors `quiz_maker` module folder and contains a sub-directory `resources` with input tests.  
Python `unittest` framework is used for unit testing.

`tests/integration_test.py` is a simple python script which performs integration testing on the whole project.

Each edit to the original source should pass both unit testing and integration testing before commit.
Each addition should bring unit testing and integration testing for validation purposes.
