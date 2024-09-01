from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ShowColor(QWidget):
    def __init__(self,parent: QWidget | None = ...,):
        super().__init__(parent)
        self.color = (255,0,0,255)
        self.penWeigh = 10

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QColor(*self.color))
        painter.setBrush(QColor(*self.color))
        # 在中心画一个圆
        painter.drawEllipse(self.rect().center(),self.penWeigh,self.penWeigh)


if __name__ ==  "__main__":
    app = QApplication([])
    win = ShowColor()
    win.show()
    app.exec()

from ui import ui_ui
