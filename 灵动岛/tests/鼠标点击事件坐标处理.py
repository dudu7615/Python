from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print(event.pos())
        return super().mousePressEvent(event)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()