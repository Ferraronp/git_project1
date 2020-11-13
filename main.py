import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class EditCoffee(QWidget):
    def __init__(self, ex):
        self.ex = ex
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        degrees = list(map(lambda x: x[0], cur.execute("""SELECT degree FROM degrees""").fetchall()))
        con.close()
        self.comboBox.addItems(degrees)
        self.comboBox_2.addItems(["В зёрнах", "Молотый"])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect("coffee.sqlite")
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
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""INSERT INTO coffee
         VALUES({}, {}, {}, {}, {}, {}, {})""".format(
            id, name, degree, ground, taste, price, size
        ))
        con.commit()
        con.close()

        self.ex.initUI()
        self.hide()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')

        db.setDatabaseName('coffee.sqlite')

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