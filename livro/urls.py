from . import views
from django.urls import path

app_name = 'livro'

urlpatterns = [
    path('', views.index, name='index'),
    path('listac', views.ListaC.as_view(), name='listac'),
    path('lista',views.lista, name='lista' ),
    path('relatorio',views.relatorio, name='relatorio' ),
    path('<int:item_id>',views.detail, name='detail'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('html/', views.html, name='html'),
]
