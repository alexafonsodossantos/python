from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.db import models

User=get_user_model()


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
        return str(self.id)


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos_id = models.ForeignKey(Produto, on_delete = models.CASCADE)
    qtd = models.IntegerField(default=1)
    prod_img = models.CharField(max_length=255)
    preço = models.FloatField()


    def __str__(self):
        return str(self.id)
