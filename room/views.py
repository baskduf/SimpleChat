from django.shortcuts import render
from django.shortcuts import redirect

def join_room(request):
    if request.user.is_authenticated:
        return render(request, 'room.html')
    else:
        return redirect('login')

def create_room(request):
    if request.user.is_authenticated:
        return render(request, 'create-room.html')
    else:
        return redirect('login')

def about(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')