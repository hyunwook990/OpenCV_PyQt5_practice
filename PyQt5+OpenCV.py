import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, QLabel

class PracticeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Unit()

    def Unit(self):
        show_btn = QPushButton("Show", self)
        show_btn.resize(show_btn.sizeHint())
        grid = QGridLayout()
        grid.addWidget(QLabel("그림 생성 버튼: "), 0, 0)
        grid.addWidget(show_btn, 0, 1)
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.setWindowTitle("MyWindow")
        self.setGeometry(200, 300, 200, 300)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PracticeApp()
    sys.exit(app.exec_())