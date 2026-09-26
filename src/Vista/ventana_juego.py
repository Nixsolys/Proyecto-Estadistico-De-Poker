from .ventana_molde import VentanaMolde
from PySide6.QtWidgets import *
from pathlib import Path
from PySide6.QtGui import QPixmap
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

        print(fondo_path)

        #imagenes
        fondo_juego_imagen = QPixmap(str(fondo_path)) 

        #labels
        label_juego_fondo = QLabel()

        label_juego_fondo.setPixmap(fondo_juego_imagen)
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

        layout_up = QHBoxLayout(self.wideget_up)
        layout_central = QHBoxLayout(self.wideget_central)
        layout_down = QHBoxLayout(self.wideget_down)

        layout_up.addWidget(boton_total)
        layout_up.addWidget(boton_relativo)

        self.capa_juego.addWidget(contenido)
        self.capa_juego.addWidget(label_juego_fondo)
