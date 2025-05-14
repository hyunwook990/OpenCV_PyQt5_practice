참고: https://wikidocs.net/21853

# 대략적인 구조
```markdown
QMainWindow
├── MenuBar (옵션)
├── ToolBar (옵션)
├── StatusBar (옵션)
└── CentralWidget: QWidget
    └── Layout: QVBoxLayout / QHBoxLayout / QGridLayout
        ├── QLabel
        ├── QPushButton
        ├── QLineEdit
        └── ...
```
# Layout
- layout: 위젯을 배치하는 방식
1. 절대적 배치
    - 위젯의 크기와 위치를 픽셀 단위로 설정하여 배치
2. 박스 레이아웃
3. 그리드 레이아웃