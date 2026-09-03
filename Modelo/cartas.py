class Carta:

    def __init__(self, palo, alfanumerico):

        palos = {
            1: "corazon",
            2: "picas",
            3: "diamante",
            4: "trebol"
        }

        pesos = {
            "A": 1.000,
            "K": 0.923,
            "Q": 0.846,
            "J": 0.769,
            "10": 0.692,
            "9": 0.615,
            "8": 0.538,
            "7": 0.461,
            "6": 0.384,
            "5": 0.307,
            "4": 0.230,
            "3": 0.153,
            "2": 0.076
        }

        self.alfanumerico = alfanumerico
        self.palo = palos.get(palo) #Asignamos con get el palo de la carta
        self.peso = pesos.get(alfanumerico) # Asignamos el peso de la carta, con get obtenemos el valor asignado a esa clave en este caso el alfanumerico

        self.fotocarta = f"{self.palo}{self.alfanumerico}.png"

        
        print("Palo:", self.palo)
        print("Carta:", self.alfanumerico)
        print("Peso:", self.peso)
        print("Imagen:", self.fotocarta)


asdeDiamantes = Carta(3,"A")
