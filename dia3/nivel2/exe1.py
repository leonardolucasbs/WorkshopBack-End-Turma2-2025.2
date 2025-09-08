""" def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado) """


#O erro ocorre porque estamos tentando somar um inteiro (10) com uma string ("5"), o que não é permitido em Python.
def somar(a, b):
    try:
        return a + b
    except TypeError:
        return "Erro: Tipos incompatíveis para soma."

resultado = somar(10, "5")
print(resultado)