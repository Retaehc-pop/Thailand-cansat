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

import main_resource_rc

class Ui_GrounStation(object):
    def setupUi(self, GrounStation):
        if not GrounStation.objectName():
            GrounStation.setObjectName(u"GrounStation")
        GrounStation.resize(1856, 811)
        GrounStation.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(GrounStation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"font: 800 14pt \"Apple SD Gothic Neo\";\n"
"color: rgb(255, 195, 0);\n"
"")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.BG = QFrame(self.centralwidget)
        self.BG.setObjectName(u"BG")
        self.BG.setStyleSheet(u"background-color: rgb(5, 5, 5);")
        self.BG.setFrameShape(QFrame.StyledPanel)
        self.BG.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.BG)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.headframe = QFrame(self.BG)
        self.headframe.setObjectName(u"headframe")
        self.headframe.setMaximumSize(QSize(16777215, 75))
        self.headframe.setStyleSheet(u"background-color: rgb(29, 31, 35);")
        self.headframe.setFrameShape(QFrame.StyledPanel)
        self.headframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headframe)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.frame_3 = QFrame(self.bodyframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 0))
        self.frame_3.setMaximumSize(QSize(250, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.t_elapsed = QLabel(self.frame_3)
        self.t_elapsed.setObjectName(u"t_elapsed")
        self.t_elapsed.setMinimumSize(QSize(60, 0))
        self.t_elapsed.setMaximumSize(QSize(16777215, 40))
        self.t_elapsed.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_elapsed, 2, 0, 1, 1)

        self.btn_r_off = QPushButton(self.frame_3)
        self.btn_r_off.setObjectName(u"btn_r_off")
        self.btn_r_off.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_r_off, 9, 3, 1, 1)

        self.Time = QLabel(self.frame_3)
        self.Time.setObjectName(u"Time")
        self.Time.setMinimumSize(QSize(60, 0))
        self.Time.setMaximumSize(QSize(16777215, 40))
        self.Time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Time, 1, 1, 1, 3)

        self.t_time = QLabel(self.frame_3)
        self.t_time.setObjectName(u"t_time")
        self.t_time.setMinimumSize(QSize(60, 0))
        self.t_time.setMaximumSize(QSize(16777215, 40))
        self.t_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_time, 1, 0, 1, 1)

        self.logo = QFrame(self.frame_3)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(250, 250))
        self.logo.setStyleSheet(u"image: url(:/LOGO/logo.png);\n"
"alternate-background-color: rgba(255, 255, 255, 0);")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 4)

        self.btn_c_off = QPushButton(self.frame_3)
        self.btn_c_off.setObjectName(u"btn_c_off")
        self.btn_c_off.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_c_off, 7, 3, 1, 1)

        self.Elapsed = QLabel(self.frame_3)
        self.Elapsed.setObjectName(u"Elapsed")
        self.Elapsed.setMinimumSize(QSize(60, 0))
        self.Elapsed.setMaximumSize(QSize(16777215, 40))
        self.Elapsed.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Elapsed, 2, 1, 1, 3)

        self.btn_clear = QPushButton(self.frame_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_clear, 5, 0, 1, 4)

        self.btn_connect = QPushButton(self.frame_3)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_connect, 3, 1, 1, 3)

        self.btn_refresh = QPushButton(self.frame_3)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_refresh, 4, 1, 1, 3)

        self.t_container = QLabel(self.frame_3)
        self.t_container.setObjectName(u"t_container")
        self.t_container.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_container, 7, 0, 1, 2)

        self.btn_r_on = QPushButton(self.frame_3)
        self.btn_r_on.setObjectName(u"btn_r_on")
        self.btn_r_on.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_r_on, 9, 2, 1, 1)

        self.btn_c_on = QPushButton(self.frame_3)
        self.btn_c_on.setObjectName(u"btn_c_on")
        self.btn_c_on.setStyleSheet(u"background-color: rgb(0, 53, 102);\n"
"color: rgb(211, 223, 227);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.btn_c_on, 7, 2, 1, 1)

        self.t_rocket = QLabel(self.frame_3)
        self.t_rocket.setObjectName(u"t_rocket")
        self.t_rocket.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.t_rocket, 9, 0, 1, 2)

        self.portlist = QComboBox(self.frame_3)
        self.portlist.addItem("")
        self.portlist.setObjectName(u"portlist")

        self.gridLayout.addWidget(self.portlist, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.bodyframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.t_gd = QLabel(self.frame_2)
        self.t_gd.setObjectName(u"t_gd")
        self.t_gd.setMinimumSize(QSize(100, 30))
        self.t_gd.setMaximumSize(QSize(100, 30))
        self.t_gd.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_gd, 14, 8, 1, 1)

        self.GD = QLabel(self.frame_2)
        self.GD.setObjectName(u"GD")
        self.GD.setMinimumSize(QSize(100, 30))
        self.GD.setMaximumSize(QSize(100, 30))
        self.GD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.GD, 14, 9, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.C_oriz_bar = QProgressBar(self.frame_4)
        self.C_oriz_bar.setObjectName(u"C_oriz_bar")
        self.C_oriz_bar.setMinimumSize(QSize(0, 30))
        self.C_oriz_bar.setMaximumSize(QSize(100, 35))
        self.C_oriz_bar.setSizeIncrement(QSize(0, 0))
        self.C_oriz_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(233, 151, 54);\n"
