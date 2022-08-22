from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views



app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.categorias, name='categorias'),
    path('promocoes', views.promocoes, name='promocoes'),
    path('perfil', views.perfil, name='perfil'),
    path('cart/<int:cart_id>', views.cart, name='cart'),
    path('<int:produto_id>/', views.detail, name='detail'),

    

    
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
