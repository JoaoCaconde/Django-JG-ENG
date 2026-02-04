from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('sobreMim/', views.sobreMim, name='sobreMim'),
    path('contato/', views.contato, name='contato'),
    path('habilidades/', views.habilidades, name='habilidades'),
]