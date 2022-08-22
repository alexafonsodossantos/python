from django.contrib import admin

# Register your models here.

from .models import Produto, Usuario, Cart

admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Cart)