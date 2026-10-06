
class Mano():
    def obtener_mano(self,bara_actual):
        carta_mano = bara_actual.obtener_carta(2) #Obtener cartas
        self.mano = [carta_mano[0],carta_mano[1]] #Añadimos la cartas a mano

        return self.mano