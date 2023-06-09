# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 660)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(197, 197, 197);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(158, 158, 158);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lableCurrentExpr = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lableCurrentExpr.sizePolicy().hasHeightForWidth())
        self.lableCurrentExpr.setSizePolicy(sizePolicy)
        self.lableCurrentExpr.setStyleSheet("font-size: 16pt;\n"
"color: black;")
        self.lableCurrentExpr.setText("")
        self.lableCurrentExpr.setTextFormat(QtCore.Qt.PlainText)
        self.lableCurrentExpr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lableCurrentExpr.setObjectName("lableCurrentExpr")
        self.verticalLayout.addWidget(self.lableCurrentExpr)
        self.lineEditInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInput.sizePolicy().hasHeightForWidth())
        self.lineEditInput.setSizePolicy(sizePolicy)
        self.lineEditInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditInput.setStyleSheet("font-size: 40pt;\n"
"border: none;\n"
"\n"
"")
        self.lineEditInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInput.setObjectName("lineEditInput")
        self.verticalLayout.addWidget(self.lineEditInput)
        self.GridButton = QtWidgets.QGridLayout()
        self.GridButton.setObjectName("GridButton")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.GridButton.addWidget(self.pushButton4, 7, 0, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton9.sizePolicy().hasHeightForWidth())
        self.pushButton9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton9.setFont(font)
        self.pushButton9.setObjectName("pushButton9")
        self.GridButton.addWidget(self.pushButton9, 5, 2, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton5.sizePolicy().hasHeightForWidth())
        self.pushButton5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.GridButton.addWidget(self.pushButton5, 7, 1, 1, 1)
        self.pushButtonSqr = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSqr.sizePolicy().hasHeightForWidth())
        self.pushButtonSqr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonSqr.setFont(font)
        self.pushButtonSqr.setObjectName("pushButtonSqr")
        self.GridButton.addWidget(self.pushButtonSqr, 4, 1, 1, 1)
        self.pushButtonSqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSqrt.sizePolicy().hasHeightForWidth())
        self.pushButtonSqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonSqrt.setFont(font)
        self.pushButtonSqrt.setObjectName("pushButtonSqrt")
        self.GridButton.addWidget(self.pushButtonSqrt, 4, 2, 1, 1)
        self.pushButtonBracketR = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBracketR.sizePolicy().hasHeightForWidth())
        self.pushButtonBracketR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonBracketR.setFont(font)
        self.pushButtonBracketR.setObjectName("pushButtonBracketR")
        self.GridButton.addWidget(self.pushButtonBracketR, 2, 2, 1, 1)
        self.pushButtonMinus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMinus.sizePolicy().hasHeightForWidth())
        self.pushButtonMinus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonMinus.setFont(font)
        self.pushButtonMinus.setObjectName("pushButtonMinus")
        self.GridButton.addWidget(self.pushButtonMinus, 7, 3, 1, 1)
        self.pushButtonMod = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMod.sizePolicy().hasHeightForWidth())
        self.pushButtonMod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonMod.setFont(font)
        self.pushButtonMod.setObjectName("pushButtonMod")
        self.GridButton.addWidget(self.pushButtonMod, 2, 0, 1, 1)
        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonC.sizePolicy().hasHeightForWidth())
        self.pushButtonC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonC.setFont(font)
        self.pushButtonC.setObjectName("pushButtonC")
        self.GridButton.addWidget(self.pushButtonC, 0, 1, 1, 1)
        self.pushButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlus.sizePolicy().hasHeightForWidth())
        self.pushButtonPlus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setStyleSheet("")
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.GridButton.addWidget(self.pushButtonPlus, 10, 3, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.GridButton.addWidget(self.pushButton1, 10, 0, 1, 1)
        self.pushButtonX_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonX_1.sizePolicy().hasHeightForWidth())
        self.pushButtonX_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonX_1.setFont(font)
        self.pushButtonX_1.setObjectName("pushButtonX_1")
        self.GridButton.addWidget(self.pushButtonX_1, 4, 0, 1, 1)
        self.pushButtonPLusMinus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPLusMinus.sizePolicy().hasHeightForWidth())
        self.pushButtonPLusMinus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonPLusMinus.setFont(font)
        self.pushButtonPLusMinus.setStyleSheet("")
        self.pushButtonPLusMinus.setObjectName("pushButtonPLusMinus")
        self.GridButton.addWidget(self.pushButtonPLusMinus, 11, 0, 1, 1)
        self.pushButtonDel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDel.sizePolicy().hasHeightForWidth())
        self.pushButtonDel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonDel.setFont(font)
        self.pushButtonDel.setStyleSheet("")
        self.pushButtonDel.setObjectName("pushButtonDel")
        self.GridButton.addWidget(self.pushButtonDel, 0, 3, 1, 1)
        self.pushButtonMult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMult.sizePolicy().hasHeightForWidth())
        self.pushButtonMult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonMult.setFont(font)
        self.pushButtonMult.setObjectName("pushButtonMult")
        self.GridButton.addWidget(self.pushButtonMult, 5, 3, 1, 1)
        self.pushButtonDot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDot.sizePolicy().hasHeightForWidth())
        self.pushButtonDot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonDot.setFont(font)
        self.pushButtonDot.setObjectName("pushButtonDot")
        self.GridButton.addWidget(self.pushButtonDot, 11, 2, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("")
        self.pushButton2.setObjectName("pushButton2")
        self.GridButton.addWidget(self.pushButton2, 10, 1, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton7.sizePolicy().hasHeightForWidth())
        self.pushButton7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")
        self.GridButton.addWidget(self.pushButton7, 5, 0, 1, 1)
        self.pushButtonCe = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCe.sizePolicy().hasHeightForWidth())
        self.pushButtonCe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonCe.setFont(font)
        self.pushButtonCe.setShortcut("")
        self.pushButtonCe.setObjectName("pushButtonCe")
        self.GridButton.addWidget(self.pushButtonCe, 0, 2, 1, 1)
        self.pushButtonBracketL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBracketL.sizePolicy().hasHeightForWidth())
        self.pushButtonBracketL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonBracketL.setFont(font)
        self.pushButtonBracketL.setObjectName("pushButtonBracketL")
        self.GridButton.addWidget(self.pushButtonBracketL, 2, 1, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("")
        self.pushButton3.setObjectName("pushButton3")
        self.GridButton.addWidget(self.pushButton3, 10, 2, 1, 1)
        self.pushButtonDiv = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDiv.sizePolicy().hasHeightForWidth())
        self.pushButtonDiv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonDiv.setFont(font)
        self.pushButtonDiv.setObjectName("pushButtonDiv")
        self.GridButton.addWidget(self.pushButtonDiv, 4, 3, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton6.sizePolicy().hasHeightForWidth())
        self.pushButton6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.GridButton.addWidget(self.pushButton6, 7, 2, 1, 1)
        self.pushButtonEqual = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEqual.sizePolicy().hasHeightForWidth())
        self.pushButtonEqual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonEqual.setFont(font)
        self.pushButtonEqual.setStyleSheet(" QPushButton#pushButtonEqual {\n"
"     background-color: rgb(180, 252, 255);\n"
" }\n"
"\n"
"QPushButton#pushButtonEqual:hover {\n"
"     background-color: rgb(124, 249, 255);\n"
" }\n"
"QPushButton#pushButtonEqual:pressed {\n"
"     background-color: rgb(102, 148, 255);     \n"
" }\n"
"")
        self.pushButtonEqual.setObjectName("pushButtonEqual")
        self.GridButton.addWidget(self.pushButtonEqual, 11, 3, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton0.sizePolicy().hasHeightForWidth())
        self.pushButton0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton0.setFont(font)
        self.pushButton0.setStyleSheet("")
        self.pushButton0.setObjectName("pushButton0")
        self.GridButton.addWidget(self.pushButton0, 11, 1, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton8.sizePolicy().hasHeightForWidth())
        self.pushButton8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton8.setFont(font)
        self.pushButton8.setObjectName("pushButton8")
        self.GridButton.addWidget(self.pushButton8, 5, 1, 1, 1)
        self.pushButtonFactorial = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonFactorial.sizePolicy().hasHeightForWidth())
        self.pushButtonFactorial.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButtonFactorial.setFont(font)
        self.pushButtonFactorial.setShortcut("")
        self.pushButtonFactorial.setObjectName("pushButtonFactorial")
        self.GridButton.addWidget(self.pushButtonFactorial, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.GridButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEditInput.setText(_translate("MainWindow", "0"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButton9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton5.setShortcut(_translate("MainWindow", "5"))
        self.pushButtonSqr.setText(_translate("MainWindow", "x²"))
        self.pushButtonSqrt.setText(_translate("MainWindow", "√x"))
        self.pushButtonBracketR.setText(_translate("MainWindow", ")"))
        self.pushButtonBracketR.setShortcut(_translate("MainWindow", ")"))
        self.pushButtonMinus.setText(_translate("MainWindow", "-"))
        self.pushButtonMinus.setShortcut(_translate("MainWindow", "-"))
        self.pushButtonMod.setText(_translate("MainWindow", "%"))
        self.pushButtonMod.setShortcut(_translate("MainWindow", "%"))
        self.pushButtonC.setText(_translate("MainWindow", "c"))
        self.pushButtonPlus.setText(_translate("MainWindow", "+"))
        self.pushButtonPlus.setShortcut(_translate("MainWindow", "+"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButton1.setShortcut(_translate("MainWindow", "1"))
        self.pushButtonX_1.setText(_translate("MainWindow", "1/x"))
        self.pushButtonPLusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButtonDel.setText(_translate("MainWindow", "⌫"))
        self.pushButtonDel.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushButtonMult.setText(_translate("MainWindow", "×"))
        self.pushButtonMult.setShortcut(_translate("MainWindow", "*"))
        self.pushButtonDot.setText(_translate("MainWindow", "."))
        self.pushButtonDot.setShortcut(_translate("MainWindow", "."))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton7.setShortcut(_translate("MainWindow", "7"))
        self.pushButtonCe.setText(_translate("MainWindow", "ce"))
        self.pushButtonBracketL.setText(_translate("MainWindow", "("))
        self.pushButtonBracketL.setShortcut(_translate("MainWindow", "("))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton3.setShortcut(_translate("MainWindow", "3"))
        self.pushButtonDiv.setText(_translate("MainWindow", "÷"))
        self.pushButtonDiv.setShortcut(_translate("MainWindow", "/"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButton6.setShortcut(_translate("MainWindow", "6"))
        self.pushButtonEqual.setText(_translate("MainWindow", "="))
        self.pushButtonEqual.setShortcut(_translate("MainWindow", "="))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButton0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton8.setShortcut(_translate("MainWindow", "8"))
        self.pushButtonFactorial.setText(_translate("MainWindow", "!"))
