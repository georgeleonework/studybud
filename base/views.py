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
    return render(request, 'base/room.html')
