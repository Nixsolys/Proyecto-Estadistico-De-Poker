from src.Vista.ventana import *

class Controlador():
    def __init__(self,ventana_main,ventana2,ventana3):
        self.controlador_ventana_manin = ventana_main
        self.controlador_ventana2 = ventana2
        self.controlador_ventana3 = ventana3

        self.controlador_ventana_manin.iniciar.clicked.connect(self.next)

    def next(self):
        print("Siguiente")
        self.controlador_ventana_manin.hide()
        self.controlador_ventana2.show() #EL usuario quiere ver la ventan ()
        
        