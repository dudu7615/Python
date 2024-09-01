import pyttsx3
import Ui_ui
from PySide6.QtWidgets import *


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Reader")
        self.initUI()

    def initUI(self):
        """定义控件"""

        self.ui.openFile.clicked.connect(self.open_file)

        self.ui.read.clicked.connect(self.read)

    def open_file(self):
        """打开文件"""
        try:
            name = QFileDialog.getOpenFileName(
                self, "打开文件", "./", "文本文档 (*.txt);;所有文件(*)"
            )
            file1 = open(name[0], encoding="utf8")
            self.ui.text.setPlainText(file1.read())
        except:
            pass

    def read(self):
        """朗读文本框文字"""
        text = self.ui.text.toPlainText()
        pyttsx3.speak(text)


app = QApplication([])
ui = UI()
ui.show()
app.exec()
