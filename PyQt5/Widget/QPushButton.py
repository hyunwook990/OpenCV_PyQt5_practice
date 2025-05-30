import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication

class PushButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushbutton()

    def pushbutton(self):
        # & -> 'alt' + '&뒤의 문자'로 단축키
        btn1 = QPushButton("&Button1", self)
        btn2 = QPushButton(self)
        btn3 = QPushButton("Button3", self)
        btn4 = QPushButton("quit", self)

        # method
        # btn1.setIcon()            # 버튼 아이콘 설정
        # btn1.isChecked()          # 버튼 선택 여부 반환
        # btn1.text()               # 버튼 텍스트 반환
        btn2.setText("Button&2")    # 버튼 텍스트 설정
        btn1.setCheckable(True)     # 누른 상태 여부 구분
        btn1.toggle()               # 상태 변경
        btn3.setEnabled(False)      # 버튼 사용 여부 설정

        # signal
        # btn1.pressed              # 버튼이 눌렸을 때 발생
        # btn1.released             # 버튼을 눌렀다 뗄 때 발생
        # btn1.toggled              # 버튼의 상태가 변경될 때 발생
                                    # 버튼을 클릭할 때 발생
        btn4.clicked.connect(QCoreApplication.instance().quit)

        grid = QGridLayout()
        grid.addWidget(QLabel("버튼 1: "), 0, 0)
        grid.addWidget(QLabel("버튼 2: "), 1, 0)
        grid.addWidget(QLabel("버튼 3: "), 2, 0)
        grid.addWidget(btn1, 0, 1)
        grid.addWidget(btn2, 1, 1)
        grid.addWidget(btn3, 2, 1)
        grid.addWidget(btn4, 3, 1)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
        
        self.setWindowTitle("pushbutton")
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PushButton()
    sys.exit(app.exec_())