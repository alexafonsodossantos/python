from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views



app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.categorias, name='categorias'),
    path('categorias_filter/<str:cat_id>/', views.categorias_filter, name='categorias_filter'),
    path('promocoes', views.promocoes, name='promocoes'),
    path('perfil', views.perfil, name='perfil'),
    path('cart/<str:username>', views.cart, name='cart'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('<int:produto_id>/', views.detail, name='detail'),
    path('update_cart', views.update_cart, name='updade_cart'),
    path('checkout/<str:username>', views.checkout, name='checkout'),

    

    

    
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
