#be nam _e_ khoda

import sys
from PyQt4 import QtCore,QtGui,Qt
import datetime
from functools import partial
import customizedlb
import os


class base(QtGui.QWidget):

    """The base class for the window containing the tools of the selected section. """

    def __init__(self, sectionname, down):
        QtGui.QWidget.__init__(self, parent=None)
        #self.setStyleSheet("margin:5px; border:1px solid rgb(0, 255, 0);")
        self.setContentsMargins(0, 0, 0, down)

        self.contentbox = QtGui.QGridLayout()
        self.setLayout(self.contentbox)
        self.contentbox.setMargin(0)


        self.sectionname = QtGui.QLabel()
        self.sectionname.setText(sectionname)
        self.sectionname.setAlignment(QtCore.Qt.AlignCenter)

        self.setStyleSheet("QLabel { background-color : rgb(220,225,230); color : black; }")
        font = QtGui.QFont('Arial', 12)
        font.setBold(True)
        self.sectionname.setFont(font)

        self.contentbox.addWidget(self.sectionname, 0, 0, 2, 21)


    def addWidget(self, item, r, c, rs, cs):

        self.contentbox.addWidget(item, r, c, rs, cs)

    def ctrl_handler(self, toolname):

        """This method defines the corresponding action of the button """

        print '%s clicked'%toolname


class home(base):
    
    def __init__(self):
        
        base.__init__(self, 'Home', 20)
        self.construct()

    def construct(self):

        self.user = 'Mehran Memarnejad'
        self.user_lb  = QtGui.QLabel()
        self.user_lb.setStyleSheet("QLabel { background-color : white; }")
        self.user_lb.setText('<b>User</b> : ' + self.user)
        self.addWidget(self.user_lb, 3, 1, 1, 7)

        self.date  = datetime.date.today().strftime('%d %b %Y')
        self.date_lb = QtGui.QLabel()
        self.date_lb.setStyleSheet("QLabel { background-color : white; }")
        self.date_lb.setText('<b>Date</b> : ' + self.date)
        self.addWidget(self.date_lb, 3, 11, 1, 8)

        self.note_lb = QtGui.QLabel()
        self.note_lb.setText('<b>Notes :</b>')
        self.note_lb.setStyleSheet("QLabel { background-color : white; }")
        self.addWidget(self.note_lb, 5, 1, 1, 8) #2 to 7

        self.employeemsg_lb = QtGui.QLabel()
        self.employeemsg_lb.setText("<b>Employee's Message :</b>")
        self.employeemsg_lb.setStyleSheet("QLabel { background-color : white; }")
        self.addWidget(self.employeemsg_lb, 5, 11, 1, 10)

        self.note_scr = QtGui.QScrollArea()
        self.note_scr.setWidgetResizable(True)
        note_widget = QtGui.QWidget()
        note_widget.setContentsMargins(0, 0, 0, 0)
        self.note_content = QtGui.QVBoxLayout(note_widget)
        self.note_content.setContentsMargins(0, 0, 0, 0)
        self.note_scr.setWidget(note_widget)
        self.addWidget(self.note_scr, 8, 1, 14, 9)

        self.new_btn = QtGui.QPushButton()
        self.new_btn.setText('New')
        self.addWidget(self.new_btn, 23, 3, 1, 2)

        self.del_btn = QtGui.QPushButton()
        self.del_btn.setText('Delete')
        self.addWidget(self.del_btn, 23, 7, 1, 2)


        self.emp_msg_scr = QtGui.QScrollArea()
        self.emp_msg_scr.setWidgetResizable(True)
        emp_msg_widget = QtGui.QWidget()
        emp_msg_widget.setContentsMargins(0, 0, 0, 0)
        self.emp_msg_content = QtGui.QVBoxLayout(emp_msg_widget)
        self.emp_msg_content.setContentsMargins(0, 0, 0, 0)
        self.emp_msg_scr.setWidget(emp_msg_widget)
        self.addWidget(self.emp_msg_scr, 8, 11, 14, 9)

        self.send_to_note_btn = QtGui.QPushButton()
        self.send_to_note_btn.setText('Send to Notes')
        self.addWidget(self.send_to_note_btn, 23, 12, 1, 2)

        self.emp_msg_del_btn = QtGui.QPushButton()
        self.emp_msg_del_btn.setText('Delete')
        self.addWidget(self.emp_msg_del_btn, 23, 16, 1, 2)

        for i in range(0, 40):

            self.add_note('This is a note %s'%i)

        for j in range(0, 40):

            self.add_emp_message('This is a employee message %s'%j)

    def set_user(self, name):

        #todo check if there is no need to change the label

        self.user = name
        self.user_lb.setText('User : ' + self.user)

    def add_note(self, text):

        note = QtGui.QLabel()
        note.setStyleSheet("QLabel { background-color : white;}")
        note.setText(text)
        self.note_content.addWidget(note)

    def add_emp_message(self, text):

        emp_msg = QtGui.QLabel()
        emp_msg.setStyleSheet("QLabel { background-color : white;}")
        emp_msg.setText(text)
        self.emp_msg_content.addWidget(emp_msg)
        
        
