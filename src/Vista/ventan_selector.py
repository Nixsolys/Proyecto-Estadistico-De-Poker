from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QGridLayout
from PySide6.QtWidgets import QPushButton
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Signal


class SelectorCartas(QDialog): #ventana secundaria

    #Señales
    carta_selecionada_mesa = Signal(object)
    carta_selecionada_jugador = Signal(object)


    def __init__(self,identificador, mazo, jugador,mesa, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Seleccionar carta")
        self.resize(500, 500)

        self.mazo = mazo
        self.mesa = mesa
        self.jugador = jugador

        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        # Organizar las cartas en filas y columnas
        self.layout_principal = QGridLayout(self)
        self.layout_principal.setSpacing(10)

        columnas = 12

        for indice, carta in enumerate(self.mazo): #Iteramos entre la posicion de la carta y la carta
            self.boton_carta = QPushButton()

            carta_path = (
                BASE_DIR
                / "resources"
                / "componentes"
                / "cartas"
                / carta.fotocarta
            )

            self.boton_carta.setIcon(QIcon(str(carta_path)))
            self.boton_carta.setIconSize(QSize(70, 100))
            self.boton_carta.setFixedSize(85, 115)

            if identificador == "Mesa":
                self.boton_carta.clicked.connect(
                    lambda checked=False, c=carta, b = self.boton_carta:
                    self.seleccionarCarta_mesa(c,b)
                )
            else:
                self.boton_carta.clicked.connect(
                lambda checked=False, c=carta, b = self.boton_carta:
                self.seleccionarCarta_jugador(c,b)
            )


            fila = indice // columnas
            columna = indice % columnas

            self.layout_principal.addWidget(
                self.boton_carta, fila, columna
            ) #Coloca el boton en esta fila y esta columna

    def seleccionarCarta_mesa(self, carta,boton):
        if len(self.mesa.espacio_cartas) == 5:
            print("Mesa llena")
        else:
            print("Carta seleccionada:", carta.fotocarta)
            self.carta_selecionada_mesa.emit(carta)
            self.eliminarBoton(boton)

    def seleccionarCarta_jugador(self, carta,boton):
        if len(self.jugador.mano) == 2:
            print("Mano llena")
        else:
            print("Carta seleccionada:", carta.fotocarta)
            self.carta_selecionada_jugador.emit(carta)
            self.eliminarBoton(boton)

    def eliminarBoton(self,boton):
        self.layout_principal.removeWidget(boton) #Borrarlo visualmente
        boton.deleteLater() #Borrar completamente el objeto