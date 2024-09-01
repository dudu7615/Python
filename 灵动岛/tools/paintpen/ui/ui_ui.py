# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(356, 133)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.gridLayout_2.addWidget(self.start, 1, 1, 1, 1)

        self.show = QWidget(self.centralwidget)
        self.show.setObjectName(u"show")

        self.gridLayout_2.addWidget(self.show, 0, 1, 1, 1)

        self.off = QPushButton(self.centralwidget)
        self.off.setObjectName(u"off")

        self.gridLayout_2.addWidget(self.off, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.white = QPushButton(self.groupBox)
        self.white.setObjectName(u"white")
        self.white.setStyleSheet(u"background: rgb(255, 0255, 255)")

        self.gridLayout.addWidget(self.white, 0, 1, 1, 1)

        self.green = QPushButton(self.groupBox)
        self.green.setObjectName(u"green")
        self.green.setStyleSheet(u"background: rgb(0, 255, 0)")

        self.gridLayout.addWidget(self.green, 0, 2, 1, 1)

        self.black = QPushButton(self.groupBox)
        self.black.setObjectName(u"black")
        self.black.setStyleSheet(u"background: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.black, 1, 0, 1, 1)

        self.choose = QPushButton(self.groupBox)
        self.choose.setObjectName(u"choose")

        self.gridLayout.addWidget(self.choose, 1, 1, 1, 2)

        self.red = QPushButton(self.groupBox)
        self.red.setObjectName(u"red")
        self.red.setStyleSheet(u"background: rgb(255, 0, 0)")

        self.gridLayout.addWidget(self.red, 0, 0, 1, 1)

        self.wight = QSlider(self.groupBox)
        self.wight.setObjectName(u"wight")
        self.wight.setMaximum(35)
        self.wight.setValue(10)
        self.wight.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.wight, 2, 0, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.off.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.white.setText(QCoreApplication.translate("MainWindow", u"\u767d", None))
        self.green.setText(QCoreApplication.translate("MainWindow", u"\u7eff", None))
        self.black.setText(QCoreApplication.translate("MainWindow", u"\u9ed1", None))
        self.choose.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.red.setText(QCoreApplication.translate("MainWindow", u"\u7ea2", None))
    # retranslateUi

