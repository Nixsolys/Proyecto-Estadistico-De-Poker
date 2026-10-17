class Mesa():
    def __init__(self,baraja):
        self.espacio_cartas = [] #Cartas que estan en la mesa
        self.baraja = baraja #Baraja que esta en la mesa

    def colocar_carta(self):
        print("MESA: ")
        if len(self.espacio_cartas) == 5:
            print("No se pueden añadir mas cartas")
        else:
            if len(self.espacio_cartas) == 0: #Para comprobar el turno, ya que en el turno inicial se colocan 3 cartas
                cartas_mesa = self.baraja.obtener_carta(3) #Obtenemos una lista con las 3 cartas

                for i in cartas_mesa:
                    self.espacio_cartas.append(i) #Añadimos la carta a los espacios en mesa

            else:
                cartas_mesa = self.baraja.obtener_carta(1) #Obtenemos una lista con una carta
                self.espacio_cartas.append(cartas_mesa[0])
            
            for i in self.espacio_cartas:
                print(f"Espacio carta: {i.fotocarta}") #Imprimir cartas que estan en la mesa

    def carta_especifica(self,carta):
        if len(self.espacio_cartas) == 5:
            print("No se pueden añadir mas cartas")
        else:
            self.espacio_cartas.append(carta)
            self.baraja.borrar(carta)