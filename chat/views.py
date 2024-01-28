from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers


"""Renders index.html, retrieves and saves chat messages if received via POST request."""
@login_required(login_url = '/login/')
def index(request):
   myChat = Chat.objects.get(id=1)
   if request.method == 'POST' and request.POST.get('textmessage', '') != '':
        print("Recived data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message =  Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [new_message,])
        return JsonResponse(serialized_obj[1:-1], safe=False)
   chatMessages = Message.objects.filter(chat__id=1)
   return render(request, 'chat/index.html', {'messages': chatMessages})


"""
- Redirects to the specified URL if the user is already logged in.
- Logs in the user if valid credentials are provided via POST request.
- Renders the login page with appropriate messages if login fails or no POST request is made.
"""
def login_view(request):
    redirect = request.GET.get('next')
    info = 'You are already logged in!'
    if request.user.is_authenticated:
        return render(request, 'auth/login.html', {'alreadyLoggedIn': True, 'info': info})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect or '/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


"""
- Creates a new user account with provided credentials if POST request is made and passwords match.
- Redirects to the login page upon successful registration.
- Renders the registration page with appropriate messages if registration fails or no POST request is made.
"""
def register_view(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        if new_password == confirm_password:
            user = User.objects.create_user(username=new_username, email=new_email, password=new_password,is_staff=True)
            if user:
                return HttpResponseRedirect('/login/',{'wrong_form':False})
        return render(request, 'auth/register.html', {'wrong_form':True})
    return render(request, 'auth/register.html')




