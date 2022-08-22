from tkinter import CASCADE
from django.db import models

# Create your models here.

from django.db import models


class Produto(models.Model):
    CATEGORIAS = (
        ('1', 'Processadores'),
        ('2', 'RAM'),
        ('3', 'Placas-Mãe'),
        ('4', 'Air Cooler'),
        ('5', 'Water Cooler'),
        ('6', 'Periféricos'),
    )
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    marca = models.CharField(max_length=140)
    categoria = models.CharField(max_length=140, choices = CATEGORIAS)
    qtd = models.IntegerField()
    preço = models.FloatField()
    prod_img = models.ImageField("Product Image", upload_to='loja/static/loja/images', null=True)
    descricao = models.TextField()

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

class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    produtos_id = models.ForeignKey(Produto, on_delete = models.CASCADE)
    qtd = models.IntegerField()

    def __str__(self):
        return str(self.id)
