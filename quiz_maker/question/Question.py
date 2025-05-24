class Question:
    __question: str
    __answers: list[str] = []
    __solution: int | None = None

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question: str):
        if not isinstance(question, str):
            raise TypeError
        self.__question = question

    @property
    def answers(self):
        return self.__answers
    
    @answers.setter
    def answers(self, answers: list[str]):
        if not isinstance(answers, list):
            raise TypeError
        for answer in answers:
            if not isinstance(answer, str):
                raise TypeError

        self.__answers = answers

        if not self.__is_valid_reference(self.solution):
            self.solution = None

    @property
    def solution(self):
        return self.__solution
    
    @solution.setter
    def solution(self, solution: int | None):   
        if solution is not None and not isinstance(solution, int):
            raise TypeError

        self.__solution = None

        if self.__is_valid_reference(solution):
            self.__solution = solution

    def __init__(self, question: str, answers: list[str], solution: int | None) -> None:
        self.question = question
        self.answers = answers
        self.solution = solution

    def __is_valid_reference(self, solution: int | None) -> bool:
        return solution in range(len(self.answers))
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, Question) and \
            self.question == value.question and \
            self.answers == value.answers and \
            self.solution == value.solution
