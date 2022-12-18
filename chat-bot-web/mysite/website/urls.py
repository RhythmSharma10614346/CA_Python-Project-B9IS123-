from django.urls import path

from . import views


urlpatterns = [
   path("", views.index,name='index'),
   path("about", views.about,name='about'),
   path("smartchatbot", views.smartchatbot,name='smartchatbot'),
   path("sendmessage",views.sendmessage, name="sendmessage"),
   path("aichatbot", views.aichatbot,name='aichatbot'),
   path("chatty", views.chatty,name='chatty'),
]