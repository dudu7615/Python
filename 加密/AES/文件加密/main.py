""" 
pip uninstall crypto
pip uninstall pycryptodome
pip install pycryptodome 
"""
from Crypto.Cipher import AES  # 加密器
import base64  # 需要进行编码
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
import ui_ui


class Main(QThread):
    Theard = Signal(str)

    def run(self):
        global result

        def add16(text0: str):
            text1 = text0.encode('utf8')
            while len(text1) % 16 != 0:
                text1 += b'\x00'
            return text1  # 返回bytes
        aes = AES.new(add16(password), AES.MODE_ECB)  # 创建一个aes对象

        if choose == "加密":
            enText = aes.encrypt(text)
            result = base64.encodebytes(enText)  # 执行加密并转码返回bytes

        elif choose == "解密":
            text0 = base64.decodebytes(text)
            result = aes.decrypt(text0)

        try:
            self.Theard.emit("")
        except:
            ...


class UI(QMainWindow):
    Thread = Signal()

    def __init__(self):
        super().__init__()
        self.ui = ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("AES 加密")
        self.initUI()

        self.myT = Main()
        self.thread = QThread(self)

        self.myT.moveToThread(self.thread)
        self.Thread.connect(self.myT.run)
        self.myT.Theard.connect(self.call_backlog)

    def initUI(self):
        self.ui.run.clicked.connect(self.start)
        self.ui.chooseFile.clicked.connect(self.readFile)

    def readFile(self):
        global text, fileName

        try:
            fileName = QFileDialog.getOpenFileName(
                self, "选择文件", "./", "所有文件(*.*)")[0]
            with open(fileName, 'rb') as f:
                text = f.read()

                while len(text) % 16 != 0:
                    text += b'\x00'

        except:
            ...

    def start(self):
        global password, choose

        password = self.ui.passwd.text()
        choose = self.ui.chooseMode.currentText()

        self.thread.start()
        self.Thread.emit()

    def call_backlog(self, msg):
        reply = QMessageBox.information(
            self, '完成', "完成\n按<Ok>保存到原位置\n按<Save>另存为",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Ok)

        reply = str(reply)

        if reply == 'StandardButton.Save':
            try:
                path = QFileDialog.getSaveFileName(
                    self, "保存文件", "./", "所有文件(*.*)")
                with open(path[0], 'wb') as file:
                    file.write(result)
            except:
                pass

        elif reply == 'StandardButton.Ok':
            with open(fileName, 'wb') as file:
                file.write(result)


app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec())
