from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import random 
import time
import Ui

class Main(QObject):
    #  通过类成员对象定义信号对象
    signal = Signal(str)
 
    def __init__(self):
        super().__init__()
        self.flag = True
 
    def run(self):
        """ 核心程序 """
        for _ in range(30):
            index = random.sample(range(3), 1)[0]
            self.signal.emit(f'{index}')
            time.sleep(1)

class UI(QMainWindow):
    """ gui界面 """
    
    _startThread = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui.Ui_MainWindow()
        self.num = 0
        self.ui.setupUi(self)

        self.myT = Main()          # 创建线程对象
        self.thread = QThread(self)     # 初始化QThread子线程
        # 把自定义线程加入到QThread子线程中
        self.myT.moveToThread(self.thread)
        self._startThread.connect(self.myT.run)     # 只能通过信号-槽启动线程处理函数
        self.myT.signal.connect(self.call_backlog)

        self.initUI()

    def initUI(self):
        """ 定义控件 """
        self.ui.Start.clicked.connect(self.start)
        self.ui.b1.clicked.connect(self.c1)
        self.ui.b2.clicked.connect(self.c2)
        self.ui.b3.clicked.connect(self.c3)

    def c1(self):
        if self.index == '1':
            self.num += 1
            self.ui.Show.setText(str(self.num))

    def c2(self):
        if self.index == '2':
            self.num += 1
            self.ui.Show.setText(str(self.num))

    def c3(self):
        if self.index == '3':
            self.num += 1
            self.ui.Show.setText(str(self.num))


    def start(self):
        if self.thread.isRunning():     # 如果该线程正在运行，则不再重新启动
            return
        self.myT.flag = True
        self.thread.start()
        self._startThread.emit()
 
    def call_backlog(self, msg):
        print(msg)
        self.index = msg
        if msg == '0':
            self.ui.a1.setPixmap(QPixmap(f"{sys.path[0]}\\a.png"))
            self.ui.a1.setScaledContents (True)
            self.ui.a2.setPixmap(QPixmap(""))
            self.ui.a3.setPixmap(QPixmap(""))
        elif msg == '1':
            self.ui.a2.setPixmap(QPixmap(f"{sys.path[0]}\\a.png"))
            self.ui.a2.setScaledContents (True)
            self.ui.a1.setPixmap(QPixmap(""))
            self.ui.a3.setPixmap(QPixmap(""))
        elif msg == '2':
            self.ui.a3.setPixmap(QPixmap(f"{sys.path[0]}\\a.png"))
            self.ui.a3.setScaledContents (True)
            self.ui.a2.setPixmap(QPixmap(""))
            self.ui.a1.setPixmap(QPixmap(""))

app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec())
