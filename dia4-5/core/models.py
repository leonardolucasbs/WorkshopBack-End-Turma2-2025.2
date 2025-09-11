

from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"RUA: {self.rua}, BAIRRO: {self.bairro}, CIDADE: {self.cidade}, ESTADO: {self.estado}, CEP: {self.cep}"
