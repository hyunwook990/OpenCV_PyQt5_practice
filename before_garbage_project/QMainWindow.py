import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    
    def InitUI(self):
        self.statusBar().showMessage("Ready")
        
        self.setWindowTitle("MyWindow")
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())