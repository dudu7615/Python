from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PIL import Image
from pathlib import Path
from dataTypes import *
from os import system

TOOLS_PATH = Path(__file__).parent / "tools"


config = Confog(
    height=50,
    icons=[
        Icon(TOOLS_PATH/"clock"/"icon.ico", "echo icon"),
        Icon(TOOLS_PATH/"paintPen"/"icon.ico", "echo icon1"),
    ],
    # ! 打包时使用
    # icons=[
    #     Icon(TOOLS_PATH/"clock"/"icon.ico", str(TOOLS_PATH/"clock"/"main.exe")),
    #     Icon(TOOLS_PATH/"paintPen"/"icon.png", str(TOOLS_PATH/"paintPen"/"main.exe")),
    # ],
    iconSize=40,
    whiteSize=5,
    leftAndRight=30,
)


class MainWindow(QMainWindow):
    def __init__(self, screen: QRect):
        super().__init__()

        weigh = (len(config.icons) * config.iconSize) + (config.leftAndRight * 2)
        place = (screen.width() // 2 - config.height // 2, 0)

        self.setWindowTitle("灵动岛")
        self.setGeometry(*place, weigh, config.height)

        # 设置窗口的背景为透明
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips)  # 设置窗口在失去焦点时仍然保持显示

    def paintEvent(self, event: QPaintEvent):
        """绘制窗口"""
        super().paintEvent(event)
        # 创建QPainter对象
        painter = QPainter(self)

        # 创建QPainterPath对象，用于绘制带有圆角的矩形
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        radius = 30.0
        path.addRoundedRect(rect, radius, radius)

        # # 设置画笔的颜色和宽度
        # painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#FFFFFF"))  # 设置画笔

        # 绘制带有圆角的矩形，并将其设置为窗口的背景
        painter.drawPath(path)

        self.paitmIcon(painter)

    def paitmIcon(self,painter: QPainter):
        """绘制图标"""
        size = config.height - (config.whiteSize + config.whiteSize)

        for icon in config.icons:
            # 加载图标
            img = QImage(icon.path).scaled(
                QSize(
                    size,
                    size,
                )
            )
            # 计算图标的位置
            place = config.leftAndRight + (
                size + config.whiteSize
            ) * config.icons.index(icon)
            # 绘制图标
            painter.drawImage(QPoint(place, 5), img)
        # self.update()

    def mousePressEvent(self, event: QMouseEvent):
        """鼠标点击事件"""
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.pos()
            index = (pos.x() - config.leftAndRight) // (
                config.height - (config.whiteSize + config.whiteSize)
            )
            if index < len(config.icons):
                system(config.icons[index].command)

    def readImg(self, path: Path):
        # // 保存图片
        savePath = Path(__file__).parent / "data" / path.name
        try:
            savePath.unlink()
        except:
            ...
        img = Image.open(path)
        newImg = img.resize((40, 40))
        newImg = newImg.convert("RGB")
        newImg.save(savePath)
        with open(path, "rb") as f:
            byte = f.read()

        return Icon(savePath, byte, (40, 40))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow(app.primaryScreen().geometry())
    window.show()
    app.exec()
