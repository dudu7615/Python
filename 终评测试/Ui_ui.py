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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 152)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.start = QDateEdit(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setCalendarPopup(True)

        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.end = QDateEdit(self.centralwidget)
        self.end.setObjectName(u"end")
        self.end.setDateTime(QDateTime(QDate(2020, 10, 1), QTime(15, 0, 0)))
        self.end.setCurrentSection(QDateTimeEdit.YearSection)
        self.end.setCalendarPopup(True)

        self.gridLayout.addWidget(self.end, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")

        self.gridLayout_2.addWidget(self.result, 1, 0, 1, 1)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")

        self.gridLayout_2.addWidget(self.run, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u8ba1\u7b97", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8ba1\u7b97", None))
    # retranslateUi

