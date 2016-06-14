# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.projectsView = QtGui.QListView(Form)
        self.projectsView.setGeometry(QtCore.QRect(70, 50, 256, 192))
        self.projectsView.setObjectName(_fromUtf8("projectsView"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 300, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 260, 113, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.refreshBtn = QtGui.QPushButton(Form)
        self.refreshBtn.setGeometry(QtCore.QRect(210, 260, 113, 32))
        self.refreshBtn.setObjectName(_fromUtf8("refreshBtn"))
        self.projectName = QtGui.QLabel(Form)
        self.projectName.setGeometry(QtCore.QRect(410, 10, 91, 16))
        self.projectName.setObjectName(_fromUtf8("projectName"))
        self.itemsView = QtGui.QListView(Form)
        self.itemsView.setGeometry(QtCore.QRect(410, 50, 256, 192))
        self.itemsView.setObjectName(_fromUtf8("itemsView"))
        self.taskNameEdit = QtGui.QLineEdit(Form)
        self.taskNameEdit.setGeometry(QtCore.QRect(410, 280, 251, 21))
        self.taskNameEdit.setObjectName(_fromUtf8("taskNameEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 260, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.addTaskButton = QtGui.QPushButton(Form)
        self.addTaskButton.setGeometry(QtCore.QRect(410, 320, 113, 32))
        self.addTaskButton.setObjectName(_fromUtf8("addTaskButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Add Project", None))
        self.refreshBtn.setText(_translate("Form", "Refresh", None))
        self.projectName.setText(_translate("Form", "Project Name", None))
        self.label.setText(_translate("Form", "New Task Name:", None))
        self.addTaskButton.setText(_translate("Form", "Add Task", None))

