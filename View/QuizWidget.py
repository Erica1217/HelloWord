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
        self.db_manager = DBManager.instance()
        self.quiz_maker = QuizMaker(self.db_manager.get_unknown_words())
        if (len(self.quiz_maker.get_example())):
            # todo 사용자에게 데이터가 없습니다 라고 알림
            return

        self.answer_btn1 = QPushButton(self.quiz_maker.get_example()[0])
        self.answer_btn2 = QPushButton(self.quiz_maker.get_example()[1])
        self.answer_btn3 = QPushButton(self.quiz_maker.get_example()[2])
        self.problem_label = QLabel(self.quiz_maker.get_problem())
        self.next_btn = QPushButton()
        self.has_answer = False

        self.text_label = QLabel()
        self.init__ui()

    def init__ui(self):
        self.resize(700, 540)
        self.setWindowTitle("Quiz")
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")
        main_layout = QVBoxLayout()

        quiz_label = QLabel('QUIZ')
        quiz_label.setStyleSheet("color:white;")
        quiz_label.setAlignment(Qt.AlignCenter)
        quiz_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 20))

        self.problem_label.setAlignment(Qt.AlignCenter)
        self.problem_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.problem_label.setStyleSheet("color:black;")
        self.problem_label.setAlignment(Qt.AlignCenter)
        self.problem_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 33))

        answer_layout = QHBoxLayout()

        self.answer_btn1.setStyleSheet("background-color: rgb(233, 211, 245, 100)")
        self.answer_btn2.setStyleSheet("background-color: rgb(233, 211, 245, 100)")
        self.answer_btn3.setStyleSheet("background-color: rgb(233, 211, 245, 100)")

        self.answer_btn1.clicked.connect(self.answer_btns_clicked)
        self.answer_btn2.clicked.connect(self.answer_btns_clicked)
        self.answer_btn3.clicked.connect(self.answer_btns_clicked)

        answer_layout.addWidget(self.answer_btn1)
        answer_layout.addWidget(self.answer_btn2)
        answer_layout.addWidget(self.answer_btn3)

        self.next_btn.setIcon(QIcon("../resource/icon/ic_right_arrow.png"))
        self.next_btn.setStyleSheet("background-color: rgb(233, 211, 245, 0)")
        self.next_btn.clicked.connect(self.next_btn_clicked)
        self.next_btn.hide()

        self.text_label.setStyleSheet("background-color: rgb(233, 211, 245, 0)")

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.text_label)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.next_btn)

        main_layout.addWidget(quiz_label)
        main_layout.addStretch(1)
        main_layout.addWidget(self.problem_label)
        main_layout.addStretch(3)
        main_layout.addLayout(answer_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
        self.show()

    def answer_btns_clicked(self):
        answer = self.sender().text()
        if self.has_answer is False:
            if self.quiz_maker.get_answer() == answer:
                self.text_label.setText("정답입니다!")
                self.text_label.setStyleSheet("background-color: rgb(233, 211, 245, 0); color: rgb(34,177,76)")
                self.text_label.setFont(QtGui.QFont("함초롬돋움", 15))
            else:
                self.text_label.setText("정답은 "+self.quiz_maker.get_answer())
                self.text_label.setStyleSheet("background-color: rgb(233, 211, 245, 0); color: rgb(255,0,0)")
                self.text_label.setFont(QtGui.QFont("함초롬돋움", 15))
            self.next_btn.show()
            self.text_label.show()
        self.has_answer = True

    def next_btn_clicked(self):
        if self.has_answer is True:
            self.quiz_maker.new_problem()
            example = self.quiz_maker.get_example()
            self.problem_label.setText(self.quiz_maker.get_problem())
            self.answer_btn1.setText(example[0])
            self.answer_btn2.setText(example[1])
            self.answer_btn3.setText(example[2])
            self.next_btn.hide()
            self.text_label.hide()
            self.has_answer = False


if __name__ == '__main__':
    import sys
    # from gtts import gTTS
    # import pygame
    # from io import BytesIO
    # mp3_fp = BytesIO()
    # tts = gTTS('hello', 'en')
    # tts.write_to_fp(mp3_fp.)
    #
    # pygame.mixer.init()
    # pygame.mixer.music.load()
    # pygame.mixer.music.play()

    app = QApplication(sys.argv)
    ex = QuizWidget()
    sys.exit(app.exec_())


