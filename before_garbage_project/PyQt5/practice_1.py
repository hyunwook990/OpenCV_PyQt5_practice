import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip   # 사용할 모듈 import
from PyQt5.QtGui import QIcon, QFont   # 아이콘 띄우기
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 툴팁 생성 (모든 버튼에 툴팁 생성)
        QToolTip.setFont(QFont('SanSerif', 10)) # 글꼴, 크기 설정
        self.setToolTip("This is a <b>QPushButton</b> widget") # 텍스트 입력

        # Quit 버튼
        btn = QPushButton('Quit', self) # 푸시 버튼 생성
        btn.move(50, 50)
        btn.resize(btn.sizeHint())  # 버튼의 크기를 적절하게 설정
        btn.setToolTip("test")  # 툴팁 설정의 또다른 방식(특정 버튼의 툴팁 설정)
        # 푸시버튼이 'clicked' 시그널을 app 객체의 quit() 메서드에 연결
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 창 띄우기
        self.setWindowTitle('My First Application') # 창 제목
        self.setWindowIcon(QIcon('web.png'))    # 아이콘 설정
        # self.move(300, 300)   # 창을 띄울 위치
        # self.resize(400, 200) # 창의 크기
        self.setGeometry(300, 300, 400, 200)    # move + resize
        self.show() # 실행

# __name__ : 현재 모듈의 이름이 저장되는 변수
# 다른 파일에서 이 파일을 import해서 실행하려면 파일명을 넣어주면 된다.
# if __name__ == 'practice_1':
#     # 객체 생성
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# 직접 실행하게되면 '__main__'이 된다.
if __name__ == '__main__':
    # 객체 생성
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())