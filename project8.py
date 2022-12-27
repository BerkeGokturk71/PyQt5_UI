from PyQt5.QtWidgets import *
from project6 import Ui_SecondWindow


# Devre penceresinin açılmasını sağlayan Pyhton kodları. 

class Second(QMainWindow):
    def __init__(self):
        super().__init__()
        self.two = Ui_SecondWindow()
        self.two.setupUi(self)
        
        



    