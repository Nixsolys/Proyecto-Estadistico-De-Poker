from .cartas import Carta
import random

class Baraja():

    def __init__(self):
        self.baraja = []

    def crear_baraja(self):

        for palo in Carta.palos:
            for alfanumero in Carta.pesos:

                carta = Carta(palo, alfanumero)

                self.baraja.append(carta)

    def obtener_carta(self,numero_cartas):
        contador = numero_cartas #Cantidad de cartas que queremos obtener
        contador2 = 0
        posiciones = []

        while contador > 0:
            numero = random.randint(0, (len(self.baraja)-1))
            contador -= 1

            posiciones.append(numero)

            print(f"Se obtuvo: {self.baraja[posiciones[contador2]].fotocarta}")
            contador2 +=1
        
        return posiciones
        

    def borrar_carta(self,posiciones):
        lista_borrar = []
        for i in posiciones:
                lista_borrar.append(self.baraja[i])

        for i in lista_borrar:
            print(f"Se elimino: {i.fotocarta}")
            self.baraja.remove(i)

            print(f"El numero de cartas restantes es: {len(self.baraja)}")

    def imprimir_mazo(self):

        for i in self.baraja:
            print(i.fotocarta)
