
#o erro ocorre porque a função 'validar_idade' não possui dois pontos (:) no final da definição, o que é obrigatório em Python.
#Além disso, a função não está sendo chamada corretamente, e a mensagem de erro personalizada não está sendo exibida.

"""
def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))"""

def validar_idade(idade: int) -> bool:

    if idade < 0 or idade > 120:
        print("A idade deve estar entre 0 e 120 anos!")
        return False
    return True


while True:
    idade = int(input("Digite sua idade: "))
    if validar_idade(idade):
        print(f"Idade válida: {idade}")
        break


