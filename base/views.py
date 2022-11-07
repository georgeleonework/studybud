from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with Me!'},
#     {'id':3, 'name':'Frontend Developers!'},
# ]

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #after we get the username and pass we need to verify that the user actually exists
        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        #were either verifying that username = username somewhere in the database or alrting the user that that username doesnt exist

    context = {}
    return render(request, 'base/login_register.html', context)



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' #this is an inline if check that ssets query parameter q

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | #checking the query here to make sure that q has EITHEr of these qualities
        Q(name__icontains=q) |
        Q(description__icontains=q)
    ) #in other words, does the topic, name, or description contain the value of the search?

    topics = Topic.objects.all()
    room_count = rooms.count()
    
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