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
                cartas.append(carta) #Guardamos la carta
                self.borrar(carta)
                contador -= 1

        return cartas

    def borrar(self,carta):
        print(f"Se elimino del mazo: {carta.fotocarta}\n")
        self.baraja.remove(carta)

    def imprimir_mazo(self): #Variable que itera en todas las cartas del mazo para imprimirlo

        for i in self.baraja:
            print(i.fotocarta)

    def obtenerCarta_especifica(self, carta):
        carta_especifica = carta
        self.baraja.remove(carta)
        
        return carta_especifica