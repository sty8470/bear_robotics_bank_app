import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Account import Account

class MainUI(QDialog):

    def __init__(self):
        super().__init__()
        self.account_obj = Account()
        self.current_balance = 0
        self.initUI()

    # method for widgets
    def initUI(self):
        self.setWindowTitle('주식회사 베어로보틱스 은행앱')
        
        self.text_v_layout = QVBoxLayout()
        self.text_h_layout = QHBoxLayout()
        msgBox = QLabel("주식회사 베어로보틱스 은행앱에 오신 여러분들을 환영합니다")
        
        self.text_button = QPushButton('Welcome to Bear Robotics Banking App')

        self.text_v_layout.addWidget(msgBox)
        self.text_h_layout.addWidget(self.text_button)

        self.text_v_layout.addLayout(self.text_h_layout)
        self.setLayout(self.text_v_layout)
        self.text_button.clicked.connect(self.textClicked)
      
        self.setFixedSize(400, 100)
        
    
    def textClicked(self):
        self.account_obj.showDialog()
    
    def showDialog(self):
        return super().exec_()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MainUI()
    window.showDialog()
    sys.exit(App.exec())
