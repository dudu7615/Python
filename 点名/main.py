from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtGui import QIcon, QGuiApplication
from pathlib import Path
import os
import base64
import random
import sys

ROOT = Path(__file__).parent
DATA = Path(
    Path(os.environ["LocalAppData"]) / "点名器" / "data"
    if getattr(sys, "frozen", False)
    else ROOT
)  # 判断程序是否被打包
if not DATA.exists():
    DATA.mkdir(exist_ok=True, parents=True)
QML = ROOT / "Ui"

os.environ["QT_QUICK_CONTROLS_CONF"] = str(QML / "qtquickcontrols2.conf")

names: list[str] = eval(
    base64.decodebytes(
        (DATA / "names").read_text(encoding="utf-8").encode("utf-8")
    ).decode("utf-8")
)


class UI(QObject):
    def __init__(self):
        super().__init__()

    @Slot(result=str)
    def run(self):
        name = random.choice(names) if names else "没有名字了，重启程序以继续"
        try:
            names.remove(name)
        except:
            ...
        return name

    def saveData(self):
        code = base64.encodebytes(str(names).encode("utf-8"))
        (DATA / "names").write_text(code.decode("utf-8"), encoding="utf-8")


if __name__ == "__main__":
    app = QGuiApplication([])
    app.setWindowIcon(QIcon(str(ROOT / "icon.png")))

    qmlRegisterType(UI, "Py", 1, 0, "Py")

    engine = QQmlApplicationEngine()
    engine.addImportPath(QML)
    engine.addImportPath(QML / "imports")

    engine.load(QML / "main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
