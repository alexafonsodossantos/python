from django.contrib import admin
# Register your models here.
from .models import Produto, Cart, Categorias
admin.site.register(Produto)
admin.site.register(Cart)
admin.site.register(Categorias)
