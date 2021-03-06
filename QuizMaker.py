import random
import copy

class QuizMaker:
    def __init__(self, words):
        self.words = words
        self.__problem = ''
        self.__example = []
        self.__answer = ''
        self.new_problem()

    def new_problem(self):
        if len(self.words) >= 4:
            words = copy.deepcopy(self.words)
            if self.__problem in words:
                del words[self.__problem]
            problem = random.sample(list(words.values()), 3)
            self.__problem = problem[0].eng
            self.__example = []
            self.__answer = problem[0].kor
            self.__example.append(problem[0].kor)
            self.__example.append(problem[1].kor)
            self.__example.append(problem[2].kor)
            random.shuffle(self.__example)

    def get_answer(self):
        return self.__answer

    def get_problem(self):
        return self.__problem

    def get_example(self):
        return self.__example
