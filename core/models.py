from django.db import models


# Create your models here.
class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preco', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('quantidade')

    def __str__(self):
        return (f'{self.nome} com {self.estoque}')


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    idade = models.IntegerField('idade')
    email = models.EmailField('Email', max_length=200)

    def __str__(self):
        return (f'{self.nome} {self.sobrenome}')