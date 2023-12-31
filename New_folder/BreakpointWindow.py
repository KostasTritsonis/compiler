from PyQt6.QtWidgets import QDialog
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from PyQt6.uic import loadUi


class BreakpointWindow(QDialog):
    dataPassed = pyqtSignal(str)
    def __init__(self):
        super(BreakpointWindow,self).__init__()
        loadUi("BreakpointWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        
        self.pushButton.clicked.connect(self.accept)
       
        self.data = None
        
    def accept(self):
        self.data = self.lineEdit.text()
        self.dataPassed.emit(self.data)
        super().accept()