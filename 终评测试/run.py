r"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \|     |// '.
                 / \|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\  - /// |   |
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


import main
import Ui_ui
import datetime
from PySide6.QtWidgets import *

class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("李昊轩终评测试题")
        self.ui = Ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.run.clicked.connect(self.start)

    def start(self):
        startDate = self.ui.start.text()
        y,m,d = startDate.split("/")
        start = datetime.datetime(int(y),int(m),int(d))

        endDate = self.ui.end.text()
        y,m,d = endDate.split("/")
        end = datetime.datetime(int(y),int(m),int(d))
        
        self.ui.result.setText(f"共跑了 {main.main(start,end)}公里")

app = QApplication([])
ui = Ui()
ui.show()
app.exec()
