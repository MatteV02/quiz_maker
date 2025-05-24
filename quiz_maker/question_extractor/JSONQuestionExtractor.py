import json

from quiz_maker.question.Question import Question


def dictToQuestion(dict: dict) -> Question:
    try:
        return Question(dict['question'], dict['answers'], dict['solution'])
    except (KeyError , TypeError):
        raise ValueError('JSON file structure is not conforming to the one the application expects')

class JSONQuestionExtractor:

    def __init__(self) -> None:
        pass

    def read(self, path: str):
        if not isinstance(path, str):
            raise TypeError

        with open(path) as file:
            questions = json.load(
                file,
                object_hook=dictToQuestion
            )
            return questions
        
    