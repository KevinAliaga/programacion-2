import random
class Juego:
    def __init__(self, v):
        self.v_orig = v
        self.v = v
        self.rec = 0
    def reiniciaPartida(self):
        self.v = self.v_orig
        print(f"Vidas: {self.v} ")
    def actualizaRecord(self):
        if self.v > self.rec:
            self.rec = self.v
            print(f"récord {self.rec}")
        else:
            print(f"Récord actual: {self.rec}")
    def quitaVida(self):
        self.v = self.v - 1

class JuegoAdivinaNumero(Juego):
    def __init__(self, v):
        super().__init__(v)
        self.num = 0
    def juega(self):
        self.reiniciaPartida()
        self.num = random.randint(0, 10)
        print("Adivina un número entre el 0 a 10")
        while self.v > 0:
            intento = int(input("introduce tu numero "))
            if intento == self.num:
                print("acertaste")
                self.actualizaRecord()
                self.v = 0
            else:
                self.quitaVida()
                if self.v > 0:
                    if self.num > intento:
                        print("es mayor.")
                    else:
                        print("es menor.")
                    print(f"tienes  {self.v} vidas")
                else:
                    print(f"Perdiste el numero era {self.num}")

partida = JuegoAdivinaNumero(3)
partida.juega()