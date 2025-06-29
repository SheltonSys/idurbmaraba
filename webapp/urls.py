from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('noticia/<int:pk>/', views.detalhe_noticia, name='detalhe_noticia'),
    
    # Página institucional
    path('oidurb/', views.o_idurb, name='oidurb'),


    # Páginas do menu
    path('legislacao/', views.legislacao, name='legislacao'),
    path('servicos/', views.servicos, name='servicos'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('mapa/', views.mapa, name='mapa'),
]
