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

print("VENTANA MOSTRADA")
print(ventana_principal.isVisible())

#Modelo
Baraja_mesa = Baraja()
Baraja_mesa.crear_baraja()

#mano
mano1 = Mano()

#Jugador
Jugador1 = Jugador("EMEL")
Jugador1.jugador_mano(Baraja_mesa)

Jugador3 = Jugador("BRAYAN")
Jugador3.jugador_mano(Baraja_mesa)

#Mesa
mesa = Mesa(Baraja_mesa)
mesa.colocar_carta()
mesa.colocar_carta()
mesa.colocar_carta()
Baraja_mesa.imprimir_mazo()

print(len(Baraja_mesa.baraja))
sys.exit(app.exec())
