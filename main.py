import sys
# from PyQt4.QtGui import QApplication, QDialog, QMainWindow
# from PyQt4.QtGui import QStringListModel
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from form import Ui_Form
from add_project import Ui_Dialog
from todoist.api import TodoistAPI
from todoist.models import Project

class ProjectListModel(QAbstractListModel):
	def __init__(self, datain, parent=None, *args):
		QAbstractListModel.__init__(self, parent, *args)
		self.listdata = datain

	def rowCount(self, parent=QModelIndex()):
		return len(self.listdata)

	def data(self, index, role):
		if index.isValid() and role == Qt.DisplayRole:
			# print "up"
			# print self.listdata[index.row()].__repr__
			return QVariant(self.listdata[index.row()]["name"])
			# return QVariant(self.listdata[index.row()])
			# return QVariant("Arthur")
		else:
			# print "down"
			return QVariant()

	def itemSelected(self, index):
		# print "Index " + index.__str__ + " clicked..."
		print index.row()
		print self.listdata[index.row()]
		# print out all the information of that project
		# print index.__str__()
		# print "I am clicked"

# class MyProject(Project):
# 	def __str__(self):
# 		return self.__repr__

class MyPopup(QDialog):
# class MyPopup(QMainWindow):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        # print self
        self.ui.setupUi(self)

    def accept(self):
    	# print "custom accept..."
    	name = self.ui.lineEdit.text()
    	# create a new project here
    	p = Project({"name": str(name), "item_order": 1, "indent": 1, "color": 1}, MyForm.api)
    	# push the object to the project list
    	# Where should I place the api. Find a way to place the object globally.
    	# I should really remember how to push things to a list in pythons
    	MyForm.api.state["Projects"].append(p)
    	# print MyForm.api.state["Projects"]
    	# print res
    	# I should sync once after I've created the project
    	# with command "project_add"
    	# res = MyForm.api.sync()
    	res = MyForm.api.sync(commands=[
    		{"type": "project_add",
    		"temp_id": p.temp_id,
    		"uuid": MyForm.api.generate_uuid(),
    		"args": {"name": "Project1", "item_order": 1, "indent": 1, "color": 1}}
    		])
    	print res
    	# Get the api
    	QDialog.accept(self)

    # def paintEvent(self, e):
    #     dc = QPainter(self)
    #     dc.drawLine(0, 0, 100, 100)
    #     dc.drawLine(100, 0, 0, 100)

class MyForm(QMainWindow):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		# self.api = TodoistAPI()
		# self.api.login("arthur_yip@hotmail.com", "zmxncbv")
		MyForm.api = TodoistAPI()
		MyForm.api.login("arthur_yip@hotmail.com", "zmxncbv")
		self.api.sync(resource_types=["all"])

		# self.model = ProjectListModel(self.api.state["Projects"])
		self.model = ProjectListModel(MyForm.api.state["Projects"])
		self.ui.listView.setModel(self.model)

		self.ui.listView.clicked.connect(self.itemSelected)
		self.ui.pushButton.clicked.connect(self.addProject)

	def itemSelected(self, index):
		# print "Index " + index.__str__ + " clicked..."
		# print index.row()
		project = self.model.listdata[index.row()]
		# print project
		self.ui.textBrowser.setText(str(project))

	def contextMenuEvent(self, pos):
		print "context menu..."

	def addProject(self):
		# print "Adding project..."
		# make a popup here
		# self.w = MyPopup()
		# self.w.setGeometry(QRect(100, 100, 400, 200))
		# self.w.show()
		self.w = MyPopup()
		self.w.show()


app = QApplication(sys.argv)
# window = QMainWindow()
# ui = Ui_Form()
# ui.setupUi(window)
myForm = MyForm()

# list_data = ["1","2"]
# api = TodoistAPI()
# resp = api.login("arthur_yip@hotmail.com", "zmxncbv")
# print resp
# print api.token
# resp1 = api.sync(resource_types=["all"])
# list_data = api.state["Projects"]
# print list_data

# model = QStringListModel(list_data)
# model = ProjectListModel(list_data)
# myForm.ui.listView.setModel(model)

# myForm.ui.listView.clicked.connect(myForm.ui.listView.model().itemSelected)

# model = QStandardItemModel(1,1)
# model.setItem(0, 0, QStandardItem(QString("Arthur")))
# ui.listView.setModel(model)

# window.show()
myForm.show()
sys.exit(app.exec_())

