# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_project.ui'
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

class Ui_AddProject(object):
    def setupUi(self, AddProject):
        AddProject.setObjectName(_fromUtf8("AddProject"))
        AddProject.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AddProject)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(AddProject)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(AddProject)
        self.label.setGeometry(QtCore.QRect(50, 70, 59, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(AddProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddProject.reject)
        QtCore.QMetaObject.connectSlotsByName(AddProject)

    def retranslateUi(self, AddProject):
        AddProject.setWindowTitle(_translate("AddProject", "Dialog", None))
        self.label.setText(_translate("AddProject", "Name", None))

