"""def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")"""

#O erro ocorre porque estamos tentando dividir dois números, mas se o segundo número for zero, isso causará um erro de "ZeroDivisionError".

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    except ValueError:
        return "Erro: Entrada inválida. Por favor, insira números válidos."
    
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")
