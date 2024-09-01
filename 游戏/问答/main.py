from PySide6.QtWidgets import *
from PySide6.QtCore import *
# from PySide6.QtGui import *
import Ui
import re
import sys
import random 

ques_ = 'aaa,,A;;bbb,,B;;ccc,,C'
ques_ = re.split(';;', ques_)
num = len(ques_)

print(num)


class UI(QMainWindow):
    def __init__(self):
        self.NumAll = 0
        self.NumRight = 0
        super().__init__()
        self.ui = Ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.ui.start.clicked.connect(self.start)
        self.ui.A.clicked.connect(self.ChooseA)
        self.ui.B.clicked.connect(self.ChooseB)
        self.ui.C.clicked.connect(self.ChooseC)
        self.ui.Open.clicked.connect(self.OpenTxt)

    def OpenTxt(self):
        global ques_,num
        path = QFileDialog.getOpenFileName(self,"打开文件","./","文本文档 (*.txt);;所有文件(*)")
        ques_ = open(path[0],encoding='utf8').read()
        ques_ = re.split(';;', ques_)
        num = len(ques_)

    def start(self):
        self.setShow()

    def setShow(self):
        self.num = random.sample(range(num), 1)[0]
        ques = ques_[self.num]
        self.ques = re.split(',,', ques)
        self.ui.Show.setText(self.ques[0])
        self.ui.show1.setText(f'分数：{self.NumRight}')
        self.ui.show2.setText(f'次数：{self.NumAll}')

    def ChooseA(self):
        self.choose('A')
        
    def ChooseB(self):
        self.choose('B')

    def ChooseC(self):
        self.choose('C')

    # Rename this here and in `ChooseA`, `ChooseB` and `ChooseC`
    def choose(self, arg0):
        if self.ques[1] == arg0:
            self.NumRight += 1
        else:
            self.NumRight -= 1
        self.NumAll += 1
        self.setShow()


app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec())
