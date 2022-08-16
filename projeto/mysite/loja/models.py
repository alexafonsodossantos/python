from django.db import models

# Create your models here.

from django.db import models


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    marca = models.CharField(max_length=140)
    qtd = models.IntegerField()
    preço = models.FloatField()

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    sobrenome = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    telefone = models.CharField(max_length=14)
    username = models.CharField(max_length=140)
    password = models.CharField(max_length=140)

    def __str__(self):
        return self.nome


