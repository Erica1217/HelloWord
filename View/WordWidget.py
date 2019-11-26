import sys

from PyQt5 import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *

from DBManager import DBManager
from View.AddWidget import AddWidget


class WordWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dbManager= DBManager()
        self.init_ui()


    def init_ui(self):
        self.resize(700, 540)
        self.setWindowTitle("Hello Word!")

        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")

        vlayout = QVBoxLayout()
        top_layout = QHBoxLayout()
        tab_widget = QTabWidget()

        title_label = QLabel("WORD")
        title_label.setStyleSheet("color:white;")

        add_btn = QPushButton()
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

    def set_table_widget(self,table_widget, data):
        i = 0

        table_widget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(2)

        for eng, word in data.items():
            table_widget.setItem(i, 0, QTableWidgetItem(word.eng))
            table_widget.setItem(i, 1, QTableWidgetItem(word.kor))
            i += 1

    def add_btn_clicked(self):
        # 새로운 add ui 추가
        AddWidget().show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = WordWidget()
    ex.show()
    sys.exit(app.exec_())