"""Título: Animais Simples

Enunciado:
Crie uma classe Animal com o método falar().
Crie as classes Gato e Cachorro, que herdam de Animal e sobrescrevem o método falar() para retornar:

"Miau!" para gatos

"Au au!" para cachorros

📌 Requisitos Técnicos:

Use herança simples.

Use polimorfismo para sobrescrever métodos."""


class Animal():
    def falar(self):
        pass

class gato(Animal):
    def falar(self):
        return"miiiiaaaaaaauuuuu"
    
class cachorro(Animal):
    def falar(self):
        return"auaauauauaua"

