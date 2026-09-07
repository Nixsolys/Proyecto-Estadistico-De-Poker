from .ventana_molde import VentanaMolde
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from .boton import BotonAnimado
from pathlib import Path
from PySide6.QtCore import Qt

class Ventanamenu(VentanaMolde):
    def __init__(self):
        print("VentanMenu")
        super().__init__()

    #Atributos
        #widget Princpal
        self.contenerdor_principal = QWidget() #Widget/contenedor principal

        #layoust
        layout = QVBoxLayout(self) #"Crea un QVBoxLayout y haz que su dueño/padre sea este objeto (self)."
        layout.addWidget(self.contenerdor_principal)
    
        #Capa
        self.capa_menu = QStackedLayout(self.contenerdor_principal) #Capa --> Se guarda en contenerdor
        self.capa_menu.setStackingMode(QStackedLayout.StackAll) #Le indicamos que muestre todas las capas al tiempo

    #Direcion raiz
        BASE_DIR = Path(__file__).resolve().parent.parent.parent #ObjetoTipoPath

    #Direcciones - Las configuramos asi para que pueda funcionar donde se ejecute el programa
        fondo_path = BASE_DIR / "resources" / "fondos" / "fondo1.png"
        logo_path = BASE_DIR / "resources" / "logotipos" / "Logotipo3PSinFondo.png"

        print(fondo_path)
        print(logo_path)

    #Imagenes
        fondo_imagen = QPixmap(str(fondo_path)) #<-- Objeto tipo Pixmasp - que guarda la imagen
        logo_imagen = QPixmap(str(logo_path)) #Guardamos las imagenes en objetos que si podemos usar con Qpixmas no
    #contenido
        self.contenido = QWidget()
        self.layout_contenido = QVBoxLayout(self.contenido)

    #Labels
        self.label_fondo_imagen = QLabel()
        self.label_logo_imagen = QLabel()

        #configuracion de labels
        self.label_fondo_imagen.setPixmap(fondo_imagen)
        self.label_fondo_imagen.setScaledContents(True)

        
        self.label_logo_imagen.setPixmap(logo_imagen)
        self.label_logo_imagen.setFixedSize(300,300)
        self.label_logo_imagen.setScaledContents(True)

    #Botones
        self.iniciar = BotonAnimado("♦",300,50)
        self.iniciar.setStyleSheet("""

            QPushButton {
            background-color: white;
            color: #C65A5A;
            border: 5px solid #C65A5A;
            border-radius: 8px;
            font-size: 30px;
        }

        QPushButton:hover {
            background-color: white;
            color: #212121;
            border: 5px solid #212121;
            border-radius: 8px;
            font-size: 30px;
        }
        """)

    #--------
        self.layout_contenido.addWidget(
            self.label_logo_imagen,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.layout_contenido.addWidget(
            self.iniciar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.capa_menu.addWidget(self.contenido)
        self.capa_menu.addWidget(self.label_fondo_imagen)
        
