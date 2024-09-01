from dataclasses import dataclass
from pathlib import Path
# from tools import Tools
# from PySide6.QtWidgets import QWidget


@dataclass
class Icon:
    # // 图片
    path: Path
    command: str



@dataclass
class Confog:
    """配置文件"""

    height: int
    icons: list[Icon]
    iconSize: int
    whiteSize: int
    leftAndRight: int

