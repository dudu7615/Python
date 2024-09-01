r"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
"""

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui import *
import yaml


with open("config.yml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textNum = 0
        self.ui = Ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("白板")
        self.setWindowIcon(QIcon(QPixmap(":/icon.ico")))
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.ui.textEdit.click.connect(self.mousePressEvent)
        self.ui.textEdit.setStyleSheet(f"font: {config['font']};")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        flags = self.windowFlags()
        if event.key() == Qt.Key.Key_F11:
            if Qt.WindowType.WindowStaysOnTopHint not in flags:
                flags = flags | Qt.WindowType.WindowStaysOnTopHint
            else:
                flags = flags & ~Qt.WindowType.WindowStaysOnTopHint
        elif event.key() == Qt.Key.Key_F12:
            if Qt.WindowType.ToolTip not in flags:
                flags = flags | Qt.WindowType.ToolTip
            else:
                flags = flags & ~Qt.WindowType.ToolTip
        self.setWindowFlags(flags)
        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            try:
                self.ui.textEdit.append(config["text"][self.textNum])
                self.textNum += 1
            except:
                ...


app = QApplication([])
ui = UI()
ui.show()
app.exec()
