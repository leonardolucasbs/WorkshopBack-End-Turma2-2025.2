
class Zoologico:
    def __init__(self):
        self.animais = []

    class Animal():
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade  
        
        def falar(self):
            pass
        
    def adicionar_animal(self, animal):
        self.animais.append(animal)
        
    def listar_animais(self):
        for animal in self.animais:
            print(f"Nome: {animal.nome}, Idade: {animal.idade}, Som: {animal.falar()}")
            
    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]
    

        

