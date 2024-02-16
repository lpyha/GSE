# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.thrust_meter_view = PlotWidget(self.centralwidget)
        self.thrust_meter_view.setObjectName("thrust_meter_view")
        self.verticalLayout_3.addWidget(self.thrust_meter_view)
        self.thermometer_view = PlotWidget(self.centralwidget)
        self.thermometer_view.setObjectName("thermometer_view")
        self.verticalLayout_3.addWidget(self.thermometer_view)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thrust_label = QtWidgets.QLabel(self.centralwidget)
        self.thrust_label.setFrameShape(QtWidgets.QFrame.Box)
        self.thrust_label.setObjectName("thrust_label")
        self.verticalLayout_2.addWidget(self.thrust_label)
        self.temp_label = QtWidgets.QLabel(self.centralwidget)
        self.temp_label.setFrameShape(QtWidgets.QFrame.Box)
        self.temp_label.setObjectName("temp_label")
        self.verticalLayout_2.addWidget(self.temp_label)
        self.pressure_label = QtWidgets.QLabel(self.centralwidget)
        self.pressure_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pressure_label.setObjectName("pressure_label")
        self.verticalLayout_2.addWidget(self.pressure_label)
        self.fill_label = QtWidgets.QLabel(self.centralwidget)
        self.fill_label.setFrameShape(QtWidgets.QFrame.Box)
        self.fill_label.setObjectName("fill_label")
        self.verticalLayout_2.addWidget(self.fill_label)
        self.dump_label = QtWidgets.QLabel(self.centralwidget)
        self.dump_label.setFrameShape(QtWidgets.QFrame.Box)
        self.dump_label.setObjectName("dump_label")
        self.verticalLayout_2.addWidget(self.dump_label)
        self.ignition_label = QtWidgets.QLabel(self.centralwidget)
        self.ignition_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ignition_label.setObjectName("ignition_label")
        self.verticalLayout_2.addWidget(self.ignition_label)
        self.purge_label = QtWidgets.QLabel(self.centralwidget)
        self.purge_label.setFrameShape(QtWidgets.QFrame.Box)
        self.purge_label.setObjectName("purge_label")
        self.verticalLayout_2.addWidget(self.purge_label)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fill_radio_button = QtWidgets.QRadioButton(self.centralwidget)
        self.fill_radio_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.fill_radio_button.setFont(font)
        self.fill_radio_button.setObjectName("fill_radio_button")
        self.verticalLayout.addWidget(self.fill_radio_button)
        self.dump_radio_button = QtWidgets.QRadioButton(self.centralwidget)
        self.dump_radio_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.dump_radio_button.setFont(font)
        self.dump_radio_button.setObjectName("dump_radio_button")
        self.verticalLayout.addWidget(self.dump_radio_button)
        self.ignition_radio_button = QtWidgets.QRadioButton(self.centralwidget)
        self.ignition_radio_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.ignition_radio_button.setFont(font)
        self.ignition_radio_button.setObjectName("ignition_radio_button")
        self.verticalLayout.addWidget(self.ignition_radio_button)
        self.purge_radio_button = QtWidgets.QRadioButton(self.centralwidget)
        self.purge_radio_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.purge_radio_button.setFont(font)
        self.purge_radio_button.setObjectName("purge_radio_button")
        self.verticalLayout.addWidget(self.purge_radio_button)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.on_off_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.on_off_button.setFont(font)
        self.on_off_button.setObjectName("on_off_button")
        self.verticalLayout_4.addWidget(self.on_off_button)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.thrust_label.setText(_translate("MainWindow", "thrust: 500N"))
        self.temp_label.setText(_translate("MainWindow", "temp: 20℃"))
        self.pressure_label.setText(_translate("MainWindow", "pressure: 1kPa"))
        self.fill_label.setText(_translate("MainWindow", "FILL"))
        self.dump_label.setText(_translate("MainWindow", "DUMP"))
        self.ignition_label.setText(_translate("MainWindow", "IGNITION"))
        self.purge_label.setText(_translate("MainWindow", "PURGE"))
        self.fill_radio_button.setText(_translate("MainWindow", "FILL"))
        self.dump_radio_button.setText(_translate("MainWindow", "DUMP"))
        self.ignition_radio_button.setText(_translate("MainWindow", "IGNITION"))
        self.purge_radio_button.setText(_translate("MainWindow", "PURGE"))
        self.on_off_button.setText(_translate("MainWindow", "ON"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
