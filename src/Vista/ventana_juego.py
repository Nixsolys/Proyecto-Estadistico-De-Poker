from .ventana_molde import VentanaMolde
from PySide6.QtWidgets import *
from pathlib import Path
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
from .boton import BotonAnimado

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
        self.capa_juego.setStackingMode(QStackedLayout.StackAll)

    #Direccion raiz
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        fondo_path = BASE_DIR / "resources" / "fondos" / "fondoconfigsinelementos.png"
        dorso_path = BASE_DIR / "resources" / "componentes" / "cartas" / "dorso.png"
        baraja_path = BASE_DIR / "resources" / "componentes" / "cartas" / "baraja.png"
        

        print(fondo_path)

    #imagenes
        fondo_juego_imagen = QPixmap(str(fondo_path)) 
        dorso_juego_imagen = QPixmap(str(dorso_path))

    #labels
        label_juego_fondo = QLabel()

        self.label_espacio1 = QLabel()
        self.label_espacio2 = QLabel() 
        self.label_espacio3 = QLabel()
        self.label_espacio4 = QLabel()
        self.label_espacio5 = QLabel()
 
        self.label_mano1 = QLabel()
        self.label_mano2 = QLabel()

        self.texto_nombre = QLabel("EMEL")
        self.texto_nombre.setFixedSize(200, 60)

    #Cajas con titulos
        caja_win = QGroupBox("Probabilidad de ganar")
        caja_lose = QGroupBox("Probabilidad de perder")

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

        self.wideget_up = QWidget()
        self.wideget_central = QWidget()
        self.wideget_down = QWidget()

        layout_contenido.addWidget( self.wideget_up)
        layout_contenido.addWidget( self.wideget_central)
        layout_contenido.addWidget( self.wideget_down)

    #Botones
        boton_total = BotonAnimado("Probabilidad Total",100,50)
        boton_relativo = BotonAnimado("Probabilidad Relativa",100,50)
        boton_resultados = BotonAnimado("Resultados", 100,50)
        boton_next_player = BotonAnimado("Next",100,50)
        boton_baraja = BotonAnimado("",100,100)
        boton_baraja.setIcon(QIcon(str(baraja_path)))

        layout_up = QHBoxLayout(self.wideget_up)
        layout_central = QHBoxLayout(self.wideget_central)
        layout_down = QHBoxLayout(self.wideget_down)

    #Layout UP

        layout_up.addWidget(boton_total)
        layout_up.addWidget(boton_relativo)
        layout_up.addWidget(self.texto_nombre)
        layout_up.addWidget(boton_resultados)

    #Layout CENTRAL
        layout_central.addWidget(self.label_espacio1)
        layout_central.addWidget(self.label_espacio2)
        layout_central.addWidget(self.label_espacio3)
        layout_central.addWidget(self.label_espacio4)
        layout_central.addWidget(self.label_espacio5)
        layout_central.addWidget(boton_baraja)
        
    #Layout Down
        layout_down.addWidget(caja_win)
        layout_down.addWidget(caja_lose)
        layout_down.addWidget(self.label_mano1)
        layout_down.addWidget(self.label_mano2)


        self.capa_juego.addWidget(contenido)
        self.capa_juego.addWidget(label_juego_fondo)
    
    