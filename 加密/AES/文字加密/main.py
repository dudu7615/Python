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

class Main(QObject):
    signal = Signal(str)
 
    def __init__(self):
        super().__init__()
        self.flag = True
 
    def run(self):
        def add16(text0:str):
            text1 = text0.encode('utf8')
            while len(text1) % 16 != 0:
                text1 += b'\x00'
            return text1  # 返回bytes
            
        aes = AES.new(add16(password_),AES.MODE_ECB) #创建一个aes对象

        if choose == "加密":
            enText = aes.encrypt(add16(text_)) #加密明文
            result = str(base64.encodebytes(enText), encoding='utf-8')  # 执行加密并转码返回bytes

        elif choose == "解密":
            text0 = base64.decodebytes(text_.encode(encoding='utf-8'))
            result = str(aes.decrypt(text0),encoding='utf-8').replace('\x00','')  # 去除补位字符 

        try:  # 防止未做加密/解密选择
            self.signal.emit(result)
        except:
            pass

class UI(QMainWindow):
    _startThread = Signal()

    def __init__(self):
        super().__init__()
        self.ui = ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("AES 加密")
        self.initUI()

        self.myT = Main()
        self.thread = QThread(self)
       
        self.myT.moveToThread(self.thread)
        self._startThread.connect(self.myT.run)
        self.myT.signal.connect(self.call_backlog)


    def initUI(self):
        self.ui.run.clicked.connect(self.start)

    def start(self):
        global password_,text_,choose

        password_ = self.ui.passwd.text()
        text_ = self.ui.text.toPlainText()
        choose = self.ui.choose.currentText()

        self.myT.flag = True
        self.thread.start()
        self._startThread.emit()

    def call_backlog(self, msg):
        self.ui.text.setText(str(msg))

app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec())

