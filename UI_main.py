# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from PySide6.QtCharts import QChartView
from compasswidget import CompassWidget

import main_resource_rc

class Ui_GrounStation(object):
    def setupUi(self, GrounStation):
        if not GrounStation.objectName():
            GrounStation.setObjectName(u"GrounStation")
        GrounStation.resize(1856, 912)
        GrounStation.setMinimumSize(QSize(0, 0))
        GrounStation.setWindowOpacity(1.000000000000000)
        GrounStation.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(GrounStation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 75 16pt \"Consolas\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BG = QFrame(self.centralwidget)
        self.BG.setObjectName(u"BG")
        self.BG.setStyleSheet(u"background-color: rgb(39, 62, 84);")
        self.BG.setFrameShape(QFrame.StyledPanel)
        self.BG.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.BG)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.headframe = QFrame(self.BG)
        self.headframe.setObjectName(u"headframe")
        self.headframe.setMaximumSize(QSize(16777215, 75))
        self.headframe.setStyleSheet(u"")
        self.headframe.setFrameShape(QFrame.StyledPanel)
        self.headframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headframe)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.headframe)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(250, 250))
        self.logo.setStyleSheet(u"image: url(:/LOGO/logo.png);\n"
"alternate-background-color: rgba(255, 255, 255, 0);")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.logo)

        self.t_teamname = QLabel(self.headframe)
        self.t_teamname.setObjectName(u"t_teamname")
        font = QFont()
        font.setFamilies([u"Apple SD Gothic Neo"])
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        self.t_teamname.setFont(font)
        self.t_teamname.setStyleSheet(u"\n"
"font: 800 36pt \"Apple SD Gothic Neo\";")
        self.t_teamname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.t_teamname)

        self.btn_minimize = QPushButton(self.headframe)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMaximumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 214, 10);")

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_restore = QPushButton(self.headframe)
        self.btn_restore.setObjectName(u"btn_restore")
        self.btn_restore.setMaximumSize(QSize(20, 20))
        self.btn_restore.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(13, 214, 30);")

        self.horizontalLayout.addWidget(self.btn_restore)

        self.btn_close = QPushButton(self.headframe)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout_6.addWidget(self.headframe, 0, 0, 1, 1)

        self.bodyframe = QFrame(self.BG)
        self.bodyframe.setObjectName(u"bodyframe")
        self.bodyframe.setStyleSheet(u"")
        self.bodyframe.setFrameShape(QFrame.StyledPanel)
        self.bodyframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bodyframe)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.bodyframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.t_c_batt = QLabel(self.frame_2)
        self.t_c_batt.setObjectName(u"t_c_batt")
        self.t_c_batt.setMinimumSize(QSize(0, 0))
        self.t_c_batt.setMaximumSize(QSize(16777215, 16777215))
        self.t_c_batt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_batt, 4, 0, 1, 1)

        self.t_sight = QLabel(self.frame_2)
        self.t_sight.setObjectName(u"t_sight")
        self.t_sight.setMinimumSize(QSize(100, 30))
        self.t_sight.setMaximumSize(QSize(123123, 123123))
        self.t_sight.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_sight, 14, 7, 1, 1)

        self.Heading = QLabel(self.frame_2)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setMinimumSize(QSize(100, 30))
        self.Heading.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.Heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Heading, 14, 6, 1, 1)

        self.t_heading = QLabel(self.frame_2)
        self.t_heading.setObjectName(u"t_heading")
        self.t_heading.setMinimumSize(QSize(100, 30))
        self.t_heading.setMaximumSize(QSize(100, 30))
        self.t_heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_heading, 14, 5, 1, 1)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.State_bar = QProgressBar(self.frame)
        self.State_bar.setObjectName(u"State_bar")
        self.State_bar.setMinimumSize(QSize(0, 30))
        self.State_bar.setMaximumSize(QSize(16777215, 30))
        self.State_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 15px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:15px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 111, 151, 255), stop:1 rgba(169, 214, 229, 255));\n"
