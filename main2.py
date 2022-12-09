import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import uic


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main2.ui", self)
        self.setFixedSize(800, 300)
        self.table = QtWidgets.QTableView()
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = [('ID', 'название сорта', 'обжарка', 'обработка',
                'описание вкуса', 'цена', 'объем упаковки')]
        data.extend(cur.execute("""SELECT * FROM coffee""").fetchall())
        con.close()
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
