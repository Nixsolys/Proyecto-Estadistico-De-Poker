class Mesa():
    def __init__(self,baraja):
        self.espacio_cartas = [] #Cartas que estan en la mesa
        self.mesa_baraja = baraja #Baraja que esta en la mesa
        self.turno_inicial = True

    def colocar_carta(self):
        print("MESA: ")
        if self.turno_inicial == True:
            self.turno_inicial = False
            posiciones_mesa = self.mesa_baraja.obtener_carta(3) #Obtenemos una lista con las 3 posiciones de la carta que queremos en la baraja
            for i in posiciones_mesa:
                self.espacio_cartas.append(self.mesa_baraja.baraja[i])#Añadimos la carta
        else:
            posiciones_mesa = self.mesa_baraja.obtener_carta(1)
            self.espacio_cartas.append(self.mesa_baraja.baraja[posiciones_mesa[0]])
        
        self.mesa_baraja.borrar_carta(posiciones_mesa)

        for i in self.espacio_cartas:
            print(f"Espacio carta: {i.fotocarta}")
