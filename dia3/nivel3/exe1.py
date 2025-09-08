# O erro  pode ocorrer porque estamos tentando acessar uma chave que não existe no dicionário 'dados'.
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar (nome, idade, cidade): ")

if dados.get(chave, "Endereço não encontrado"):
    raise KeyError("Chave não encontrada no dicionário.")

print(f"O valor da chave '{chave}' é: {{dados[chave]}}")