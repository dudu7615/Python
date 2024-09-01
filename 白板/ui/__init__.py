from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class text(QTextEdit):
    click = Signal(QMouseEvent)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        self.click.emit(event)


from ui import icon_rc
from ui import Ui_ui
