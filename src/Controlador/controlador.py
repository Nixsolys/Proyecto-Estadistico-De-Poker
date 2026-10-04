from src.Vista.ventana_menu import *
from src.Modelo.Jugador import *
from src.Modelo.baraja import *

#La tarea de esta clase es administrar y comunicar los distintos modulos, con el fin
#De cada modulo se centre unicamente en sus labores, por ejemplo que la vista no este saturada 
#Con funciones de crear jugadores

class Controlador():
    def __init__(self,ventana_main):

    #Ventanas
        self.controlador_ventana_main = ventana_main #Ventana - para conectarla con el controlador
        self.v_menu = self.controlador_ventana_main.menu #Ventana menu principal
        self.v_config = self.controlador_ventana_main.configuracion #Ventana de la configuracion
        self.v_juego = self.controlador_ventana_main.juego #Ventana del juego

        self.lista_jugadores = []
        self.jugador_actual = []
        self.baraja_main = Baraja()
        self.baraja_main.crear_baraja()

    #Funciones que conectan los botones de las distintas ventanas, con el controlador

        #Menu
        self.v_menu.iniciar.clicked.connect(self.next) #pasar pagina

        #Configuración
        self.v_config.añadir_jugador.clicked.connect(self.crear_jugador) #Crear y añadir jugador a la lista
        self.v_config.eliminar_jugador.clicked.connect(self.eliminar_jugador) #Eliminar jugadores
        self.v_config.iniciar_juego.clicked.connect(self.iniciar_juego) #Iniciar juego

        #Juego
        self.v_juego.boton_next_player.clicked.connect(self.siguiente_jugador)



#Cambiar pagina
    def next(self):
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.v_config)

#Crear jugador
    def crear_jugador(self):

        if len(self.lista_jugadores) > 0: #Comprobar si hay mas de un jugador
            contador = 0
            for i in self.lista_jugadores: #Iterar en la lista de jugadores
                if i.nombre == self.v_config.nombre.text(): #Comprobar que no sea igual el nombre
                    print("No se puede crear jugadores con nombres iguales")
                    contador = 1
                    
            if contador != 1: #Crear el jugador una vez se pase el filtro
                print("Se añade el jugador")
                Jugador1 = Jugador(self.v_config.nombre.text())

                self.v_config.lista_jugadores.addItem(Jugador1.nombre)
                self.lista_jugadores.append(Jugador1) # <--- Gurdar jugador
        else:
            print("Se añade el jugador") #Crear el primer jugador
            Jugador1 = Jugador(self.v_config.nombre.text())

            self.v_config.lista_jugadores.addItem(Jugador1.nombre)
            self.lista_jugadores.append(Jugador1) # <--- Gurdar jugador
            print(self.lista_jugadores)


#Eliminar jugador
    def eliminar_jugador(self):
            posicion_jugador_lista = self.v_config.lista_jugadores.currentRow()

            # Comprobar si hay un jugador seleccionado
            if posicion_jugador_lista == -1:
                print("Selecciona un jugador para eliminar")
                return #Para romper la funcion en caso de que no se haya selecionado ningun jugador

            # Eliminar de la lista de jugadores
            self.lista_jugadores.pop(posicion_jugador_lista)

            # Eliminar de la lista visual
            self.v_config.lista_jugadores.takeItem(posicion_jugador_lista)

#Iniciar juego
    def iniciar_juego(self):
        if len(self.lista_jugadores) < 2:
            print("No hay suficientes jugadores para iniciar el juego (Minimo 2)")
        else:
            self.controlador_ventana_main.capa_main.setCurrentWidget(self.v_juego)

            for i in self.lista_jugadores: #Crear mano para cada jugador
                i.jugador_mano(self.baraja_main) 

            self.jugador_actual.append(self.lista_jugadores[0])
            self.v_juego.texto_nombre.setText(self.lista_jugadores[0].nombre)

    def siguiente_jugador(self):

        posicion =  self.lista_jugadores.index(self.jugador_actual[0])

        if self.lista_jugadores[posicion] == self.lista_jugadores[-1]:
            jugador = self.lista_jugadores[0]
            self.jugador_actual[0] = jugador
        else:
            jugador = self.lista_jugadores[posicion+1]
            self.jugador_actual[0] = jugador

        self.v_juego.texto_nombre.setText(jugador.nombre)

        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        carta = BASE_DIR / "resources" / "componentes" / "cartas" / jugador.mano[0].fotocarta

        self.v_juego.label_mano1.setPixmap(QPixmap(str(carta)))
        self.v_juego.label_mano1.setFixedSize(300, 200)
        self.v_juego.label_mano1.setScaledContents(True)

