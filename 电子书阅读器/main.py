r"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / -||||| -:- |||||- \
               |   | \\\  - ///  |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  '. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       '=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
"""

import re
import sys
from pathlib import Path

import download
import yaml
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import *

ROOT = Path(
    Path(sys.executable).parent
    if getattr(sys, "frozen", False)
    else Path(__file__).parent / "__"
)  # 判断程序是否被打包
ROOT.mkdir(exist_ok=True)  # 创建文件夹


try:
    with open(ROOT / "novelReaderSetting.yaml", encoding="utf8") as f:
        """读取配置文件"""
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    with open(config["path"], encoding="utf8") as f:
        """读取小说文件"""
        text = f.read()
    novelList = re.findall(config["re"], text)  # 小说目录
    novelText_ = re.split(f'({config["re"]})', text)[1:]
    novelText = [  # 小说正文
        i + novelText_[novelText_.index(i) + 1]
        for i in novelText_
        if novelText_.index(i) % 2 == 0
    ]
    del novelText_

except:
    config = {
        "ScrollBarValue": 0,
        "hideScrollBar": True,
        "num": 0,
        "path": "",
        "re": "第.+章 .+",
        "style": {
            "color": {"background": "#ffffff", "foreground": "#000000"},
            "font": {"font-family": "Microsoft YaHei UI", "size": 20},
        },
    }
    text = ""


class mainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainUi = ui_main.Ui_MainWindow()
        self.mainUi.setupUi(self)
        self.setWindowTitle("电子书阅读器")
        self.setWindowIcon(QIcon(QPixmap(":/icon/icon.ico")))
        self.initUI()

    def initUI(self):
        self.setStyleAndScrollBar()

        try:
            self.setNovelList()
            self.setText(novelText[config["num"]])
        except:
            ...
        self.mainUi.open.triggered.connect(self.opener)
        self.mainUi.enterRe.triggered.connect(self.openEnterRe)
        self.mainUi.openList.triggered.connect(self.openList)
        self.mainUi.setFont.triggered.connect(self.openSetting)
        self.mainUi.startDownload.triggered.connect(self.download)
        self.mainUi.showNovelList.clicked.connect(self.listClicked)
        self.mainUi.text.changePassage.connect(
            self.textClicked
        )  # 使用重写的QTextEdit以便使用changePassage信号进行换章
        self.mainUi.text.verticalScrollBar().valueChanged.connect(
            lambda value: (exec('config["ScrollBarValue"] = value'), self.saveYaml())
        )  # 保存滚动条位置
        self.mainUi.text.setContextMenuPolicy(
            Qt.ContextMenuPolicy.NoContextMenu
        )  # 禁用右键菜单
        self.mainUi.text.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )  # 禁止选择文字

    def setNovelList(self):
        # 设置小说目录
        self.mainUi.showNovelList.clear()  # 清除旧目录
        self.novelList:list[QTreeWidgetItem] = []
        for i in novelList:
            bookList = QTreeWidgetItem(self.mainUi.showNovelList)
            bookList.setText(0, i)
            self.novelList.append(bookList)
            self.mainUi.showNovelList.addTopLevelItem(bookList)

    def listClicked(self, _):
        """选择后进行处理"""
        item = self.mainUi.showNovelList.currentItem()
        self.comePassage(item.text(0))

    def setStyleAndScrollBar(self):
        """设置样式"""
        self.mainUi.text.setStyleSheet(
            (
                f"background-color: {config['style']['color']['background']};"
                f"color: {config['style']['color']['foreground']};"
                f"font-size: {config['style']['font']['size']}px;"
                f"font-family: \"{config['style']['font']['font-family']}\";"
            )
        )

        if config["hideScrollBar"]:
            self.mainUi.text.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            )
        else:
            self.mainUi.text.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded
            )

    def opener(self):
        """打开文件"""
        global text

        fileName = QFileDialog.getOpenFileName(
            self, "选取文件", "./", "文本文件 (*.txt);;所有文件 (*)"
        )
        if fileName[0]:
            config["path"] = fileName[0]
            with open(fileName[0], encoding="utf8") as f:
                text = f.read()
            self.makeList(text)
            self.setText(self.setText(novelText[config["num"]]))

    def openEnterRe(self):
        """打开正则表达式输入界面"""
        self.enterReUi = enterReUI()
        self.enterReUi.signal.connect(self.makeList)  # 在完成输入后生成目录
        self.enterReUi.show()

    def openList(self):
        """打开目录"""
        self.mainUi.dockWidget.show()
        # self.listUi = listUI()
        # self.listUi.signal.connect(self.comePassage)  # 在点击目录后跳转到对应章节
        # self.listUi.show()

    def openSetting(self):
        """打开设置"""
        self.settingUi = settingUI()
        self.settingUi.signal.connect(self.setStyleAndScrollBar)  # 在设置完成后重新设置文本
        self.settingUi.show()

    def download(self):
        """下载小说"""
        self.downloadUi = download.UI()
        self.downloadUi.show()

    def makeList(self, text: str):
        """生成目录"""
        global novelText, novelList

        novelList = re.findall(config["re"], text)
        novelText_ = re.split(f'({config["re"]})', text)[1:]
        novelText = [  # 生成正文（每章一个项目）
            i + novelText_[novelText_.index(i) + 1]
            for i in novelText_
            if novelText_.index(i) % 2 == 0
        ]
        del novelText_
        self.setNovelList()

    def setText(self, text: str):
        """将文本转换为html并显示"""
        self.mainUi.text.setText(text)
        self.saveYaml()
        self.setMessage()

    def comePassage(self, passage: str):
        """跳转到某一章"""
        config["num"] = novelList.index(passage)
        self.setText(novelText[novelList.index(passage)])

        # 设置选择的章节
        self.mainUi.showNovelList.setCurrentItem(self.novelList[config["num"]])

    def setMessage(self):
        """设置消息栏"""
        try:
            self.mainUi.massager.showMessage(
                f"{round((config['num']+1)/len(novelList)*100,2)} % ({novelList[config['num']]})"
            )
        except:
            self.mainUi.massager.showMessage("错误！目录为空")

    def saveYaml(self):
        """保存设置"""
        with open(ROOT / "novelReaderSetting.yaml", "w+", encoding="utf8") as f:
            f.write(yaml.dump(config, indent=2, allow_unicode=True))

    def textClicked(self, msg: int):
        try:
            if msg == 0:
                self.comePassage(novelList[config["num"] + 1])

            elif msg == 1:
                self.comePassage(novelList[config["num"] - 1])
                self.mainUi.text.verticalScrollBar().setValue(
                    self.mainUi.text.verticalScrollBar().maximum()
                )
        except:
            ...

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_F11:
            if Qt.WindowType.WindowStaysOnTopHint not in self.windowFlags():
                flags = self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint
            else:
                flags = self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint
            self.setWindowFlags(flags)
            self.show()
        elif event.key() == Qt.Key.Key_F12:
            if Qt.WindowType.ToolTip not in self.windowFlags():
                flags = self.windowFlags() | Qt.WindowType.ToolTip
            else:
                flags = self.windowFlags() & ~Qt.WindowType.ToolTip
            self.setWindowFlags(flags)
            self.show()


class enterReUI(QDialog):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = ui_enterRe.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("输入正则表达式")
        self.initUI()

    def initUI(self):
        self.ui.re.setText(config["re"])
        self.ui.ok.clicked.connect(self.enter)

    def enter(self):
        config["re"] = self.ui.re.text()
        self.signal.emit(text)
        self.close()


class listUI(QDialog):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = ui_list.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("目录")
        self.initUI()

    def initUI(self):
        self.ui.show.clear()  # 清除旧目录
        for i in novelList:
            bookList = QTreeWidgetItem(self.ui.show)
            bookList.setText(0, i)
            self.ui.show.addTopLevelItem(bookList)
        self.ui.show.clicked.connect(self.listClicked)

    def listClicked(self, _):
        """选择后进行处理"""
        item = self.ui.show.currentItem()
        self.signal.emit(item.text(0))
        self.close()


class settingUI(QDialog):
    signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_setting.Ui_Dialog()
        self.ui.setupUi(self)
        self.fontColor = "#000000"
        self.backGroundColor = "#ffffff"
        self.setWindowTitle("设置字体")
        self.initUI()

    def initUI(self):
        self.ui.font.setCurrentFont(QFont(config["style"]["font"]["font-family"]))
        self.ui.size.setValue(config["style"]["font"]["size"])
        self.ui.hideScrollBar.setChecked(config["hideScrollBar"])
        self.fontColor = config["style"]["color"]["foreground"]
        self.backGroundColor = config["style"]["color"]["background"]

        self.ui.ok.clicked.connect(self.finishSetting)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.chooseFontColor.clicked.connect(self.chooseFontColor)
        self.ui.chooseBackGroundColor.clicked.connect(self.chooseBackGroundColor)
        self.ui.size.textChanged.connect(self.settingChanged)
        self.ui.font.currentFontChanged.connect(self.settingChanged)
        self.ui.showText.setStyleSheet(
            f'{config["style"]}background-color: {self.backGroundColor};color: {self.fontColor};'
        )

    def settingChanged(self):
        self.styles = (
            f"background-color: {self.backGroundColor};"
            f"color: {self.fontColor};"
            f"font-size: {self.ui.size.value()}px;"
            f'font-family: "{self.ui.font.currentText()}";'
        )
        self.ui.showText.setStyleSheet(self.styles)
        config["style"]["color"]["background"] = self.backGroundColor
        config["style"]["color"]["foreground"] = self.fontColor
        config["style"]["font"]["font-family"] = self.ui.font.currentText()
        config["style"]["font"]["size"] = self.ui.size.value()

    def chooseFontColor(self):
        """选择字体颜色"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.fontColor = color.name()
            self.settingChanged()

    def chooseBackGroundColor(self):
        """选择背景颜色"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.backGroundColor = color.name()
            self.settingChanged()

    def finishSetting(self):
        """完成设置"""
        self.hideScrollBar = self.ui.hideScrollBar.isChecked()
        self.settingChanged()
        self.signal.emit()
        self.close()

    def exit(self):
        """退出设置"""
        self.signal.emit()
        self.close()


app = QApplication([])
ui = mainUI()
ui.show()
ui.mainUi.text.verticalScrollBar().setValue(
    int(config["ScrollBarValue"])
)  # 设置滚动条位置（在窗口显示前无效）
sys.exit(app.exec())
