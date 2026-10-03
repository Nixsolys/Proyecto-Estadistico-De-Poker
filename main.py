#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from src.Vista.ventana_menu import Ventanamenu
from src.Vista.ventana_principal import Ventana
from src.Vista.ventana_configuracion import VConfiguracion
from src.Vista.ventana_juego import VentanaJuego
from src.Controlador.controlador import*
from src.Modelo.baraja import*
from src.Modelo.cartas import*
from src.Modelo.Jugador import*
from src.Modelo.mano import*
from src.Modelo.mesa import*

#Administrador
app = QApplication(sys.argv)


#Ventanas
menu = Ventanamenu()
configuracion = VConfiguracion()
juego = VentanaJuego()
ventana_principal = Ventana(menu,configuracion,juego)
controlador = Controlador(ventana_principal)

ventana_principal.show()

sys.exit(app.exec())
