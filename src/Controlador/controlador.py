from src.Vista.ventana_menu import *

class Controlador():
    def __init__(self,ventana_main):
        self.controlador_ventana_main = ventana_main

        self.controlador_ventana_main.menu.iniciar.clicked.connect(self.next)

    def next(self):
        
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.controlador_ventana_main.configuracion)
        
        