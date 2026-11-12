
class Indentificar():
    def __init__(self,mesa,jugador):

        self.lista_cartas_mesa = []
        self.lista_cartas_mano = []

        self.listaPesoMesa = []
        self.listaPesoMano = []

        for i in mesa.espacio_cartas:
            self.lista_cartas_mesa.append(i)
            self.listaPesoMesa.append(i.peso)

        for i in jugador.mano:
            self.lista_cartas_mano.append(i)
            self.listaPesoMano.append(i.peso)

    def obtenerTipo(self):
        pass

    def escaleraReal(self):
        if self.listaPesoMano[1] == self.listaPesoMano[0] - 0.076:
            self.listaPesoMesa.append(self.listaPesoMano[1])
            self.listaPesoMesa.append(self.listaPesoMano[0])        
    def EscaleraColor(self):
        pass

    def poker(self):
        contador_mesa = self.contarCarta(self.listaPesoMesa)
        contador_mano = self.contarCarta(self.listaPesoMano)

        if "poker" in contador_mesa[0]:
            print("POKER 1")
            return 0
        elif "trio" in contador_mesa[0] and contador_mesa[1][2] in self.listaPesoMano:
            print("POKER 2")
            return 1
        elif "pareja" in contador_mesa[0] and "pareja" in contador_mano[0] and self.listaPesoMano[0] in contador_mesa[1]:
            print("POKER 3")
            return 1
        else:
            return False

    def fullHouse(self):
        contador_mesa = self.contarCarta(self.listaPesoMesa)
        contador_mano = self.contarCarta(self.listaPesoMano)
        if "trio" in contador_mesa[0]:
            if "pareja" in contador_mesa[0]:
                print("Mesa: FullHouse - 1")
                return 0
            elif "pareja" in contador_mano[0]:
                print("Jugador: Pareja, Fullhouse - 2")
                return 1
            elif self.listaPesoMano[0] in self.listaPesoMesa or self.listaPesoMano[1] in self.listaPesoMesa:
                print("Jugador y Mesa: Pareja, Fullhouse - 3")
                return 2
            else:
                return False


    def color(self):

        colorMesa = self.contarColor(self.lista_cartas_mesa)
        colorMano = self.contarColor(self.lista_cartas_mano)

        if colorMesa:
            if colorMesa[0] == 5:
                if colorMesa[1] == self.lista_cartas_mano[0].palo or colorMesa[1] == self.lista_cartas_mano[0].palo:
                    print("Jugador y Mesa: Color - 1")
                    return 2
            elif colorMesa[0] == 4:
                if colorMesa[1] == self.lista_cartas_mano[0].palo or colorMesa[1] == self.lista_cartas_mano[0].palo:
                    print("Jugador y Mesa: Color - 2")
                    return 2
            elif colorMesa[0] == 3 and colorMano and colorMesa[1] == colorMano[1]:
                    print("Jugador y Mesa: Color - 3")
                    return 2

    def escalera(self):
        pass
    def trio(self):
        pass
    def doblePareja(self):
        pass
    def pareja(self):
        contador_mesa = self.contarCarta(self.lista_cartas_mesa)
        contador_mano = self.contarCarta(self.lista_cartas_mano)

        
    def cartaAlta(self):
        return 

    def obtenerPeso(self):
        pass

    def contarColor(self,cartas):
        #Variable para contar los distintos palos
        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 0
        #Itereador para ir aumentado las variables contadoras
        for i in cartas:
            if i.palo == "corazon":
                contador1 +=1
            if i.palo == "pica":
                contador2 +=1
            if i.palo == "diamante":
                contador3 +=1
            if i.palo == "trebol":
                contador4 +=1
        #Filtrar por mano
        if len(cartas) == 2:
            if contador1 > 1:
                return [contador1,"corazon"]
            elif contador2 > 1:
                return [contador2,"pica"]
            elif contador3 > 1:
                return [contador3,"diamante"]
            elif contador4 > 1:
                return [contador4,"trebol"]
            else:
                return False
        #Filtrar Mesa
        else:
            if contador1 > 2:
                return [contador1,"corazon"]
            elif contador2 > 2:
                return [contador2,"pica"]
            elif contador3 > 2:
                return [contador3,"diamante"]
            elif contador4 > 2:
                return [contador4,"trebol"]
            else:
                return False

    def contarCarta(self,cartas):
        indicador = []
        carta = []
        for i in cartas:
            contador = cartas.count(i)
            if contador == 2:
                indicador.append("pareja")
                carta.append(i)
            elif contador == 3:
                indicador.append("trio")
                carta.append(i)
            elif contador == 4:
                indicador.append("poker")
                carta.append(i)

        return indicador,carta

    def resultado(self):
        if self.escaleraReal():
            print("Se detecto una escalera Real")
        elif self.EscaleraColor():
            pass
        elif self.poker():
            pass
        elif self.fullHouse():
            pass
        elif self.color():
            print("Se detecto un color")
        elif self.escalera():
            pass
        elif self.trio():
            pass
        elif self.doblePareja():
            pass
        elif self.pareja():
            pass
        elif self.cartaAlta():
            pass          