"}")
        self.State_bar.setValue(24)
        self.State_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.State_bar, 0, 0, 1, 2)

        self.t_state = QLabel(self.frame)
        self.t_state.setObjectName(u"t_state")
        self.t_state.setMinimumSize(QSize(200, 30))
        self.t_state.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.t_state.setFont(font1)

        self.gridLayout_8.addWidget(self.t_state, 1, 0, 1, 1)

        self.state_t = QLabel(self.frame)
        self.state_t.setObjectName(u"state_t")
        self.state_t.setMinimumSize(QSize(0, 30))
        self.state_t.setMaximumSize(QSize(16777215, 30))
        self.state_t.setFont(font1)

        self.gridLayout_8.addWidget(self.state_t, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 11)

        self.t_Drop = QLabel(self.frame_2)
        self.t_Drop.setObjectName(u"t_Drop")
        self.t_Drop.setMinimumSize(QSize(100, 30))
        self.t_Drop.setMaximumSize(QSize(100, 30))
        self.t_Drop.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.t_Drop.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_Drop, 3, 0, 1, 1)

        self.Drop = QLabel(self.frame_2)
        self.Drop.setObjectName(u"Drop")
        self.Drop.setMinimumSize(QSize(100, 30))
        self.Drop.setMaximumSize(QSize(100, 30))
        self.Drop.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.Drop.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Drop.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Drop, 3, 1, 1, 1)

        self.t_operation = QLabel(self.frame_2)
        self.t_operation.setObjectName(u"t_operation")
        self.t_operation.setMinimumSize(QSize(100, 30))
        self.t_operation.setMaximumSize(QSize(100, 60))
        self.t_operation.setStyleSheet(u"")
        self.t_operation.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_operation, 2, 0, 1, 1)

        self.R_pkg = QLabel(self.frame_2)
        self.R_pkg.setObjectName(u"R_pkg")
        self.R_pkg.setMinimumSize(QSize(100, 30))
        self.R_pkg.setMaximumSize(QSize(100, 60))
        self.R_pkg.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.R_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_pkg, 6, 1, 1, 1)

        self.t_container_1 = QLabel(self.frame_2)
        self.t_container_1.setObjectName(u"t_container_1")
        self.t_container_1.setMinimumSize(QSize(200, 50))
        self.t_container_1.setMaximumSize(QSize(16777215, 60))
        self.t_container_1.setAutoFillBackground(False)
        self.t_container_1.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"alternate-background-color: rgba(255, 255, 255, 100);\n"
