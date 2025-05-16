import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QLabel, QLineEdit, QTextEdit

class Grid(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()            # 객체 생성
        widget = QWidget()
        widget.setLayout(grid)          # widget에 추가
        self.setCentralWidget(widget)   # widget 배치

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle("Grid")
        self.setGeometry(300, 300, 400, 200)
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Grid()
    sys.exit(app.exec_())
