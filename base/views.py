from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with Me!'},
#     {'id':3, 'name':'Frontend Developers!'},
# ]

def home(request):
    rooms = Room.objects.all() #this gives us access to all of the rooms in the database
    
    topics = Topic.objects.all()
    
    context = {'rooms': rooms, 'topics':topics}
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




def updateRoom(request, pk): #the pk here tells us which item were updating
    room = Room.objects.get(id=pk) #this initializes the room we want to access by the pk
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #the instance value determines the room were updated
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


    

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home') #this will send the user back to home if theyve successfully deleted their room
    return render(request, 'base/delete.html', {'obj':room})