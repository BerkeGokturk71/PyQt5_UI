from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator
from uidesigner import Ui_MainWindow
from project8 import Second
from PyQt5.QtCore import pyqtSignal
from hazirliyan_yansit import Hazir
from quest2_yansit import Quest


class Main(QMainWindow):
    sinyal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.pencereac = Second()
        
        self.ui.Button.clicked.connect(self.math)
        self.ui.isemler_hakkinda_2.triggered.connect(self.hazir_pencere)  # hazırlayanlar sekmesine tıklandığında karşımıza çıkması için. 
        self.ui.actionQuestion.triggered.connect(self.soru)  # question sekmesine tıklandığında karşımıza çıkması için.

    def soru(self):
        self.quest = Quest()
        self.quest.show()

    def hazir_pencere(self):
        self.hakkinda_ac = Hazir()
        self.hakkinda_ac.show()
        
           
    def math(self):

        try:  # try-except bloğu bizlere boş değer girilmesi, eksik veri girilmesi durumunda hata ayıklamamızı sağlar.
            
            
            self.pencereac.show()
            
            self.ui.lineEdit_1.setValidator(QIntValidator(0,2147483647,self)) 
            self.ui.lineEdit_2.setValidator(QIntValidator(0,999999,self))
            self.ui.lineEdit_3.setValidator(QIntValidator(0,999999,self))
            self.ui.lineEdit_4.setValidator(QIntValidator(0,999999,self))
            self.ui.lineEdit_5.setValidator(QIntValidator(0,999999999,self))
        
        # değerleri text methodu ile çekmemizi sağlıyor.

            received_Line1 = float(self.ui.lineEdit_1.text()) 
            received_Line2 = float(self.ui.lineEdit_2.text())
            received_Line3 = float(self.ui.lineEdit_3.text())
            received_Line4 = float(self.ui.lineEdit_4.text())
            received_Line5 = float(self.ui.lineEdit_5.text()) 
            received_Line6 = float(self.ui.lineEdit_6.text()) 
            received_Line7 = float(self.ui.lineEdit_7.text()) 
            received_Line8 = float(self.ui.lineEdit_8.text()) 
        
        # matematiksel işlemlerin yapılması ve veri dönüşümleri

            math_calculator1 = float(received_Line2**2/received_Line1)
            math_calculator2 = float(received_Line3**2/received_Line1)
            math_calculator3 = str(received_Line4/math_calculator1)[0:7] # ilk 6 rakamı alınmasını sağlar
            math_calculator4 = str(received_Line5/math_calculator2)[0:7]
            math_calculator5 = str(received_Line6/math_calculator1)[0:7]
            math_calculator6 = str(received_Line7/math_calculator1)[0:7]
            math_calculator7 = str(received_Line8/math_calculator2)[0:7]

        # hesaplanan değerlerin devre üzerinde dinamik olarak gözükmesini yansıtır.

            self.pencereac.two.label_55.setText(str(math_calculator3))
            self.pencereac.two.label_56.setText(str(math_calculator4))
            self.pencereac.two.label_57.setText(str(math_calculator5))
            self.pencereac.two.label_58.setText(str(math_calculator6))
            self.pencereac.two.label_59.setText(str(math_calculator7))         
            

        except ValueError: 
        # hata mesajını veren sekmenin açılmasını sağlar
            self.pencereac.close()
            msn = QMessageBox()
            msn.setIcon(QMessageBox.Warning)
            msn.setText("Please Enter Value to Line ")
            msn.setWindowTitle("Error!")
            msn.show()
            msn.exec_()
            
uygulama = QApplication([])
pencere = Main()
pencere.setWindowTitle("Solutions For The Transformer Questions")
pencere.move(50,50) #ekranın üzerindeki konumu belirliyor.
pencere.show()
uygulama.exec_()    # programın kapatılmasında sorun çıkmamasını sağlıyor.