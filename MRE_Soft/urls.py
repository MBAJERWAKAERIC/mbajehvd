from django.urls import path 
from . import  views

urlpatterns = [

    path("", views.index, name="index"),
   
    path("eric", views.eric, name="eric")
]
