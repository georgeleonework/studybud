from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with Me!'},
#     {'id':3, 'name':'Frontend Developers!'},
# ]

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #after we get the username and pass we need to verify that the user actually exists
        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        #were either verifying that username = username somewhere in the database or alrting the user that that username doesnt exist

        user = authenticate(request, username=username, password=password)

#in the following check were going to log the user in if there is a match for both username and password.
        if user is not None:
            login(request, user)
            return redirect('home') #once the user is logged in we want to redirect them to the home page
        else:
            messages.error(request, 'Username OR Password is does not exist')
    
    context = {'page':page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request) #this will delete that token session 
    return redirect('home')

def registerPage(request):
    page = 'register'
    return render(request, 'base/login_register.html')

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


 #all we need to do is add this decorator to restrict certain functionality to a login status
#the login url parameter above is where we redirect users in the case that theyre not logged in
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #this is the name value from our form which allows ur to reference easier
    context = {'form': form}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='login')
def updateRoom(request, pk): #the pk here tells us which item were updating
    room = Room.objects.get(id=pk) #this initializes the room we want to access by the pk
    form = RoomForm(instance=room)

    if request.user != room.host: #this requires that only the person who created or was assigned hosting privileges can do things
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) #the instance value determines the room were updated
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here ')   
        
    if request.method == 'POST':
        room.delete()
        return redirect('home') #this will send the user back to home if theyve successfully deleted their room
    return render(request, 'base/delete.html', {'obj':room})