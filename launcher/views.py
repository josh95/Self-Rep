from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
clientID = "9f81a88b0163d675a0b0"
def index(request):
    context = {"clientID" : clientID}
    return render(request, "index.html", context)
