import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 객체 생성
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()            # 수평 박스 생성
        hbox.addStretch(1)              # 빈 공간 생성
        hbox.addWidget(okButton)        # 버튼 추가
        hbox.addWidget(cancelButton)    # 버튼 추가
        hbox.addStretch(1)              # 인자가 같음 = 두 빈 공간의 크기는 항상 같은 크기를 유지

        vbox = QVBoxLayout()            # 수직 박스 생성
        vbox.addStretch(3)              # 빈 공간 생성
        vbox.addLayout(hbox)            # 박스 추가
        vbox.addStretch(1)              # 빈 공간 3:1 비율로 유지

        widet = QWidget()                 # QMainWindow에는 setLayout이 없으므로
        widet.setLayout(vbox)             # layout에 배치
        self.setCentralWidget(widet)      # layout 생성

        self.setWindowTitle("box")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())