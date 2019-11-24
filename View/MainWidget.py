import sys

from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore


class main_ui(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(700,540)
        self.setWindowTitle("Hello Word!")
        self.setStyleSheet("background-color: rgb(251, 183, 191)")
        self.show()

        daily_btn=QPushButton("Daily")
        daily_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        daily_btn.setStyleSheet("background-color: rgb(233, 211, 245)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../OneDrive/사진/sw2/947540.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        daily_btn.setIcon(icon1)
        daily_btn.setIconSize(QtCore.QSize(150, 140))

        words_btn=QPushButton("Words")
        words_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        words_btn.setStyleSheet("background-color: rgb(233, 211, 245)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../OneDrive/사진/sw2/947540.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        words_btn.setIcon(icon2)
        words_btn.setIconSize(QtCore.QSize(150, 140))

        quiz_btn=QPushButton("Quiz")
        quiz_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        quiz_btn.setStyleSheet("background-color: rgb(233, 211, 245)")

        repeat_btn = QPushButton("Repeat")
        repeat_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        repeat_btn.setStyleSheet("background-color: rgb(233, 211, 245)")



        hbox1=QHBoxLayout()
        hbox1.addWidget(daily_btn)
        hbox1.addWidget(words_btn)
        hbox2=QHBoxLayout()

        hbox2.addWidget(quiz_btn)
        hbox2.addWidget(repeat_btn)
        vbox=QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = main_ui()
    ex.show()
    sys.exit(app.exec_())