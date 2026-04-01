import math
class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def distancia_punto(self, otro_punto):
        return math.sqrt((self.__x - otro_punto.get_x())**2 + 
                         (self.__y - otro_punto.get_y())**2)

    def distancia_coords(self, x, y):
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)

punto1 = MiPunto()           
punto2 = MiPunto(10, 30.5)   
resultado = punto1.distancia_punto(punto2)

print("Punto 1:", punto1.get_x(), ",", punto1.get_y())
print("Punto 2:", punto2.get_x(), ",", punto2.get_y())
print("La distancia entre ellos es:", round(resultado, 4))