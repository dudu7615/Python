from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class textEdit(QTextEdit):
    changePassage = Signal(int)
    changePage = Signal(int)

    def sizeHint(self):
        """重写控件大小的方法，返回控件的大小
        * `self.document()` 返回文本编辑器中当前显示的文本的 `QTextDocument` 对象。
        * 我们使用 `doc.blockCount()` 方法获取文本中的总块数，
        * 然后使用 `range()` 函数遍历每个块的索引，
        * 使用 `doc.findBlockByNumber(i)` 方法获取每个块的 `QTextBlock` 对象。
        * 接下来，我们使用 `documentLayout().blockBoundingRect()` 方法获取每个块的边框矩形，
        * 然后使用 `.height()` 方法获取每个块的高度，并使用 `sum()` 函数将所有块的高度相加，以计算文本的总高度。
        """
        doc = self.document()
        height = sum(
            self.document()
            .documentLayout()
            .blockBoundingRect(doc.findBlockByNumber(i))
            .height()
            for i in range(doc.blockCount())
        )
        # 返回控件的大小
        return QSize(self.width(), int(height))

    def mousePressEvent(self, event: QMouseEvent):
        """重写鼠标点击事件，进行翻页、发射信号
        * `self.verticalScrollBar()` 方法获取滚动条的对象。
        * `self.verticalScrollBar().value()` 方法获取滚动条的当前值
        * `self.verticalScrollBar().maximum()` 方法获取滚动条的最大值。
        * `self.verticalScrollBar().minimum()` 方法获取滚动条的最小值。
        * `self.verticalScrollBar().setValue()` 方法设置滚动条的值。
        * `self.height()` 方法获取控件的高度。
        """
        if event.button() == Qt.MouseButton.LeftButton:
            if self.verticalScrollBar().value() == self.verticalScrollBar().maximum():
                self.changePassage.emit(0)
            else:
                # 鼠标左键向后翻页
                scrollBar = self.verticalScrollBar()
                scrollBar.setValue(scrollBar.value() + self.height())
                self.changePage.emit(scrollBar.value())
        elif event.button() == Qt.MouseButton.RightButton:
            if self.verticalScrollBar().value() == self.verticalScrollBar().minimum():
                self.changePassage.emit(1)
            else:
                # 鼠标右键向前翻页
                scrollBar = self.verticalScrollBar()
                scrollBar.setValue(scrollBar.value() - self.height())
                self.changePage.emit(scrollBar.value())


from ui import ui_enterRe
from ui import ui_list
from ui import ui_main
from ui import Ui_setting
from ui.icon_rc import *
