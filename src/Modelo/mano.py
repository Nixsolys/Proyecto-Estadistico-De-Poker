from .baraja import Baraja

class Mano():

    def obtener_mano(self,bara_actual):
        posiciones = bara_actual.obtener_carta(2)
        print(posiciones[0])
        print(posiciones[1])
        self.mano = [bara_actual.baraja[posiciones[0]], bara_actual.baraja[posiciones[1]]]
        bara_actual.borrar_carta(posiciones)