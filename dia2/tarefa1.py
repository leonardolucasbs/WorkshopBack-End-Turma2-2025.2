import math


n1 = int(input("digite um numero: "))


def raizquadrada(n1):
    raiz = math.sqrt(n1)
    return (f"a raiz de {n1} é {raiz}")

print(raizquadrada(n1))