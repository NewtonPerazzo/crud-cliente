from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
