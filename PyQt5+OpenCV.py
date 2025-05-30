import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton

class PracticeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Unit()

    def Unit(self):
        show_btn = QPushButton("Show", self)
        grid = QGridLayout()
        widget = QWidget()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PracticeApp()
    sys.exit(app.exec_())
