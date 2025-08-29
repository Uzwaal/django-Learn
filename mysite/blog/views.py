
from django.shortcuts import render
from .models import Room

# Create your views here.

context=[
    {'id':1, 'name':'I dont know'},
    {'id':2, 'name':'I know'},
    {'id':3, 'name':'I dont know know'},
]

def home(request):
    rooms = Room.objects.all()
    return render(request,'blog/home.html', {'items':rooms})

def room(request):
    return render(request,'blog/room.html')

def furniture(request):
    return render(request,'furniture.html')

