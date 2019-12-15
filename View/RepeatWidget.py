from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DBManager import DBManager
from QuizMaker import QuizMaker
from WordSpeaker import WordSpeaker


class RepeatWidget(QWidget):

    def __init__(self):
        super(RepeatWidget, self).__init__()
        self.db_manager = DBManager.instance()
        self.quiz_maker = QuizMaker(self.db_manager.get_known_words())
        self.word_speaker = WordSpeaker()
        self.problem_label = QLabel(self.quiz_maker.get_problem())
        self.next_btn = QPushButton()
        self.answer_line_edit = QLineEdit()
        self.text_label = QLabel()
        self.has_answer = False

        self.init__ui()

        self.word_speaker.speak(self.quiz_maker.get_problem())

    def init__ui(self):
        self.resize(700, 540)
        self.setWindowTitle("Repeat")
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")
        main_layout = QVBoxLayout()

        quiz_label = QLabel('REPEAT')
        quiz_label.setStyleSheet("color:white;")
        quiz_label.setAlignment(Qt.AlignCenter)
        quiz_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 20))

        play_button = QPushButton('▶')
        input_button = QPushButton('입력')
        input_button.clicked.connect(self.answer_btns_clicked)
        play_button.clicked.connect(self.play_btn_clicked)

        self.answer_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        hlayout = QHBoxLayout()
        hlayout.addSpacing(30)
        hlayout.addWidget(play_button)
        hlayout.addSpacing(30)
        hlayout.addWidget(self.answer_line_edit)
        hlayout.addSpacing(10)
        hlayout.addWidget(input_button)

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
        main_layout.addStretch(4)
        main_layout.addLayout(hlayout)
        main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
        self.show()

    def answer_btns_clicked(self):
        answer = self.answer_line_edit.text()
        print(answer,self.quiz_maker.get_problem())
        if self.has_answer is False:
            if self.quiz_maker.get_problem() == answer:
                self.text_label.setText("정답입니다!")
                self.text_label.setStyleSheet("background-color: rgb(233, 211, 245, 0); color: rgb(0,255,0)")
                self.text_label.setFont(QtGui.QFont("함초롬돋움", 14))
            else:
                self.text_label.setText("정답은 "+self.quiz_maker.get_answer())
                self.text_label.setStyleSheet("background-color: rgb(233, 211, 245, 0); color: rgb(255,0,0)")
                self.text_label.setFont(QtGui.QFont("함초롬돋움", 14))
            self.next_btn.show()
            self.text_label.show()
        self.has_answer = True

    def next_btn_clicked(self):
        if self.has_answer is True:
            self.quiz_maker.new_problem()
            answer = self.quiz_maker.get_problem()
            self.problem_label.setText(answer)
            self.next_btn.hide()
            self.text_label.hide()
            self.has_answer = False
            self.word_speaker.speak(answer)

    def play_btn_clicked(self):
        answer = self.quiz_maker.get_problem()
        self.word_speaker.speak(answer)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = RepeatWidget()
    sys.exit(app.exec_())

