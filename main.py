import sys
# from PyQt4.QtGui import QApplication, QDialog, QMainWindow
# from PyQt4.QtGui import QStringListModel
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from form import Ui_Form
from add_project import Ui_AddProject
from add_task import Ui_AddTask
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
		pass
		# print "Index " + index.__str__ + " clicked..."
		# print index.row()
		# print self.listdata[index.row()]
		# print out all the information of that project
		# print index.__str__()
		# print "I am clicked"

class ItemListModel(QAbstractListModel):
	def __init__(self, datain, parent=None, *args):
		QAbstractListModel.__init__(self, parent, *args)
		self.listdata = datain

	def rowCount(self, parent=QModelIndex()):
		return len(self.listdata)

	def data(self, index, role):
		if index.isValid() and role == Qt.DisplayRole:
			return QVariant(self.listdata[index.row()]["content"])
		else:
			return QVariant()

	def itemSelected(self, index):
		pass

# class MyProject(Project):
# 	def __str__(self):
# 		return self.__repr__

class MyPopup(QDialog):
# class MyPopup(QMainWindow):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_AddProject()
        # print self
        self.ui.setupUi(self)

    def accept(self):
    	# print "custom accept..."
    	# you sync with adding a project, the api will take care of everything after you sync.
    	MyForm.projectModel.beginInsertRows(QModelIndex(), len(MyForm.api.state["Projects"]), len(MyForm.api.state["Projects"]))
    	# print "--------------------------"
    	name = self.ui.lineEdit.text()
    	# create a new project here
    	p = Project({"name": str(name), "item_order": 1, "indent": 1, "color": 1}, MyForm.api)
    	# push the object to the project list
    	# Where should I place the api. Find a way to place the object globally.
    	# I should really remember how to push things to a list in pythons
    	# MyForm.api.state["Projects"].append(p)
    	# print MyForm.api.state["Projects"]
    	# print res
    	# I should sync once after I've created the project
    	# with command "project_add"
    	# res = MyForm.api.sync()
    	res = MyForm.api.sync(commands=[
    		{"type": "project_add",
    		"temp_id": p.temp_id,
    		"uuid": MyForm.api.generate_uuid(),
    		"args": {"name": str(name), "item_order": 1, "indent": 1, "color": 1}}
    		])
    	MyForm.api.sync(resource_types=["all"])
    	# print res
    	# print "--------------------------"
    	# print MyForm.api.state["Projects"]
    	MyForm.projectModel.endInsertRows()
    	# Get the api
    	QDialog.accept(self)

    # def paintEvent(self, e):
    #     dc = QPainter(self)
    #     dc.drawLine(0, 0, 100, 100)
    #     dc.drawLine(100, 0, 0, 100)

class AddTaskPopup(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.ui = Ui_AddTask()
		self.ui.setupUi(self)

	def accept(self):
		print "creating task..."
		QDialog.accept(self)

class MyForm(QMainWindow):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		# self.api = TodoistAPI()
		# self.api.login("arthur_yip@hotmail.com", "zmxncbv")
		MyForm.api = TodoistAPI()
		MyForm.api.login("arthur_yip@hotmail.com", "zmxncbv")
		res = MyForm.api.sync(resource_types=["all"])
		# print res
		MyForm.seq_no = res["seq_no"]

		# self.model = ProjectListModel(self.api.state["Projects"])
		# self.model = ProjectListModel(MyForm.api.state["Projects"])
		MyForm.projectModel = ProjectListModel(MyForm.api.state["Projects"])
		# self.ui.projectsView.setModel(self.model)
		self.ui.projectsView.setModel(MyForm.projectModel)

		self.ui.projectsView.clicked.connect(self.itemSelected)
		self.ui.pushButton.clicked.connect(self.addProject)
		self.ui.addTaskButton.clicked.connect(self.addTask)
		self.ui.refreshBtn.clicked.connect(self.refresh)

	def itemSelected(self, index):
		# print "Index " + index.__str__ + " clicked..."
		# print index.row()
		# project = self.model.listdata[index.row()]
		project = MyForm.projectModel.listdata[index.row()]
		details = MyForm.api.get_project(project["id"])

		# items = MyForm.api.get_completed_items(project["id"])
		# print items
		# print MyForm.api.state["Items"]
		items = MyForm.api.state["Items"]
		relavant_items = [x for x in items if x["project_id"] == project["id"]]
		self.ui.projectName.setText(project["name"])
		print relavant_items
		# set the view with selected items
		MyForm.itemsModel = ItemListModel(relavant_items)
		self.ui.itemsView.setModel(MyForm.itemsModel)
		# print details
		# print project
		# load all the items
		self.ui.textBrowser.setText(str(project))

	def contextMenuEvent(self, pos):
		# print "context menu..."
		pass

	def addProject(self):
		# print "Adding project..."
		# make a popup here
		# self.w = MyPopup()
		# self.w.setGeometry(QRect(100, 100, 400, 200))
		# self.w.show()
		self.w = MyPopup()
		self.w.show()

	def addTask(self):
		self.w = AddTaskPopup()
		self.w.show()

	def refresh(self):
		# res = MyForm.api.sync(resource_types=["all"])
		# print "---------------"
		# print MyForm.api.seq_no
		# MyForm.api.seq_no = 0
		# print MyForm.api.state
		# res = MyForm.api.sync(resource_types=["all"])
		# print res
		# print MyForm.api.state["Projects"]
		# print self.ui.projectsView.model().listdata
		model = self.ui.projectsView.model()
		# self.ui.projectsView.model().dataChanged.emit()
		index = model.index(5)
		model.dataChanged.emit(index, index)


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
# myForm.ui.projectsView.setModel(model)

# myForm.ui.projectsView.clicked.connect(myForm.ui.projectsView.model().itemSelected)

# model = QStandardItemModel(1,1)
# model.setItem(0, 0, QStandardItem(QString("Arthur")))
# ui.projectsView.setModel(model)

# window.show()
myForm.show()
sys.exit(app.exec_())

