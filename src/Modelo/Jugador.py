from .mano import Mano


class Jugador():
    def __init__(self,nombre):

        self.nombre = nombre

    def jugador_mano(self,baraja_actual):
        mano1 = Mano()
        self.mano = mano1.obtener_mano(baraja_actual)