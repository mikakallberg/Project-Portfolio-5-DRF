""" Url path for active chats """
from django.urls import path
from message import views


urlpatterns = [
    path('message/', views.MessageList.as_view()),
    path('message/<int:pk>/', views.MessageDetail.as_view()),
]