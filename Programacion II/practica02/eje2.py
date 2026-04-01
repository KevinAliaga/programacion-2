import math
class AlgebraVectorial:
    def __init__(self, x, y, z):
        self.v = [x, y, z]
    def perp(self, b):
        p = 0
        for i in range(3):
            p += self.v[i] * b.v[i]
        return math.isclose(p, 0, abs_tol=1e-9)
    def para(self, b):
        cx = self.v[1] * b.v[2] - self.v[2] * b.v[1]
        cy = self.v[2] * b.v[0] - self.v[0] * b.v[2]
        cz = self.v[0] * b.v[1] - self.v[1] * b.v[0]
        m = math.sqrt(cx**2 + cy**2 + cz**2)
        return math.isclose(m, 0, abs_tol=1e-9)
    def proy(self, b):
        p = 0
        for i in range(3):
            p += self.v[i] * b.v[i]
        nb2 = 0
        for c in b.v:
            nb2 += c**2
        e = p / nb2
        return [e * b.v[0], e * b.v[1], e * b.v[2]]
    def comp(self, b):
        p = 0
        for i in range(3):
            p += self.v[i] * b.v[i]
        nb = math.sqrt(b.v[0]**2 + b.v[1]**2 + b.v[2]**2)
        return p / nb
v1 = AlgebraVectorial(1, 0, 0)
v2 = AlgebraVectorial(0, 1, 0)
v3 = AlgebraVectorial(2, 2, 2)
print("Perp:", v1.perp(v2))
print("Para:", v1.para(v3))
print("Proy:", v3.proy(v1))
print("Comp:", v3.comp(v1))