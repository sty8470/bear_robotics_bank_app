from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Add import Add

class Deposit(QDialog):

    def __init__(self):
        super().__init__()
        self.add_obj = Add()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('예금[예치]')
        
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QLabel("어떤 방식으로 예금하시기를 원하나요? ")
        
        self.cash_button = QPushButton('Cash')
        self.check_button = QPushButton('Check')
        self.deposit_amount = QLineEdit('Enter amount ..')

        self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.cash_button)
        self.text_h_layout.addWidget(self.check_button)

        self.text_v_layout.addLayout(self.text_h_layout)
        self.setLayout(self.text_v_layout)
        
        self.cash_button.clicked.connect(self.cashTextClicked)
        self.check_button.clicked.connect(self.checkTextClicked)
      
        self.setFixedSize(300, 100)
    
    def cashTextClicked(self):
        self.add_obj.showDialog()
    
    def checkTextClicked(self):
        self.add_obj.showDialog()
    
    def showDialog(self):
        return super().exec_()
