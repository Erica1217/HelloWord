import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore


class main_ui(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(700,540)
        self.setWindowTitle("Hello Word!")

        title_label = QLabel("HELLO WORD!")
        title_label.setStyleSheet("color:white;")

        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")
        self.show()

        daily_btn=QPushButton("Daily")
        daily_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        daily_btn.setStyleSheet("background-color: rgb(233, 211, 245, 100) ")

        words_btn=QPushButton("Words")
        words_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        words_btn.setStyleSheet("background-color: rgb(233, 211, 245, 100)")

        quiz_btn=QPushButton("Quiz")
        quiz_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        quiz_btn.setStyleSheet("background-color: rgb(233, 211, 245, 100)")

        repeat_btn = QPushButton("Repeat")
        repeat_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        repeat_btn.setStyleSheet("background-color: rgb(233, 211, 245, 100)")

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
