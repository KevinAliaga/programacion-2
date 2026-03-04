import time, random
class Cronometro:
    def __init__(self):
        self.inicia()
        self.__finaliza = 0.0        
    def get_inicia(self): 
        return self.__inicia
    def get_finaliza(self): 
        return self.__finaliza
    def inicia(self): 
        self.__inicia = time.time() * 1000
    def detener(self): 
        self.__finaliza = time.time() * 1000
    def lapsoDeTiempo(self): 
        return self.__finaliza - self.__inicia

def ordenar(lis):
    n = len(lis)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if lis[j] < lis[m]:
                m = j
        lis[i], lis[m] = lis[m], lis[i]

numero = []
for i in range(10000):
    num = random.randint(1, 1000)
    numero.append(num)
print("Ordenando 10,000 números (espera un momento)...")
crono = Cronometro()
crono.inicia()
ordenar(numero)
crono.detener()
print(f"Tiempo: {crono.lapsoDeTiempo():.2f} ms")