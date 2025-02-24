import sys
import yaml
import asyncio
from datetime import datetime
from pathlib import Path
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from models import *


ROOT = Path(__file__).parent
IMGS_PATH = ROOT / "clock"

_config = yaml.load(
    (IMGS_PATH / "config.yml").read_text(encoding="utf-8"), Loader=yaml.FullLoader
)
config = Config(
    name=_config["name"],
    size=(_config["size"][0], _config["size"][1]),
    font=Font(*_config["font"]),
    color=(_config["color"][0], _config["color"][1], _config["color"][2]),
    place=_config["place"],
)


@logger.catch
async def img():
    logger.info("开始运行图片模块运行")
    i = True  # 是否是第一次
    nowTime = datetime.now()
    # logger.debug(f"{self.config}")
    while True:
        logger.debug(f"{datetime.now().minute} {nowTime.minute}")
        if datetime.now().minute != nowTime.minute or i:
            nowTime = datetime.now()
            makeImg.BgImg(
                IMGS_PATH,
                config.size,
                "bg.jpg",
                "weather.png",
                # "exam.png",
                f"month{nowTime.month}.png",
                f"day{nowTime.day}.png",
                f"hour{nowTime.hour}.png",
                f"minute{nowTime.minute}.png",
                f"weekday{nowTime.weekday()+1}.png",
            )
            setBg.setBackGroundImg(IMGS_PATH / "result.png")

            if i:
                i = False
        await asyncio.sleep(10)



@logger.catch
async def weater():
    logger.info("开始运行天气模块")
    i = True  # 是否是第一次
    while True:
        logger.debug(f"{datetime.now().minute}")
        if datetime.now().minute == 0 or i:
            makeImg.weatherImg(
                IMGS_PATH,
                config.size,
                config.place["weather"],
                weather.getweather(),
                config.font,
                config.color,
            )
            if i:
                i = False
        await asyncio.sleep(50)


class TrayIcon(QSystemTrayIcon):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(str(ROOT / "icon.ico")))
        self.initUI()

    def initUI(self):
        self.menu = QMenu()
        # self.menu.addAction("显示主窗口")
        self.menu.addAction("退出")
        self.setContextMenu(self.menu)
        self.menu.triggered.connect(self.clickEvent)

    def clickEvent(self, action: QAction):
        """点击托盘菜单时触发"""

        sys.exit()

async def run():
    await asyncio.gather(weater(), img())

@logger.catch
def main():
    logger.info("程序启动")
    asyncio.run(run())
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    tray = TrayIcon()
    tray.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
