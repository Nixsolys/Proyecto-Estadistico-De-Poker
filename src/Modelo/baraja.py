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
        contador2 = 0 #Varaible que nos ayuda a imprimir la carta que obtuvimos
        posiciones = []

        while contador > 0:
            numero = random.randint(0, (len(self.baraja)-1)) #Numero aleatorio entre el numero de cartas actuales y 0
            contador -= 1

            posiciones.append(numero) #Guardamos el numero aleatorio

            print(f"Se obtuvo: {self.baraja[posiciones[contador2]].fotocarta}")#Se imprime la carta en base a la posicion con el numero aleatorio
            contador2 +=1 #Aumenta de numero para imprimir la siguiente carta
        
        return posiciones
        

    def borrar_carta(self,posiciones):
        lista_borrar = []
        for i in posiciones: #Guardamos los elementos que queremos borrar primero
                lista_borrar.append(self.baraja[i])

        for i in lista_borrar: #Ahora iteramos en la lista y borramos los elementos directamente
            print(f"Se elimino: {i.fotocarta}")
            self.baraja.remove(i)

            print(f"El numero de cartas restantes es: {len(self.baraja)}")

    def imprimir_mazo(self): #Variable que itera en todas las cartas del mazo para imprimirlo

        for i in self.baraja:
            print(i.fotocarta)
