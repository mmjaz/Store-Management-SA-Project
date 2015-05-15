__author__ = 'mehdi'

import sys
from welcomemsg import *
class AddForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.
        dispmessage)
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'),self.
        ExitApp)#baayad hatman trigger() baashad


    def dispmessage(self):
        A=self.ui.ID.text()
        B=self.ui.Name.text()
        C=self.ui.Cost.text()
        print A
        print B
        print C
        #self.clientsocket.send((A,B,C))
        self.close()
    def ExitApp(self):
        self.close()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AddForm()
    myapp.show()
    sys.exit(app.exec_())
