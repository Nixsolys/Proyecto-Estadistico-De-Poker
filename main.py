#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication
from src.Vista.ventana_menu import Ventanamenu
from src.Vista.ventana_principal import Ventana
from src.Vista.ventana_configuracion import VConfiguracion
from src.Vista.ventana_juego import VentanaJuego
from src.Vista.ventana_graficos import VentanaGrafica

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
graficas = VentanaGrafica()
ventana_principal = Ventana(menu,configuracion,juego,graficas)
controlador = Controlador(ventana_principal)

ventana_principal.show()

sys.exit(app.exec())
