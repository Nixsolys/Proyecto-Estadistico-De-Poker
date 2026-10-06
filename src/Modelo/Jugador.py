from .mano import Mano


class Jugador():
    def __init__(self,nombre):

        self.nombre = nombre
        print(f"Se a creado el jugador con el nombre: {self.nombre} ")
        
    def jugador_mano(self,baraja_actual):
        mano1 = Mano()
        self.mano = mano1.obtener_mano(baraja_actual) #Añadimos las cartas de la mano al jugador

        print(f"El jugador: {self.nombre}")
        print(f"Obtuvo: {self.mano[0].fotocarta} y {self.mano[1].fotocarta}")