from setting_files import *
from setting_files.Clock import RTC
from setting_files.Port import Port
from setting_files.GNSS import GNSS
from ui_main import Ui_GrounStation as Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn()
        self.baud = None
        self.port = None
        self.refresh()
        self.show()

    def connect_btn(self):
        self.ui.btn_c_off.clicked.connect(self.send)
        self.ui.btn_c_on.clicked.connect(self.send)
        self.ui.btn_r_off.clicked.connect(self.send)
        self.ui.btn_r_on.clicked.connect(self.send)
        self.ui.btn_connect.clicked.connect(self.start)
        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_clear.clicked.connect(self.clear)

    def refresh(self):
        self.ui.port_box.clear()
        for port in Port.list_port():
            self.ui.port_box.addItem(port)
        baudrate = [110, 300, 600, 1200, 2400, 4800, 9600,
                    14400, 19200, 38400, 57600, 115200, 128000, 256000]
        self.ui.baud_box.clear()
        for baud in baudrate:
            self.ui.baud_box.addItem(str(baud))

    def start(self):
        Window.start(self.ui.port_box.currentText(),
                     self.ui.baud_box.currentText())

    def clear(self):
        Window.set_ui()

    def send(self):
        Window.serial.port.write()


class SerialThread(QThread):
    carrier1 = QtCore.Signal(object)
    carrier2 = QtCore.Signal(object)
    carrier3 = QtCore.Signal(object)

    def __init__(self, com, baud, parent=None):
        super(SerialThread, self).__init__(parent)
        '''
        'C': ["TYP", "PKG", "ALT", "LAT", "LNG", "TMP", "HUM", "PRE", "BAT", "P10", "P25", "ACX", "ACY", "ACZ", "GYX", "GYY", "GYZ"],
        'R': ["TYP", "PKG", "ALT", "LAT", "LNG", "TMP", "BAT", "ACX", "ACY", "ACZ", "GAL", "GYX", "GYY", "GYZ"],
        'G': ["TYP", "LAT", "LNG", "ALT", "MGX", "MGY", "MGZ"]
        '''
        self.dict = {
            'C': ["TYP", "PKG", "ALT", "LAT", "LNG", "TMP", "HUM", "PRE", "BAT", "P10", "P25", "ACX", "ACY", "ACZ", "GYX", "GYY", "GYZ"],
            'R': ["TYP", "PKG", "ALT", "LAT", "LNG", "TMP", "BAT", "ACX", "ACY", "ACZ", "GAL", "GYX", "GYY", "GYZ"],
            'G': ["TYP", "LAT", "LNG", "ALT", "MGX", "MGY", "MGZ"]
        }
        self.port = Port(com=com, baudrate=baud, end='$', start='SPR',
                         file_name='Cansat', key=self.dict)
        self.port.connect()

    def __del__(self):
        self.wait()

    def run(self):
        print('[THREAD_PORT_START]')
        while True:
            self.pkg = self.port.reading_keys()
            if self.pkg["TYP"] == 'C':
                self.pkg1 = self.pkg
                self.carrier1.emit(self.pkg1)
            elif self.pkg["TYP"] == 'G':
                self.pkg2 = self.pkg
                self.carrier2.emit(self.pkg2)
            elif self.pkg["TYP"] == 'R':
                self.pkg3 = self.pkg
                self.carrier3.emit(self.pkg3)

    def stop(self):
        self._isRunning = False


class TimerThread(QThread):
    carrier1 = QtCore.Signal(object)
    carrier2 = QtCore.Signal(object)

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)
        self.clock = RTC()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.carrier1.emit(self.clock.time_pc())
            self.carrier2.emit(self.clock.time_elapsed())
            time.sleep(0.01)

    def stop(self):
        self._isRunning = False