"background-color: none;\n"
"border-radius: 10px;\n"
"")
        self.t_container_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_container_1, 1, 0, 1, 2)

        self.C_velo_graph = QChartView(self.frame_2)
        self.C_velo_graph.setObjectName(u"C_velo_graph")
        self.C_velo_graph.setMinimumSize(QSize(350, 200))
        self.C_velo_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.C_velo_graph, 1, 6, 4, 3)

        self.C_alt_graph = QChartView(self.frame_2)
        self.C_alt_graph.setObjectName(u"C_alt_graph")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_alt_graph.sizePolicy().hasHeightForWidth())
        self.C_alt_graph.setSizePolicy(sizePolicy)
        self.C_alt_graph.setMinimumSize(QSize(350, 200))
        self.C_alt_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.C_alt_graph, 1, 2, 4, 2)

        self.C_humid_graph = QChartView(self.frame_2)
        self.C_humid_graph.setObjectName(u"C_humid_graph")
        sizePolicy.setHeightForWidth(self.C_humid_graph.sizePolicy().hasHeightForWidth())
        self.C_humid_graph.setSizePolicy(sizePolicy)
        self.C_humid_graph.setMinimumSize(QSize(350, 200))
        self.C_humid_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.C_humid_graph, 1, 9, 4, 2)

        self.t_gd = QLabel(self.frame_2)
        self.t_gd.setObjectName(u"t_gd")
        self.t_gd.setMinimumSize(QSize(100, 30))
        self.t_gd.setMaximumSize(QSize(123123, 123123))
        self.t_gd.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_gd, 14, 9, 1, 1)

        self.C_temp_graph = QChartView(self.frame_2)
        self.C_temp_graph.setObjectName(u"C_temp_graph")
        sizePolicy.setHeightForWidth(self.C_temp_graph.sizePolicy().hasHeightForWidth())
        self.C_temp_graph.setSizePolicy(sizePolicy)
        self.C_temp_graph.setMinimumSize(QSize(350, 200))
        self.C_temp_graph.setMaximumSize(QSize(400, 250))

        self.gridLayout_2.addWidget(self.C_temp_graph, 1, 4, 4, 2)

        self.GD = QLabel(self.frame_2)
        self.GD.setObjectName(u"GD")
        self.GD.setMinimumSize(QSize(100, 30))
        self.GD.setMaximumSize(QSize(100, 30))
        self.GD.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.GD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.GD, 14, 10, 1, 1)

        self.C_batt_Bar = QProgressBar(self.frame_2)
        self.C_batt_Bar.setObjectName(u"C_batt_Bar")
        self.C_batt_Bar.setMinimumSize(QSize(0, 30))
        self.C_batt_Bar.setMaximumSize(QSize(100, 16777215))
        self.C_batt_Bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 15px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 15px;\n"
"	\n"
"	background-color: rgb(56, 122, 71);\n"
"}")
        self.C_batt_Bar.setValue(100)
        self.C_batt_Bar.setAlignment(Qt.AlignCenter)
        self.C_batt_Bar.setTextVisible(True)

        self.gridLayout_2.addWidget(self.C_batt_Bar, 4, 1, 1, 1)

        self.t_rocket_1 = QLabel(self.frame_2)
        self.t_rocket_1.setObjectName(u"t_rocket_1")
        self.t_rocket_1.setMinimumSize(QSize(200, 50))
        self.t_rocket_1.setMaximumSize(QSize(16777215, 60))
        self.t_rocket_1.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"alternate-background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 10px;\n"
"")
        self.t_rocket_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_rocket_1, 5, 0, 1, 2)

        self.C_pkg = QLabel(self.frame_2)
        self.C_pkg.setObjectName(u"C_pkg")
        self.C_pkg.setMinimumSize(QSize(100, 30))
        self.C_pkg.setMaximumSize(QSize(100, 60))
        self.C_pkg.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.C_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_pkg, 2, 1, 1, 1)

        self.t_apogee = QLabel(self.frame_2)
        self.t_apogee.setObjectName(u"t_apogee")
        self.t_apogee.setMinimumSize(QSize(100, 30))
        self.t_apogee.setMaximumSize(QSize(100, 60))
        self.t_apogee.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_apogee, 7, 0, 1, 1)

        self.t_r_pkg = QLabel(self.frame_2)
        self.t_r_pkg.setObjectName(u"t_r_pkg")
        self.t_r_pkg.setMinimumSize(QSize(100, 30))
        self.t_r_pkg.setMaximumSize(QSize(100, 60))
        self.t_r_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_pkg, 6, 0, 1, 1)

        self.Sight = QLabel(self.frame_2)
        self.Sight.setObjectName(u"Sight")
        self.Sight.setMinimumSize(QSize(100, 30))
        self.Sight.setMaximumSize(QSize(100, 30))
        self.Sight.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.Sight.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Sight, 14, 8, 1, 1)

        self.t_r_batt = QLabel(self.frame_2)
        self.t_r_batt.setObjectName(u"t_r_batt")
        self.t_r_batt.setMinimumSize(QSize(0, 0))
        self.t_r_batt.setMaximumSize(QSize(16777215, 16777215))
        self.t_r_batt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_batt, 8, 0, 1, 1)

        self.apogee = QLabel(self.frame_2)
        self.apogee.setObjectName(u"apogee")
        self.apogee.setMinimumSize(QSize(100, 30))
        self.apogee.setMaximumSize(QSize(100, 60))
        self.apogee.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.apogee.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.apogee, 7, 1, 1, 1)

        self.R_batt_Bar = QProgressBar(self.frame_2)
        self.R_batt_Bar.setObjectName(u"R_batt_Bar")
        self.R_batt_Bar.setMinimumSize(QSize(0, 30))
        self.R_batt_Bar.setMaximumSize(QSize(100, 16777215))
        self.R_batt_Bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 15px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 15px;\n"
