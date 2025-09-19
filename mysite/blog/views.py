
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

context=[
    {'id':1, 'name':'I dont know'},
    {'id':2, 'name':'I know'},
    {'id':3, 'name':'I dont know know'},
]


def loginPage(request):
    if request=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
         try:
             user= User.objects.get(username=username)
         except:
             messages.error(request,'User does not exist')

         user=authenticate(request, username=username, password=password)
         if user is not None:
             login(request,user)
             return redirect('home')
         else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')



    context={}
    return render (request,'registration.html', context)

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


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('/')
    return render(request,'blog/delete.html', {'obj':room})


from django.contrib import messages

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            print("Messages in view:", list(messages.get_messages(request)))

    return render(request, 'registration.html', {})