"}")
        self.C_oriz_bar.setMinimum(-100)
        self.C_oriz_bar.setValue(0)
        self.C_oriz_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_oriz_bar, 4, 3, 1, 1)

        self.t_c_acc_z = QLabel(self.frame_4)
        self.t_c_acc_z.setObjectName(u"t_c_acc_z")
        self.t_c_acc_z.setMinimumSize(QSize(0, 30))
        self.t_c_acc_z.setMaximumSize(QSize(16777215, 35))
        self.t_c_acc_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_acc_z, 4, 0, 1, 1)

        self.C_accy_bar = QProgressBar(self.frame_4)
        self.C_accy_bar.setObjectName(u"C_accy_bar")
        self.C_accy_bar.setMinimumSize(QSize(0, 30))
        self.C_accy_bar.setMaximumSize(QSize(100, 35))
        self.C_accy_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(231, 76, 60);\n"
"}")
        self.C_accy_bar.setMinimum(-100)
        self.C_accy_bar.setValue(0)
        self.C_accy_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_accy_bar, 3, 1, 1, 1)

        self.C_accx_bar = QProgressBar(self.frame_4)
        self.C_accx_bar.setObjectName(u"C_accx_bar")
        self.C_accx_bar.setMinimumSize(QSize(0, 30))
        self.C_accx_bar.setMaximumSize(QSize(100, 35))
        self.C_accx_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(212, 223, 228);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 118, 242);\n"
"}")
        self.C_accx_bar.setMinimum(-100)
        self.C_accx_bar.setValue(0)
        self.C_accx_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_accx_bar, 2, 1, 1, 1)

        self.t_c_orien_z = QLabel(self.frame_4)
        self.t_c_orien_z.setObjectName(u"t_c_orien_z")
        self.t_c_orien_z.setMinimumSize(QSize(0, 30))
        self.t_c_orien_z.setMaximumSize(QSize(16777215, 35))
        self.t_c_orien_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_orien_z, 4, 2, 1, 1)

        self.t_c_acc_x = QLabel(self.frame_4)
        self.t_c_acc_x.setObjectName(u"t_c_acc_x")
        self.t_c_acc_x.setMinimumSize(QSize(0, 30))
        self.t_c_acc_x.setMaximumSize(QSize(16777215, 35))
        self.t_c_acc_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_acc_x, 2, 0, 1, 1)

        self.R_oriz_bar = QProgressBar(self.frame_4)
        self.R_oriz_bar.setObjectName(u"R_oriz_bar")
        self.R_oriz_bar.setMinimumSize(QSize(0, 30))
        self.R_oriz_bar.setMaximumSize(QSize(100, 35))
        self.R_oriz_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(233, 151, 54);\n"
"}")
        self.R_oriz_bar.setMinimum(-100)
        self.R_oriz_bar.setValue(0)
        self.R_oriz_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_oriz_bar, 4, 7, 1, 1)

        self.t_r_orien_z = QLabel(self.frame_4)
        self.t_r_orien_z.setObjectName(u"t_r_orien_z")
        self.t_r_orien_z.setMinimumSize(QSize(0, 30))
        self.t_r_orien_z.setMaximumSize(QSize(16777215, 35))
        self.t_r_orien_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_orien_z, 4, 6, 1, 1)

        self.t_mui = QLabel(self.frame_4)
        self.t_mui.setObjectName(u"t_mui")
        self.t_mui.setMinimumSize(QSize(100, 30))
        self.t_mui.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Apple SD Gothic Neo"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        self.t_mui.setFont(font1)
        self.t_mui.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"border-radius: 10px;\n"
"")
        self.t_mui.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_mui, 0, 0, 1, 8)

        self.t_r_acc_y = QLabel(self.frame_4)
        self.t_r_acc_y.setObjectName(u"t_r_acc_y")
        self.t_r_acc_y.setMinimumSize(QSize(0, 30))
        self.t_r_acc_y.setMaximumSize(QSize(16777215, 35))
        self.t_r_acc_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_acc_y, 3, 4, 1, 1)

        self.t_c_orien_y = QLabel(self.frame_4)
        self.t_c_orien_y.setObjectName(u"t_c_orien_y")
        self.t_c_orien_y.setMinimumSize(QSize(0, 30))
        self.t_c_orien_y.setMaximumSize(QSize(16777215, 35))
        self.t_c_orien_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_orien_y, 3, 2, 1, 1)

        self.C_accz_bar = QProgressBar(self.frame_4)
        self.C_accz_bar.setObjectName(u"C_accz_bar")
        self.C_accz_bar.setMinimumSize(QSize(0, 30))
        self.C_accz_bar.setMaximumSize(QSize(100, 35))
        self.C_accz_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(233, 151, 54);\n"
"}")
        self.C_accz_bar.setMinimum(-100)
        self.C_accz_bar.setValue(0)
        self.C_accz_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_accz_bar, 4, 1, 1, 1)

        self.R_orix_bar = QProgressBar(self.frame_4)
        self.R_orix_bar.setObjectName(u"R_orix_bar")
        self.R_orix_bar.setMinimumSize(QSize(0, 30))
        self.R_orix_bar.setMaximumSize(QSize(100, 35))
        self.R_orix_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(212, 223, 228);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 118, 242);\n"
