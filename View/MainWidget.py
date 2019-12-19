import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *
from DBManager import DBManager
from View.DailyWidget import DailyWidget
from View.QuizWidget import QuizWidget
from View.WordsWidget import WordWidget
from View.RepeatWidget import RepeatWidget


class MainWidget(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super(MainWidget, self).__init__(parent)
        self.dbmanager= DBManager.instance()
        self.dbmanager.load()
        self.thisWindow = self
        self.init_ui()


    def init_ui(self):
        self.resize(700,540)
        self.setWindowTitle("HELLO WORD!")

        title_label = QLabel("HELLO WORD !")
        title_label.setStyleSheet("color:white;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial Rounded MT Bold" ,20))


        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")
        self.show()

        icon_size = QSize(200, 200)
        BTN_STYLE_SHEET = "background-color: rgb(233, 211, 245, 100)"

        daily_icon = QtGui.QIcon('../resource/icon/ic_daily.png')
        daily_btn=QPushButton()
        daily_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        daily_btn.setStyleSheet(BTN_STYLE_SHEET)
        daily_btn.setIconSize(icon_size)
        daily_btn.setIcon(daily_icon)
        daily_label=QLabel("DAILY")
        daily_label.move(10, 100)

        words_icon = QtGui.QIcon('../resource/icon/ic_words.png')
        words_btn=QPushButton()
        words_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        words_btn.setStyleSheet(BTN_STYLE_SHEET)
        words_btn.setIconSize(icon_size)
        words_btn.setIcon(words_icon)

        quiz_icon = QtGui.QIcon('../resource/icon/ic_quiz.png')
        quiz_btn=QPushButton()
        quiz_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        quiz_btn.setStyleSheet(BTN_STYLE_SHEET)
        quiz_btn.setIconSize(icon_size)
        quiz_btn.setIcon(quiz_icon)

        repeat_icon = QtGui.QIcon('../resource/icon/ic_repeat.png')
        repeat_btn = QPushButton()
        repeat_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        repeat_btn.setStyleSheet(BTN_STYLE_SHEET)
        repeat_btn.setIconSize(icon_size)
        repeat_btn.setIcon(repeat_icon)

        hbox1=QHBoxLayout()
        hbox1.addWidget(title_label)
        hbox2=QHBoxLayout()
        hbox2.addWidget(daily_btn)
        hbox2.addSpacing(10)
        hbox2.addWidget(words_btn)
        hbox3=QHBoxLayout()
        hbox3.addWidget(quiz_btn)
        hbox3.addSpacing(10)
        hbox3.addWidget(repeat_btn)
        vbox=QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addSpacing(9)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        daily_btn.clicked.connect(self.daily_clicked)
        words_btn.clicked.connect(self.words_clicked)
        quiz_btn.clicked.connect(self.quiz_clicked)
        repeat_btn.clicked.connect(self.repeat_clicked)

        self.setLayout(vbox)

    def daily_clicked(self):
        if (len(self.dbmanager.get_known_words()) < 20):
            QMessageBox.information(
                self, '알림', "단어가 부족합니다.",
                QMessageBox.Yes)
            return
        self.thisWindow = DailyWidget()
        self.thisWindow.show()

    def words_clicked(self):
        self.thisWindow = WordWidget()
        self.thisWindow.show()

    def quiz_clicked(self):
        self.thisWindow = QuizWidget()
        self.thisWindow.show()

    def repeat_clicked(self):
        if (len(self.dbmanager.get_known_words())==0):
            QMessageBox.information(
                self, '알림', "복습할 단어가 없습니다.",
                QMessageBox.Yes)
            return
        self.thisWindow = RepeatWidget()
        self.thisWindow.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.dbmanager.save()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
