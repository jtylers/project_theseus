# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_graphics.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keypad = QtWidgets.QWidget(self.centralwidget)
        self.keypad.setGeometry(QtCore.QRect(30, 80, 361, 131))
        self.keypad.setObjectName("keypad")
        self.gridLayoutWidget = QtWidgets.QWidget(self.keypad)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 340, 112))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 1, 3, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout.addWidget(self.pushButton0, 0, 0, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout.addWidget(self.pushButton8, 2, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 2, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 0, 3, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout.addWidget(self.pushButton9, 2, 1, 1, 1)
        self.pushButtona = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtona.setObjectName("pushButtona")
        self.gridLayout.addWidget(self.pushButtona, 2, 2, 1, 1)
        self.pushButtonb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonb.setObjectName("pushButtonb")
        self.gridLayout.addWidget(self.pushButtonb, 2, 3, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 1, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButtonc = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonc.setObjectName("pushButtonc")
        self.gridLayout.addWidget(self.pushButtonc, 3, 0, 1, 1)
        self.pushButtond = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtond.setObjectName("pushButtond")
        self.gridLayout.addWidget(self.pushButtond, 3, 1, 1, 1)
        self.pushButtone = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtone.setObjectName("pushButtone")
        self.gridLayout.addWidget(self.pushButtone, 3, 2, 1, 1)
        self.pushButtonf = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonf.setObjectName("pushButtonf")
        self.gridLayout.addWidget(self.pushButtonf, 3, 3, 1, 1)
        self.puzzle = QtWidgets.QWidget(self.centralwidget)
        self.puzzle.setGeometry(QtCore.QRect(40, 270, 201, 91))
        self.puzzle.setObjectName("puzzle")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.puzzle)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 181, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_1 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_1.setMaximum(1)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.horizontalLayout.addWidget(self.verticalSlider_1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_2.setMaximum(1)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_3.setMaximum(1)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_4 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_4.setMaximum(1)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout.addWidget(self.verticalSlider_4)
        self.verticalSlider_5 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_5.setMaximum(1)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout.addWidget(self.verticalSlider_5)
        self.dial = QtWidgets.QDial(self.horizontalLayoutWidget)
        self.dial.setMaximum(4)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.lid_display = QtWidgets.QWidget(self.centralwidget)
        self.lid_display.setGeometry(QtCore.QRect(30, 30, 241, 31))
        self.lid_display.setObjectName("lid_display")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.lid_display)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcdMinutes = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.lcdMinutes.setAutoFillBackground(False)
        self.lcdMinutes.setSmallDecimalPoint(True)
        self.lcdMinutes.setDigitCount(1)
        self.lcdMinutes.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMinutes.setProperty("value", 3.0)
        self.lcdMinutes.setProperty("intValue", 3)
        self.lcdMinutes.setObjectName("lcdMinutes")
        self.horizontalLayout_2.addWidget(self.lcdMinutes)
        self.lcdSeconds = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.lcdSeconds.setDigitCount(2)
        self.lcdSeconds.setObjectName("lcdSeconds")
        self.horizontalLayout_2.addWidget(self.lcdSeconds)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.RGB = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.RGB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RGB.setText("")
        self.RGB.setObjectName("RGB")
        self.horizontalLayout_2.addWidget(self.RGB)
        self.LEDs = QtWidgets.QWidget(self.centralwidget)
        self.LEDs.setGeometry(QtCore.QRect(40, 210, 251, 51))
        self.LEDs.setObjectName("LEDs")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.LEDs)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 241, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LED_0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_0.setText("")
        self.LED_0.setObjectName("LED_0")
        self.horizontalLayout_3.addWidget(self.LED_0)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.LED_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_1.setText("")
        self.LED_1.setObjectName("LED_1")
        self.horizontalLayout_3.addWidget(self.LED_1)
        self.LED_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_2.setText("")
        self.LED_2.setObjectName("LED_2")
        self.horizontalLayout_3.addWidget(self.LED_2)
        self.LED_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_3.setText("")
        self.LED_3.setObjectName("LED_3")
        self.horizontalLayout_3.addWidget(self.LED_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.LED_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_4.setText("")
        self.LED_4.setObjectName("LED_4")
        self.horizontalLayout_3.addWidget(self.LED_4)
        self.LED_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_5.setText("")
        self.LED_5.setObjectName("LED_5")
        self.horizontalLayout_3.addWidget(self.LED_5)
        self.LED_6 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_6.setText("")
        self.LED_6.setObjectName("LED_6")
        self.horizontalLayout_3.addWidget(self.LED_6)
        self.LED_7 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.LED_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LED_7.setText("")
        self.LED_7.setObjectName("LED_7")
        self.horizontalLayout_3.addWidget(self.LED_7)
        self.inner_box = QtWidgets.QWidget(self.centralwidget)
        self.inner_box.setGeometry(QtCore.QRect(40, 380, 171, 51))
        self.inner_box.setObjectName("inner_box")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.inner_box)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.WIRE_RED = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.WIRE_RED.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.WIRE_RED.setText("")
        self.WIRE_RED.setObjectName("WIRE_RED")
        self.horizontalLayout_4.addWidget(self.WIRE_RED)
        self.WIRE_GREEN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.WIRE_GREEN.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.WIRE_GREEN.setText("")
        self.WIRE_GREEN.setObjectName("WIRE_GREEN")
        self.horizontalLayout_4.addWidget(self.WIRE_GREEN)
        self.WIRE_BLUE = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.WIRE_BLUE.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.WIRE_BLUE.setText("")
        self.WIRE_BLUE.setObjectName("WIRE_BLUE")
        self.horizontalLayout_4.addWidget(self.WIRE_BLUE)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.Solenoid = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.Solenoid.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Solenoid.setText("")
        self.Solenoid.setObjectName("Solenoid")
        self.horizontalLayout_4.addWidget(self.Solenoid)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mock Box"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButtona.setText(_translate("MainWindow", "a"))
        self.pushButtonb.setText(_translate("MainWindow", "b"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButtonc.setText(_translate("MainWindow", "c"))
        self.pushButtond.setText(_translate("MainWindow", "d"))
        self.pushButtone.setText(_translate("MainWindow", "e"))
        self.pushButtonf.setText(_translate("MainWindow", "f"))

