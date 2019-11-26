import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *


class main_ui(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.resize(700,540)
        self.setWindowTitle("Hello Word!")

        title_label = QLabel("HELLO WORD!")
        title_label.setStyleSheet("color:white;")


        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")
        self.show()

        icon_size = QSize(150, 150)
        BTN_STYLE_SHEET = "background-color: rgb(233, 211, 245, 100)"

        daily_icon = QtGui.QIcon('../resource/icon/ic_daily.png')
        daily_btn=QPushButton()
        daily_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        daily_btn.setStyleSheet(BTN_STYLE_SHEET)
        daily_btn.setIconSize(icon_size)
        daily_btn.setIcon(daily_icon)

        words_icon = QtGui.QIcon('../resource/icon/ic_words.png')
        words_btn=QPushButton("Words")
        words_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        words_btn.setStyleSheet(BTN_STYLE_SHEET)
        daily_btn.setIconSize(icon_size)
        daily_btn.setIcon(words_icon)

        quiz_icon = QtGui.QIcon('../resource/icon/ic_quiz.png')
        quiz_btn=QPushButton("Quiz")
        quiz_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        quiz_btn.setStyleSheet(BTN_STYLE_SHEET)
        quiz_btn.setIconSize(icon_size)
        quiz_btn.setIcon(quiz_icon)

        repeat_icon = QtGui.QIcon('../resource/icon/ic_repeat.png')
        repeat_btn = QPushButton("Repeat")
        repeat_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        repeat_btn.setStyleSheet(BTN_STYLE_SHEET)
        quiz_btn.setIconSize(icon_size)
        quiz_btn.setIcon(repeat_icon)

        hbox1=QHBoxLayout()
        hbox1.addWidget(title_label)
        hbox2=QHBoxLayout()
        hbox2.addWidget(daily_btn)
        hbox2.addWidget(words_btn)
        hbox3=QHBoxLayout()
        hbox3.addWidget(quiz_btn)
        hbox3.addWidget(repeat_btn)
        vbox=QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = main_ui()
    ex.show()
    sys.exit(app.exec_())
