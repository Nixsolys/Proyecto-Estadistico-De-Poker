from .baraja import Baraja

class Mano():

    def obtener_mano(self,bara_actual):
        print("MANO:")
        posiciones = bara_actual.obtener_carta(2)
        self.mano = [bara_actual.baraja[posiciones[0]], bara_actual.baraja[posiciones[1]]]
        bara_actual.borrar_carta(posiciones)

