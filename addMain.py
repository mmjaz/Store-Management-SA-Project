__author__ = 'mehdi'
import sys
import AddKalaForm
from addkala import * #addkala is user interface
class ItemManagement(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Add() #class addkala
        self.ui.setupUi(self)
        self.Addform = AddKalaForm.AddForm()

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.
        openWindowOfAdd)
        #QtCore.QObject.connect(self.ui.ModifyButton, QtCore.SIGNAL('clicked()'),self.
        #openWindowOfModify)
        #QtCore.QObject.connect(self.ui.DeleteButton, QtCore.SIGNAL('clicked()'),self.
        #openWindowOfDelete)

    def openWindowOfAdd(self):
        print 'add clicked'
        self.Addform.show()
    def openWindowOfModify(self):
        pass
    def openWindowOfDelete(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ItemManagement()
    myapp.show()
    sys.exit(app.exec_())
