import sys
from PySide6.QtWidgets import QMainWindow,QApplication,QTreeWidget,QTreeWidgetItem
from PySide6.QtGui import QIcon



class TreeWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TreeWidget 例子')

        self.tree = QTreeWidget()
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置树形控件头部的标题
        self.tree.setHeaderLabels(['Key', 'Value'])

        # 设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'Root')
        root.setIcon(0, QIcon('./images/root.png'))

        # 设置树形控件的列的宽度
        self.tree.setColumnWidth(0, 150)

        # 设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon('./images/IOS.png'))

        # 优化1 设置节点的状态

        root.addChild(child1)

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '')
        child2.setIcon(0, QIcon('./images/android.png'))

        # 设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')
        child3.setIcon(0, QIcon('./images/music.png'))

        # 加载根节点的所有属性与子控件
        self.tree.addTopLevelItem(root)

        # 优化3 给节点添加响应事件
        self.tree.clicked.connect(self.onClicked)

        # 节点全部展开
        self.tree.expandAll()
        self.setCentralWidget(self.tree)

    def onClicked(self):
        item = self.tree.currentItem()
        print(f'Key={item.text(0)},value={item.text(1)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec())
