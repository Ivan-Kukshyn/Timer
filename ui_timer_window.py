# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_timer_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSplitter, QWidget)

class Ui_TimerWindow(object):
    def setupUi(self, TimerWindow):
        if not TimerWindow.objectName():
            TimerWindow.setObjectName(u"TimerWindow")
        TimerWindow.resize(350, 300)
        self.labelTime = QLabel(TimerWindow)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setGeometry(QRect(50, 50, 241, 85))
        self.splitter = QSplitter(TimerWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(11, 1, 156, 87))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.labelStatus = QLabel(TimerWindow)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(30, 150, 288, 26))
        font = QFont()
        font.setPointSize(14)
        self.labelStatus.setFont(font)
        self.btnPause = QPushButton(TimerWindow)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setGeometry(QRect(190, 200, 75, 71))
        font1 = QFont()
        font1.setPointSize(18)
        self.btnPause.setFont(font1)
        self.btnPause.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBack = QPushButton(TimerWindow)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(80, 200, 75, 72))
        font2 = QFont()
        font2.setPointSize(36)
        self.btnBack.setFont(font2)
        self.btnBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(TimerWindow)

        QMetaObject.connectSlotsByName(TimerWindow)
    # setupUi

    def retranslateUi(self, TimerWindow):
        TimerWindow.setWindowTitle(QCoreApplication.translate("TimerWindow", u"Timer", None))
        self.labelTime.setText(QCoreApplication.translate("TimerWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">00:00:00</span></p></body></html>", None))
        self.labelStatus.setText("")
        self.btnPause.setText(QCoreApplication.translate("TimerWindow", u"\u2590\u2590", None))
        self.btnBack.setText(QCoreApplication.translate("TimerWindow", u"\u25fc", None))
    # retranslateUi

