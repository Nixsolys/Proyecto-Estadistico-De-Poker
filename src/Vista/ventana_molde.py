from PySide6.QtWidgets import *
from pathlib import Path
from PySide6.QtGui import QIcon

class VentanaMolde(QWidget):
    def __init__(self):
            super().__init__()

            print("VentanMolde")
    
            BASE_DIR = Path(__file__).resolve().parent.parent.parent
    
            #Direcciones
            logo_path = BASE_DIR / "resources" / "logotipos" / "Logotipo3PSinFondo.png"
    
            # Configuración de ventana
            self.setWindowTitle("Proyect - Poker - probability")
            self.setWindowIcon(QIcon(str(logo_path)))
            self.setFixedSize(1200, 600) #<-- Tamaño fijo de la ventana