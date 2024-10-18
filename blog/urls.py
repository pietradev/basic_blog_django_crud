from django.urls import path
from . import views  # Importando as views do app 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Define a URL da página inicial (lista de posts)
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Define a URL para detalhes de um post
    path('post/new/', views.post_new, name='post_new'),  # Define a URL para criar um novo post
]
