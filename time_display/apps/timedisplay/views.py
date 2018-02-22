from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%b %d,%Y", gmtime()),
  'clock': strftime('%H:%M %p', gmtime())
  }
  return render(request,'timedisplay/index.html', context)
