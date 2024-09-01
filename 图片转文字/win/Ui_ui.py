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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWinsow(object):
    def setupUi(self, MainWinsow):
        if not MainWinsow.objectName():
            MainWinsow.setObjectName(u"MainWinsow")
        MainWinsow.resize(400, 235)
        self.centralwidget = QWidget(MainWinsow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.showPath = QLabel(self.centralwidget)
        self.showPath.setObjectName(u"showPath")
        self.showPath.setMinimumSize(QSize(0, 0))
        self.showPath.setMaximumSize(QSize(99999, 99999))
        self.showPath.setWordWrap(False)

        self.gridLayout.addWidget(self.showPath, 0, 0, 1, 2)

        self.prog = QProgressBar(self.centralwidget)
        self.prog.setObjectName(u"prog")
        self.prog.setMaximumSize(QSize(16777215, 9999999))
        self.prog.setValue(24)
        self.prog.setTextVisible(True)
        self.prog.setOrientation(Qt.Horizontal)
        self.prog.setInvertedAppearance(False)
        self.prog.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.prog, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chooseDir = QPushButton(self.centralwidget)
        self.chooseDir.setObjectName(u"chooseDir")

        self.horizontalLayout.addWidget(self.chooseDir)

        self.chooseFile = QPushButton(self.centralwidget)
        self.chooseFile.setObjectName(u"chooseFile")

        self.horizontalLayout.addWidget(self.chooseFile)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")

        self.horizontalLayout.addWidget(self.run)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.showText = QTextEdit(self.centralwidget)
        self.showText.setObjectName(u"showText")

        self.gridLayout.addWidget(self.showText, 3, 0, 1, 2)

        MainWinsow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWinsow)

        QMetaObject.connectSlotsByName(MainWinsow)
    # setupUi

    def retranslateUi(self, MainWinsow):
        MainWinsow.setWindowTitle(QCoreApplication.translate("MainWinsow", u"MainWindow", None))
        self.showPath.setText(QCoreApplication.translate("MainWinsow", u"\u8bf7\u8f93\u5165\u8def\u5f84", None))
        self.chooseDir.setText(QCoreApplication.translate("MainWinsow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.chooseFile.setText(QCoreApplication.translate("MainWinsow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.run.setText(QCoreApplication.translate("MainWinsow", u"\u5f00\u59cb", None))
    # retranslateUi

