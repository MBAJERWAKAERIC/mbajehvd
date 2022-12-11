from django.shortcuts import render

task = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "task": task
    })
    
def add(request):
    return render(request, "task/add.html")  