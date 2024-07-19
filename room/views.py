from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'room.html')
    else:
        return render(request, 'login.html')