from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



app_name = 'loja'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>/', views.detail, name='detail'),
    

    
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
