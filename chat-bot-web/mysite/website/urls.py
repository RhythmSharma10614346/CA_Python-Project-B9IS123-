from django.urls import path
from mysite.website import views

urlpatterns = [
   path("", views.index,name='index'),
   path("about", views.about,name='about'),
   path("smartchatbot", views.smartchatbot,name='smartchatbot'),
   path("sendmessage",views.sendmessage, name="sendmessage"),
 
]