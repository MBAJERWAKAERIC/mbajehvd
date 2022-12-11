from django import forms 
from django.shortcuts import render

task = ["foo", "bar", "baz"]

class NewTasksForm(forms.Form):
    tasks = forms.CharField(label="New Tasks")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    
# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "task": task
    })
    
def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            task.append(task)
        else:
            return render (request, "task/add.html", {
                "form": form
            })
    return render(request, "task/add.html", {
        "form": NewTasksForm()
    })