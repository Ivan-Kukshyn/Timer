# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 300)
        self.btnStart = QPushButton(MainWindow)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(140, 190, 71, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(48)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layoutWidget = QWidget(MainWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 80, 284, 72))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinHour = QSpinBox(self.layoutWidget)
        self.spinHour.setObjectName(u"spinHour")
        font1 = QFont()
        font1.setPointSize(36)
        self.spinHour.setFont(font1)
        self.spinHour.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.spinHour)

        self.spinMinute = QSpinBox(self.layoutWidget)
        self.spinMinute.setObjectName(u"spinMinute")
        self.spinMinute.setFont(font1)
        self.spinMinute.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.spinMinute)

        self.spinSecond = QSpinBox(self.layoutWidget)
        self.spinSecond.setObjectName(u"spinSecond")
        self.spinSecond.setFont(font1)
        self.spinSecond.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.spinSecond)

        self.labelHead = QLabel(MainWindow)
        self.labelHead.setObjectName(u"labelHead")
        self.labelHead.setGeometry(QRect(140, 20, 91, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.labelHead.setFont(font2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.labelHead.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440", None))
    # retranslateUi

