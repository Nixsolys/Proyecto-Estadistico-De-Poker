#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from Vista.ventana import Ventana


app = QApplication(sys.argv)


ventana1 = Ventana()


ventana1.show()

sys.exit(app.exec())
