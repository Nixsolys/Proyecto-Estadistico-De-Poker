class Carta:

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

    def __init__(self, palo, alfanumerico):


        self.alfanumero = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        self.alfanumerico = str(alfanumerico)
        self.palo = self.palos.get(palo) #Asignamos con get el palo de la carta
        self.peso = self.pesos.get(alfanumerico) # Asignamos el peso de la carta, con get obtenemos el valor asignado a esa clave en este caso el alfanumerico

        self.fotocarta = f"{self.palo}{self.alfanumerico}.png"

        print("Imagen:", self.fotocarta)


