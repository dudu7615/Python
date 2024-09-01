# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 227)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Open = QPushButton(self.centralwidget)
        self.Open.setObjectName(u"Open")

        self.gridLayout_2.addWidget(self.Open, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.B = QPushButton(self.centralwidget)
        self.B.setObjectName(u"B")

        self.gridLayout.addWidget(self.B, 2, 1, 1, 1)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.gridLayout.addWidget(self.start, 1, 1, 1, 1)

        self.show2 = QLabel(self.centralwidget)
        self.show2.setObjectName(u"show2")

        self.gridLayout.addWidget(self.show2, 1, 2, 1, 1)

        self.C = QPushButton(self.centralwidget)
        self.C.setObjectName(u"C")

        self.gridLayout.addWidget(self.C, 2, 2, 1, 1)

        self.A = QPushButton(self.centralwidget)
        self.A.setObjectName(u"A")

        self.gridLayout.addWidget(self.A, 2, 0, 1, 1)

        self.show1 = QLabel(self.centralwidget)
        self.show1.setObjectName(u"show1")

        self.gridLayout.addWidget(self.show1, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Show = QLabel(self.centralwidget)
        self.Show.setObjectName(u"Show")

        self.verticalLayout.addWidget(self.Show)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9898\u76ee\u6587\u4ef6", None))
        self.B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.show2.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u6570\uff1a0", None))
        self.C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.show1.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570\uff1a0", None))
        self.Show.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">None</p><p align=\"center\">None</p></body></html>", None))
    # retranslateUi

