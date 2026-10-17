from .mano import Mano


class Jugador():

    def __init__(self,nombre):

        self.mano = []

        self.nombre = nombre
        print(f"Se a creado el jugador con el nombre: {self.nombre} ")
        
    def jugadorMano_ramdon(self,baraja_actual):
        mano1 = Mano()
        self.mano = mano1.obtenerMano_ramdon(baraja_actual) #Añadimos las cartas de la mano al jugador

        print(f"El jugador: {self.nombre}")
        print(f"Obtuvo: {self.mano[0].fotocarta} y {self.mano[1].fotocarta}")

    def jugadorMano(self,carta):
        self.mano.append(carta)