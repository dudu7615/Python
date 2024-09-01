import win32con
import win32gui
from pathlib import Path
from .log import logger


def setBackGroundImg(imgPath: Path):
    """设置壁纸"""
    logger.debug("开始设置壁纸")
    win32gui.SystemParametersInfo(
        win32con.SPI_SETDESKWALLPAPER, 
        str(imgPath), 
        win32con.SPIF_SENDWININICHANGE
    )
