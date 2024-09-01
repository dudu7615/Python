from PIL import Image, ImageDraw, ImageFont
from .log import logger
import datetime
from pathlib import Path
# import yaml
import time
from models import *

ROOT = Path(__file__).parent.parent
IMGS_PATH = ROOT / "clock"

def weatherImg(
    path: Path,
    size: tuple[int, int],
    place: tuple[float, float],
    weather: str,
    font: Font,
    fill: tuple[int, int, int],
):
    """绘制天气图片保存到path"""
    textFont = ImageFont.truetype(font=font.name, size=font.size)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(img).text(place, weather, font=textFont, fill=fill)
    img.save(path / "weather.png")
    logger.debug("绘制天气图片成功")


def examDaysImg(
    path: Path,
    size: tuple[int, int],
    place: tuple[float, float],
    days: str,
    font: tuple[str, int],
    fill: tuple[int, int, int],
):
    """中考剩余时间"""
    textFont = ImageFont.truetype(*font)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(img).text(place, f"中考剩余{days}天", font=textFont, fill=fill)
    img.save(path / "exam.png")
    logger.debug("绘制中考时间图片成功")


def BgImg(path: Path, size: tuple[int, int], *imgs: str):
    """合成背景图片"""
    logger.debug("开始合成背景图片")
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    for imgPath in imgs:
        logger.debug(f"正在合成背景图片{imgPath}")
        new = Image.open(path / imgPath).convert("RGBA")
        img.alpha_composite(new)
    img.save(path / "result.png")
    logger.debug("合成背景图片成功")
