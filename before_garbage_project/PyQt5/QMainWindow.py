import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)   # 객체 생성
        exitAction.setShortcut('Ctrl+Q')    # 단축키 설정
        exitAction.setStatusTip('Exit application') # statusBar에 표시할 텍스트
        exitAction.triggered.connect(qApp.quit) # 동작 설정

        # statusBar()는 QWidget에는 없고 QMainWindow에만 있다.
        self.statusBar().showMessage("Ready")   # 객체 생성 및 처음 나오는 text설정
        
        self.toolbar = self.addToolBar('Exit')  # 툴바 생성
        self.toolbar.addAction(exitAction)  # 툴바에 동작 추가

        self.setWindowTitle("MyWindow")
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())