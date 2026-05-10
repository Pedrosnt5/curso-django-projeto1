"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# COMENTÁRIOS SOBRE AS ROTAS (URLS) DO PROJETO NO FINAL DO ARQUIVO!

urlpatterns = [
    # esses comandos esperam uma ROTA e uma FUNÇÃO (VIEW) para serem executados
    # path('rota/', view_funcionalidade)    #http://127.0.0.1:8000/rota/
    path('admin/', admin.site.urls),    #http://127.0.0.1:8000/admin/
    path('home/')                       #http://127.0.0.1:8000/home/
]



# aqui é onde ficam as rotas do projeto, ou seja, os caminhos para acessar as funcionalidades do sistema
# cada rota é associada a uma função (view) que é responsável por processar a requisição (HTTP REQUEST) e retornar uma resposta (HTTP RESPONSE)
# as rotas são definidas usando a função path() que recebe dois argumentos: a rota (string) e a função (view) que será executada quando a rota for acessada
# as rotas podem conter parâmetros, por exemplo: path('produto/<int:id>/', view_produto) onde <int:id> é um parâmetro que será passado para a função view_produto
# as rotas podem ser organizadas em arquivos separados usando a função include(), por exemplo: path('blog/', include('blog.urls')) onde as rotas do blog ficam em um arquivo separado chamado blog/urls.py
# as rotas podem ser protegidas usando decoradores, por exemplo: @login_required para exigir que o usuário esteja logado para acessar a rota
# as rotas podem ser nomeadas usando o argumento name, por exemplo: path('home/', view_home, name='home') para facilitar a referência às rotas em outras partes do código, como templates ou redirecionamentos
# as rotas são processadas na ordem em que são definidas, ou seja, a primeira rota que corresponder à requisição será executada, por isso é importante organizar as rotas de forma lógica e evitar rotas conflitantes
