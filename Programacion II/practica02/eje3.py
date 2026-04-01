import math
class Vector3D:
    def __init__(self, x, y, z):
        self.c = [x, y, z]
    def __add__(self, b):              # a) Suma 
        res = []
        for i in range(3):
            res.append(self.c[i] + b.c[i])
        return Vector3D(res[0], res[1], res[2])
    def __rmul__(self, r):           # b) Multiplicación 
        res = []
        for coor in self.c:
            res.append(r * coor)
        return Vector3D(res[0], res[1], res[2])
    def __sub__(self, b):
        res = []
        for i in range(3):
            res.append(self.c[i] - b.c[i])
        return Vector3D(res[0], res[1], res[2])
    def norma(self):                  # c) Longitud o Norma
        suma_cuad = 0
        for coor in self.c:
            suma_cuad += coor**2
        return math.sqrt(suma_cuad)
    def __truediv__(self, r):             # d) Normal
        return (1.0 / r) * self
    def __mul__(self, b):                # e) Producto Escalar
        p_punto = 0
        for i in range(3):
            p_punto += self.c[i] * b.c[i]
        return p_punto
    def cruz(self, b):                   # f) Producto Vectorial
        v = self.c
        bv = b.c
        rx = v[1]*bv[2] - v[2]*bv[1]
        ry = v[2]*bv[0] - v[0]*bv[2]
        rz = v[0]*bv[1] - v[1]*bv[0]
        return Vector3D(rx, ry, rz)
    def __str__(self):
        return f"({self.c[0]}, {self.c[1]}, {self.c[2]})"
a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
r = 2
print(f"Vector a {a}")
print(f"Vector b {b}")
print(f"a)Suma {a + b}")
print(f"b)Escalar {r * a}")
print(f"c)Norma {a.norma():.4f}")
print(f"d)Normal de a {a / a.norma()}")
print(f"e)Prod.Escalar {a * b}")
print(f"f)Prod.Vectorial {a.cruz(b)}")