class Controller:
    def __init__(self):
        self.show_ui()

    def show_ui(self):
        self.window_ui = QtWidgets.QMainWindow()
        self.ui_main = MainWindow()
        self.set_ui()
        self.set_clock()

    def set_clock(self):
        self.clock = TimerThread()
        self.clock.carrier1.connect(self.update_clock)
        self.clock.carrier2.connect(self.update_elapsed)
        self.clock.start()

    def update_clock(self, time):
        self.ui_main.ui.Time.setText(time)

    def update_elapsed(self, time):
        self.ui_main.ui.Elapsed.setText(time)

    def set_ui(self):
        self.ui_main.ui.date.setText(str(RTC.date()))

        self.container = {'PKG': [], "ALT": [],
                          "TMP": [], "VEL": [], "HUM": [], "LAT": 0, "LON": 0}

        self.rocket = {'PKG': [], "ALT": [],
                       "VEL": [], "TMP": [], "LAT": 0, "LON": 0}

    def start(self, com, baud):
        self.serial = SerialThread(com, baud)
        self.serial.carrier1.connect(self.update_container)
        self.serial.carrier2.connect(self.update_rocket)
        self.serial.carrier3.connect(self.update_ground)
        self.ui_main.ui.file_name.setText(self.serial.port.path)
        self.serial.start()

    def update_container(self, data):
        self.ui_main.ui.C_pkg.setText(data["PKG"])
        self.ui_main.ui.alt_c.setText(f'Altitude {data["ALT"]} M')
        self.ui_main.ui.tmp_c.setText(f'Temperature {data["TMP"]} C')
        self.ui_main.ui.vel_c.setText(f'Velocity {data["ACZ"]} M/S')
        self.ui_main.ui.hum_c.setText(f'Humidity {data["HUM"]} %')

        self.ui_main.ui.PM10.setText(data["PM10"])
        self.ui_main.ui.PM25.setText(data["PM25"])
        self.ui_main.ui.AQI.setText((data["PM25"]+data["PM10"])/2)

        self.ui_main.ui.acx_c.setText(f'[ACC X] {data["ACX"]}')
        self.ui_main.ui.acy_c.setText(f'[ACC Y] {data["ACY"]}')
        self.ui_main.ui.acz_c.setText(f'[ACC Z] {data["ACZ"]}')
        self.ui_main.ui.gyx_c.setText(f'[GYR X] {data["GYX"]}')
        self.ui_main.ui.gyy_c.setText(f'[GYR Y] {data["GYY"]}')
        self.ui_main.ui.gyz_c.setText(f'[GYR Z] {data["GYZ"]}')

        self.ui_main.ui.lat_c.setText(data["LAT"])
        self.ui_main.ui.lng_c.setText(data["LNG"])

        self.container["PKG"].append(int(data['PKG']))
        self.container["ALT"].append(float(data['ALT']))
        self.container["TMP"].append(float(data['TMP']))
        self.container["ACZ"].append(float(data['ACZ']))
        self.container["HUM"].append(float(data['HUM']))
        self.container["LAT"] = data["LAT"]
        self.container["LNG"] = data["LNG"]

        self.plot(self.ui_main.ui.graph_1, data['PKG'], data['ALT'])
        self.plot(self.ui_main.ui.graph_2, data['PKG'], data['TMP'])
        self.plot(self.ui_main.ui.graph_3, data['PKG'], data['ACZ'])
        self.plot(self.ui_main.ui.graph_4, data['PKG'], data['HUM'])
        x = threading.Thread(target=self.update_ground)
        x.start()

    def update_rocket(self, data):
        self.ui_main.ui.R_pkg.setText(data["PKG"])
        self.ui_main.ui.alt_r.setText(f'Altitude {data["ALT"]} M')
        self.ui_main.ui.tmp_r.setText(f'Temperature {data["TMP"]} C')
        self.ui_main.ui.vel_r.setText(f'Velocity {data["ACZ"]} M/S')

        self.ui_main.ui.acx_r.setText(f'[ACC X] {data["ACX"]}')
        self.ui_main.ui.acy_r.setText(f'[ACC Y] {data["ACY"]}')
        self.ui_main.ui.acz_r.setText(f'[ACC Z] {data["ACZ"]}')
        self.ui_main.ui.gyx_r.setText(f'[GYR X] {data["GYX"]}')
        self.ui_main.ui.gyy_r.setText(f'[GYR Y] {data["GYY"]}')
        self.ui_main.ui.gyz_r.setText(f'[GYR Z] {data["GYZ"]}')

        self.ui_main.ui.lat_r.setText(data["LAT"])
        self.ui_main.ui.lng_r.setText(data["LNG"])

        self.container["PKG"].append(int(data['PKG']))
        self.container["ALT"].append(float(data['ALT']))
        self.container["TMP"].append(float(data['TMP']))
        self.container["ACZ"].append(float(data['ACZ']))

        self.plot(self.ui_main.ui.graph_1, data['PKG'], data['ALT'])
        self.plot(self.ui_main.ui.graph_2, data['PKG'], data['TMP'])
        self.plot(self.ui_main.ui.graph_3, data['PKG'], data['ACZ'])

    def update_ground(self, data):
        "lat_g, lng_g, lat_c, lng_c, alt_g, alt_c, x, y, z"
        g = GNSS(data["LAT"], data["LNG"], self.container["LAT"],
                 self.container["LON"], data["ALT"], self.container["ALT"][-1], data["MGX"], data["MGY"], data["MGZ"])
        self.ui_main.ui.Azimuth.setText(str(g.azimuth()))
        self.ui_main.ui.Elevation.setText(str(g.elevation()))
        self.ui_main.ui.Heading.setText(str(g.heading()))
        self.ui_main.ui.Sight.setText(str(g.line_of_sight()))

    def plot(self, graph, pkg, data):
        x = threading.Thread(target=self.update_graph, args=(graph, pkg, data))
        x.start()

    def update_graph(self, graph, pkg, data):
        if len(pkg) > 50:
            graph.plot(pkg[-50:-1], data[-50:-1])
        else:
            graph.plot(pkg, data)


if __name__ == "__main__":
    app = QApplication()
    Window = Controller()
    sys.exit(app.exec())