"}")
        self.R_orix_bar.setMinimum(-100)
        self.R_orix_bar.setValue(0)
        self.R_orix_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_orix_bar, 2, 7, 1, 1)

        self.t_c_acc_y = QLabel(self.frame_4)
        self.t_c_acc_y.setObjectName(u"t_c_acc_y")
        self.t_c_acc_y.setMinimumSize(QSize(0, 30))
        self.t_c_acc_y.setMaximumSize(QSize(16777215, 35))
        self.t_c_acc_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_acc_y, 3, 0, 1, 1)

        self.t_r_orien_x = QLabel(self.frame_4)
        self.t_r_orien_x.setObjectName(u"t_r_orien_x")
        self.t_r_orien_x.setMinimumSize(QSize(0, 30))
        self.t_r_orien_x.setMaximumSize(QSize(16777215, 35))
        self.t_r_orien_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_orien_x, 2, 6, 1, 1)

        self.t_r_acc_x = QLabel(self.frame_4)
        self.t_r_acc_x.setObjectName(u"t_r_acc_x")
        self.t_r_acc_x.setMinimumSize(QSize(0, 30))
        self.t_r_acc_x.setMaximumSize(QSize(16777215, 35))
        self.t_r_acc_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_acc_x, 2, 4, 1, 1)

        self.t_c_orien_x = QLabel(self.frame_4)
        self.t_c_orien_x.setObjectName(u"t_c_orien_x")
        self.t_c_orien_x.setMinimumSize(QSize(0, 30))
        self.t_c_orien_x.setMaximumSize(QSize(16777215, 35))
        self.t_c_orien_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_orien_x, 2, 2, 1, 1)

        self.R_accx_bar = QProgressBar(self.frame_4)
        self.R_accx_bar.setObjectName(u"R_accx_bar")
        self.R_accx_bar.setMinimumSize(QSize(0, 30))
        self.R_accx_bar.setMaximumSize(QSize(100, 35))
        self.R_accx_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(212, 223, 228);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 118, 242);\n"
"}")
        self.R_accx_bar.setMinimum(-100)
        self.R_accx_bar.setValue(0)
        self.R_accx_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_accx_bar, 2, 5, 1, 1)

        self.R_accy_bar = QProgressBar(self.frame_4)
        self.R_accy_bar.setObjectName(u"R_accy_bar")
        self.R_accy_bar.setMinimumSize(QSize(0, 30))
        self.R_accy_bar.setMaximumSize(QSize(100, 35))
        self.R_accy_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(231, 76, 60);\n"
"}")
        self.R_accy_bar.setMinimum(-100)
        self.R_accy_bar.setValue(0)
        self.R_accy_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_accy_bar, 3, 5, 1, 1)

        self.R_oriy_bar = QProgressBar(self.frame_4)
        self.R_oriy_bar.setObjectName(u"R_oriy_bar")
        self.R_oriy_bar.setMinimumSize(QSize(0, 30))
        self.R_oriy_bar.setMaximumSize(QSize(100, 35))
        self.R_oriy_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(231, 76, 60);\n"
"}")
        self.R_oriy_bar.setMinimum(-100)
        self.R_oriy_bar.setValue(0)
        self.R_oriy_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_oriy_bar, 3, 7, 1, 1)

        self.R_accz_bar = QProgressBar(self.frame_4)
        self.R_accz_bar.setObjectName(u"R_accz_bar")
        self.R_accz_bar.setMinimumSize(QSize(0, 30))
        self.R_accz_bar.setMaximumSize(QSize(100, 35))
        self.R_accz_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(233, 151, 54);\n"
"}")
        self.R_accz_bar.setMinimum(-100)
        self.R_accz_bar.setValue(0)
        self.R_accz_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_accz_bar, 4, 5, 1, 1)

        self.C_orix_bar = QProgressBar(self.frame_4)
        self.C_orix_bar.setObjectName(u"C_orix_bar")
        self.C_orix_bar.setMinimumSize(QSize(0, 30))
        self.C_orix_bar.setMaximumSize(QSize(100, 35))
        self.C_orix_bar.setSizeIncrement(QSize(0, 0))
        self.C_orix_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(212, 223, 228);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 118, 242);\n"
"}")
        self.C_orix_bar.setMinimum(-100)
        self.C_orix_bar.setValue(0)
        self.C_orix_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_orix_bar, 2, 3, 1, 1)

        self.t_r_acc_z = QLabel(self.frame_4)
        self.t_r_acc_z.setObjectName(u"t_r_acc_z")
        self.t_r_acc_z.setMinimumSize(QSize(0, 30))
        self.t_r_acc_z.setMaximumSize(QSize(16777215, 35))
        self.t_r_acc_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_acc_z, 4, 4, 1, 1)

        self.C_oriy_bar = QProgressBar(self.frame_4)
        self.C_oriy_bar.setObjectName(u"C_oriy_bar")
        self.C_oriy_bar.setMinimumSize(QSize(0, 30))
        self.C_oriy_bar.setMaximumSize(QSize(100, 35))
        self.C_oriy_bar.setSizeIncrement(QSize(0, 0))
        self.C_oriy_bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(231, 76, 60);\n"
