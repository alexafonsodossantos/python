from django.urls import path

from . import views



app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>/', views.detail, name='detail'),
    
]

