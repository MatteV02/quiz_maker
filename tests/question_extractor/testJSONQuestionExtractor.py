import unittest

import quiz_maker.question_extractor.JSONQuestionExtractor as base


class TestJSONQuestionExtractor(unittest.TestCase):
    __JSONQuestionExtractor: base.JSONQuestionExtractor

    def setUp(self) -> None:
        self.__JSONQuestionExtractor = base.JSONQuestionExtractor()
        return super().setUp()
    
    def test_class(self):
        self.__check_class_members()

    def test_read(self):
        self.__check_argument_not_a_string()
        self.__check_file_not_existing()
        self.__check_file_wrong_formatting()
        self.__check_files_not_conforming()
        
        # test with one_question.json
        questions = self.__JSONQuestionExtractor.read('tests/resources/one_question.json')
        self.assertEqual(
            questions, [
                base.Question(
                    'Question 1', 
                    [
                        'Answer 1',
                        'Answer 2',
                        'Answer 3',
                        'Answer 4',
                    ], 
                    0
                )
            ]
        )

    
    def __check_class_members(self):
        self.assertTrue(callable(self.__JSONQuestionExtractor.read))

    def __check_argument_not_a_string(self):
        with self.assertRaises(TypeError):
            self.__JSONQuestionExtractor.read(1) # type: ignore

    def __check_file_not_existing(self):
        with self.assertRaises(FileNotFoundError):
            self.__JSONQuestionExtractor.read('not_existing.json')
    
    def __check_file_wrong_formatting(self):
        with self.assertRaises(ValueError):
            self.__JSONQuestionExtractor.read('tests/resources/wrong_format.json')
    
    def __check_file_not_conforming(self, path: str):
        with self.assertRaises(ValueError):
            self.__JSONQuestionExtractor.read(path)

    def __check_files_not_conforming(self):
        self.__check_file_not_conforming('tests/resources/not_conforming/wrong_keys.json')
        self.__check_file_not_conforming('tests/resources/not_conforming/wrong_answers_type.json')
        self.__check_file_not_conforming('tests/resources/not_conforming/wrong_question_type.json')
        self.__check_file_not_conforming('tests/resources/not_conforming/wrong_solution_type.json')
