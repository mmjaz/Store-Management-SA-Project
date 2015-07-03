#be nam _e_ khoda


from PyQt4 import QtCore,QtGui
import datetime
from functools import partial
import customizedlb
import os
import toolsfunction


class Base(QtGui.QWidget):

    """The Base class for the window containing the tools of the selected section. """

    def __init__(self, sectionname, down):
        QtGui.QWidget.__init__(self, parent=None)
        #self.setStyleSheet("margin:5px; border:1px solid rgb(0, 255, 0);")
        self.setContentsMargins(0, 0, 0, down)

        self.contentbox = QtGui.QVBoxLayout()
        self.setLayout(self.contentbox)
        self.contentbox.setMargin(0)


        self.sectionname = QtGui.QLabel()
        self.sectionname.setText(sectionname)
        self.sectionname.setAlignment(QtCore.Qt.AlignCenter)

        self.setStyleSheet("QLabel { background-color : rgb(220,225,230); color : black; }")
        font = QtGui.QFont('Arial', 12)
        font.setBold(True)
        self.sectionname.setFont(font)

        section_layout = QtGui.QHBoxLayout()
        section_layout.addWidget(self.sectionname)
        self.contentbox.addLayout(section_layout)

    def addLayout(self, item):

        self.contentbox.addSpacing(25)
        self.contentbox.addLayout(item)

    def ctrl_handler(self, toolname):

        """This method defines the corresponding action of the button """

        tool_widget = eval('toolsfunction.%s()'%toolname)

        QtGui.QWidget().setLayout(self.layout())
        self.contentbox = QtGui.QVBoxLayout(self)
        self.contentbox.setMargin(0)


        self.contentbox.addWidget(tool_widget)


class home(Base):
    
    def __init__(self):
        
        Base.__init__(self, 'Home', 70)
        self.construct()

    def construct(self):

        grid = QtGui.QGridLayout()
        grid.setContentsMargins(25,0,0,0)
        self.user = 'Mehran Memarnejad'
        self.user_lb  = QtGui.QLabel()
        self.user_lb.setStyleSheet("QLabel { background-color : white; }")
        self.user_lb.setText('<b>User</b> : ' + self.user)
        grid.addWidget(self.user_lb, 3, 1, 1, 7)

        self.date  = datetime.date.today().strftime('%d %b %Y')
        self.date_lb = QtGui.QLabel()
        self.date_lb.setStyleSheet("QLabel { background-color : white; }")
        self.date_lb.setText('<b>Date</b> : ' + self.date)
        grid.addWidget(self.date_lb, 3, 11, 1, 8)



        self.note_lb = QtGui.QLabel()
        self.note_lb.setText('<b>Notes :</b>')
        self.note_lb.setStyleSheet("QLabel { background-color : white; }")
        grid.addWidget(self.note_lb, 5, 1, 1, 8) #2 to 7

        self.employeemsg_lb = QtGui.QLabel()
        self.employeemsg_lb.setText("<b>Employee's Message :</b>")
        self.employeemsg_lb.setStyleSheet("QLabel { background-color : white; }")
        grid.addWidget(self.employeemsg_lb, 5, 11, 1, 10)

        self.note_scr = QtGui.QScrollArea()
        self.note_scr.setWidgetResizable(True)
        note_widget = QtGui.QWidget()
        note_widget.setContentsMargins(0, 0, 0, 0)
        self.note_content = QtGui.QVBoxLayout(note_widget)
        self.note_content.setContentsMargins(0, 0, 0, 0)
        self.note_scr.setWidget(note_widget)
        grid.addWidget(self.note_scr, 8, 1, 14, 7)

        self.new_btn = QtGui.QPushButton()
        self.new_btn.setText('New')
        grid.addWidget(self.new_btn, 23, 2, 1, 2)

        self.del_btn = QtGui.QPushButton()
        self.del_btn.setText('Delete')
        grid.addWidget(self.del_btn, 23, 5, 1, 2)


        self.emp_msg_scr = QtGui.QScrollArea()
        self.emp_msg_scr.setWidgetResizable(True)
        emp_msg_widget = QtGui.QWidget()
        emp_msg_widget.setContentsMargins(0, 0, 0, 0)
        self.emp_msg_content = QtGui.QVBoxLayout(emp_msg_widget)
        self.emp_msg_content.setContentsMargins(0, 0, 0, 0)
        self.emp_msg_scr.setWidget(emp_msg_widget)
        grid.addWidget(self.emp_msg_scr, 8, 11, 14, 7)

        self.send_to_note_btn = QtGui.QPushButton()
        self.send_to_note_btn.setText('Send to Notes')
        grid.addWidget(self.send_to_note_btn, 23, 12, 1, 2)

        self.emp_msg_del_btn = QtGui.QPushButton()
        self.emp_msg_del_btn.setText('Delete')
        grid.addWidget(self.emp_msg_del_btn, 23, 15, 1, 2)

        self.addLayout(grid)

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
        
        
class employee_management(Base):

    def __init__(self):

        Base.__init__(self, 'Employee Management', 237)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)
        #vbox.addSpacing(40)

        self.new_emp = customizedlb.toollabel('New Employee', 'Add a new member', '%s\Pics\\tool menu\employee management\\add.png'%os.getcwd())
        self.new_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'NewEmployee'))
        vbox.addWidget(self.new_emp)

        self.modify_emp = customizedlb.toollabel('Modify Information', 'Modify an existing member', '%s\Pics\\tool menu\employee management\modify.png'%os.getcwd())
        self.modify_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyInformation'))
        vbox.addWidget(self.modify_emp)

        self.remove_emp = customizedlb.toollabel('Remove Employee', 'Fire an Employee', '%s\Pics\\tool menu\employee management\\remove.png'%os.getcwd())
        self.remove_emp.toollabel_clicked.connect(partial(self.ctrl_handler, 'RemoveEmployee'))
        vbox.addWidget(self.remove_emp)

        self.addLayout(vbox)


