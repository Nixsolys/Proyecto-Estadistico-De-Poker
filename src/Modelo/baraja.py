from .cartas import Carta
import random

class Baraja():

    def __init__(self):
        self.baraja = []

    def crear_baraja(self):

        for palo in Carta.palos: #Varaible que va iterar en Corazon, Diamante, Trebol y Picas
            for alfanumero in Carta.pesos: #Variable que va iterar desde 2 to A

                carta = Carta(palo, alfanumero) #Se crea la carta

                self.baraja.append(carta) #Se guarda en la lista

    def obtener_carta(self,numero_cartas):
        contador = numero_cartas #Cantidad de cartas que queremos obtener
        cartas = []

        while contador > 0:
            
                carta = random.choice(self.baraja) #Escoge una carta aleatoria del mazo
                print(f"Se obtuvo: {carta.fotocarta}")#Se imprime la carta Ñ
                cartas.append(carta) #Guardamos la carta
                print(f"Se elimino: {carta.fotocarta}")
                self.baraja.remove(carta) #Borramos la carta del mazo
                contador -= 1

        return cartas

    def imprimir_mazo(self): #Variable que itera en todas las cartas del mazo para imprimirlo

        for i in self.baraja:
            print(i.fotocarta)
 