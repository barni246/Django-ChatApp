from django.shortcuts import render

# def index(request):
   # if request.method == 'POST' and input != '':
   #  print("Recived data: " + request.POST['textmessage'])
   # return render(request, 'chat/index.html', {'username': 'Barni'})

def index(request):
    if request.method == 'POST' and request.POST.get('textmessage', '') != '':
        received_data = request.POST['textmessage']
        print("Received data: " + received_data)
    return render(request, 'chat/index.html', {'username': 'Barni'})
