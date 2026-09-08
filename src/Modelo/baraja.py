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
        contador = numero_cartas
        posiciones = []

        while contador > 0:
            numero = random.randint(0, (len(self.baraja)-1))
            print(numero)
            print(contador)
            contador -= 1

            posiciones.append(numero)
        
        return posiciones
        

    def borrar_carta(self,posiciones):
        for i in posiciones:
            print(i)
            self.baraja.pop(i)