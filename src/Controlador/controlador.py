from src.Vista.ventana_menu import *
from src.Modelo.Jugador import *
from src.Modelo.baraja import *
from PySide6.QtGui import QPixmap
from src.Modelo.mesa import *
from src.Vista.ventan_selector import SelectorCartas
"""
La tarea de esta clase es administrar y comunicar los distintos modulos, con el fin
De cada modulo se centre unicamente en sus labores, por ejemplo que la vista no este saturada 
Con funciones de crear jugadores"""

class Controlador():
    def __init__(self,ventana_main):

    #Ventanas
        self.controlador_ventana_main = ventana_main #Ventana principal - para conectarla con el controlador
        self.v_menu = self.controlador_ventana_main.menu #Ventana menu principal
        self.v_config = self.controlador_ventana_main.configuracion #Ventana de la configuracion
        self.v_juego = self.controlador_ventana_main.juego #Ventana del juego
        self.v_graficas = self.controlador_ventana_main.grafica #Ventana de las graficas

    #Atributos
        self.lista_jugadores = []
        self.jugador_actual = []

        self.baraja_main = Baraja()
        self.baraja_main.crear_baraja()

        self.mesa = Mesa(self.baraja_main)
    
    #Direccion raiz
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent

    #Funciones que conectan los botones de las distintas ventanas, con el controlador

        #Menu
        self.v_menu.iniciar.clicked.connect(self.next) #pasar pagina

        #Configuración
        self.v_config.añadir_jugador.clicked.connect(self.crear_jugador) #Crear y añadir jugador a la lista
        self.v_config.eliminar_jugador.clicked.connect(self.eliminar_jugador) #Eliminar jugadores
        self.v_config.iniciar_juego.clicked.connect(self.iniciar_juego) #Iniciar juego

        #Juego
        self.v_juego.boton_next_player.clicked.connect(self.siguiente_jugador) #Mostrar datos del sigueinte jugador
        self.v_juego.boton_baraja.clicked.connect(self.ponerMesa_ramdon) #Colocar cartas en la mesa

        self.v_juego.boton_baraja.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu) #Conecta el boton con click derecho
        self.v_juego.boton_baraja.customContextMenuRequested.connect(self.v_juego.abrir_menu_cartas) #Click derecho se conecta con esa funcion
        self.v_juego.señal_mesa.connect(self.seleccionarCarta_mesa)
        self.v_juego.señal_jugador.connect(self.seleccionarCarta_jugador)
        self.v_juego.señal_repartir.connect(self.repartirMano_ramdon)

        self.v_juego.boton_resultados.clicked.connect(self.resultados)

# -------------------------------------------------- METODOS --------------------------------------------------------------------

#Pagina 1 - Menu de entrada

    #Cambiar pagina 
    def next(self): #Menu --> Configuracion 
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.v_config)

#Pagina 2 - Configuracion

    def crear_jugador(self):
        if len(self.lista_jugadores) > 0: #Comprobar si hay mas de un jugador
            contador = 0
            for i in self.lista_jugadores: #Iterar en la lista de jugadores
                if i.nombre == self.v_config.nombre.text(): #Comprobar que no sea igual el nombre
                    print("No se puede crear jugadores con nombres iguales")
                    contador = 1
                    
            if contador != 1: #Crear el jugador una vez se pase el filtro
                Jugador1 = Jugador(self.v_config.nombre.text())
                
                self.v_config.lista_jugadores.addItem(Jugador1.nombre)
                self.lista_jugadores.append(Jugador1) # <--- Gurdar jugador en la variable de lista de jugadores

        else:
            #Crear el primer jugador
            Jugador1 = Jugador(self.v_config.nombre.text())

            self.v_config.lista_jugadores.addItem(Jugador1.nombre)
            self.lista_jugadores.append(Jugador1) # <--- Gurdar jugador

    def eliminar_jugador(self):
            posicion_jugador_lista = self.v_config.lista_jugadores.currentRow()

            # Comprobar si hay un jugador seleccionado
            if posicion_jugador_lista == -1:
                print("Selecciona un jugador para eliminar")
                return #Para romper la funcion en caso de que no se haya selecionado ningun jugador

            # Eliminar de la lista de jugadores
            print(f"Se elimino el jugador: {self.lista_jugadores[posicion_jugador_lista].nombre}")
            self.lista_jugadores.pop(posicion_jugador_lista)

            # Eliminar de la lista visual
            self.v_config.lista_jugadores.takeItem(posicion_jugador_lista)

    #Cambiar pagina
    def iniciar_juego(self): #Configuracion --> Juego
        if len(self.lista_jugadores) < 2:
            print("No hay suficientes jugadores para iniciar el juego (Minimo 2)")
        else:
            self.controlador_ventana_main.capa_main.setCurrentWidget(self.v_juego) #Cambiar ventana

            #Ubicar al primer jugador
            self.jugador_actual.append(self.lista_jugadores[0])
            self.v_juego.texto_nombre.setText(self.lista_jugadores[0].nombre)

    def siguiente_jugador(self):
        posicion = self.lista_jugadores.index(self.jugador_actual[0]) #Devuelve la posicion del jugador actual

        if self.lista_jugadores[posicion] == self.lista_jugadores[-1]: #Comprobar si es el ultimo jugador de la lista
            #Actualizar jugador actual
            jugador = self.lista_jugadores[0]
            self.jugador_actual[0] = jugador 
        else:
            #Actualizar jugador actual
            jugador = self.lista_jugadores[posicion+1]
            self.jugador_actual[0] = jugador

        self.actualizarJugador() #Actualizar informacion del jugador

