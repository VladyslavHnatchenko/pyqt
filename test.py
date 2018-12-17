from PyQt5.QtWidgets import QTableWidgetItem
from qtable import *
import sys


data = []
data.append(('Add', 'QTableWidget'))
data.append(('new data', 'in Python'))
data.append(('very, very', 'simple'))


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)

        self.ui.pushButton.clicked.connect(self.clear)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(item)

                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )

                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def clear(self):
        self.ui.tableWidget.clear()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())

# from PyQt5 import QtWidgets
# from combobox import Ui_MainWindow
# import sys
#
#
# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.ui.comboBox.addItem("Developer")
#         self.ui.comboBox.addItem("Designer")
#
#
# app = QtWidgets.QApplication([])
# application = MyWindow()
# application.show()
#
# sys.exit(app.exec())

# from PyQt5 import QtWidgets
# from signaledit import Ui_MainWindow
# import sys
#
#
# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#
# app = QtWidgets.QApplication([])
# application = MyWindow()
# application.show()
#
# sys.exit(app.exec())

# from PyQt5 import QtWidgets, QtCore
# from myform import Ui_MainWindow
# import sys
#
#
# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.btnClicked)
#
#     def btnClicked(self):
#         self.ui.label.setText("You're pressed the button!")
#         self.ui.label.adjustSize()
#
#
# app = QtWidgets.QApplication([])
# application = MyWindow()
# application.show()
#
# sys.exit(app.exec())
