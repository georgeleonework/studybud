from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design with Me!'},
    {'id':3, 'name':'Frontend Developers!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    # this loop checks each of the rooms and finds a match for the user generated pk, and then sets it as the context below
    context = {'room': room}
    return render(request, 'base/room.html', context)
