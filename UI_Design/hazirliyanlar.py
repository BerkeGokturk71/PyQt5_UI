# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/BATUHAN/Desktop/Hazirliyanlarui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# Qt5'te tasarlanan hazırlayanlar kısmının arayüzünün Python'a aktarılan kodları.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hazirliyan(object):
    def setupUi(self, Hazirliyan):
        Hazirliyan.setObjectName("Hazirliyan")
        Hazirliyan.setFixedSize(646, 572)
        self.centralwidget = QtWidgets.QWidget(Hazirliyan)
        self.centralwidget.setStyleSheet("background-color: rgb(211, 234, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 40, 592, 491))
        self.frame.setStyleSheet("border-radius:23px;\n"
"background-color: rgb(183, 200, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.gridLayout.addLayout(self.formLayout, 4, 0, 2, 3)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        Hazirliyan.setCentralWidget(self.centralwidget)

        self.retranslateUi(Hazirliyan)
        QtCore.QMetaObject.connectSlotsByName(Hazirliyan)

    def retranslateUi(self, Hazirliyan):
        _translate = QtCore.QCoreApplication.translate
        Hazirliyan.setWindowTitle(_translate("Hazirliyan", "About Us"))
        self.label_3.setText(_translate("Hazirliyan", "Yigit Can Argın"))
        self.label_4.setText(_translate("Hazirliyan", "Emre Can Çinal"))
        self.label_2.setText(_translate("Hazirliyan", "Batuhan Ünal"))
        self.label.setText(_translate("Hazirliyan", "Hazırlayanlar"))

