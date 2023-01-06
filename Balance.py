from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
import json

class Balance(QDialog):

    def __init__(self):
        super().__init__()
        self.current_path = os.path.dirname(os.path.realpath(__file__))  
        self.config_file_path = os.path.normpath(os.path.join(self.current_path, 'config.json'))
        self.current_balane = 0
        self.change_balance = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('현재 잔금확인')
        
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        
        self.balance_label = QLabel('Your current balance is ${}'.format(self.get_balance()))
        self.text_h_layout.addWidget(self.balance_label)

        self.text_v_layout.addLayout(self.text_h_layout)
        self.setLayout(self.text_v_layout)
      
        self.setFixedSize(200, 100)
    
    def get_balance(self):
        if self.change_balance == None:
            with open(self.config_file_path) as data:
                self.current_balance = json.load(data)
                return float(self.current_balance['balance'])
    
    def showDialog(self):
        return super().exec_()

