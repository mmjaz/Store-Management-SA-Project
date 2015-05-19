#be nam _e_ khoda


from PyQt4 import QtCore,QtGui


class mylabel (QtGui.QLabel):

    mylb_clicked = QtCore.pyqtSignal()

    def __init__(self):

        QtGui.QLabel.__init__(self, parent=None)

        #self("<html><img 'home.png'></html>")
        self.setStyleSheet("QLabel { background-color : white; color : gray; }")

        lb_font = QtGui.QFont('calibri', 12)
        #lb_font.setBold(True)
        self.setFont(lb_font)

        self.setMargin(5)

    def mousePressEvent(self, event):

        if (event.button() == QtCore.Qt.LeftButton):

            self.mylb_clicked.emit()
            self.selected()

    def dragLeaveEvent(self, *args, **kwargs):

        self.deselect()

    def enterEvent(self, *args, **kwargs):

        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def leaveEvent(self, *args, **kwargs):

        QtGui.QApplication.restoreOverrideCursor()

    def deselect(self):

        self.setStyleSheet("QLabel { background-color : white; color : gray; }")
        
    def selected(self):
        """It is used to change the color of a clicked label (one label)."""
        self.setStyleSheet("QLabel { background-color : rgb(220,225,230); color : black; }")
        

class menulbcalss(QtGui.QWidget):

    selected_tool_sgnl = QtCore.pyqtSignal()

    def __init__(self, text, address):

        super(menulbcalss, self).__init__()

        self.create_lb(text, address)

    def create_lb(self, text, icon_address):

        self.layout = QtGui.QGridLayout()
        self.layout.setMargin(0)

        self.icn_lb = mylabel()
        self.icn_lb.mylb_clicked.connect(self.select_iclb)


        self.icn_pic = QtGui.QPixmap(icon_address)
        #icn_pic = icn_pic.scaled(icn_lb.size(), QtCore.Qt.KeepAspectRatio)
        self.icn_lb.setPixmap(self.icn_pic)
        self.layout.addWidget(self.icn_lb, 0, 0, 2, 3)

        self.txt_lb = mylabel()
        self.txt_lb.mylb_clicked.connect(self.select_iclb)
        self.txt_lb.setMargin(1)
        self.txt_lb.setText(text)
        self.layout.addWidget(self.txt_lb, 0, 1, 2, 6)

        self.setLayout(self.layout)
        
    def select_iclb(self):
        """It is used to sync the coloring of icon and text. """
        #Todo bayad in bakhsh ro dorost konam ehsas mikonam loop ast (dorost shod)
        self.selected_tool_sgnl.emit()
        self.txt_lb.selected()
        self.icn_lb.selected()

    def deselect_iclb(self):
        """It is used to sync the coloring of icon and text. """
        
        self.txt_lb.deselect()
        self.icn_lb.deselect()


class mylabel2(QtGui.QLabel):

    mylb2_clicked = QtCore.pyqtSignal()
    mylb2_undermouse = QtCore.pyqtSignal()
    mylb2_outmouse = QtCore.pyqtSignal()

    def __init__(self, fsize , fcolor):

        QtGui.QLabel.__init__(self, parent=None)
        self.fcolor = fcolor

        #self("<html><img 'home.png'></html>")
        self.setStyleSheet("QLabel { background-color : white; color : %s;}"%fcolor)

        lb_font = QtGui.QFont('calibri', fsize)
        #lb_font.setBold(True)
        self.setFont(lb_font)

        self.setMargin(5)

    def mousePressEvent(self, event):

        if (event.button() == QtCore.Qt.LeftButton):

            self.mylb2_clicked.emit()

    def enterEvent(self, *args, **kwargs):

        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("QLabel { background-color : rgb(220,225,230);color : %s;}"%self.fcolor)
        self.mylb2_undermouse.emit()

    def leaveEvent(self, *args, **kwargs):

        QtGui.QApplication.restoreOverrideCursor()
        self.setStyleSheet("QLabel { background-color : white; color : %s;}"%self.fcolor)
        self.mylb2_outmouse.emit()

    def selected(self):

        self.setStyleSheet("QLabel { background-color : rgb(220,225,230);color : %s;}"%self.fcolor)

    def deselected(self):

        self.setStyleSheet("QLabel { background-color : white; color : %s;}"%self.fcolor)


class toollabel(QtGui.QWidget):

    toollabel_clicked = QtCore.pyqtSignal()

    def __init__(self,ptext, stext, icon_address):

        super(toollabel, self).__init__()
        self.create_lb(ptext, stext, icon_address)

    def create_lb(self, ptext, stext, address):

        self.contentbox = QtGui.QGridLayout()
        self.contentbox.setContentsMargins(0, 0, 0, 0)
        self.contentbox.setMargin(0)
        self.setLayout(self.contentbox)
        self.contentbox.setSpacing(0)

        self.icn_lb = mylabel2(0,'red')
        self.icn_lb.mylb2_clicked.connect(self.select_iclb)
        self.icn_lb.mylb2_undermouse.connect(self.undermouse_iclb)
        self.icn_lb.mylb2_outmouse.connect(self.outmouse_iclb)

        self.icn_pic = QtGui.QPixmap(address)
        #icn_pic = icn_pic.scaled(icn_lb.size(), QtCore.Qt.KeepAspectRatio)
        self.icn_lb.setPixmap(self.icn_pic)
        self.contentbox.addWidget(self.icn_lb, 0, 0, 2, 2)

        self.ptxt_lb = mylabel2(12, 'blue')
        self.ptxt_lb.mylb2_clicked.connect(self.select_iclb)
        self.ptxt_lb.mylb2_undermouse.connect(self.undermouse_iclb)
        self.ptxt_lb.mylb2_outmouse.connect(self.outmouse_iclb)
        self.ptxt_lb.setMargin(1)
        self.ptxt_lb.setText(ptext)
        self.contentbox.addWidget(self.ptxt_lb, 0, 2, 1, 4)

        self.stxt_lb = mylabel2(8, 'black')
        self.stxt_lb.mylb2_clicked.connect(self.select_iclb)
        self.stxt_lb.mylb2_undermouse.connect(self.undermouse_iclb)
        self.stxt_lb.mylb2_outmouse.connect(self.outmouse_iclb)
        self.stxt_lb.setMargin(1)
        self.stxt_lb.setText(stext)
        self.contentbox.addWidget(self.stxt_lb, 1, 2, 1, 4)

    def select_iclb(self):

        self.toollabel_clicked.emit()

    def undermouse_iclb(self):

        self.icn_lb.selected()
        self.ptxt_lb.selected()
        self.stxt_lb.selected()

    def outmouse_iclb(self):

        self.icn_lb.deselected()
        self.ptxt_lb.deselected()
        self.stxt_lb.deselected()




        





