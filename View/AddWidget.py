import sys

from PyQt5 import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *

from DBManager import DBManager


class AddWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dbManager= DBManager.instance()
        self.kor_edit = QLineEdit()
        self.kor_edit.setMaximumHeight(60)
        self.kor_edit.setStyleSheet(("background-color: rgb(255, 255, 255, 100)"))

        self.eng_edit = QLineEdit()
        self.eng_edit.setMaximumHeight(60)
        self.eng_edit.setStyleSheet(("background-color: rgb(255, 255, 255, 100)"))
        self.init_ui()


    def init_ui(self):
        self.resize(700, 540)
        self.setWindowTitle("ADD")

        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                           "rgb(200, 191, 231), stop:1 rgb(252, 171, 205));")

        vlayout = QVBoxLayout()

        title_label = QLabel("ADD")
        title_label.setStyleSheet("color:white;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial Rounded MT Bold", 20))
        title_label.setStyleSheet("background-color: rgb(255,255,255,0); color:white;")

        top_layout = QHBoxLayout()
        top_layout.addStretch(1)
        top_layout.addWidget(title_label)
        top_layout.addStretch(1)

        eng_label = QLabel("영어")
        eng_label.setStyleSheet("background-color: rgb(255, 255, 255, 0)")
        eng_layout = QHBoxLayout()
        eng_layout.addStretch(1)
        eng_layout.addWidget(eng_label)
        eng_layout.addWidget(self.eng_edit)
        eng_layout.addStretch(1)

        kor_label = QLabel("한글")
        kor_label.setStyleSheet("background-color: rgb(255, 255, 255, 0)")
        kor_layout = QHBoxLayout()
        kor_layout.addStretch(1)
        kor_layout.addWidget(kor_label)
        kor_layout.addWidget(self.kor_edit)
        kor_layout.addStretch(1)

        import_btn = QPushButton("import CSV")
        import_btn.setStyleSheet("background-color: rgb(255, 255, 255, 100)")
        ok_btn = QPushButton("OK")
        ok_btn.setStyleSheet("background-color: rgb(255, 255, 255, 100)")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(import_btn)
        btn_layout.addStretch(1)
        btn_layout.addWidget(ok_btn)

        bottom_layout = QVBoxLayout()
        bottom_layout.addStretch(2)
        bottom_layout.addLayout(eng_layout)
        bottom_layout.addLayout(kor_layout)
        bottom_layout.addStretch(4)
        bottom_layout.addLayout(btn_layout)

        vlayout.addLayout(top_layout)
        vlayout.addLayout(bottom_layout)

        ok_btn.clicked.connect(self.ok_btn)
        import_btn.clicked.connect(self.import_csv_btn)

        self.setLayout(vlayout)

    def ok_btn(self):
        eng = self.eng_edit.text()
        kor = self.kor_edit.text()
        self.dbManager.add_word(eng, kor)
        self.eng_edit.setText('')
        self.kor_edit.setText('')

    def import_csv_btn(self):
        csv_path = QFileDialog.getOpenFileName(self)
        print(csv_path[0])
        if len(csv_path[0])>=4 and csv_path[0][-4:]==".csv":
            self.dbManager.add_words_from_csv(csv_path)
        else:
            QMessageBox.information(
                self, '알림', "csv파일이 아닙니다.",
                QMessageBox.Yes)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = AddWidget()
    ex.show()
    sys.exit(app.exec_())
