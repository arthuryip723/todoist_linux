# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_task.ui'
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

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName(_fromUtf8("AddTask"))
        AddTask.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AddTask)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(AddTask)
        self.label.setGeometry(QtCore.QRect(60, 80, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(AddTask)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(AddTask)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddTask.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        AddTask.setWindowTitle(_translate("AddTask", "Dialog", None))
        self.label.setText(_translate("AddTask", "Task Name:", None))

