"""numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])"""

#O erro ocorre porque o usuário pode digitar um índice que está fora do intervalo da lista, o que causará um erro de "IndexError".
numeros = [10, 20, 30]  
indice = int(input("Digite um índice para acessar a lista: "))

try:
    print(numeros[indice])
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
