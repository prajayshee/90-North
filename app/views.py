from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Chat
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def chat_view(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude logged-in user from the list
    chats = Chat.objects.filter(sender=request.user) | Chat.objects.filter(receiver=request.user)
    return render(request, 'chat.html', {'users': users, 'chats': chats})