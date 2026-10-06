from .ventana_molde import VentanaMolde
from PySide6.QtWidgets import *
from pathlib import Path
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
from .boton import BotonAnimado
from PySide6.QtCore import QSize

class VentanaJuego(VentanaMolde):   
    def __init__(self):
        print("Ventana Juego en ejecucion: ")
        super().__init__()

    #Widget Principal
        self.wideget_principal = QWidget()

    #Layouts
        layout = QVBoxLayout(self)
        layout.addWidget(self.wideget_principal)

    #capa
        self.capa_juego = QStackedLayout(self.wideget_principal)
        self.capa_juego.setStackingMode(QStackedLayout.StackAll) #Los muestra simultaneamente

    #Direcciones

        #Direccion Raiz
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        fondo_path = BASE_DIR / "resources" / "fondos" / "fondoconfigsinelementos.png"
        dorso_path = BASE_DIR / "resources" / "componentes" / "cartas" / "zonaoscura.png"
        baraja_path = BASE_DIR / "resources" / "componentes" / "cartas" / "baraja.png"
        
    #imagenes
        fondo_juego_imagen = QPixmap(str(fondo_path))
        dorso_juego_imagen = QPixmap(str(dorso_path)) 

    #labels - Donde se guardan los pixmap
        label_juego_fondo = QLabel()
        #Espacios en la mesa
        self.label_espacio1 = QLabel()
        self.label_espacio2 = QLabel() 
        self.label_espacio3 = QLabel()
        self.label_espacio4 = QLabel()
        self.label_espacio5 = QLabel()

        #Espacios de la mano
        self.label_mano1 = QLabel()
        self.label_mano2 = QLabel()

        #Caja - nombre jugador
        self.texto_nombre = QLabel()
        self.texto_nombre.setFixedSize(200, 60)
        self.texto_nombre.setStyleSheet("""
            QLabel {
                color: white;
                background-color: black;
                font-size: 24px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
        """)

    #Configuracion de labels
        for label in [
            self.label_espacio1,
            self.label_espacio2,
            self.label_espacio3,
            self.label_espacio4,
            self.label_espacio5,
            self.label_mano1,
            self.label_mano2
        ]:
            label.setFixedSize(180, 210)
            label.setScaledContents(True)
            
    #Cajas con titulos
        caja_win = QGroupBox("Probabilidad de ganar")
        caja_lose = QGroupBox("Probabilidad de perder")

    #Guardar imagenes
        label_juego_fondo.setPixmap(fondo_juego_imagen)

        self.label_espacio1.setPixmap(dorso_juego_imagen)
        self.label_espacio2.setPixmap(dorso_juego_imagen)
        self.label_espacio3.setPixmap(dorso_juego_imagen)
        self.label_espacio4.setPixmap(dorso_juego_imagen)
        self.label_espacio5.setPixmap(dorso_juego_imagen)

        self.label_mano1.setPixmap(dorso_juego_imagen)
        self.label_mano2.setPixmap(dorso_juego_imagen)

    #Contenido
        contenido = QWidget()
        layout_contenido = QVBoxLayout(contenido)

    #Widget Principales
        self.wideget_up = QWidget()
        self.wideget_central = QWidget()
        self.wideget_down = QWidget()

    #Guardar widgets principales en el layout de contenido
        layout_contenido.addWidget( self.wideget_up)
        layout_contenido.addWidget( self.wideget_central)
        layout_contenido.addWidget( self.wideget_down)

    #Layouts Principales
        layout_up = QHBoxLayout(self.wideget_up)
        layout_central = QHBoxLayout(self.wideget_central)
        layout_down = QHBoxLayout(self.wideget_down)
    
    #Botones
        self.boton_total = BotonAnimado("Probabilidad Total",100,50)

        self.boton_relativo = BotonAnimado("Probabilidad Relativa",100,50)

        self.boton_resultados = BotonAnimado("Resultados", 100,50)

        self.boton_next_player = BotonAnimado("Next",100,50)

        self.boton_baraja = BotonAnimado("",190,190)
        self.boton_baraja.setIcon(QIcon(str(baraja_path)))
        self.boton_baraja.setIconSize(QSize(270, 270))
        self.boton_baraja.setFlat(True)

    #Layout UP
        layout_up.addWidget(self.boton_total)
        layout_up.addWidget(self.boton_relativo)
        layout_up.addWidget(self.texto_nombre)
        layout_up.addWidget(self.boton_resultados)
        layout_up.addWidget(self.boton_next_player)

    #Layout CENTRAL
        layout_central.addWidget(self.label_espacio1)
        layout_central.addWidget(self.label_espacio2)
        layout_central.addWidget(self.label_espacio3)
        layout_central.addWidget(self.label_espacio4)
        layout_central.addWidget(self.label_espacio5)

    #Layout Down
        layout_down.addWidget(caja_win)
        layout_down.addWidget(caja_lose)
        layout_down.addWidget(self.label_mano1)
        layout_down.addWidget(self.label_mano2) 
        layout_down.addWidget(self.boton_baraja)

    #Añadir capas
        self.capa_juego.addWidget(contenido)
        self.capa_juego.addWidget(label_juego_fondo)