"}")
        self.C_oriy_bar.setMinimum(-100)
        self.C_oriy_bar.setValue(0)
        self.C_oriy_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_oriy_bar, 3, 3, 1, 1)

        self.t_r_orien_y = QLabel(self.frame_4)
        self.t_r_orien_y.setObjectName(u"t_r_orien_y")
        self.t_r_orien_y.setMinimumSize(QSize(0, 30))
        self.t_r_orien_y.setMaximumSize(QSize(16777215, 35))
        self.t_r_orien_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_orien_y, 3, 6, 1, 1)

        self.t_c_lat = QLabel(self.frame_4)
        self.t_c_lat.setObjectName(u"t_c_lat")
        self.t_c_lat.setMinimumSize(QSize(100, 30))
        self.t_c_lat.setMaximumSize(QSize(100, 30))
        self.t_c_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_lat, 5, 0, 1, 1)

        self.C_lat = QLabel(self.frame_4)
        self.C_lat.setObjectName(u"C_lat")
        self.C_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_lat, 5, 1, 1, 1)

        self.R_lat = QLabel(self.frame_4)
        self.R_lat.setObjectName(u"R_lat")
        self.R_lat.setMinimumSize(QSize(100, 30))
        self.R_lat.setMaximumSize(QSize(100, 30))
        self.R_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_lat, 5, 5, 1, 1)

        self.t_r_lat = QLabel(self.frame_4)
        self.t_r_lat.setObjectName(u"t_r_lat")
        self.t_r_lat.setMinimumSize(QSize(100, 30))
        self.t_r_lat.setMaximumSize(QSize(100, 30))
        self.t_r_lat.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_lat, 5, 4, 1, 1)

        self.t_c_long = QLabel(self.frame_4)
        self.t_c_long.setObjectName(u"t_c_long")
        self.t_c_long.setMinimumSize(QSize(100, 30))
        self.t_c_long.setMaximumSize(QSize(100, 30))
        self.t_c_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_c_long, 5, 2, 1, 1)

        self.C_long = QLabel(self.frame_4)
        self.C_long.setObjectName(u"C_long")
        self.C_long.setMinimumSize(QSize(100, 30))
        self.C_long.setMaximumSize(QSize(100, 30))
        self.C_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.C_long, 5, 3, 1, 1)

        self.t_r_long = QLabel(self.frame_4)
        self.t_r_long.setObjectName(u"t_r_long")
        self.t_r_long.setMinimumSize(QSize(100, 30))
        self.t_r_long.setMaximumSize(QSize(100, 30))
        self.t_r_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.t_r_long, 5, 6, 1, 1)

        self.R_long = QLabel(self.frame_4)
        self.R_long.setObjectName(u"R_long")
        self.R_long.setMinimumSize(QSize(100, 30))
        self.R_long.setMaximumSize(QSize(100, 30))
        self.R_long.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.R_long, 5, 7, 1, 1)

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


        self.gridLayout_2.addWidget(self.frame_4, 12, 0, 1, 10)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 30))
        self.label_5.setMaximumSize(QSize(150, 30))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 3, 6, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 30))
        self.label_7.setMaximumSize(QSize(150, 30))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 10, 6, 1, 1)

        self.graphicsView = QChartView(self.frame_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(350, 200))
        self.graphicsView.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.graphicsView, 0, 6, 3, 2)

        self.t_c_humidity = QLabel(self.frame_2)
        self.t_c_humidity.setObjectName(u"t_c_humidity")
        self.t_c_humidity.setMinimumSize(QSize(150, 30))
        self.t_c_humidity.setMaximumSize(QSize(150, 16777215))
        self.t_c_humidity.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_humidity, 3, 8, 1, 1)

        self.t_c_temp = QLabel(self.frame_2)
        self.t_c_temp.setObjectName(u"t_c_temp")
        self.t_c_temp.setMinimumSize(QSize(150, 30))
        self.t_c_temp.setMaximumSize(QSize(150, 30))
        self.t_c_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_temp, 3, 4, 1, 1)

        self.R_batt_Bar = QProgressBar(self.frame_2)
        self.R_batt_Bar.setObjectName(u"R_batt_Bar")
        self.R_batt_Bar.setMinimumSize(QSize(0, 30))
        self.R_batt_Bar.setMaximumSize(QSize(100, 16777215))
        self.R_batt_Bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(56, 122, 71);\n"
"}")
        self.R_batt_Bar.setValue(100)
        self.R_batt_Bar.setAlignment(Qt.AlignCenter)
        self.R_batt_Bar.setTextVisible(True)
        self.R_batt_Bar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.R_batt_Bar, 10, 1, 1, 1)

        self.R_temp = QLabel(self.frame_2)
        self.R_temp.setObjectName(u"R_temp")
        self.R_temp.setMinimumSize(QSize(150, 30))
        self.R_temp.setMaximumSize(QSize(150, 16777215))
        self.R_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_temp, 10, 5, 1, 1)

        self.C_alt_graph = QChartView(self.frame_2)
        self.C_alt_graph.setObjectName(u"C_alt_graph")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_alt_graph.sizePolicy().hasHeightForWidth())
        self.C_alt_graph.setSizePolicy(sizePolicy)
        self.C_alt_graph.setMinimumSize(QSize(350, 200))
        self.C_alt_graph.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.C_alt_graph, 0, 2, 3, 2)

        self.t_c_batt = QLabel(self.frame_2)
        self.t_c_batt.setObjectName(u"t_c_batt")
        self.t_c_batt.setMinimumSize(QSize(0, 0))
        self.t_c_batt.setMaximumSize(QSize(16777215, 16777215))
        self.t_c_batt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_batt, 3, 0, 1, 1)

        self.t_r_batt = QLabel(self.frame_2)
        self.t_r_batt.setObjectName(u"t_r_batt")
        self.t_r_batt.setMinimumSize(QSize(0, 0))
        self.t_r_batt.setMaximumSize(QSize(16777215, 16777215))
        self.t_r_batt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_batt, 10, 0, 1, 1)

        self.C_batt_Bar = QProgressBar(self.frame_2)
        self.C_batt_Bar.setObjectName(u"C_batt_Bar")
        self.C_batt_Bar.setMinimumSize(QSize(0, 30))
        self.C_batt_Bar.setMaximumSize(QSize(100, 16777215))
        self.C_batt_Bar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(43, 59, 77);\n"
