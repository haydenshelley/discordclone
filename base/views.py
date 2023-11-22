from django.shortcuts import render

rooms = [
  {'id': 1, 'name':'Python'},
  {'id': 2, 'name':'Ruby'},
  {'id': 3, 'name':'Javascript'},
]

def home(request):
  return render(request, 'base/home.html', {'rooms':rooms})

def room(request):
  return render(request, 'base/room.html')