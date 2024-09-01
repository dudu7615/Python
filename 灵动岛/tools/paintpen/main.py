from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui import *
import paintPen


class MainWindow(QMainWindow):
    def __init__(self, screen: QRect):
        super().__init__()
        self.color: tuple[int,int,int,int] = (255, 0, 0, 255)
        self.penWidth: int = 10
        place = (screen.width() // 2 - self.height() // 2, 0)
        self.setGeometry(*place, 400, 300)
        self.setWindowTitle("屏幕批注")
        # self.setWindowIcon()
        self.ui = ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.ui.red.clicked.connect(self.red)
        self.ui.green.clicked.connect(self.green)
        self.ui.white.clicked.connect(self.white)
        self.ui.black.clicked.connect(self.black)
        self.ui.choose.clicked.connect(self.choose)
        self.ui.wight.valueChanged.connect(self.setWight)
        self.ui.start.clicked.connect(self.showPen)
        self.ui.off.clicked.connect(self.hidePen)

    def red(self):
        self.color = (255, 0, 0, 255)
        self.changePen()

    def green(self):
        self.color = (0, 255, 0, 255)
        self.changePen()

    def white(self):
        self.color = (255, 255, 255, 255)
        self.changePen()

    def black(self):
        self.color = (0, 0, 0, 255, 255)
        self.changePen()

    def setWight(self, wight: int):
        self.penWidth = wight
        self.changePen()

    def changePen(self):
        self.ui.show.penWeigh = self.penWidth
        self.ui.show.color = self.color
        self.ui.show.update()

    def choose(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.getRgb()

        self.changePen()

    def showPen(self):
        self.pen = paintPen.MainWindow(
            self.screen().geometry(), self.color, self.penWidth
        )
        self.pen.show()

    def hidePen(self):
        self.pen.close()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow(app.primaryScreen().geometry())
    window.show()
    app.exec()
