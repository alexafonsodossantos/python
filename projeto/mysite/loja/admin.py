from django.contrib import admin

# Register your models here.

from .models import Produto, User, Cart, Payment

admin.site.register(Produto)
admin.site.register(Payment)
admin.site.register(Cart)
