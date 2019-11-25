from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DBManager import DBManager
from QuizMaker import QuizMaker


class QuizWidget(QWidget):

    def __init__(self):
        super(QuizWidget, self).__init__()
        self.db_manager = DBManager()
        self.quiz_maker = QuizMaker(self.db_manager.get_unknown_words())
        self.init__ui()

    def init__ui(self):
        main_layout = QVBoxLayout()

        quiz_label = QLabel('QUIZ')
        problem_label = QLabel()

        answer_layout = QHBoxLayout()
        answer_btn1 = QPushButton(self.quiz_maker.get_example()[0])
        answer_btn2 = QPushButton(self.quiz_maker.get_example()[1])
        answer_btn3 = QPushButton(self.quiz_maker.get_example()[2])

        answer_layout.addWidget(answer_btn1)
        answer_layout.addWidget(answer_btn2)
        answer_layout.addWidget(answer_btn3)

        main_layout.addWidget(quiz_label)
        main_layout.addWidget(problem_label)
        main_layout.addLayout(answer_layout)

        self.show()

    # def answer_btns_clicked(self):
    # def next_btn_clicked(self):


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = QuizWidget()
    sys.exit(app.exec_())

