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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 246)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.passwd = QLineEdit(self.centralwidget)
        self.passwd.setObjectName(u"passwd")

        self.gridLayout.addWidget(self.passwd, 0, 0, 1, 1)

        self.choose = QComboBox(self.centralwidget)
        self.choose.addItem("")
        self.choose.addItem("")
        self.choose.setObjectName(u"choose")

        self.gridLayout.addWidget(self.choose, 0, 1, 1, 1)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")

        self.gridLayout.addWidget(self.run, 0, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.text = QTextEdit(self.centralwidget)
        self.text.setObjectName(u"text")

        self.gridLayout.addWidget(self.text, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.passwd, self.text)
        QWidget.setTabOrder(self.text, self.choose)
        QWidget.setTabOrder(self.choose, self.run)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose.setItemText(0, QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.choose.setItemText(1, QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))

        self.run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>", None))
    # retranslateUi

