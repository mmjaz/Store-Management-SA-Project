#Be nam _e_ khoda
#Mehran Memarnejad

import sys
from PyQt4 import QtCore,QtGui,Qt
from functools import partial
from customizedlb import menulbcalss
import os
import toolpagectrl
               

class manager(QtGui.QWidget):

    def __init__(self):

        super(manager, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.username = ''
        self.password = ''
        self.rememberstate = False
        self.menu_item = ['self.home_lb', 'self.employee_management_lb', 'self.account_lb', 'self.item_management_lb',
                          'self.order_management_lb', 'self.producer_info_lb', 'self.kala_aghsati_lb', 'self.report_lb','self.setting_lb', 'self.help_lb']
        self.window_constructor()

    def window_constructor(self):
        """It is used to  make the main window and initialize it"""

        #############################################################################
        #General configuration of the main window                                   #
        #############################################################################

        self.setStyleSheet("QWidget { background-color : white}")
        self.setWindowTitle('Store Management System (Manager)')
        self.setWindowFlags(Qt.Qt.CustomizeWindowHint | Qt.Qt.WindowCloseButtonHint | Qt.Qt.WindowMinimizeButtonHint)

        screensize = QtGui.QDesktopWidget().screenGeometry()
        self.setFixedSize(3*screensize.width()/5, 7.6*screensize.height()/10)
        self.center()

        self.setContentsMargins(0, 0, 0, 0)


        self.contentbox = QtGui.QGridLayout()
        self.contentbox.setContentsMargins(0, 0, 0, 0)
        self.contentbox.setSpacing(0)
        self.setLayout(self.contentbox)

        #############################################################################
        #The Application Header Showing (SMS)                                       #
        #############################################################################

        top_banner = QtGui.QPixmap('%s\Pics\\top.jpg'%os.getcwd())
        top_banner_lb = QtGui.QLabel()
        #scaled_top_banner = top_banner.scaled(top_banner_lb.size(), QtCore.Qt.KeepAspectRatio)
        top_banner_lb.setPixmap(top_banner)
        #top_banner_lb.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.contentbox.addWidget(top_banner_lb, 0, 0, 1, 28)

        #############################################################################
        #The left Hand Menu Bar Containing The Main Tools                           #
        #############################################################################

        self.home_lb = menulbcalss('Home', '%s\Pics\Menu\home.png'%os.getcwd())
        self.contentbox.addWidget(self.home_lb, 5, 0, 2, 7)
        self.home_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'home'))


        self.employee_management_lb = menulbcalss('Employee Management', '%s\Pics\Menu\employee.png'%os.getcwd())
        self.contentbox.addWidget(self.employee_management_lb, 7, 0, 2, 7)
        self.employee_management_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'employee_management'))

        self.item_management_lb = menulbcalss('Item Management', '%s\Pics\Menu\item.png'%os.getcwd())
        self.contentbox.addWidget(self.item_management_lb, 9, 0, 2, 7)
        self.item_management_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'item_management'))

        self.order_management_lb = menulbcalss('Order Management', '%s\Pics\Menu\order.png'%os.getcwd())
        self.contentbox.addWidget(self.order_management_lb, 11, 0, 2, 7)
        self.order_management_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'order_management'))

        self.producer_info_lb = menulbcalss('Producer Info', '%s\Pics\Menu\\factory.png'%os.getcwd())
        self.contentbox.addWidget(self.producer_info_lb, 13, 0, 2, 7)
        self.producer_info_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'producer_info'))

        self.kala_aghsati_lb = menulbcalss('Kala Aghsati', '%s\Pics\Menu\kala aghsati.png'%os.getcwd())
        self.contentbox.addWidget(self.kala_aghsati_lb, 15, 0, 2, 7)
        self.kala_aghsati_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'kala_aghsati'))

        self.report_lb = menulbcalss('Report', '%s\Pics\Menu\\report.png'%os.getcwd())
        self.contentbox.addWidget(self.report_lb, 17, 0, 2, 7)
        self.report_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'report'))

        self.account_lb = menulbcalss('Account', '%s\Pics\Menu\\account.png'%os.getcwd())
        self.contentbox.addWidget(self.account_lb, 19, 0, 2, 7)
        self.account_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'account'))

        self.setting_lb = menulbcalss('Setting', '%s\Pics\Menu\setting.png'%os.getcwd())
        self.contentbox.addWidget(self.setting_lb, 21, 0, 2, 7)
        self.setting_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'setting'))

        self.help_lb = menulbcalss('Help and Support', '%s\Pics\Menu\help.png'%os.getcwd())
        self.contentbox.addWidget(self.help_lb, 23, 0, 2, 7)
        self.help_lb.selected_tool_sgnl.connect(partial(self.mylb_handler, 'help'))


        self.contentbox.rowStretch(7)

        # seperator = QtGui.QLabel('')
        # self.contentbox.addWidget(seperator, 2, 6, 23, 1)
        # seperator.setFrameStyle(QtGui.QFrame.VLine)
        # seperator.setFrameShadow(QtGui.QFrame.Raised)

        #############################################################################
        #The Right Hand Containing The Tools Of Menu Item                           #
        #############################################################################

        self.maintoolwidget = QtGui.QWidget()
        self.maintoolwidgetlayout = QtGui.QVBoxLayout()
        self.maintoolwidget.setContentsMargins(0,0,0,0)
        self.maintoolwidgetlayout.setContentsMargins(0,0,0,0)
        self.maintoolwidget.setLayout(self.maintoolwidgetlayout)
        self.contentbox.addWidget(self.maintoolwidget, 2, 7, 30, 40)

        #tool_widget = righthand.help()
        #tool_widget = righthand.employee_management()
        #self.contentbox.addWidget(tool_widget, 2, 7, 30, 40)

        self.home_lb.select_iclb()
        self.show()

    def mylb_handler(self, name):

        tool_widget = eval('toolpagectrl.%s()'%name)

        old_layout = self.maintoolwidget.layout()
        for i in reversed(range(old_layout.count())):
            old_layout.itemAt(i).widget().setParent(None)

        self.maintoolwidgetlayout.addWidget(tool_widget)


        """It is used to select the clicked tool in the menu and deselect the previously selected tool."""
        #TOdo the input parameter name is not used any more

        for item in self.menu_item:

            eval('%s.deselect_iclb()'%item)

        #eval(('self.%s.select_iclb'%name))

    def center(self):
        """This function moves window to the center."""

        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())




def main():
    app = QtGui.QApplication(sys.argv)
    manager_pg = manager()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

