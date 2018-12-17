from PyQt5.QtWidgets import QTableWidgetItem
from qtable import *
import sys


data = []
data.append(('BMW', '2005'))
data.append(('Audi', '2003'))
data.append(('Volvo', '1990'))
data.append(('Toyota', '2018'))


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(
            len(data)
        )
        self.ui.tableWidget.setColumnCount(
            len(data)
        )

        self.ui.pushButton.clicked.connect(self.clear)

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Brand', 'Year of issue')
        )

        # self.ui.tableWidget.setVerticalHeaderLabels(
        #     ('900$', '5000$', '13000$')
        # )

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

        self.ui.tableWidget.sortByColumn(
            1, QtCore.Qt.AscendingOrder
        )

    def clear(self):
        self.ui.tableWidget.clear()


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()

sys.exit(app.exec())
