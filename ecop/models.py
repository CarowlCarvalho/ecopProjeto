from django.db import models


class Enderecos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    rua = models.CharField('Rua', max_length=100)
    n = models.CharField('Nº', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)

    def __str__(self):
        return self.nome
