from urllib import response

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
   return render(request, 'index.html', {})
 
def about(request):
   return render(request, 'about.html', {})
 
def smartchatbot(request):
   return render(request, 'smartchatbot.html', {})
 
def sendmessage(request):
   user_message=request.POST["mymessage"]
   print(user_message)
   return JsonResponse({"message":str(response.message)})

def aichatbot(request):
   return render(request, 'aichatbot.html', {})
