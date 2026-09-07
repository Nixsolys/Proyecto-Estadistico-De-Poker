#Inicia el programa
import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMainWindow
from src.Vista.ventana import*
from src.Controlador.controlador import*

app = QApplication(sys.argv)

ventana1 = Ventana()
ventana2 = VentanaSecundaria()
ventana3 = VentanaTerciaria()
controlador = Controlador(ventana1,ventana2,ventana3)
ventana1.show()


sys.exit(app.exec())
