# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/BATUHAN/Desktop/project_design_copy2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# Anasayfadaki label, push button, line edit ve bunların CSS ile tasarlanan dizaynlarını sağlayan
# ana pencerenin Qt5 ile tasarlanan Python kodları.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):                     #pencereyi oluşturan main window sınıfı.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 826)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Custom-Icon-Design-Pretty-Office-2-FAQ (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("border-radius: 70px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(:/icons/arkaplan.png);\n"
"}")
# spacer ve grid layout ile responsive tasarım oluşturma. 
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(22, 15, 17, 9)
        self.formLayout.setHorizontalSpacing(14)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
# label oluşturma 
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("border:none;\n"
"background-color: rgb(255, 198, 233);\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"")
        self.lineEdit_1.setMaxLength(10)
        self.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_4.setMaxLength(10)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_5.setMaxLength(10)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel::hover{\n"
"color:red;\n"
"\n"
"}")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border:none;\n"
"border-bottom: 2px solid gray;\n"
"color:rgb(73, 120, 120);\n"
"border-radius: 14px;\n"
"\n"
"background-color: rgb(255, 198, 233);\n"
"")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(17, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 3, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 0, 0, 1, 1)
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button.sizePolicy().hasHeightForWidth())
        self.Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button.setFont(font)
        self.Button.setStyleSheet("QPushButton{\n"
"color:pink;\n"
"    \n"
"    \n"
"    background-color: rgb(255, 240, 210);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(205, 209, 255);\n"
"color:magenta;\n"
"\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Dtafalonso-Android-Lollipop-Calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button.setIcon(icon1)
        self.Button.setIconSize(QtCore.QSize(65, 59))
        self.Button.setObjectName("Button")
        self.gridLayout.addWidget(self.Button, 3, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 3, 4, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 1, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 4, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1109, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuSorular = QtWidgets.QMenu(self.menuBar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Custom-Icon-Design-Pretty-Office-2-FAQ (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSorular.setIcon(icon2)
        self.menuSorular.setObjectName("menuSorular")
        MainWindow.setMenuBar(self.menuBar)
        self.Menubar_info = QtWidgets.QAction(MainWindow)
        self.Menubar_info.setObjectName("Menubar_info")
        self.actionQuestion = QtWidgets.QAction(MainWindow)
        self.actionQuestion.setObjectName("actionQuestion")
        self.isemler_hakkinda_2 = QtWidgets.QAction(MainWindow)
        self.isemler_hakkinda_2.setObjectName("isemler_hakkinda_2")
        self.menuSorular.addSeparator()
        self.menuSorular.addSeparator()
        self.menuSorular.addAction(self.actionQuestion)
        self.menuSorular.addAction(self.isemler_hakkinda_2)
        self.menuBar.addAction(self.menuSorular.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# labelların isimlendirilmesi 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "S :"))
        self.label_2.setText(_translate("MainWindow", "V1 :"))
        self.label_3.setText(_translate("MainWindow", "V2 :"))
        self.label_4.setText(_translate("MainWindow", "XL :"))
        self.label_5.setText(_translate("MainWindow", "XH :"))
        self.label_6.setText(_translate("MainWindow", "XM :"))
        self.label_7.setText(_translate("MainWindow", "RL :"))
        self.label_8.setText(_translate("MainWindow", "RH :"))
        self.Button.setText(_translate("MainWindow", "Calculate"))
        self.menuSorular.setTitle(_translate("MainWindow", "Sorular"))
        self.Menubar_info.setText(_translate("MainWindow", "İşlemler hakkında Bilgi"))
        self.actionQuestion.setText(_translate("MainWindow", "Question"))
        self.isemler_hakkinda_2.setText(_translate("MainWindow", "About Us2"))

import icons_rc
