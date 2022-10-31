from django.shortcuts import render

def home(request):
    
    return render(request,'chat/layout.html')

def single_chat(request,room):

    return render(request,'chat/chat.html',{'chat':room})