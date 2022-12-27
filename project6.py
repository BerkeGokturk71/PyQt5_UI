# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/BATUHAN/Desktop/Second_screen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# Devre sayfasının tasarlanıp Pyhton'a aktarılan kodları.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
       
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.setFixedSize(1075, 753)
        SecondWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(:/icons/makine devre.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(550, 240, 201, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(16)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("QLabel::hover{\n"
"    color: rgb(255, 138, 80);\n"
"    \n"
"\n"
"}")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(290, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(16)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("QLabel::hover{\n"
"    color: rgb(255, 138, 80);\n"
"    \n"
"\n"
"}")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setGeometry(QtCore.QRect(490, 340, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(16)
        self.label_57.setFont(font)
        self.label_57.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_57.setStyleSheet("QLabel::hover{\n"
"    color: rgb(255, 138, 80);\n"
"    \n"
"\n"
"}")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(130, 260, 271, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(16)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("QLabel::hover{\n"
"    color: rgb(255, 138, 80);\n"
"    \n"
"\n"
"}")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(700, 230, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(16)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("QLabel::hover{\n"
"    color: rgb(255, 138, 80);\n"
"    \n"
"\n"
"}")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Answer The Question"))
        self.label_56.setText(_translate("SecondWindow", "45"))
        self.label_55.setText(_translate("SecondWindow", "45"))
        self.label_57.setText(_translate("SecondWindow", "45"))
        self.label_58.setText(_translate("SecondWindow", "45"))
        self.label_59.setText(_translate("SecondWindow", "45"))

import icons_rc