class item_management(Base):

    def __init__(self):
        Base.__init__(self, 'Item Management', 171)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.item_list = customizedlb.toollabel('Item List', 'List of all items', '%s\Pics\\tool menu\item management\item list.png'%os.getcwd())
        self.item_list.toollabel_clicked.connect(partial(self.ctrl_handler, 'ItemList'))
        vbox.addWidget(self.item_list)

        self.new_item = customizedlb.toollabel('New Item', 'Add a new Item', '%s\Pics\\tool menu\item management\\new item.png'%os.getcwd())
        self.new_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'NewItem'))
        vbox.addWidget(self.new_item)

        self.modify_item = customizedlb.toollabel('Modify Item', 'Change item info', '%s\Pics\\tool menu\item management\modify item.png'%os.getcwd())
        self.modify_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyItem'))
        vbox.addWidget(self.modify_item)

        self.remove_item = customizedlb.toollabel('Remove Item', 'Remove item', '%s\Pics\\tool menu\item management\\remove item.png'%os.getcwd())
        self.remove_item.toollabel_clicked.connect(partial(self.ctrl_handler, 'RemoveItem'))
        vbox.addWidget(self.remove_item)


        self.addLayout(vbox)


class order_management(Base):

    def __init__(self):
        Base.__init__(self,'Order Management', 236)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.new_order = customizedlb.toollabel('New Order', 'Add a new order', '%s\Pics\\tool menu\order management\\new order.png'%os.getcwd())
        self.new_order.toollabel_clicked.connect(partial(self.ctrl_handler, 'NewOrder'))
        vbox.addWidget(self.new_order)

        self.modify_order = customizedlb.toollabel('Modify Order', 'Change order info', '%s\Pics\\tool menu\order management\modify order.png'%os.getcwd())
        self.modify_order.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyOrder'))
        vbox.addWidget(self.modify_order)

        self.order_status = customizedlb.toollabel('Remove Order', 'Cancel an order', '%s\Pics\\tool menu\order management\\remove order.png'%os.getcwd())
        self.order_status.toollabel_clicked.connect(partial(self.ctrl_handler, 'RemoveOrder'))
        vbox.addWidget(self.order_status)


        self.addLayout(vbox)


class producer_info(Base):

    def __init__(self):
        Base.__init__(self, 'Producer Information', 171)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.producer_list = customizedlb.toollabel('Producer List', 'List of all producers', '%s\Pics\\tool menu\producer management\producer list.png'%os.getcwd())
        self.producer_list.toollabel_clicked.connect(partial(self.ctrl_handler, 'ProducerList'))
        vbox.addWidget(self.producer_list)

        self.new_producer = customizedlb.toollabel('New Producer', 'Add a new Producer', '%s\Pics\\tool menu\producer management\\new producer.png'%os.getcwd())
        self.new_producer.toollabel_clicked.connect(partial(self.ctrl_handler, 'NewProducer'))
        vbox.addWidget(self.new_producer)

        self.modify_producer = customizedlb.toollabel('Modify Producer', 'Change producer info', '%s\Pics\\tool menu\producer management\modify producer.png'%os.getcwd())
        self.modify_producer.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyProducer'))
        vbox.addWidget(self.modify_producer)

        self.remove_producer = customizedlb.toollabel('Remove Producer', 'Remove Producer', '%s\Pics\\tool menu\producer management\\remove producer.png'%os.getcwd())
        self.remove_producer.toollabel_clicked.connect(partial(self.ctrl_handler, 'RemoveProducer'))
        vbox.addWidget(self.remove_producer)


        self.addLayout(vbox)


class kala_aghsati(Base):

    def __init__(self):
        Base.__init__(self,'Kala Aghsati', 303)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.Items_report = customizedlb.toollabel('Kala Aghasati List', 'New kala aghsati', '%s\Pics\\tool menu\kala aghsati\kala aghsati list.png'%os.getcwd())
        self.Items_report.toollabel_clicked.connect(partial(self.ctrl_handler, 'KalaAghsatiList'))
        vbox.addWidget(self.Items_report)

        self.advance_search = customizedlb.toollabel('Payment Information', 'Customer payment Information', '%s\Pics\\tool menu\kala aghsati\customer payment.png'%os.getcwd())
        self.advance_search.toollabel_clicked.connect(partial(self.ctrl_handler, 'PaymentInformation'))
        vbox.addWidget(self.advance_search)


        self.addLayout(vbox)


