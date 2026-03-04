import math
def calcular_promedio(datos):
    return sum(datos) / len(datos)
def calcular_desviacion(datos):
    prom = calcular_promedio(datos)
    n = len(datos)

    suma_cuadrados = sum((x - prom) ** 2 for x in datos)
    return math.sqrt(suma_cuadrados / (n - 1))

entrada = input("10 numeros: ")
numeros = [float(x) for x in entrada.split()]
print(f"El promedio es {round(calcular_promedio(numeros), 2)}")
print(f"La desviación estandar es {round(calcular_desviacion(numeros), 5)}")