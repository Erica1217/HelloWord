import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *


class AddWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(700,540)
        self.setWindowTitle("add")




if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = main_ui()
    ex.show()
    sys.exit(app.exec_())
