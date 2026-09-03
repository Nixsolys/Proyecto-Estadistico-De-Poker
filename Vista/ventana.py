from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt




class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        # Configuración de ventana
        self.setWindowTitle("Proyect - Poker - probability")

        self.setWindowIcon(
            QIcon(
                "Proyecto-Estadistico-De-Poker/resources/logotipos/Logotipo3PSinFondo.png"
            )
        )

        self.setFixedSize(1200, 600) #<-- Tamaño fijo de la ventana



        # Widget central
        central = QWidget()
        self.setCentralWidget(central)

        #Layout de capas
        capas = QStackedLayout(central)
        capas.setStackingMode(QStackedLayout.StackAll)

        # Fondo
        self.fondo = QLabel() #Creamos un objeto tipo QL 
        self.logoPrincipal = QLabel()

        #contenido
        contenido = QWidget()
        layoutMain = QVBoxLayout(contenido)


        #Imagenes
        fondo1 = QPixmap(
            "Proyecto-Estadistico-De-Poker/resources/fondos/fondo1.png"
        ) #<-- Objeto tipo Pixmasp - que guarda la imagen

        logo1 = QPixmap(
            "Proyecto-Estadistico-De-Poker/resources/logotipos/Logotipo3PSinFondo.png"
        )

        #Guardamos las imagenes en objetos que si podemos usar con Qpixmas no

        #Logo
        self.fondo.setPixmap(fondo1) #Guardamos la imagen en el QLabel
        self.fondo.setScaledContents(True) #La imagen se adapte correctamente
        
        #Fondo
        self.logoPrincipal.setFixedSize(300,300) #Tamaño
        self.logoPrincipal.setScaledContents(True) #Dado un escala del Qlabel la imagen se adapta
        self.logoPrincipal.setAlignment(Qt.AlignmentFlag.AlignCenter) #centramos el contenido dentro del label es decir la imagen
        self.logoPrincipal.setPixmap(logo1) #Guaradamos le imagen en la "Caja" --> Logoprincipal -->QLabel

        #Botones
        iniciar = QPushButton("♦")

        iniciar.setFixedSize(300, 50)
        iniciar.setStyleSheet("""

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
        
            boton.setText("Calcular")
}







        """)
  

        
        layoutMain.addWidget(self.logoPrincipal) 
        layoutMain.setAlignment(Qt.AlignmentFlag.AlignCenter)#centramos el label
        layoutMain.addStretch(1) #Espacios
        layoutMain.addWidget(iniciar) #Guardamos boton
        layoutMain.addStretch(4) 

        capas.addWidget(contenido)#Las primeras capas quedan ultimas
        capas.addWidget(self.fondo) 