"	\n"
"	background-color: rgb(56, 122, 71);\n"
"}")
        self.R_batt_Bar.setValue(100)
        self.R_batt_Bar.setAlignment(Qt.AlignCenter)
        self.R_batt_Bar.setTextVisible(True)
        self.R_batt_Bar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.R_batt_Bar, 8, 1, 1, 1)

        self.R_alt_graph = QChartView(self.frame_2)
        self.R_alt_graph.setObjectName(u"R_alt_graph")
        sizePolicy.setHeightForWidth(self.R_alt_graph.sizePolicy().hasHeightForWidth())
        self.R_alt_graph.setSizePolicy(sizePolicy)
        self.R_alt_graph.setMinimumSize(QSize(350, 200))
        self.R_alt_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.R_alt_graph, 5, 2, 4, 2)

        self.t_az = QLabel(self.frame_2)
        self.t_az.setObjectName(u"t_az")
        self.t_az.setMinimumSize(QSize(100, 30))
        self.t_az.setMaximumSize(QSize(123123, 123123))
        self.t_az.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_az, 14, 0, 1, 2)

        self.Azimuth = QLabel(self.frame_2)
        self.Azimuth.setObjectName(u"Azimuth")
        self.Azimuth.setMinimumSize(QSize(100, 30))
        self.Azimuth.setMaximumSize(QSize(100, 30))
        self.Azimuth.setCursor(QCursor(Qt.ArrowCursor))
        self.Azimuth.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.Azimuth.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Azimuth, 14, 2, 1, 1)

        self.R_velo_graph = QChartView(self.frame_2)
        self.R_velo_graph.setObjectName(u"R_velo_graph")
        self.R_velo_graph.setMinimumSize(QSize(350, 200))
        self.R_velo_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.R_velo_graph, 5, 6, 4, 3)

        self.t_ele = QLabel(self.frame_2)
        self.t_ele.setObjectName(u"t_ele")
        self.t_ele.setMinimumSize(QSize(100, 30))
        self.t_ele.setMaximumSize(QSize(123123, 123123))
        self.t_ele.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_ele, 14, 3, 1, 1)

        self.R_temp_graph = QChartView(self.frame_2)
        self.R_temp_graph.setObjectName(u"R_temp_graph")
        sizePolicy.setHeightForWidth(self.R_temp_graph.sizePolicy().hasHeightForWidth())
        self.R_temp_graph.setSizePolicy(sizePolicy)
        self.R_temp_graph.setMinimumSize(QSize(350, 200))
        self.R_temp_graph.setMaximumSize(QSize(350, 250))

        self.gridLayout_2.addWidget(self.R_temp_graph, 5, 4, 4, 2)

        self.Elevation = QLabel(self.frame_2)
        self.Elevation.setObjectName(u"Elevation")
        self.Elevation.setMinimumSize(QSize(100, 30))
        self.Elevation.setMaximumSize(QSize(100, 30))
        self.Elevation.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.Elevation.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Elevation, 14, 4, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.t_mui = QLabel(self.frame_4)
        self.t_mui.setObjectName(u"t_mui")
        self.t_mui.setMinimumSize(QSize(100, 30))
        self.t_mui.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Apple SD Gothic Neo"])
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setItalic(False)
        self.t_mui.setFont(font2)
        self.t_mui.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"border-radius: 10px;\n"
