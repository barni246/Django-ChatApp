from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
   myChat = Chat.objects.get(id=1)
   if request.method == 'POST' and request.POST.get('textmessage', '') != '':
        print("Recived data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
   chatMessages = Message.objects.filter(chat__id=1)
   return render(request, 'chat/index.html', {'messages': chatMessages})

# def index(request):
#     if request.method == 'POST' and request.POST.get('textmessage', '') != '':
#         received_data = request.POST['textmessage']
#         print("Received data: " + received_data)
#     return render(request, 'chat/index.html', {'username': 'Barni'})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username') , password = request.POST.get('password') )
        if user:
            login(request,user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword' : True})
    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'), email = request.POST.get('email') , password = request.POST.get('password'))
        if user:
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'auth/register.html', {'invalidRegister': True})
    return render(request, 'auth/register.html')
