from PyQt5 import pyqtSignal, QObject


class Nut(QObject):
    cracked = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def crack(self):
        self.cracked.emit()


def crackit():
    print("hazelnut cracked!")


hazelnut = Nut()
hazelnut.cracked.connect(crackit)
hazelnut.crack()
