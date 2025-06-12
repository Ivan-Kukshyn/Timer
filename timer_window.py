from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import QWidget, QPushButton

from ui_timer_window import Ui_TimerWindow

class TimerWindow(QWidget):
    def __init__(self, timer, main_window):
        super().__init__()
        self.ui = Ui_TimerWindow()
        self.ui.setupUi(self)

        self.timer = timer
        self.main_window = main_window

        self.timer.time_updated.connect(self.update_timer_display)
        self.timer.status_updated.connect(self.update_status)
        self.timer.finished.connect(self.timer_finished)

        self.ui.btnPause.clicked.connect(self.pause_timer)
        self.ui.btnBack.clicked.connect(self.back_to_main)

        self.btnContinue = QPushButton("▶", self)
        font = QFont()
        font.setPointSize(48)
        self.btnContinue.setFont(font)
        self.btnContinue.setGeometry(self.ui.btnPause.geometry())
        self.btnContinue.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnContinue.clicked.connect(self.continue_timer)
        self.btnContinue.hide()

        self.ui.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def pause_timer(self):
        self.timer.pause()
        self.ui.btnPause.hide()
        self.btnContinue.show()

    def continue_timer(self):
        self.timer.continue_timer()
        self.btnContinue.hide()
        self.ui.btnPause.show()

    def back_to_main(self):
        self.timer.reset()
        self.hide()
        self.main_window.show()

    def update_timer_display(self, seconds):
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        self.ui.labelTime.setText(f"{h:02}:{m:02}:{s:02}")
        font = QFont()
        font.setPointSize(48)
        self.ui.labelTime.setFont(font)
        self.ui.labelTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def update_status(self, text):
        self.ui.labelStatus.setText(text)

    def timer_finished(self):
        self.hide()
        self.main_window.show()
        self.main_window.show_timer_expired_message()