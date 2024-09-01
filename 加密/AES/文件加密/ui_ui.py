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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(264, 105)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.passwd = QLineEdit(self.centralwidget)
        self.passwd.setObjectName(u"passwd")

        self.horizontalLayout.addWidget(self.passwd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chooseMode = QComboBox(self.centralwidget)
        self.chooseMode.addItem("")
        self.chooseMode.addItem("")
        self.chooseMode.setObjectName(u"chooseMode")

        self.horizontalLayout_2.addWidget(self.chooseMode)

        self.chooseFile = QPushButton(self.centralwidget)
        self.chooseFile.setObjectName(u"chooseFile")

        self.horizontalLayout_2.addWidget(self.chooseFile)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")

        self.horizontalLayout_2.addWidget(self.run)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.chooseMode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.chooseMode.setItemText(1, QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))

        self.chooseFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
    # retranslateUi

