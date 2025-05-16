import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt, QTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
    
    def initUI(self):

        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet(
            "color : red;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: #FA8072;"
            "border-radius: 3px"
        )
        lbl_green.setStyleSheet(
            "color : green;"
            "background-color: #7FFFD4;"
        )
        lbl_blue.setStyleSheet(
            "color : blue;"
            "background-color: #87CEFA;"
            "border-style: dashed;"
            "border-width: 3px;"
            "border-color: #1E90FF"
        )

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        # QMainWindow()는 자체적으로 레이아웃을 설정할 수 없기에 setLayout()을 사용하지 못함
        # QWidget()을 통해서 setLayout을 적용,
        # setCentralWidget을 통해서 중앙 위젯으로 지정.
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)   # 객체 생성
        exitAction.setShortcut('Ctrl+Q')    # 단축키 설정
        exitAction.setStatusTip('Exit application') # statusBar에 표시할 텍스트
        exitAction.triggered.connect(qApp.quit) # 동작 설정

        # statusBar()는 QWidget에는 없고 QMainWindow에만 있다.
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))   # 객체 생성 및 처음 나오는 text설정

        self.statusBar()    # statusBar 생성

        self.toolbar = self.addToolBar('Exit')  # 툴바 생성
        self.toolbar.addAction(exitAction)  # 툴바에 동작 추가

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu("&FIle")
        filemenu.addAction(exitAction)

        self.setWindowTitle("MyWindow")
        # self.setGeometry(300, 300, 400, 200)
        self.resize(500, 350)   # 창 크기 설정
        self.center()   # center 함수 실행
        self.show()

    def center(self):
        qr = self.frameGeometry()   # 창의 위치, 크기 정보를 가져온다.
        cp = QDesktopWidget().availableGeometry().center()  # 모니터의 가운데를 파악
        qr.moveCenter(cp)   # 모니터의 중심점으로 창의 중심점을 이동한다.
        self.move(qr.topLeft()) # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)에 이동 (실제 이동 작업)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())