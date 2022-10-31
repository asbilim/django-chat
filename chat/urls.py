from django.urls import path
from .views import home,single_chat
urlpatterns = [
    path('',home,name="chat-home"),
    path('room/<str:room>/',single_chat,name="single-chat")
]
