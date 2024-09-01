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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(394, 287)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.showPath = QLabel(self.groupBox)
        self.showPath.setObjectName(u"showPath")
        self.showPath.setMinimumSize(QSize(0, 0))
        self.showPath.setMaximumSize(QSize(99999, 99999))
        self.showPath.setWordWrap(False)

        self.gridLayout.addWidget(self.showPath, 0, 0, 1, 1)

        self.chooseFile = QPushButton(self.groupBox)
        self.chooseFile.setObjectName(u"chooseFile")

        self.gridLayout.addWidget(self.chooseFile, 0, 1, 1, 1)

        self.run = QPushButton(self.groupBox)
        self.run.setObjectName(u"run")

        self.gridLayout.addWidget(self.run, 0, 2, 1, 1)

        self.prog = QProgressBar(self.groupBox)
        self.prog.setObjectName(u"prog")
        self.prog.setMaximumSize(QSize(16777215, 9999999))
        self.prog.setValue(0)
        self.prog.setTextVisible(True)
        self.prog.setOrientation(Qt.Horizontal)
        self.prog.setInvertedAppearance(False)
        self.prog.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.prog, 1, 0, 1, 1)

        self.chooseDir = QPushButton(self.groupBox)
        self.chooseDir.setObjectName(u"chooseDir")

        self.gridLayout.addWidget(self.chooseDir, 1, 1, 1, 1)

        self.save = QPushButton(self.groupBox)
        self.save.setObjectName(u"save")

        self.gridLayout.addWidget(self.save, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.showText = QTextEdit(self.centralwidget)
        self.showText.setObjectName(u"showText")

        self.gridLayout_2.addWidget(self.showText, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u8bbe\u7f6e", None))
        self.showPath.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8def\u5f84", None))
        self.chooseFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.chooseDir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
    # retranslateUi

