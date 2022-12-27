# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/BATUHAN/Desktop/question_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Question(object):
    def setupUi(self, Question):
        Question.setObjectName("Question")
        Question.resize(1134, 762)
        Question.setStyleSheet("border-image: url(:/icons/question.png);")
        self.centralwidget = QtWidgets.QWidget(Question)
        self.centralwidget.setObjectName("centralwidget")
        Question.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Question)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 26))
        self.menubar.setObjectName("menubar")
        Question.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Question)
        self.statusbar.setObjectName("statusbar")
        Question.setStatusBar(self.statusbar)

        self.retranslateUi(Question)
        QtCore.QMetaObject.connectSlotsByName(Question)

    def retranslateUi(self, Question):
        _translate = QtCore.QCoreApplication.translate
        Question.setWindowTitle(_translate("Question", "Question"))

import icons_rc
