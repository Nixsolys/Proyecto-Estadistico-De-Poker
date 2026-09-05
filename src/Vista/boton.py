from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtWidgets import QPushButton

class BotonAnimado(QPushButton):

    def __init__(self, texto,ancho,alto):
        super().__init__(texto) #Ejecuta la clase padre para heredar/activar los atributos


        self.tamaño_normal = QSize(ancho,alto) #Estamos indicado que el tamaño del boton es el que ya trae
        self.tamaño_hover = self.tamaño_normal * 1.1 #Aumento de tamaño

        #Animacion del tamaño
        self.animacion = QPropertyAnimation(self, b"size") #(Boton1, propiedad que queremos modificar)
        self.animacion.setDuration(150) #Duracion esta en milisegundos
        self.animacion.setEasingCurve(QEasingCurve.OutCubic) #Controla la velocidad de animacion para que se a uniforme

    def enterEvent(self, event): #Metodo especial de herencia <-- Se ejecuta cuando el mouse esta encima #Event, mouse hace clik, salio etc
        self.animacion.stop() #Cancelamos toda anaimacion anterior
        self.animacion.setStartValue(self.size()) #Inicia la animacion desde el tamaño
        self.animacion.setEndValue(self.tamaño_hover) #Termina en el el aumetno de tamaño
        self.animacion.start() #Inicio

        super().enterEvent(event) #Para que el boton siga teniendo boton solo tenga el comprtamiento que le indiacos

    def leaveEvent(self, event): #Metodo especial de herencia <-- Cuando el mouse sale -- Ejecutamos la animacion inversa
        self.animacion.stop()
        self.animacion.setStartValue(self.size())
        self.animacion.setEndValue(self.tamaño_normal)
        self.animacion.start()

        super().leaveEvent(event)


