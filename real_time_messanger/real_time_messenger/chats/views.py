from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser, Message

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('members_list')
    return render(request, 'chats/login.html')

def members_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    members = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'chats/login_member_list.html', {'members': members})

def chat_view(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    other_user = CustomUser.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user],
    )
    return render(request, 'chats/message.html', {'other_user': other_user, 'messages': messages})
