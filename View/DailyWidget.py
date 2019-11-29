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
        self.db_manager = DBManager()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Daily")
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")

        main_layout = QVBoxLayout()
        daily_label = QLabel("DAILY")
        daily_label.setAlignment(Qt.AlignCenter)

        word_list_layout = QHBoxLayout()

        word_list_table1 = QTableWidget()
        word_list_table2 = QTableWidget()

        word_list_table1.setColumnCount(2)
        word_list_table1.setRowCount(10)
        word_list_table2.setColumnCount(2)
        word_list_table2.setRowCount(10)

        word_list_layout.addWidget(word_list_table1)
        word_list_layout.addWidget(word_list_table2)

        header1 = word_list_table1.horizontalHeader()
        header2 = word_list_table2.horizontalHeader()

        header1.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        main_layout.addWidget(daily_label)
        main_layout.addLayout(word_list_layout)

        word_list_table1.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        word_list_table2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        word_list_table1.setWordWrap(False)
        word_list_table2.setWordWrap(False)

        # 테이블에 데이터 추가
        daily_words = list(self.db_manager.get_daily_words())
        for i in range(0,10):
            # word_list_table1.setItem(i, 0, QTableWidgetItem(daily_words[i]))
            # word_list_table2.setItem(i, 0, QTableWidgetItem(daily_words[i+10]))

            word_list_table1.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            word_list_table2.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


        self.setLayout(main_layout)
        self.show()

    # def word_clicked(self):

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = DailyWidget()
    sys.exit(app.exec_())
