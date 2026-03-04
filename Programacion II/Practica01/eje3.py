import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
    
entrada = input("Ingrese a, b, c: ")
a, b, c = [float(n) for n in entrada.split()]
eq = EcuacionCuadratica(a, b, c)
disc = eq.getDiscriminante()
if disc > 0:
    r1 = round(eq.getRaiz1(), 5)
    r2 = round(eq.getRaiz2(), 5)
    print(f"La ecuación tiene dos raíces {r1} y {r2}")
elif disc == 0:
    r1 = int(eq.getRaiz1()) if eq.getRaiz1().is_integer() else eq.getRaiz1()
    print(f"La ecuacion tiene una raiz {r1}")
else:
    print("La ecuacion no tiene raices reales")