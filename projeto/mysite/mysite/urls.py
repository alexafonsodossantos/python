from django.contrib import admin
from django.urls import include, path

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', include('loja.urls', namespace="loja")),
    


]