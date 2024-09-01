# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QRadioButton,
    QScrollBar, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Ui(object):
    def setupUi(self, Ui):
        if not Ui.objectName():
            Ui.setObjectName(u"Ui")
        Ui.resize(415, 260)
        self.centralwidget = QWidget(Ui)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.showTime = QTextEdit(self.centralwidget)
        self.showTime.setObjectName(u"showTime")
        self.showTime.setReadOnly(True)

        self.verticalLayout.addWidget(self.showTime)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.setTime = QScrollBar(self.centralwidget)
        self.setTime.setObjectName(u"setTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setTime.sizePolicy().hasHeightForWidth())
        self.setTime.setSizePolicy(sizePolicy1)
        self.setTime.setMaximum(45)
        self.setTime.setPageStep(5)
        self.setTime.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.setTime)

        self.start = QRadioButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.horizontalLayout.addWidget(self.start)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui)

        QMetaObject.connectSlotsByName(Ui)
    # setupUi

    def retranslateUi(self, Ui):
        Ui.setWindowTitle(QCoreApplication.translate("Ui", u"Ui", None))
        self.showTime.setHtml(QCoreApplication.translate("Ui", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:100pt; font-weight:700;\">00:00</span></p></body></html>", None))
        self.start.setText(QCoreApplication.translate("Ui", u"\u8ba1\u65f6\u505c\u6b62", None))
    # retranslateUi

