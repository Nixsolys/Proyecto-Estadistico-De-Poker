from src.Vista.ventana_menu import *
from src.Modelo.Jugador import *

class Controlador():
    def __init__(self,ventana_main):
        self.controlador_ventana_main = ventana_main

        self.controlador_ventana_main.menu.iniciar.clicked.connect(self.next)
        self.controlador_ventana_main.configuracion.añadir_jugador.clicked.connect(self.crear_jugador)

    def next(self):
        
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.controlador_ventana_main.configuracion)
        
    def crear_jugador(self):
        Jugador1 = Jugador(self.controlador_ventana_main.configuracion.nombre.text())