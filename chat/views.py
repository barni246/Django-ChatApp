from django.shortcuts import render
from .models import Message, Chat

def index(request):
   myChat = Chat.objects.get(id=1)
   if request.method == 'POST':
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
    return render(request, 'auth/login.html')
