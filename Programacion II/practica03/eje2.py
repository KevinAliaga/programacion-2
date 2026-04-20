import random
class Juego:
    def __init__(self, v):
        self.v_orig = v
        self.v = v
        self.rec = 0
    def reiniciaPartida(self):
        self.v = self.v_orig
        print(f"Nueva Partida vidas: {self.v}")
    def actualizaRecord(self):
        if self.v > self.rec:
            self.rec = self.v
            print(f"record {self.rec}")
    def quitaVida(self):
        self.v = self.v - 1
class JuegoAdivinaNumero(Juego):
    def __init__(self, v):
        super().__init__(v)
        self.num = 0
    def validaNumero(self, n):
        if 0 <= n <= 10:
            return True
        return False
    def juega(self):
        self.reiniciaPartida()
        self.num = random.randint(0, 10)
        print("adivina un número entre 0 y 10")
        while self.v > 0:
            intento = int(input("introduce número "))
            if self.validaNumero(intento):
                if intento == self.num:
                    print("correcto ")
                    self.actualizaRecord()
                    self.v = 0
                else:
                    self.quitaVida()
                    if self.v > 0:
                        if self.num > intento: 
                            print("es mayor ")
                        else: print("Es menor.")
                        print(f"vidas {self.v}")
                    else:
                        print(f"perdiste era {self.num}")
            else:
                print("numero no valido")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        print("numero debe ser par entre 0 y 10 ")
        return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 != 0:
            return True
        print("numero debe ser impar entre 0 y 10 ")
        return False

j1 = JuegoAdivinaNumero(3)
j1.juega()
j2 = JuegoAdivinaPar(3)
j2.juega()
j3 = JuegoAdivinaImpar(3)
j3.juega()