"")
        self.t_mui.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_mui, 0, 0, 1, 8)

        self.t_c_lat = QLabel(self.frame_4)
        self.t_c_lat.setObjectName(u"t_c_lat")
        self.t_c_lat.setMinimumSize(QSize(100, 30))
        self.t_c_lat.setMaximumSize(QSize(200, 30))
        self.t_c_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_lat, 4, 0, 1, 1)

        self.t_r_lat = QLabel(self.frame_4)
        self.t_r_lat.setObjectName(u"t_r_lat")
        self.t_r_lat.setMinimumSize(QSize(100, 30))
        self.t_r_lat.setMaximumSize(QSize(200, 30))
        self.t_r_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_lat, 4, 4, 1, 1)

        self.R_latitude = QLabel(self.frame_4)
        self.R_latitude.setObjectName(u"R_latitude")
        self.R_latitude.setMinimumSize(QSize(100, 30))
        self.R_latitude.setMaximumSize(QSize(200, 30))
        self.R_latitude.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.R_latitude.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_latitude, 4, 5, 1, 1)

        self.C_latitude = QLabel(self.frame_4)
        self.C_latitude.setObjectName(u"C_latitude")
        self.C_latitude.setMaximumSize(QSize(200, 16777215))
        self.C_latitude.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.C_latitude.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_latitude, 4, 1, 1, 1)

        self.t_r_long = QLabel(self.frame_4)
        self.t_r_long.setObjectName(u"t_r_long")
        self.t_r_long.setMinimumSize(QSize(100, 30))
        self.t_r_long.setMaximumSize(QSize(200, 30))
        self.t_r_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_long, 4, 6, 1, 1)

        self.C_longitude = QLabel(self.frame_4)
        self.C_longitude.setObjectName(u"C_longitude")
        self.C_longitude.setMinimumSize(QSize(100, 30))
        self.C_longitude.setMaximumSize(QSize(200, 30))
        self.C_longitude.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.C_longitude.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_longitude, 4, 3, 1, 1)

        self.t_c_long = QLabel(self.frame_4)
        self.t_c_long.setObjectName(u"t_c_long")
        self.t_c_long.setMinimumSize(QSize(100, 30))
        self.t_c_long.setMaximumSize(QSize(200, 30))
        self.t_c_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_long, 4, 2, 1, 1)

        self.R_longitude = QLabel(self.frame_4)
        self.R_longitude.setObjectName(u"R_longitude")
        self.R_longitude.setMinimumSize(QSize(100, 30))
        self.R_longitude.setMaximumSize(QSize(200, 30))
        self.R_longitude.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.R_longitude.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_longitude, 4, 7, 1, 1)

        self.t_rocket_2 = QLabel(self.frame_4)
        self.t_rocket_2.setObjectName(u"t_rocket_2")
        self.t_rocket_2.setMinimumSize(QSize(0, 30))
        self.t_rocket_2.setMaximumSize(QSize(16777215, 30))
        self.t_rocket_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_rocket_2, 1, 4, 1, 4)

        self.t_container_2 = QLabel(self.frame_4)
        self.t_container_2.setObjectName(u"t_container_2")
        self.t_container_2.setMinimumSize(QSize(0, 30))
        self.t_container_2.setMaximumSize(QSize(16777215, 30))
        self.t_container_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_container_2, 1, 0, 1, 4)

        self.C_acc_graph = QChartView(self.frame_4)
        self.C_acc_graph.setObjectName(u"C_acc_graph")
        self.C_acc_graph.setMinimumSize(QSize(350, 200))

        self.gridLayout_5.addWidget(self.C_acc_graph, 2, 0, 2, 2)

        self.C_gyro_graph = QChartView(self.frame_4)
        self.C_gyro_graph.setObjectName(u"C_gyro_graph")
        self.C_gyro_graph.setMinimumSize(QSize(350, 200))

        self.gridLayout_5.addWidget(self.C_gyro_graph, 2, 2, 2, 2)

        self.R_acc_graph = QChartView(self.frame_4)
        self.R_acc_graph.setObjectName(u"R_acc_graph")
        self.R_acc_graph.setMinimumSize(QSize(350, 200))

        self.gridLayout_5.addWidget(self.R_acc_graph, 2, 4, 2, 2)

        self.R_gyro_graph = QChartView(self.frame_4)
        self.R_gyro_graph.setObjectName(u"R_gyro_graph")
        self.R_gyro_graph.setMinimumSize(QSize(350, 200))

        self.gridLayout_5.addWidget(self.R_gyro_graph, 2, 6, 2, 2)


        self.gridLayout_2.addWidget(self.frame_4, 12, 0, 1, 11)

        self.frame5 = QFrame(self.frame_2)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setFrameShape(QFrame.StyledPanel)
        self.frame5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AQI = QLabel(self.frame5)
        self.AQI.setObjectName(u"AQI")
        self.AQI.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.AQI.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.AQI, 3, 1, 1, 1)

        self.t_aqi = QLabel(self.frame5)
        self.t_aqi.setObjectName(u"t_aqi")
        self.t_aqi.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_aqi, 3, 0, 1, 1)

        self.PM10 = QLabel(self.frame5)
        self.PM10.setObjectName(u"PM10")
        self.PM10.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.PM10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.PM10, 1, 1, 1, 1)

        self.PM25 = QLabel(self.frame5)
        self.PM25.setObjectName(u"PM25")
        self.PM25.setStyleSheet(u"color: rgb(242, 48, 106);\n"
"color: rgb(117, 191, 255);")
        self.PM25.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.PM25, 2, 1, 1, 1)

        self.t_pm25 = QLabel(self.frame5)
        self.t_pm25.setObjectName(u"t_pm25")
        self.t_pm25.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_pm25, 2, 0, 1, 1)

        self.t_parti = QLabel(self.frame5)
        self.t_parti.setObjectName(u"t_parti")
        self.t_parti.setMinimumSize(QSize(100, 30))
        self.t_parti.setFont(font2)
        self.t_parti.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"alternate-background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 10px;\n"
