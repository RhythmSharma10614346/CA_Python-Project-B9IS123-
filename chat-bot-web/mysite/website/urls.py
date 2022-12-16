from django.urls import path

from . import views
from chatbot.smartchatbot import responses

urlpatterns = [
   path("", views.index,name='index'),
   path("about", views.about,name='about'),
   path("smartchatbot", views.smartchatbot,name='smartchatbot'),
   path("sendmessage",views.sendmessage, name="sendmessage"),
   path("aichatbot", views.aichatbot,name='aichatbot'),
 
]