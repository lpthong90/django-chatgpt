from django.urls import path
from .. import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='list'),
    path('<int:chat_id>/', views.detail, name='detail'),
    path('<int:chat_id>/messages/', views.message_index, name='message_index'),
]