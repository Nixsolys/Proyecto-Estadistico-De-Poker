from .baraja import Baraja

class Mano():

    def obtener_mano(self,bara_actual):
        print("MANO:")
        carta_mano = bara_actual.obtener_carta(2) #Obtener cartas
        self.mano = [carta_mano[0],carta_mano[1]] #Añadimos la cartas a mano
        

