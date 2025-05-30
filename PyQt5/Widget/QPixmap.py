import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Pixmap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pix_map()

    def pix_map(self):
        pixmap = QPixmap("study\\data\\bom.jpg")

        label_image = QLabel()
        label_image.setPixmap(pixmap)
        label_size = QLabel("width: " + str(pixmap.width()) + ", Height: " + str(pixmap.height()))
        label_size.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.addWidget(label_image)
        grid.addWidget(label_size)
        
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.setWindowTitle("pixmap")
        self.move(300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Pixmap()
    sys.exit(app.exec_())