"")
        self.t_parti.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_parti, 0, 0, 1, 2)

        self.t_pm10 = QLabel(self.frame5)
        self.t_pm10.setObjectName(u"t_pm10")
        self.t_pm10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_pm10, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame5, 5, 9, 4, 2)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.bodyframe)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(250, 0))
        self.widget_3.setMaximumSize(QSize(250, 16777215))
        self.widget_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Time = QLabel(self.widget_3)
        self.Time.setObjectName(u"Time")
        self.Time.setMinimumSize(QSize(100, 0))
        self.Time.setMaximumSize(QSize(16777215, 40))
        self.Time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Time, 2, 0, 1, 4)

        self.t_time = QLabel(self.widget_3)
        self.t_time.setObjectName(u"t_time")
        self.t_time.setMinimumSize(QSize(60, 0))
        self.t_time.setMaximumSize(QSize(16777215, 40))
        self.t_time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.t_time, 1, 0, 1, 4)

        self.btn_refresh = QPushButton(self.widget_3)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_refresh, 6, 1, 1, 3)

        self.btn_c_on = QPushButton(self.widget_3)
        self.btn_c_on.setObjectName(u"btn_c_on")
        self.btn_c_on.setMinimumSize(QSize(50, 0))
        self.btn_c_on.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_c_on, 9, 2, 1, 1)

        self.t_rocket = QLabel(self.widget_3)
        self.t_rocket.setObjectName(u"t_rocket")
        self.t_rocket.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_rocket, 11, 0, 1, 2)

        self.t_container = QLabel(self.widget_3)
        self.t_container.setObjectName(u"t_container")
        self.t_container.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_container, 9, 0, 1, 2)

        self.btn_r_on = QPushButton(self.widget_3)
        self.btn_r_on.setObjectName(u"btn_r_on")
        self.btn_r_on.setMinimumSize(QSize(50, 0))
        self.btn_r_on.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_r_on, 11, 2, 1, 1)

        self.btn_mqtt = QPushButton(self.widget_3)
        self.btn_mqtt.setObjectName(u"btn_mqtt")
        self.btn_mqtt.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_mqtt, 6, 0, 1, 1)

        self.portlist = QComboBox(self.widget_3)
        self.portlist.setObjectName(u"portlist")
        self.portlist.setStyleSheet(u"background-color: rgb(19, 31, 43);")

        self.gridLayout.addWidget(self.portlist, 5, 0, 1, 1)

        self.btn_r_off = QPushButton(self.widget_3)
        self.btn_r_off.setObjectName(u"btn_r_off")
        self.btn_r_off.setMinimumSize(QSize(50, 0))
        self.btn_r_off.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_r_off, 11, 3, 1, 1)

        self.btn_clear = QPushButton(self.widget_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_clear, 7, 0, 1, 4)

        self.btn_connect = QPushButton(self.widget_3)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_connect, 5, 1, 1, 3)

        self.btn_c_off = QPushButton(self.widget_3)
        self.btn_c_off.setObjectName(u"btn_c_off")
        self.btn_c_off.setMinimumSize(QSize(50, 0))
        self.btn_c_off.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"border-radius: 5px;\n"
