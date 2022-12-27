from PyQt5.QtWidgets import *
from hazirliyanlar import Ui_Hazirliyan


# hazırlayanlar penceresi oluşturmak için yazıldı
class Hazir(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hazir = Ui_Hazirliyan()
        self.hazir.setupUi(self)

    