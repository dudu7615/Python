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


import asyncio
import datetime
import sys
import time

import aiohttp
import requests
from lxml import etree
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from ui import Ui_download

downloadSet = {
    "url"       : "http://www.biquge66.net",
    "list"      : '//*[@id="list"]/div/li/a/@href',
    "bookTittle": '//*[@id="info"]/h1/text()',
    "tittle"    : '// *[@id = "wrapper"]/article/h1/text()',
    "text"      : '//*[@id="booktxt"]/p/text()',
}

searchSet = {
    "names": '//*[@id="main"]/div/div/div/dl/dt/a/text()',
    "links": '//*[@id="main"]/div/div/div/dl/dt/a/@href',
}

class Download(QThread):
    result = Signal(str)
    porgress = Signal(str)

    def run(self):
        global bookTittle
        self.porgress.emit(f"{datetime.datetime.now():%H:%M:%S} [开始下载]")
        response = requests.get(url)
        tree = etree.HTML(response.text)

        UrlList = tree.xpath(downloadSet["list"])
        bookTittle = tree.xpath(downloadSet["bookTittle"])[0]
        self.porgress.emit(f"{datetime.datetime.now():%H:%M:%S} [已获取章节列表]")
        asyncio.run(self.download(UrlList))

    async def download(self, urlList: list):
        async with aiohttp.ClientSession(downloadSet["url"]) as session:
            tasks = [self.getter(url, session) for url in urlList]
            result = await asyncio.gather(*tasks)
            self.porgress.emit(f"{datetime.datetime.now():%H:%M:%S} [下载完成]")
            self.result.emit("".join(result))

    async def getter(self, url: str, session: aiohttp.ClientSession):
        for _ in range(tryTimes):
            try:
                async with await session.get(f"{url}") as resp:
                    page = await resp.text()
                tree = etree.HTML(page)
                tittle = tree.xpath(downloadSet["tittle"])[0]
                text = "".join(tree.xpath(downloadSet["text"]))
                # print(f"{tittle}")
                self.porgress.emit(f"{datetime.datetime.now():%H:%M:%S} [已下载] {tittle}")
                return f"{tittle}\n{text}\n"
            except:...
        self.porgress.emit(f"{datetime.datetime.now():%H:%M:%S} [下载失败] {url}")
        return f"{url} 下载失败\n"


class UI(QMainWindow):
    """gui界面"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_download.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("电子书下载器")
        self.initUI()

        self.download = Download()
        self.download.result.connect(self.finished)
        self.download.porgress.connect(self.ui.Info.append)

    def initUI(self):
        """定义控件"""
        self.ui.Run.clicked.connect(self.startDownload)
        self.ui.Saver.clicked.connect(self.Save)

        self.ui.search.clicked.connect(self.search)

    def Save(self):
        path = QFileDialog.getSaveFileName(
            self, "保存文件", "./", "文本文件 (*.txt);;所有文件(*.*)"
        )
        if path[0]:
            with open(path[0], "w+", encoding="utf8") as file:
                file.write(self.result)
            self.ui.Info.append(f"{datetime.datetime.now():%H:%M:%S} [已保存] {path[0]}")

    def search(self):
        params = (("searchkey", self.ui.enterBookName.text()),)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"
        }
        resp = requests.get(
            "http://www.biquge66.net/search/",
            headers=headers,
            params=params,
            verify=False,
        )

        html = etree.HTML(resp.text)

        names = html.xpath(searchSet["names"])
        links = html.xpath(searchSet["links"])

        urlDict = {names[n]: links[n] for n in range(len(names))}

        self.ui.showLinks.clear()

        for name in names:
            item = QTreeWidgetItem(self.ui.showLinks)
            item.setText(0, name)
            item.setText(1, urlDict[name])
            # item.setText(2, synopsisDict[name])
            self.ui.showLinks.addTopLevelItem(item)

        self.ui.showLinks.itemClicked.connect(self.runSearch)

    def runSearch(self, _):
        item = self.ui.showLinks.currentItem()
        self.ui.EntryNum.setText(f'{downloadSet["url"]}{item.text(1)}')

    def startDownload(self):
        global url,tryTimes
        if self.download.isRunning():
            return

        url = self.ui.EntryNum.text()
        tryTimes = self.ui.tryTimes.value()
        self.startTime = time.time()
        self.ui.PBar.setMaximum(0)  # 进度条设置忙状态
        self.download.start()

    def finished(self, msg):
        self.result = msg

        self.finishTime = time.time() - self.startTime

        # 恢复进度条
        self.ui.PBar.setMaximum(100)
        self.ui.PBar.setValue(100)

        # self.ui.Info.setText(self.result)
        reply = QMessageBox.information(
            self,
            "下载完成",
            f"{bookTittle}下载完成\n共用时{int(self.finishTime)}秒\n按<Save>保存为txt",
            QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Save,
        )

        if reply.name == "Save":
            self.Save()


if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    ui.show()
    sys.exit(app.exec())