class employee_management(base):

    def __init__(self):

        base.__init__(self, 'Employee Management', 233)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.new_emp = customizedlb.toollabel('New Employee', 'Add a new member', '%s\Pics\\tool menu\employee management\\add.png'%os.getcwd())
        self.new_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'New Employee'))
        vbox.addWidget(self.new_emp)

        self.modify_emp = customizedlb.toollabel('Modify Information', 'Modify an existing member', '%s\Pics\\tool menu\employee management\modify.png'%os.getcwd())
        self.modify_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'Modify Employee'))
        vbox.addWidget(self.modify_emp)

        self.remove_emp = customizedlb.toollabel('Remove Employee', 'Fire an Employee', '%s\Pics\\tool menu\employee management\\remove.png'%os.getcwd())
        self.remove_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'Remove Employee'))
        vbox.addWidget(self.remove_emp)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class item_management(base):

    def __init__(self):
        base.__init__(self, 'Item Management', 167)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.item_list = customizedlb.toollabel('Item List', 'List of all items', '%s\Pics\\tool menu\item management\item list.png'%os.getcwd())
        self.item_list.toollabel_clicked.connect(partial(self.ctrl_handler, 'Item List'))
        vbox.addWidget(self.item_list)

        self.new_item = customizedlb.toollabel('New Item', 'Add a new Item', '%s\Pics\\tool menu\item management\\new item.png'%os.getcwd())
        self.new_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'New Item'))
        vbox.addWidget(self.new_item)

        self.modify_item = customizedlb.toollabel('Modify Item', 'Change item info', '%s\Pics\\tool menu\item management\modify item.png'%os.getcwd())
        self.modify_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'Modify Item'))
        vbox.addWidget(self.modify_item)

        self.remove_item = customizedlb.toollabel('Remove Item', 'Remove item', '%s\Pics\\tool menu\item management\\remove item.png'%os.getcwd())
        self.remove_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'Remove Item'))
        vbox.addWidget(self.remove_item)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class order_management(base):

    def __init__(self):
        base.__init__(self,'Order Management', 227)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.new_order = customizedlb.toollabel('New Order', 'Add a new order', '%s\Pics\\tool menu\order management\\new order.png'%os.getcwd())
        self.new_order.toollabel_clicked.connect(partial(self.ctrl_handler, 'New Order'))
        vbox.addWidget(self.new_order)

        self.modify_order = customizedlb.toollabel('Modify Order', 'Change order info', '%s\Pics\\tool menu\order management\modify order.png'%os.getcwd())
        self.modify_order.toollabel_clicked.connect(partial(self.ctrl_handler, 'Modify Order'))
        vbox.addWidget(self.modify_order)

        self.order_status = customizedlb.toollabel('Order Status', 'Peygiri order', '%s\Pics\\tool menu\order management\order status.png'%os.getcwd())
        self.order_status.toollabel_clicked.connect(partial(self.ctrl_handler, 'Order Status'))
        vbox.addWidget(self.order_status)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class producer_info(base):

    def __init__(self):
        base.__init__(self,'Not created personal info page', 489)


class kala_aghsati(base):

    def __init__(self):
        base.__init__(self,'Not created kala aghsati page', 489)


