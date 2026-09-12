from .baraja import Baraja

class Mano():

    def obtener_mano(self,bara_actual):
        print("MANO:")
        carta_mano = bara_actual.obtener_carta(2) #Obtener cartas
        self.mano = [bara_actual.baraja[carta_mano[0]], bara_actual.baraja[carta_mano[1]]] #Añadimos la cartas a mano
        bara_actual.borrar_carta(carta_mano) #Borramos las cartas que obtuvimos de la baraja