class report(Base):

    def __init__(self):

        Base.__init__(self, 'Report', 237)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.Items_report = customizedlb.toollabel('Items Report', 'Get report about items', '%s\Pics\\tool menu\\report\items report.png'%os.getcwd())
        self.Items_report.toollabel_clicked.connect(partial(self.ctrl_handler, 'Items Report'))
        vbox.addWidget(self.Items_report)

        self.advance_search = customizedlb.toollabel('Advance Search', 'Search Presicely', '%s\Pics\\tool menu\\report\search.png'%os.getcwd())
        self.advance_search.toollabel_clicked.connect(partial(self.ctrl_handler, 'Advance Search'))
        vbox.addWidget(self.advance_search)

        self.advance_report = customizedlb.toollabel('Advance Report', 'Get accurate report', '%s\Pics\\tool menu\\report\\advance report.png'%os.getcwd())
        self.advance_report.toollabel_clicked.connect(partial(self.ctrl_handler, 'Advance Report'))
        vbox.addWidget(self.advance_report)


        self.addLayout(vbox)


class account(Base):

    def __init__(self):
        Base.__init__(self,'Account', 159)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.new_account = customizedlb.toollabel('New Account', 'Create a new account', '%s\Pics\\tool menu\\account\\new.png'%os.getcwd())
        self.new_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'NewAccount'))
        vbox.addWidget(self.new_account)

        self.modify_account = customizedlb.toollabel('Modify Account', 'Modify an existing account', '%s\Pics\\tool menu\\account\modify.png'%os.getcwd())
        self.modify_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyAccount'))
        vbox.addWidget(self.modify_account)

        self.block_account = customizedlb.toollabel('Block Account', 'Block an account', '%s\Pics\\tool menu\\account\\block.png'%os.getcwd())
        self.block_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'BlockAccount'))
        vbox.addWidget(self.block_account)

        self.remove_account = customizedlb.toollabel('Remove Account', 'Remove an account', '%s\Pics\\tool menu\\account\\remove.png'%os.getcwd())
        self.remove_account.toollabel_clicked.connect(partial(self.ctrl_handler, 'RemoveAccount'))
        vbox.addWidget(self.remove_account)

        self.addLayout(vbox)


class setting(Base):

    def __init__(self):
        Base.__init__(self,'Setting', 171)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)


        self.network_config = customizedlb.toollabel('Network Configuration', 'Set  network IP', '%s\Pics\\tool menu\setting\\network.png'%os.getcwd())
        self.network_config.toollabel_clicked.connect(partial(self.ctrl_handler, 'NetworkConfiguration'))
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(self.network_config)
        hbox1.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox1)

        self.change_account_info = customizedlb.toollabel('Change Account Setting', 'Change Account Setting', '%s\Pics\\tool menu\setting\change info.png'%os.getcwd())
        self.change_account_info.toollabel_clicked.connect(partial(self.ctrl_handler, 'ModifyAccount'))
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.change_account_info)
        hbox2.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox2)

        self.product_activation = customizedlb.toollabel('Product Activation', 'Activate Product With License Key', '%s\Pics\\tool menu\setting\\activate.png'%os.getcwd())
        self.product_activation.toollabel_clicked.connect(partial(self.ctrl_handler, 'ProductActivation'))
        hbox3 = QtGui.QHBoxLayout()
        hbox3.addWidget(self.product_activation)
        hbox3.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox3)

        self.update_product = customizedlb.toollabel('Update Product', 'Installed Version : 1.1', '%s\Pics\\tool menu\setting\update.png'%os.getcwd())
        self.update_product.toollabel_clicked.connect(partial(self.ctrl_handler, 'UpdateProduct'))
        hbox4 = QtGui.QHBoxLayout()
        hbox4.addWidget(self.update_product)
        hbox4.setContentsMargins(6,0,0,0)
        vbox.addLayout(hbox4)

        self.addLayout(vbox)


class help(Base):

    def __init__(self):
        Base.__init__(self,'Help', 237)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()
        vbox.setContentsMargins(50, 0, 350, 20)

        self.help = customizedlb.toollabel('Help', 'Help', '%s\Pics\\tool menu\help\\help.png'%os.getcwd())
        self.help.toollabel_clicked.connect(lambda: os.system('start help.pdf'))
        vbox.addWidget(self.help)

        self.support = customizedlb.toollabel('Support', 'Get Online Help', '%s\Pics\\tool menu\help\support.png'%os.getcwd())
        self.support.toollabel_clicked.connect(partial(self.ctrl_handler, 'Support'))
        vbox.addWidget(self.support)

        self.SMS_info = customizedlb.toollabel('SMS Information', 'About System', '%s\Pics\\tool menu\help\information.png'%os.getcwd())
        self.SMS_info.toollabel_clicked.connect(partial(self.ctrl_handler, 'SMSInfo'))
        vbox.addWidget(self.SMS_info)

        self.addLayout(vbox)
