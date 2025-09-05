

class Animal():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar():
        return (f"nome: {self.nome} | idade: { self.idade}")


    def falar(self):
        pass

class gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


    def falar(self):
        return"miiiiaaaaaaauuuuu🐱 "
    
    
class cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return"auaauauauaua🐶"
    

