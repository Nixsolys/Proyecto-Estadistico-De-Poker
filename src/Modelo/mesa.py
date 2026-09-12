class Mesa():
    def __init__(self,baraja):
        self.espacio_cartas = [] #Cartas que estan en la mesa
        self.mesa_baraja = baraja #Baraja que esta en la mesa
        self.turno_inicial = True

    def colocar_carta(self):
        print("MESA: ")
        if self.turno_inicial == True: #Para comprobar el turno, ya que en el turno inicial se colocan 3 cartas
            self.turno_inicial = False
            cartas_mesa = self.mesa_baraja.obtener_carta(3) #Obtenemos una lista con las 3 cartas

            for i in cartas_mesa:
                self.espacio_cartas.append(i) #Añadimos la carta a los espacios en mesa

        else:
            cartas_mesa = self.mesa_baraja.obtener_carta(1) #Obtenemos una lista con una
            self.espacio_cartas.append(cartas_mesa[0])
        

        for i in self.espacio_cartas:
            print(f"Espacio carta: {i.fotocarta}") #Imprimir cartas que estan en la mesa
