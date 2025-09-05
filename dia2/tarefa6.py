class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f"Nome: {self.nome} | Idade: {self.idade}"

    def falar(self):
        pass


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Miiiiaaaaaaauuuuu 🐱"
    
    
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au au 🐶"


class Zoologico:
    def __init__(self):
        self.animais = []
        
    def adicionar_animal(self, animal):
        self.animais.append(animal)
        
    def listar_animais(self):
        for animal in self.animais:
            print(f"{animal.apresentar()} | Som: {animal.falar()}")
            
    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]
