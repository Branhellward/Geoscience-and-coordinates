# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Area_calculate_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_area_calculate(object):
    def setupUi(self, area_calculate):
        area_calculate.setObjectName("Form")
        area_calculate.resize(400, 140)
        area_calculate.setMinimumSize(QtCore.QSize(400, 140))
        area_calculate.setMaximumSize(QtCore.QSize(400, 140))
        self.label_6 = QtWidgets.QLabel(area_calculate)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(area_calculate)
        self.pushButton_3.setGeometry(QtCore.QRect(204, 90, 181, 25))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(area_calculate)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(area_calculate)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 39, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.setDisabled(True)

        self.retranslateUi(area_calculate)
        QtCore.QMetaObject.connectSlotsByName(area_calculate)

    def retranslateUi(self, area_calculate):
        _translate = QtCore.QCoreApplication.translate
        area_calculate.setWindowTitle(_translate("Form", "Area Calculate"))
        self.label_6.setText(_translate("Form", "Area Calculate"))
        self.pushButton_3.setText(_translate("Form", "Instruction"))
        self.label_4.setText(_translate("Form", "Status"))
        self.pushButton_5.setText(_translate("Form", "Select file"))
        self.pushButton_4.setText(_translate("Form", "Calculate area"))