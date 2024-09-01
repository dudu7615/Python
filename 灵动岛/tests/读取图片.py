import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PIL import Image
from pathlib import Path


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle("Canvas")
        # self.readImg()
        self.show()

    def readImg(self, path: Path):
        savePath = Path(__file__).parent / "data" / path.name
        img = Image.open(path)
        newImg = img.resize((500, 500))
        newImg.save(savePath)
        

        return savePath

    def paintEvent(self, _):
        qp = QPainter(self)
        # qp.begin(self)
        self.drawRectangles(qp)
        # qp.end()

    def drawRectangles(self, qp: QPainter):
        qp.drawImage(
            QPoint(0, 0),
            QImage(
                self.readImg(Path(r"D:\dudu\Documents\dudu\python\计时器\ui\icon.ico"))
            ),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Canvas()
    sys.exit(app.exec())
