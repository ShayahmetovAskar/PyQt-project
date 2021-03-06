# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from src.styles import Styles
from src.colors import Colors
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(f"background-color: {Colors.get_color(Colors.contentFrameColor)};")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_center = QtWidgets.QFrame(self.centralwidget)
        self.frame_center.setStyleSheet(f"background-color: {Colors.get_color(Colors.contentFrameColor)};")
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_center)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_center)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.frame_center, 1, 1, 1, 1)
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_top)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_titlebar = QtWidgets.QFrame(self.frame_top)
        self.frame_titlebar.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_titlebar.setStyleSheet(f"background-color: {Colors.get_color(Colors.titleBarColor)};")
        self.frame_titlebar.setObjectName("frame_titlebar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_titlebar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addWidget(self.frame_titlebar, 0, 1, 1, 1)
        self.frame_info = QtWidgets.QFrame(self.frame_top)
        self.frame_info.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_info.setStyleSheet(f"background-color: {Colors.get_color(Colors.infoBarColor)};")
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.horizontalLayoutTopBar = QtWidgets.QHBoxLayout(self.frame_info)
        self.horizontalLayoutTopBar.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTopBar.setSpacing(0)
        self.horizontalLayoutTopBar.setObjectName("horizontalLayoutInfoBar")
        self.stackedWidgetTopBar = QtWidgets.QStackedWidget(self.frame_info)
        self.stackedWidgetTopBar.setObjectName("stackedWidgetInfoBar")
        self.horizontalLayoutTopBar.addWidget(self.stackedWidgetTopBar)
        self.gridLayout_2.addWidget(self.frame_info, 1, 1, 1, 1)
        self.frame_toggle = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMinimumSize(QtCore.QSize(70, 70))
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 70))
        self.frame_toggle.setStyleSheet("background-color: rgb(32, 34, 37);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayoutToggle = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayoutToggle.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutToggle.setSpacing(0)
        self.verticalLayoutToggle.setObjectName("verticalLayoutToggle")
        self.pushButtonToggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonToggle.sizePolicy().hasHeightForWidth())
        self.pushButtonToggle.setSizePolicy(sizePolicy)
        self.pushButtonToggle.setStyleSheet("QPushButton {\n"
                                            "    border-image: url(\"src/icons/icon_toggle.png\");\n"
                                            "    background-color: rgb(32, 34, 37);\n"
                                            "    background-position: center;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(40, 43, 46);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(43, 46, 50);\n"
                                            "}")
        self.pushButtonToggle.setText("")
        self.pushButtonToggle.setObjectName("pushButtonToggle")
        self.verticalLayoutToggle.addWidget(self.pushButtonToggle)
        self.gridLayout_2.addWidget(self.frame_toggle, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.frame_top, 0, 0, 1, 2)
        self.frame_side = QtWidgets.QFrame(self.centralwidget)
        self.frame_side.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_side.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_side.setStyleSheet(f"background-color: {Colors.get_color(Colors.sideBarColor)};")
        self.frame_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_side.setObjectName("frame_side")
        self.verticalLayout_sideBar = QtWidgets.QVBoxLayout(self.frame_side)
        self.verticalLayout_sideBar.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_sideBar.setSpacing(0)
        self.verticalLayout_sideBar.setObjectName("verticalLayout_sideBar")
        self.gridLayout.addWidget(self.frame_side, 1, 0, 2, 1)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_bottom.setStyleSheet(f"background-color: {Colors.get_color(Colors.statusBarColor)};")
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frameSizeGrip = QtWidgets.QSizeGrip(self.frame_bottom)
        self.frameSizeGrip.setStyleSheet("""QSizeGrip {
                                                image: url(src/icons/size_grip.png);
                                            }
                                            """)
        self.frameSizeGrip.setMinimumSize(QtCore.QSize(20, 20))
        self.frameSizeGrip.setMaximumSize(QtCore.QSize(20, 20))
        self.frameSizeGrip.setObjectName("frameSizeGrip")
        self.horizontalLayout_2.addWidget(self.frameSizeGrip)
        self.gridLayout.addWidget(self.frame_bottom, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
