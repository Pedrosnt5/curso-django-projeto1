from recipes import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'), # Home a rota '' (vazio) é a rota raiz do site, ou seja, http://127.0.0.1:8000/ (é a primeira rota a ser acessada quando o site é carregado)
    path('contato/', views.contato, name='contato'),    # /contato/
    path('sobre/', views.sobre, name='sobre')           # /sobre/
]