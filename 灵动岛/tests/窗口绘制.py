import sys  
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
  
class RoundedWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
  
        self.setWindowTitle('Rounded Window')  
        self.setGeometry(300, 300, 500, 400)  
  
        # 设置窗口的背景为透明  
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
 
  
    def paintEvent(self, event:QPaintEvent):  
        # 创建QPainter对象  
        painter = QPainter(self)  
  
        # 创建QPainterPath对象，用于绘制带有圆角的矩形  
        path = QPainterPath()  
        rect = QRect(0, 0, self.width(), self.height())  
        radius = 100.0  
        path.addRoundedRect(rect, radius, radius)  
  
        # # 设置画笔的颜色和宽度  
        # painter.setPen(Qt.NoPen)  
        painter.setBrush(QColor("#FFFFFF"))  # 设置画笔
  
        # 绘制带有圆角的矩形，并将其设置为窗口的背景  
        painter.drawPath(path)  
  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    window = RoundedWindow()  
    window.show()  
    sys.exit(app.exec())