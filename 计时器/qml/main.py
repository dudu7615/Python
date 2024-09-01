from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import Slot, QThread, Signal, QObject, QMutex, QWaitCondition
from PySide6.QtGui import QIcon, QGuiApplication

import sys
import time
from threading import Thread
from win32com import client
from pathlib import Path
from Ui import *

QML = Path(__file__).parent / "Ui"

class Main(QThread):
    signal = Signal(int)
    paused = False

    def __init__(self):
        super().__init__()
        self.secs = 0
        self.mutex = QMutex()
        self.pauseCond = QWaitCondition()

    def run(self):
        for i in range(self.secs, -1, -1):
            self.mutex.lock()

            if self.paused:
                self.pauseCond.wait(self.mutex)
            self.mutex.unlock()

            self.signal.emit(i)
            time.sleep(1)

    def pause(self):
        self.mutex.lock()
        self.paused = True
        self.mutex.unlock()

    def resume(self):
        self.mutex.lock()
        self.paused = False
        self.pauseCond.wakeAll()
        self.mutex.unlock()


class UI(QObject):
    signal = Signal(str, arguments=["time"])

    def __init__(self):
        super().__init__()

        self.main = Main()
        self.main.signal.connect(self.callBack)

    @Slot(int)
    def changeTime(self, time: int):
        self.min = time
        self.main.terminate()
        self.signal.emit(f"{time:02d}:00")

    @Slot(bool)
    def start(self, start: bool):
        if start:
            if self.main.isRunning():
                self.main.resume()
                return
            self.main.secs = self.min * 60
            self.main.start()
        else:
            if self.main.isRunning():
                self.main.pause()
                return
            self.main.terminate()

    def speak(self, text: str):
        engine = client.Dispatch("SAPI.SpVoice")
        engine.Speak(text)

    def callBack(self, msg: int):
        min, sec = divmod(msg, 60)
        self.signal.emit(f"{min:02d}:{sec:02d}")

        if msg == 0 and self.min != 0:
            self.signal.emit(f"{min:02d}:{sec:02d}")
            Thread(target=self.speak, args=(f"{self.min}分钟计时完成",)).start()


if __name__ == "__main__":
    app = QGuiApplication([])
    app.setWindowIcon(QIcon(":/icon.ico"))

    qmlRegisterType(UI, "py", 1, 0, "Py")

    engine = QQmlApplicationEngine()
    engine.addImportPath(QML)
    engine.addImportPath(QML / "imports")

    engine.load(QML / "main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
