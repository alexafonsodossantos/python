from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.db import models

User=get_user_model()






    
class Categorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoria = models.CharField(max_length=50)
    cat_img  = models.ImageField("Category image", upload_to='loja/static/loja/images', null=True)
    
    def __str__(self):
        return str(self.categoria)

class Produto(models.Model):

    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    marca = models.CharField(max_length=140)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
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
    produtos_nome = models.CharField(max_length=255, null=True)
    qtd = models.IntegerField(default=1)
    prod_img = models.CharField(max_length=255)
    preço = models.FloatField()


    def __str__(self):
        return str(self.id)