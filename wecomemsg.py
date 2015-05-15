# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomems.ui'
#
# Created: Tue May 12 22:27:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(469, 283)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ID = QtGui.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.IDLable = QtGui.QLabel(self.centralwidget)
        self.IDLable.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.IDLable.setProperty("qlable", _fromUtf8(""))
        self.IDLable.setObjectName(_fromUtf8("IDLable"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.pushButton.setProperty("click", _fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.NameLable = QtGui.QLabel(self.centralwidget)
        self.NameLable.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.NameLable.setProperty("qlable", _fromUtf8(""))
        self.NameLable.setObjectName(_fromUtf8("NameLable"))
        self.Name = QtGui.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.Costlabel = QtGui.QLabel(self.centralwidget)
        self.Costlabel.setGeometry(QtCore.QRect(10, 120, 81, 20))
        self.Costlabel.setProperty("qlable", _fromUtf8(""))
        self.Costlabel.setObjectName(_fromUtf8("Costlabel"))
        self.Cost = QtGui.QLineEdit(self.centralwidget)
        self.Cost.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.Cost.setObjectName(_fromUtf8("Cost"))

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.IDLable.setText(_translate("MainWindow", "ID", None))
        self.pushButton.setText(_translate("MainWindow", "ADD", None))
        self.NameLable.setText(_translate("MainWindow", "Name", None))
        self.Costlabel.setText(_translate("MainWindow", "Cost", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

