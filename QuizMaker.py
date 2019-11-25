import random

class QuizMaker:
    def __init__(self,words):
        self.words = words
        self.__problem = ''
        self.__example = []
        self.__answer = ''
        self.new_problem()

    def new_problem(self):
        if(len(self.words)>=3):
            problem = random.sample(list(self.words), 3)
            self.__problem = problem[0].eng
            self.__example = []
            self.__answer = problem[0].kor
            self.__example.append(problem[0].kor)
            self.__example.append(problem[1].kor)
            self.__example.append(problem[2].kor)
            random.shuffle(self.new_problem)
    def get_problem(self):
        return self.__problem

    def get_example(self):
        return self.__example