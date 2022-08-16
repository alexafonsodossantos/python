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



