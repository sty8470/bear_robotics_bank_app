from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Balance import Balance 
from Deposit import Deposit 
from Withdraw import Withdraw

class Account(QDialog):

    def __init__(self):
        super().__init__()
        current_balance = 100
        self.balance_obj = Balance()
        self.deposit_obj = Deposit()
        self.withdraw_obj = Withdraw()
      
        self.initUI()

    def initUI(self):
        self.setWindowTitle('사용자 계좌창구')
        
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QLabel("어떤 용무를 보기를 원하시나요? 선택해주세요")
        
        self.balance_button = QPushButton('Check Balance')
        self.deposit_button = QPushButton('Deposit')
        self.withdraw_button = QPushButton('Withdraw')

        self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.balance_button)
        self.text_h_layout.addWidget(self.deposit_button)
        self.text_h_layout.addWidget(self.withdraw_button)

        self.text_v_layout.addLayout(self.text_h_layout)
        self.setLayout(self.text_v_layout)
        
        self.balance_button.clicked.connect(self.balanceTextClicked)
        self.deposit_button.clicked.connect(self.depositTextClicked)
        self.withdraw_button.clicked.connect(self.withdrawTextBlicked)
      
        self.setFixedSize(300, 100)
        
    def balanceTextClicked(self):
        self.balance_obj.showDialog()
    
    def depositTextClicked(self):
        self.deposit_obj.showDialog()
    
    def withdrawTextBlicked(self):
        self.withdraw_obj.showDialog()
    
    def showDialog(self):
        return super().exec_()

