from django.contrib import admin
from django.urls import path
from webapp.views import login_view, logout_view
from . import views
from django.contrib.auth.views import LogoutView
from .views import painel_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login e logout
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Site público
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('noticia/<int:pk>/', views.detalhe_noticia, name='detalhe_noticia'),
    path('oidurb/', views.o_idurb, name='oidurb'),
    path('legislacao/', views.legislacao, name='legislacao'),
    path('servicos/', views.servicos, name='servicos'),  # <-- página pública de serviços
    path('transparencia/', views.transparencia, name='transparencia'),
    path('mapa/', views.mapa, name='mapa'),

    # Painel administrativo
    path('painel/', painel_view, name='painel'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Notícias
    path('noticias/', views.noticias_listar, name='noticias_listar'),
    path('noticias/nova/', views.noticia_nova, name='noticia_nova'),

    # Admin/painel - separa com prefixo
    path('painel/servicos/', views.servicos_listar, name='servicos_listar'),  # <-- corrigido!
    path('painel/sistemas/', views.sistemas_listar, name='sistemas_listar'),
    path('painel/equipe/', views.equipe_listar, name='equipe_listar'),

    # Páginas institucionais
    path('organograma/', views.organograma, name='organograma'),
    path('relatorios/', views.relatorios_view, name='relatorios'),
    path('prestacao-contas/', views.prestacao_contas_view, name='prestacao_contas'),
    path('planejamento/', views.planejamento_view, name='planejamento'),
    path('plano-diretor/', views.plano_diretor_view, name='plano_diretor'),
    path('codigo-obras/', views.codigo_obras_view, name='codigo_obras'),
    path('uso-do-solo/', views.uso_solo_view, name='uso_solo'),


    path('painel/servicos/novo/', views.servico_novo, name='servico_novo'),

]
