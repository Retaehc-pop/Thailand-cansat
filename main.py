import Port
import serial

import RTC
from ui_main import Ui_GrounStation as UI_MainWindow
from UI_splashscreen import Ui_MainWindow as UI_splashscreen
from UI_Function import *
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn()

        def move_window(event):
            if UiFunctions.return_status(self) == 1:
                UiFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.headframe.mouseMoveEvent = move_window
        UiFunctions.ui_definitions(self)
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def connect_btn(self):
        self.ui.btn_connect.clicked.connect(self.online)
        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_c_on.clicked.connect(lambda: self.cmd('C_ON'))
        self.ui.btn_c_off.clicked.connect(lambda: self.cmd('C_OF'))
        self.ui.btn_r_on.clicked.connect(lambda: self.cmd('R_ON'))
        self.ui.btn_r_off.clicked.connect(lambda: self.cmd('R_OF'))

    def refresh(self):
        self.ui.portlist.clear()
        for com in Port.Port.list_port():
            self.ui.portlist.addItem(com)

    def clear(self):
        pass

    def online(self):
        port = self.ui.portlist.currentText()
        try:
            self.device = serial.Serial(port, baudrate=int(9600), timeout=60)
            Window.start_serial(self.device)
            Window.start_clock()
        except:
            print("[Cannot connect port]")

    def cmd(self, cmd):
        self.device.write(f"CMD,{cmd}$".encode())
        print(f"CMD,{cmd}$")


GLOBAL_SPLASH_COUNTER = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_splashscreen()
        self.ui.setupUi(self)
        self.ui.lb_title.setText(" ")
        SplashScreenFunctions.ui_definitions(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)
        self.show()

    def progress(self):
        global GLOBAL_SPLASH_COUNTER
        status_text = str(GLOBAL_SPLASH_COUNTER) + '%'
        if GLOBAL_SPLASH_COUNTER <= 17:
            self.ui.lb_status.setText('Loading Assets...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 29:
            self.ui.lb_status.setText('Scanning all COM Ports...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 42:
            self.ui.lb_status.setText('Connecting to WAREDTANAS...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 54:
            self.ui.lb_status.setText('Verifying WAREDTANS...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 64:
            self.ui.lb_status.setText('Verifying Devices...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 75:
            self.ui.lb_status.setText('Preparing Interface...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 100:
            self.ui.lb_status.setText('Done.\n' + status_text)
        else:
            self.timer.stop()
            Window.show_ui()
            self.close()

        GLOBAL_SPLASH_COUNTER += 1


class ThreadMain(QThread):
    # @Slot(float, result=int,)
    # def get(self,f):
    #     return int(f)

    carrier1 = QtCore.Signal(object)
    carrier2 = QtCore.Signal(object)
    carrier3 = QtCore.Signal(object)

    def __init__(self, device, parent=None):
        super(ThreadMain, self).__init__(parent)
        self.device = device
        self.port = Port.Port(device=self.device)
        # self.startread.connect_port(9600)

    def __del__(self):
        self.wait()

    def run(self):
        print('[THREAD_MAIN_START]')
        while True:
            self.pkg = self.port.reading()
            print(f"[THREAD_IN] : {self.pkg}")
            if self.pkg[3] == 'C':
                print('[CANSAT]', end="")
                self.pkg1 = self.pkg[:]
                self.carrier1.emit(self.pkg1)
            elif self.pkg[3] == 'SP1':
                print('[PAYLOAD1]', end="")
                self.pkg2 = self.pkg[:]
                self.carrier2.emit(self.pkg2)
            elif self.pkg[3] == 'SP2':
                print('[PAYLOAD2]', end="")
                self.pkg3 = self.pkg[:]
                self.carrier3.emit(self.pkg3)

    def stop(self):
        self._isRunning = False


class ThreadTimer(QThread):
    time_carrier = QtCore.Signal(object)
    elapsed_carrier = QtCore.Signal(object)

    def __init__(self, parent=None):
        self._isRunning = True
        super(ThreadTimer, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        clock = RTC.GetTime()
        while True:
            self.time_carrier.emit(clock.time_pc())
            self.elapsed_carrier.emit(clock.time_elapsed())

    def stop(self):
        self._isRunning = False
        self.terminate()


class Controller:
    def __init__(self):
        self.show_splash()

    def show_splash(self):
        self.window_splash = QtWidgets.QMainWindow()
        self.ui_ui = SplashScreen()
        print('[SPLASHSCREEN]', end="")

    def show_ui(self):
        self.window_ui = QtWidgets.QMainWindow()
        self.ui_main = MainWindow()
        print('[MAINWINDOW]', end="")

    def start_clock(self):
        self.worker_time = ThreadTimer()
        self.worker_time.time_carrier.connect(self.update_time)
        self.worker_time.elapsed_carrier.connect(self.update_elapsed)
        self.worker_time.start()

    def start_serial(self, device):
        self.worker_serial = ThreadMain(device)
        self.worker_serial.carrier1.connect(self.update_cansat)
        self.worker_serial.carrier2.connect(self.update_rocket)
        self.worker_serial.carrier3.connect(self.update_ground)
        self.worker_serial.start()

    def update_time(self, time):
        self.ui_main.ui.Time.setText(time)

    def update_elapsed(self, time):
        self.ui_main.ui.Elapsed.setText(time)

    def update_cansat(self, data):
        pass

    def update_rocket(self, data):
        pass

    def update_ground(self, data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Controller()
    sys.exit(app.exec_())
