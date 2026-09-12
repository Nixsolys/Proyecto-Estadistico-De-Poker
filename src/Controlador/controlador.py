from src.Vista.ventana_menu import *
from src.Modelo.Jugador import *

#La tarea de esta clase es administrar y comunicar los distintos modulos, con el fin
#De cada modulo se centre unicamente en sus labores, por ejemplo que la vista no este saturada 
#Con funciones de crear jugadores

class Controlador():
    def __init__(self,ventana_main):

    #Ventana - para conectarla con el controlador
        self.controlador_ventana_main = ventana_main

    #Funciones que conectan los botones, con el controlador
        #pasar pagina
        self.controlador_ventana_main.menu.iniciar.clicked.connect(self.next)
        #Crear y añadir jugador a la lista
        self.controlador_ventana_main.configuracion.añadir_jugador.clicked.connect(self.crear_jugador)
        #Eliminar jugadores
        self.controlador_ventana_main.configuracion.eliminar_jugador.clicked.connect(self.eliminar_jugador)

    #Lista de jugadores
        self.lista_jugadores = []

#Cambiar pagina
    def next(self):
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.controlador_ventana_main.configuracion)

#Crear jugador
    def crear_jugador(self):
        
            Jugador1 = Jugador(self.controlador_ventana_main.configuracion.nombre.text())

            self.controlador_ventana_main.configuracion.lista_jugadores.addItem(Jugador1.nombre)
            self.lista_jugadores.append(Jugador1) # <--- Gurdar jugador
            print(self.lista_jugadores)

#Eliminar jugador
    def eliminar_jugador(self):

        posicion_jugador_lista = self.controlador_ventana_main.configuracion.lista_jugadores.currentRow() #Esta funcion devuelve la posicion del elemento selecionado
        self.lista_jugadores.pop(posicion_jugador_lista) #Eliminar de la lista "self.lista_jugadores = []" 
        self.controlador_ventana_main.configuracion.lista_jugadores.takeItem(posicion_jugador_lista) #Eliminar de la lista visual
        print(self.lista_jugadores)
        