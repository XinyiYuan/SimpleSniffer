# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 10, 1241, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterText = QtWidgets.QLineEdit(self.layoutWidget)
        self.filterText.setObjectName("filterText")
        self.horizontalLayout.addWidget(self.filterText)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.resetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.packetList = QtWidgets.QTableWidget(self.centralwidget)
        self.packetList.setGeometry(QtCore.QRect(12, 72, 1251, 311))
        self.packetList.setObjectName("packetList")
        self.packetList.setColumnCount(5)
        self.packetList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.packetList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetList.setHorizontalHeaderItem(4, item)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 390, 1251, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.packetOverview = QtWidgets.QTreeWidget(self.layoutWidget1)
        self.packetOverview.setObjectName("packetOverview")
        self.packetOverview.headerItem().setText(0, "Packet Overview")
        self.horizontalLayout_2.addWidget(self.packetOverview)
        self.packetContent = QtWidgets.QTextEdit(self.layoutWidget1)
        self.packetContent.setObjectName("packetContent")
        self.horizontalLayout_2.addWidget(self.packetContent)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resetButton.clicked.connect(self.packetOverview.clear)
        self.resetButton.clicked.connect(self.packetContent.clear)
        self.resetButton.clicked.connect(self.packetList.clearContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filterText.setText(_translate("MainWindow", "filter:"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        item = self.packetList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "source"))
        item = self.packetList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "destination"))
        item = self.packetList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.packetList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Length"))
        item = self.packetList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Content"))
