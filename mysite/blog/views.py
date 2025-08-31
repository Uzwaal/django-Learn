
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

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


def createRoom(request):
    form = RoomForm()  # create a new empty form
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect after saving

    context = {'form': form}
    return render(request, 'blog/room_form.html', context)



def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'blog/room_form.html', context)

