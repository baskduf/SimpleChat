from django.shortcuts import render
from django.shortcuts import redirect
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from django.contrib.auth.models import User

# myapp/views.py (추가된 부분)
from django.http import JsonResponse


@login_required
def kick_user(request, room_name, user_id):
    room = Room.objects.get(name=room_name)
    if request.user == room.owner:
        user_to_kick = User.objects.get(id=user_id)
        room.users.remove(user_to_kick)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': '권한이 없습니다.'})


@login_required
def create_room_process(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        room = Room.objects.create(name=room_name, owner=request.user)
        room.users.add(request.user)
        return redirect('room_detail_process', room_id=room.id)
    return render(request, 'create-room.html')


@login_required
def room_detail_process(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'room-detail.html', {'room': room})


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
