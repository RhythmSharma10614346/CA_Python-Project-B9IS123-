from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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
