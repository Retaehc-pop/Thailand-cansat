import Port
import serial
import math
import RTC
import mqtt
import time
from ui_main import Ui_GrounStation as UI_MainWindow
from UI_splashscreen import Ui_MainWindow as UI_splashscreen
from UI_Function import *
from compasswidget import CompassWidget
import sys
import threading
from PySide6.QtCharts import *
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from GNSS import Coord


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn()
        self.refresh()

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
        self.ui.btn_mqtt.clicked.connect(Window.start_mqtt)
        self.ui.btn_clear.clicked.connect(self.clear())
        self.ui.btn_c_on.clicked.connect(lambda: self.cmd('C_ON'))
        self.ui.btn_c_off.clicked.connect(lambda: self.cmd('C_OF'))
        self.ui.btn_r_on.clicked.connect(lambda: self.cmd('R_ON'))
        self.ui.btn_r_off.clicked.connect(lambda: self.cmd('R_OF'))

    def refresh(self):
        self.ui.portlist.clear()
        for com in Port.Port.list_port():
            self.ui.portlist.addItem(com)

    def clear(self):
        try:
            Window.clear()
        except:
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
    carrier1 = QtCore.Signal(object)
    carrier2 = QtCore.Signal(object)
    carrier3 = QtCore.Signal(object)

    def __init__(self, device, parent=None):
        super(ThreadMain, self).__init__(parent)
        self.device = device
        self.port = Port.Port(device=self.device)

    def __del__(self):
        self.wait()

    def run(self):
        print('[THREAD_MAIN_START]')
        while True:
            self.pkg = self.port.reading()
            print(f"[THREAD_IN] : {self.pkg}")
            if self.pkg["TYP"] == 'C':
                print('[CANSAT]', end="")
                self.pkg1 = self.pkg
                self.carrier1.emit(self.pkg1)
            elif self.pkg["TYP"] == 'R':
                print('[ROCKET]', end="")
                self.pkg2 = self.pkg
                self.carrier2.emit(self.pkg2)
            elif self.pkg["TYP"] == 'G':
                print('[GROUND]', end="")
                self.pkg3 = self.pkg
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



class Chart:
    def __init__(self, Graph: QChartView, Title: str, unit: str, howmany=1, ):
        self.color = QColor(217, 17, 194)
        self.pen = QPen(self.color)
        self.pen.setWidth(2)
        self.howmany = howmany

        self.LINE = []
        self.POINT = []
        for i in range(howmany):
            self.LINE.append(QSplineSeries())
            self.POINT.append(QScatterSeries())
        # self.LINE = QSplineSeries()
        # self.POINT = QScatterSeries()
        self.CHART = QChart()
        self.X_AXIS = QValueAxis()
        self.Y_AXIS = QValueAxis()
        self.Graph = Graph

        self.Title = Title
        self.Unit = unit
        self.x = []
        self.y = []
        self.setup()

    def setup(self):
        self.Graph.setRenderHint(QPainter.Antialiasing)
        self.CHART.legend().setVisible(False)
        self.CHART.setDropShadowEnabled(True)
        self.CHART.setAnimationOptions(QChart.SeriesAnimations)
        self.CHART.setTheme(QChart.ChartThemeBrownSand)
        self.CHART.createDefaultAxes()
        self.X_AXIS.setRange(0, 100)
        self.Y_AXIS.setRange(0, 100)
        for i in range(self.howmany):
            self.CHART.setAxisX(self.X_AXIS, self.LINE[i])
            self.CHART.setAxisY(self.Y_AXIS, self.LINE[i])
            self.CHART.addSeries(self.LINE[i])
            self.CHART.addSeries(self.POINT[i])
        self.CHART.setTitle(f"{self.Title} 0 {self.Unit}")
        self.Graph.setChart(self.CHART)

    def clear(self):
        for i in range(self.howmany):
            self.LINE[i].clear()
            self.POINT[i].clear()

    def plot(self, x, y, index=0):
        self.x.append(x)
        self.y.append(y)

        self.LINE[index].append(x, y)
        self.POINT[index].append(x, y)
        self.X_AXIS.setRange(min(self.x), max(self.x))
        self.Y_AXIS.setRange(min(self.y), max(self.y))
        self.CHART.setAxisX(self.X_AXIS, self.LINE[index])
        self.CHART.setAxisY(self.Y_AXIS, self.LINE[index])
        self.CHART.addSeries(self.LINE[index])
        self.CHART.addSeries(self.POINT[index])
        self.CHART.setTitle(f"{self.Title}{x}{self.Unit}")
        self.Graph.setChart(self.CHART)
        self.LINE[index].setPen(self.pen)
        self.POINT[index].setColor(self.color)
        self.POINT[index].setMarkerSize(8)


