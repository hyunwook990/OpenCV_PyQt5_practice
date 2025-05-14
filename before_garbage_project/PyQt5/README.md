참고: https://wikidocs.net/21853

# 대략적인 구조
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