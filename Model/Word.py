class Word:

    def __init__(self):
        self.__init__("","",0)
        return

    def __init__(self, eng, kor):
        self.__init__(eng,kor,0)

    def __init__(self, eng, kor, count):
        self.eng = eng
        self.kor = kor
        self.count = count
