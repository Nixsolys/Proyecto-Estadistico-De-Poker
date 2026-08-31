from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap




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


        # Layout principal
        layoutMain = QVBoxLayout(central) #De una ves se cololca en el Widget Central


        # Fondo
        self.fondo = QLabel() #Creamos un objeto tipo QL 
        self.logoPrincipal = QLabel()

        fondo1 = QPixmap(
            "Proyecto-Estadistico-De-Poker/resources/fondos/fondo1.png"
        ) #<-- Objeto tipo Pixmasp - que guarda la imagen

        logo1 = QPixmap(
            "Proyecto-Estadistico-De-Poker/resources/logotipos/Logotipo3PSinFondo.png"
        )

        self.fondo.setPixmap(fondo1) #Guardamos la imagen en el QL
        self.fondo.setScaledContents(True)

        self.logoPrincipal.setPixmap(logo1)

        layoutMain.addWidget(self.fondo) #<-- Añadimos el QL al layout principal que guarda la imagen
        layoutMain.addWidget(self.logoPrincipal)

  