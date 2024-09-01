from aip import AipOcr
from os import listdir
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import Ui_ui
import sys

class Main(QObject):
    Thread = Signal(str)

    def __init__(self):
        super().__init__()
        # self.flag = True

    def run(self):
        """ 核心程序 """
        global result
        APP_ID = '30347098'
        API_KEY = 'uCCdCzL9aQQYf6wDF9KlVmzm'
        SECRET_KEY = 'VnaP7543j3Xr13d5WATcbl8q6I8rsIWa'

        ocrMain = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        def readImg(filePath: str):
            """ 读取文件 """
            with open(filePath, "rb") as fp:
                return fp.read()

        def imgToText(imgPath: str):
            """ 调用通用文字识别API """
            image = readImg(imgPath)

            options = {
                "language_type": "CHN_ENG",
                "detect_direction": "true",
                "detect_language": "true",
                "probability": "false",
            }
            result = eval(str(ocrMain.basicAccurate(image, options)))
            return "".join(res["words"] + "\n" for res in result["words_result"])

        # 返回进度条数字，将结果保存为{文件名:内容}的格式
        long = len(path)
        result = {}
        prog = 0
        for file in path:
            try:
                now = path.index(file)
                text = imgToText(file)

                result[file] = text
                prog = (now+1) / long * 100
            except:
                result[file] = "识别失败"

            self.Thread.emit(str(int(prog)))
        self.Thread.emit(str(int(prog)))


class UI(QMainWindow):
    Thread = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("图片转文字")
        self.initUI()

        self.ocrTheard = Main()
        self.threader = QThread(self)

        self.ocrTheard.moveToThread(self.threader)
        self.Thread.connect(self.ocrTheard.run)
        self.ocrTheard.Thread.connect(self.callBack)

    def initUI(self):
        self.ui.chooseDir.clicked.connect(self.chooseDir)
        self.ui.chooseFile.clicked.connect(self.chooseFile)
        self.ui.run.clicked.connect(self.start)
        self.ui.save.clicked.connect(self.save)

        self.ui.showText.setReadOnly(True)

        self.ui.prog.setValue(0)

    def chooseFile(self):
        global path
        try:
            path = QFileDialog.getOpenFileName(
                self, "打开文件", "./", "所有文件(*)")[:-1]
            self.ui.showPath.setText(str(path))
        except:
            pass

    def chooseDir(self):
        global path
        path = []
        try:
            path0 = QFileDialog.getExistingDirectory(self, "打开文件夹", "./")
            path1 = listdir(path0)
            path.extend(f'{path0}/{x}' for x in path1)
            print(path)
            self.ui.showPath.setText(path0)
        except:
            pass

    def save(self):
        try:
            savePath = QFileDialog.getExistingDirectory(self, "打开文件夹", "./")
        except:
            ...

        # 保存
        for fileName in list(result.keys()):
            with open(f'{savePath}/{str(fileName).split("/")[-1]}.txt', 'w', encoding='utf-8') as f:
                f.write(result[fileName])

        # 弹窗提示
        reply = QMessageBox.information(
            self,
            '保存完成',
            f'<font size="3">已保存到 <b>{savePath}</b></font>',
            QMessageBox.StandardButton.Close,
        )
        reply = str(reply)
        if reply == 'StandardButton.Close':
            sys.exit()

    def start(self):
        self.ui.prog.setValue(0)

        # self.myT.flag = True
        self.threader.start()

        self.Thread.emit()

    def callBack(self, msg: str):
        self.ui.prog.setValue(int(msg))
        if msg == "100":
            text = "".join(f"{x}:\n{result[x]}" for x in list(result.keys()))
            self.ui.showText.setPlainText(text)


app = QApplication([])
ui = UI()
ui.show()
sys.exit(app.exec())