class report(base):

    def __init__(self):

        base.__init__(self, 'Report', 233)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.Items_report = customizedlb.toollabel('Items Report', 'Get report about items', '%s\Pics\\tool menu\\report\items report.png'%os.getcwd())
        self.Items_report.toollabel_clicked.connect(partial(self.ctrl_handler, 'Items Report'))
        vbox.addWidget(self.Items_report)

        self.advance_search = customizedlb.toollabel('Advance Search', 'Search Presicely', '%s\Pics\\tool menu\\report\search.png'%os.getcwd())
        self.advance_search.toollabel_clicked.connect(partial(self.ctrl_handler, 'Advance Search'))
        vbox.addWidget(self.advance_search)

        self.advance_report = customizedlb.toollabel('Advance Report', 'Get accurate report', '%s\Pics\\tool menu\\report\\advance report.png'%os.getcwd())
        self.advance_report.toollabel_clicked.connect(partial(self.ctrl_handler, 'Advance Report'))
        vbox.addWidget(self.advance_report)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class account(base):

    def __init__(self):
        base.__init__(self,'Account', 155)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.new_account = customizedlb.toollabel('New Account', 'Create a new account', '%s\Pics\\tool menu\\account\\new.png'%os.getcwd())
        self.new_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'New Account'))
        vbox.addWidget(self.new_account)

        self.modify_account = customizedlb.toollabel('Modify Account', 'Modify an existing account', '%s\Pics\\tool menu\\account\modify.png'%os.getcwd())
        self.modify_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'Modify Account'))
        vbox.addWidget(self.modify_account)

        self.block_account = customizedlb.toollabel('Block Account', 'Modify an existing account', '%s\Pics\\tool menu\\account\\block.png'%os.getcwd())
        self.block_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'Block Account'))
        vbox.addWidget(self.block_account)

        self.remove_account = customizedlb.toollabel('Remove Account', 'Remove an account', '%s\Pics\\tool menu\\account\\remove.png'%os.getcwd())
        self.remove_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'Remove Account'))
        vbox.addWidget(self.remove_account)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class setting(base):

    def __init__(self):
        base.__init__(self,'Setting', 167)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.network_config = customizedlb.toollabel('Network Configuration', 'Set  network IP', '%s\Pics\\tool menu\setting\\network.png'%os.getcwd())
        self.network_config.toollabel_clicked.connect(partial(self.ctrl_handler, 'Network Configuration'))
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(self.network_config)
        hbox1.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox1)

        self.change_account_info = customizedlb.toollabel('Change Account Info', 'Change Account Info', '%s\Pics\\tool menu\setting\change info.png'%os.getcwd())
        self.change_account_info.toollabel_clicked.connect(partial(self.ctrl_handler, 'Modify Account'))
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.change_account_info)
        hbox2.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox2)

        self.product_activation = customizedlb.toollabel('Product Activation', 'Activate Product With License Key', '%s\Pics\\tool menu\setting\\activate.png'%os.getcwd())
        self.product_activation.toollabel_clicked.connect(partial(self.ctrl_handler, 'Product Activation'))
        hbox3 = QtGui.QHBoxLayout()
        hbox3.addWidget(self.product_activation)
        hbox3.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox3)

        self.update_product = customizedlb.toollabel('Update Product', 'Installed Version : 1.1', '%s\Pics\\tool menu\setting\update.png'%os.getcwd())
        self.update_product.toollabel_clicked.connect(partial(self.ctrl_handler, 'Remove Account'))
        hbox4 = QtGui.QHBoxLayout()
        hbox4.addWidget(self.update_product)
        hbox4.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox4)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)


class help(base):

    def __init__(self):
        base.__init__(self,'Help', 233)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

        vbox.addSpacing(40)

        self.help = customizedlb.toollabel('Help', 'Help', '%s\Pics\\tool menu\help\\help.png'%os.getcwd())
        self.help.toollabel_clicked.connect(partial(self.ctrl_handler, 'Help'))
        vbox.addWidget(self.help)

        self.support = customizedlb.toollabel('Support', 'Get Online Help', '%s\Pics\\tool menu\help\support.png'%os.getcwd())
        self.support.toollabel_clicked.connect(partial(self.ctrl_handler, 'Support'))
        vbox.addWidget(self.support)

        self.SMS_info = customizedlb.toollabel('SMS Information', 'About System', '%s\Pics\\tool menu\help\information.png'%os.getcwd())
        self.SMS_info.toollabel_clicked.connect(partial(self.ctrl_handler, 'SMS Info'))
        vbox.addWidget(self.SMS_info)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.addWidget(widget, 4, 2, 8, 6)
