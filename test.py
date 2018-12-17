from PyQt5 import QtWidgets, QtCore
from qline import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText("Welcome on PythonScripts")

        self.ui.lineEdit_2.setMaxLength(10)

        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ui.lineEdit_4.setReadOnly(True)

        self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")

        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
