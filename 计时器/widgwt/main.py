import sys
from threading import Thread

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtTextToSpeech import QTextToSpeech
from qt_material import apply_stylesheet
from ui import *


class Timer(QThread):
    signal = Signal(int)
    paused = False

    def __init__(self):
        super().__init__()
        self.mutex = QMutex()
        self.pauseCond = QWaitCondition()
        self.secs = 0

    def run(self):
        for i in range(1,self.secs+1):
            self.sleep(1)
            self.mutex.lock()

            if self.paused:
                self.pauseCond.wait(self.mutex)
            self.mutex.unlock()

            self.signal.emit(self.secs-i)

    def pause(self):
        self.mutex.lock()
        self.paused = True
        self.mutex.unlock()

    def resume(self):
        self.mutex.lock()
        self.paused = False
        self.pauseCond.wakeAll()
        self.mutex.unlock()


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ui.Ui_Ui()
        self.ui.setupUi(self)
        self.setWindowTitle("计时器")
        self.setWindowIcon(QIcon(QPixmap(":/icon.ico")))
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # 设置置顶
        

        self.timer = Timer()
        self.timer.signal.connect(self.callBack)

        xpt = self.width() *(100.0/415)
        ypt = self.height() *(100.0/260)
        self.pt = int(min(xpt,ypt))

        self.mins = 0
        self.initUI()
    def initUI(self):
        self.ui.setTime.valueChanged.connect(self.timeChanged)
        self.ui.start.clicked.connect(self.start)
        self.timer.signal.connect(self.callBack)

    def speak(self, text: str):
        QTextToSpeech().say(text)

    def getTime(self,text:str):
        return f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">p, li {{ white-space: pre-wrap; }}hr {{ height: 1px; border-width: 0; }}li.unchecked::marker {{ content: \"\2610\"; }}li.checked::marker {{ content: \"\2612\"; }}</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\"><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:{self.pt}pt; font-weight:700;\">{text}</span></p></body></html>"

    def timeChanged(self,min:int):
        self.mins = min
        self.timer.terminate()
        self.ui.start.setChecked(False)
        self.ui.showTime.setText(self.getTime(f"{self.mins:02d}:00"))

    def start(self,run:bool):
        if self.timer.isRunning():
            if run:
                self.ui.start.setText("正在计时")
                self.timer.pause()
                self.timer.start()
            else:
                self.timer.pause()
                self.ui.start.setText("计时暂停")
        else:
            if run:
                self.ui.start.setText("计时开始")
                self.timer.secs = self.mins * 60
                self.timer.start()
                self.ui.showTime.setText(self.getTime(f"{self.mins:02d}:00"))
            else:
                self.timer.pause()
                self.ui.start.setText("计时暂停")

    def callBack(self, msg: int):
        self.ui.showTime.setText(self.getTime(f"{msg//60:02d}:{msg%60:02d}"))
        # self.ui.showTime.display(secs - (msg + 1))
        if msg ==0:
            Thread(target=self.speak, args=(f"{self.mins}分钟计时完成",)).start()

            reply = QMessageBox.information(
                self, "时间到", f"{self.mins}分钟 计时完成\n按<OK>键关闭程序",
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)

            if reply.name == "Close":
                sys.exit()

    def resizeEvent(self, event: QResizeEvent) -> None:
        size = event.size()
        xpt = size.width() *(100.0/415)
        ypt = size.height() *(100.0/260)
        self.pt = int(min(xpt,ypt))
        self.ui.showTime.setText(self.getTime(self.ui.showTime.toPlainText()))



app = QApplication([])
# apply_stylesheet(app, theme='dark_blue.xml')
ui = UI()
ui.show()
sys.exit(app.exec())
