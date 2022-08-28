from django.contrib import admin

# Register your models here.

from .models import Produto, User, Cart

admin.site.register(Produto)
admin.site.register(Cart)
