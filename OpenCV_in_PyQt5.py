import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2

class PracticeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show_btn = QPushButton("New_Window")
        self.show_btn.resize(self.show_btn.sizeHint())
        self.show_btn.clicked.connect(self.show_image)

        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("이미지를 새 창에 띄우기: "), 0, 0)
        self.grid.addWidget(self.show_btn, 0, 1)
        self.grid.addWidget(QLabel("이미지를 현재 창에 띄우기: "), 1, 0)


        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)

        self.setWindowTitle("MyWindow")
        self.move(300, 300)
        self.show()

    def show_image(self):
        image = cv2.imread("study\\data\\bom.jpg", cv2.IMREAD_COLOR)
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PracticeApp()
    sys.exit(app.exec_())