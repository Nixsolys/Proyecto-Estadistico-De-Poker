#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from src.Vista.ventana_menu import Ventanamenu
from src.Vista.ventana_principal import Ventana
from src.Vista.ventana_configuracion import VConfiguracion
from src.Controlador.controlador import*

app = QApplication(sys.argv)

menu = Ventanamenu()
configuracion = VConfiguracion()
ventana1 = Ventana(menu,configuracion)
controlador = Controlador(ventana1)
ventana1.show()

sys.exit(app.exec())
