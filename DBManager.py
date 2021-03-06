from Model.Word import Word
import csv
import pickle
from datetime import datetime
import random


class DBManager:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls()
        cls.instance = cls._get_instance
        return cls._instance

    def __init__(self):
        self.GRADE_CUT = 3
        # self.load()
        self.__all_words = dict()
        self.__known_words = dict()
        self.__unknown_words = dict()
        self.__daily_words = []

    '''
    이미 있는 단어는 false, 없는 단어는 true 리턴
    '''
    def add_word(self, eng, kor):
        new_word = Word(eng, kor, 0)
        if eng not in self.__all_words:
            self.__all_words[eng] = new_word
            self.__unknown_words[eng] = new_word
            return True
        return False

    '''
    csv파일을 선택하여 여러개 한번에 추가
    영어 | 한글
    ---- | ----
    banana | 바나나
    apple | 사과
    paper | 종이
    '''
    def add_words_from_csv(self, path):
        f = open(path, 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.add_word(line[0], line[1])
        f.close()

    # 사용자가 문제를 맞췄을 때
    def solve_quiz(self, eng):
        self.__all_words[eng].count += 1
        if self.__all_words[eng].count == self.GRADE_CUT and eng in self.__unknown_words:
            self.__known_words[eng] = self.__all_words[eng]
            del self.__unknown_words[eng]

    def get_all_words(self):
        return self.__all_words

    def get_known_words(self):
        return self.__known_words

    def get_unknown_words(self):
        return self.__unknown_words

    def get_daily_words(self):
        return self.__daily_words

    def load(self):
        try:
            with open('data.pickle', 'rb') as f:
                data = pickle.load(f)
                self.__all_words = data[0]
                self.__known_words = data[1]
                self.__unknown_words = data[2]
                self.__daily_words = data[3]
                pre_time = data[4]
                now = datetime.now()
                print(pre_time, now)
                if pre_time.year != now.year or pre_time.month != now.month or pre_time.day != now.day or len(self.__daily_words)==0:
                    if len(self.__unknown_words.values()) >= 20:
                        self.__daily_words = random.sample(list(self.__unknown_words.values()), 20)
                    else:
                        self.__daily_words = self.__unknown_words.values()

        except Exception as ex:
            print('error', ex)

    def save(self):
        data = [self.__all_words,
                self.__known_words,
                self.__unknown_words,
                self.__daily_words,
                datetime.now()]
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


