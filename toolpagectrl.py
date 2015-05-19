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


class home(base):
    
    def __init__(self):
        
        base.__init__(self, 'Home',20)
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

        base.__init__(self, 'Employee Management', 270)
        self.construct()

    def construct(self):

        vbox = QtGui.QVBoxLayout()

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

    def ctrl_handler(self, toolname):

        print '%s clicked'%toolname


class account(base):

    def __init__(self):
        base.__init__(self,'Not created account page', 489)


class item_management(base):

    def __init__(self):
        base.__init__(self,'Not created item mgt page', 489)


class order_management(base):

    def __init__(self):
        base.__init__(self,'Not created order mgt page', 489)


class producer_info(base):

    def __init__(self):
        base.__init__(self,'Not created personal info page', 489)


class kala_aghsati(base):

    def __init__(self):
        base.__init__(self,'Not created kala aghsati page', 489)


class report(base):

    def __init__(self):
        base.__init__(self,'Not created report page', 489)


class setting(base):

    def __init__(self):
        base.__init__(self,'Not created setting page', 489)


class help(base):

    def __init__(self):
        base.__init__(self,'Not created help page', 489)
