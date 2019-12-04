from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DBManager import DBManager


class DailyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.db_manager = DBManager.instance()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Daily")
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")

        main_layout = QVBoxLayout()
        daily_label = QLabel("DAILY")
        daily_label.setAlignment(Qt.AlignCenter)
        daily_label.setStyleSheet("color:white;")
        daily_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 20))

        word_list_layout = QHBoxLayout()

        self.word_list_table1 = QTableWidget()
        self.word_list_table2 = QTableWidget()

        self.word_list_table1.setColumnCount(2)
        self.word_list_table1.setRowCount(10)
        self.word_list_table2.setColumnCount(2)
        self.word_list_table2.setRowCount(10)
        self.word_list_table1.setStyleSheet("background-color: rgb(255, 255, 255, 80)")
        self.word_list_table2.setStyleSheet("background-color: rgb(233, 255, 255, 80)")

        word_list_layout.addWidget(self.word_list_table1)
        word_list_layout.addWidget(self.word_list_table2)

        header1 = self.word_list_table1.horizontalHeader()
        header2 = self.word_list_table2.horizontalHeader()

        header1.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        main_layout.addWidget(daily_label)
        main_layout.addLayout(word_list_layout)

        self.word_list_table1.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.word_list_table2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.word_list_table1.setHorizontalHeaderLabels(["영어", "뜻"])
        self.word_list_table2.setHorizontalHeaderLabels(["영어", "뜻"])

        self.word_list_table1.setWordWrap(False)
        self.word_list_table2.setWordWrap(False)

        # 테이블에 데이터 추가
        daily_words = list(self.db_manager.get_daily_words().values())
        for i in range(0, 10):
            self.word_list_table1.setItem(i, 0, QTableWidgetItem(daily_words[i].eng))
            self.word_list_table1.setItem(i, 1, QTableWidgetItem(daily_words[i].kor))
            self.word_list_table2.setItem(i, 0, QTableWidgetItem(daily_words[i+10].eng))
            self.word_list_table2.setItem(i, 1, QTableWidgetItem(daily_words[i+10].kor))

            self.word_list_table1.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            self.word_list_table2.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


        self.setLayout(main_layout)
        self.show()

    # def word_clicked(self):

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = DailyWidget()
    sys.exit(app.exec_())
