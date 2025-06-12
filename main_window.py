from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox

from json_storage import load_data, save_data
from logic import TimerManager
from timer_window import TimerWindow
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = TimerManager()
        self.timer_window = TimerWindow(self.timer, self)

        self.ui.btnStart.clicked.connect(self.start_and_show_timer)

        # Load saved values
        self.last_set_time = 0
        self.set_timer()

        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setSource(QUrl.fromLocalFile("ringtone.wav"))
        self.audio_output.setVolume(0.8)

        self.media_player.setLoops(QMediaPlayer.Loops.Infinite)

        self.ui.spinSecond.valueChanged.connect(self.normalize_time_input)
        self.ui.spinMinute.valueChanged.connect(self.normalize_time_input)

    def set_timer(self):
        data = load_data()
        self.ui.spinHour.setValue(data.get("set_hour", 0))
        self.ui.spinMinute.setValue(data.get("set_minute", 0))
        self.ui.spinSecond.setValue(data.get("set_second", 0))

    def normalize_time_input(self):
        second = self.ui.spinSecond.value()
        minute = self.ui.spinMinute.value()
        hour = self.ui.spinHour.value()

        if second >= 60:
            extra_minute, second = divmod(second, 60)
            minute += extra_minute
            self.ui.spinSecond.setValue(second)
            self.ui.spinMinute.setValue(minute)

        if minute >= 60:
            extra_hour, minute = divmod(minute, 60)
            hour += extra_hour
            self.ui.spinMinute.setValue(minute)
            self.ui.spinHour.setValue(hour)


    def start_and_show_timer(self):
        hour = self.ui.spinHour.value()
        minute = self.ui.spinMinute.value()
        second = self.ui.spinSecond.value()

        self.last_set_time = hour * 3600 + minute * 60 + second

        # Save values
        save_data({
            "set_hour": hour,
            "set_minute": minute,
            "set_second": second
        })

        total_seconds = hour * 3600 + minute * 60 + second
        if total_seconds == 0:
            QMessageBox.warning(self, "Увага!", "Таймер не встановлено.")
            return
        self.timer.start(total_seconds)

        self.timer_window.show()
        self.hide()

    def show_timer_expired_message(self):
        h, rem = divmod(self.last_set_time, 3600)
        m, s = divmod(rem, 60)

        self.media_player.play()

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Час вийшов!")
        msg_box.setText(f"<div style='font-size:24px; text-align:center;'>{h:02}:{m:02}:{s:02}</div>")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Close)

        msg_box.setStyleSheet("QLabel{min-width: 200px; min-height: 100px;}")

        msg_box.exec()

        self.media_player.stop()
