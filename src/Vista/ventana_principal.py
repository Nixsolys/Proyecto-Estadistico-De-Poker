from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

class Ventana(QMainWindow):

    def __init__(self,menu,configuracion):
        super().__init__()
#atributos      
        self.configuracion = configuracion
        self.menu = menu
        self.setCentralWidget(self.menu)


        BASE_DIR = Path(__file__).resolve().parent.parent.parent #ObjetoTipoPath

#Direcciones - Las confioguramos asi para que pueda funcionar donde se ejecute el programa

        logo_path = BASE_DIR / "resources" / "logotipos" / "Logotipo3PSinFondo.png"

#Configuración de ventana
        self.setWindowTitle("Proyect - Poker - probability")
        self.setWindowIcon(QIcon(str(logo_path)))
        self.setFixedSize(1200, 600) #<-- Tamaño fijo de la ventana

#capas
        self.capa_main = QStackedWidget()

        self.capa_main.addWidget(self.menu)
        self.capa_main.addWidget(self.configuracion)

        self.setCentralWidget(self.capa_main)

"""
♠		
♥		
♣	
♦	
♤	
♡	
♧	
♢	
"""