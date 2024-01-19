from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import get_object_or_404


@login_required(login_url = '/login/')
def index(request):
   myChat = Chat.objects.get(id=1)
   if request.method == 'POST' and request.POST.get('textmessage', '') != '':
        print("Recived data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message =  Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [new_message,])
        
       # nachrichten = Message.objects.all()
       # for nachricht in nachrichten:
       #  print(f"Nachricht ID: {nachricht.id}, Text: {nachricht.text}")
        # nachricht = get_object_or_404(Message, pk=227)
        # nachricht.delete()
        
        return JsonResponse(serialized_obj[1:-1], safe=False)
   chatMessages = Message.objects.filter(chat__id=1)
   return render(request, 'chat/index.html', {'messages': chatMessages})


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




# def login_view(request):
#     redirect = request.GET.get('next')
    
#     if request.user.is_authenticated:
#         return render(request, 'auth/login.html', {'alreadyLoggedIn': True})

    
#     if request.method == 'POST':
#         user = authenticate(username = request.POST.get('username') , password = request.POST.get('password') )
#         if user:
#             login(request,user)
#            # return HttpResponseRedirect('/chat/')
#             return HttpResponseRedirect(request.POST.get('redirect'))
#         else:
#             return render(request, 'auth/login.html', {'wrongPassword' : True, 'redirect': redirect})
#     return render(request, 'auth/login.html', {'redirect': redirect})


# def register_view(request):
#     if request.method == 'POST':
#         new_username = request.POST.get('username')
#         new_email = request.POST.get('email')
#         new_password = request.POST.get('password')
#         confirm_password = request.POST.get('password')
#         user = User.objects.create_user(username = new_username, email = new_email , password = new_password)
#         if new_password == confirm_password:
#             return HttpResponseRedirect('/login/')
#         else:
#             return render(request, 'auth/register.html')
#     return render(request, 'auth/register.html')


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




