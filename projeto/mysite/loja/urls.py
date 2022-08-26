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
    path('cart/<str:username>', views.cart, name='cart'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('<int:produto_id>/', views.detail, name='detail'),
    path('checkout/<str:username>/', views.checkout, name='checkout'),
    path('submit_payment/<str:payment_id>', views.payment_details, name='submit_payment'),
    

    

    
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
