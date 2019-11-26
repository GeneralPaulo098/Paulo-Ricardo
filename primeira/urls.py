from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('produto/', views.produto_list),
    path('produto/show/<int:id>/', views.produto_show),
    path('produto/deleta/<int:id>/', views.produto_delete),
    path('produto/editar/<int:id>/',views.editar),
    path('produto/create/', views.create),
    path('produto/pesquisa/', views.pesquisa)
 

]