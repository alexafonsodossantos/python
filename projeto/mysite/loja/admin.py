from django.contrib import admin

# Register your models here.

from .models import Produto, Usuario

admin.site.register(Produto)
admin.site.register(Usuario)