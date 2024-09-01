from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(
        self,
        screen: QRect,
        color: tuple[int] = (255, 255, 255, 255),
        penWidth: int = 10,
    ):
        super().__init__()
        self.screenSize = screen

        self.color = QColor(*color)
        self.penWidth = penWidth

        self.lastPos = QPoint(0, 0)
        self.path = QPainterPath()
        self.setWindowTitle("屏幕批准")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(screen)

    def paintEvent(self, event: QPaintEvent):
        # 屏幕绘制
        rectPainter = QPainter(self)
        path = QPainterPath()
        rect = QRect(0, 0, self.screenSize.width(), self.screenSize.height())
        radius = 0.0
        path.addRoundedRect(rect, radius, radius)
        rectPainter.setBrush((QColor(0, 0, 0, 1)))
        rectPainter.drawPath(path)

        # 绘制路径
        pathPainter = QPainter(self)
        pathPainter.setPen(
            QPen(
                self.color,
                self.penWidth,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        pathPainter.drawPath(self.path)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """每次绘制时更新起始点"""
        self.lastPos = event.position()
        self.path.moveTo(self.lastPos)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.path.moveTo(self.lastPos)
        self.path.lineTo(event.position())

        self.lastPos = event.position()

        self.update()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow(app.primaryScreen().geometry())
    window.show()
    app.exec()
