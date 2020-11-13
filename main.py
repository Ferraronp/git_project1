import sys
import sqlite3

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class EditCoffe_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 225)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 491, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 250)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 4, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setProperty("value", 250)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(430, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "taste"))
        self.label_3.setText(_translate("Form", "ground"))
        self.label_5.setText(_translate("Form", "price"))
        self.label.setText(_translate("Form", "name"))
        self.label_2.setText(_translate("Form", "degree"))
        self.label_6.setText(_translate("Form", "size"))
        self.pushButton.setText(_translate("Form", "Добавить"))


class Main_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 510)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 480, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить"))


class EditCoffee(QWidget, EditCoffe_Form):
    def __init__(self, ex):
        self.ex = ex
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect("data\\coffee.sqlite")
        cur = con.cursor()
        degrees = list(map(lambda x: x[0], cur.execute("""SELECT degree FROM degrees""").fetchall()))
        con.close()
        self.comboBox.addItems(degrees)
        self.comboBox_2.addItems(["В зёрнах", "Молотый"])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect("data\\coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT id FROM coffee""").fetchall()
        id = result[-1][0] + 1
        con.close()

        name = self.lineEdit.text()
        degree = self.comboBox.currentIndex() + 1
        ground = self.comboBox_2.currentIndex()
        taste = self.lineEdit_2.text()
        price = self.spinBox.value()
        size = self.spinBox_2.value()
        con = sqlite3.connect("data\\coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""INSERT INTO coffee
         VALUES({}, {}, {}, {}, {}, {}, {})""".format(
            id, name, degree, ground, taste, price, size
        ))
        con.commit()
        con.close()

        self.ex.initUI()
        self.hide()


class Example(QWidget, Main_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')

        db.setDatabaseName('data\\coffee.sqlite')

        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.tableView.setModel(model)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.ex = EditCoffee(self)
        self.ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
