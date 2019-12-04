import sys

from PyQt5 import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *

from DBManager import DBManager
from View.AddWidget import AddWidget
from WordSpeaker import WordSpeaker


class WordWidget(QWidget):
    def __init__(self, parent=None):
        super(WordWidget, self).__init__(parent)
        self.thisWindow = self
        self.dbManager = DBManager.instance()
        self.init_ui()

    def init_ui(self):
        self.resize(700, 540)
        self.setWindowTitle("Hello Word!")

        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")

        vlayout = QVBoxLayout()
        top_layout = QHBoxLayout()
        tab_widget = QTabWidget()

        title_label = QLabel("WORDS")
        title_label.setStyleSheet("color:white;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 20))
        title_label.setStyleSheet("background-color: rgb(255,255,255,0); color:white;")

        add_btn = QPushButton()
        add_btn.setStyleSheet("background-color: rgb(255,255,255,0);")
        add_icon = QIcon("../resource/icon/ic_add.png")
        add_btn.setIcon(add_icon)
        add_btn.setIconSize(QSize(70,70))
        add_btn.clicked.connect(self.add_btn_clicked)

        top_layout.addStretch(3)
        top_layout.addWidget(title_label)
        top_layout.addStretch(2)
        top_layout.addWidget(add_btn)

        all_tab = QTableWidget()
        known_tab = QTableWidget()
        unknown_tab = QTableWidget()

        self.set_table_widget(all_tab, self.dbManager.get_all_words())
        self.set_table_widget(known_tab, self.dbManager.get_know_words())
        self.set_table_widget(unknown_tab, self.dbManager.get_unknown_words())

        tab_widget.addTab(all_tab, "All")
        tab_widget.addTab(unknown_tab, "Unknown")
        tab_widget.addTab(known_tab, "Known")

        vlayout.addLayout(top_layout)
        vlayout.addWidget(tab_widget)

        self.setLayout(vlayout)

    def set_table_widget(self, table_widget, data):
        i = 0

        table_widget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(2)

        for eng, word in data.items():
            table_widget.setItem(i, 0, QTableWidgetItem(str(word.eng)))
            table_widget.setItem(i, 1, QTableWidgetItem(str(word.kor)))
            i += 1
        table_widget.cellClicked.connect(self.word_clicked)

    def add_btn_clicked(self):
        # 새로운 add ui 추가
        self.thisWindow = AddWidget()
        self.thisWindow.show()
        print(self.dbManager.get_all_words())

    def word_clicked(self, row, col):
        sender = self.sender()
        word = sender.item(row, col).text()
        WordSpeaker.speak(word)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WordWidget()
    ex.show()
    sys.exit(app.exec_())
