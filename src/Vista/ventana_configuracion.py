from .ventana_molde import VentanaMolde
from PySide6.QtWidgets import *
from .boton import BotonAnimado
from PySide6.QtCore import Qt
from pathlib import Path
from PySide6.QtGui import QPixmap

class VConfiguracion(VentanaMolde):
    def __init__(self):
        super().__init__()

    #Direcciones
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        fondo_path = BASE_DIR / "resources" / "fondos" / "fondoconfigsinelementos.png"
        panelderecho_path = BASE_DIR / "resources" / "componentes" / "kingqueen.png"

    #layout Principal
        self.layout = QHBoxLayout(self)

    #widgets
        self.widget_principal = QWidget()

    #Capa
        self.capa_config = QStackedLayout(self.layout) #Capa --> Se guarda en contenerdor
        self.capa_config.setStackingMode(QStackedLayout.StackAll) #Le indicamos que muestre todas las capas al tiempo

    #Textos
        self.texto1 = QLabel("CONFIGURACIÓN")
        self.texto1.setStyleSheet("""
            QLabel {
                color: white;
                background-color: black;
                font-size: 24px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
        """)


        self.texto2 = QLabel("IZQUIERDA")
        self.texto3 = QLabel("DERECHA")
        self.texto4 = QLabel("C1")
        self.texto5 = QLabel("I1")
        self.texto6 = QLabel("D1")

    #Caja de textos
        self.nombre = QLineEdit() #Caja de textos
        self.nombre.setPlaceholderText("-------------  Ingrese el nombre del jugador  -----------")
        self.nombre.setFixedSize(300, 50)

    #Caja - Lista de jugadores
        self.lista_jugadores = QListWidget()
        self.lista_jugadores.setFixedSize(300,200)

    #Botones
        self.añadir_jugador = BotonAnimado("♥",50,50)

    #Imagenes
        fondo_config_imagen = QPixmap(str(fondo_path))
        panel_derecho_imagen = QPixmap(str(panelderecho_path))

    #label
        label_config_imagen = QLabel()
        label_panel_derecho_imagen =QLabel()


        label_config_imagen.setPixmap(fondo_config_imagen)
        label_panel_derecho_imagen.setPixmap(panel_derecho_imagen)
        label_panel_derecho_imagen.setFixedSize(350,480)
        label_panel_derecho_imagen.setScaledContents(True)

    #añadimos mas layouts a widgets
        self.layout_secundario = QHBoxLayout(self.widget_principal)

    #Añadir mas widgets
        izquierda = QWidget()
        centro = QWidget()
        derecaha = QWidget()

        self.layout_secundario.addWidget(izquierda)
        self.layout_secundario.addWidget(centro)
        self.layout_secundario.addWidget(derecaha)


    #Añadir mas layouts
        layout_izquierdo = QVBoxLayout(izquierda)
        layout_centro = QVBoxLayout(centro)
        layout_derecho = QVBoxLayout(derecaha)

    #columna izquierda
        layout_izquierdo.addWidget(label_panel_derecho_imagen,alignment=Qt.AlignmentFlag.AlignCenter)
        
    #Columna central
        layout_centro.addWidget(self.texto1,alignment=Qt.AlignmentFlag.AlignCenter)
        layout_centro.addStretch(1)
        layout_centro.addWidget(self.nombre,alignment=Qt.AlignmentFlag.AlignCenter)
        layout_centro.addWidget(self.lista_jugadores,alignment=Qt.AlignmentFlag.AlignCenter)
        layout_centro.addStretch(1)
    #columna Derecha
        layout_derecho.addWidget(self.añadir_jugador)

    #Añdir widget principal a capa
        self.capa_config.addWidget(self.widget_principal)
        self.capa_config.addWidget(label_config_imagen)