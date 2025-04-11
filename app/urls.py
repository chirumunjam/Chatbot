from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('chat/', views.chat, name='chat'),
    path('history/', views.chat_history, name='history'),
]