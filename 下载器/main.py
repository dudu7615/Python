from pathlib import Path

import download
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import *

ROOT = Path(__file__).parent


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("多线程下载器")
        self.initUI()

    def initUI(self):
        self.ui.start.clicked.connect(self.start)

    def start(self):
        url = self.ui.url.text()
        bitSize = int(self.ui.bitSize.text()[:-1]) * 1024**2
        self.ui.savePath.setText(str(ROOT / Path(url).name))

        self.download = download.downloader(basePath=ROOT, url=url, bitSize=bitSize)
        self.download.info.connect(self.ui.info.append)
        self.download.finished.connect(self.finish)
        self.download.start()

    def finish(self):
        QMessageBox.information(self, "下载完成", "下载完成")


if __name__ == "__main__":
    app = QApplication([])
    ui = MainUI()
    ui.show()
    app.exec()
