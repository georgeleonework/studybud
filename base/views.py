from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with Me!'},
#     {'id':3, 'name':'Frontend Developers!'},
# ]

def home(request):
    rooms = Room.objects.all() #this gives us access to all of the rooms in the database
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk) #sets tge room to view as the instance where the id matches the key
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #this is the name value from our form which allows ur to reference easier
    context = {'form': form}
    return render(request, 'base/room_form.html', context)