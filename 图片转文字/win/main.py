from os import popen,listdir
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import Ui_ui
import sys

ocr = f'{sys.path[0]}\\ocrMain.exe'

class Main(QObject):
    signal = Signal(str)
 
    def __init__(self):
        super().__init__()
        self.flag = True
 

    def run(self):
        """ 核心程序 """
        ok = ''
        long = len(path)
        
        for file in path:
            now = path.index(file)
            x = popen(f'{ocr} {file}', "r").read()

            ok += f'文件 "{file}" 识别结果：\n {x}'
            prog = (now+1) / long * 100
            self.signal.emit(f'{ok}#-#{prog}')

class UI(QMainWindow):
    _startThread = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_ui.Ui_MainWinsow()
        self.ui.setupUi(self)
        self.setWindowTitle("OCR 图片转文字")
        self.initUI()

        self.myT = Main()
        self.thread = QThread(self)
       
        self.myT.moveToThread(self.thread)
        self._startThread.connect(self.myT.run)
        self.myT.signal.connect(self.call_backlog)


    def initUI(self):
        self.ui.chooseDir.clicked.connect(self.chooseDir)
        self.ui.chooseFile.clicked.connect(self.chooseFile)
        self.ui.run.clicked.connect(self.start)

        self.ui.showText.setReadOnly(True)

        self.ui.prog.setValue(0)


    def chooseFile(self):
        global path
        try:
            path = QFileDialog.getOpenFileName(self,"打开文件","./","所有文件(*)")[:-1]
            self.ui.showPath.setText(str(path))
        except:
            pass

    def chooseDir(self):
        global path
        path = []
        try:
            path0 = QFileDialog.getExistingDirectory(self,"打开文件夹","./")
            path1 = listdir(path0)
            path.extend(f'{path0}/{x}' for x in path1)
            print(path)
            self.ui.showPath.setText(path0)
        except:
            pass

    def start(self):

        self.ui.prog.setValue(0)
        
        self.myT.flag = True
        self.thread.start()
        
        self._startThread.emit()

    def call_backlog(self, msg):
        x = str(msg).split('#-#')
        self.ui.showText.setPlainText(x[0])
        self.ui.prog.setValue(int(float(x[1])))

app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec())
