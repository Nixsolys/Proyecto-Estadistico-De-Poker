#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from src.Vista.ventana_menu import Ventanamenu
from src.Vista.ventana_principal import Ventana
from src.Vista.ventana_configuracion import VConfiguracion
from src.Controlador.controlador import*
from src.Modelo.baraja import*
from src.Modelo.cartas import*
from src.Modelo.Jugador import*
from src.Modelo.mano import*

#Administrador
app = QApplication(sys.argv)


#Ventanas
menu = Ventanamenu()
configuracion = VConfiguracion()
ventana_principal = Ventana(menu,configuracion)
controlador = Controlador(ventana_principal)
ventana_principal.show()

#Modelo
Baraja_mesa = Baraja()
Baraja_mesa.crear_baraja()

#mano

#Jugador
Jugador = Jugador("Camilo")
Jugador.jugador_mano(Baraja_mesa)

print(len(Baraja_mesa.baraja))
sys.exit(app.exec())