"	color: rgb(210, 222, 226);\n"
"	border-style: none;	\n"
"	border-radius: 5px;\n"
"	text-alignL center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(56, 122, 71);\n"
"}")
        self.C_batt_Bar.setValue(100)
        self.C_batt_Bar.setAlignment(Qt.AlignCenter)
        self.C_batt_Bar.setTextVisible(True)

        self.gridLayout_2.addWidget(self.C_batt_Bar, 3, 1, 1, 1)

        self.C_temp = QLabel(self.frame_2)
        self.C_temp.setObjectName(u"C_temp")
        self.C_temp.setMinimumSize(QSize(150, 30))
        self.C_temp.setMaximumSize(QSize(150, 16777215))
        self.C_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_temp, 3, 5, 1, 1)

        self.t_rocket_1 = QLabel(self.frame_2)
        self.t_rocket_1.setObjectName(u"t_rocket_1")
        self.t_rocket_1.setMinimumSize(QSize(200, 50))
        self.t_rocket_1.setMaximumSize(QSize(16777215, 60))
        self.t_rocket_1.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"alternate-background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 10px;\n"
"")
        self.t_rocket_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_rocket_1, 4, 0, 1, 2)

        self.R_alt_graph = QChartView(self.frame_2)
        self.R_alt_graph.setObjectName(u"R_alt_graph")
        sizePolicy.setHeightForWidth(self.R_alt_graph.sizePolicy().hasHeightForWidth())
        self.R_alt_graph.setSizePolicy(sizePolicy)
        self.R_alt_graph.setMinimumSize(QSize(350, 200))
        self.R_alt_graph.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.R_alt_graph, 4, 2, 4, 2)

        self.R_alt = QLabel(self.frame_2)
        self.R_alt.setObjectName(u"R_alt")
        self.R_alt.setMinimumSize(QSize(150, 30))
        self.R_alt.setMaximumSize(QSize(150, 30))
        self.R_alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_alt, 10, 3, 1, 1)

        self.t_apogee = QLabel(self.frame_2)
        self.t_apogee.setObjectName(u"t_apogee")
        self.t_apogee.setMinimumSize(QSize(100, 30))
        self.t_apogee.setMaximumSize(QSize(100, 60))
        self.t_apogee.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_apogee, 6, 0, 1, 1)

        self.C_alt = QLabel(self.frame_2)
        self.C_alt.setObjectName(u"C_alt")
        self.C_alt.setMinimumSize(QSize(150, 30))
        self.C_alt.setMaximumSize(QSize(150, 30))
        self.C_alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_alt, 3, 3, 1, 1)

        self.t_r_alt = QLabel(self.frame_2)
        self.t_r_alt.setObjectName(u"t_r_alt")
        self.t_r_alt.setMinimumSize(QSize(150, 30))
        self.t_r_alt.setMaximumSize(QSize(150, 30))
        self.t_r_alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_alt, 10, 2, 1, 1)

        self.C_temp_graph = QChartView(self.frame_2)
        self.C_temp_graph.setObjectName(u"C_temp_graph")
        sizePolicy.setHeightForWidth(self.C_temp_graph.sizePolicy().hasHeightForWidth())
        self.C_temp_graph.setSizePolicy(sizePolicy)
        self.C_temp_graph.setMinimumSize(QSize(350, 200))
        self.C_temp_graph.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.C_temp_graph, 0, 4, 3, 2)

        self.t_c_alt = QLabel(self.frame_2)
        self.t_c_alt.setObjectName(u"t_c_alt")
        self.t_c_alt.setMinimumSize(QSize(150, 30))
        self.t_c_alt.setMaximumSize(QSize(150, 30))
        self.t_c_alt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_alt, 3, 2, 1, 1)

        self.t_r_temp = QLabel(self.frame_2)
        self.t_r_temp.setObjectName(u"t_r_temp")
        self.t_r_temp.setMinimumSize(QSize(150, 30))
        self.t_r_temp.setMaximumSize(QSize(150, 30))
        self.t_r_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_temp, 10, 4, 1, 1)

        self.t_r_pkg = QLabel(self.frame_2)
        self.t_r_pkg.setObjectName(u"t_r_pkg")
        self.t_r_pkg.setMinimumSize(QSize(100, 30))
        self.t_r_pkg.setMaximumSize(QSize(100, 60))
        self.t_r_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_pkg, 5, 0, 1, 1)

        self.C_pkg = QLabel(self.frame_2)
        self.C_pkg.setObjectName(u"C_pkg")
        self.C_pkg.setMinimumSize(QSize(100, 30))
        self.C_pkg.setMaximumSize(QSize(100, 60))
        self.C_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_pkg, 1, 1, 1, 1)

        self.C_humidity = QLabel(self.frame_2)
        self.C_humidity.setObjectName(u"C_humidity")
        self.C_humidity.setMinimumSize(QSize(150, 30))
        self.C_humidity.setMaximumSize(QSize(150, 16777215))
        self.C_humidity.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_humidity, 3, 9, 1, 1)

        self.C_humid_graph = QChartView(self.frame_2)
        self.C_humid_graph.setObjectName(u"C_humid_graph")
        sizePolicy.setHeightForWidth(self.C_humid_graph.sizePolicy().hasHeightForWidth())
        self.C_humid_graph.setSizePolicy(sizePolicy)
        self.C_humid_graph.setMinimumSize(QSize(350, 200))
        self.C_humid_graph.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.C_humid_graph, 0, 8, 3, 2)

        self.apogee = QLabel(self.frame_2)
        self.apogee.setObjectName(u"apogee")
        self.apogee.setMinimumSize(QSize(100, 30))
        self.apogee.setMaximumSize(QSize(100, 60))
        self.apogee.setStyleSheet(u"color: rgb(242, 48, 106);")
        self.apogee.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.apogee, 6, 1, 1, 1)

        self.t_r_on = QLabel(self.frame_2)
        self.t_r_on.setObjectName(u"t_r_on")
        self.t_r_on.setMinimumSize(QSize(100, 30))
        self.t_r_on.setMaximumSize(QSize(100, 60))
        self.t_r_on.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_r_on, 7, 0, 1, 1)

        self.R_pkg = QLabel(self.frame_2)
        self.R_pkg.setObjectName(u"R_pkg")
        self.R_pkg.setMinimumSize(QSize(100, 30))
        self.R_pkg.setMaximumSize(QSize(100, 60))
        self.R_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_pkg, 5, 1, 1, 1)

        self.R_on = QLabel(self.frame_2)
        self.R_on.setObjectName(u"R_on")
        self.R_on.setMinimumSize(QSize(100, 30))
        self.R_on.setMaximumSize(QSize(100, 60))
        self.R_on.setStyleSheet(u"color: rgb(67, 231, 163);")
        self.R_on.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_on, 7, 1, 1, 1)

        self.t_operation = QLabel(self.frame_2)
        self.t_operation.setObjectName(u"t_operation")
        self.t_operation.setMinimumSize(QSize(100, 30))
        self.t_operation.setMaximumSize(QSize(100, 60))
        self.t_operation.setStyleSheet(u"")
        self.t_operation.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_operation, 1, 0, 1, 1)

        self.C_on = QLabel(self.frame_2)
        self.C_on.setObjectName(u"C_on")
        self.C_on.setMinimumSize(QSize(100, 30))
        self.C_on.setMaximumSize(QSize(100, 60))
        self.C_on.setStyleSheet(u"color: rgb(67, 231, 163);")
        self.C_on.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_on, 2, 1, 1, 1)

        self.t_c_pkg = QLabel(self.frame_2)
        self.t_c_pkg.setObjectName(u"t_c_pkg")
        self.t_c_pkg.setMinimumSize(QSize(100, 30))
        self.t_c_pkg.setMaximumSize(QSize(100, 60))
        self.t_c_pkg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_c_pkg, 2, 0, 1, 1)

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

        self.gridLayout_2.addWidget(self.t_container_1, 0, 0, 1, 2)

        self.C_velo = QLabel(self.frame_2)
        self.C_velo.setObjectName(u"C_velo")
        self.C_velo.setMinimumSize(QSize(150, 30))
        self.C_velo.setMaximumSize(QSize(150, 30))
        self.C_velo.setStyleSheet(u"color: rgb(242, 48, 106);")
        self.C_velo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.C_velo, 3, 7, 1, 1)

        self.t_az = QLabel(self.frame_2)
        self.t_az.setObjectName(u"t_az")
        self.t_az.setMinimumSize(QSize(100, 30))
        self.t_az.setMaximumSize(QSize(100, 30))
        self.t_az.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_az, 14, 2, 1, 1)

        self.Azimuth = QLabel(self.frame_2)
        self.Azimuth.setObjectName(u"Azimuth")
        self.Azimuth.setMinimumSize(QSize(100, 30))
        self.Azimuth.setMaximumSize(QSize(100, 30))
        self.Azimuth.setCursor(QCursor(Qt.ArrowCursor))
        self.Azimuth.setStyleSheet(u"color: rgb(242, 48, 106);")
        self.Azimuth.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Azimuth, 14, 3, 1, 1)

        self.R_temp_graph = QChartView(self.frame_2)
        self.R_temp_graph.setObjectName(u"R_temp_graph")
        sizePolicy.setHeightForWidth(self.R_temp_graph.sizePolicy().hasHeightForWidth())
        self.R_temp_graph.setSizePolicy(sizePolicy)
        self.R_temp_graph.setMinimumSize(QSize(350, 200))
        self.R_temp_graph.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.R_temp_graph, 4, 4, 4, 2)

        self.graphicsView_2 = QChartView(self.frame_2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setMinimumSize(QSize(350, 200))
        self.graphicsView_2.setMaximumSize(QSize(350, 200))

        self.gridLayout_2.addWidget(self.graphicsView_2, 4, 6, 4, 2)

        self.Sight = QLabel(self.frame_2)
        self.Sight.setObjectName(u"Sight")
        self.Sight.setMinimumSize(QSize(100, 30))
        self.Sight.setMaximumSize(QSize(100, 30))
        self.Sight.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Sight, 14, 7, 1, 1)

        self.Elevation = QLabel(self.frame_2)
        self.Elevation.setObjectName(u"Elevation")
        self.Elevation.setMinimumSize(QSize(100, 30))
        self.Elevation.setMaximumSize(QSize(100, 30))
        self.Elevation.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Elevation, 14, 5, 1, 1)

        self.t_sight = QLabel(self.frame_2)
        self.t_sight.setObjectName(u"t_sight")
        self.t_sight.setMinimumSize(QSize(100, 30))
        self.t_sight.setMaximumSize(QSize(100, 30))
        self.t_sight.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_sight, 14, 6, 1, 1)

        self.t_ele = QLabel(self.frame_2)
        self.t_ele.setObjectName(u"t_ele")
        self.t_ele.setMinimumSize(QSize(100, 30))
        self.t_ele.setMaximumSize(QSize(100, 30))
        self.t_ele.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.t_ele, 14, 4, 1, 1)

        self.R_velo = QLabel(self.frame_2)
        self.R_velo.setObjectName(u"R_velo")
        self.R_velo.setMinimumSize(QSize(150, 30))
        self.R_velo.setMaximumSize(QSize(150, 30))
        self.R_velo.setStyleSheet(u"color: rgb(242, 48, 106);")
        self.R_velo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.R_velo, 10, 7, 1, 1)

        self.frame5 = QFrame(self.frame_2)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setFrameShape(QFrame.StyledPanel)
        self.frame5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.PM10 = QLabel(self.frame5)
        self.PM10.setObjectName(u"PM10")
        self.PM10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.PM10, 1, 1, 1, 1)

        self.PM25 = QLabel(self.frame5)
        self.PM25.setObjectName(u"PM25")
        self.PM25.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.PM25, 2, 1, 1, 1)

        self.t_pm25 = QLabel(self.frame5)
        self.t_pm25.setObjectName(u"t_pm25")
        self.t_pm25.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_pm25, 2, 0, 1, 1)

        self.t_pm10 = QLabel(self.frame5)
        self.t_pm10.setObjectName(u"t_pm10")
        self.t_pm10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_pm10, 1, 0, 1, 1)

        self.t_parti = QLabel(self.frame5)
        self.t_parti.setObjectName(u"t_parti")
        self.t_parti.setMinimumSize(QSize(100, 30))
        self.t_parti.setFont(font1)
        self.t_parti.setStyleSheet(u"font: 800 24pt \"Apple SD Gothic Neo\";\n"
"alternate-background-color: rgba(255, 255, 255, 100);\n"
"border-radius: 10px;\n"
"")
        self.t_parti.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_parti, 0, 0, 1, 2)

        self.t_aqi = QLabel(self.frame5)
        self.t_aqi.setObjectName(u"t_aqi")
        self.t_aqi.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.t_aqi, 3, 0, 1, 1)

        self.AQI = QLabel(self.frame5)
        self.AQI.setObjectName(u"AQI")
        self.AQI.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.AQI, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame5, 4, 8, 4, 2)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)


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
        GrounStation.setWindowTitle(QCoreApplication.translate("GrounStation", u"MainWindow", None))
        self.t_teamname.setText(QCoreApplication.translate("GrounStation", u"ALIEN SAT", None))
        self.btn_minimize.setText("")
        self.btn_restore.setText("")
        self.btn_close.setText("")
        self.t_elapsed.setText(QCoreApplication.translate("GrounStation", u"ELAPSED :", None))
        self.btn_r_off.setText(QCoreApplication.translate("GrounStation", u"OFF", None))
        self.Time.setText(QCoreApplication.translate("GrounStation", u"HH:MM:SS.MS", None))
        self.t_time.setText(QCoreApplication.translate("GrounStation", u"TIME :", None))
        self.btn_c_off.setText(QCoreApplication.translate("GrounStation", u"OFF", None))
        self.Elapsed.setText(QCoreApplication.translate("GrounStation", u"HH:MM:SS.MS", None))
        self.btn_clear.setText(QCoreApplication.translate("GrounStation", u"Clear", None))
        self.btn_connect.setText(QCoreApplication.translate("GrounStation", u"Connect", None))
        self.btn_refresh.setText(QCoreApplication.translate("GrounStation", u"Refresh", None))
        self.t_container.setText(QCoreApplication.translate("GrounStation", u"CANSAT", None))
        self.btn_r_on.setText(QCoreApplication.translate("GrounStation", u"ON", None))
        self.btn_c_on.setText(QCoreApplication.translate("GrounStation", u"ON", None))
        self.t_rocket.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.portlist.setItemText(0, QCoreApplication.translate("GrounStation", u"COM11", None))

        self.t_gd.setText(QCoreApplication.translate("GrounStation", u"Ground Distance", None))
        self.GD.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.GD.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.C_oriz_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_c_acc_z.setText(QCoreApplication.translate("GrounStation", u"ACC z", None))
        self.C_accy_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.C_accx_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_c_orien_z.setText(QCoreApplication.translate("GrounStation", u"ORIEN z", None))
        self.t_c_acc_x.setText(QCoreApplication.translate("GrounStation", u"ACC x", None))
        self.R_oriz_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_r_orien_z.setText(QCoreApplication.translate("GrounStation", u"ORIEN z", None))
        self.t_mui.setText(QCoreApplication.translate("GrounStation", u"GNSS & IMU", None))
        self.t_r_acc_y.setText(QCoreApplication.translate("GrounStation", u"ACC y", None))
        self.t_c_orien_y.setText(QCoreApplication.translate("GrounStation", u"ORIEN y", None))
        self.C_accz_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.R_orix_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_c_acc_y.setText(QCoreApplication.translate("GrounStation", u"ACC y", None))
        self.t_r_orien_x.setText(QCoreApplication.translate("GrounStation", u"ORIEN x", None))
        self.t_r_acc_x.setText(QCoreApplication.translate("GrounStation", u"ACC x", None))
        self.t_c_orien_x.setText(QCoreApplication.translate("GrounStation", u"ORIEN x", None))
        self.R_accx_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.R_accy_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.R_oriy_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.R_accz_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.C_orix_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_r_acc_z.setText(QCoreApplication.translate("GrounStation", u"ACC z", None))
        self.C_oriy_bar.setFormat(QCoreApplication.translate("GrounStation", u"%v", None))
        self.t_r_orien_y.setText(QCoreApplication.translate("GrounStation", u"ORIEN y", None))
        self.t_c_lat.setText(QCoreApplication.translate("GrounStation", u" Latitude", None))
        self.C_lat.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_lat.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.R_lat.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.R_lat.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_lat.setText(QCoreApplication.translate("GrounStation", u"Latitude", None))
        self.t_c_long.setText(QCoreApplication.translate("GrounStation", u"Longitude", None))
        self.C_long.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_long.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_long.setText(QCoreApplication.translate("GrounStation", u"Longitude", None))
        self.R_long.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.R_long.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_rocket_2.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.t_container_2.setText(QCoreApplication.translate("GrounStation", u"CONTAINER", None))
        self.label_5.setText(QCoreApplication.translate("GrounStation", u"Velocity", None))
        self.label_7.setText(QCoreApplication.translate("GrounStation", u"Velocity", None))
        self.t_c_humidity.setText(QCoreApplication.translate("GrounStation", u"Humidity", None))
        self.t_c_temp.setText(QCoreApplication.translate("GrounStation", u"Temperature", None))
        self.R_batt_Bar.setFormat(QCoreApplication.translate("GrounStation", u"%p", None))
        self.R_temp.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.R_temp.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_c_batt.setText(QCoreApplication.translate("GrounStation", u"Battery", None))
        self.t_r_batt.setText(QCoreApplication.translate("GrounStation", u"Battery", None))
        self.C_batt_Bar.setFormat(QCoreApplication.translate("GrounStation", u"%p", None))
        self.C_temp.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_temp.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_rocket_1.setText(QCoreApplication.translate("GrounStation", u"ROCKET", None))
        self.R_alt.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.R_alt.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_apogee.setText(QCoreApplication.translate("GrounStation", u"PEAK :", None))
        self.C_alt.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_alt.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_alt.setText(QCoreApplication.translate("GrounStation", u"Altitude", None))
        self.t_c_alt.setText(QCoreApplication.translate("GrounStation", u"Altitude", None))
        self.t_r_temp.setText(QCoreApplication.translate("GrounStation", u"Temperature", None))
        self.t_r_pkg.setText(QCoreApplication.translate("GrounStation", u"PKG :", None))
        self.C_pkg.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_pkg.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.C_humidity.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.C_humidity.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.apogee.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_r_on.setText(QCoreApplication.translate("GrounStation", u"OPR : ", None))
        self.R_pkg.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.R_pkg.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.R_on.setText(QCoreApplication.translate("GrounStation", u"NO", None))
        self.t_operation.setText(QCoreApplication.translate("GrounStation", u"PKG :", None))
        self.C_on.setText(QCoreApplication.translate("GrounStation", u"NO", None))
        self.t_c_pkg.setText(QCoreApplication.translate("GrounStation", u"OPR : ", None))
        self.t_container_1.setText(QCoreApplication.translate("GrounStation", u"CANSAT", None))
        self.C_velo.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_az.setText(QCoreApplication.translate("GrounStation", u"Azimuth", None))
        self.Azimuth.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.Sight.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.Sight.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.Elevation.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.Elevation.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_sight.setText(QCoreApplication.translate("GrounStation", u"Sight", None))
        self.t_ele.setText(QCoreApplication.translate("GrounStation", u"Elevation", None))
        self.R_velo.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.PM10.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.PM10.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.PM25.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.PM25.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.t_pm25.setText(QCoreApplication.translate("GrounStation", u"PM 2.5", None))
        self.t_pm10.setText(QCoreApplication.translate("GrounStation", u"PM 10", None))
        self.t_parti.setText(QCoreApplication.translate("GrounStation", u"DUST PARTICLE", None))
        self.t_aqi.setText(QCoreApplication.translate("GrounStation", u"AQI", None))
        self.AQI.setStyleSheet(QCoreApplication.translate("GrounStation", u"color: rgb(242, 48, 106);", None))
        self.AQI.setText(QCoreApplication.translate("GrounStation", u"0", None))
        self.copyright.setText(QCoreApplication.translate("GrounStation", u"Ground station for Alien sat by space AC for Thailand CanSat competition V0.3", None))
    # retranslateUi

