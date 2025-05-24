# Quiz maker

Quiz maker takes as input a JSON file which describes how the question is done and outputs an HTML form with a script which can correct the answers.  

> [!WARNING]
> Tested on Python 3.13

## CLI
```bash
quiz -i JSON_FILE_INPUT -o HTML_FILE_OUTPUT
```

## JSON
Example of JSON input file.  

```json
[
    {
        "question": "Question content",
        "solutions": [
            "a"
        ],
        "answers": [
            "correct answer",
            "wrong answer 1",
            "wrong answer 2",
            "wrong answer 3"
        ]
    }
]
```