class Controller:
    def __init__(self):
        self._send = False
        self.state_alt = []
        self.peak = -10000
        self.state = "PRELAUNCH"

        self.show_splash()

    def clear(self):
        self.ui_main.ui.Sight.setText("0")
        self.ui_main.ui.Azimuth.setText("0")
        self.ui_main.ui.Elevation.setText("0")
        self.ui_main.ui.GD.setText("0")
        self.ui_main.ui.Heading.setText("0")
        self.ui_main.ui.PM10.setText("0")
        self.ui_main.ui.PM25.setText("0")
        self.ui_main.ui.AQI.setText("0")
        self.ui_main.ui.C_pkg.setText("0")
        self.ui_main.ui.R_pkg.setText("0")
        self.ui_main.ui.Drop.setText("0")
        self.ui_main.ui.apogee.setText("0")
        self.ui_main.ui.C_latitude.setText("0")
        self.ui_main.ui.C_longitude.setText("0")
        self.ui_main.ui.R_latitude.setText("0")
        self.ui_main.ui.R_longitude.setText("0")

    def setup(self):
        self.c = {"PKG": 0, "ALT": 0, "LAT": 0,
                  "LNG": 0, "TEM": 0, "HUM": 0,
                  "PRE": 0, "BAT": 0, "P10": 0,
                  "P25": 0, "ACX": 0, "ACY": 0,
                  "ACZ": 0, "GYX": 0, "GYY": 0,
                  "GYZ": 0}
        self.r = {"PKG": 0, "ALT": 0, "LAT": 0,
                  "LNG": 0, "TEM": 0, "BAT": 0,
                  "ACX": 0, "ACY": 0, "ACZ": 0,
                  "GYX": 0, "GYY": 0, "GYZ": 0}
        self.g = {"LAT": 0.0, "LNG": 0.0, "ALT": 0.0,
                  "MGX": 0.0, "MGY": 0.0, "MGZ": 0.0}

    def show_splash(self):
        self.window_splash = QtWidgets.QMainWindow()
        self.ui_ui = SplashScreen()
        print('[SPLASHSCREEN]', end="")

    def show_ui(self):
        self.window_ui = QtWidgets.QMainWindow()
        self.ui_main = MainWindow()
        self.setup()
        self.set_graph()
        self.clear()
        print('[MAINWINDOW]', end="")

    def start_clock(self):
        # x = threading.Thread(target=self.update_time)
        # y = threading.Thread(target=self.update_elapsed)
        # x.start()
        # y.start()
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

    def start_mqtt(self):
        try:
            self.mqtt = mqtt.Initialise_client()
            print("[MQTT_CONNECTED]")
            self._send = True
        except TimeoutError:
            print("[MQTT_FAILED]")
            self._send = False

    def update_time(self, data):
        # while True:
        #     self.clock = RTC.GetTime()
        #     self.ui_main.ui.Time.setText(self.clock.time_pc())
        #     time.sleep(0.1)
        self.ui_main.ui.Time.setText(data)

    def update_elapsed(self, data):
        # while True:
        #     self.ui_main.ui.Elapsed.setText(self.clock.time_elapsed())
        #     time.sleep(0.1)
        self.ui_main.ui.Elapsed.setText(data)

    def set_graph(self):
        self.C_ALT = Chart(self.ui_main.ui.C_alt_graph, "ALTITUDE", "(m)")
        self.C_TEM = Chart(self.ui_main.ui.C_temp_graph, "TEMPERATURE", "(C)")
        self.C_VEL = Chart(self.ui_main.ui.C_velo_graph, "VELOCITY", "(m/s)")
        self.C_HUM = Chart(self.ui_main.ui.C_humid_graph, "HUMIDITY", "(m)")
        self.C_ACC = Chart(self.ui_main.ui.C_acc_graph, "Acceleration", "(m/s2)", 3)
        self.C_GYR = Chart(self.ui_main.ui.C_gyro_graph, "Gyroscope", "(deg)", 3)

        self.R_ALT = Chart(self.ui_main.ui.R_alt_graph, "ALTITUDE", "(m)")
        self.R_TEM = Chart(self.ui_main.ui.R_temp_graph, "TEMPERATURE", "(C)")
        self.R_VEL = Chart(self.ui_main.ui.R_velo_graph, "VELOCITY", "(m/s)")
        self.R_ACC = Chart(self.ui_main.ui.R_acc_graph, "Acceleration", "(m/s2)", 3)
        self.R_GYR = Chart(self.ui_main.ui.R_gyro_graph, "Gyroscope", "(deg)", 3)

    def update_graph(self, graph, x, y, index=0):
        graph.plot(x, y, index)

    def update_cansat(self, data):
        self.c = data
        self.ui_main.ui.C_pkg.setText(str(self.c["PKG"]))
        self.ui_main.ui.PM10.setText(f'{self.c["P10"]} ug/m3')
        self.ui_main.ui.PM25.setText(f'{self.c["P25"]} ug/m3')
        self.ui_main.ui.AQI.setText(f'{(self.c["P25"] + self.c["P10"]) / 2} ug/m3')
        self.ui_main.ui.Drop.setText(f'{self.c["ACZ"]} m/s')

        a = threading.Thread(target=lambda: self.update_graph(self.C_ACC, self.c["PKG"], self.c["ALT"], 0))
        b = threading.Thread(target=lambda: self.update_graph(self.C_ACC, self.c["PKG"], self.c["ALT"], 1))
        c = threading.Thread(target=lambda: self.update_graph(self.C_ACC, self.c["PKG"], self.c["ALT"], 2))

        d = threading.Thread(target=lambda: self.update_graph(self.C_GYR, self.c["PKG"], self.c["ALT"], 0))
        e = threading.Thread(target=lambda: self.update_graph(self.C_GYR, self.c["PKG"], self.c["ALT"], 1))
        f = threading.Thread(target=lambda: self.update_graph(self.C_GYR, self.c["PKG"], self.c["ALT"], 2))

        w = threading.Thread(target=lambda: self.update_graph(self.C_ALT, self.c["PKG"], self.c["ALT"]))
        x = threading.Thread(target=lambda: self.update_graph(self.C_TEM, self.c["PKG"], self.c["TEM"]))
        y = threading.Thread(target=lambda: self.update_graph(self.C_VEL, self.c["PKG"],
                                                              self.to_vel(self.c["ACX"], self.c["ACY"], self.c["ACZ"])))
        z = threading.Thread(target=lambda: self.update_graph(self.C_HUM, self.c["PKG"], self.c["HUM"]))
        w.start()
        x.start()
        y.start()
        z.start()
        if self._send:
            mqttc = threading.Thread(target=lambda: mqtt.sendserver(self.mqtt, data))
            mqttc.start()

    def update_rocket(self, data):
        self.r = data
        self.ui_main.ui.R_pkg.setText(str(self.r["PKG"]))
        a = threading.Thread(target=lambda: self.update_graph(self.R_ACC, self.r["PKG"], self.r["ALT"], 0))
        b = threading.Thread(target=lambda: self.update_graph(self.R_ACC, self.r["PKG"], self.r["ALT"], 1))
        c = threading.Thread(target=lambda: self.update_graph(self.R_ACC, self.r["PKG"], self.r["ALT"], 2))
        d = threading.Thread(target=lambda: self.update_graph(self.R_GYR, self.r["PKG"], self.r["ALT"], 0))
        e = threading.Thread(target=lambda: self.update_graph(self.R_GYR, self.r["PKG"], self.r["ALT"], 1))
        f = threading.Thread(target=lambda: self.update_graph(self.R_GYR, self.r["PKG"], self.r["ALT"], 2))

        x = threading.Thread(target=lambda: self.update_graph(self.R_ALT, self.r["PKG"], self.r["ALT"]))
        y = threading.Thread(target=lambda: self.update_graph(self.R_TEM, self.r["PKG"], self.r["TEM"]))
        z = threading.Thread(target=lambda: self.update_graph(self.R_VEL, self.r["PKG"],
                                                              self.to_vel(self.r["ACX"], self.r["ACY"], self.r["ACZ"])))
        x.start()
        y.start()
        z.start()
        if self._send:
            mqttc = threading.Thread(target=lambda: mqtt.sendserver(self.mqtt, data))
            mqttc.start()

    def update_state(self):
        self.state_alt.append(float(self.r["ALT"]))
        if float(self.r["ALT"]) > self.peak:
            self.peak = float(self.r["ALT"])
        if len(self.state_alt) < 10:
            self.state = 'PRELAUNCH'
            self.ground = self.state_alt[0]
            self.ui_main.ui.State_bar.setMinimumSize(int(round(self.ground)))
            self.ui_main.ui.State_bar.setMaximum(500)
        elif self.state == "PRELAUNCH" and self.state_alt[-1] - self.ground > 10:
            self.state = "LAUNCHED"
        elif self.state == "LAUNCHED" and self.peak - self.state_alt[-1] > 10:
            self.state = "APOGEE"
            self.ui_main.ui.State_bar.setMaximumSize(self.peak * 2)
        elif self.state == "APOGEE" and self.peak - self.state_alt[-1] > 30:
            self.state = "DESCEND"
        elif self.state == "DESCEND" and self.state_alt[-1] - self.ground < 10:
            self.state = "LANDED"

        self.ui_main.ui.State_bar.setValue((self.peak * 2) - self.state_alt[-1])
        self.ui_main.ui.state_t.setText(self.state)

    def update_ground(self, data):
        self.g = data
        self.GNSS = Coord(self.g["LAT"], self.g["LNG"], self.c["LAT"], self.c["LNG"], self.g["ALT"], self.c["ALT"],
                          self.g["MGX"], self.g["MGY"], self.g["MGZ"])
        self.ui_main.ui.Azimuth.setText(str(self.GNSS.azimuth()))
        self.ui_main.ui.Elevation.setText(str(self.GNSS.elevation()))
        self.ui_main.ui.GD.setText(str(self.GNSS.ground_distance()))
        self.ui_main.ui.Sight.setText(str(self.GNSS.line_of_sight()))
        self.ui_main.ui.Heading.setText(str(self.GNSS.heading()))

    @staticmethod
    def to_vel(a, b, c):
        vel = math.sqrt((a * a) + (b * b) + (c * c))
        return vel


if __name__ == "__main__":
    app = QApplication()
    Window = Controller()
    sys.exit(app.exec())
