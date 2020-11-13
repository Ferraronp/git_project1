import sys

from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())