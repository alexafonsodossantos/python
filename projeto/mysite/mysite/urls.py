from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', include('loja.urls', namespace="loja")),
    path('profile/', include('loja.urls', namespace="profile")),
]