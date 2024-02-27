from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:chat_id>/', views.detail, name='chat_detail'),
    path('<int:chat_id>/messages/', views.message_index, name='message_index'),
]