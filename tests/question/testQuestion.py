import unittest

from quiz_maker.question.Question import Question

# TODO add test of __eq__ method

class TestQuestion(unittest.TestCase):
    __question: Question
    __question_str: str
    __answers: list[str]
    __solution: int

    def setUp(self) -> None:
        self.__question_str = 'Question'
        self.__answers = ['Answer a', 'Answer b', 'Answer c', 'Answer d']
        self.__solution = 0
        self.__question = Question(self.__question_str, self.__answers, self.__solution)

        return super().setUp()
    
    def test_class(self):
        self.__check_class_members()
        self.__check_properties()
        self.__check_setters()
        self.__check_init_errors()
        self.__check_setter_errors()

    def test_setter_solution_out_of_range(self):
        self.__question.solution = 100
        self.assertIsNone(self.__question.solution)

    def test_setter_question_solution_invalid(self):
        self.__question.solution = 3
        self.__question.answers = ['0', '1', '2']
        self.assertIsNone(self.__question.solution)

    
    def __check_class_members(self):
        self.assertIsInstance(self.__question, Question)

        self.assertIsInstance(self.__question.question, str)
        self.assertIsInstance(self.__question.answers, list)
        for answer in self.__question.answers:
            self.assertIsInstance(answer, str)
        self.assertIsInstance(self.__question.solution, int)

    def __check_properties(self):
        self.assertEqual(self.__question.question, self.__question_str) 
        self.assertEqual(self.__question.answers, self.__answers)
        self.assertEqual(self.__question.solution, self.__solution)  
    
    def __check_init_error(self, question, answers, solution, exception: type[BaseException]):
        with self.assertRaises(exception):
            Question(question, answers, solution)

    def __check_init_errors(self):
        self.__check_init_error(1.0, ['str'], 1, TypeError)
        self.__check_init_error('str', 'str', 1, TypeError)
        self.__check_init_error('str', [1], 1, TypeError)
        self.__check_init_error('str', ['str'], 'str', TypeError)

    def __check_setter_question_error(self, question, exception: type[BaseException]):
        with self.assertRaises(exception):
            self.__question.question = question

    def __check_setter_answers_error(self, answers, exception: type[BaseException]):
        with self.assertRaises(exception):
            self.__question.answers = answers

    def __check_setter_solution_error(self, answers, exception: type[BaseException]):
        with self.assertRaises(exception):
            self.__question.answers = answers

    def __check_setter_errors(self):
        self.__check_setter_question_error(1.0, TypeError)
        self.__check_setter_answers_error('str', TypeError)
        self.__check_setter_answers_error([1], TypeError)
        self.__check_setter_solution_error('str', TypeError)

    def __check_setter_question(self, question):
        self.__question.question = question
        self.assertEqual(self.__question.question, question)

    def __check_setter_answers(self, answers):
        self.__question.answers = answers
        self.assertEqual(self.__question.answers, answers)

    def __check_setter_solution(self, solution):
        self.__question.solution = solution
        self.assertEqual(self.__question.solution, solution)

    def __check_setters(self):
        self.__check_setter_question('str')
        self.__check_setter_answers(['str'])
        self.__check_setter_solution(0)