#Pagina 3 - Juego

    def ponerMesa_ramdon(self):
        #Ubicar mesa
        self.mesa.colocar_carta()
        self.actualizarMesa()


    def actualizarJugador(self):

        jugador = self.jugador_actual[0]
        self.v_juego.texto_nombre.setText(jugador.nombre) #Ubicar nombre

        if len(jugador.mano) == 2:

            carta1 = self.BASE_DIR / "resources" / "componentes" / "cartas" / jugador.mano[0].fotocarta
            carta2 = self.BASE_DIR / "resources" / "componentes" / "cartas" / jugador.mano[1].fotocarta

            foto_carta1 = QPixmap(str(carta1))
            foto_carta2 = QPixmap(str(carta2))

            self.v_juego.label_mano1.setPixmap(foto_carta1)
            self.v_juego.label_mano2.setPixmap(foto_carta2)

        elif len(jugador.mano) == 1:
            carta1 = self.BASE_DIR / "resources" / "componentes" / "cartas" / jugador.mano[0].fotocarta

            foto_carta1 = QPixmap(str(carta1))

            self.v_juego.label_mano1.setPixmap(foto_carta1)

        else:
            jugador = self.jugador_actual[0]

            vacio = self.BASE_DIR / "resources" / "componentes" / "cartas" / "zonaoscura.png"

            foto_vacio = QPixmap(str(vacio))
   
            self.v_juego.label_mano1.setPixmap(foto_vacio)
            self.v_juego.label_mano2.setPixmap(foto_vacio)
            print("El jugador no tiene mano:")

    def actualizarMesa(self):

        print(len(self.mesa.espacio_cartas))

        if len(self.mesa.espacio_cartas) == 1:
            carta1 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[0].fotocarta

            foto_carta1 = QPixmap(str(carta1))
            self.v_juego.label_espacio1.setPixmap(foto_carta1)

        elif len(self.mesa.espacio_cartas) == 2:
            carta2 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[1].fotocarta

            foto_carta2 = QPixmap(str(carta2))
            self.v_juego.label_espacio2.setPixmap(foto_carta2)

        elif len(self.mesa.espacio_cartas) == 3:
            carta1 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[0].fotocarta
            carta2 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[1].fotocarta
            carta3 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[2].fotocarta

            foto_carta1 = QPixmap(str(carta1))
            foto_carta2 = QPixmap(str(carta2))
            foto_carta3 = QPixmap(str(carta3))

            self.v_juego.label_espacio1.setPixmap(foto_carta1)
            self.v_juego.label_espacio2.setPixmap(foto_carta2)
            self.v_juego.label_espacio3.setPixmap(foto_carta3)

        elif len(self.mesa.espacio_cartas) == 4:
            carta4 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[3].fotocarta

            foto_carta4 = QPixmap(str(carta4))
            self.v_juego.label_espacio4.setPixmap(foto_carta4)

        elif len(self.mesa.espacio_cartas) == 5:
            carta5 = self.BASE_DIR / "resources" / "componentes" / "cartas" / self.mesa.espacio_cartas[4].fotocarta

            foto_carta5 = QPixmap(str(carta5))
            self.v_juego.label_espacio5.setPixmap(foto_carta5)

    def seleccionarCarta_mesa(self):
        self.selector_cartas = SelectorCartas("Mesa",self.baraja_main.baraja, self.jugador_actual[0], self.mesa, self.v_juego) #Le indicamos que su ventana padre es juego
        self.selector_cartas.carta_selecionada_mesa.connect(self.ponerCarta_mesa)
        self.selector_cartas.exec() #Abre la ventana de inmediato y obliga a cerrarla 

    def ponerCarta_mesa(self,carta):
        print(f"La carta insertada es: {carta.fotocarta} ")
        self.mesa.carta_especifica(carta)
        self.actualizarMesa()

    def seleccionarCarta_jugador(self):
        self.selector_cartas = SelectorCartas("Jugador",self.baraja_main.baraja,self.jugador_actual[0], self.mesa,self.v_juego) #Le indicamos que su ventana padre es juego
        self.selector_cartas.carta_selecionada_jugador.connect(self.ponerCarta_jugador)
        self.selector_cartas.exec()

    def repartirMano_ramdon(self):
        if self.jugador_actual[0].mano:
            print("El jugador ya tiene mano")
        else:
            self.jugador_actual[0].jugadorMano_ramdon(self.baraja_main)
            self.actualizarJugador()

    def ponerCarta_jugador(self,carta):
            self.jugador_actual[0].jugadorMano(carta)
            self.baraja_main.baraja.remove(carta)
            self.actualizarJugador()
        
    def resultados(self):
        self.controlador_ventana_main.capa_main.setCurrentWidget(self.v_graficas)