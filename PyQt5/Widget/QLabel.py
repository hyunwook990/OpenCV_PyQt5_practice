import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt

class Label(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label()

    def label(self):

        self.setWindowTitle("label")
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Label()
    sys.exit(app.exec_())