"color: rgb(211, 223, 227);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_c_off, 9, 3, 1, 1)

        self.t_elapsed = QLabel(self.widget_3)
        self.t_elapsed.setObjectName(u"t_elapsed")
        self.t_elapsed.setMinimumSize(QSize(60, 0))
        self.t_elapsed.setMaximumSize(QSize(16777215, 40))
        self.t_elapsed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.t_elapsed, 3, 0, 1, 4)

        self.Elapsed = QLabel(self.widget_3)
        self.Elapsed.setObjectName(u"Elapsed")
        self.Elapsed.setMinimumSize(QSize(100, 0))
        self.Elapsed.setMaximumSize(QSize(16777215, 40))
        self.Elapsed.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Elapsed, 4, 0, 1, 4)

        self.compass = CompassWidget(self.widget_3)
        self.compass.setObjectName(u"compass")
        self.compass.setMaximumSize(QSize(250, 250))

        self.gridLayout.addWidget(self.compass, 0, 0, 1, 4)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.bodyframe, 1, 0, 1, 1)

        self.endframe = QFrame(self.BG)
        self.endframe.setObjectName(u"endframe")
        self.endframe.setMaximumSize(QSize(16777215, 30))
        self.endframe.setStyleSheet(u"")
        self.endframe.setFrameShape(QFrame.StyledPanel)
        self.endframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.endframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.copyright = QLabel(self.endframe)
        self.copyright.setObjectName(u"copyright")

        self.horizontalLayout_2.addWidget(self.copyright)


        self.gridLayout_6.addWidget(self.endframe, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.BG, 0, 0, 1, 1)

        GrounStation.setCentralWidget(self.centralwidget)

        self.retranslateUi(GrounStation)

        QMetaObject.connectSlotsByName(GrounStation)
    # setupUi

    def retranslateUi(self, GrounStation):
        GrounStation.setWindowTitle(QCoreApplication.translate("GrounStation", u"ALIEN SET", None))
        self.t_teamname.setText(QCoreApplication.translate("GrounStation", u"ALIEN SAT", None))
        self.btn_minimize.setText("")
        self.btn_restore.setText("")
        self.btn_close.setText("")
        self.t_c_batt.setText(QCoreApplication.translate("GrounStation", u"Battery", None))
        self.t_sight.setText(QCoreApplication.translate("GrounStation", u"Sight", None))
        self.Heading.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_heading.setText(QCoreApplication.translate("GrounStation", u"Heading", None))
        self.State_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_state.setText(QCoreApplication.translate("GrounStation", u"STATE : ", None))
        self.state_t.setText(QCoreApplication.translate("GrounStation", u"PRELAUNCH", None))
        self.t_Drop.setText(QCoreApplication.translate("GrounStation", u"Drop : ", None))
        self.Drop.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_operation.setText(QCoreApplication.translate("GrounStation", u"PKG :", None))
        self.R_pkg.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_container_1.setText(QCoreApplication.translate("GrounStation", u"CANSAT", None))
        self.t_gd.setText(QCoreApplication.translate("GrounStation", u"GD.", None))
        self.GD.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.C_batt_Bar.setFormat(QCoreApplication.translate("GrounStation", u"%p", None))
        self.t_rocket_1.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.C_pkg.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_apogee.setText(QCoreApplication.translate("GrounStation", u"PEAK :", None))
        self.t_r_pkg.setText(QCoreApplication.translate("GrounStation", u"PKG :", None))
        self.Sight.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_batt.setText(QCoreApplication.translate("GrounStation", u"Battery", None))
        self.apogee.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.R_batt_Bar.setFormat(QCoreApplication.translate("GrounStation", u"%p", None))
        self.t_az.setText(QCoreApplication.translate("GrounStation", u"Azimuth", None))
        self.Azimuth.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_ele.setText(QCoreApplication.translate("GrounStation", u"Elevation", None))
        self.Elevation.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_mui.setText(QCoreApplication.translate("GrounStation", u"GNSS & IMU", None))
        self.t_c_lat.setText(QCoreApplication.translate("GrounStation", u" Latitude", None))
        self.t_r_lat.setText(QCoreApplication.translate("GrounStation", u"Latitude", None))
        self.R_latitude.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.C_latitude.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_long.setText(QCoreApplication.translate("GrounStation", u"Longitude", None))
        self.C_longitude.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_c_long.setText(QCoreApplication.translate("GrounStation", u"Longitude", None))
        self.R_longitude.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_rocket_2.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.t_container_2.setText(QCoreApplication.translate("GrounStation", u"CONTAINER", None))
        self.AQI.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_aqi.setText(QCoreApplication.translate("GrounStation", u"AQI", None))
        self.PM10.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.PM25.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_pm25.setText(QCoreApplication.translate("GrounStation", u"PM 2.5", None))
        self.t_parti.setText(QCoreApplication.translate("GrounStation", u"DUST PARTICLE", None))
        self.t_pm10.setText(QCoreApplication.translate("GrounStation", u"PM 10", None))
        self.Time.setText(QCoreApplication.translate("GrounStation", u"HH:MM:SS.MS", None))
        self.t_time.setText(QCoreApplication.translate("GrounStation", u"TIME :", None))
        self.btn_refresh.setText(QCoreApplication.translate("GrounStation", u"Refresh", None))
        self.btn_c_on.setText(QCoreApplication.translate("GrounStation", u"ON", None))
        self.t_rocket.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.t_container.setText(QCoreApplication.translate("GrounStation", u"CANSAT", None))
        self.btn_r_on.setText(QCoreApplication.translate("GrounStation", u"ON", None))
        self.btn_mqtt.setText(QCoreApplication.translate("GrounStation", u"MQTT", None))
        self.btn_r_off.setText(QCoreApplication.translate("GrounStation", u"OFF", None))
        self.btn_clear.setText(QCoreApplication.translate("GrounStation", u"Clear", None))
        self.btn_connect.setText(QCoreApplication.translate("GrounStation", u"Connect", None))
        self.btn_c_off.setText(QCoreApplication.translate("GrounStation", u"OFF", None))
        self.t_elapsed.setText(QCoreApplication.translate("GrounStation", u"ELAPSED :", None))
        self.Elapsed.setText(QCoreApplication.translate("GrounStation", u"HH:MM:SS.MS", None))
        self.copyright.setText(QCoreApplication.translate("GrounStation", u"Ground station for Alien sat by space AC for Thailand CanSat competition V0.9", None))
    # retranslateUi

