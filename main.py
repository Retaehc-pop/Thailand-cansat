import Port
import serial
import math
import RTC
from ui_main import Ui_GrounStation as UI_MainWindow
from UI_splashscreen import Ui_MainWindow as UI_splashscreen
from UI_Function import *
import sys
import threading
from PySide6.QtCharts import *
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
            if self.pkg[0] == 'C':
                print('[CANSAT]', end="")
                self.pkg1 = self.pkg[:]
                self.carrier1.emit(self.pkg1)
            elif self.pkg[0] == 'R':
                print('[ROCKET]', end="")
                self.pkg2 = self.pkg[:]
                self.carrier2.emit(self.pkg2)
            elif self.pkg[0] == 'G':
                print('[GROUND]', end="")
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
        self.spline_alt, self.spline_temp, self.spline_vel, self.spline_hum, self.spline_altr, self.spline_tempr, self.spline_velr = (
            QSplineSeries(), QSplineSeries(), QSplineSeries(), QSplineSeries(), QSplineSeries(), QSplineSeries(),
            QSplineSeries())
        self.point_alt, self.point_temp, self.point_vel, self.point_hum, self.point_altr, self.point_tempr, self.point_velr = (
            QScatterSeries(), QScatterSeries(), QScatterSeries(), QScatterSeries(), QScatterSeries(), QScatterSeries(),
            QScatterSeries())
        self.chart_alt, self.chart_temp, self.chart_vel, self.chart_hum, self.chart_altr, self.chart_tempr, self.chart_velr = (
            QChart(), QChart(), QChart(), QChart(), QChart(), QChart(), QChart())
        self.axisX_alt, self.axisX_temp, self.axisX_vel, self.axisX_hum, self.axisX_altr, self.axisX_tempr, self.axisX_velr = (
            QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis())
        self.axisY_alt, self.axisY_temp, self.axisY_vel, self.axisY_hum, self.axisY_altr, self.axisY_tempr, self.axisY_velr = (
            QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis(), QValueAxis())

        self.show_splash()
        self.setup()

    def setup(self):
        self.c = {"PKG": 0, "ALT": 0, "LAT": 0,
                  "LNG": 0, "TEM": 0, "HUM": 0,
                  "PRE": 0, "BAT": 0, "P10": 0,
                  "P25": 0, "ACX": 0, "ACY": 0,
                  "ACZ": 0, "ORX": 0, "ORY": 0,
                  "ORZ": 0}
        self.r = {"PKG": 0, "ALT": 0, "LAT": 0,
                  "LNG": 0, "TEM": 0, "BAT": 0,
                  "ACX": 0, "ACY": 0, "ACZ": 0,
                  "ORX": 0, "ORY": 0, "ORZ": 0}
        self.g = {"LAT": 0.0, "LNG": 0.0, "ALT": 0.0,
                  "MGX": 0.0, "MGY": 0.0, "MGZ": 0.0}

    def show_splash(self):
        self.window_splash = QtWidgets.QMainWindow()
        self.ui_ui = SplashScreen()
        print('[SPLASHSCREEN]', end="")

    def show_ui(self):
        self.window_ui = QtWidgets.QMainWindow()
        self.ui_main = MainWindow()
        self.set_graph()
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

    def set_graph(self):
        self.color = QColor(217, 17, 194)
        self.pen = QPen(self.color)
        self.pen.setWidth(2)

        self.C_ALT = {"GRAPH": self.ui_main.ui.C_alt_graph,
                      "LINE": self.spline_alt,
                      "POINT": self.point_alt,
                      "CHART": self.chart_alt,
                      "X-AXIS": self.axisX_alt,
                      "Y-AXIS": self.axisY_alt,
                      "TITLE": f"Altitude {self.c['ALT']}M",
                      "X": self.c["PKG"],
                      "y": self.c["ALT"]}

        self.C_TEMP = {"GRAPH": self.ui_main.ui.C_temp_graph,
                       "LINE": self.spline_temp,
                       "POINT": self.point_temp,
                       "CHART": self.chart_temp,
                       "X-AXIS": self.axisX_temp,
                       "Y-AXIS": self.axisY_temp,
                       "TITLE": f"Temperature {self.c['TEM']}C",
                       "X": self.c["PKG"],
                       "y": self.c["TEM"]}

        self.C_VEL = {"GRAPH": self.ui_main.ui.C_velo_graph,
                      "LINE": self.spline_vel,
                      "POINT": self.point_vel,
                      "CHART": self.chart_vel,
                      "X-AXIS": self.axisX_vel,
                      "Y-AXIS": self.axisY_vel,
                      "TITLE": f'Velocity {self.to_vel(self.c["ACX"],self.c["ACY"],self.c["ACZ"])} m/s',
                      "X": self.c["PKG"],
                      "y": self.to_vel(self.c["ACX"],self.c["ACY"],self.c["ACZ"])}

        self.C_HUM = {"GRAPH": self.ui_main.ui.C_humid_graph,
                      "LINE": self.spline_hum,
                      "POINT": self.point_hum,
                      "CHART": self.chart_hum,
                      "X-AXIS": self.axisX_hum,
                      "Y-AXIS": self.axisY_hum,
                      "TITLE": f"HUMIDITY {self.c['HUM']} %",
                      "X": self.c["PKG"],
                      "y": self.c["HUM"]}
        self.R_ALT = {"GRAPH": self.ui_main.ui.R_alt_graph,
                      "LINE": self.spline_altr,
                      "POINT": self.point_altr,
                      "CHART": self.chart_altr,
                      "X-AXIS": self.axisX_altr,
                      "Y-AXIS": self.axisY_altr,
                      "TITLE": f"ALTITUDE {self.r['ALT']} M",
                      "X": self.r["PKG"],
                      "y": self.r["ALT"]}

        self.R_TEMP = {"GRAPH": self.ui_main.ui.R_temp_graph,
                       "LINE": self.spline_tempr,
                       "POINT": self.point_tempr,
                       "CHART": self.chart_tempr,
                       "X-AXIS": self.axisX_tempr,
                       "Y-AXIS": self.axisY_tempr,
                       "TITLE": f"HUMIDITY {self.r['TEM']} %",
                       "X": self.r["PKG"],
                       "y": self.r["TEM"]}

        self.R_VEL = {"GRAPH": self.ui_main.ui.R_velo_graph,
                      "LINE": self.spline_velr,
                      "POINT": self.point_velr,
                      "CHART": self.chart_velr,
                      "X-AXIS": self.axisX_velr,
                      "Y-AXIS": self.axisY_velr,
                      "TITLE": f'VELOCITY {self.to_vel(self.r["ACX"],self.r["ACY"],self.r["ACZ"])} %',
                      "X": self.c["PKG"],
                      "y": self.to_vel(self.r["ACX"],self.r["ACY"],self.r["ACZ"])}

        self.GRAPH = [self.C_ALT, self.C_TEMP, self.C_VEL, self.C_HUM, self.R_ALT, self.R_TEMP, self.R_VEL]

        for item in self.GRAPH:
            item["GRAPH"].setRenderHint(QPainter.Antialiasing)
            item["CHART"].legend().setVisible(False)
            item["CHART"].setDropShadowEnabled(True)
            item["CHART"].setAnimationOptions(QChart.SeriesAnimations)
            item["CHART"].setTheme(QChart.ChartThemeDark)
            item["CHART"].createDefaultAxes()
            item["X-AXIS"].setRange(0,100)
            item["Y-AXIS"].setRange(0,100)
            item["CHART"].setAxisX(item["X-AXIS"], item["LINE"])
            item["CHART"].setAxisY(item["Y-AXIS"], item["LINE"])
            item["CHART"].addSeries(item["LINE"])
            item["CHART"].addSeries(item["POINT"])
            item["CHART"].setTitle(item["TITLE"])
            item["GRAPH"].setChart(item["CHART"])

    def update_graph(self, item):
        item["LINE"].append(item["X"],item["Y"])
        item["POINT"].append(item["X"],item["Y"])
        item["X-AXIS"].setRange(min(item["X"]), max(item["X"]))
        item["Y-AXIS"].setRange(min(item["Y"]), max(item["Y"]))
        item["CHART"].setAxisX(item["X-AXIS"], item["LINE"])
        item["CHART"].setAxisY(item["Y-AXIS"], item["LINE"])
        item["CHART"].addSeries(item["LINE"])
        item["CHART"].addSeries(item["POINT"])
        item["CHART"].setTitle(item["TITLE"])
        item["GRAPH"].setChart(item["CHART"])
        item["LINE"].setPen(self.pen)
        item["POINT"].setColor(self.color)
        item["POINT"].setMarkerSize(8)

    def update_cansat(self, data):
        self.c["PKG"] = int(data[1])
        self.c["ALT"] = float(data[2])
        self.c["LAT"] = float(data[3])
        self.c["LNG"] = float(data[4])
        self.c["TEM"] = float(data[5])
        self.c["HUM"] = float(data[6])
        self.c["PRE"] = float(data[7])
        self.c["BAT"] = float(data[8])
        self.c["P10"] = float(data[9])
        self.c["P25"] = float(data[10])
        self.c["ACX"] = float(data[11])
        self.c["ACY"] = float(data[12])
        self.c["ACZ"] = float(data[13])
        self.c["ORX"] = float(data[14])
        self.c["ORY"] = float(data[15])
        self.c["ORZ"] = float(data[16])
        self.update_main()

    def update_rocket(self, data):
        self.r["PKG"] = int(data[1])
        self.r["ALT"] = float(data[2])
        self.r["LAT"] = float(data[3])
        self.r["LNG"] = float(data[4])
        self.r["TEM"] = float(data[5])
        self.r["BAT"] = float(data[6])
        self.r["ACX"] = float(data[7])
        self.r["ACY"] = float(data[8])
        self.r["ACZ"] = float(data[9])
        self.r["ORX"] = float(data[10])
        self.r["ORY"] = float(data[11])
        self.r["ORZ"] = float(data[12])
        self.update_main()

    def update_ground(self, data):
        self.g["LAT"] = float(data[1])
        self.g["LNG"] = float(data[2])
        self.g["ALT"] = float(data[3])
        self.g["MGX"] = float(data[4])
        self.g["MGY"] = float(data[4])
        self.g["MGZ"] = float(data[4])

    def update_main(self):
        self.thread_text = threading.Thread(target=self.update_text)
        self.thread_bar = threading.Thread(target=self.update_bar)
        self.thread_graph = threading.Thread(target=self.update_graph)
        self.thread_text.start()
        self.thread_bar.start()

    def update_bar(self):
        self.ui_main.ui.C_accx_bar.setValue(self.c["ACX"])
        self.ui_main.ui.C_accy_bar.setValue(self.c["ACY"])
        self.ui_main.ui.C_accz_bar.setValue(self.c["ACZ"])

        self.ui_main.ui.C_orix_bar.setValue(self.c["ORX"])
        self.ui_main.ui.C_oriy_bar.setValue(self.c["ORY"])
        self.ui_main.ui.C_oriz_bar.setValue(self.c["ORZ"])

        self.ui_main.ui.R_accx_bar.setValue(self.r["ACX"])
        self.ui_main.ui.R_accy_bar.setValue(self.r["ACY"])
        self.ui_main.ui.R_accz_bar.setValue(self.r["ACZ"])

        self.ui_main.ui.R_orix_bar.setValue(self.r["ORX"])
        self.ui_main.ui.R_oriy_bar.setValue(self.r["ORY"])
        self.ui_main.ui.R_oriz_bar.setValue(self.r["ORZ"])

    def update_text(self):
        self.ui_main.ui.C_pkg.setText(str(self.c["PKG"]))
        self.ui_main.ui.PM10.setText(f'{self.c["P10"]} ug/m3')
        self.ui_main.ui.PM25.setText(f'{self.c["P25"]} ug/m3')
        self.ui_main.ui.AQI.setText(f'{(self.c["P25"] + self.c["P10"]) / 2} ug/m3')
        self.ui_main.ui.R_pkg.setText({self.r["PKG"]})

    @staticmethod
    def to_vel(a,b,c):
        vel = math.sqrt((a*a)+(b*b)+(c*c))
        return vel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Controller()
    sys.exit(app.exec())
