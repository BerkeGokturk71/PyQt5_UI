from PyQt5.QtWidgets import *
from quest2 import Ui_Question


# Soru penceresinin açılmasını sağlayan Python kodları. 

class Quest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quest = Ui_Question()
        self.quest.setupUi(self)