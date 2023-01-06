import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Balance import Balance

import os
import json 

class Withdraw(QDialog):

    def __init__(self):
        super().__init__()
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.config_file_path = os.path.normpath(os.path.join(self.current_path, 'config.json'))
        self.balance = Balance()
        self.initUI()

    # method for widgets
    def initUI(self):
        self.setWindowTitle('출금하기')
        
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QLabel("얼마나 출금하기 원하시는지 입력해주세요")
        
        self.deposit_amount = QLineEdit()
        self.submit_button = QPushButton('출금')

        self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.deposit_amount)
        self.text_h_layout.addWidget(self.submit_button)

        self.text_v_layout.addLayout(self.text_h_layout)
        self.submit_button.clicked.connect(self.accept)
        self.setLayout(self.text_v_layout)
      
        self.setFixedSize(300, 100)
        
    def get_balance(self):
        with open(self.config_file_path) as data:
            self.current_balance = json.load(data)
            return float(self.current_balance['balance'])

    def set_balance(self):
        add_balance = float(self.deposit_amount.text())
        new_balance = self.get_balance() - add_balance
        if add_balance > self.get_balance():
            QMessageBox.warning(self, "잔금 부족경고", "출금하실 금액이 현재 잔고를 초과합니다!")
       
        else:
            self.balance.current_balance = new_balance
            with open(self.config_file_path, 'w') as f:
                balance_dict = {'balance': new_balance}
                json.dump(balance_dict, f)
            QMessageBox.information(self, "Information", "출금이 완료되었습니다")
            
    def accept(self):
        self.set_balance()
        self.done(1)
    
    def showDialog(self):
        return super().exec_()