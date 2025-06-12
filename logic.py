from PySide6.QtCore import QTimer, Signal, QObject


class TimerManager(QObject):
    time_updated = Signal(int)
    status_updated = Signal(str)
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.time_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.running = False
        self.was_paused = False

    def start(self, duration_sec=None):
        if duration_sec is not None:
            self.time_left = duration_sec
        if self.time_left <= 0:
            return
        self.timer.start(1000)
        self.running = True
        self.time_updated.emit(self.time_left)

        h, rem = divmod(self.time_left, 3600)
        m, s = divmod(rem, 60)
        if h > 0:
            time = f"{h:02}:{m:02}:{s:02}"
        else:
            time = f"{m:02}:{s:02}"
        self.status_updated.emit(f"Загально " + time)

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.running = False

    def continue_timer(self):
        if not self.running and self.time_left > 0:
            self.timer.start(1000)
            self.running = True

    def reset(self):
        self.timer.stop()
        self.time_left = 0
        self.running = False
        self.time_updated.emit(self.time_left)

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_updated.emit(self.time_left)
        if self.time_left <= 0:
            self.timer.stop()
            self.running = False
            self.finished.emit()