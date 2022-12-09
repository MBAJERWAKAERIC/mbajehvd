from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "html/index.html")
    
def index(request):
    return HttpResponse("MBAJE RWAKA ERIC")

def eric( request):
    return HttpResponse("Salut Eric")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")
    
