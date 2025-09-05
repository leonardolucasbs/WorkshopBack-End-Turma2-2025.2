
import math

def formatacoes(n1):
    paraCima = math.floor(n1)
    teto = math.ceil(n1)
    arredondado = round(n1)

    return (f"Seu valor arredondado para baixo: {paraCima} , Seu valor arredondado para cima: {teto} , Seu valor arredondado para o inteiro mais próximo: {arredondado}")

n1 = float(input("digite um número: "))
print(formatacoes(n1))




